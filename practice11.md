# Практическое занятие 11: Паттерны и антипаттерны проектирования

Сегодняшнее занятие устроено не так, как предыдущие. Мы не поднимаем новый сервер и не подключаем новую библиотеку — мы работаем с уже написанным кодом и учимся видеть в нём структуру. Половина заданий начинается словами «вот код, найдите в нём проблему», вторая половина — «а теперь исправьте».

Врач сначала ставит диагноз и только потом лечит. Пропустите первый шаг — и лечение пойдёт наугад: вы начнёте вводить фабрики и стратегии там, где болит совсем другое. Поэтому в каждом задании сперва разбор, и только затем рефакторинг.

Все задания выполняются **строго по порядку**: каждое следующее опирается на каталоги и классы, созданные в предыдущих.

---

## Часть 0: Подготовка рабочего места

### Задание 0.1: Каталог проекта и проверка JDK

Всё занятие проходит на голой Java — без Maven, Spring и внешних зависимостей. Так виднее сами паттерны: ни один фреймворк не делает работу за вас.

**Linux / macOS / Git Bash:**

```bash
mkdir -p patterns-lab/src/ru/fa/patterns/{solid/refactored,singleton,creational,behavioral,io,jdk,antipatterns/refactored}
cd patterns-lab
```

**Windows PowerShell:**

```powershell
"solid/refactored","singleton","creational","behavioral","io","jdk","antipatterns/refactored" |
    ForEach-Object { New-Item -ItemType Directory -Force -Path "patterns-lab/src/ru/fa/patterns/$_" }
cd patterns-lab
```

Создайте `src/ru/fa/patterns/Setup.java`:

```java
package ru.fa.patterns;

public class Setup {
    public static void main(String[] args) {
        System.out.println("Java: " + System.getProperty("java.version"));
        System.out.println("Кодировка вывода: " + System.getProperty("stdout.encoding"));
        System.out.println("Проверка русских букв: Ёжик, объём, щавель");
    }
}
```

Скомпилируйте и запустите:

```bash
javac -encoding UTF-8 -d out -sourcepath src src/ru/fa/patterns/Setup.java
java -cp out ru.fa.patterns.Setup
```

Эти две команды — шаблон на всё занятие; дальше в заданиях будет указано только имя класса. Ключ `-sourcepath src` заставляет `javac` самому найти и собрать все классы, на которые ссылается указанный файл, поэтому достаточно указать класс с `main`. Ключ `-encoding UTF-8` обязателен: без него русские строки ломаются прямо при компиляции. И помните, что **каждый публичный класс живёт в отдельном файле**, имя которого совпадает с именем класса, — это требование языка, а не пожелание.

Если консоль Windows выводит «кракозябры», выполните `chcp 65001`, а при необходимости добавьте флаг: `java -Dstdout.encoding=UTF-8 -cp out ...`.

**Ответьте письменно:** (1) Какая версия JDK у вас установлена и удовлетворяет ли она требованию Java 21? (2) Что вывела строка «Кодировка вывода»? (3) Что произойдёт, если убрать `-sourcepath` и компилировать класс, который ссылается на другой класс проекта?

---

## Часть 1: SOLID — найти нарушения и вылечить

Работаем как приёмная комиссия на код-ревью. Сначала диагноз по каждому подозрительному месту с названием нарушенного принципа, потом лечение. Ответ «тут как-то некрасиво» рецензией не считается.

### Задание 1.1: Диагноз

Сначала создайте вспомогательный класс `src/ru/fa/patterns/solid/MySqlReaderStorage.java` — публичный класс с единственным методом `void insert(String name, String email)`, печатающим `"MySQL INSERT: <имя> / <email>"`. Затем — `src/ru/fa/patterns/solid/ReaderService.java`:

```java
package ru.fa.patterns.solid;

import java.util.ArrayList;
import java.util.List;

// Разбираемый код. В этом файле НИЧЕГО не исправляйте — он нужен для отчёта
public class ReaderService {

    private final List<String> readers = new ArrayList<>();
    private final MySqlReaderStorage storage = new MySqlReaderStorage();   // метка (1)

    public void register(String name, String email, int categoryCode) {    // метка (2)
        if (name == null || name.isBlank()) throw new IllegalArgumentException("Пустое имя");
        readers.add(name);
        storage.insert(name, email);
        String body;                                                       // метка (3)
        if (categoryCode == 1) {
            body = "Вы записаны как обычный читатель, лимит книг 5.";
        } else if (categoryCode == 2) {
            body = "Вы записаны как студент, лимит книг 10.";
        } else if (categoryCode == 3) {
            body = "Вы записаны как преподаватель, лимит книг 30.";
        } else {
            throw new IllegalArgumentException("Неизвестная категория: " + categoryCode);
        }
        System.out.println("SMTP -> " + email + ": " + body);               // метка (4)
    }

    public double fine(int categoryCode, int daysOverdue) {                 // метка (5)
        if (categoryCode == 3) return 0;
        return daysOverdue * 10.0;
    }

    public String toHtml() {                                                // метка (6)
        StringBuilder sb = new StringBuilder("<ul>");
        for (String reader : readers) sb.append("<li>").append(reader).append("</li>");
        return sb.append("</ul>").toString();
    }
}
```

Заполните таблицу — по строке на каждую метку:

| Метка | Что здесь сделано | Какой принцип нарушен | Чем обернётся через полгода |
|-------|-------------------|-----------------------|-----------------------------|
| (1)–(6) | | | |

Образец ответа для метки (1): «сервис сам создаёт конкретную реализацию хранилища — нарушен DIP — подменить хранилище заглушкой в тесте невозможно, каждый тест пойдёт в MySQL».

**Ответьте письменно:** (1) Сколько у `ReaderService` причин для изменения — перечислите их поимённо. (2) Какие метки нарушают сразу два принципа и почему. (3) Какое из шести нарушений опаснее прочих и чем именно.

---

### Задание 1.2: Лечение

Разложите `ReaderService` на классы в пакете `ru.fa.patterns.solid.refactored`. Часть кода дана, остальное пишете вы.

```java
package ru.fa.patterns.solid.refactored;

public record Reader(String name, String email, ReaderCategory category) { }
```

```java
package ru.fa.patterns.solid.refactored;

public enum ReaderCategory {
    REGULAR("обычный читатель", 5, 10.0),
    STUDENT("студент", 10, 5.0),
    TEACHER("преподаватель", 30, 0.0);

    private final String title;
    private final int bookLimit;
    private final double dailyFine;      // рублей за день просрочки

    ReaderCategory(String t, int limit, double fine) { title = t; bookLimit = limit; dailyFine = fine; }

    public String title() { return title; }
    public int bookLimit() { return bookLimit; }
    public double dailyFine() { return dailyFine; }

    // Текст приветствия живёт рядом с данными, а не в цепочке if
    public String welcomeMessage() {
        return "Вы записаны как %s, лимит книг %d.".formatted(title, bookLimit);
    }
}
```

Две абстракции, от которых будет зависеть сервис. Каждая — в своём файле того же пакета, поэтому строка `package` нужна в обеих:

```java
package ru.fa.patterns.solid.refactored;

public interface ReaderStorage {
    void insert(Reader reader);
    int count();
}
```

```java
package ru.fa.patterns.solid.refactored;

public interface Notifier {
    void notify(Reader reader, String message);
}
```

Напишите самостоятельно:

1. `InMemoryReaderStorage implements ReaderStorage` — хранит читателей в списке, печатает `"Сохранён читатель: <имя>"`.
2. `ConsoleNotifier implements Notifier` — печатает `"SMTP -> <email>: <текст>"`.
3. `ReaderRegistrationService` — получает `ReaderStorage` и `Notifier` **через конструктор**; метод `register(Reader reader)` проверяет имя, сохраняет и отправляет `reader.category().welcomeMessage()`.
4. `FineCalculator` — метод `double fine(ReaderCategory category, int daysOverdue)` без единого `if` по категории.
5. `HtmlReaderList` — метод `String render(List<Reader> readers)`.
6. `SolidDemo` с `main`: обходит `ReaderCategory.values()` в цикле, регистрирует по одному читателю на каждую категорию и печатает для неё пеню за 4 дня просрочки; затем печатает HTML-список всех зарегистрированных. Цикл по `values()` здесь принципиален: именно он позволит новой категории появиться в выводе без единой правки демо.

Соберите и запустите `ru.fa.patterns.solid.refactored.SolidDemo`. Затем сделайте контрольное изменение: **добавьте четвёртую категорию `GUEST("гость", 2, 20.0)`** и пересоберите. Правило приёмки: изменён ровно один файл — `ReaderCategory.java`.

**Ответьте письменно:** (1) Сколько файлов пришлось изменить при добавлении `GUEST` и какой принцип это подтверждает? (2) Что даёт получение зависимостей через конструктор при написании теста для `ReaderRegistrationService`? (3) Классов стало заметно больше. Чем оправданы эти лишние строки?

---

### Задание 1.3: LSP и ISP на живом примере

Создайте `src/ru/fa/patterns/solid/LiskovDemo.java`. Классы `Rectangle` и `Square` возьмите из Лекции 11 (пункт 2.3) и вложите в `LiskovDemo` как статические (`static class Rectangle`, `static class Square`). Добавьте клиентский метод и точку входа:

```java
    // Клиентский код написан под Rectangle и про Square ничего не знает
    static void resizeAndCheck(Rectangle rectangle) {
        rectangle.setWidth(5);
        rectangle.setHeight(4);
        System.out.println(rectangle.getClass().getSimpleName()
                + ": ожидали площадь 20, получили " + rectangle.area());
    }

    public static void main(String[] args) {
        resizeAndCheck(new Rectangle());
        resizeAndCheck(new Square());
    }
```

Запустите `ru.fa.patterns.solid.LiskovDemo` и зафиксируйте вывод: вторая строка расходится с ожиданием.

Теперь вылечите оба принципа в пакете `ru.fa.patterns.solid.refactored`:

- **LSP.** Заведите `sealed interface Shape permits Rect, Sq` с методом `int area()` и две реализации-записи: `record Rect(int width, int height)` и `record Sq(int side)`. Напишите `ShapeDemo`, считающий суммарную площадь списка фигур. Сломать контракт теперь нельзя: у записей нет сеттеров.
- **ISP.** «Толстый» интерфейс `Device { print(); scan(); fax(); }` заставлял простой принтер бросать `UnsupportedOperationException` в двух методах из трёх. Разбейте его на три интерфейса по одной роли (`Printer`, `DocScanner`, `FaxSender`), напишите `SimplePrinter` (только печать) и `MultifunctionDevice` (все три роли), а также `DeviceDemo`, вызывающий печать для обоих через переменную типа `Printer`.

**Ответьте письменно:** (1) Какая площадь получилась у `Square` и почему клиентский код при этом нельзя считать ошибочным? (2) Почему неизменяемые объекты нарушают LSP гораздо реже изменяемых? (3) Почему `UnsupportedOperationException` в реализации интерфейса — почти всегда сигнал нарушения ISP?

---

## Часть 2: Singleton тремя способами

Одиночка — это единственный ключ от серверной. Пока ключ один, порядок есть. Но если два сотрудника одновременно увидят, что ключа на доске нет, каждый закажет себе новый — и ключей станет два. Ровно это происходит с наивным синглтоном в многопоточной среде, и сейчас вы увидите это своими глазами.

### Задание 2.1: Стенд для гонки

Создайте `src/ru/fa/patterns/singleton/Counters.java` — класс со счётчиками вызовов конструкторов: три публичных статических поля `NAIVE`, `SAFE` и `ENUM` типа `AtomicInteger` (из `java.util.concurrent.atomic`) и приватный конструктор.

Затем `SingletonRace.java` — стенд: запускает N потоков одновременно и считает, сколько **разных** объектов они получили:

```java
package ru.fa.patterns.singleton;

import java.util.*;
import java.util.concurrent.*;
import java.util.function.Supplier;

public final class SingletonRace {

    private SingletonRace() { }

    public static int distinctInstances(Supplier<Object> factory, int threads) throws Exception {
        // IdentityHashMap сравнивает по ссылке, а не по equals — нам нужны именно разные объекты
        Set<Object> seen = Collections.newSetFromMap(
                Collections.synchronizedMap(new IdentityHashMap<Object, Boolean>()));
        CountDownLatch start = new CountDownLatch(1);
        CountDownLatch done = new CountDownLatch(threads);
        ExecutorService pool = Executors.newFixedThreadPool(threads);
        for (int i = 0; i < threads; i++) {
            pool.submit(() -> {
                try {
                    start.await();                  // все потоки ждут общей отмашки
                    seen.add(factory.get());
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                } finally {
                    done.countDown();
                }
            });
        }
        start.countDown();                          // старт: рвутся с места одновременно
        done.await(10, TimeUnit.SECONDS);
        pool.shutdown();
        pool.awaitTermination(10, TimeUnit.SECONDS);
        return seen.size();
    }
}
```

Способ первый — `NaiveRegistry.java`, ленивый и небезопасный:

```java
package ru.fa.patterns.singleton;

public class NaiveRegistry {
    private static NaiveRegistry instance;

    private NaiveRegistry() {
        Counters.NAIVE.incrementAndGet();
        // Задержка имитирует тяжёлую инициализацию и делает гонку заметной
        try { Thread.sleep(20); } catch (InterruptedException e) { Thread.currentThread().interrupt(); }
    }

    public static NaiveRegistry getInstance() {
        if (instance == null) {
            instance = new NaiveRegistry();
        }
        return instance;
    }
}
```

**Ответьте письменно:** (1) В какой именно момент между проверкой `instance == null` и присваиванием второй поток успевает вклиниться? (2) Зачем в стенде два `CountDownLatch`, а не один? (3) Почему множество построено на `IdentityHashMap`, а не на обычном `HashSet`?

---

### Задание 2.2: Двойная проверка блокировки и enum

Способ второй — `SafeRegistry.java`. Возьмите двойную проверку блокировки из Лекции 11 (пункт 3.1), переименуйте класс в `SafeRegistry`, уберите поле `values` **вместе с методом `get(String)`** — иначе он будет ссылаться на удалённое поле и класс не соберётся: в этом стенде реестр ничего не хранит, нам важен только факт его создания. Останутся `private static volatile SafeRegistry instance`, приватный конструктор и `getInstance()`. В конструктор поставьте те же две строки, что и в наивном варианте:

```java
    private SafeRegistry() {
        Counters.SAFE.incrementAndGet();
        try { Thread.sleep(20); } catch (InterruptedException e) { Thread.currentThread().interrupt(); }
    }
```

Способ третий — `EnumRegistry.java`, за основу берите вариант через `enum` из того же пункта лекции:

```java
package ru.fa.patterns.singleton;

public enum EnumRegistry {
    INSTANCE;

    EnumRegistry() {
        Counters.ENUM.incrementAndGet();
        try { Thread.sleep(20); } catch (InterruptedException e) { Thread.currentThread().interrupt(); }
    }
}
```

Соберите всё в `SingletonDemo.java`:

```java
package ru.fa.patterns.singleton;

public class SingletonDemo {
    public static void main(String[] args) throws Exception {
        int threads = 50;
        System.out.println("Наивный   : разных объектов = "
                + SingletonRace.distinctInstances(NaiveRegistry::getInstance, threads)
                + ", конструктор вызван раз = " + Counters.NAIVE.get());
        System.out.println("С volatile: разных объектов = "
                + SingletonRace.distinctInstances(SafeRegistry::getInstance, threads)
                + ", конструктор вызван раз = " + Counters.SAFE.get());
        System.out.println("enum      : разных объектов = "
                + SingletonRace.distinctInstances(() -> EnumRegistry.INSTANCE, threads)
                + ", конструктор вызван раз = " + Counters.ENUM.get());
    }
}
```

Запустите `ru.fa.patterns.singleton.SingletonDemo` **пять раз подряд** и запишите все результаты. Число объектов у наивного варианта будет разным от запуска к запуску, но единицей оно не окажется почти никогда: пока первый поток спит 20 мс в конструкторе, остальные 49 успевают пройти проверку `instance == null`, и гонка воспроизводится стабильно. Уберите `Thread.sleep(20)` из конструктора `NaiveRegistry`, запустите ещё пять раз — вот теперь результат станет непредсказуемым, иногда честно равным единице. Это и есть самое неприятное свойство гонок: они не воспроизводятся по требованию.

Отдельно уберите слово `volatile` из `SafeRegistry` (задержку в конструктор верните) и снова запустите несколько раз — скорее всего, тест по-прежнему покажет один объект.

**Ответьте письменно:** (1) Сколько объектов создал наивный вариант в каждом из пяти запусков с задержкой и в каждом из пяти без неё — почему разброс отличается? (2) Почему удаление `volatile` не сломало программу на вашей машине и почему это не повод считать такой код правильным? (3) Почему счётчик `ENUM` вынесен в отдельный класс `Counters`, а не сделан статическим полем внутри `EnumRegistry` — что произойдёт, если попробовать?

---

### Задание 2.3: Атака рефлексией

Приватный конструктор — не замок, а табличка «не входить». Проверим. `ReflectionAttack.java`:

```java
package ru.fa.patterns.singleton;

import java.lang.reflect.Constructor;

public class ReflectionAttack {
    public static void main(String[] args) throws Exception {
        NaiveRegistry legal = NaiveRegistry.getInstance();
        Constructor<NaiveRegistry> c = NaiveRegistry.class.getDeclaredConstructor();
        c.setAccessible(true);                                   // обходим private
        System.out.println("Синглтон продублирован: " + (legal != c.newInstance()));
        System.out.println("Конструктор вызван раз: " + Counters.NAIVE.get());
        try {
            Constructor<?> ec = EnumRegistry.class.getDeclaredConstructors()[0];
            ec.setAccessible(true);
            ec.newInstance("HACKED", 1);
            System.out.println("enum удалось продублировать — этого быть не должно");
        } catch (Exception e) {
            System.out.println("enum не поддался: " + e.getClass().getSimpleName() + " — " + e.getMessage());
        }
    }
}
```

Заполните сводную таблицу — по результатам собственных запусков, а не по учебнику. Исключение одно: строку про сериализацию мы в этом стенде не проверяем (ни один класс не реализует `Serializable`), поэтому она и помечена «по материалу лекции».

| Критерий | Наивный ленивый | Двойная проверка + `volatile` | `enum` |
|----------|-----------------|-------------------------------|--------|
| Потокобезопасность (ваш результат) | | | |
| Ленивая инициализация | | | |
| Устойчивость к рефлексии | | | |
| Устойчивость к сериализации (по материалу лекции) | | | |
| Объём кода и удобство тестирования | | | |

**Ответьте письменно:** (1) Какое исключение и с каким сообщением выдала JVM при попытке создать второй экземпляр перечисления? (2) Какой из трёх вариантов вы выберете для реестра настроек и почему? (3) Почему в Spring-приложении ручной Singleton почти никогда не нужен — чем бин со scope `singleton` лучше статического поля?

---

## Часть 3: Фабричный метод и Строитель

Порождающие паттерны — про то, откуда берутся объекты. Аналогия — мебельный цех: клиент не подходит к станку. Он либо называет модель, и цех сам решает, какой станок включить (Фабричный метод), либо заполняет бланк с галочками — цвет, размер, фурнитура — и только в конце жмёт «оформить» (Строитель).

### Задание 3.1: Строитель для книги

Класс `Book` со Строителем разобран в Лекции 11 (пункт 3.4). Перенесите его в `src/ru/fa/patterns/creational/Book.java` (пакет `ru.fa.patterns.creational`) и доработайте:

1. Добавьте поля `int pages` и `List<String> tags`. В `Builder` список объявите сразу инициализированным — `private final List<String> tags = new ArrayList<>();` — иначе книга «без тегов» уронит `List.copyOf(null)` с `NullPointerException`. Методы билдера: `pages(int)` и `tag(String)`, последний добавляет один тег в список и возвращает `this`.
2. Список тегов в конструкторе `Book` копируйте защитно: `this.tags = List.copyOf(builder.tags);`. Все поля остаются `final`, сеттеров нет.
3. Заведите методы доступа `title()`, `author()`, `year()`, `pages()`, `isbn()`, `tags()` — они понадобятся в заданиях 3.2 и 4.1.
4. Расширьте валидацию в `build()`: пустое название, пустой автор, год вне диапазона 1450–2100 и неположительное число страниц дают `IllegalStateException` с понятным сообщением.
5. В `toString()` выводите все поля, например: `"%s — %s (%d), %d с., ISBN %s, теги %s".formatted(...)`.

Напишите `BuilderDemo`, который: (а) собирает три книги — со всеми полями и двумя тегами, без ISBN, без тегов; (б) печатает их; (в) в `try/catch` пытается собрать книгу без автора и печатает текст пойманного `IllegalStateException`; (г) вызывает `book.tags().add("взлом")` в `try/catch` и печатает класс пойманного исключения. Запустите `ru.fa.patterns.creational.BuilderDemo`.

**Ответьте письменно:** (1) Выпишите сигнатуры всех перегрузок конструктора, которые пришлось бы завести без Строителя для шести полей, из которых два необязательные. (2) Что случится, если убрать `List.copyOf` и присвоить `builder.tags` напрямую — как внешний код изменит «неизменяемую» книгу? (3) В каком случае вместо Строителя достаточно обычного `record`?

---

### Задание 3.2: Фабричный метод для выгрузки каталога

Экспорт каталога состоит из неизменной части (собрать текст, записать файл, отчитаться) и переменной (в каком формате форматировать). Переменную часть отдаём подклассу.

```java
package ru.fa.patterns.creational;

import java.util.List;

public interface CatalogFormatter {
    String format(List<Book> books);
    String fileExtension();
}
```

Реализация для CSV — `CsvCatalogFormatter implements CatalogFormatter`: метод `format` собирает `StringBuilder`, начиная со строки-шапки `"title;author;year;pages\n"` и добавляя по строке на книгу через `;`, а `fileExtension()` возвращает `"csv"`.

```java
package ru.fa.patterns.creational;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public abstract class CatalogExporter {

    // Фабричный метод: что именно создать — решает подкласс
    protected abstract CatalogFormatter createFormatter();

    // Неизменная часть алгоритма, общая для всех форматов
    public final Path export(List<Book> books, String baseName) throws IOException {
        CatalogFormatter formatter = createFormatter();
        String content = formatter.format(books);
        Path target = Path.of(baseName + "." + formatter.fileExtension());
        Files.writeString(target, content, StandardCharsets.UTF_8);
        System.out.println("Записан файл " + target.toAbsolutePath() + " (" + content.length() + " символов)");
        return target;
    }
}
```

Обратите внимание: перед вами сразу два паттерна, а не один. `createFormatter()` — **Фабричный метод**: что именно создать, решает подкласс. А сам `export()` — **Шаблонный метод**: базовый класс держит скелет алгоритма (сформатировать, записать файл, отчитаться), подкласс подставляет ровно один шаг и в порядок действий не вмешивается. Именно поэтому `export()` объявлен `final`.

Напишите самостоятельно: `CsvCatalogExporter` (возвращает `new CsvCatalogFormatter()`); `MarkdownCatalogFormatter` (таблица Markdown с шапкой `| Название | Автор | Год |` и строкой-разделителем, расширение `md`); `MarkdownCatalogExporter`; `ExporterDemo`, который собирает билдером четыре книги, выгружает их обоими экспортёрами в `catalog.csv` и `catalog.md`, читает файлы обратно через `Files.readString` и печатает первые две строки каждого.

Запустите `ru.fa.patterns.creational.ExporterDemo` и убедитесь, что файлы созданы (`cat catalog.md`, в PowerShell `Get-Content catalog.md`).

Теперь добавьте **простую фабрику** — это не паттерн GoF, но её постоянно путают с фабричным методом:

```java
package ru.fa.patterns.creational;

public final class CatalogExporters {
    private CatalogExporters() { }

    public static CatalogExporter of(String format) {
        return switch (format.toLowerCase()) {
            case "csv" -> new CsvCatalogExporter();
            case "md", "markdown" -> new MarkdownCatalogExporter();
            default -> throw new IllegalArgumentException("Неизвестный формат: " + format);
        };
    }
}
```

**Ответьте письменно:** (1) Чтобы добавить формат JSON, какие файлы придётся создать и какие изменить — сначала для варианта с фабричным методом, затем для варианта с `CatalogExporters.of`. (2) Какой из двух вариантов соблюдает OCP и почему второй всё равно широко применяется? (3) Почему метод `export` объявлен `final` — какой инвариант Шаблонного метода это защищает и что сломается, если подкласс его переопределит?

---

## Часть 4: Стратегия и Наблюдатель

Стратегия — это тарифы в такси: маршрут один, а считают по-разному. Наблюдатель — рассылка библиотеки: она не знает поимённо, кто читает её письма, а подписчик может отписаться в любой момент.

### Задание 4.1: Стратегия — расчёт пени

```java
package ru.fa.patterns.behavioral;

@FunctionalInterface
public interface FinePolicy {
    double amount(int daysOverdue);
}
```

Перечисление `FineTariff` (в своём файле) хранит по стратегии на тариф:

```java
package ru.fa.patterns.behavioral;

public enum FineTariff {
    REGULAR(FineTariff::regularFine),
    STUDENT(FineTariff::studentFine);
    // TODO: TEACHER — пеня всегда 0
    // TODO: VIP — первые GRACE_DAYS дней бесплатно, дальше двойная ставка

    private static final double DAILY_RATE = 10.0;
    private static final int GRACE_DAYS = 3;

    private final FinePolicy policy;

    FineTariff(FinePolicy policy) { this.policy = policy; }

    // Правила вынесены в статические методы: читать статическое поле
    // прямо из объявления константы перечисления нельзя
    private static double regularFine(int days) { return days * DAILY_RATE; }
    private static double studentFine(int days) { return days * DAILY_RATE / 2; }

    public double fineFor(int daysOverdue) { return policy.amount(daysOverdue); }
}
```

Допишите два тарифа, отмеченные `TODO`, и напишите `StrategyDemo`, который:

1. Печатает таблицу: для каждого тарифа — пеня за 0, 2, 5 и 30 дней просрочки.
2. Показывает подмену стратегии на лету: заводит переменную `FinePolicy current`, присваивает ей сначала `days -> 0`, затем `days -> days * 100`, и печатает результат обоих вариантов для 5 дней.
3. Демонстрирует, что `Comparator` — тоже стратегия: метод `printSorted(List<Book> books, String title, Comparator<Book> order)` печатает книги в заданном порядке. Вызовите его трижды — по названию, по году и по числу страниц по убыванию. Класс `Book` импортируйте из `ru.fa.patterns.creational`.

**Ответьте письменно:** (1) Что нужно изменить, чтобы добавить тариф «пенсионер», и какие файлы это затронет? (2) Что даёт аннотация `@FunctionalInterface` помимо документации? (3) Где в задании стратегию выбирает клиент, а где она зашита в перечисление — какой вариант гибче и чем платит за гибкость?

---

### Задание 4.2: Наблюдатель и его классическая ловушка

Издатель и интерфейс подписчика — каждый в своём файле пакета `ru.fa.patterns.behavioral`:

```java
package ru.fa.patterns.behavioral;

@FunctionalInterface
public interface LoanListener {
    void onIssued(String reader, String title);
}
```

```java
package ru.fa.patterns.behavioral;

import java.util.*;

public class Library {
    private final List<LoanListener> listeners = new ArrayList<>();

    public void subscribe(LoanListener listener) { listeners.add(listener); }
    public void unsubscribe(LoanListener listener) { listeners.remove(listener); }

    public void issue(String reader, String title) {
        System.out.println("Выдана книга «" + title + "» читателю " + reader);
        for (LoanListener listener : listeners) {
            listener.onIssued(reader, title);       // рассылка уведомлений
        }
    }
}
```

Напишите `ObserverDemo`. Порядок подписки важен, соблюдайте его.

1. **Первым** подпишите «разового» слушателя, который отписывается прямо внутри обработчика. Он должен быть анонимным классом, иначе не получится сослаться на `this`:

```java
Library library = new Library();

LoanListener oneShot = new LoanListener() {
    @Override public void onIssued(String reader, String title) {
        System.out.println("[разовый] сработал и отписывается");
        library.unsubscribe(this);      // здесь и ломается перебор списка
    }
};
library.subscribe(oneShot);
```

2. Затем подпишите лямбдами ещё двух слушателей: журнал выдач и счётчик (счётчик держите в `AtomicInteger`, потому что лямбда не может менять локальную переменную).
3. Вызовите `library.issue("Иванов", "Чистый код")` — вы получите `ConcurrentModificationException`. Сохраните трассировку стека в отчёт.
4. Почините `Library`: перебирайте копию (`new ArrayList<>(listeners)`) либо храните слушателей в `CopyOnWriteArrayList`. Запустите снова и убедитесь, что отработали все три слушателя.
5. Добавьте слушателя, который бросает `RuntimeException` с текстом `"внешний сервис недоступен"`, и подпишите его **вторым — сразу после разового, до журнала и счётчика**. Место в списке здесь и есть суть эксперимента: рассылка идёт по порядку подписки, поэтому все, кто стоит после упавшего, уведомления не получат. Пересоберите, вызовите `issue()` и убедитесь: журнал и счётчик молчат, а исключение вылетает наружу из `issue()` в `main`. Затем сделайте рассылку устойчивой — оберните вызов каждого слушателя в `try/catch` с печатью предупреждения `"[!] слушатель упал: <сообщение>"` — и убедитесь, что теперь уведомление получают все четверо, а падение второго умещается в одну строку предупреждения.

**Ответьте письменно:** (1) Почему исключение возникает именно при отписке первого слушателя, а при отписке предпоследнего программа отработает молча — и чем второй случай опаснее? (2) Чем `CopyOnWriteArrayList` отличается от копирования списка на каждую рассылку и когда какой вариант уместен? (3) Какой принцип SOLID стоит за словами «добавление новой реакции не требует правки `Library`»?

---

## Часть 5: Декоратор поверх стандартных потоков

Посылка в пункте выдачи — готовый декоратор: товар обёрнут в пузырчатую плёнку, плёнка в коробку, коробка заклеена скотчем и подписана наклейкой. Каждый слой добавляет свойство, но посылка остаётся посылкой — её всё так же можно нести. Ровно так устроены потоки в `java.io`.

### Задание 5.1: Цепочка из стандартных классов

```java
package ru.fa.patterns.io;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.zip.GZIPInputStream;
import java.util.zip.GZIPOutputStream;

public class StreamChainDemo {

    private static final int LINES = 1000;

    public static void main(String[] args) throws IOException {
        Path plain = Path.of("catalog.txt");
        Path packed = Path.of("catalog.txt.gz");

        // Цепочка на запись: символы -> байты -> сжатие -> файл
        try (Writer writer = new BufferedWriter(new OutputStreamWriter(
                new GZIPOutputStream(new FileOutputStream(packed.toFile())), StandardCharsets.UTF_8))) {
            for (int i = 1; i <= LINES; i++) writer.write("Книга №" + i + "; автор Иванов; 2024\n");
        }
        // То же самое без сжатия — для сравнения размеров
        try (Writer writer = Files.newBufferedWriter(plain, StandardCharsets.UTF_8)) {
            for (int i = 1; i <= LINES; i++) writer.write("Книга №" + i + "; автор Иванов; 2024\n");
        }
        System.out.println("Без сжатия: " + Files.size(plain) + " байт");
        System.out.println("Со сжатием: " + Files.size(packed) + " байт");

        // Цепочка на чтение — зеркальная
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(
                new GZIPInputStream(new FileInputStream(packed.toFile())), StandardCharsets.UTF_8))) {
            System.out.println("Первая строка из архива: " + reader.readLine());
        }
    }
}
```

Запустите `ru.fa.patterns.io.StreamChainDemo` и разберите цепочку по слоям:

| Класс в цепочке | Роль | Паттерн | Что добавляет |
|-----------------|------|---------|---------------|
| `FileOutputStream` | источник/приёмник | — | |
| `GZIPOutputStream` | | | |
| `OutputStreamWriter` | | | |
| `BufferedWriter` | | | |

**Ответьте письменно:** (1) Какие размеры файлов получились и во сколько раз сжатие уменьшило объём? (2) Какой класс в цепочке — Адаптер, а не Декоратор, и по какому признаку вы это определили? (3) Что произойдёт, если не закрыть `Writer`, — почему архив окажется битым, а обычный файл, скорее всего, нет?

---

### Задание 5.2: Собственные декораторы

```java
package ru.fa.patterns.io;

import java.io.*;

public class CountingOutputStream extends FilterOutputStream {
    private long count;

    public CountingOutputStream(OutputStream out) { super(out); }

    @Override public void write(int b) throws IOException {
        out.write(b);
        count++;
    }

    @Override public void write(byte[] b, int off, int len) throws IOException {
        out.write(b, off, len);     // пишем блоком: FilterOutputStream разложил бы массив на байты
        count += len;
    }

    public long count() { return count; }
}
```

```java
package ru.fa.patterns.io;

import java.io.*;
import java.util.Locale;

public class UpperCaseWriter extends FilterWriter {

    public UpperCaseWriter(Writer out) { super(out); }

    @Override public void write(int c) throws IOException {
        super.write(Character.toUpperCase(c));
    }

    @Override public void write(char[] cbuf, int off, int len) throws IOException {
        String upper = new String(cbuf, off, len).toUpperCase(Locale.ROOT);
        super.write(upper, 0, upper.length());
    }

    @Override public void write(String str, int off, int len) throws IOException {
        String upper = str.substring(off, off + len).toUpperCase(Locale.ROOT);
        super.write(upper, 0, upper.length());
    }
}
```

Напишите `DecoratorDemo`, который собирает матрёшку с двумя счётчиками на разных уровнях:

```
OutputStreamWriter -> CountingOutputStream (считает исходные байты)
                   -> GZIPOutputStream
                   -> CountingOutputStream (считает сжатые байты)
                   -> FileOutputStream("counted.gz")
```

Запишите те же 1000 строк, закройте поток (иначе `GZIPOutputStream` не допишет хвост архива) и напечатайте оба счётчика с коэффициентом сжатия. Затем отдельно запишите файл через `new BufferedWriter(new UpperCaseWriter(...))` и прочитайте результат обратно.

**Ответьте письменно:** (1) Сколько байт насчитал внешний счётчик и сколько внутренний, почему числа отличаются? (2) Почему в `CountingOutputStream` пришлось переопределить и `write(int)`, и `write(byte[], int, int)` — что будет с производительностью, если оставить только первый? (3) Сколько классов понадобилось бы, чтобы получить наследованием все комбинации «буферизация × сжатие × подсчёт × верхний регистр»?

---

### Задание 5.3: Порядок обёрток и декоратор в коллекциях

Два коротких эксперимента в классе `WrapOrderDemo`.

1. **Порядок слоёв.** Запишите строку `"Библиотека"` двумя цепочками — `new UpperCaseWriter(new BufferedWriter(w))` и `new BufferedWriter(new UpperCaseWriter(w))` — и сравните файлы. Объясните, почему здесь результат одинаковый, а для пары «шифрование + сжатие» порядок стал бы критичным.
2. **Декоратор в коллекциях.** Заведите изменяемый `List<String> original` из двух книг и оберните его: `List<String> readOnly = Collections.unmodifiableList(original);`. Поймайте `UnsupportedOperationException` при попытке `readOnly.add("взлом")` и напечатайте класс исключения. Затем добавьте книгу в **оригинал** (`original.add("Совершенный код")`) и напечатайте `readOnly`.

**Ответьте письменно:** (1) Что напечатала последняя строка и почему `unmodifiableList` не даёт настоящей неизменяемости? (2) Чем `List.copyOf(original)` отличается от `Collections.unmodifiableList(original)` — вспомните задание 3.1. (3) Здесь обёртка отнимает возможность, а не добавляет. Остаётся ли это Декоратором и почему?

---

## Часть 6: Паттерны в знакомом коде JDK и Spring

После курса ботаники двор перестаёт быть «зелёным фоном»: во дворе растут клён, липа и рябина. С паттернами то же самое — код, который вы пишете с первой лекции, вдруг оказывается размечен именами.

### Задание 6.1: Опознание по фрагменту

Для каждого из десяти фрагментов назовите паттерн, его группу (порождающий, структурный, поведенческий) и признак, по которому вы его узнали. Ответ оформите таблицей.

```java
// 1
BufferedReader reader = new BufferedReader(
        new InputStreamReader(new FileInputStream("data.txt"), StandardCharsets.UTF_8));
// 2
books.sort(Comparator.comparing(Book::year).thenComparing(Book::title));
// 3
HttpRequest request = HttpRequest.newBuilder().uri(URI.create("https://example.org")).GET().build();
// 4
Integer cached = Integer.valueOf(100);
// 5
executorService.submit(() -> System.out.println("задача"));
// 6
Files.walkFileTree(Path.of("src"), myFileVisitor);
// 7
for (String tag : book.tags()) { System.out.println(tag); }
// 8
List<String> asList = Arrays.asList(array);
// 9
Runtime.getRuntime().availableProcessors();
// 10
DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
```

**Ответьте письменно:** (1) Какие два фрагмента реализуют разные паттерны, хотя устроены похоже, и в чём разница намерений? (2) Во фрагменте 1 паттерна два — назовите оба и укажите отвечающий за каждый класс; какую роль играет третий класс, `FileInputStream`? (3) Почему `for-each` из фрагмента 7 считается паттерном, хотя в коде нет ни одного нового класса?

---

### Задание 6.2: Приспособленец, который можно потрогать

```java
package ru.fa.patterns.jdk;

public class FlyweightDemo {
    public static void main(String[] args) {
        Integer a = 127, b = 127;
        Integer c = 128, d = 128;
        System.out.println("127 == 127 : " + (a == b));
        System.out.println("128 == 128 : " + (c == d));
        System.out.println("127 equals 127 : " + a.equals(b));

        String s1 = "библиотека";
        String s3 = new String("библиотека");
        System.out.println("литералы: " + (s1 == "библиотека"));
        System.out.println("new String: " + (s1 == s3));
        System.out.println("после intern(): " + (s1 == s3.intern()));
    }
}
```

Запустите обычным способом, а затем с увеличенным кешем автоупаковки:

```bash
java -cp out ru.fa.patterns.jdk.FlyweightDemo
java -XX:AutoBoxCacheMax=1000 -cp out ru.fa.patterns.jdk.FlyweightDemo
```

Если ваша JVM не приняла флаг `-XX:AutoBoxCacheMax`, используйте равнозначный вариант `java -Djava.lang.Integer.IntegerCache.high=1000 -cp out ru.fa.patterns.jdk.FlyweightDemo`.

**Ответьте письменно:** (1) Какая строка вывода изменилась после запуска с флагом и почему? (2) Что здесь внутреннее, а что внешнее состояние приспособленца? (3) Какой практический вывод про сравнение объектов-обёрток через `==` следует из эксперимента?

---

### Задание 6.3: Заместитель своими руками

Интерфейс и его «медленная» реализация — каждый в своём файле пакета `ru.fa.patterns.jdk`, поэтому строка `package` нужна в обоих:

```java
package ru.fa.patterns.jdk;

public interface BookRepository {
    String findTitle(long id);
}
```

```java
package ru.fa.patterns.jdk;

public class SlowBookRepository implements BookRepository {
    @Override public String findTitle(long id) {
        try { Thread.sleep(100); } catch (InterruptedException e) { Thread.currentThread().interrupt(); }
        return "Книга №" + id;                      // имитация тяжёлого запроса в БД
    }
}
```

```java
package ru.fa.patterns.jdk;

import java.lang.reflect.Proxy;

public class ProxyDemo {
    public static void main(String[] args) {
        BookRepository real = new SlowBookRepository();

        // Заместитель создаётся в рантайме: ни одного написанного руками класса-обёртки
        BookRepository logged = (BookRepository) Proxy.newProxyInstance(
                BookRepository.class.getClassLoader(),
                new Class<?>[]{BookRepository.class},
                (proxy, method, methodArgs) -> {
                    long start = System.nanoTime();
                    Object result = method.invoke(real, methodArgs);
                    System.out.println("[proxy] " + method.getName() + " занял "
                            + (System.nanoTime() - start) / 1_000_000 + " мс");
                    return result;
                });

        System.out.println(logged.findTitle(1));
        System.out.println(logged.findTitle(1));
        System.out.println("Класс заместителя: " + logged.getClass().getName());
    }
}
```

Доработайте: добавьте в обработчик `Map<Long, String> cache` и возвращайте закешированное значение без обращения к оригиналу. Второй вызов `findTitle(1)` должен уложиться в 0 мс.

Затем заполните таблицу по своему проекту из Практического занятия 7 и материалу Лекции 11:

| Паттерн | Механизм Spring | Что это даёт |
|---------|-----------------|--------------|
| Одиночка, Прототип | | |
| Фабричный метод, Строитель | | |
| Заместитель, Фасад | | |
| Шаблонный метод, Стратегия | | |
| Наблюдатель, Цепочка обязанностей | | |

**Ответьте письменно:** (1) Что напечатала строка «Класс заместителя» и почему это имя не совпадает ни с одним написанным вами классом? (2) Как этот эксперимент объясняет, почему `@Transactional` не срабатывает при вызове метода изнутри того же класса (Лекция 7)? (3) Почему любой бин, внедряемый через интерфейс, можно считать Стратегией — и кто здесь «клиент, выбирающий алгоритм»?

---

## Часть 7: Антипаттерны и рефакторинг

Убрать квартиру за один вечер не выходит: сил хватает ровно на то, чтобы переложить хлам из угла в угол. Работает другой подход — по одной полке, со списком, и после каждой полки проверять, что ничего не потерялось. Рефакторинг устроен так же.

### Задание 7.1: Разбор пациента

Создайте `src/ru/fa/patterns/antipatterns/LibraryManager.java`:

```java
package ru.fa.patterns.antipatterns;

import java.util.*;

// Разбираемый код. Он работает, но содержит сразу несколько антипаттернов
public class LibraryManager {

    private final List<String[]> books = new ArrayList<>();      // {название, автор, год}
    private final List<String[]> readers = new ArrayList<>();    // {имя, категория}
    private final Map<String, String> issued = new HashMap<>();  // название -> имя читателя

    private int legacyCounter = 0;              // осталось после переезда с версии 1.0
    // public void exportToExcel() { старый код выгрузки, больше не вызывается }

    public void addBook(String title, String author, int year) {
        if (title != null) {
            if (!title.isBlank()) {
                if (author != null && !author.isBlank()) {
                    if (year > 1450 && year < 2100) {
                        books.add(new String[]{title, author, String.valueOf(year)});
                        System.out.println("Добавлена книга: " + title);
                    } else {
                        System.out.println("Ошибка: год " + year + " вне диапазона");
                    }
                } else {
                    System.out.println("Ошибка: не указан автор");
                }
            } else {
                System.out.println("Ошибка: пустое название");
            }
        } else {
            System.out.println("Ошибка: название равно null");
        }
    }

    public void addReader(String name, int category) {
        readers.add(new String[]{name, String.valueOf(category)});
        System.out.println("Зарегистрирован читатель: " + name);
    }

    public void issue(String title, String reader) {
        if (issued.containsKey(title)) {
            System.out.println("Книга «" + title + "» уже на руках");
            return;
        }
        issued.put(title, reader);
        System.out.println("Выдана книга «" + title + "» читателю " + reader);
        System.out.println("SMTP -> " + reader + "@example.com: вы взяли книгу «" + title + "»");
    }

    public double fine(int category, int daysOverdue) {
        if (category == 3) return 0;
        if (category == 2) return daysOverdue * 10.0 * 0.5;
        return daysOverdue * 10.0;
    }

    public double averageBookYear() {
        double sum = 0;
        for (String[] book : books) sum += Integer.parseInt(book[2]);
        return books.isEmpty() ? 0 : sum / books.size();
    }

    public double averageReaderCategory() {
        double sum = 0;
        for (String[] reader : readers) sum += Integer.parseInt(reader[1]);
        return readers.isEmpty() ? 0 : sum / readers.size();
    }

    public String reportHtml() {
        StringBuilder sb = new StringBuilder("<table>");
        for (String[] book : books) {
            sb.append("<tr><td>").append(book[0]).append("</td><td>")
              .append(book[1]).append("</td><td>").append(book[2]).append("</td></tr>");
        }
        return sb.append("</table>").toString();
    }

    public void backup() {
        System.out.println("Резервная копия: книг " + books.size() + ", читателей " + readers.size());
    }
}
```

И `LibraryManagerDemo.java`:

```java
package ru.fa.patterns.antipatterns;

public class LibraryManagerDemo {
    public static void main(String[] args) {
        LibraryManager manager = new LibraryManager();
        manager.addBook("Чистый код", "Роберт Мартин", 2008);
        manager.addBook("Рефакторинг", "Мартин Фаулер", 1999);
        manager.addBook("", "Автор", 2020);
        manager.addBook("Книга из будущего", "Автор", 2200);
        manager.addReader("Иванов", 1);
        manager.addReader("Петрова", 2);
        manager.addReader("Сидоров", 3);
        manager.issue("Чистый код", "Иванов");
        manager.issue("Чистый код", "Петрова");
        System.out.printf("Пеня за 4 дня: обычный %.2f, студент %.2f, преподаватель %.2f%n",
                manager.fine(1, 4), manager.fine(2, 4), manager.fine(3, 4));
        System.out.printf("Средний год книг: %.2f%n", manager.averageBookYear());
        System.out.printf("Средняя категория: %.2f%n", manager.averageReaderCategory());
        System.out.println(manager.reportHtml());
        manager.backup();
    }
}
```

Найдите **не менее шести** антипаттернов и оформите таблицу «антипаттерн — где именно (метод) — чем вреден — чем лечится». Ищите как минимум: God Object, Spaghetti Code, Magic Numbers, Copy-Paste Programming, Lava Flow и смешение слоёв (отправка почты внутри бизнес-операции). Отдельно разберите приём, который в Лекции 11 не назывался: доменные данные здесь хранятся в `String[]` и `int` вместо собственных типов. Смысл поля виден только по комментарию, год превращается в строку и обратно через `Integer.parseInt`, а компилятор не может помешать перепутать `book[0]` с `book[1]`. В литературе это называют одержимостью примитивами (primitive obsession); по сути это частный случай Big Ball of Mud — слои и смысл данных размыты. Лечится записями: `record BookRecord(String title, String author, int year)`.

**Ответьте письменно:** (1) Сколько у класса ответственностей — перечислите их. (2) Какие числа в коде магические и что означает каждое? (3) Что придётся править, если завтра у книги появится жанр, — в скольких методах?

---

### Задание 7.2: Характеризующий снимок поведения

Тестов у нас нет, поэтому роль теста сыграет вывод программы. Зафиксируйте поведение **до** правок:

```bash
javac -encoding UTF-8 -d out -sourcepath src src/ru/fa/patterns/antipatterns/LibraryManagerDemo.java
java -Dstdout.encoding=UTF-8 -cp out ru.fa.patterns.antipatterns.LibraryManagerDemo > before.txt
cat before.txt
```

**Windows PowerShell:**

```powershell
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
javac -encoding UTF-8 -d out -sourcepath src src/ru/fa/patterns/antipatterns/LibraryManagerDemo.java
java -Dstdout.encoding=UTF-8 -cp out ru.fa.patterns.antipatterns.LibraryManagerDemo | Out-File -Encoding utf8 before.txt
Get-Content before.txt
```

**При перенаправлении вывода в файл флаг `-Dstdout.encoding=UTF-8` обязателен.** В консоли Java подстраивается под её кодировку, а вот когда вывод уходит в файл или в конвейер, она берёт системную кодировку (на русской Windows — `windows-1251`), и в `before.txt` попадут «кракозябры». Строка `[Console]::OutputEncoding` нужна по той же причине с другой стороны: она заставляет PowerShell читать поток дочернего процесса как UTF-8. И последнее: `before.txt` и `after.txt` создавайте **одним и тем же способом** — `Out-File -Encoding utf8` в Windows PowerShell 5.1 дописывает в начало файла BOM, и файл, записанный иначе, побайтно с ним не совпадёт.

Этот файл — эталон. После рефакторинга вывод обязан совпасть строка в строку.

**Ответьте письменно:** (1) Почему рефакторинг без зафиксированного поведения считается лотереей? (2) Чем такой снимок хуже настоящих тестов JUnit из Занятия 10 и когда он всё-таки оправдан? (3) Вывод этой программы полностью детерминирован — проверьте, запустив её трижды. Какой метод пришлось бы добавить в `LibraryManager` (и вызвать из демо), чтобы вывод стал зависеть от порядка обхода `HashMap issued`? Напишите его сигнатуру и объясните, чем такой метод опасен для эталонного снимка.

---

### Задание 7.3: Рефакторинг по шагам

Работайте в пакете `ru.fa.patterns.antipatterns.refactored`. **После каждого шага** пересобирайте проект и сверяйтесь с эталоном. Шаг, после которого вывод изменился, разбирайте сразу, а не в конце.

| Шаг | Что сделать | Против чего |
|-----|-------------|-------------|
| 1 | Переписать `addBook` на ранние возвраты: четыре проверки, четыре выхода, нулевая вложенность | Spaghetti Code |
| 2 | Ввести константы `MIN_YEAR`, `MAX_YEAR`, `DAILY_FINE`, `STUDENT_DISCOUNT` и перечисление `ReaderCategory` с явным кодом вместо `int` (см. ниже) | Magic Numbers |
| 3 | Ввести `record BookRecord(String title, String author, int year)` и `record ReaderRecord(String name, ReaderCategory category)`; массивы `String[]` и `Integer.parseInt` исчезают | Одержимость примитивами |
| 4 | Свернуть два метода-близнеца в обобщённый (см. код ниже) | Copy-Paste Programming |
| 5 | Разложить God Object на классы: `BookCatalog`, `ReaderRegistry`, `LoanService`, `FineCalculator`, `HtmlCatalogReport`, `BackupService` | God Object |
| 6 | Завести интерфейс `Notifier` с методом `notify(String reader, String message)` и реализацию `ConsoleNotifier`; `LoanService` получает его через конструктор | Нарушение DIP |
| 7 | Удалить `legacyCounter` и закомментированный `exportToExcel` | Lava Flow |

Перечисление для шага 2. Числовой код задайте **явно**, а не через `ordinal()`: эталонная строка «Средняя категория: 2,00» получена на кодах 1, 2, 3, и опираться здесь на порядок объявления констант — то самое сцепление с числом, от которого шаг 2 как раз избавляет.

```java
package ru.fa.patterns.antipatterns.refactored;

public enum ReaderCategory {
    REGULAR(1), STUDENT(2), TEACHER(3);

    private final int code;

    ReaderCategory(int code) { this.code = code; }

    public int code() { return code; }
}
```

Обобщённый метод для шага 4:

```java
import java.util.function.ToDoubleFunction;   // не забудьте импорт

public static <T> double average(List<T> items, ToDoubleFunction<T> metric) {
    return items.stream().mapToDouble(metric).average().orElse(0);
}
// Вызовы: average(books, BookRecord::year) и average(readers, r -> r.category().code())
```

Напишите `RefactoredDemo` с тем же сценарием, что и `LibraryManagerDemo`, и сравните вывод:

```bash
javac -encoding UTF-8 -d out -sourcepath src src/ru/fa/patterns/antipatterns/refactored/RefactoredDemo.java
java -Dstdout.encoding=UTF-8 -cp out ru.fa.patterns.antipatterns.refactored.RefactoredDemo > after.txt
diff before.txt after.txt && echo "Поведение не изменилось"
```

**Windows PowerShell:**

```powershell
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
javac -encoding UTF-8 -d out -sourcepath src src/ru/fa/patterns/antipatterns/refactored/RefactoredDemo.java
java -Dstdout.encoding=UTF-8 -cp out ru.fa.patterns.antipatterns.refactored.RefactoredDemo | Out-File -Encoding utf8 after.txt
Compare-Object (Get-Content before.txt) (Get-Content after.txt)
```

Команду `javac` пропускать нельзя: без неё вы сравните эталон со старой сборкой и получите либо `Error: Could not find or load main class`, либо чужой вывод. Кодировку задавайте теми же двумя способами, что и в задании 7.2, — иначе `after.txt` разойдётся с `before.txt` на всех русских буквах, хотя поведение программы не менялось.

Пустой вывод `diff` или `Compare-Object` означает, что рефакторинг прошёл чисто. Оформите журнал: «шаг — что сделано — какой антипаттерн устранён — какой принцип соблюдён — вывод совпал».

**Ответьте письменно:** (1) На каком шаге вывод разошёлся с эталоном (если разошёлся) и что было причиной? (2) Какой шаг дал наибольший выигрыш в читаемости, а какой — в тестируемости; это один и тот же шаг? (3) Строк кода стало больше. Почему это не аргумент против рефакторинга?

---

### Задание 7.4: Свой код под тем же микроскопом

Откройте любую свою работу с предыдущих занятий — проект из Занятия 6, 7 или 8. Найдите в нём **два** антипаттерна из списка Лекции 11 и оформите по каждому: фрагмент кода (5–20 строк) с указанием файла; название антипаттерна и признак опознания; план лечения (какой рефакторинг, какой паттерн, какой принцип SOLID восстанавливается); переписанный фрагмент.

Если в своих работах ничего не нашли, возьмите чужой код и объясните письменно, по каким признакам вы убедились, что ваш код чист.

**Ответьте письменно:** (1) Какие два антипаттерна вы нашли и что подталкивало писать именно так? (2) Какой из двух чинили бы первым и почему? (3) Какой антипаттерн из Лекции 11 кажется вам самым частым в учебных проектах?

---

## Часть 8: Контрольные вопросы

Ответьте письменно:

1. Из каких четырёх элементов состоит описание паттерна? Почему паттерн — это не готовый код для копирования?
2. На какие три группы делятся паттерны «банды четырёх» и на какой вопрос отвечает каждая?
3. Что такое избыточное усложнение (over-engineering)? Сформулируйте правило трёх и принцип YAGNI.
4. Сформулируйте принцип единственной ответственности. Как проверить, что причин для изменения несколько?
5. Сформулируйте принцип открытости/закрытости. Какая конструкция чаще всего сигнализирует о его нарушении?
6. Сформулируйте принцип подстановки Лисков. Разберите на примере квадрата и прямоугольника, почему математическое «является» не совпадает с программным.
7. Сформулируйте принцип разделения интерфейсов. Почему `UnsupportedOperationException` в реализации — симптом его нарушения?
8. Сформулируйте принцип инверсии зависимостей. В чём разница между DIP, DI и IoC?
9. Какие три способа реализации Одиночки вы применили? Сравните их по потокобезопасности, лености и устойчивости к рефлексии.
10. Зачем в двойной проверке блокировки нужно `volatile`? Что именно может пойти не так без него?
11. Чем Фабричный метод отличается от Абстрактной фабрики и чем от простой фабрики со `switch` с точки зрения OCP?
12. Какую проблему решает Строитель? Что такое телескопический конструктор и чем он плох?
13. Почему объект, собранный Строителем, обычно делают неизменяемым и какую роль играет защитное копирование коллекций?
14. Чем Прототип отличается от Строителя? В чём разница между поверхностным и глубоким копированием?
15. Что такое Декоратор? Чем он отличается от наследования и почему порядок обёрток важен?
16. Разберите цепочку `new BufferedReader(new InputStreamReader(new FileInputStream(f), UTF_8))`: какой класс здесь Адаптер, какой Декоратор и по каким признакам вы их различили?
17. Чем Заместитель отличается от Декоратора при одинаковой технической структуре? Назовите четыре разновидности Заместителя.
18. Как устроен Наблюдатель? Какие две ошибки чаще всего допускают при его реализации?
19. Чем Стратегия отличается от Состояния? Кто в каждом случае решает, какой объект будет следующим?
20. Что такое Шаблонный метод и зачем сам метод-шаблон объявляют `final`?
21. Что такое Приспособленец? Как кеш `Integer.valueOf` объясняет поведение оператора `==` для значений 127 и 128?
22. Назовите три антипаттерна, найденных вами в `LibraryManager`, и рефакторинг, которым лечится каждый.
23. Что такое God Object и Shotgun Surgery? Почему их называют двумя сторонами одной ошибки?
24. Каков правильный порядок действий при рефакторинге и почему нельзя смешивать изменение структуры с изменением поведения в одном коммите?

---

## Результаты занятия

К концу занятия вы должны сдать:

1. **Часть 1:** таблица диагнозов по шести меткам `ReaderService`; пакет `ru.fa.patterns.solid.refactored` с классами `InMemoryReaderStorage`, `ConsoleNotifier`, `ReaderRegistrationService`, `FineCalculator`, `HtmlReaderList`, `SolidDemo`; подтверждение, что категория `GUEST` добавилась правкой одного файла; вывод `LiskovDemo` и его исправленная версия на `sealed`-интерфейсе; три раздельных интерфейса устройства с `SimplePrinter`, `MultifunctionDevice` и `DeviceDemo`.
2. **Часть 2:** `Counters`, `SingletonRace`, `NaiveRegistry`, `SafeRegistry`, `EnumRegistry`, `SingletonDemo`, `ReflectionAttack`; результаты пяти запусков гонки и сводная таблица трёх реализаций.
3. **Часть 3:** `Book` со Строителем и `BuilderDemo` с перехваченными исключениями; `MarkdownCatalogFormatter`, оба экспортёра, `CatalogExporters`, `ExporterDemo`; созданные файлы `catalog.csv` и `catalog.md`.
4. **Часть 4:** дополненный `FineTariff` (четыре тарифа) и `StrategyDemo` с тремя сортировками через `Comparator`; `ObserverDemo` и все три версии `Library` — со снимком `ConcurrentModificationException`, с выводом, где упавший второй слушатель оборвал рассылку журналу и счётчику, и с устойчивой рассылкой после `try/catch`.
5. **Часть 5:** `StreamChainDemo` с заполненной таблицей разбора цепочки и размерами файлов; `CountingOutputStream`, `UpperCaseWriter`, `DecoratorDemo` с показаниями двух счётчиков; `WrapOrderDemo` с двумя экспериментами.
6. **Часть 6:** таблица опознания десяти фрагментов; вывод `FlyweightDemo` в двух запусках (обычном и с флагом кеша); `ProxyDemo` с добавленным кешированием и именем сгенерированного класса-заместителя; заполненная таблица «паттерн — механизм Spring».
7. **Часть 7:** таблица антипаттернов `LibraryManager`; файлы `before.txt`, `after.txt` и результат их сравнения; пакет `ru.fa.patterns.antipatterns.refactored` с `RefactoredDemo`; журнал рефакторинга из семи шагов; разбор двух антипаттернов в собственном коде с переписанными фрагментами.
8. Ответы на все блоки «Ответьте письменно».
9. Ответы на контрольные вопросы (1–24).
