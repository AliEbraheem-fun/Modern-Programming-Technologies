# Лекция 4: Вложенные классы, Интерфейсы, Обобщения и Исключения

## Введение

Добро пожаловать на четвёртую лекцию курса "Современные технологии программирования". На предыдущих занятиях мы освоили основы Java — классы, интерфейсы, массивы и другие фундаментальные конструкции. Сегодня мы углубимся в более продвинутые механизмы языка: разберёмся, как и зачем создавать классы внутри других классов, познакомимся с вложенными интерфейсами, научимся писать универсальный типобезопасный код с помощью обобщений (Generics), а также изучим систему исключений Java — как правильно обрабатывать ошибки и создавать надёжные программы.

---

## Часть 1: Вложенные классы (Nested Classes)

### 1.1 Зачем нужны вложенные классы?

Представьте, что вы проектируете класс `Order` (Заказ). У него есть внутренняя концепция `OrderItem` (Позиция заказа). `OrderItem` не имеет смысла без `Order` — нельзя иметь позицию заказа без самого заказа. В таких случаях логично сделать `OrderItem` вложенным классом внутри `Order`.

**Преимущества вложенных классов:**
- Группировка логически связанных классов
- Повышение инкапсуляции (вложенный класс может иметь доступ к приватным членам внешнего)
- Улучшение читаемости кода

В Java есть несколько видов вложенных классов:

| Вид | Ключевое слово | Доступ к внешнему классу |
|-----|----------------|--------------------------|
| Нестатический внутренний класс | (без `static`) | Да, ко всем членам |
| Статический вложенный класс | `static` | Нет (только к статическим) |

Давайте разберём каждый из этих видов подробнее.

### 1.2 Нестатический внутренний класс (Non-static Inner Class)

Нестатический внутренний класс — это класс, объявленный внутри другого класса **без** ключевого слова `static`. Он **всегда связан с экземпляром** внешнего класса.

**Аналогия:** Представьте строение дома. Комнаты внутри дома — это внутренние классы. Комната не существует без дома (внешнего класса), но у неё есть доступ ко всем ресурсам дома (электричество, водоснабжение — приватные поля). Вы не можете построить комнату, не построив сначала сам дом.

```java
class Outer {
    private String secret = "секрет внешнего класса";

    public class Inner {
        public void showSecret() {
            System.out.println("Доступ из Inner: " + secret);
        }
    }

    public static void runInnerExample() {
        Outer outer = new Outer();
        Outer.Inner inner = outer.new Inner();
        inner.showSecret();
    }
}
```

**Важно:** Чтобы создать экземпляр нестатического внутреннего класса извне, нужен экземпляр внешнего класса (`outer.new Inner()`).

**Историческое ограничение (до Java 16):** Нестатический внутренний класс **не мог содержать статических членов** (статических полей, методов и вложенных классов), за исключением `static final` констант времени компиляции. **Начиная с Java 16** (JEP 395) это ограничение снято — внутренние классы могут объявлять статические поля и методы:
```java
class Outer {
    class Inner {
        static final int CONSTANT = 42;  // OK — константа времени компиляции (всегда работало)
        static int counter = 0;          // OK начиная с Java 16 (JEP 395)
    }
}
```

Обратите внимание на то, как работает разрешение имён, когда переменные с одинаковым именем существуют на разных уровнях — во внешнем классе, во внутреннем классе и в локальной области:

**Ссылка на внешний класс из внутреннего:**
```java
class Outer {
    int x = 10;

    class Inner {
        int x = 20;

        void display() {
            int x = 30;
            System.out.println(x);           // 30 — локальная переменная
            System.out.println(this.x);      // 20 — поле Inner
            System.out.println(Outer.this.x); // 10 — поле Outer
        }
    }
}
```

### 1.3 Статический вложенный класс (Static Nested Class)

Статический вложенный класс объявляется с ключевым словом `static`. Он **не связан** с экземпляром внешнего класса и не имеет доступа к нестатическим членам внешнего класса. В отличие от нестатического внутреннего класса, статический вложенный **может содержать как статические, так и нестатические члены**.

**Аналогия:** Статический вложенный класс — это как отдельный офис внутри здания компании. Он находится в том же здании (внешнем классе), но работает самостоятельно и не зависит от конкретного этажа (экземпляра внешнего класса). Он может пользоваться общими ресурсами здания (статическими полями), но не имеет ключей от чужих кабинетов (нестатических полей).

```java
class Container {
    static int staticValue = 42;

    static class StaticNested {
        void printInfo() {
            System.out.println("Статическое значение: " + staticValue);
        }
    }

    public static void runStaticNestedExample() {
        Container.StaticNested nested = new Container.StaticNested();
        nested.printInfo();
    }
}
```

Один из самых частых случаев использования статических вложенных классов на практике — паттерн Builder. Давайте рассмотрим его.

**Практический пример — Builder pattern:**
```java
public class Person {
    private final String firstName;
    private final String lastName;
    private final int age;

    private Person(Builder builder) {
        this.firstName = builder.firstName;
        this.lastName = builder.lastName;
        this.age = builder.age;
    }

    // Статический вложенный класс Builder
    public static class Builder {
        private String firstName;
        private String lastName;
        private int age;

        public Builder firstName(String firstName) {
            this.firstName = firstName;
            return this;
        }

        public Builder lastName(String lastName) {
            this.lastName = lastName;
            return this;
        }

        public Builder age(int age) {
            this.age = age;
            return this;
        }

        public Person build() {
            return new Person(this);
        }
    }

    @Override
    public String toString() {
        return firstName + " " + lastName + " (" + age + ")";
    }
}

// Использование:
Person person = new Person.Builder()
    .firstName("Иван")
    .lastName("Петров")
    .age(25)
    .build();
System.out.println(person); // Иван Петров (25)
```

**Дополнительно:** Вложенные классы (как статические, так и нестатические) могут наследоваться от других классов, **не связанных** с внешним классом, а также реализовывать любые интерфейсы, включая вложенные.

---

## Часть 2: Вложенные интерфейсы (Nested Interfaces)

Теперь, когда мы разобрались с вложенными классами, давайте поговорим о вложенных интерфейсах. Идея похожа: интерфейс можно объявить внутри класса или внутри другого интерфейса.

**Особенности вложенных интерфейсов:**
- Вложенный интерфейс **всегда является `static`** по умолчанию, даже если это явно не указано
- Вложенный интерфейс внутри класса может быть любой видимости (`public`, `private`, `protected`, package-private)
- Вложенный интерфейс внутри интерфейса **всегда** неявно `public static`
- Вложенный интерфейс может быть реализован как самим внешним классом, так и **любым другим классом**

```java
// Вложенный интерфейс внутри класса
class Machine {
    public interface PowerSwitch {
        void turnOn();
        void turnOff();
    }

    public static class Engine implements PowerSwitch {
        public void turnOn() {
            System.out.println("Двигатель включён");
        }

        public void turnOff() {
            System.out.println("Двигатель выключен");
        }
    }

    public static void runInterfaceInClassExample() {
        PowerSwitch ps = new Engine();
        ps.turnOn();
        ps.turnOff();
    }
}
```

**Вложенный интерфейс внутри интерфейса:**
```java
// Вложенный интерфейс внутри интерфейса (неявно public static)
interface Device {
    void start();

    interface Status {
        int READY = 1;
        int ERROR = -1;
    }
}

class Printer implements Device {
    public void start() {
        System.out.println("Принтер запущен. Статус: " + Status.READY);
    }

    public static void runInterfaceInInterfaceExample() {
        new Printer().start();
    }
}
```

---

## Часть 3: Обобщения (Generics)

Переходим к одной из самых мощных и в то же время непростых тем в Java — обобщениям. Если вложенные классы помогают нам организовать код, то обобщения позволяют сделать его по-настоящему универсальным и типобезопасным.

### 3.1 Зачем нужны обобщения?

До появления обобщений в Java 5 коллекции работали с типом `Object`, что порождало проблемы:

```java
// БЕЗ обобщений (Java до 5):
List list = new ArrayList();
list.add("Строка");
list.add(42);           // Можно добавить что угодно!

String s = (String) list.get(0);  // Нужно приведение типа
Integer i = (Integer) list.get(0); // ClassCastException в рантайме!
```

Вы могли заметить, что такой код компилируется без ошибок, но падает при выполнении. Это самый неприятный вид ошибок — те, которые обнаруживаются только во время работы программы. Обобщения решают именно эту проблему.

**С обобщениями (Java 5+):**
```java
List<String> list = new ArrayList<>();
list.add("Строка");
// list.add(42); // Ошибка КОМПИЛЯЦИИ — безопасно!

String s = list.get(0); // Приведение не нужно
```

**Обобщения обеспечивают:**
1. **Типобезопасность** на этапе компиляции
2. **Устранение приведения типов** (`cast`)
3. **Возможность написания универсального кода**

### 3.2 Параметры типа

Обобщённый класс принимает один или несколько параметров типа:

```java
// Обобщённый класс — хранит значение любого типа
class Box<T> {
    private T value;

    public void set(T value) {
        this.value = value;
    }

    public T get() {
        return value;
    }
}

// Обобщённый интерфейс
interface Transformer<T> {
    T transform(T input);
}

class UpperCaseTransformer implements Transformer<String> {
    public String transform(String input) {
        return input.toUpperCase();
    }
}

// Использование:
Box<String> strBox = new Box<>();
strBox.set("Привет");
System.out.println("Box: " + strBox.get());

Transformer<String> transformer = new UpperCaseTransformer();
System.out.println("Transform: " + transformer.transform("hello"));
```

**Принятые соглашения по именованию параметров типа:**

| Буква | Значение |
|-------|----------|
| `T` | Type (тип общего назначения) |
| `E` | Element (элемент коллекции) |
| `K` | Key (ключ Map) |
| `V` | Value (значение Map) |
| `N` | Number (числовой тип) |
| `R` | Return type (тип возвращаемого значения) |

### 3.3 Ограниченные параметры типа (Bounded Type Parameters)

Иногда нам нужно не просто любое значение типа `T`, а значение с определёнными свойствами. Можно ограничить параметр типа с помощью `extends`:

```java
// T должен быть Number или его наследником
class NumberBox<T extends Number> {
    private T number;

    public NumberBox(T number) {
        this.number = number;
    }

    // Можем вызывать методы Number, так как T extends Number
    public double doubleValue() {
        return number.doubleValue();
    }
}

// Использование:
NumberBox<Integer> nb = new NumberBox<>(123);
System.out.println("Double value: " + nb.doubleValue());

// Ошибка компиляции:
// NumberBox<String> strBox = new NumberBox<>("text");
```

**Множественные ограничения:**
```java
// T должен реализовывать оба интерфейса
public <T extends Comparable<T> & Cloneable> T max(T a, T b) {
    return a.compareTo(b) >= 0 ? a : b;
}
```

### 3.4 Обобщённые методы

Обобщения можно применять не только к классам, но и к отдельным методам:

```java
public class Utils {

    // Обобщённый метод — тип T определяется при вызове
    public static <T> void swap(T[] array, int i, int j) {
        T temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }

    // Обобщённый метод с ограничением
    public static <T extends Comparable<T>> T findMax(T[] array) {
        if (array == null || array.length == 0) {
            throw new IllegalArgumentException("Массив пуст");
        }
        T max = array[0];
        for (T element : array) {
            if (element.compareTo(max) > 0) {
                max = element;
            }
        }
        return max;
    }
}

// Использование:
Integer[] numbers = {3, 1, 4, 1, 5, 9, 2, 6};
Utils.swap(numbers, 0, 7);  // [6, 1, 4, 1, 5, 9, 2, 3]

String maxStr = Utils.findMax(new String[]{"banana", "apple", "cherry"});
System.out.println(maxStr); // cherry
```

### 3.5 Стирание типов (Type Erasure)

Это важный момент: **параметры типа существуют только во время компиляции**. В байт-коде они заменяются на `Object` (или на верхнюю границу, если указана). Этот механизм называется стиранием типов.

**Почему так?** Для обратной совместимости с кодом, написанным до Java 5.

```java
List<String> strings = new ArrayList<>();
List<Integer> integers = new ArrayList<>();

// В байт-коде оба будут ArrayList
System.out.println(strings.getClass() == integers.getClass()); // true!

// Нельзя:
// if (obj instanceof List<String>) {} // Ошибка компиляции!

// Можно (без параметра типа):
if (obj instanceof List<?>) {} // OK
```

**Следствия стирания типов — что нельзя делать с параметрами типа:**
```java
public class Container<T> {
    // НЕЛЬЗЯ:
    // T obj = new T();           // Нельзя создавать экземпляры T
    // T[] array = new T[10];     // Нельзя создавать массивы T
    // if (obj instanceof T) {}   // Нельзя использовать instanceof с T
    // Class<T> c = T.class;      // Нельзя получить класс T

    // МОЖНО:
    T value;                      // Можно объявлять переменные типа T
    List<T> list = new ArrayList<>(); // Можно создавать коллекции
}
```

**Демонстрация стирания типов во время исполнения:**
```java
class TypeErasureDemo<T> {
    public void check(Object obj) {
        // if (obj instanceof T) {} — Ошибка: нельзя использовать instanceof с параметром типа
        System.out.println("Тип T стёрт до Object на этапе исполнения");
    }
}

// Использование:
TypeErasureDemo<String> ted = new TypeErasureDemo<>();
ted.check("Test");
```

**Подклассы могут расширять обобщённые классы двумя способами:**
```java
// 1. С конкретизацией типа — фиксируем T как String:
class StringBox extends Box<String> {}

// 2. С сохранением параметра типа — T передаётся дальше:
class GenericBox<T> extends Box<T> {}

// Использование:
StringBox sb = new StringBox();
sb.set("Generic Java");
System.out.println("StringBox: " + sb.get());

GenericBox<Double> gb = new GenericBox<>();
gb.set(3.14);
System.out.println("GenericBox<Double>: " + gb.get());
```

### 3.6 Wildcards (Подстановочные знаки)

Wildcard `?` означает "неизвестный тип". Он используется при работе с коллекциями разных типов. Давайте разберём три варианта использования wildcards.

#### Неограниченный Wildcard `?`

```java
class WildcardDemo {
    // Метод печатает любой List, независимо от типа элементов
    public static void printList(List<?> list) {
        for (Object obj : list) {
            System.out.println("Элемент: " + obj);
        }
    }
}

// Использование:
List<String> words = Arrays.asList("one", "two", "three");
WildcardDemo.printList(words); // OK для любого List<?>
```

#### Upper Bounded Wildcard `? extends T`

**"Producer Extends"** — когда вы хотите **читать** из коллекции элементы типа T или его подтипов:

```java
class WildcardDemo {
    // Сумма всех чисел в списке (работает с List<Integer>, List<Double> и т.д.)
    public static double sumNumbers(List<? extends Number> list) {
        double sum = 0;
        for (Number n : list) {    // Безопасно читать как Number
            sum += n.doubleValue();
        }
        return sum;
    }
}

List<Integer> nums = Arrays.asList(1, 2, 3);
System.out.println("Сумма: " + WildcardDemo.sumNumbers(nums)); // 6.0

// НЕЛЬЗЯ добавлять в список с ? extends:
// list.add(5);  // Ошибка! Тип неизвестен (может быть List<Integer>, List<Double>...)
```

#### Lower Bounded Wildcard `? super T`

**"Consumer Super"** — когда вы хотите **записывать** в коллекцию элементы типа T:

```java
class WildcardDemo {
    // Добавляет числа в список (работает с List<Number>, List<Object>)
    public static void addIntegers(List<? super Integer> list) {
        list.add(10);  // Безопасно добавлять Integer
        list.add(20);
    }
}

List<Number> numberList = new ArrayList<>();
WildcardDemo.addIntegers(numberList); // OK
System.out.println("После добавления целых чисел: " + numberList);
// addIntegers(new ArrayList<Double>()); // Ошибка! Double не является super Integer
```

#### Мнемоническое правило PECS

Чтобы легко запомнить, когда какой wildcard использовать, воспользуйтесь правилом PECS:

**P**roducer **E**xtends, **C**onsumer **S**uper:
- Если структура **производит** данные (вы из неё читаете) → `? extends T`
- Если структура **потребляет** данные (вы в неё пишете) → `? super T`

```java
// Классический пример: копирование коллекции
public static <T> void copy(List<? super T> dest, List<? extends T> src) {
    for (T item : src) {   // src — producer, читаем из него
        dest.add(item);    // dest — consumer, пишем в него
    }
}
```

---

## Часть 4: Исключения (Exceptions)

Мы научились писать универсальный код с обобщениями, но даже самый хорошо типизированный код может столкнуться с непредвиденными ситуациями: файл не найден, сеть недоступна, пользователь ввёл некорректные данные. Для обработки таких ситуаций в Java существует система исключений.

### 4.1 Иерархия исключений

В Java исключения — это объекты. Все они наследуют от класса `Throwable`:

```
Throwable
├── Error (непроверяемые — не нужно обрабатывать)
│   ├── OutOfMemoryError
│   ├── StackOverflowError
│   └── AssertionError
│
└── Exception
    ├── RuntimeException (непроверяемые — unchecked)
    │   ├── NullPointerException
    │   ├── ArrayIndexOutOfBoundsException
    │   ├── ClassCastException
    │   ├── IllegalArgumentException
    │   ├── IllegalStateException
    │   └── ArithmeticException
    │
    └── Другие Exception (проверяемые — checked)
        ├── IOException
        │   ├── FileNotFoundException
        │   └── EOFException
        ├── SQLException
        └── ParseException
```

### 4.2 Checked vs Unchecked исключения

| Критерий | Checked | Unchecked |
|----------|---------|-----------|
| Наследуют от | `Exception` (но не `RuntimeException`) | `RuntimeException` или `Error` |
| Компилятор требует обработки | **Да** | Нет |
| Когда возникают | Предсказуемые ситуации (файл не найден, нет подключения) | Ошибки программиста (null, выход за границы массива) |
| Примеры | `IOException`, `SQLException` | `NPE`, `ArrayIndexOutOfBoundsException` |

**Философия:**
- **Checked** — "ожидаемые" проблемы, которые программа должна уметь обработать. Компилятор *заставляет* вас подумать об этих случаях.
- **Unchecked** — ошибки в коде, которые нужно **исправить**, а не обрабатывать. Например, `NullPointerException` означает ошибку программиста, а не внешнее условие.

### 4.3 Блок try-catch-finally

Давайте посмотрим, как выглядит обработка исключений на практике:

```java
class ExceptionFlowDemo {
    public void riskyMethod() throws IOException {
        throw new IOException("Ошибка ввода-вывода");
    }

    public void showFlow() {
        try {
            riskyMethod();
        } catch (IOException e) {
            System.out.println("Обработка IOException: " + e.getMessage());
        } finally {
            System.out.println("Блок finally выполнен");
        }
    }
}

// Использование:
new ExceptionFlowDemo().showFlow();
```

**Важные правила:**
- `catch` блоки проверяются **по порядку** — первый подходящий будет выполнен
- Более специфичные исключения должны идти **перед** более общими
- `finally` выполняется **всегда**, даже если было исключение, даже если в `catch` тоже возникло исключение

**Multi-catch (Java 7+):**
```java
try {
    // ...
} catch (IOException | SQLException e) {
    // Обработка нескольких типов в одном блоке
    System.out.println("Ошибка ввода/вывода или БД: " + e.getMessage());
}
```

### 4.4 Методы класса Throwable

```java
try {
    int[] arr = new int[5];
    arr[10] = 1; // ArrayIndexOutOfBoundsException
} catch (ArrayIndexOutOfBoundsException e) {
    System.out.println(e.getMessage());    // Сообщение об ошибке
    System.out.println(e.getClass().getName()); // Полное имя класса
    e.printStackTrace();                   // Полный стек вызовов в stderr
}
```

### 4.5 Оператор throw

`throw` используется для **явного бросания** исключения:

```java
// Unchecked exception — бросается неявно при делении на ноль
class Divider {
    public int divide(int a, int b) {
        return a / b; // может вызвать ArithmeticException
    }
}

// Checked exception — явно бросается через throw
class InvalidAgeException extends Exception {
    public InvalidAgeException(String msg) {
        super(msg);
    }
}

class Voter {
    public void register(int age) throws InvalidAgeException {
        if (age < 18)
            throw new InvalidAgeException("Возраст должен быть 18+");
        System.out.println("Регистрация успешна!");
    }
}

// Использование:
Divider d = new Divider();
try {
    System.out.println("Результат: " + d.divide(10, 0));
} catch (ArithmeticException e) {
    System.out.println("Ошибка: " + e.getMessage());
}

Voter voter = new Voter();
try {
    voter.register(16);
} catch (InvalidAgeException e) {
    System.out.println("Ошибка регистрации: " + e.getMessage());
}
```

### 4.6 Ключевое слово throws

Обратите внимание на разницу между `throw` и `throws` — это одно из мест, где начинающие часто путаются. `throw` бросает исключение, а `throws` в сигнатуре метода **объявляет**, что метод **может бросить** checked исключение:

```java
// Метод объявляет, что может бросить IOException
public String readFile(String path) throws IOException {
    // FileReader бросает FileNotFoundException (наследник IOException)
    FileReader fr = new FileReader(path);
    // ... чтение файла
    return content;
}

// Вызывающий код ОБЯЗАН обработать или пробросить дальше
public void processFile() {
    try {
        String content = readFile("data.txt");
        System.out.println(content);
    } catch (IOException e) {
        System.out.println("Файл не найден: " + e.getMessage());
    }
}

// ИЛИ пробросить дальше:
public void processFile() throws IOException {
    String content = readFile("data.txt"); // Пробрасываем вверх по стеку
}
```

### 4.7 Создание собственных исключений

Иногда стандартных исключений недостаточно, и нам нужно описать специфичную для нашей предметной области ошибку. В таких случаях создаём собственный класс исключения:

```java
// Checked исключение — наследуем от Exception
class InvalidAgeException extends Exception {
    public InvalidAgeException(String msg) {
        super(msg);
    }
}

class Voter {
    public void register(int age) throws InvalidAgeException {
        if (age < 18)
            throw new InvalidAgeException("Возраст должен быть 18+");
        System.out.println("Регистрация успешна!");
    }
}

// Использование:
Voter voter = new Voter();
try {
    voter.register(16);
} catch (InvalidAgeException e) {
    System.out.println("Ошибка регистрации: " + e.getMessage());
}
```

### 4.8 Try-with-resources (Java 7+)

Ресурсы (файлы, соединения с БД, сетевые сокеты) должны быть закрыты после использования. Без try-with-resources это выглядит громоздко:

```java
// Без try-with-resources — много boilerplate кода:
FileReader fr = null;
try {
    fr = new FileReader("file.txt");
    // чтение...
} catch (IOException e) {
    e.printStackTrace();
} finally {
    if (fr != null) {
        try {
            fr.close(); // close() тоже может бросить IOException!
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

Согласитесь, выглядит довольно громоздко. К счастью, начиная с Java 7, появилась конструкция try-with-resources, которая делает всё гораздо элегантнее.

**С try-with-resources — элегантно и безопасно:**
```java
// Ресурс автоматически закрывается при выходе из блока try
try (FileReader fr = new FileReader("file.txt");
     BufferedReader br = new BufferedReader(fr)) {

    String line;
    while ((line = br.readLine()) != null) {
        System.out.println(line);
    }
} catch (IOException e) {
    System.out.println("Ошибка чтения: " + e.getMessage());
}
// fr и br автоматически закрыты здесь, даже если было исключение
```

**Требование:** класс ресурса должен реализовывать интерфейс `AutoCloseable` (или `Closeable`):

```java
class ResourceDemo {
    public void readFromFile(String path) {
        try (BufferedReader br = new BufferedReader(new FileReader(path))) {
            System.out.println("Первая строка: " + br.readLine());
        } catch (IOException e) {
            System.out.println("Ошибка чтения: " + e.getMessage());
        }
    }
}

// Использование:
new ResourceDemo().readFromFile("example.txt");
// BufferedReader закрывается автоматически при выходе из блока try
```

### 4.9 Цепочка исключений (Exception Chaining)

Часто полезно сохранить оригинальное исключение при выбрасывании нового. Это позволяет не терять информацию о первопричине ошибки при перемещении между уровнями абстракции:

```java
public void loadUserData(int userId) throws DataLoadException {
    try {
        // Чтение из базы данных
        database.findUser(userId);
    } catch (SQLException e) {
        // Оборачиваем низкоуровневое исключение в высокоуровневое
        throw new DataLoadException("Не удалось загрузить данные пользователя " + userId, e);
    }
}

// Пользовательское исключение с причиной:
public class DataLoadException extends Exception {
    public DataLoadException(String message, Throwable cause) {
        super(message, cause); // Сохраняем исходное исключение
    }
}

// При выводе стека будет видна полная цепочка:
// DataLoadException: Не удалось загрузить данные пользователя 5
//   Caused by: SQLException: Connection refused
```

---

## Часть 5: Практические паттерны использования

Мы рассмотрели много теории. Теперь давайте закрепим всё, что изучили, обратив внимание на типичные решения и рекомендации.

### 5.1 Когда использовать нестатический vs статический вложенный класс?

**Нестатический внутренний класс** — когда:
- Вложенный класс нужен только вместе с внешним
- Нужен доступ к нестатическим членам внешнего класса
- Пример: `Iterator` внутри `LinkedList`

**Статический вложенный класс** — когда:
- Класс логически принадлежит внешнему, но может работать самостоятельно
- Вложенный класс не нужен экземпляр внешнего
- Примеры: `Builder`, `Entry` в `HashMap`, вспомогательные классы

### 5.2 Стратегия обработки исключений

```java
// ПРАВИЛЬНО: ловим конкретное исключение, обрабатываем осмысленно
try {
    int value = Integer.parseInt(input);
    process(value);
} catch (NumberFormatException e) {
    System.out.println("Введите корректное число");
} catch (ProcessingException e) {
    logger.error("Ошибка обработки", e);
    throw new ServiceException("Сервис недоступен", e);
}

// НЕПРАВИЛЬНО: ловим Exception и игнорируем
try {
    process(input);
} catch (Exception e) {
    // Не делайте так! "Swallowing exceptions"
}
```

**Правило:** Никогда не игнорируйте исключения молча. Как минимум — залогируйте их.

---

## Часть 6: Итоги

| Концепция | Ключевая идея |
|-----------|---------------|
| Нестатический внутренний класс | Связан с экземпляром внешнего, имеет доступ ко всем членам |
| Статический вложенный класс | Независим от экземпляра внешнего, доступ только к статическим членам |
| Вложенный интерфейс | Группирует контракты с внешним классом/интерфейсом |
| Обобщения | Типобезопасность на этапе компиляции |
| Стирание типов | Параметры типа удаляются в байт-коде |
| `? extends T` | Для чтения (Producer) |
| `? super T` | Для записи (Consumer) |
| Checked исключения | Обязательно обрабатывать, наследники Exception |
| Unchecked исключения | Ошибки кода, наследники RuntimeException |
| try-with-resources | Автоматическое закрытие ресурсов (AutoCloseable) |

---

## Часть 7: Дополнительные примеры

Чтобы увидеть, как все изученные концепции работают вместе, давайте рассмотрим полноценный пример обобщённого репозитория — шаблон, который часто встречается в реальных проектах.

### Полный пример с обобщённым репозиторием

```java
// Интерфейс с обобщениями
public interface Repository<T, ID> {
    void save(T entity);
    Optional<T> findById(ID id);
    List<T> findAll();
    void delete(ID id);
}

// Реализация для конкретного типа
public class UserRepository implements Repository<User, Long> {
    private Map<Long, User> storage = new HashMap<>();
    private long nextId = 1;

    @Override
    public void save(User user) {
        if (user.getId() == null) {
            user.setId(nextId++);
        }
        storage.put(user.getId(), user);
    }

    @Override
    public Optional<User> findById(Long id) {
        return Optional.ofNullable(storage.get(id));
    }

    @Override
    public List<User> findAll() {
        return new ArrayList<>(storage.values());
    }

    @Override
    public void delete(Long id) {
        if (!storage.containsKey(id)) {
            throw new EntityNotFoundException("Пользователь не найден: " + id);
        }
        storage.remove(id);
    }
}
```
