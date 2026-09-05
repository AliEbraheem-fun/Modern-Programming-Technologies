# Практическое занятие 10: Документирование и тестирование

Сегодня вы соберёте с нуля Maven-проект и научите его двум вещам, которых ему до сих пор не хватало: рассказывать о себе (Javadoc) и проверять себя самому (JUnit 5, Mockito, MockMvc).

Задания выполняются **строго по порядку**: каждое следующее опирается на код и зависимости из предыдущего. Части 1–6 живут в одном проекте `library-tests`, для Части 7 понадобится отдельный проект Spring Boot.

---

## Часть 1: Проект и документация Javadoc

### Задание 1.1: Создание Maven-проекта

Создайте вручную (без IDE) структуру каталогов:

```
library-tests/
├── pom.xml
└── src/
    ├── main/java/ru/fa/library/service/
    └── test/java/ru/fa/library/service/
```

Файл `pom.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0">
    <modelVersion>4.0.0</modelVersion>

    <groupId>ru.fa</groupId>
    <artifactId>library-tests</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.release>21</maven.compiler.release>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.13.0</version>
            </plugin>
        </plugins>
    </build>
</project>
```

Проверьте окружение и соберите пустой проект:

```bash
java -version      # 21 или выше
mvn -version       # Maven 3.9+ и тот же JDK
mvn clean compile
```

**Ответьте письменно:** (1) Что означает `maven.compiler.release` и чем оно отличается от пары `source`/`target`? (2) Зачем явно указывать `project.build.sourceEncoding`? (3) Какой каталог Maven считает корнем тестов и почему туда нельзя класть основной код?

---

### Задание 1.2: Оформление Javadoc

Создайте `src/main/java/ru/fa/library/service/FineCalculator.java`. Пока — без единого комментария:

```java
package ru.fa.library.service;

public class FineCalculator {

    public static final double DAILY_RATE = 5.0;

    public static final double MAX_FINE = 500.0;

    public double calculate(int daysOverdue) {
        if (daysOverdue < 0) {
            throw new IllegalArgumentException(
                    "Количество дней не может быть отрицательным: " + daysOverdue);
        }
        return Math.min(daysOverdue * DAILY_RATE, MAX_FINE);
    }

    public double calculateForBooks(int daysOverdue, int bookCount) {
        if (bookCount <= 0) {
            throw new IllegalArgumentException(
                    "Количество книг должно быть больше нуля: " + bookCount);
        }
        return calculate(daysOverdue) * bookCount;
    }
}
```

Посмотрите на класс глазами человека, который видит его впервые. По сигнатуре `double calculate(int daysOverdue)` не понять: в каких единицах результат? что будет при нуле? растёт ли штраф бесконечно? Это как купить кофемашину без инструкции — кнопки есть, а что они делают, выясняется опытным путём. Напишем инструкцию.

Допишите документирующие комментарии:

- **к классу** — краткое описание существительным («Калькулятор штрафов...»), подробное описание со ссылками `{@link #DAILY_RATE}` и `{@link #MAX_FINE}`, пример в блоке `<pre>{@code ... }</pre>`, теги `@author` (ваша фамилия), `@version 1.0`, `@since 1.0`;
- **к обеим константам** — короткий однострочный `/** ... */`;
- **к обоим методам** — краткое описание глаголом в третьем лице, подробное описание с поведением на границах, `@param` на каждый параметр, `@return`, `@throws`, хотя бы один `{@code}` и один `{@value}`.

Ориентир — так должен выглядеть первый метод:

```java
    /**
     * Вычисляет штраф за указанное количество дней просрочки.
     *
     * <p>Результат равен произведению дней на ставку {@link #DAILY_RATE},
     * но не превышает {@value #MAX_FINE} рублей. Для нуля дней возвращается {@code 0.0}.
     *
     * @param daysOverdue количество дней просрочки, неотрицательное число
     * @return сумма штрафа в рублях, от {@code 0.0} до {@link #MAX_FINE}
     * @throws IllegalArgumentException если {@code daysOverdue} отрицательное
     */
    public double calculate(int daysOverdue) {
```

Метод `calculateForBooks` и сам класс задокументируйте самостоятельно. Добавьте документацию пакета — файл `src/main/java/ru/fa/library/service/package-info.java`:

```java
/**
 * Сервисный слой онлайн-библиотеки.
 *
 * <p>Пакет содержит расчёт штрафов, учёт книг на полке и выдачу книг читателям.
 * Классы пакета не зависят от веб-слоя и от базы данных.
 *
 * @since 1.0
 */
package ru.fa.library.service;
```

Выполните `mvn clean compile` — проект должен собираться.

**Ответьте письменно:** (1) Почему первое предложение описания должно быть самодостаточным? (2) Что произойдёт, если написать `List<String>` в описании без `{@code}`? (3) Чем `{@value #MAX_FINE}` лучше, чем написанное текстом «500 рублей»?

---

### Задание 1.3: Генерация командой javadoc

Утилита `javadoc` лежит рядом с `java` и `javac` в каталоге `bin` вашего JDK. Запустите её из корня проекта.

Linux / macOS:

```bash
javadoc -d docs -sourcepath src/main/java -subpackages ru.fa.library \
        -encoding UTF-8 -charset UTF-8 -docencoding UTF-8 \
        -author -version -windowtitle "Онлайн-библиотека"
```

Windows (PowerShell или cmd) — то же самое **одной строкой**, обратный слэш здесь не работает:

```
javadoc -d docs -sourcepath src/main/java -subpackages ru.fa.library -encoding UTF-8 -charset UTF-8 -docencoding UTF-8 -author -version -windowtitle "Онлайн-библиотека"
```

Откройте результат в браузере:

```bash
xdg-open docs/index.html     # Linux
open docs/index.html         # macOS
start docs\index.html        # Windows
```

Найдите на сгенерированном сайте: страницу класса `FineCalculator` с таблицами «Field Summary» и «Method Summary»; строку с автором и версией; подставленное значение вместо `{@value #MAX_FINE}`; страницу `package-summary.html` с текстом из `package-info.java`; указатель `index-all.html` и работающий поиск.

Затем три эксперимента; после каждого возвращайте код в исходное состояние.

**Первый.** Запустите ту же команду **без** флагов `-author -version` и в другой каталог (`-d docs-noauthor`), сравните страницы класса.

**Второй.** Временно удалите из документации метода `calculateForBooks` строку `@param bookCount ...` и запустите генерацию снова. В консоли появится `warning: no @param for bookCount`, но генерация дойдёт до конца, документация обновится, а код возврата останется нулевым: отсутствующий тег doclint считает предупреждением. Верните тег на место.

**Третий.** Теперь испортите ссылку: в документации метода `calculate` замените `{@link #MAX_FINE}` на несуществующее `{@link #MAX_FINEE}` и запустите генерацию. На этот раз `javadoc` напечатает `error: reference not found`, подведёт итог «1 error» и завершится с ненулевым кодом — новый HTML не создан. Каталог `docs` при этом не очищается: там останется документация от предыдущего успешного запуска. Ориентируйтесь на вывод в консоли и на код возврата (`echo $LASTEXITCODE` в PowerShell, `echo %ERRORLEVEL%` в cmd), а не на наличие файлов. Повторите ту же команду с флагом `-Xdoclint:none` в конце: документация сгенерируется, только ссылка в ней работать не будет. Верните `{@link #MAX_FINE}` на место.

**Ответьте письменно:** (1) Почему `@author` и `@version` по умолчанию не попадают в HTML? (2) Что такое doclint, какие замечания он считает предупреждениями, а какие — ошибками, и когда его стоит отключать? (3) Что произойдёт с русским текстом, если убрать `-encoding UTF-8 -charset UTF-8 -docencoding UTF-8`?

---

### Задание 1.4: Генерация через maven-javadoc-plugin

Руками команду `javadoc` в реальном проекте не вызывают — это делает система сборки. Выигрыш вы почувствуете сразу: длинная строка с десятком флагов превращается в один блок `pom.xml`, одинаковый у всех участников проекта, а генерация встраивается в обычную сборку.

Добавьте в `pom.xml` внутрь `<plugins>`, рядом с `maven-compiler-plugin`:

```xml
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-javadoc-plugin</artifactId>
                <version>3.11.2</version>
                <configuration>
                    <encoding>UTF-8</encoding>
                    <charset>UTF-8</charset>
                    <docencoding>UTF-8</docencoding>
                    <author>true</author>
                    <version>true</version>
                    <doclint>none</doclint>
                    <windowtitle>Онлайн-библиотека</windowtitle>
                </configuration>
                <executions>
                    <execution>
                        <id>attach-javadocs</id>
                        <goals><goal>jar</goal></goals>
                    </execution>
                </executions>
            </plugin>
```

```bash
mvn clean javadoc:javadoc     # только HTML
mvn clean package             # обычный jar + javadoc-jar
```

Каталог с HTML по умолчанию — `target/site/apidocs` (в некоторых версиях плагина — `target/reports/apidocs`); точный путь плагин печатает в консоли. Откройте оттуда `index.html`. После `mvn package` в `target` должны лежать два архива: `library-tests-1.0-SNAPSHOT.jar` и `library-tests-1.0-SNAPSHOT-javadoc.jar`.

**Ответьте письменно:** (1) Зачем нужен отдельный `*-javadoc.jar`, если HTML уже сгенерирован? (2) К какой фазе жизненного цикла привязана цель `jar` этого плагина? (3) Чем генерация через плагин удобнее ручного вызова команды?

---

## Часть 2: Подключение JUnit 5 и первые тесты

### Задание 2.1: Зависимость и плагин Surefire

Добавьте в `pom.xml` секцию зависимостей (перед `<build>`):

```xml
    <dependencies>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>5.11.4</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
```

И третий плагин внутрь `<plugins>`:

```xml
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>3.5.2</version>
            </plugin>
```

```bash
mvn dependency:tree
mvn test
```

Тестов пока нет, поэтому Surefire напишет `No tests to run`. Зато в дереве зависимостей видно, что один артефакт `junit-jupiter` привёл за собой `junit-jupiter-api`, `junit-jupiter-params` и `junit-jupiter-engine`.

**Ответьте письменно:** (1) Что делает `<scope>test</scope>` и что случится, если его убрать? (2) Какие три подпроекта образуют JUnit 5 и за что отвечает каждый? (3) Зачем нужен отдельный плагин Surefire — разве Maven не запускает тесты сам?

---

### Задание 2.2: Первые тесты калькулятора

Создайте `src/test/java/ru/fa/library/service/FineCalculatorTest.java`:

```java
package ru.fa.library.service;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class FineCalculatorTest {

    /** Допустимая погрешность при сравнении вещественных чисел. */
    private static final double DELTA = 0.001;

    @Test
    void calculate_returnsRateTimesDays() {
        FineCalculator calculator = new FineCalculator();   // Arrange — подготовка

        double fine = calculator.calculate(10);             // Act — действие

        assertEquals(50.0, fine, DELTA);                    // Assert — проверка
    }

    @Test
    void calculate_isCappedAtMaxFine() {
        FineCalculator calculator = new FineCalculator();

        double fine = calculator.calculate(1000);

        assertEquals(FineCalculator.MAX_FINE, fine, DELTA);
    }

}
```

```bash
mvn test                                  # все тесты
mvn test -Dtest=FineCalculatorTest        # один класс
mvn test -Dtest=FineCalculatorTest#calculate_isCappedAtMaxFine    # один метод
```

В PowerShell аргумент с решёткой берите в кавычки, иначе оболочка может обрезать строку: `mvn test "-Dtest=FineCalculatorTest#calculate_isCappedAtMaxFine"`.

Сломайте один тест намеренно: замените ожидаемые `50.0` на `51.0`, выполните `mvn test`, прочитайте сообщение и загляните в отчёт `target/surefire-reports/`. Верните правильное значение. Отдельно напишите временный тест с `assertEquals(0.3, 0.1 + 0.2)` **без** дельты и посмотрите, что произойдёт.

**Ответьте письменно:** (1) Почему при сравнении `double` нужна дельта? (2) В каком порядке идут аргументы `assertEquals` и чем плохо их перепутать? (3) По какому признаку Surefire понимает, что класс `FineCalculatorTest` — тестовый?

---

### Задание 2.3: @BeforeEach, @AfterEach и @DisplayName

Создайте в основном коде `src/main/java/ru/fa/library/service/BookShelf.java`:

```java
package ru.fa.library.service;

import java.util.ArrayList;
import java.util.List;

/** Полка с книгами: хранит названия и позволяет их добавлять и убирать. */
public class BookShelf {

    private final List<String> titles = new ArrayList<>();

    /**
     * Добавляет книгу на полку.
     *
     * @param title название книги, не пустое
     * @throws IllegalArgumentException если название {@code null} или пустое
     */
    public void add(String title) {
        if (title == null || title.isBlank()) {
            throw new IllegalArgumentException("Название книги не задано");
        }
        titles.add(title);
    }

    /** @return {@code true}, если книга была на полке и её убрали */
    public boolean remove(String title) { return titles.remove(title); }

    /** @return количество книг на полке */
    public int size() { return titles.size(); }

    /** @return неизменяемая копия списка названий */
    public List<String> titles() { return List.copyOf(titles); }
}
```

Тест `src/test/java/ru/fa/library/service/BookShelfTest.java`:

```java
package ru.fa.library.service;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

@DisplayName("Книжная полка")
class BookShelfTest {

    private BookShelf shelf;

    @BeforeEach
    void setUp() {
        // Выполняется перед КАЖДЫМ тестом — полка всегда новая
        System.out.println("  [setUp] создаём полку");
        shelf = new BookShelf();
        shelf.add("Война и мир");
    }

    @AfterEach
    void tearDown() {
        // Выполняется после КАЖДОГО теста, даже если тест упал
        System.out.println("  [tearDown] книг на полке: " + shelf.size());
    }

    @Test
    @DisplayName("После добавления книги размер увеличивается")
    void add_increasesSize() {
        shelf.add("Мастер и Маргарита");

        assertEquals(2, shelf.size(), "На полке должно быть две книги");
    }

    @Test
    @DisplayName("Удаление существующей книги возвращает true")
    void remove_returnsTrueForExistingBook() {
        boolean removed = shelf.remove("Война и мир");

        assertTrue(removed);
        assertEquals(0, shelf.size());
    }

    @Test
    @DisplayName("Каждый тест получает свежую полку")
    void eachTestGetsFreshShelf() {
        assertEquals(1, shelf.size(), () -> "Ожидали одну книгу, а на полке: " + shelf.titles());
        assertFalse(shelf.titles().contains("Мастер и Маргарита"));
    }
}
```

Выполните `mvn test` и прочитайте порядок сообщений в консоли. Вы увидите `[setUp]` и `[tearDown]` по три раза — по одному разу на каждый тест, а не по одному на весь класс. И обратите внимание: третий тест проходит, хотя первый добавлял на полку вторую книгу.

**Ответьте письменно:** (1) Сколько раз выполнился `setUp` и почему именно столько? (2) Почему поле `shelf` в первом и третьем тесте — разные объекты? (3) Чем `@BeforeAll` отличается от `@BeforeEach` и почему он по умолчанию обязан быть статическим?

---

## Часть 3: Тестирование исключений

### Задание 3.1: assertThrows и его родственники

Метод обязан не только возвращать правильный результат, но и правильно **отказываться** работать — в лекции мы сравнивали это с предохранителем, который проверяют на сгорание, а не на пропускание тока. Сейчас предметом проверки будет именно отказ: пять тестов, из которых три ждут исключения.

Создайте `src/test/java/ru/fa/library/service/FineCalculatorExceptionTest.java`:

```java
package ru.fa.library.service;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

@DisplayName("Калькулятор штрафов: ошибочные и граничные данные")
class FineCalculatorExceptionTest {

    private static final double DELTA = 0.001;

    private FineCalculator calculator;

    @BeforeEach
    void setUp() {
        calculator = new FineCalculator();
    }

    @Test
    @DisplayName("Отрицательное количество дней вызывает IllegalArgumentException")
    void calculate_throwsOnNegativeDays() {
        assertThrows(IllegalArgumentException.class, () -> calculator.calculate(-1));
    }

    @Test
    @DisplayName("Сообщение об ошибке содержит само значение")
    void calculate_exceptionMessageContainsValue() {
        IllegalArgumentException exception = assertThrows(
                IllegalArgumentException.class,
                () -> calculator.calculate(-5)
        );

        assertAll(
                () -> assertTrue(exception.getMessage().contains("отрицательным")),
                () -> assertTrue(exception.getMessage().contains("-5"))
        );
    }

    @Test
    @DisplayName("Ноль книг — ошибка, и именно IllegalArgumentException")
    void calculateForBooks_throwsExactlyOnZeroBooks() {
        assertThrowsExactly(IllegalArgumentException.class,
                () -> calculator.calculateForBooks(10, 0));
    }

    @Test
    @DisplayName("Ноль дней — валидное значение, исключения нет")
    void calculate_doesNotThrowOnZero() {
        double fine = assertDoesNotThrow(() -> calculator.calculate(0));

        assertEquals(0.0, fine, DELTA);
    }

    @Test
    @DisplayName("На границе максимума штраф ещё считается по ставке")
    void exactlyAtCap_returnsMaxFine() {
        int daysToCap = (int) (FineCalculator.MAX_FINE / FineCalculator.DAILY_RATE);  // 100
        assertEquals(FineCalculator.MAX_FINE, calculator.calculate(daysToCap), DELTA);
    }
}
```

Граничные значения (0, −1, максимум, максимум плюс-минус единица) — первое, что нужно проверять: именно там живёт большинство ошибок. Запустите `mvn test`, затем поставьте эксперимент: временно уберите из `FineCalculator.calculate` проверку `if (daysOverdue < 0)`, прогоните тесты и прочитайте, что скажет JUnit. Верните проверку.

**Ответьте письменно:** (1) Что возвращает `assertThrows` и зачем это нужно? (2) Чем `assertThrows` отличается от `assertThrowsExactly`? (3) Почему `assertAll` показывает обе ошибки сразу, а два `assertTrue` подряд — только первую? (4) Почему вызов внутри `assertThrows` обёрнут в лямбду, а не написан напрямую?

---

## Часть 4: Параметризованные тесты

### Задание 4.1: @ValueSource и @NullAndEmptySource

Сейчас вы замените пачку почти одинаковых тестовых методов одним параметризованным. В отчёте `mvn test` следите за числом прогонов: методов станет меньше, а строк в отчёте — больше, потому что каждый набор данных считается отдельным тестом со своим именем.

Создайте `src/test/java/ru/fa/library/service/FineCalculatorParamTest.java`:

```java
package ru.fa.library.service;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.*;   // ValueSource, CsvSource, MethodSource, Arguments

import java.util.stream.Stream;

import static org.junit.jupiter.api.Assertions.*;

@DisplayName("Калькулятор штрафов: наборы данных")
class FineCalculatorParamTest {

    private static final double DELTA = 0.001;

    private final FineCalculator calculator = new FineCalculator();

    @ParameterizedTest(name = "просрочка {0} дней — исключения нет")
    @ValueSource(ints = {0, 1, 5, 100, 1000})
    void calculate_acceptsNonNegativeDays(int days) {
        assertDoesNotThrow(() -> calculator.calculate(days));
    }

    @ParameterizedTest(name = "прогон {index}: {0} дней — ошибка")
    @ValueSource(ints = {-1, -5, -100, Integer.MIN_VALUE})
    void calculate_rejectsNegativeDays(int days) {
        assertThrows(IllegalArgumentException.class, () -> calculator.calculate(days));
    }

    @ParameterizedTest(name = "название «{0}» отвергается")
    @NullAndEmptySource
    @ValueSource(strings = {"   ", "\t"})
    void add_rejectsBlankTitles(String title) {
        assertThrows(IllegalArgumentException.class, () -> new BookShelf().add(title));
    }
}
```

Запустите `mvn test` и посчитайте, сколько всего прогонов дали эти три метода.

**Ответьте письменно:** (1) Сколько раз выполнился каждый параметризованный метод? (2) Почему `null` нельзя передать через `@ValueSource(strings = ...)` и какая аннотация решает эту задачу? (3) Что означают плейсхолдеры `{0}` и `{index}` в атрибуте `name`?

---

### Задание 4.2: @CsvSource и @MethodSource

Допишите в тот же класс ещё два теста и метод-источник:

```java
    @ParameterizedTest(name = "{0} дней → {1} руб.")
    @CsvSource({
            "0,   0.0",
            "1,   5.0",
            "10,  50.0",
            "99,  495.0",
            "100, 500.0",
            "999, 500.0"
    })
    @DisplayName("Таблица соответствия дней и штрафа")
    void calculate_matchesTable(int days, double expectedFine) {
        assertEquals(expectedFine, calculator.calculate(days), DELTA);
    }

    @ParameterizedTest(name = "{3}")
    @MethodSource("fineCases")
    @DisplayName("Штраф за несколько книг")
    void calculateForBooks_worksForAllCases(int days, int books,
                                            double expected, String description) {
        assertEquals(expected, calculator.calculateForBooks(days, books), DELTA);
    }

    /** Источник данных для {@link #calculateForBooks_worksForAllCases}. */
    static Stream<Arguments> fineCases() {
        return Stream.of(
                Arguments.of(0, 1, 0.0, "без просрочки штрафа нет"),
                Arguments.of(1, 1, 5.0, "один день, одна книга — одна ставка"),
                Arguments.of(10, 3, 150.0, "три книги по 50 рублей"),
                Arguments.of(100, 2, 1000.0, "две книги по максимуму"),
                Arguments.of(1000, 2, 1000.0, "выше максимума штраф не растёт")
        );
    }
```

Запустите `mvn test` и посмотрите на имена прогонов (в IDE они видны нагляднее, чем в консоли). Затем замените одно значение в `@CsvSource` на заведомо неверное и убедитесь, что упал ровно один прогон, а остальные прошли. Верните правильное значение.

**Ответьте письменно:** (1) Почему метод-источник для `@MethodSource` обязан быть статическим? (2) Когда `@CsvSource` неудобен и лучше взять `@MethodSource`? (3) Чем `@CsvFileSource` отличается от `@CsvSource` и где должен лежать файл с данными?

---

## Часть 5: Повторяющиеся и динамические тесты

### Задание 5.1: @RepeatedTest

Некоторый код ведёт себя по-разному от запуска к запуску: случайность, конкурентность, кэш. Проверять его один раз — как проверять кубик одним броском.

Создайте `src/test/java/ru/fa/library/service/CardNumberGeneratorTest.java`:

```java
package ru.fa.library.service;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.RepeatedTest;
import org.junit.jupiter.api.RepetitionInfo;

import java.util.concurrent.ThreadLocalRandom;

import static org.junit.jupiter.api.Assertions.*;

@DisplayName("Генератор номеров читательского билета")
class CardNumberGeneratorTest {

    /** Генерирует восьмизначный номер читательского билета. */
    static String generate() {
        return String.format("%08d", ThreadLocalRandom.current().nextInt(100_000_000));
    }

    @RepeatedTest(value = 10, name = "прогон {currentRepetition} из {totalRepetitions}")
    @DisplayName("Номер билета всегда состоит из 8 цифр")
    void generate_hasFixedLength(RepetitionInfo info) {
        // JUnit сам внедряет информацию о текущем прогоне, если она нужна
        assertTrue(info.getCurrentRepetition() <= info.getTotalRepetitions());

        String number = generate();

        assertEquals(8, number.length());
        assertTrue(number.matches("\\d{8}"), "Номер должен состоять только из цифр: " + number);
    }
}
```

Запустите `mvn test` и убедитесь, что в отчёте десять прогонов.

**Ответьте письменно:** (1) В каких случаях `@RepeatedTest` действительно полезен, а в каких — трата времени? (2) Почему десять повторов не гарантируют, что редкая ошибка будет найдена? (3) Какие объекты JUnit умеет внедрять в тестовый метод?

---

### Задание 5.2: @TestFactory и динамические тесты

Все предыдущие тесты определялись на этапе компиляции. Динамические тесты создаются во время выполнения, поэтому их количество может зависеть от данных, прочитанных из файла или базы.

Создайте `src/test/java/ru/fa/library/service/DynamicFineTest.java`:

```java
package ru.fa.library.service;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.DynamicTest;
import org.junit.jupiter.api.TestFactory;

import java.util.List;
import java.util.stream.Stream;

import static org.junit.jupiter.api.Assertions.assertEquals;

@DisplayName("Динамические тесты калькулятора")
class DynamicFineTest {

    private final FineCalculator calculator = new FineCalculator();

    @TestFactory
    @DisplayName("Штраф для набора дней, известного только в рантайме")
    Stream<DynamicTest> fineTests() {
        // Такой список мог бы быть прочитан из файла или из базы
        List<Integer> days = List.of(0, 3, 20, 200);

        return days.stream()
                .map(d -> DynamicTest.dynamicTest(
                        "просрочка " + d + " дней",
                        () -> assertEquals(
                                Math.min(d * FineCalculator.DAILY_RATE, FineCalculator.MAX_FINE),
                                calculator.calculate(d),
                                0.001)));
    }
}
```

Запустите `mvn test`. Теперь добавьте в список `days` ещё два числа и прогоните снова: количество тестов изменилось без единой новой аннотации.

**Ответьте письменно:** (1) Чем `@TestFactory` принципиально отличается от `@ParameterizedTest`? (2) Почему метод, помеченный `@TestFactory`, не может возвращать `void`? (3) Как ведут себя `@BeforeEach` и `@AfterEach` по отношению к динамическим тестам?

---

## Часть 6: Mockito — тестирование сервиса в изоляции

### Задание 6.1: Подключение Mockito и код сервиса

Модульный тест обязан проверять один класс. Но реальный сервис зависит от репозитория и от отправителя уведомлений: чтобы проверить его «по-настоящему», пришлось бы поднять базу и почтовый сервер. На тренинге кассиров банкомат заменяют картонным макетом — он выдаёт «купюры» по команде, но денег не тратит; проверяют при этом кассира, а не банкомат. Mockito делает такие макеты для Java-объектов.

Добавьте в `<dependencies>`:

```xml
        <dependency>
            <groupId>org.mockito</groupId>
            <artifactId>mockito-junit-jupiter</artifactId>
            <version>5.14.2</version>
            <scope>test</scope>
        </dependency>
```

Создайте модель `src/main/java/ru/fa/library/model/Book.java`:

```java
package ru.fa.library.model;

/** Книга библиотечного фонда. */
public class Book {

    private final Long id;
    private final String title;
    private boolean available;

    public Book(Long id, String title, boolean available) {
        this.id = id;
        this.title = title;
        this.available = available;
    }

    public Long getId() { return id; }
    public String getTitle() { return title; }
    public boolean isAvailable() { return available; }
    public void setAvailable(boolean available) { this.available = available; }
}
```

И три файла в пакете `ru.fa.library.service` — два интерфейса и сервис:

```java
// BookRepository.java
package ru.fa.library.service;

import ru.fa.library.model.Book;
import java.util.Optional;

/** Хранилище книг. Реализация в этом занятии не нужна — её заменит мок. */
public interface BookRepository {
    Optional<Book> findById(Long id);
    Book save(Book book);
}

// NotificationSender.java (отдельный файл в том же пакете)
package ru.fa.library.service;

/** Отправитель уведомлений читателю. */
public interface NotificationSender {
    void send(String email, String text);
}
```

```java
// LoanService.java
package ru.fa.library.service;

import ru.fa.library.model.Book;

/** Сервис выдачи книг читателям. */
public class LoanService {

    private final BookRepository repository;
    private final NotificationSender sender;

    public LoanService(BookRepository repository, NotificationSender sender) {
        this.repository = repository;
        this.sender = sender;
    }

    /**
     * Выдаёт книгу читателю и отправляет уведомление.
     *
     * @param bookId идентификатор книги
     * @param email  адрес читателя
     * @throws IllegalArgumentException если книги с таким идентификатором нет
     * @throws IllegalStateException    если книга уже выдана
     */
    public void lend(Long bookId, String email) {
        Book book = repository.findById(bookId)
                .orElseThrow(() -> new IllegalArgumentException("Книга не найдена: " + bookId));
        if (!book.isAvailable()) {
            throw new IllegalStateException("Книга уже выдана: " + book.getTitle());
        }
        book.setAvailable(false);
        repository.save(book);
        sender.send(email, "Вы получили книгу «" + book.getTitle() + "»");
    }
}
```

Выполните `mvn clean compile`.

**Ответьте письменно:** (1) Почему у `BookRepository` нет ни одной реализации, но проект компилируется? (2) Чем стаб отличается от мока? (3) Что вернёт `findById` у только что созданного мока, если его не настраивать?

---

### Задание 6.2: Моки, when().thenReturn() и verify()

Создайте `src/test/java/ru/fa/library/service/LoanServiceTest.java`:

```java
package ru.fa.library.service;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.ArgumentCaptor;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import ru.fa.library.model.Book;

import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.*;   // any, anyString, eq
import static org.mockito.Mockito.*;            // when, verify, never, verifyNoInteractions

@ExtendWith(MockitoExtension.class)
@DisplayName("Сервис выдачи книг")
class LoanServiceTest {

    @Mock
    private BookRepository repository;

    @Mock
    private NotificationSender sender;

    @InjectMocks
    private LoanService service;   // Mockito сам подставит моки в конструктор

    @Test
    @DisplayName("Доступная книга выдаётся, сохраняется, читателю уходит уведомление")
    void lend_marksBookAsUnavailableAndNotifies() {
        Book book = new Book(1L, "Война и мир", true);
        when(repository.findById(1L)).thenReturn(Optional.of(book));   // учим мок отвечать

        service.lend(1L, "ivan@example.com");

        assertFalse(book.isAvailable());
        verify(repository).save(book);                              // ровно один вызов
        verify(sender).send(eq("ivan@example.com"), anyString());    // уведомление ушло
    }

    @Test
    @DisplayName("Занятую книгу выдать нельзя, уведомление не отправляется")
    void lend_throwsWhenBookIsAlreadyLent() {
        Book book = new Book(1L, "Война и мир", false);   // уже выдана
        when(repository.findById(1L)).thenReturn(Optional.of(book));

        IllegalStateException exception = assertThrows(IllegalStateException.class,
                () -> service.lend(1L, "ivan@example.com"));

        assertTrue(exception.getMessage().contains("Война и мир"));
        verify(repository, never()).save(any());
        verifyNoInteractions(sender);
    }

    @Test
    @DisplayName("Несуществующая книга приводит к IllegalArgumentException")
    void lend_throwsWhenBookNotFound() {
        when(repository.findById(99L)).thenReturn(Optional.empty());

        assertThrows(IllegalArgumentException.class, () -> service.lend(99L, "ivan@example.com"));
        verifyNoInteractions(sender);
    }

    // Задание: допишите тест lend_notificationContainsBookTitle.
    // Он должен выдать доступную книгу, перехватить текст уведомления
    // и проверить, что тот содержит название книги:
    //
    //     ArgumentCaptor<String> textCaptor = ArgumentCaptor.forClass(String.class);
    //     verify(sender).send(eq("ivan@example.com"), textCaptor.capture());
    //     assertTrue(textCaptor.getValue().contains("Война и мир"));
}
```

Запустите `mvn test`. На JDK 21 Mockito может напечатать предупреждение «A Java agent has been loaded dynamically» — оно безвредно.

Три эксперимента (после каждого возвращайте код в исходное состояние). Уберите строку `when(repository.findById(1L))...` из первого теста и прочитайте ошибку: мок вернул пустой `Optional`, и сервис бросил `IllegalArgumentException`. Замените `verify(sender).send(eq("ivan@example.com"), anyString())` на `verify(sender).send("ivan@example.com", anyString())` — получите `InvalidUseOfMatchersException`. Добавьте настройку `when(repository.save(any())).thenReturn(null);` в третий тест, `lend_throwsWhenBookNotFound` — там сервис до `save()` не доходит, заглушка остаётся невостребованной, и строгий режим `MockitoExtension` сообщит об этом исключением `UnnecessaryStubbingException`. В первом тесте та же строка ошибки не вызвала бы: `save()` там действительно вызывается.

**Ответьте письменно:** (1) Что делает `@ExtendWith(MockitoExtension.class)` и что было бы без него? (2) Почему нельзя смешивать «сырое» значение и матчер в одном вызове `verify`? (3) Зачем нужен `ArgumentCaptor`, если есть `verify`?

---

## Часть 7: Тестирование Spring-приложения

### Задание 7.1: Проект для веб-слоя

Эта часть выполняется в **отдельном** проекте Spring Boot. Приёмка квартиры выглядит так: розетку проверяют тестером прямо в стене, потом проверяют весь щиток, и только затем заселяются и включают технику разом. `@WebMvcTest` — это проверка щитка: поднимается веб-слой и ничего больше.

Откройте [https://start.spring.io](https://start.spring.io) и сгенерируйте проект:

- **Project:** Maven, **Language:** Java, **Spring Boot:** 3.5.x
- **Group:** `ru.fa`, **Artifact:** `student-web`, **Package name:** `ru.fa.student`
- **Packaging:** Jar, **Java:** 21
- **Dependencies:** Spring Web

Модель здесь намеренно проще, чем в Лекции 7: `Student` — это record без JPA, поэтому вместо `new Student(); setName(...)` используется конструктор `new Student(id, name, surname)`, а вместо геттеров — методы записи `id()`, `name()`, `surname()`. Код из разделов 12.2–12.4 лекции написан под сущность из Лекции 7 и в этот проект не переносится дословно.

Зависимость `spring-boot-starter-test` Initializr добавляет сам — она уже приносит JUnit 5, Mockito, AssertJ и модуль Spring Test, дописывать в `pom.xml` ничего не нужно. Создайте четыре файла в пакете `ru.fa.student`:

```java
// Student.java
package ru.fa.student;

/** Студент: идентификатор, имя, фамилия. */
public record Student(Long id, String name, String surname) { }

// StudentService.java (отдельный файл в том же пакете)
package ru.fa.student;

import java.util.List;

/** Сервис работы со студентами. */
public interface StudentService {

    List<Student> findAll();

    /**
     * Возвращает студента по идентификатору.
     *
     * @param id идентификатор студента
     * @return найденный студент или {@code null}, если студента с таким id нет
     */
    Student findById(Long id);

    Student save(Student student);
}
```

```java
// StudentServiceImpl.java
package ru.fa.student;

import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

/** Хранилище студентов в памяти — чтобы приложение можно было запустить. */
@Service
public class StudentServiceImpl implements StudentService {

    private final List<Student> students = new ArrayList<>();

    @Override
    public List<Student> findAll() { return List.copyOf(students); }

    @Override
    public Student findById(Long id) {
        return students.stream().filter(s -> s.id().equals(id)).findFirst().orElse(null);
    }

    @Override
    public Student save(Student student) {
        Student saved = new Student((long) (students.size() + 1),
                student.name(), student.surname());
        students.add(saved);
        return saved;
    }
}
```

```java
// StudentRestController.java
package ru.fa.student;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/** REST-контроллер студентов. */
@RestController
@RequestMapping("/api/students")
public class StudentRestController {

    private final StudentService studentService;

    public StudentRestController(StudentService studentService) {
        this.studentService = studentService;
    }

    @GetMapping
    public List<Student> getAll() {
        return studentService.findAll();
    }

    @GetMapping("/{id}")
    public ResponseEntity<Student> getById(@PathVariable Long id) {
        Student student = studentService.findById(id);
        return student != null ? ResponseEntity.ok(student) : ResponseEntity.notFound().build();
    }

    @PostMapping
    public ResponseEntity<Student> create(@RequestBody Student student) {
        return ResponseEntity.status(HttpStatus.CREATED).body(studentService.save(student));
    }
}
```

Запустите приложение и убедитесь, что по адресу `http://localhost:8080/api/students` возвращается пустой массив `[]`. Затем остановите его.

```bash
./mvnw spring-boot:run      # Linux / macOS
.\mvnw.cmd spring-boot:run  # Windows
```

---

### Задание 7.2: @WebMvcTest и MockMvc

Создайте `src/test/java/ru/fa/student/StudentRestControllerTest.java`:

```java
package ru.fa.student;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.http.MediaType;
import org.springframework.test.context.bean.override.mockito.MockitoBean;
import org.springframework.test.web.servlet.MockMvc;

import java.util.List;

import static org.mockito.Mockito.*;                                         // when, verify, any
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;   // get, post
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;     // status и др.

@WebMvcTest(StudentRestController.class)
@DisplayName("REST-контроллер студентов")
class StudentRestControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockitoBean                       // подменяет бин StudentService моком Mockito
    private StudentService studentService;

    @Test
    @DisplayName("GET /api/students возвращает 200 и список студентов")
    void getAll_returnsList() throws Exception {
        when(studentService.findAll()).thenReturn(List.of(new Student(1L, "Иван", "Петров")));

        mockMvc.perform(get("/api/students"))
                .andExpect(status().isOk())
                .andExpect(content().contentTypeCompatibleWith(MediaType.APPLICATION_JSON))
                .andExpect(jsonPath("$[0].name").value("Иван"))
                .andExpect(jsonPath("$[0].surname").value("Петров"));
    }

    @Test
    @DisplayName("GET /api/students/99 возвращает 404, если студента нет")
    void getById_returns404() throws Exception {
        when(studentService.findById(99L)).thenReturn(null);

        mockMvc.perform(get("/api/students/99"))
                .andExpect(status().isNotFound());
    }

    @Test
    @DisplayName("POST /api/students возвращает 201 и созданного студента")
    void create_returns201() throws Exception {
        when(studentService.save(any(Student.class)))
                .thenReturn(new Student(5L, "Пётр", "Иванов"));

        mockMvc.perform(post("/api/students")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("{\"name\": \"Пётр\", \"surname\": \"Иванов\"}"))
                .andExpect(status().isCreated())
                .andExpect(jsonPath("$.id").value(5));

        verify(studentService).save(any(Student.class));
    }
}
```

```bash
./mvnw test      # Linux / macOS
.\mvnw.cmd test  # Windows
```

Все три теста должны пройти. Обратите внимание на время: контекст поднимается за доли секунды, потому что ни база, ни сервер не запускаются. Если у вас Spring Boot ниже 3.4, аннотации `@MockitoBean` не существует — используйте устаревшую `@MockBean` из пакета `org.springframework.boot.test.mock.mockito`.

Два эксперимента. Первый: уберите аннотацию `@MockitoBean` с поля `studentService`, прочитайте ошибку запуска контекста и верните аннотацию. Второй: замените `@WebMvcTest(StudentRestController.class)` на пару `@SpringBootTest` и `@AutoConfigureMockMvc` (импорты `org.springframework.boot.test.context.SpringBootTest` и `org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc`), сравните время выполнения тестов до и после, затем верните `@WebMvcTest`.

**Ответьте письменно:** (1) Какие бины поднимает `@WebMvcTest` и каких в контексте заведомо нет? (2) Почему `MockMvc` работает без запуска Tomcat и что именно он вызывает? (3) Что этот тест проверяет и что он принципиально проверить не может?

---

### Задание 7.3: Интеграционный тест всего приложения

Предыдущий тест проверял контроллер в одиночестве: сервис был подменён моком, сервер не запускался. Теперь проверим приложение целиком — с настоящим сервером, настоящим сервисом и настоящим HTTP-запросом по сети. Это и есть **интеграционный тест**: он отвечает на вопрос, который срез принципиально не задаёт, — собираются ли компоненты вместе.

Создайте в том же проекте `student-web` файл `src/test/java/ru/fa/student/StudentWebApplicationIntegrationTest.java`:

```java
package ru.fa.student;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@DisplayName("Сквозной сценарий: создание студента и чтение списка")
class StudentWebApplicationIntegrationTest {

    // TestRestTemplate уже знает адрес и случайный порт поднятого сервера,
    // поэтому в запросах указывается только путь
    @Autowired
    private TestRestTemplate restTemplate;

    @Test
    @DisplayName("Созданный студент возвращается в общем списке")
    void createdStudent_appearsInList() {
        Student request = new Student(null, "Анна", "Смирнова");

        ResponseEntity<Student> created =
                restTemplate.postForEntity("/api/students", request, Student.class);

        assertEquals(HttpStatus.CREATED, created.getStatusCode());
        assertNotNull(created.getBody());
        assertEquals("Анна", created.getBody().name());
        assertNotNull(created.getBody().id(), "Сервис обязан присвоить идентификатор");

        ResponseEntity<Student[]> all =
                restTemplate.getForEntity("/api/students", Student[].class);

        assertEquals(HttpStatus.OK, all.getStatusCode());
        assertNotNull(all.getBody());
        assertTrue(all.getBody().length > 0, "Список не должен быть пустым");

        boolean found = Arrays.stream(all.getBody())
                .anyMatch(s -> "Анна".equals(s.name()) && "Смирнова".equals(s.surname()));
        assertTrue(found, "Созданный студент должен быть в списке");
    }
}
```

```bash
./mvnw test      # Linux / macOS
.\mvnw.cmd test  # Windows
```

Сравните вывод с предыдущим заданием: в логе появятся строки о старте Tomcat и случайном порте, а общее время прогона заметно вырастет. Здесь никаких моков нет — работают настоящий `StudentServiceImpl` и настоящая сериализация JSON, а запрос идёт через сетевой стек. Поэтому такой тест ловит то, что срез пропускает: например, если убрать у `StudentServiceImpl` аннотацию `@Service`, `@WebMvcTest` этого не заметит (сервис там всё равно мок), а интеграционный тест упадёт ещё на старте контекста. Проверьте это: временно уберите `@Service`, прогоните оба теста и верните аннотацию.

**Ответьте письменно:** (1) Чем `@SpringBootTest` отличается от `@WebMvcTest` по составу контекста и по времени выполнения? (2) Какие значения принимает `webEnvironment` и что означает `RANDOM_PORT`? (3) Почему в запросах `TestRestTemplate` указывается только путь, без хоста и порта? (4) Почему таких тестов в проекте должно быть немного?

---

## Часть 8: Контрольные вопросы

Ответьте письменно:

1. Назовите три вида комментариев в Java. Чем документирующий комментарий отличается от блочного синтаксически и по назначению?
2. Из каких трёх частей состоит документирующий комментарий и где заканчивается краткое описание?
3. Почему нельзя ставить точку в середине первого предложения Javadoc и как задать границу краткого описания явно?
4. Что такое дескриптор Javadoc? Чем блочные дескрипторы отличаются от строчных?
5. Перечислите пять блочных дескрипторов и объясните назначение каждого. В чём разница между `@throws` и `@exception`?
6. Чем `{@code}` отличается от `{@literal}`? Что делает `{@value}` и зачем он нужен?
7. Как работает `{@inheritDoc}` и когда он необходим, а когда документация наследуется сама?
8. Какими опциями команды `javadoc` задаются каталог вывода, кодировка и вывод автора? Что такое doclint?
9. Для чего нужен `package-info.java` и на какую страницу попадает его текст?
10. Что делает `maven-javadoc-plugin` и чем цель `javadoc:javadoc` отличается от `javadoc:jar`?
11. Чем ручное тестирование отличается от автоматизированного? В чём различие подходов чёрного и белого ящика?
12. Опишите пирамиду тестирования. Почему модульных тестов должно быть больше всего и что такое антипаттерн «мороженое»?
13. Расшифруйте FIRST. Какое из пяти свойств нарушает тест, зависящий от текущей даты?
14. Опишите схему AAA. Как она называется в терминологии BDD?
15. Из каких трёх подпроектов состоит JUnit 5 и за что отвечает каждый? Что такое `TestEngine`?
16. Какие зависимости и плагины нужны для запуска тестов JUnit 5 в Maven-проекте? Где должны лежать тестовые классы и как их принято называть?
17. Чем класс `Assertions` из JUnit 5 отличается от `Assert` из JUnit 4? Назовите минимум два отличия.
18. Почему при сравнении `double` нужна дельта? Что не так с прямым сравнением `0.1 + 0.2` и `0.3`?
19. Что делает `assertAll` и чем он лучше нескольких утверждений подряд?
20. Как проверить выброс исключения в JUnit 5? Что возвращает `assertThrows` и чем он лучше атрибута `@Test(expected = ...)` из JUnit 4?
21. Сколько экземпляров тестового класса создаёт JUnit при трёх тестовых методах, зачем он так делает и как это поведение изменить?
22. Перечислите источники данных для `@ParameterizedTest`. Почему `@ValueSource` не умеет передавать `null`?
23. Чем `@RepeatedTest`, `@ParameterizedTest` и `@TestFactory` отличаются по моменту, когда становится известен набор проверок?
24. Объясните разницу между dummy, stub, mock, spy и fake. Что делают `when().thenReturn()`, `verify()` и `ArgumentCaptor`? Какое правило действует при смешивании матчеров с обычными значениями?
25. Чем `@WebMvcTest` отличается от `@SpringBootTest`? Зачем в срезе веб-слоя нужен `@MockitoBean` и что такое `MockMvc`?
26. Что такое интеграционное тестирование и чем оно отличается от модульного? Что даёт `webEnvironment = RANDOM_PORT` и зачем в таком тесте `TestRestTemplate`?

---

## Результаты занятия

К концу занятия вы должны сдать:

1. Проект `library-tests` с полностью документированным классом `FineCalculator` (класс, обе константы, оба метода) и файлом `package-info.java`.
2. Сгенерированную документацию: каталог `docs` (команда `javadoc`) и вывод плагина в `target`, включая `library-tests-1.0-SNAPSHOT-javadoc.jar`.
3. `pom.xml` с настроенными `maven-compiler-plugin`, `maven-javadoc-plugin`, `maven-surefire-plugin` и зависимостями `junit-jupiter` и `mockito-junit-jupiter`.
4. Тестовые классы `FineCalculatorTest`, `BookShelfTest` (с `@BeforeEach`, `@AfterEach`, `@DisplayName`) и `FineCalculatorExceptionTest` (с `assertThrows`, `assertThrowsExactly`, `assertDoesNotThrow`, `assertAll`).
5. Параметризованный класс `FineCalculatorParamTest` с `@ValueSource`, `@NullAndEmptySource`, `@CsvSource` и `@MethodSource`.
6. Тесты `CardNumberGeneratorTest` (`@RepeatedTest`) и `DynamicFineTest` (`@TestFactory`).
7. Тест `LoanServiceTest` с `@Mock`, `@InjectMocks`, `when().thenReturn()`, `verify()`, `never()`, `verifyNoInteractions()` и дописанным вами тестом с `ArgumentCaptor`.
8. Проект Spring Boot `student-web` с тестом `StudentRestControllerTest` (`@WebMvcTest`, `MockMvc`, `@MockitoBean`) — все три теста проходят.
9. Интеграционный тест `StudentWebApplicationIntegrationTest` (`@SpringBootTest` с `webEnvironment = RANDOM_PORT`, `TestRestTemplate`): сквозной сценарий «создали студента — получили его в списке» проходит.
10. Вывод команды `mvn test` для обоих проектов: все тесты зелёные.
11. Ответы на вопросы из заданий и на контрольные вопросы (1–26).
