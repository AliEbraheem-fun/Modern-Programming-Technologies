"""Parse quiz1..quiz6 markdown files and produce a unified JSON pool of questions.

Filters out questions whose body mentions specific Java versions or release dates.
Run from project root: python exam/build_pool.py
"""
from __future__ import annotations
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent / "pool.json"

QUIZ_FILES = [
    "quiz1.md",
    "quiz2-1.md",
    "quiz2-2.md",
    "quiz3.md",
    "quiz4.md",
    "quiz5.md",
    # quiz6.md DROPPED — Maven/JDBC/Hibernate are frameworks, not Java basics.
]

# A question is excluded if its full text (question + options) matches ANY of these.
EXCLUDE_PATTERNS = [
    # --- Versions and dates ---
    re.compile(r"\bJava\s*\d+\b", re.IGNORECASE),
    re.compile(r"\b(JDK|JRE|JVM)\s*\d+\b", re.IGNORECASE),
    re.compile(r"когда\s+(был|была|были)\s+(выпущ|релиз|представл)", re.IGNORECASE),
    re.compile(r"\bв\s+каком\s+году\b", re.IGNORECASE),
    re.compile(r"\bв\s+какой\s+версии\b", re.IGNORECASE),
    re.compile(r"\b(год|года|году)\s+(выхода|релиза)\b", re.IGNORECASE),
    re.compile(r"\bLTS-?версия\b", re.IGNORECASE),
    re.compile(r"\bтекущ(ая|ей|их)\s+LTS\b", re.IGNORECASE),
    re.compile(r"\bкакая\s+версия\b", re.IGNORECASE),
    re.compile(r"\b(stable|релиз|выпуск)\s+\d{4}\b", re.IGNORECASE),
    re.compile(r"\b20[12]\d\b"),  # raw years 2010-2029 in question body

    # --- Frameworks / libraries (out of Java basics scope) ---
    re.compile(r"\b(Maven|Gradle|Hibernate|JDBC|JPA|Spring|Thymeleaf|Tomcat|Jetty|JWT|BCrypt|MapStruct|Lombok|HikariCP)\b"),
    re.compile(r"\bpom\.xml\b|\bbuild\.gradle\b", re.IGNORECASE),
    re.compile(r"\b(DAO|ORM)\b"),
    re.compile(r"\b(SELECT|INSERT|UPDATE|DELETE|CREATE\s+TABLE|DROP\s+TABLE|FROM\s+\w|WHERE\s+\w|JOIN)\b"),
    re.compile(r"\bSQL[- ]?(инъекци|инжекци)", re.IGNORECASE),
    re.compile(r"\b@(Entity|Table|Column|Id|GeneratedValue|OneToMany|ManyToOne|Service|Repository|Controller|RestController|Autowired|Bean|Configuration|SpringBootApplication|Transactional|Valid|RestControllerAdvice|ExceptionHandler|RequestMapping|GetMapping|PostMapping|PutMapping|DeleteMapping|PathVariable|RequestBody|RequestParam|PreAuthorize|EnableMethodSecurity|MockitoBean|WebMvcTest)\b"),

    # --- JPMS / modules (advanced, not basics) ---
    re.compile(r"\bmodule-info\b", re.IGNORECASE),
    re.compile(r"\bJPMS\b", re.IGNORECASE),
    re.compile(r"\bпакет[а-я]*\s+(exports|requires|opens|provides|uses)\b", re.IGNORECASE),
    re.compile(r"\bдиректив[а-я]*\s+(exports|requires|opens|provides|uses)\b", re.IGNORECASE),
    re.compile(r"директива\s+(exports|requires|opens|provides|uses)\b", re.IGNORECASE),
    re.compile(r"\bmodul(е|я|и|ей)?\b", re.IGNORECASE),  # модульная система, модуль и т.п.

    # --- Specific String API beyond .length() ---
    re.compile(r"\bString\s*\.\s*(join|format|valueOf|copyValueOf|chars|codePoints|matches|repeat|strip|stripLeading|stripTrailing|intern|getBytes)\b"),
    re.compile(r'"[^"]*"\s*\.\s*(indexOf|lastIndexOf|substring|replaceAll|matches|split|charAt|chars|codePoints|repeat|trim|strip|isBlank|toUpperCase|toLowerCase|contains|startsWith|endsWith|concat|join|format|hashCode|intern|getBytes|toCharArray)\s*\('),

    # --- Specific Collection / Stream / Optional / Files / Math API method calls ---
    re.compile(r"\b(Collections|Arrays|Stream|Collectors|Optional|Files|Paths|Path|IntStream|LongStream|DoubleStream|Math|Objects|Comparator)\s*\.\s*\w+\s*\("),
    re.compile(r"\b(ArrayList|LinkedList|HashMap|HashSet|TreeMap|TreeSet|LinkedHashMap|LinkedHashSet|PriorityQueue|Deque|ArrayDeque|Vector|Stack|Hashtable|EnumSet|EnumMap)\s*\.\s*\w+\s*\("),
    re.compile(r"\bкакой\s+метод\s+(Stream\s*API|Collections|Comparator|Optional|Files|NIO|BufferedReader|Iterator)\b", re.IGNORECASE),
    re.compile(r"\bкакой\s+принцип\s+именования\b", re.IGNORECASE),

    # --- Concurrency API specifics (keep concepts like synchronized, wait/notify; drop class-name memorization) ---
    re.compile(r"\b(ExecutorService|ThreadPoolExecutor|CountDownLatch|CyclicBarrier|Semaphore|ReentrantLock|AtomicInteger|AtomicLong|AtomicReference|ConcurrentHashMap|CompletableFuture|FutureTask|ForkJoinPool|ThreadLocal|ScheduledExecutorService)\b"),
    re.compile(r"\bpackage\s+java\.util\.concurrent\b", re.IGNORECASE),
    re.compile(r"\bjava\.util\.concurrent\b", re.IGNORECASE),

    # --- Specific I/O classes (concept-level OK, but memorising class hierarchy = drop) ---
    re.compile(r"\b(BufferedReader|BufferedWriter|FileReader|FileWriter|FileInputStream|FileOutputStream|ObjectInputStream|ObjectOutputStream|PrintWriter|InputStreamReader|OutputStreamWriter|DataInputStream|DataOutputStream|RandomAccessFile)\b"),
    re.compile(r"\bScanner\b"),  # specific class usage

    # --- NIO.2 specific paths ---
    re.compile(r"\bNIO(\.2|\s+\.2)?\b"),

    # --- Classloader API specifics (the conceptual variant is gated by QUESTION_ONLY list below) ---
    re.compile(r"\bClassLoader\s*\.\s*\w+", re.IGNORECASE),

    # --- JNI / native / JVM-internals trivia (out of basics) ---
    re.compile(r"\bJNI\b"),
    re.compile(r"\bsystem\s*\.\s*load(Library)?\s*\(", re.IGNORECASE),
    re.compile(r"\bнативн(ый|ого|ому|ом|ые)\s+метод", re.IGNORECASE),
    re.compile(r"\bVerification\b", re.IGNORECASE),
    re.compile(r"\bэтап\w*\s+(Loading|Linking|Initialization|Verification|Preparation|Resolution)\b", re.IGNORECASE),
    re.compile(r"\bкакие\s+три\s+этапа\s+проходит\s+класс\b", re.IGNORECASE),

    # --- jshell command trivia ---
    re.compile(r"\bjshell\b", re.IGNORECASE),

    # --- Classloader concept questions (too obscure for "easy to remember basics") ---
    re.compile(r"\bзагрузчик\w*\s+класс", re.IGNORECASE),
    re.compile(r"\bкакой\s+принцип\s+использу\w*\s+загрузчик", re.IGNORECASE),

    # --- JPMS specifics that slip through ---
    re.compile(r"\bopen\s+module\b", re.IGNORECASE),
    re.compile(r"\bexports\s+[\w.]+\s+to\s+[\w.]+", re.IGNORECASE),
    re.compile(r"@ParametersAreNonnullByDefault"),
    re.compile(r"\bpackage-info\.java\b", re.IGNORECASE),

    # --- Annotation internals trivia ---
    re.compile(r"\bRetentionPolicy\b"),

    # --- Functional-interface method-name memorization (Consumer.accept, Supplier.get etc.) ---
    re.compile(r"\bкакой\s+метод\s+(Consumer|Supplier|Function|Predicate|BiConsumer|BiFunction|BiPredicate|UnaryOperator|BinaryOperator)", re.IGNORECASE),

    # --- Other API memorization patterns ---
    # NOTE: we intentionally do NOT use a broad "какой метод" filter — too many
    # fundamental questions (main(), equals()) would be lost. The specific
    # framework/class filters above are enough.
    re.compile(r"\bкакой\s+интерфейс\s+(нужно|должен)\s+реализовать\b", re.IGNORECASE),
    re.compile(r"\bкакое\s+утверждение\s+верно\s+о\s+потокобезопасности\b", re.IGNORECASE),
    re.compile(r"\bкакая\s+структура\s+данных\s+лежит\s+в\s+основе\b", re.IGNORECASE),
]

# Patterns that should ONLY match if found in the question text (not in options/code).
# Reason: terms like "Metaspace" or "Bootstrap ClassLoader" often appear as distractors
# in options of conceptual questions ("где хранятся объекты в JVM?") — those should be kept.
QUESTION_ONLY_EXCLUDE_PATTERNS = [
    re.compile(r"\bMetaspace\b", re.IGNORECASE),
    re.compile(r"\b(Bootstrap|Platform|Application)\s+ClassLoader\b", re.IGNORECASE),
    re.compile(r"\.class\.getClassLoader\(\)"),
    re.compile(r"\bClassLoad\w*\s+иерархи", re.IGNORECASE),
    re.compile(r"\bReflection\b", re.IGNORECASE),
]

# Match each question block.
# The structure is:
# <div class="quiz-question" data-correct="N">
# <h4>Текст вопроса</h4>
# ...code blocks and other content...
# <div class="quiz-option" data-index="0">текст</div>
# <div class="quiz-option" data-index="1">текст</div>
# ...
# <div class="quiz-feedback"></div>
# </div>

QUESTION_RE = re.compile(
    r'<div class="quiz-question"\s+data-correct="(?P<correct>\d+)">\s*'
    r'(?P<body>.+?)'
    r'<div class="quiz-feedback">',
    re.DOTALL,
)

H4_RE = re.compile(r'<h4>(?P<text>.+?)</h4>', re.DOTALL)
OPTION_RE = re.compile(
    r'<div class="quiz-option"\s+data-index="(?P<idx>\d+)">(?P<text>.+?)</div>',
    re.DOTALL,
)
JSHELL_HINT_RE = re.compile(r'<span class="jshell-hint">.*?</span>', re.DOTALL)
TAG_RE = re.compile(r'<[^>]+>')
QUESTION_PREFIX_RE = re.compile(r'^Вопрос\s+\d+\.\s*', re.IGNORECASE)


def clean_text(s: str) -> str:
    s = JSHELL_HINT_RE.sub('', s)
    s = TAG_RE.sub('', s)
    s = s.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
    s = s.replace('&laquo;', '«').replace('&raquo;', '»').replace('&nbsp;', ' ')
    return s.strip()


def strip_question_prefix(s: str) -> str:
    return QUESTION_PREFIX_RE.sub('', s, count=1).strip()


def extract_code_blocks(body: str) -> str:
    """Extract fenced code blocks from question body (they sit between h4 and first option)."""
    # Pull text between </h4> and first <div class="quiz-option"
    m = re.search(r'</h4>(?P<between>.+?)<div class="quiz-option"', body, re.DOTALL)
    if not m:
        return ''
    between = m.group('between').strip()
    # Keep fenced code blocks verbatim
    code_blocks = re.findall(r'```\w*\n.*?\n```', between, re.DOTALL)
    return '\n\n'.join(cb.strip() for cb in code_blocks)


def parse_quiz(path: Path) -> list[dict]:
    text = path.read_text(encoding='utf-8')
    questions = []
    for m in QUESTION_RE.finditer(text):
        correct = int(m.group('correct'))
        body = m.group('body')

        h4 = H4_RE.search(body)
        if not h4:
            continue
        question_text = strip_question_prefix(clean_text(h4.group('text')))

        code = extract_code_blocks(body)

        options = []
        for om in OPTION_RE.finditer(body):
            options.append({
                'idx': int(om.group('idx')),
                'text': clean_text(om.group('text')),
            })
        options.sort(key=lambda x: x['idx'])
        option_texts = [o['text'] for o in options]

        if len(option_texts) < 2 or correct >= len(option_texts):
            continue

        questions.append({
            'source': path.name,
            'question': question_text,
            'code': code,
            'options': option_texts,
            'correct': correct,
        })
    return questions


def is_excluded(q: dict) -> tuple[bool, str]:
    haystack = q['question'] + '\n' + q['code'] + '\n' + '\n'.join(q['options'])
    for pat in EXCLUDE_PATTERNS:
        m = pat.search(haystack)
        if m:
            return True, f"matched /{pat.pattern}/ -> {m.group(0)!r}"
    # Question-only patterns: ignore mentions in code/options (used as distractors).
    for pat in QUESTION_ONLY_EXCLUDE_PATTERNS:
        m = pat.search(q['question'])
        if m:
            return True, f"(question only) matched /{pat.pattern}/ -> {m.group(0)!r}"
    return False, ''


def main() -> int:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    pool: list[dict] = []
    skipped: list[tuple[str, str, str]] = []  # (source, question, reason)
    per_source_kept: dict[str, int] = {}
    per_source_skipped: dict[str, int] = {}

    for name in QUIZ_FILES:
        path = ROOT / name
        if not path.exists():
            print(f"[warn] missing {name}", file=sys.stderr)
            continue
        qs = parse_quiz(path)
        for q in qs:
            excluded, reason = is_excluded(q)
            if excluded:
                skipped.append((name, q['question'][:80], reason))
                per_source_skipped[name] = per_source_skipped.get(name, 0) + 1
            else:
                pool.append(q)
                per_source_kept[name] = per_source_kept.get(name, 0) + 1

    # Strip the 'source' field before writing
    out_pool = [
        {
            'q': item['question'],
            'code': item['code'],
            'options': item['options'],
            'correct': item['correct'],
        }
        for item in pool
    ]
    OUT.write_text(json.dumps(out_pool, ensure_ascii=False, indent=2), encoding='utf-8')

    print(f"Wrote {len(out_pool)} questions to {OUT}")
    print("\nPer-source counts:")
    for name in QUIZ_FILES:
        kept = per_source_kept.get(name, 0)
        skip = per_source_skipped.get(name, 0)
        print(f"  {name}: kept {kept}, skipped {skip}")

    if skipped:
        print(f"\nSkipped {len(skipped)} questions (first 20):")
        for src, q, reason in skipped[:20]:
            print(f"  [{src}] {reason}")
            print(f"    {q!r}")

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
