# Тест 5: Коллекции, I/O и Многопоточность (Лекция 5)

<style>
.quiz-container {
  max-width: 800px;
  margin: 0 auto;
}
.quiz-question {
  background: #f8f9fa;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 20px;
}
.quiz-question h4 {
  margin-top: 0;
  color: #333;
}
.quiz-option {
  display: block;
  padding: 10px 15px;
  margin: 8px 0;
  background: #fff;
  border: 2px solid #ddd;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s;
}
.quiz-option:hover {
  border-color: #3F51B5;
  background: #f0f2ff;
}
.quiz-option.selected {
  border-color: #3F51B5;
  background: #e8eaf6;
}
.quiz-option.correct {
  border-color: #4caf50;
  background: #e8f5e9;
}
.quiz-option.wrong {
  border-color: #f44336;
  background: #ffebee;
}
.quiz-option.disabled {
  pointer-events: none;
}
.quiz-feedback {
  margin-top: 10px;
  padding: 10px 15px;
  border-radius: 6px;
  display: none;
  font-weight: 500;
}
.quiz-feedback.correct {
  display: block;
  background: #e8f5e9;
  color: #2e7d32;
}
.quiz-feedback.wrong {
  display: block;
  background: #ffebee;
  color: #c62828;
}
.quiz-score {
  text-align: center;
  padding: 20px;
  background: #e8eaf6;
  border-radius: 8px;
  margin-top: 30px;
  display: none;
}
.quiz-score h3 {
  margin-top: 0;
  color: #3F51B5;
}
.quiz-btn {
  display: block;
  margin: 30px auto 0;
  padding: 12px 40px;
  background: #3F51B5;
  color: #fff;
  border: none;
  border-radius: 6px;
  font-size: 16px;
  cursor: pointer;
}
.quiz-btn:hover {
  background: #303f9f;
}
.jshell-hint {
  display: inline-block;
  background: #fff3e0;
  color: #e65100;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 0.85em;
  margin-left: 8px;
}
</style>

<div class="quiz-container" id="quiz">

<!-- ===== РАЗДЕЛ 1: COLLECTIONS FRAMEWORK (Вопросы 1–15) ===== -->

<div class="quiz-question" data-correct="2">
<h4>Вопрос 1. Какой интерфейс является корнем иерархии коллекций в Java (JCF)?</h4>

<div class="quiz-option" data-index="0">Collection</div>
<div class="quiz-option" data-index="1">List</div>
<div class="quiz-option" data-index="2">Iterable</div>
<div class="quiz-option" data-index="3">Map</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 2. Какое утверждение верно об интерфейсе Map в иерархии JCF?</h4>

<div class="quiz-option" data-index="0">Map наследует интерфейс Collection</div>
<div class="quiz-option" data-index="1">Map наследует интерфейс Iterable</div>
<div class="quiz-option" data-index="2">Map является подтипом интерфейса Set</div>
<div class="quiz-option" data-index="3">Map НЕ наследует Collection — это отдельная ветвь иерархии</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 3. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
List<String> list = new ArrayList<>();
list.add("A");
list.add("B");
list.add("A");
System.out.println(list.size() + " " + list.get(2));
```

<div class="quiz-option" data-index="0">2 B</div>
<div class="quiz-option" data-index="1">3 A</div>
<div class="quiz-option" data-index="2">2 A</div>
<div class="quiz-option" data-index="3">Ошибка: дубликат не добавится</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 4. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
Set<String> set = new HashSet<>();
set.add("Java");
set.add("Python");
set.add("Java");
System.out.println(set.size());
```

<div class="quiz-option" data-index="0">3</div>
<div class="quiz-option" data-index="1">1</div>
<div class="quiz-option" data-index="2">Ошибка: дубликат вызовет исключение</div>
<div class="quiz-option" data-index="3">2</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 5. Какая реализация Set сохраняет порядок вставки элементов?</h4>

<div class="quiz-option" data-index="0">HashSet</div>
<div class="quiz-option" data-index="1">LinkedHashSet</div>
<div class="quiz-option" data-index="2">TreeSet</div>
<div class="quiz-option" data-index="3">EnumSet</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 6. Какая реализация Map хранит записи отсортированными по ключам?</h4>

<div class="quiz-option" data-index="0">HashMap</div>
<div class="quiz-option" data-index="1">LinkedHashMap</div>
<div class="quiz-option" data-index="2">Hashtable</div>
<div class="quiz-option" data-index="3">TreeMap</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 7. Какой принцип именования используется для классов коллекций в JCF?</h4>

<div class="quiz-option" data-index="0">Interface + Implementation (например, ListArray, SetHash)</div>
<div class="quiz-option" data-index="1">Implementation + Interface (например, ArrayList, HashSet, TreeMap)</div>
<div class="quiz-option" data-index="2">Abstract + Interface (например, AbstractList, AbstractSet)</div>
<div class="quiz-option" data-index="3">Произвольные имена без единой конвенции</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 8. Какой интерфейс нужно реализовать для сортировки объектов «по умолчанию» с помощью Collections.sort()?</h4>

<div class="quiz-option" data-index="0">Comparator</div>
<div class="quiz-option" data-index="1">Sortable</div>
<div class="quiz-option" data-index="2">Comparable (метод compareTo())</div>
<div class="quiz-option" data-index="3">Iterable</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 9. В чём ключевое отличие Comparable от Comparator?</h4>

<div class="quiz-option" data-index="0">Comparable определяет естественный порядок внутри самого класса (compareTo), а Comparator — внешний объект для альтернативной сортировки</div>
<div class="quiz-option" data-index="1">Comparable может сравнивать любые типы, а Comparator — только один</div>
<div class="quiz-option" data-index="2">Comparable находится в пакете java.util, а Comparator — в java.lang</div>
<div class="quiz-option" data-index="3">Comparable работает только с числами, а Comparator — со строками</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 10. Какой код правильно создаёт Comparator для сортировки по длине строки, а при равной длине — по алфавиту?</h4>

<div class="quiz-option" data-index="0">Comparator.comparing(String::length).reversed()</div>
<div class="quiz-option" data-index="1">Comparator.naturalOrder().thenComparing(String::length)</div>
<div class="quiz-option" data-index="2">Comparator.comparingInt(String::length).thenComparing(Comparator.naturalOrder())</div>
<div class="quiz-option" data-index="3">Comparator.comparingInt(String::length)</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 11. Какое утверждение верно о потокобезопасности стандартных коллекций (ArrayList, HashSet, HashMap)?</h4>

<div class="quiz-option" data-index="0">Все стандартные коллекции потокобезопасны по умолчанию</div>
<div class="quiz-option" data-index="1">Ни одна из стандартных коллекций НЕ является потокобезопасной</div>
<div class="quiz-option" data-index="2">Только HashMap является потокобезопасным</div>
<div class="quiz-option" data-index="3">ArrayList потокобезопасен, а HashSet — нет</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 12. Какой из следующих способов создания потокобезопасной коллекции является корректным?</h4>

<div class="quiz-option" data-index="0">Collections.synchronizedList(new ArrayList&lt;&gt;())</div>
<div class="quiz-option" data-index="1">new ArrayList&lt;&gt;().synchronized()</div>
<div class="quiz-option" data-index="2">new ThreadSafeList&lt;&gt;()</div>
<div class="quiz-option" data-index="3">ArrayList.concurrent()</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 13. Какая структура данных лежит в основе PriorityQueue в Java?</h4>

<div class="quiz-option" data-index="0">Двусвязный список</div>
<div class="quiz-option" data-index="1">Красно-чёрное дерево</div>
<div class="quiz-option" data-index="2">Хэш-таблица</div>
<div class="quiz-option" data-index="3">Мин-куча (min-heap) — элемент с наименьшим приоритетом извлекается первым</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 14. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
Queue<Integer> pq = new PriorityQueue<>();
pq.add(30);
pq.add(10);
pq.add(20);
System.out.println(pq.poll() + " " + pq.poll());
```

<div class="quiz-option" data-index="0">30 10</div>
<div class="quiz-option" data-index="1">30 20</div>
<div class="quiz-option" data-index="2">10 20</div>
<div class="quiz-option" data-index="3">20 10</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 15. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
Set<String> set = new HashSet<>();
set.add(null);
set.add("A");
set.add(null);
System.out.println(set.size() + " " + set.contains(null));
```

<div class="quiz-option" data-index="0">3 true</div>
<div class="quiz-option" data-index="1">2 true</div>
<div class="quiz-option" data-index="2">1 true</div>
<div class="quiz-option" data-index="3">Ошибка: NullPointerException</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 2: STREAM API (Вопросы 16–19) ===== -->

<div class="quiz-question" data-correct="2">
<h4>Вопрос 16. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
List<Integer> nums = List.of(1, 2, 3, 4, 5);
long count = nums.stream()
    .filter(n -> n % 2 == 0)
    .count();
System.out.println(count);
```

<div class="quiz-option" data-index="0">5</div>
<div class="quiz-option" data-index="1">3</div>
<div class="quiz-option" data-index="2">2</div>
<div class="quiz-option" data-index="3">0</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 17. Какой метод Stream API преобразует каждый элемент потока в другой объект?</h4>

<div class="quiz-option" data-index="0">filter()</div>
<div class="quiz-option" data-index="1">collect()</div>
<div class="quiz-option" data-index="2">reduce()</div>
<div class="quiz-option" data-index="3">map()</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 18. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
List<String> words = List.of("hello", "world", "java");
List<String> result = words.stream()
    .map(String::toUpperCase)
    .collect(Collectors.toList());
System.out.println(result);
```

<div class="quiz-option" data-index="0">[hello, world, java]</div>
<div class="quiz-option" data-index="1">[HELLO, WORLD, JAVA]</div>
<div class="quiz-option" data-index="2">[Hello, World, Java]</div>
<div class="quiz-option" data-index="3">Ошибка компиляции</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 19. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
List<String> words = List.of("cat", "car", "dog", "deer");
Map<Character, List<String>> grouped = words.stream()
    .collect(Collectors.groupingBy(w -> w.charAt(0)));
System.out.println(grouped.get('c'));
```

<div class="quiz-option" data-index="0">[cat, car]</div>
<div class="quiz-option" data-index="1">[cat, car, dog, deer]</div>
<div class="quiz-option" data-index="2">[dog, deer]</div>
<div class="quiz-option" data-index="3">Ошибка компиляции</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 3: ПОТОКИ ВВОДА/ВЫВОДА (Вопросы 20–28) ===== -->

<div class="quiz-question" data-correct="3">
<h4>Вопрос 20. Какие два базовых абстрактных класса представляют байтовые потоки в Java?</h4>

<div class="quiz-option" data-index="0">FileReader и FileWriter</div>
<div class="quiz-option" data-index="1">BufferedReader и BufferedWriter</div>
<div class="quiz-option" data-index="2">DataInputStream и DataOutputStream</div>
<div class="quiz-option" data-index="3">InputStream и OutputStream</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 21. Чем символьные потоки (Reader/Writer) отличаются от байтовых (InputStream/OutputStream)?</h4>

<div class="quiz-option" data-index="0">Символьные потоки работают с char (16-бит, учитывают кодировку), байтовые — с byte (8-бит, сырые данные)</div>
<div class="quiz-option" data-index="1">Символьные потоки быстрее байтовых</div>
<div class="quiz-option" data-index="2">Байтовые потоки не могут читать файлы</div>
<div class="quiz-option" data-index="3">Символьные потоки работают только с UTF-8</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 22. Какой метод класса BufferedReader позволяет читать файл построчно?</h4>

<div class="quiz-option" data-index="0">read()</div>
<div class="quiz-option" data-index="1">nextLine()</div>
<div class="quiz-option" data-index="2">readLine()</div>
<div class="quiz-option" data-index="3">getLine()</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 23. К какому типу потоков относится System.in?</h4>

<div class="quiz-option" data-index="0">PrintStream</div>
<div class="quiz-option" data-index="1">InputStream</div>
<div class="quiz-option" data-index="2">Reader</div>
<div class="quiz-option" data-index="3">BufferedReader</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 24. К какому типу потоков относятся System.out и System.err?</h4>

<div class="quiz-option" data-index="0">OutputStream</div>
<div class="quiz-option" data-index="1">Writer</div>
<div class="quiz-option" data-index="2">BufferedWriter</div>
<div class="quiz-option" data-index="3">PrintStream</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 25. Какой интерфейс должен реализовать класс, чтобы его объекты можно было сериализовать через ObjectOutputStream?</h4>

<div class="quiz-option" data-index="0">Serializable</div>
<div class="quiz-option" data-index="1">Externalizable</div>
<div class="quiz-option" data-index="2">Cloneable</div>
<div class="quiz-option" data-index="3">Writable</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 26. Какой класс NIO.2 представляет путь к файлу или директории?</h4>

<div class="quiz-option" data-index="0">File</div>
<div class="quiz-option" data-index="1">FileSystem</div>
<div class="quiz-option" data-index="2">Path</div>
<div class="quiz-option" data-index="3">FilePath</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 27. Какой метод NIO.2 позволяет рекурсивно обойти дерево файлов, возвращая Stream&lt;Path&gt;?</h4>

<div class="quiz-option" data-index="0">Files.list()</div>
<div class="quiz-option" data-index="1">Files.walk()</div>
<div class="quiz-option" data-index="2">Files.traverse()</div>
<div class="quiz-option" data-index="3">Path.walk()</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 28. Какой метод NIO.2 создаёт все промежуточные каталоги вместе с целевым?</h4>

<div class="quiz-option" data-index="0">Files.createDirectories()</div>
<div class="quiz-option" data-index="1">Files.createDirectory()</div>
<div class="quiz-option" data-index="2">Files.mkdirs()</div>
<div class="quiz-option" data-index="3">Path.createDirs()</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 4: МНОГОПОТОЧНОСТЬ (Вопросы 29–40) ===== -->

<div class="quiz-question" data-correct="2">
<h4>Вопрос 29. Какая из перечисленных причин НЕ является мотивацией для использования многопоточности?</h4>

<div class="quiz-option" data-index="0">Использование всех ядер процессора</div>
<div class="quiz-option" data-index="1">Неблокирующий пользовательский интерфейс</div>
<div class="quiz-option" data-index="2">Автоматическое ускорение любого кода в 2 раза</div>
<div class="quiz-option" data-index="3">Обработка множества одновременных запросов на сервере</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 30. Какие два основных способа создания потока в Java?</h4>

<div class="quiz-option" data-index="0">Реализовать интерфейс Callable и наследовать класс Process</div>
<div class="quiz-option" data-index="1">Наследовать класс Thread (переопределить run()) или реализовать интерфейс Runnable</div>
<div class="quiz-option" data-index="2">Использовать класс Executor и интерфейс Scheduler</div>
<div class="quiz-option" data-index="3">Вызвать Runtime.getRuntime().exec() или System.thread()</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 31. В чём разница между вызовом start() и run() у объекта Thread?</h4>

<div class="quiz-option" data-index="0">Разницы нет — оба запускают новый поток</div>
<div class="quiz-option" data-index="1">run() создаёт новый поток, а start() выполняет код в текущем</div>
<div class="quiz-option" data-index="2">start() вызывает run() синхронно в том же потоке</div>
<div class="quiz-option" data-index="3">start() создаёт новый поток и вызывает run() в нём, а прямой вызов run() выполняет код в текущем потоке</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 32. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
Thread t = new Thread(() -> System.out.print("A"));
t.run();
System.out.print("B");
```

<div class="quiz-option" data-index="0">AB — вызов run() выполняется синхронно в текущем потоке</div>
<div class="quiz-option" data-index="1">BA — новый поток выполнится позже</div>
<div class="quiz-option" data-index="2">Порядок случайный (AB или BA)</div>
<div class="quiz-option" data-index="3">Ошибка выполнения</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 33. Каков правильный порядок состояний жизненного цикла потока от создания до завершения?</h4>

<div class="quiz-option" data-index="0">RUNNABLE → NEW → BLOCKED → TERMINATED</div>
<div class="quiz-option" data-index="1">NEW → TERMINATED → RUNNABLE → WAITING</div>
<div class="quiz-option" data-index="2">NEW → RUNNABLE → (BLOCKED / WAITING / TIMED_WAITING) → TERMINATED</div>
<div class="quiz-option" data-index="3">CREATED → RUNNING → STOPPED → DEAD</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 34. Какой метод приостанавливает выполнение текущего потока на указанное количество миллисекунд?</h4>

<div class="quiz-option" data-index="0">Thread.wait(ms)</div>
<div class="quiz-option" data-index="1">Thread.sleep(ms)</div>
<div class="quiz-option" data-index="2">Thread.pause(ms)</div>
<div class="quiz-option" data-index="3">Thread.delay(ms)</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 35. Почему операция counter++ НЕ является потокобезопасной?</h4>

<div class="quiz-option" data-index="0">Потому что это три операции (чтение, инкремент, запись), и другой поток может вмешаться между ними</div>
<div class="quiz-option" data-index="1">Потому что ++ работает только с типом long</div>
<div class="quiz-option" data-index="2">Потому что компилятор оптимизирует эту операцию</div>
<div class="quiz-option" data-index="3">Потому что counter++ вызывает исключение в многопоточной среде</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 36. Что обеспечивает ключевое слово synchronized в Java?</h4>

<div class="quiz-option" data-index="0">Ускоряет выполнение метода за счёт кэширования</div>
<div class="quiz-option" data-index="1">Запрещает вызов метода из другого класса</div>
<div class="quiz-option" data-index="2">Гарантирует, что только один поток одновременно может выполнять синхронизированный блок (захватывая монитор объекта)</div>
<div class="quiz-option" data-index="3">Делает переменную видимой только в текущем потоке</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 37. В каком классе определены методы wait(), notify() и notifyAll()?</h4>

<div class="quiz-option" data-index="0">Thread</div>
<div class="quiz-option" data-index="1">Object</div>
<div class="quiz-option" data-index="2">Runnable</div>
<div class="quiz-option" data-index="3">Lock</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 38. Что произойдёт при вызове wait() вне synchronized-блока? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
Object lock = new Object();
lock.wait();
```

<div class="quiz-option" data-index="0">Поток заснёт и будет ждать notify()</div>
<div class="quiz-option" data-index="1">Ничего — метод просто вернёт управление</div>
<div class="quiz-option" data-index="2">Ошибка компиляции</div>
<div class="quiz-option" data-index="3">Будет выброшен IllegalMonitorStateException — wait() требует захвата монитора</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 39. Какой класс из пакета java.util.concurrent обеспечивает атомарный инкремент без synchronized?</h4>

<div class="quiz-option" data-index="0">AtomicInteger (метод incrementAndGet())</div>
<div class="quiz-option" data-index="1">SynchronizedInteger</div>
<div class="quiz-option" data-index="2">VolatileInteger</div>
<div class="quiz-option" data-index="3">ThreadSafeCounter</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 40. Почему реализация Runnable предпочтительнее наследования Thread?</h4>

<div class="quiz-option" data-index="0">Runnable работает быстрее, чем Thread</div>
<div class="quiz-option" data-index="1">Thread не может выполнять код</div>
<div class="quiz-option" data-index="2">Runnable не занимает единственное наследование (Java не поддерживает множественное наследование классов) и разделяет задачу от механизма потока</div>
<div class="quiz-option" data-index="3">Runnable поддерживает возврат значений, а Thread — нет</div>
<div class="quiz-feedback"></div>
</div>

<button class="quiz-btn" onclick="showScore()">Показать результат</button>

<div class="quiz-score" id="quizScore">
<h3 id="scoreText"></h3>
<p id="scoreDetail"></p>
<button class="quiz-btn" onclick="resetQuiz()">Пройти заново</button>
</div>

</div>

<script>
(function() {
  var answers = {
    'Вопрос 1': 'Корень иерархии коллекций — Iterable, от которого наследуется Collection, а от Collection — List, Set и Queue. Map — это отдельная иерархия.',
    'Вопрос 2': 'Map не наследует Collection и не является частью иерархии Iterable → Collection. Map хранит пары ключ-значение и образует отдельную ветвь JCF.',
    'Вопрос 3': 'List допускает дубликаты и сохраняет порядок вставки. Строка "A" добавляется дважды, поэтому size() = 3, а get(2) возвращает второй "A".',
    'Вопрос 4': 'HashSet не допускает дубликатов. Повторное добавление "Java" игнорируется (метод add() вернёт false), поэтому размер множества равен 2.',
    'Вопрос 5': 'LinkedHashSet хранит элементы в порядке вставки, используя связный список поверх хэш-таблицы. HashSet не гарантирует порядок, TreeSet сортирует.',
    'Вопрос 6': 'TreeMap хранит записи отсортированными по ключам, используя красно-чёрное дерево. HashMap не гарантирует порядок, LinkedHashMap сохраняет порядок вставки.',
    'Вопрос 7': 'В JCF принята конвенция «Реализация + Интерфейс»: ArrayList (массив + List), HashSet (хэш + Set), TreeMap (дерево + Map), LinkedList (связный список + List).',
    'Вопрос 8': 'Для сортировки «по умолчанию» элементы должны реализовать Comparable с методом compareTo(). Comparator задаёт альтернативный порядок извне.',
    'Вопрос 9': 'Comparable определяет «естественный порядок» внутри класса через compareTo(). Comparator — отдельный объект, позволяющий задать любую пользовательскую сортировку.',
    'Вопрос 10': 'Метод comparing/comparingInt задаёт первичный критерий, thenComparing — вторичный. Сначала сортируем по длине, при равенстве — по естественному порядку (алфавиту).',
    'Вопрос 11': 'Стандартные коллекции (ArrayList, HashSet, HashMap) НЕ потокобезопасны. Для многопоточного доступа нужны обёртки или конкурентные коллекции.',
    'Вопрос 12': 'Collections.synchronizedList() оборачивает список в потокобезопасную обёртку, синхронизируя все операции. Также существуют CopyOnWriteArrayList и ConcurrentHashMap.',
    'Вопрос 13': 'PriorityQueue реализована на основе мин-кучи (min-heap). Элемент с наименьшим значением (или приоритетом) всегда находится в голове очереди.',
    'Вопрос 14': 'PriorityQueue — это мин-куча. poll() извлекает минимальный элемент: сначала 10, затем 20. Элементы выходят в порядке возрастания.',
    'Вопрос 15': 'HashSet допускает ровно один null. Повторное добавление null игнорируется (дубликат). Итого: "A" и null — 2 элемента, contains(null) возвращает true.',
    'Вопрос 16': 'filter(n -> n % 2 == 0) оставляет только чётные числа: 2 и 4. Метод count() подсчитывает количество элементов в потоке — результат 2.',
    'Вопрос 17': 'Метод map() применяет функцию к каждому элементу потока и возвращает поток преобразованных элементов. filter() отбирает, collect() собирает, reduce() свёртывает.',
    'Вопрос 18': 'map(String::toUpperCase) преобразует каждую строку в верхний регистр. collect(Collectors.toList()) собирает результат в список: [HELLO, WORLD, JAVA].',
    'Вопрос 19': 'Collectors.groupingBy() группирует элементы по первой букве. Слова "cat" и "car" начинаются с символа \'c\', поэтому grouped.get(\'c\') возвращает [cat, car].',
    'Вопрос 20': 'InputStream (чтение байтов) и OutputStream (запись байтов) — базовые абстрактные классы для байтовых потоков. Reader/Writer — для символьных.',
    'Вопрос 21': 'Reader/Writer оперируют символами (char, 16-бит) и учитывают кодировку текста. InputStream/OutputStream работают с сырыми байтами (8-бит) без интерпретации.',
    'Вопрос 22': 'BufferedReader.readLine() читает строку до символа перевода строки или конца потока. Возвращает null при достижении конца файла.',
    'Вопрос 23': 'System.in имеет тип InputStream — байтовый поток ввода. Для удобного чтения текста его обычно оборачивают в BufferedReader или Scanner.',
    'Вопрос 24': 'System.out и System.err имеют тип PrintStream — байтовый поток вывода с удобными методами println(), print() и printf().',
    'Вопрос 25': 'Для сериализации объекта через ObjectOutputStream класс должен реализовать маркерный интерфейс Serializable (без методов).',
    'Вопрос 26': 'Path (java.nio.file) — интерфейс NIO.2, представляющий путь к файлу или директории. Заменяет устаревший класс File для большинства операций.',
    'Вопрос 27': 'Files.walk() рекурсивно обходит дерево файлов и возвращает Stream<Path>. Files.list() возвращает только содержимое одного каталога (без рекурсии).',
    'Вопрос 28': 'Files.createDirectories() создаёт целевой каталог и все несуществующие промежуточные. Files.createDirectory() создаёт только один каталог и бросает исключение, если родительский не существует.',
    'Вопрос 29': 'Многопоточность не ускоряет код автоматически. Она полезна для параллельных вычислений, неблокирующего UI и обработки множества запросов, но требует правильного проектирования.',
    'Вопрос 30': 'Два основных способа: наследовать Thread (переопределить run()) или реализовать Runnable (передать в конструктор Thread). Также можно использовать лямбда-выражение для Runnable.',
    'Вопрос 31': 'Метод start() создаёт новый поток ОС и вызывает run() в нём. Прямой вызов run() — обычный вызов метода в текущем потоке без создания нового.',
    'Вопрос 32': 'Вызов run() (а не start()) выполняет метод синхронно в текущем потоке. Сначала печатается "A", затем "B". Новый поток не создаётся.',
    'Вопрос 33': 'Поток начинается в состоянии NEW (создан), переходит в RUNNABLE (после start()), может попасть в BLOCKED/WAITING/TIMED_WAITING, и завершается в TERMINATED.',
    'Вопрос 34': 'Thread.sleep(ms) приостанавливает текущий поток на заданное время. wait() — метод Object для межпоточного взаимодействия, работает только в synchronized-блоке.',
    'Вопрос 35': 'Операция counter++ состоит из трёх шагов: чтение значения, увеличение на 1, запись обратно. Между этими шагами другой поток может вмешаться — это называется состояние гонки (race condition).',
    'Вопрос 36': 'synchronized захватывает монитор (блокировку) объекта. Пока один поток находится в synchronized-блоке, другие потоки ждут освобождения монитора.',
    'Вопрос 37': 'Методы wait(), notify() и notifyAll() определены в классе Object, а не в Thread. Они используются для межпоточного взаимодействия и вызываются только внутри synchronized-блока.',
    'Вопрос 38': 'Методы wait(), notify() и notifyAll() требуют, чтобы текущий поток владел монитором объекта (был внутри synchronized). Иначе выбрасывается IllegalMonitorStateException.',
    'Вопрос 39': 'AtomicInteger из java.util.concurrent.atomic обеспечивает атомарные операции (incrementAndGet(), compareAndSet()) без synchronized, используя аппаратные CAS-инструкции.',
    'Вопрос 40': 'Java не поддерживает множественное наследование классов. Реализуя Runnable, класс может наследовать другой класс. Также Runnable отделяет задачу от механизма выполнения.'
  };

  document.querySelectorAll('.quiz-option').forEach(function(option) {
    option.addEventListener('click', function() {
      var question = this.closest('.quiz-question');
      if (question.classList.contains('answered')) return;
      question.classList.add('answered');

      var correct = parseInt(question.getAttribute('data-correct'));
      var selected = parseInt(this.getAttribute('data-index'));
      var feedback = question.querySelector('.quiz-feedback');
      var qNum = question.querySelector('h4').textContent.split('.')[0];

      question.querySelectorAll('.quiz-option').forEach(function(opt) {
        opt.classList.add('disabled');
      });

      this.classList.add('selected');

      if (selected === correct) {
        this.classList.add('correct');
        feedback.className = 'quiz-feedback correct';
        feedback.textContent = 'Правильно! ' + answers[qNum];
      } else {
        this.classList.add('wrong');
        question.querySelectorAll('.quiz-option')[correct].classList.add('correct');
        feedback.className = 'quiz-feedback wrong';
        feedback.textContent = 'Неправильно. ' + answers[qNum];
      }
    });
  });

  window.showScore = function() {
    var total = document.querySelectorAll('.quiz-question').length;
    var correctCount = 0;
    document.querySelectorAll('.quiz-question').forEach(function(q) {
      var correct = parseInt(q.getAttribute('data-correct'));
      var selected = q.querySelector('.quiz-option.selected');
      if (selected && parseInt(selected.getAttribute('data-index')) === correct) {
        correctCount++;
      }
    });

    var scoreDiv = document.getElementById('quizScore');
    var scoreText = document.getElementById('scoreText');
    var scoreDetail = document.getElementById('scoreDetail');

    scoreDiv.style.display = 'block';
    scoreText.textContent = 'Ваш результат: ' + correctCount + ' из ' + total;

    var pct = Math.round(correctCount / total * 100);
    if (pct >= 90) scoreDetail.textContent = 'Отлично! Вы прекрасно усвоили материал.';
    else if (pct >= 70) scoreDetail.textContent = 'Хорошо! Но есть темы для повторения.';
    else if (pct >= 50) scoreDetail.textContent = 'Удовлетворительно. Рекомендуется перечитать лекцию.';
    else scoreDetail.textContent = 'Нужно повторить материал лекции и практики.';

    scoreDiv.scrollIntoView({ behavior: 'smooth' });
  };

  window.resetQuiz = function() {
    document.querySelectorAll('.quiz-question').forEach(function(q) {
      q.classList.remove('answered');
      q.querySelectorAll('.quiz-option').forEach(function(opt) {
        opt.classList.remove('selected', 'correct', 'wrong', 'disabled');
      });
      q.querySelector('.quiz-feedback').className = 'quiz-feedback';
      q.querySelector('.quiz-feedback').textContent = '';
    });
    document.getElementById('quizScore').style.display = 'none';
    document.querySelector('.quiz-container').scrollIntoView({ behavior: 'smooth' });
  };
})();
</script>