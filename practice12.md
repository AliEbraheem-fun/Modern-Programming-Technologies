# Практическое занятие 12: Системы контроля версий и процессы разработки

Всё занятие проходит в командной строке: кнопки «Commit» в IDE сегодня под запретом. Пока вы не увидите, что происходит с указателями вручную, графический интерфейс будет казаться магией, а магия ломается в самый неподходящий момент.

Работайте в **Git Bash** (Windows) или обычном терминале (Linux, macOS). **PowerShell** тоже подходит: где команды различаются, приведены оба варианта.

## Часть 1: Подготовка и первый репозиторий

Репозиторий — это не папка с файлами, а папка с файлами плюс их полная биография: как медицинская карта, где снимки хранятся вместе с пациентом и видно, когда и что изменилось.

### Задание 1.1: Настройка Git, редактора и оболочки

Проверьте версии и настройте Git один раз для всех проектов. Git нужен не ниже **2.23** — именно в этой версии появились команды `switch` и `restore`, которыми мы пользуемся весь день.

```bash
git --version
java -version
mvn -version

git config --global user.name "Ivan Ivanov"
git config --global user.email "ivan@example.com"
git config --global init.defaultBranch main
```

Следующие две настройки зависят от операционной системы. Выполните **только свой** блок — команды из чужого блока перезапишут ваши значения.

Windows (Git Bash или PowerShell):

```bash
git config --global core.autocrlf true
git config --global core.editor "notepad"
```

Linux и macOS:

```bash
git config --global core.autocrlf input
git config --global core.editor "nano"
```

Проверьте, что получилось:

```bash
git config --list
```

Редактор настроить **обязательно**: сегодня `git rebase -i` и `git commit` без `-m` его откроют, а выйти из незнакомого редактора — отдельный навык.

| Редактор | Сохранить и выйти | Выйти без сохранения |
|----------|-------------------|----------------------|
| Блокнот | Ctrl+S, закрыть окно | Закрыть окно, «Не сохранять» |
| nano | Ctrl+O, Enter, Ctrl+X | Ctrl+X, ответить `n` |
| vim (открывается, если ничего не настроено) | Esc, `:wq`, Enter | Esc, `:q!`, Enter |

Держите под рукой таблицу различий оболочек — дальше в тексте эти команды не дублируются.

| Действие | Git Bash / Linux / macOS | PowerShell |
|----------|--------------------------|------------|
| Создать вложенные каталоги | `mkdir -p src/main/java/ru/fa/library` | `mkdir src/main/java/ru/fa/library` |
| Создать файл с одной строкой | `echo "текст" > f.txt` | `Set-Content -Encoding utf8 f.txt "текст"` |
| Дописать строку | `echo "текст" >> f.txt` | `Add-Content -Encoding utf8 f.txt "текст"` |
| Показать файл | `cat f.txt` | `cat f.txt` (алиас `Get-Content`) |
| Цикл 1…6 | `for i in $(seq 1 6); do ... done` | `foreach ($i in 1..6) { ... }` |
| Две команды подряд | `команда1 && команда2` | `команда1; команда2` |

Оператор `>` в Windows PowerShell 5.1 пишет файл в UTF-16, и Git примет его за двоичный, — поэтому там `Set-Content -Encoding utf8`. **Файлы с Java-кодом создавайте в редакторе или IDE и сохраняйте в UTF-8**; в оболочке делайте только простые текстовые файлы (`README.md`, `.gitignore`, `notes.txt`).

**Ответьте письменно:** (1) Какая у вас версия Git и какой редактор настроен как `core.editor`? (2) Зачем нужна настройка `core.autocrlf` и что произойдёт без неё в команде из Windows- и Linux-разработчиков?

### Задание 1.2: Репозиторий и серия коммитов

Создайте каталог для всех сегодняшних экспериментов (например, `D:\git-practice` или `~/git-practice`), перейдите в него и выполните:

```bash
git init -b main library
cd library
git status
```

Создайте `README.md` со строкой `# Библиотека`, затем понаблюдайте за тремя состояниями файла:

```bash
git status                 # README.md — untracked
git add README.md
git status                 # README.md — staged
git commit -m "docs: добавить README проекта"
git log
```

Создайте каталог `src/main/java/ru/fa/library` и три файла с кодом.

```java
// Book.java
package ru.fa.library;

/** Книга библиотеки: название, автор и год издания. */
public record Book(String title, String author, int year) {
}
```

```java
// BookService.java
package ru.fa.library;

import java.util.ArrayList;
import java.util.List;

/** Хранилище книг и операции над ними. */
public class BookService {

    private final List<Book> books = new ArrayList<>();

    /** Добавляет книгу в библиотеку. */
    public void add(Book book) {
        books.add(book);
    }

    /** Возвращает все книги библиотеки. */
    public List<Book> findAll() {
        return List.copyOf(books);
    }
}
```

```java
// LibraryApp.java
package ru.fa.library;

/** Точка входа: небольшая демонстрация работы BookService. */
public class LibraryApp {

    public static void main(String[] args) {
        BookService service = new BookService();
        service.add(new Book("Война и мир", "Толстой", 1869));
        service.add(new Book("Мастер и Маргарита", "Булгаков", 1967));

        System.out.println("Все книги:");
        service.findAll().forEach(book ->
                System.out.println("  " + book.title() + " — " + book.author() + ", " + book.year()));
    }
}
```

Проверьте сборку и запуск (команды одинаковы в обеих оболочках) и сделайте **три отдельных** коммита вместо одного общего:

```bash
javac -d out -sourcepath src/main/java src/main/java/ru/fa/library/LibraryApp.java
java -cp out ru.fa.library.LibraryApp

git add src/main/java/ru/fa/library/Book.java
git commit -m "feat: добавить модель Book"
git add src/main/java/ru/fa/library/BookService.java
git commit -m "feat: добавить BookService с хранением книг"
git add src/main/java/ru/fa/library/LibraryApp.java
git commit -m "feat: добавить точку входа LibraryApp"
```

Допишите в `README.md` строку `Учебный проект курса «Современные технологии программирования».` и сделайте четвёртый коммит `docs: описать назначение проекта`.

**Ответьте письменно:** (1) Что означает `untracked` в выводе `git status`? (2) Почему три коммита лучше одного «добавил всё» — приведите ситуацию, в которой это спасёт? (3) Каталог `out` отмечен как неотслеживаемый: почему его нельзя коммитить?

### Задание 1.3: История — log, diff, show, blame

Добавьте в `BookService.java` после `findAll()` метод, но **не коммитьте сразу**:

```java
    /** Возвращает количество книг в библиотеке. */
    public int count() {
        return books.size();
    }
```

```bash
git diff                      # рабочий каталог против индекса
git add src/main/java/ru/fa/library/BookService.java
git diff                      # пусто: всё уже в индексе
git diff --staged             # индекс против последнего коммита
git commit -m "feat: добавить подсчёт книг"
```

Выполните и разберите вывод каждой команды ниже:

```bash
git log --oneline
git log --oneline --graph --all --decorate
git log -3 --stat
git log -p -1
git log --grep="feat"
git show HEAD~2
git blame src/main/java/ru/fa/library/BookService.java
```

Попробуйте частичную подготовку: измените в `LibraryApp` текст `"Все книги:"` на `"Каталог библиотеки:"` и выполните `git add -p src/main/java/ru/fa/library/LibraryApp.java`. Git покажет кусок изменений и спросит, включать ли его: `y` — да, `n` — нет, `q` — выйти. Ответьте `y` и закоммитьте (`docs: поправить заголовок вывода`).

**Ответьте письменно:** (1) В чём разница между `git diff` и `git diff --staged`? Опишите состояние файла, при котором обе команды покажут изменения. (2) На какой коммит указывает `HEAD~2` в вашем репозитории? (3) Зачем нужен `git blame`, если есть `git log`?

---

## Часть 2: Файл .gitignore

Репозиторий — чемодан в поездку: кладут только то, что нельзя купить на месте. Классы, папку IDE и локальные пароли «купить на месте» можно.

### Задание 2.1: Исключение мусора

Убедитесь, что `git status` показывает каталог `out/`, и создайте в корне репозитория `.gitignore`:

```text
# Результаты сборки
out/
target/
*.class
*.jar

# Настройки IDE
.idea/
*.iml
.vscode/

# Логи и временные файлы
*.log
.DS_Store
```

```bash
git status                    # каталога out/ в списке больше нет
git add .gitignore
git commit -m "chore: добавить .gitignore"
git check-ignore -v out/ru/fa/library/Book.class
```

### Задание 2.2: Файл уже отслеживается

Смоделируйте типичную ошибку: создайте `application-local.properties` со строкой `db.password=SuperSecret123` и закоммитьте его.

```bash
git add application-local.properties
git commit -m "chore: локальные настройки"
```

Теперь спохватитесь. Допишите в `.gitignore`:

```text
# Локальные настройки и секреты
application-local.properties
.env
```

```bash
git add .gitignore
git commit -m "chore: не хранить локальные настройки в репозитории"
git ls-files application-local.properties    # файл всё ещё в индексе — правило не сработало (пустой вывод после git rm --cached будет доказательством обратного)

git rm --cached application-local.properties
git commit -m "chore: убрать локальные настройки из репозитория"
git status                    # теперь файл игнорируется
git log --oneline -- application-local.properties
```

**Ответьте письменно:** (1) Почему правило `.gitignore` не подействовало на уже отслеживаемый файл? (2) Последняя команда показала, что пароль остался в истории: какие действия нужны в реальном проекте и в каком порядке? (3) Чем `git rm --cached file` отличается от `git rm file`?

---

## Часть 3: Ветки и быстрая перемотка

Ветка — закладка в книге: сколько бы вы их ни положили, книга не станет толще, а перелистнуть на другую закладку — мгновенная операция.

### Задание 3.1: Ветка под задачу и fast-forward

```bash
git switch -c feature/find-by-title
git branch
```

Добавьте в `BookService.java` после `count()` метод поиска и закоммитьте:

```java
    /** Ищет книги по части названия. */
    public List<Book> findBooks(String query) {
        return books.stream()
                .filter(book -> book.title().contains(query))
                .toList();
    }
```

```bash
git commit -am "feat: добавить поиск книг по названию"
```

Вторым коммитом добавьте в конец `LibraryApp.main` вызов поиска:

```java
        System.out.println("Поиск по запросу «Мастер»:");
        service.findBooks("Мастер").forEach(book -> System.out.println("  " + book.title()));
```

```bash
javac -d out -sourcepath src/main/java src/main/java/ru/fa/library/LibraryApp.java
java -cp out ru.fa.library.LibraryApp
git commit -am "feat: показать результаты поиска в LibraryApp"

git switch main
git log --oneline -1              # запомните хеш вершины main
git merge feature/find-by-title
git log --oneline --graph -5
```

**Ответьте письменно:** (1) Что означает слово `Fast-forward` в выводе `git merge` и появился ли новый коммит слияния? (2) Что делает `git commit -am` и почему она не сработала бы для только что созданного файла? (3) Куда переместился указатель `main`?

### Задание 3.2: Слияние с запретом перемотки

```bash
git switch -c feature/oldest-book
```

Добавьте в `BookService.java` после `findBooks` метод и слейте ветку иначе:

```java
    /** Возвращает год издания самой старой книги, или 0 для пустой библиотеки. */
    public int oldestYear() {
        return books.stream().mapToInt(Book::year).min().orElse(0);
    }
```

```bash
git commit -am "feat: добавить год самой старой книги"
git switch main
git merge --no-ff feature/oldest-book -m "merge: год самой старой книги"
git log --oneline --graph -8
git show --format="%h %p" -s HEAD
```

**Ответьте письменно:** (1) Чем граф после `--no-ff` отличается от графа из задания 3.1? (2) Сколько родителей у коммита слияния и как это видно в выводе `%p`? (3) Почему многие команды используют `--no-ff` всегда?

---

## Часть 4: Конфликт слияния

Конфликт — не поломка, а вопрос. Два повара дописали в один и тот же рецепт «варить 20 минут» и «варить 40 минут»; автоматика не знает, какой суп вы хотите, и честно спрашивает.

### Задание 4.1: Создаём конфликт специально

Создайте ветку и измените в ней **тело метода `findBooks`**:

```bash
git switch -c feature/search-by-author
```

```java
    /** Ищет книги по фамилии автора. */
    public List<Book> findBooks(String query) {
        return books.stream()
                .filter(book -> book.author().contains(query))
                .toList();
    }
```

```bash
git commit -am "feat: искать книги по автору"
git switch main
```

Теперь измените **тот же метод** в `main` по-другому:

```java
    /** Ищет книги по части названия без учёта регистра. */
    public List<Book> findBooks(String query) {
        String needle = query.toLowerCase();
        return books.stream()
                .filter(book -> book.title().toLowerCase().contains(needle))
                .toList();
    }
```

```bash
git commit -am "feat: искать по названию без учёта регистра"
git merge feature/search-by-author
```

Git ответит `CONFLICT (content): Merge conflict in src/main/java/ru/fa/library/BookService.java` и `Automatic merge failed`. Осмотритесь, **не разрешая конфликт**, а затем отмените слияние целиком:

```bash
git status
git diff
git log --merge --oneline
cat src/main/java/ru/fa/library/BookService.java

git merge --abort
git status                    # состояние вернулось к тому, что было до слияния
```

**Ответьте письменно:** (1) Какие файлы `git status` перечислил в разделе `Unmerged paths`? (2) Что находится между `<<<<<<< HEAD` и `=======`, а что — между `=======` и `>>>>>>>`? (3) Почему Git не смог слить изменения автоматически, хотя правки в других файлах объединил без вопросов?

### Задание 4.2: Разрешение конфликта вручную

Повторите слияние и разрешите конфликт. Удалите все три маркера и напишите **третий, правильный вариант**, объединяющий оба намерения:

```bash
git merge feature/search-by-author
```

```java
    /** Ищет книги по части названия или фамилии автора без учёта регистра. */
    public List<Book> findBooks(String query) {
        String needle = query.toLowerCase();
        return books.stream()
                .filter(book -> book.title().toLowerCase().contains(needle)
                        || book.author().toLowerCase().contains(needle))
                .toList();
    }
```

Измените в `LibraryApp` запрос поиска на `"тол"`: должна найтись «Война и мир» — по фамилии автора и без учёта регистра. Проверьте, что маркеров не осталось, а код собирается и работает:

```bash
git grep -n "<<<<<<<"          # не должно быть ни одной строки
javac -d out -sourcepath src/main/java src/main/java/ru/fa/library/LibraryApp.java
java -cp out ru.fa.library.LibraryApp

git add src/main/java/ru/fa/library/BookService.java src/main/java/ru/fa/library/LibraryApp.java
git commit --no-edit           # принять сообщение о слиянии, подготовленное Git
git log --oneline --graph -8
git branch -d feature/search-by-author
```

Флаг `--no-edit` принимает готовое сообщение; без него откроется редактор — выйти из него можно так, как описано в задании 1.1.

**Ответьте письменно:** (1) Почему после разрешения конфликта обязательно собирать проект и запускать тесты, а не ограничиваться удалением маркеров? (2) Что сделали бы `git checkout --ours` и `git checkout --theirs` и почему здесь они не подошли? (3) Назовите три приёма, снижающих число конфликтов в командной работе.

---

## Часть 5: merge против rebase на одинаковой истории

Merge — вклеить в тетрадь дополнительный лист с пометкой «здесь сошлись два черновика». Rebase — переписать свои страницы набело сразу после последней страницы соседа. Чтобы сравнить честно, нужны две одинаковые тетради.

### Задание 5.1: Две одинаковые ветки

Создайте отдельный маленький репозиторий, чтобы не путать историю основного:

```bash
cd ..
git init -b main rebase-demo
cd rebase-demo
```

```bash
echo "строка 1" > main.txt
git add . && git commit -m "C1: начальная версия"
echo "строка 2" >> main.txt
git commit -am "C2: вторая строка"

git switch -c feature/report
echo "отчёт: черновик" > report.txt
git add report.txt && git commit -m "C3: черновик отчёта"
echo "отчёт: итог" >> report.txt
git commit -am "C4: доработать отчёт"

git branch feature/report-copy    # точная копия ветки: те же коммиты и хеши

git switch main
echo "строка 3" >> main.txt
git commit -am "C5: третья строка"
echo "строка 4" >> main.txt
git commit -am "C6: четвёртая строка"

git branch stable                 # запомним состояние main до слияния
git log --oneline --graph --all --decorate
```

В PowerShell вместо `echo ... >` используйте `Set-Content -Encoding utf8`, вместо `echo ... >>` — `Add-Content -Encoding utf8`, а `&&` замените на `;` (см. таблицу из задания 1.1).

### Задание 5.2: Одну ветку сливаем, другую перебазируем

```bash
git switch main
git merge feature/report -m "merge: влить отчёт в main"

git switch feature/report-copy
git rebase stable

git log --oneline --graph --all --decorate
git log --oneline main
git log --oneline feature/report-copy
git show --format="%h %s" -s feature/report        # исходный C4
git show --format="%h %s" -s feature/report-copy   # C4' после rebase
```

**Ответьте письменно:** (1) Сколько коммитов в `main` и сколько в `feature/report-copy`, откуда взялась разница? (2) Совпадают ли хеши коммитов «C4» в двух ветках и почему? (3) Какая история удобнее читается, а какая честнее отражает реальный ход событий? (4) В каком случае вы применили бы rebase к рабочей ветке, а в каком — категорически нет?

---

## Часть 6: Интерактивный rebase

Черновик перед сдачей переписывают набело: пять записок «доделал», «фикс», «ещё раз фикс» превращают в один осмысленный абзац.

### Задание 6.1: Мусорная история

```bash
cd ../library
git switch -c feature/statistics
```

Добавьте в `BookService.java` после `oldestYear()` метод — намеренно с ошибкой, он не проверяет пустой список:

```java
    /** Возвращает средний год издания книг библиотеки. */
    public double averageYear() {
        return books.stream().mapToInt(Book::year).average().getAsDouble();
    }
```

```bash
git commit -am "wip"
```

Сделайте ещё три коммита с плохими сообщениями, каждый раз слегка меняя тот же код:

1. добавьте в JavaDoc метода строку `@return средний год издания` → `git commit -am "фикс"`;
2. вынесите поток в локальную переменную, не трогая логику: первой строкой тела `var years = books.stream().mapToInt(Book::year);`, второй — `return years.average().getAsDouble();` → `git commit -am "ещё раз фикс"`;
3. добавьте в конец `LibraryApp.main` строку ниже → `git commit -am "готово"`.

```java
        System.out.printf("Средний год издания: %.1f%n", service.averageYear());
```

Ошибку с пустым списком пока не исправляйте — `getAsDouble()` должен остаться в коде, он понадобится нам в задании 7.3.

### Задание 6.2: Объединение коммитов

```bash
git log --oneline -4
git rebase -i HEAD~4
```

Откроется редактор со списком коммитов **от старых к новым**. Замените первые слова строк (хеши и тексты не трогайте):

```text
pick   <хеш> wip
squash <хеш> фикс
squash <хеш> ещё раз фикс
squash <хеш> готово
```

Сохраните и закройте редактор. Откроется **второй** редактор — с объединённым сообщением: удалите всё и напишите одну строку `feat: добавить средний год издания книг`, снова сохраните и закройте.

```bash
git log --oneline -3
javac -d out -sourcepath src/main/java src/main/java/ru/fa/library/LibraryApp.java
java -cp out ru.fa.library.LibraryApp
git switch main
git merge feature/statistics
```

Если запутались в редакторе — `git rebase --abort` вернёт репозиторий в состояние до начала операции.

**Ответьте письменно:** (1) Сколько коммитов было и сколько стало, изменились ли их хеши? (2) Чем `squash` отличается от `fixup` и когда удобнее второй? (3) Почему `rebase -i` допустим для `feature/statistics`, но был бы недопустим для общей ветки `main`?

---

## Часть 7: stash, tag и cherry-pick

Stash — смахнуть недоделанные бумаги со стола в верхний ящик, разобраться со срочным делом и достать их обратно ровно в том же виде.

### Задание 7.1: stash — отложить работу

Начните править `LibraryApp.java`: добавьте в конец `main` строку, которая **не компилируется**, — так бывает, когда работу прерывают на середине.

```java
        System.out.println("Незаконченная строка"
```

```bash
git stash push -m "недописанный вывод в LibraryApp"
git status                     # рабочий каталог чистый
git stash list
javac -d out -sourcepath src/main/java src/main/java/ru/fa/library/LibraryApp.java   # собирается

git stash pop
git stash list                 # пусто
```

Удалите незаконченную строку из файла и убедитесь, что проект снова компилируется.

**Ответьте письменно:** (1) Чем `git stash` удобнее коммита «временно, потом уберу»? (2) В чём разница между `git stash pop` и `git stash apply`? (3) Что делает флаг `-u` у `git stash push` и когда он обязателен?

### Задание 7.2: tag — метка версии

```bash
git switch main
git tag -a v1.0.0 -m "Первая версия учебной библиотеки"
git tag
git show v1.0.0
git switch -c release/1.0 v1.0.0      # ветка поддержки выпущенной версии
git log --oneline -1
```

### Задание 7.3: cherry-pick — перенести один коммит

В `main` обнаружилась ошибка. Метод `averageYear()`, который вы написали в задании 6.1, заканчивается вызовом `getAsDouble()`: для пустой библиотеки `average()` возвращает пустой `OptionalDouble`, и `getAsDouble()` бросает `NoSuchElementException`. Должен возвращаться 0 — как это уже делает `oldestYear()` через `orElse(0)`. Исправьте это **в main**, заменив метод целиком (обе строки, включая `var years`):

```bash
git switch main
```

```java
    /** Возвращает средний год издания книг, или 0 для пустой библиотеки. */
    public double averageYear() {
        return books.stream().mapToInt(Book::year).average().orElse(0);
    }
```

Эту же ситуацию вы позже проверите тестом `handlesEmptyLibrary` в задании 11.1.

```bash
git commit -am "fix: не падать на пустой библиотеке при расчёте среднего года"
git log --oneline -1              # запишите хеш этого коммита

git switch release/1.0
git cherry-pick <хеш-фикса>
git log --oneline -2
git show --format="%h %s" -s HEAD
```

**Ответьте письменно:** (1) Совпадают ли хеши двух коммитов с одинаковым содержимым и почему? (2) Что делает флаг `-x` у `cherry-pick` и чем он полезен через полгода? (3) Почему `cherry-pick` не должен становиться основным способом переноса кода между ветками?

---

## Часть 8: Ломаем историю и восстанавливаем через reflog

Reflog — корзина операционной системы: пока её не очистили, выброшенное можно достать обратно.

### Задание 8.1: Потеря коммитов и восстановление

```bash
git switch main
git log --oneline -5              # выпишите эти пять строк в отчёт
git reset --hard HEAD~3
git log --oneline -5              # трёх коммитов больше нет
```

Откройте `BookService.java` и убедитесь, что метода `averageYear()` в нём тоже нет. Теперь загляните в журнал перемещений командой `git reflog`:

```text
b7d2f10 (HEAD -> main) HEAD@{0}: reset: moving to HEAD~3
9c4e1a2 HEAD@{1}: commit: fix: не падать на пустой библиотеке при расчёте среднего года
71ba9f3 HEAD@{2}: merge feature/statistics: Fast-forward
5e0c2d8 HEAD@{3}: checkout: moving from feature/statistics to main
```

Верните ветку и проверьте второй сценарий — восстановление удалённой ветки:

```bash
git reset --hard HEAD@{1}
git log --oneline -5                       # сравните со списком, выписанным в начале

git branch -D feature/statistics
git reflog | grep statistics               # Git Bash
git reflog | Select-String statistics      # PowerShell
```

Строк со словом `statistics` будет несколько, и хеши в них указывают на разное: в записях `checkout: moving from feature/statistics to main` хеш — это вершина `main` на момент переключения, а вовсе не вершина удалённой ветки. Хеш в начале каждой строки reflog — это то, чем стал `HEAD` **после** операции. Поэтому вам нужна строка `merge feature/statistics: Fast-forward` (или `rebase (finish): returning to refs/heads/feature/statistics`): именно там `HEAD` совпал с вершиной ветки. Возьмите хеш из её начала:

```bash
git branch feature/statistics <хеш-из-нужной-строки>
git log --oneline -2 feature/statistics
```

**Ответьте письменно:** (1) Что хранит reflog и чем он отличается от `git log`? (2) Reflog доступен только на вашей машине — какие практические последствия у этого ограничения? (3) В каком случае reflog не поможет вернуть работу (подсказка: он помнит коммиты, а не правки)?

---

## Часть 9: Поиск ошибки через git bisect

Игра «угадай число от 1 до 1000 за десять вопросов»: каждый вопрос отбрасывает половину вариантов. Ровно это `bisect` делает с историей коммитов.

### Задание 9.1: Репозиторий с подложенной ошибкой

```bash
cd ..
git init -b main bisect-demo
cd bisect-demo
mkdir src
```

Создайте в редакторе `src/Statistics.java`:

```java
/** Статистика по массиву целых чисел. */
public class Statistics {

    /** Возвращает сумму элементов массива. */
    public static int sum(int[] values) {
        int result = 0;
        for (int value : values) {
            result += value;
        }
        return result;
    }

    /** Возвращает среднее арифметическое элементов массива. */
    public static double average(int[] values) {
        return (double) sum(values) / values.length;
    }
}
```

Создайте `.gitignore` (файлы проверки не должны попадать в историю — иначе при переключении на старые коммиты они будут заменяться старыми версиями):

```text
out/
Check.java
check.sh
check.ps1
```

Создайте `notes.txt` со строкой `Журнал изменений`, сделайте первый коммит и пометьте заведомо исправное состояние:

```bash
git add .
git commit -m "feat: добавить класс Statistics"
git tag baseline
```

Сделайте шесть «шумовых» коммитов:

```bash
for i in $(seq 1 6); do
  echo "Заметка $i" >> notes.txt
  git commit -qam "docs: заметка $i"
done
```

```powershell
foreach ($i in 1..6) {
  Add-Content -Encoding utf8 notes.txt "Заметка $i"
  git commit -qam "docs: заметка $i"
}
```

Теперь **подложите ошибку**: замените тело метода `sum` на «оптимизированный» вариант и закоммитьте.

```java
    /** Возвращает сумму элементов массива. */
    public static int sum(int[] values) {
        int result = 0;
        for (int i = 1; i < values.length; i++) {
            result += values[i];
        }
        return result;
    }
```

```bash
git commit -am "refactor: переписать суммирование через индексный цикл"
```

Добавьте ещё шесть шумовых коммитов тем же циклом (диапазон `7 12` в Git Bash, `7..12` в PowerShell) и посмотрите на историю: `git log --oneline`. Четырнадцать коммитов, и по сообщениям не догадаться, в каком поломка. Именно так выглядит настоящая история через месяц работы.

### Задание 9.2: Проверочная программа и ручной поиск

Создайте в корне репозитория `Check.java` — он не отслеживается Git и потому переживёт все переключения коммитов:

```java
/** Проверка Statistics: код возврата 0 — всё хорошо, 1 — ошибка. */
public class Check {

    public static void main(String[] args) {
        int[] data = {10, 20, 30, 40};
        int sum = Statistics.sum(data);
        double average = Statistics.average(data);

        if (sum != 100 || Math.abs(average - 25.0) > 1e-9) {
            System.out.println("ПЛОХО: sum=" + sum + ", average=" + average);
            System.exit(1);
        }
        System.out.println("ХОРОШО: sum=" + sum + ", average=" + average);
    }
}
```

Запустите поиск. Git переключит вас на середину диапазона; на каждом шаге повторяйте две команды сборки и проверки и отвечайте `git bisect good` (вывод `ХОРОШО`) или `git bisect bad` (вывод `ПЛОХО`), пока Git не напишет `... is the first bad commit`.

```bash
javac -d out src/Statistics.java Check.java
java -cp out Check                # сейчас ожидается: ПЛОХО: sum=90, average=22.5

git bisect start
git bisect bad                    # текущее состояние сломано
git bisect good baseline          # на метке baseline всё работало
# далее на каждом шаге: javac ... && java -cp out Check, затем git bisect good | bad
git show <хеш-плохого-коммита>
git bisect reset
```

### Задание 9.3: Автоматический поиск

Напишите скрипт-проверку (он тоже не отслеживается Git).

```sh
#!/bin/sh
# check.sh — Git Bash, Linux, macOS
# не собирается — коммит пропускаем (код 125), иначе результат определяет Check
javac -d out src/Statistics.java Check.java || exit 125
java -cp out Check
```

Сохраните `check.sh` с переводами строк LF (в IntelliJ IDEA — переключатель CRLF/LF в статусной строке, в VS Code — индикатор в правом нижнем углу, в Notepad++ — Правка → Конвертация конца строк). При CRLF Git Bash подставит `\r` в аргументы, и проверка будет падать на каждом шаге.

```powershell
# check.ps1 — PowerShell
javac -d out src/Statistics.java Check.java
if ($LASTEXITCODE -ne 0) { exit 125 }
java -cp out Check
exit $LASTEXITCODE
```

```bash
git bisect start HEAD baseline
git bisect run sh check.sh                                                     # Git Bash
git bisect run powershell -NoProfile -ExecutionPolicy Bypass -File check.ps1   # PowerShell
git bisect reset
```

**Ответьте письменно:** (1) Сколько шагов понадобилось Git, чтобы найти виновный коммит среди тринадцати кандидатов (метка `baseline` заведомо исправна), и по какой формуле получается это число? (2) Что означает код возврата 125 в `git bisect run` и зачем он нужен? (3) Что случилось бы, будь `Check.java` закоммичен в репозиторий?

---

## Часть 10: Удалённый репозиторий, push и pull request

Удалённый репозиторий — общий склад: у каждого дома полная мастерская, а на склад свозят готовые детали и оттуда забирают чужие.

### Задание 10.1: Локальный «сервер», push и отклонённый push

Аккаунт для этого задания не нужен: сервером будет обычный каталог.

```bash
cd ../library
git init --bare ../library-server.git
git remote add origin ../library-server.git
git remote -v
git push -u origin main
git push origin --tags
```

Изобразите коллегу: склонируйте репозиторий во второй каталог, допишите в `README.md` строку `Работа над проектом ведётся в ветках feature/*.` и отправьте изменение.

```bash
cd ..
git clone library-server.git library-colleague
cd library-colleague
git commit -am "docs: описать правило именования веток"
git push origin main
```

Вернитесь в свой репозиторий, создайте файл `CONTRIBUTING.md` со строкой `Перед merge request прогоняйте mvn test.` и попробуйте отправить его, не забирая чужие изменения:

```bash
cd ../library
git add CONTRIBUTING.md
git commit -m "docs: добавить правила участия в проекте"
git push origin main              # rejected — non-fast-forward

git fetch origin
git log --oneline HEAD..origin/main       # что нового на сервере
git log --oneline origin/main..HEAD       # что нового у вас
git pull --rebase origin main
git log --oneline --graph -5
git push origin main
```

**Ответьте письменно:** (1) Почему сервер отклонил первый `push`? (2) Что `git pull --rebase` сделал с вашим коммитом и как это видно в `git log`? (3) Почему `git push --force` здесь был бы неправильным решением и чем от него отличается `--force-with-lease`?

### Задание 10.2: GitHub или GitLab и pull request

Создайте через веб-интерфейс github.com или gitlab.com **пустой** репозиторий `library` — без README и `.gitignore`, иначе истории разойдутся. Привяжите его вторым удалённым репозиторием:

```bash
git remote add gh https://github.com/ВАШ-ЛОГИН/library.git
git push -u gh main
git push gh --tags
```

При первой отправке по HTTPS Git попросит авторизоваться: на Windows окно входа откроет Git Credential Manager, на Linux и macOS вместо пароля используется персональный токен доступа из настроек аккаунта. Если создаёте токен на GitHub, сразу выдайте ему и право `workflow` (для fine-grained токена — разрешение Workflows: Read and write): без него часть 11 не отправится на сервер. **Если аккаунт создать не удалось**, дальше везде вместо `gh` подставляйте `origin` (локальный сервер из задания 10.1), pull request заменяется слиянием `git merge --no-ff` с письменным разбором изменений, а конвейер из части 11 проверяется локально командой `mvn verify`.

Оформите изменение по правилам командной работы: выполните `git switch -c feature/genre-field`, добавьте в `Book.java` поле жанра, обновите вызовы конструктора в `LibraryApp` и выведите жанр в списке книг.

```java
public record Book(String title, String author, int year, String genre) {
}

// в LibraryApp.main:
        service.add(new Book("Война и мир", "Толстой", 1869, "роман"));
        service.add(new Book("Мастер и Маргарита", "Булгаков", 1967, "роман"));

// там же, в строке вывода каждой книги — добавьте жанр в конец:
        service.findAll().forEach(book ->
                System.out.println("  " + book.title() + " — " + book.author()
                        + ", " + book.year() + ", " + book.genre()));
```

```bash
javac -d out -sourcepath src/main/java src/main/java/ru/fa/library/LibraryApp.java
java -cp out ru.fa.library.LibraryApp     # в списке книг появился жанр
git commit -am "feat: добавить жанр в модель книги"
git push -u gh feature/genre-field
```

В веб-интерфейсе откройте **pull request** (на GitLab — merge request) из `feature/genre-field` в `main` и опишите его по шаблону:

```text
Что сделано: добавлено поле genre в модель Book.
Зачем: первый шаг к фильтру книг по жанру (история №4 бэклога).
Как проверить: собрать проект и запустить LibraryApp — у каждой книги в выводе появится жанр.
За рамками: поиск по жанру вынесен в отдельную задачу.
```

Обменяйтесь ссылками с соседом по группе: он оставляет минимум два содержательных комментария к вашему коду, вы — к его. После этого слейте pull request кнопкой в интерфейсе и приведите локальный репозиторий в порядок:

```bash
git switch main
git pull gh main
git branch -d feature/genre-field
git push gh --delete feature/genre-field
```

**Ответьте письменно:** (1) Зачем нужен pull request, если технически можно просто выполнить `git push` в `main`? (2) Какие два замечания вы оставили в чужом pull request и почему они сформулированы как замечания к коду, а не к автору? (3) Какие проверки в этом процессе должен выполнять человек, а какие — автоматика?

---

## Часть 11: Конвейер CI/CD для Maven-проекта

Конвейер с контролем качества на заводе: деталь на ленте автоматически проходит замер и проверку, брак отсеивается сразу, а не после того, как из него собрали автомобиль.

### Задание 11.1: Maven-проект и тесты

Структура каталогов уже соответствует Maven (`src/main/java`). Зависимость JUnit 5 и плагин Surefire вы подключали в Практике 10 — повторяем ту же связку, новое здесь только одно: запускать тесты будет не человек, а конвейер. Создайте в корне `pom.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">

    <modelVersion>4.0.0</modelVersion>

    <groupId>ru.fa</groupId>
    <artifactId>library</artifactId>
    <version>1.0.0</version>
    <packaging>jar</packaging>

    <properties>
        <maven.compiler.release>21</maven.compiler.release>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>5.11.4</version>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>3.5.2</version>
            </plugin>
        </plugins>
    </build>
</project>
```

Создайте каталог `src/test/java/ru/fa/library` и в нём `BookServiceTest.java`:

```java
package ru.fa.library;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

class BookServiceTest {

    private final BookService service = new BookService();

    @BeforeEach
    void fillLibrary() {
        service.add(new Book("Война и мир", "Толстой", 1869, "роман"));
        service.add(new Book("Мастер и Маргарита", "Булгаков", 1967, "роман"));
    }

    @Test
    @DisplayName("Поиск находит книгу по фамилии автора без учёта регистра")
    void findsBookByAuthorIgnoringCase() {
        assertEquals("Мастер и Маргарита", service.findBooks("булгаков").get(0).title());
    }

    @Test
    @DisplayName("Поиск по части названия возвращает одну книгу")
    void findsBookByTitlePart() {
        assertEquals(1, service.findBooks("война").size());
    }

    @Test
    @DisplayName("Пустая библиотека: средний год равен нулю, поиск ничего не находит")
    void handlesEmptyLibrary() {
        assertEquals(0.0, new BookService().averageYear());
        assertTrue(new BookService().findBooks("Пушкин").isEmpty());
    }
}
```

Каталог `target/` уже перечислен в `.gitignore` из задания 2.1. Соберите проект и отправьте изменения:

```bash
mvn -q clean test
mvn package
java -cp target/library-1.0.0.jar ru.fa.library.LibraryApp

git add pom.xml src/test
git commit -m "build: перевести проект на Maven и добавить тесты"
git push gh main
```

### Задание 11.2: Файл .gitlab-ci.yml

Создайте в корне репозитория `.gitlab-ci.yml`:

```yaml
# Образ по умолчанию для всех заданий: Maven и JDK 21
default:
  image: maven:3.9-eclipse-temurin-21

variables:
  MAVEN_OPTS: "-Dmaven.repo.local=$CI_PROJECT_DIR/.m2/repository"
  MAVEN_CLI_OPTS: "--batch-mode --errors --show-version"

# Кешируем зависимости, чтобы не качать их при каждом запуске
cache:
  key: maven-repository
  paths:
    - .m2/repository

stages:
  - build
  - test
  - package
  - deploy

compile:
  stage: build
  script:
    - mvn $MAVEN_CLI_OPTS compile

unit-test:
  stage: test
  script:
    - mvn $MAVEN_CLI_OPTS test
  artifacts:
    when: always            # отчёты нужны и тогда, когда тесты упали
    reports:
      junit:
        - target/surefire-reports/TEST-*.xml
    expire_in: 1 week

build-jar:
  stage: package
  script:
    - mvn $MAVEN_CLI_OPTS package -DskipTests
  artifacts:
    paths:
      - target/*.jar
    expire_in: 1 week

deploy-production:
  stage: deploy
  script:
    - echo "Выкладываем релиз $CI_COMMIT_TAG на продуктив"
  environment:
    name: production
  rules:
    # только по тегу вида v1.0.0 и только по нажатию кнопки человеком
    - if: $CI_COMMIT_TAG =~ /^v\d+\.\d+\.\d+$/
      when: manual
```

На **GitLab** синтаксис проверяется заранее в разделе CI/CD → Editor → Validate, а результат запуска виден в CI/CD → Pipelines. На **GitHub** этот файл не запустится, поэтому дополнительно создайте `.github/workflows/build.yml`:

```yaml
name: Сборка и тесты
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with:
          java-version: '21'
          distribution: 'temurin'
          cache: maven
      - run: mvn --batch-mode --show-version verify
```

```bash
git add .gitlab-ci.yml .github
git commit -m "ci: добавить конвейер сборки и тестов"
git push gh main
```

Если GitHub отклонит отправку с сообщением про `workflow` scope, дело не в Git: персональному токену не хватает прав на изменение конвейеров. Выдайте классическому токену галочку `workflow` (fine-grained токену — разрешение Workflows: Read and write) в настройках аккаунта и повторите `git push`. На GitLab такого ограничения нет.

Дождитесь завершения конвейера (вкладка Actions на GitHub, CI/CD на GitLab) и найдите в его выводе строку с числом пройденных тестов.

### Задание 11.3: Красный конвейер

Сломайте один тест намеренно: замените в `findsBookByTitlePart` ожидание `assertEquals(1, ...)` на `assertEquals(2, ...)`.

```bash
git switch -c experiment/red-pipeline
mvn -q test                       # сначала посмотрите, как падение выглядит локально
git commit -am "test: временно сломать ожидание в тесте поиска"
git push -u gh experiment/red-pipeline
```

Откройте pull request из этой ветки в `main` и посмотрите, что показывает платформа: конвейер красный, кнопка слияния предупреждает о непройденных проверках. Сделайте снимок экрана — он нужен в отчёте.

Теперь верните тест в рабочее состояние (`assertEquals(1, ...)`) и убедитесь, что конвейер позеленел. Отправка обязательна: без неё платформа ничего не перезапустит.

```bash
mvn -q test                       # снова зелено
git commit -am "test: вернуть корректное ожидание"
git push gh experiment/red-pipeline
```

Дождитесь зелёного конвейера, закройте pull request **без слияния** (эта ветка была экспериментом) и уберите её:

```bash
git switch main
git branch -D experiment/red-pipeline     # именно -D: ветка не слита в main
git push gh --delete experiment/red-pipeline
```

**Ответьте письменно:** (1) Зачем кешируется каталог `.m2/repository` и почему для этого пришлось менять `MAVEN_OPTS`? (2) Что делает `artifacts:reports:junit` и чем отличается от `artifacts:paths`? (3) Почему `deploy-production` описан с `when: manual`? (4) Что произойдёт с заданиями стадий `package` и `deploy`, если `unit-test` завершится с ошибкой?

---

## Часть 12: Учебный кейс — Agile и Scrum

Scrum — это ритм, как расписание занятий: заранее известно, когда встречаемся, что показываем и когда обсуждаем, что улучшить. Без ритма команда обсуждает всё сразу и не заканчивает ничего. Но прежде чем ставить ритм, нужно понять, ради чего он: расписание само по себе никого не учит.

Выберите **одну** тему из перечня курсовых работ РПД: информационно-справочная система библиотеки, кинотеатра, магазина цифровой техники, ресторана, аэропорта или пиццерии. Все ответы этой части оформите в репозитории — в файле `docs/scrum-case.md`, который в конце нужно закоммитить и отправить на сервер.

```bash
git switch main
mkdir docs
```

### Задание 12.1: Agile до Scrum

Scrum — только один из способов работать гибко, и без ценностей за ним он превращается в набор обязательных совещаний. Начните с основы. Ответы пишите в тот же `docs/scrum-case.md`.

1. Выпишите **четыре ценности** манифеста гибкой разработки в форме «А важнее Б». Поясните своими словами оговорку «не отрицая важности того, что справа» и приведите одну ситуацию из вашего проекта, где правая часть всё-таки перевешивает левую.
2. Опишите, как ваш проект выглядел бы по **каскадной модели**: перечислите этапы и примерные сроки от требований до сдачи. Затем назовите, какой из двенадцати принципов Agile нарушается при такой работе сильнее всего, и к какой конкретной потере это приведёт именно в вашем проекте.
3. Опровергните два заблуждения: «Agile — это отсутствие документации» и «Agile — это просто работать быстрее». На каждое — по примеру из вашего проекта: какая документация вам всё равно понадобится и что ускоряется на самом деле.

**Ответьте письменно:** (1) Почему Agile называют набором ценностей и принципов, а не методологией, и чем тогда является Scrum по отношению к нему? (2) Назовите проект, для которого каскадная модель подошла бы лучше гибкой, и объясните, какое его свойство это определяет.

### Задание 12.2: Команда, роли и бэклог продукта

Опишите в `docs/scrum-case.md`:

1. Состав команды из пяти человек: кто владелец продукта, кто скрам-мастер, кто разработчики. Для каждой роли — две-три обязанности **в вашем проекте**, а не общими словами.
2. Один пример решения владельца продукта и один пример решения команды разработчиков: покажите на них разницу между «что» и «как».
3. Бэклог продукта: **восемь пользовательских историй** в формате «Как …, я хочу …, чтобы …», упорядоченных по ценности, с оценкой в стори-поинтах по ряду Фибоначчи (1, 2, 3, 5, 8, 13).

Для трёх верхних историй допишите критерии приёмки по образцу:

```text
Как администратор системы,
я хочу искать сеанс по названию фильма и дате,
чтобы быстро находить нужный сеанс в расписании на неделю.

Критерии приёмки:
- поиск не учитывает регистр;
- при пустом результате показывается понятное сообщение;
- время ответа не превышает 300 мс на базе из 5000 сеансов.
```

**Ответьте письменно:** (1) Почему скрам-мастер не должен распределять задачи внутри команды? (2) Какая из восьми историй самая рискованная по оценке и почему разброс оценок в команде важнее самой цифры?

### Задание 12.3: Планирование спринта

Спринт длится две недели, средняя скорость команды — **20 стори-поинтов**. Опишите в файле:

1. Цель спринта одной фразой (например: «пользователь может найти сеанс и купить билет»).
2. Бэклог спринта: какие истории вы берёте, чтобы суммарная оценка не превышала 20 поинтов, и почему именно их.
3. Разбивку **одной** взятой истории на четыре-шесть технических задач (сущность и репозиторий, сервис, контроллер, шаблон, тесты) — так, как они будут выглядеть на доске.
4. Что вы **не** берёте в спринт и почему, хотя это тоже нужно.

**Ответьте письменно:** (1) Что произойдёт, если в середине спринта владелец продукта попросит добавить ещё одну историю, и как правильно поступить? (2) Почему стори-поинты нельзя переводить в часы и объявлять план по часам?

### Задание 12.4: События, определение готовности и связь с Git

Допишите в `docs/scrum-case.md`:

1. Таблицу всех **пяти** событий Scrum для вашего проекта: событие, когда проходит, сколько длится, кто участвует, чем заканчивается.
2. Одно отличие обзора спринта от ретроспективы, сформулированное своими словами.
3. Определение готовности (Definition of Done) из шести пунктов, привязанное к вашему процессу; обязательно включите пункты про код-ревью и про зелёный конвейер CI из части 11.
4. Два конкретных действия по итогам воображаемой ретроспективы — с ответственным и сроком.
5. Связку с Git: имена веток для трёх верхних историй бэклога (по соглашению `feature/…`), список проверок, которые конвейер должен пройти до слияния merge request, и пример сообщения коммита, автоматически закрывающего задачу в трекере:

```bash
git commit -m "feat: добавить поиск сеанса по названию фильма

Поиск не учитывает регистр, пустой результат показывает сообщение.

Closes #4"
```

6. Заведите **доску задач** для своего проекта в GitHub Projects (или GitLab Boards, или Trello) со столбцами «Бэклог», «В работе», «Ревью», «Готово». Перенесите туда бэклог спринта из задания 12.3, проставьте столбцу «В работе» WIP-лимит, равный числу разработчиков в команде, и приложите снимок экрана доски. В файле опишите одним абзацем, что именно должно быть выполнено, чтобы карточка перешла из «В работе» в «Ревью», — это и есть «явные правила» из Kanban.

```bash
git add docs/scrum-case.md
git commit -m "docs: описать организацию работы по Scrum для учебного проекта"
git push gh main
```

**Ответьте письменно:** (1) Какую проблему решает определение готовности и что происходит в команде без него? (2) Как определение готовности вашей команды связано с конвейером CI из части 11? (3) Ретроспектива закончилась словами «всё было нормально» — почему это провал и как его исправить? (4) Чем Kanban отличается от Scrum и зачем столбцу нужен WIP-лимит, если он только мешает брать новые задачи?

---

## Часть 13: Контрольные вопросы

Ответьте письменно:

1. Чем распределённая система контроля версий отличается от централизованной? Назовите два следствия для повседневной работы разработчика.
2. Почему Git хранит снимки проекта, а не разницы между версиями? Перечислите четыре типа объектов Git и скажите, что хранит каждый.
3. Что такое индекс (staging area) и зачем он нужен, если можно было бы коммитить прямо из рабочего каталога?
4. Что такое ветка с точки зрения устройства репозитория, что такое `HEAD` и когда возникает состояние detached HEAD?
5. В каком случае Git выполняет слияние быстрой перемоткой? Что даёт флаг `--no-ff` и почему многие команды применяют его всегда?
6. Какие три коммита участвуют в трёхстороннем слиянии и как Git решает, чью версию строки взять?
7. Что означают маркеры `<<<<<<<`, `=======` и `>>>>>>>`, какая часть относится к текущей ветке и почему после удаления маркеров обязательно собрать проект и прогнать тесты?
8. Чем отличаются `git reset --soft`, `--mixed` и `--hard`? Какая из трёх команд по-настоящему опасна и почему?
9. Почему историю, которую уже видели другие, отменяют через `git revert`, а не через `git reset`?
10. В чём разница между `git fetch` и `git pull`? Опишите безопасный порядок получения чужих изменений.
11. Сформулируйте золотое правило rebase и объясните, что именно ломается при его нарушении.
12. Чем `squash` отличается от `fixup` в интерактивном rebase? Что делают команды `reword` и `drop`?
13. Чем `git push --force-with-lease` лучше `git push --force` и в каком единственном сценарии принудительная отправка допустима?
14. Чем `git cherry-pick` отличается от слияния ветки целиком и почему у перенесённого коммита другой хеш?
15. Что хранит reflog, чем он отличается от `git log` и в каком случае не поможет вернуть потерянную работу?
16. Как `git bisect` находит виновный коммит примерно за восемь шагов вместо трёхсот проверок? Что означает код возврата 125 в `git bisect run`?
17. Что попадает в `.gitignore`, а что нет? Почему правило не действует на уже отслеживаемый файл и как это исправить?
18. Почему пароль, попавший в коммит, считается скомпрометированным навсегда? Какова правильная последовательность действий?
19. Зачем нужен `git stash`, если можно сделать временный коммит? В чём разница между `pop` и `apply`?
20. Чем аннотированный тег отличается от легковесного, почему для релизов используют первый и что означают три числа версии по SemVer?
21. Что такое stage, job и runner в GitLab CI? Что произойдёт с последующими стадиями, если задание стадии `test` завершится с ошибкой?
22. Зачем в конвейере кешируют локальный репозиторий Maven и почему для этого меняют `MAVEN_OPTS`? Чем `artifacts:reports:junit` отличается от `artifacts:paths`?
23. Чем непрерывная интеграция отличается от непрерывной доставки, а непрерывная доставка — от непрерывного развёртывания?
24. Назовите три роли Scrum и объясните, кто решает «что делать», а кто — «как делать». Чем обзор спринта отличается от ретроспективы и зачем команде определение готовности?
25. Назовите четыре ценности Agile-манифеста. Чем гибкий подход отличается от каскадной модели и почему Agile — это не отказ от документации и планирования?
26. Чем Kanban отличается от Scrum по ритму, ролям и ключевой метрике? Что такое WIP-лимит и зачем связывать трекер задач с репозиторием?

---

## Результаты занятия

К концу занятия вы должны сдать:

1. Репозиторий `library` со всей историей: минимум 20 коммитов, ветки, коммит слияния, разрешённый вручную конфликт, тег `v1.0.0`, ветка `release/1.0` с перенесённым через `cherry-pick` исправлением.
2. Файл `.gitignore` и объяснение, как из репозитория был убран `application-local.properties`.
3. Вывод `git log --oneline --graph --all --decorate` для репозиториев `library` и `rebase-demo` с пояснением, где видно слияние, а где — перебазирование.
4. Репозиторий `bisect-demo`: хеш и сообщение найденного «плохого» коммита плюс журнал работы `git bisect run`.
5. Ссылку на репозиторий на GitHub или GitLab, ссылку на закрытый pull request и два ваших содержательных комментария в чужом pull request, либо, при работе без аккаунта, — журнал слияния `git merge --no-ff` с письменным разбором изменений и два письменных замечания к коду соседа.
6. Файлы `pom.xml`, `BookServiceTest.java`, `.gitlab-ci.yml` (и `.github/workflows/build.yml`, если работали на GitHub), а также снимки экрана с зелёным и с красным конвейером, либо вывод `mvn verify` для успешной и для падающей сборки.
7. Файл `docs/scrum-case.md` с разбором ценностей Agile и каскадной модели, ролями, бэклогом продукта из восьми историй, бэклогом спринта, таблицей событий, определением готовности и связкой с Git, а также снимок экрана доски задач с WIP-лимитом.
8. Ответы на вопросы из блоков «Ответьте письменно» всех частей.
9. Ответы на контрольные вопросы (1–26).
