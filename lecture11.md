# Лекция 11: Паттерны и антипаттерны проектирования

## Введение

Добро пожаловать на 11-ю лекцию курса «Современные технологии программирования». За предыдущие лекции мы набрали внушительный арсенал: синтаксис Java и ООП, коллекции и потоки, системы сборки, JDBC и Hibernate, Spring и Spring Boot, документирование и тестирование. Вы умеете написать работающее приложение. Сегодня разговор пойдёт о другом — о том, как написать приложение, которое не превратится в кошмар через полгода поддержки.

Разница здесь примерно как между «уметь класть кирпичи» и «уметь проектировать дом». Кирпичи вы класть научились. Но если строить без чертежа, через год выяснится, что несущую стену снести нельзя, окна прорубать некуда, а пристроить веранду можно, только разобрав половину здания. В программировании так же: код, который «просто работает», очень быстро становится кодом, который страшно трогать.

**Паттерны проектирования (design patterns)** — это проверенные решения типовых задач проектирования. Их не изобретают заново на каждом проекте, их узнают и применяют. **Антипаттерны (antipatterns)** — наоборот, типовые решения, которые кажутся разумными, но систематически приводят к беде.

Сегодня мы разберём принципы SOLID, 23 классических паттерна «банды четырёх» и десять самых частых антипаттернов. И, что важнее всего, увидим, что все эти паттерны вы уже применяли. Каждый раз, когда писали `new BufferedReader(new FileReader(file))`, вы использовали Декоратор. Каждый раз, когда ставили `@Transactional`, за вас работал Заместитель. Сегодня мы дадим этим вещам имена.

---

## Часть 1: Что такое паттерн проектирования

### 1.1 Общий словарь профессии

Представьте разговор двух строителей: «здесь нужна несущая стена, а тут — вентилируемый фасад». Два слова — и оба понимают целый комплекс решений: материалы, нагрузки, технологию монтажа. Объяснять конструкцию с нуля не требуется.

Паттерн — такое же слово в словаре программиста. Когда на код-ревью вы пишете «здесь напрашивается Стратегия», коллега мгновенно понимает: нужно вынести варьирующийся алгоритм в отдельный интерфейс, а класс-клиент должен получать реализацию извне. Без общего словаря на это ушло бы три абзаца.

Формально паттерн описывается четырьмя вещами:

| Элемент | Что означает |
|---------|--------------|
| **Название** | Слово из общего словаря: Singleton, Observer, Facade |
| **Задача** | В какой ситуации паттерн уместен, какую проблему решает |
| **Решение** | Структура классов и их взаимодействие (не конкретный код) |
| **Последствия** | Что вы получаете и чем за это платите |

Обратите внимание на третий пункт: паттерн — это **не готовый код для копирования**, а идея структуры. В каждом проекте она реализуется по-своему, и в современной Java часто выглядит совсем не так, как в каноническом описании из книги 1994 года.

### 1.2 «Банда четырёх» и три группы паттернов

В 1994 году Эрих Гамма, Ричард Хелм, Ральф Джонсон и Джон Влиссидес выпустили книгу «Design Patterns: Elements of Reusable Object-Oriented Software». За авторами закрепилось прозвище **«банда четырёх» (Gang of Four, GoF)**, а за описанными в ней 23 паттернами — статус классики.

| Группа | Чем занимается | Паттерны |
|--------|----------------|----------|
| **Порождающие** (Creational) | Как создавать объекты | Singleton, Factory Method, Abstract Factory, Builder, Prototype |
| **Структурные** (Structural) | Как собирать объекты в структуры | Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy |
| **Поведенческие** (Behavioral) | Как объекты взаимодействуют и распределяют обязанности | Chain of Responsibility, Command, Interpreter, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, Visitor |

Логика деления простая. Порождающие отвечают на вопрос «откуда взялся объект», структурные — «из чего он состоит», поведенческие — «как объекты договариваются между собой».

### 1.3 Когда паттерн вредит

Самая частая ошибка студента, только что прочитавшего книгу по паттернам, — применять их везде. Результат предсказуем: вместо одного класса на 30 строк появляется шесть интерфейсов, три фабрики и конфигурационный файл — и всё это, чтобы сложить два числа.

Это называется **избыточным усложнением (over-engineering)**. Паттерн — лекарство, а у любого лекарства есть побочные эффекты: лишние классы, лишний уровень косвенности, более сложная отладка. Здоровому коду лекарство не нужно.

1. **Правило трёх.** Не выносите абстракцию, пока не увидели три реальных случая её использования. Один — пишите прямо. Два — потерпите. Три — обобщайте.
2. **YAGNI (You Aren't Gonna Need It).** Не проектируйте фабрику под пять будущих СУБД, если сейчас у вас одна и переезд не планируется.
3. **Паттерн — ответ на боль, а не на красоту.** Не можете назвать конкретную проблему, которую вводимый паттерн решает, — значит, проблемы нет.

Хороший индикатор: если после введения паттерна код стало *легче менять* — паттерн уместен. Если читать стало сложнее, а менять легче не стало, вы усложнили на пустом месте.

---

## Часть 2: Принципы SOLID — фундамент паттернов

**SOLID** — акроним из пяти принципов объектно-ориентированного проектирования, сформулированных Робертом Мартином. Почти каждый паттерн GoF — способ соблюсти один или несколько из них.

Аналогия для всей части: кухня ресторана. Если один повар отвечает и за салаты, и за горячее, и за десерты, и за мытьё посуды, кухня встанет, как только он заболеет. Если каждый отвечает за своё, а взаимодействуют они через понятные интерфейсы («заказ на раздачу»), кухня работает даже при замене людей. SOLID — правила организации такой кухни, только для классов.

### 2.1 S — Single Responsibility Principle (принцип единственной ответственности)

**У класса должна быть только одна причина для изменения.**

```java
// Плохо: класс делает три разные вещи
public class SalesReport {
    private final List<Double> amounts;
    public SalesReport(List<Double> amounts) { this.amounts = amounts; }
    // Причина изменения №1: поменялись правила расчёта
    public double total() { return amounts.stream().mapToDouble(Double::doubleValue).sum(); }
    // Причина изменения №2: поменялась вёрстка отчёта
    public String toHtml() { return "<h1>Итого: " + total() + "</h1>"; }
    // Причина изменения №3: сменили почтовый сервис
    public void sendByEmail(String address) { System.out.println(address + ": " + toHtml()); }
}
```

Такой класс правят и бухгалтеры, и вёрстальщики, и админы почты — три команды в одном файле, три источника конфликтов при слиянии. Разделяем по причинам изменения:

```java
// Три файла пакета ru.fa.patterns.solid; в каждом — своя строка package ru.fa.patterns.solid; и нужные импорты
public class SalesCalculator {
    public double total(List<Double> amounts) {
        return amounts.stream().mapToDouble(Double::doubleValue).sum();
    }
}

public class HtmlReportRenderer {
    public String render(double total) { return "<h1>Итого: " + total + "</h1>"; }
}

public class ReportMailer {
    public void send(String address, String body) { System.out.println(address + ": " + body); }
}
```

Строк стало больше — это нормальная цена. Зато изменение правил расчёта теперь не может случайно сломать вёрстку.

### 2.2 O — Open/Closed Principle (принцип открытости/закрытости)

**Классы должны быть открыты для расширения, но закрыты для изменения.**

Аналогия — удлинитель с розетками. Чтобы подключить новый прибор, вы не разбираете удлинитель и не паяете провода: просто втыкаете вилку. Розетка открыта для расширения, но закрыта для изменения.

```java
// Плохо: каждая новая фигура требует правки этого метода
public class AreaCalculator {
    public double area(Object shape) {
        if (shape instanceof Circle c) return Math.PI * c.radius() * c.radius();
        if (shape instanceof Square s) return s.side() * s.side();
        throw new IllegalArgumentException("Неизвестная фигура: " + shape);
    }
}
```

```java
// Четыре файла пакета ru.fa.patterns.solid; в каждом — своя строка package ru.fa.patterns.solid; и нужные импорты
// Хорошо: поведение живёт в самих фигурах
public interface Shape { double area(); }

public record Circle(double radius) implements Shape {
    @Override public double area() { return Math.PI * radius * radius; }
}

public record Square(double side) implements Shape {
    @Override public double area() { return side * side; }
}

public class AreaCalculator {
    // Этот класс не меняется никогда, сколько бы фигур ни добавили
    public double total(List<Shape> shapes) {
        return shapes.stream().mapToDouble(Shape::area).sum();
    }
}
```

Добавили треугольник — написали новый `record Triangle implements Shape`. Существующий код не тронут, а значит, не сломан. На этом принципе построены Стратегия, Шаблонный метод и Фабричный метод.

### 2.3 L — Liskov Substitution Principle (принцип подстановки Лисков)

**Объект подкласса должен быть подставим вместо объекта базового класса без нарушения работы программы.**

Если код написан для `Птица`, передача в него `Пингвин` не должна ломать логику. А если `Пингвин.летать()` бросает исключение, значит, `Пингвин` не является `Птица` в том смысле, в каком её понимает код.

```java
// Два файла пакета ru.fa.patterns.solid; в каждом — своя строка package ru.fa.patterns.solid; и нужные импорты
public class Rectangle {
    protected int width;
    protected int height;
    public void setWidth(int width) { this.width = width; }
    public void setHeight(int height) { this.height = height; }
    public int area() { return width * height; }
}

// С точки зрения математики квадрат — прямоугольник. С точки зрения кода — нет
public class Square extends Rectangle {
    @Override public void setWidth(int width) { this.width = width; this.height = width; }
    @Override public void setHeight(int height) { this.width = height; this.height = height; }
}

// Клиентский код, написанный под Rectangle, ломается:
// rectangle.setWidth(5); rectangle.setHeight(4);
// для Rectangle площадь 20, для Square — 16. Контракт нарушен
```

Решение — не наследовать `Square` от `Rectangle`, а сделать оба неизменяемыми реализациями общего интерфейса `Shape` (как в примере с OCP). Неизменяемые (immutable) объекты вообще нарушают LSP гораздо реже: если у объекта нет сеттеров, то нечему и рассогласовываться.

Практический вывод: наследование — это обещание. Наследуя, вы обещаете, что ваш класс ведёт себя как родитель. Не можете выполнить обещание — используйте композицию.

### 2.4 I — Interface Segregation Principle (принцип разделения интерфейсов)

**Клиента нельзя заставлять зависеть от методов, которые он не использует.** Аналогия — пульт от телевизора с пятьюдесятью кнопками, из которых вы жмёте четыре.

```java
// Два файла пакета ru.fa.patterns.solid; в каждом — своя строка package ru.fa.patterns.solid; и нужные импорты
// Плохо: «толстый» интерфейс
public interface Device {
    void print(String document);
    void scan(String document);
    void fax(String document);
}

// Простому принтеру приходится реализовывать то, чего он не умеет
public class SimplePrinter implements Device {
    @Override public void print(String document) { System.out.println("Печать: " + document); }
    @Override public void scan(String document) { throw new UnsupportedOperationException(); }
    @Override public void fax(String document) { throw new UnsupportedOperationException(); }
}
```

```java
// Пять файлов пакета ru.fa.patterns.solid; в каждом — своя строка package ru.fa.patterns.solid; и нужные импорты
// Хорошо: одна роль — один интерфейс
public interface Printer { void print(String document); }
public interface DocScanner { void scan(String document); }
public interface FaxSender { void fax(String document); }

public class SimplePrinter implements Printer {
    @Override public void print(String document) { System.out.println("Печать: " + document); }
}

// МФУ собирает нужные роли
public class MultifunctionDevice implements Printer, DocScanner, FaxSender {
    @Override public void print(String document) { System.out.println("Печать: " + document); }
    @Override public void scan(String document) { System.out.println("Сканирование: " + document); }
    @Override public void fax(String document) { System.out.println("Факс: " + document); }
}
```

`UnsupportedOperationException` в реализации интерфейса — почти всегда сигнал нарушения ISP. Кстати, именно ISP объясняет обилие мелких интерфейсов в JDK: `Comparable`, `Comparator`, `Iterable`, `Runnable`, `AutoCloseable` — каждый описывает одну роль.

### 2.5 D — Dependency Inversion Principle (принцип инверсии зависимостей)

**Модули верхнего уровня не должны зависеть от модулей нижнего уровня. Оба должны зависеть от абстракций.**

Вспомните розетку: чайник не припаян к проводке дома. И чайник, и проводка зависят от стандарта розетки — абстракции, о которой договорились обе стороны. Поэтому чайник можно заменить, не трогая проводку.

```java
// Плохо: сервис намертво привязан к конкретной реализации
public class OrderService {
    private final MySqlOrderRepository repository = new MySqlOrderRepository();
    public void placeOrder(String orderId) { repository.save(orderId); }
}
```

```java
// Три файла пакета ru.fa.patterns.solid; в каждом — своя строка package ru.fa.patterns.solid; и нужные импорты
// Хорошо: абстракция принадлежит верхнему уровню
public interface OrderRepository { void save(String orderId); }

public class MySqlOrderRepository implements OrderRepository {
    @Override public void save(String orderId) { System.out.println("Сохраняем " + orderId); }
}

public class OrderService {
    private final OrderRepository repository;
    // Зависимость приходит извне — это и есть внедрение зависимостей
    public OrderService(OrderRepository repository) { this.repository = repository; }
    public void placeOrder(String orderId) { repository.save(orderId); }
}
```

Здесь мы напрямую выходим на материал Лекции 7. **Внедрение зависимостей (Dependency Injection)**, которое делает за нас Spring, — это техническая реализация DIP. Когда вы помечаете класс аннотацией `@Service` и принимаете `OrderRepository` в конструкторе, контейнер сам находит реализацию и передаёт её. Ваш сервис не знает и не хочет знать, работает ли под ним PostgreSQL, H2 в тестах или заглушка Mockito. Именно поэтому Spring-приложения так легко тестировать: в юнит-тесте вы просто передаёте в конструктор мок.

Различайте три термина, их часто путают: **DIP** — принцип (зависеть от абстракций), **DI** — техника (получать зависимости извне), **IoC** — более общий принцип инверсии управления, частным случаем которого является DI.

### 2.6 SOLID одной таблицей

Мы разобрали все пять принципов подробно — теперь сведём их в шпаргалку, по которой удобно быстро проверять код на нарушения:

| Принцип | Формулировка | Главный симптом нарушения |
|---------|--------------|---------------------------|
| **SRP** | Одна причина для изменения | Класс правят разные команды по разным поводам |
| **OCP** | Открыт для расширения, закрыт для изменения | Длинная цепочка `if/instanceof` или `switch` по типу |
| **LSP** | Подкласс подставим вместо родителя | Переопределённый метод бросает исключение или меняет смысл |
| **ISP** | Не навязывай клиенту лишние методы | `UnsupportedOperationException` в реализации |
| **DIP** | Зависимость от абстракций | `new ConcreteClass()` внутри бизнес-логики |

---

## Часть 3: Порождающие паттерны

Порождающие паттерны отвечают на вопрос «как создать объект, не привязываясь жёстко к его классу». Общая аналогия для части — заказ еды. Можно готовить самому (`new`), можно заказать конкретное блюдо в конкретной пиццерии (Фабричный метод), можно выбрать целую кухню — итальянскую или японскую (Абстрактная фабрика), а можно собрать бургер по шагам в приложении доставки (Строитель).

### 3.1 Singleton (Одиночка)

**Задача.** Гарантировать, что у класса существует ровно один экземпляр, и дать к нему глобальную точку доступа. Аналогия — пульт от телевизора в комнате. Он один. Если у каждого члена семьи заведётся свой пульт со своим состоянием громкости, начнётся хаос.

Наивная реализация ломается в многопоточной среде: два потока могут одновременно пройти проверку `if (instance == null)` и создать два объекта. Потокобезопасный вариант с **двойной проверкой блокировки (double-checked locking)**:

```java
public final class ConfigRegistry {
    // volatile обязателен: без него другой поток может увидеть
    // ссылку на ещё не до конца сконструированный объект
    private static volatile ConfigRegistry instance;
    private final Map<String, String> values = new ConcurrentHashMap<>();

    private ConfigRegistry() {                       // приватный конструктор
        values.put("app.name", "Онлайн-библиотека");
    }

    public static ConfigRegistry getInstance() {
        ConfigRegistry local = instance;             // читаем volatile-поле один раз
        if (local == null) {
            synchronized (ConfigRegistry.class) {
                local = instance;
                if (local == null) {
                    instance = local = new ConfigRegistry();
                }
            }
        }
        return local;
    }

    public String get(String key) { return values.get(key); }
}
```

Ключевое слово `volatile` здесь не украшение. Без него JVM вправе переупорядочить операции так, что ссылка `instance` станет ненулевой раньше, чем конструктор закончит работу, — и второй поток получит полуготовый объект. Мы разбирали `volatile` в Лекции 5, когда говорили о видимости изменений между потоками.

Более простой и надёжный вариант — через `enum`. Джошуа Блох в «Effective Java» называет его лучшим способом реализовать Singleton:

```java
public enum Configuration {
    INSTANCE;

    private final Map<String, String> values = new ConcurrentHashMap<>();

    public void set(String key, String value) { values.put(key, value); }
    public String get(String key) { return values.get(key); }
}

// Использование: Configuration.INSTANCE.set("app.name", "Библиотека");
```

JVM сама гарантирует, что константа `enum` создаётся ровно один раз и потокобезопасно; вдобавок такой Singleton устойчив к созданию дубликата через рефлексию и сериализацию.

**Где встречается.** В JDK: `Runtime.getRuntime()`, `Desktop.getDesktop()`. В Spring: **все бины по умолчанию имеют scope `singleton`** — контейнер создаёт один экземпляр на весь контекст приложения. Обратите внимание на разницу: Spring-синглтон живёт в контейнере, а не в статическом поле, поэтому его легко подменить в тестах.

**Осторожно.** Singleton — самый переоценённый паттерн. Глобальное состояние затрудняет тестирование (состояние протекает между тестами) и прячет зависимости. В Spring-приложении вам почти никогда не нужен ручной Singleton — используйте бин.

### 3.2 Factory Method (Фабричный метод)

**Задача.** Определить интерфейс для создания объекта, но позволить подклассам решать, какой конкретно класс инстанцировать. Аналогия — сеть пиццерий: головная компания задаёт процесс (принять заказ, приготовить, упаковать, выдать), но что именно готовит миланский филиал, а что неаполитанский — решает филиал.

```java
// Пять файлов пакета ru.fa.patterns.creational; в каждом — своя строка package ru.fa.patterns.creational; и нужные импорты
public interface Notification { void send(String text); }

public class EmailNotification implements Notification {
    @Override public void send(String text) { System.out.println("E-mail: " + text); }
}

public class SmsNotification implements Notification {
    @Override public void send(String text) { System.out.println("SMS: " + text); }
}

public abstract class NotificationDispatcher {
    // Фабричный метод: что создавать — решает подкласс
    protected abstract Notification createNotification();

    // Общий алгоритм, одинаковый для всех подклассов
    public void dispatch(String text) {
        Notification notification = createNotification();
        notification.send(text);
        System.out.println("Уведомление отправлено");
    }
}

public class EmailDispatcher extends NotificationDispatcher {
    @Override protected Notification createNotification() { return new EmailNotification(); }
}
```

**Где встречается.** Настоящий фабричный метод в JDK — `Collection.iterator()`: каждая коллекция сама решает, какой итератор вернуть, и решает это именно подкласс. А вот `Calendar.getInstance()` и `NumberFormat.getInstance()` — не паттерн GoF, а **статические фабричные методы**: выбор класса спрятан внутри одного метода, никакой подкласс в нём не участвует. Разницу мы разберём на практике. В Spring фабричный метод — это интерфейс `FactoryBean` и `BeanFactory` в целом.

### 3.3 Abstract Factory (Абстрактная фабрика)

**Задача.** Создавать целые **семейства** связанных объектов, не привязываясь к их конкретным классам. Разница с Фабричным методом принципиальная: тот создаёт один продукт, Абстрактная фабрика — согласованный набор. Аналогия — комплект мебели: выбрали скандинавский стиль, значит, и стол, и стулья, и шкаф будут скандинавскими. Смешать скандинавский стол с барочным стулом фабрика не даст.

```java
// Семь файлов пакета ru.fa.patterns.creational; в каждом — своя строка package ru.fa.patterns.creational; и нужные импорты
public interface Button { void render(); }
public interface Checkbox { void render(); }

// Семейство «тёмная тема»
public class DarkButton implements Button {
    @Override public void render() { System.out.println("Тёмная кнопка"); }
}
public class DarkCheckbox implements Checkbox {
    @Override public void render() { System.out.println("Тёмный чекбокс"); }
}

// Абстрактная фабрика описывает всё семейство целиком
public interface UiFactory {
    Button createButton();
    Checkbox createCheckbox();
}

public class DarkUiFactory implements UiFactory {
    @Override public Button createButton() { return new DarkButton(); }
    @Override public Checkbox createCheckbox() { return new DarkCheckbox(); }
}

// Клиент знает только интерфейсы — смешать темы он не сможет
public class SettingsDialog {
    private final Button button;
    private final Checkbox checkbox;

    public SettingsDialog(UiFactory factory) {
        this.button = factory.createButton();
        this.checkbox = factory.createCheckbox();
    }

    public void render() { button.render(); checkbox.render(); }
}
```

**Где встречается.** В JDK: `DocumentBuilderFactory`, `TransformerFactory` из пакетов работы с XML — каждая создаёт согласованный набор объектов конкретной реализации парсера.

### 3.4 Builder (Строитель)

**Задача.** Пошагово собирать сложный объект, у которого много необязательных параметров. Проблема, которую он решает, называется «телескопический конструктор»: `new Book(title, author)`, `new Book(title, author, year)`, `new Book(title, author, year, isbn)` — и так до десяти перегрузок, в которых невозможно разобраться. Аналогия — сборка бургера в приложении доставки: отмечаете галочками котлету, сыр, соус и только в конце нажимаете «Заказать».

```java
public final class Book {
    private final String title;
    private final String author;
    private final int year;
    private final String isbn;

    private Book(Builder builder) {                  // конструктор приватный
        this.title = builder.title;
        this.author = builder.author;
        this.year = builder.year;
        this.isbn = builder.isbn;
    }

    public static Builder builder() { return new Builder(); }

    @Override public String toString() {
        return "%s — %s (%d), ISBN: %s".formatted(title, author, year, isbn);
    }

    public static final class Builder {
        private String title;
        private String author;
        private int year;
        private String isbn = "не указан";           // значение по умолчанию

        public Builder title(String title) { this.title = title; return this; }
        public Builder author(String author) { this.author = author; return this; }
        public Builder year(int year) { this.year = year; return this; }
        public Builder isbn(String isbn) { this.isbn = isbn; return this; }

        public Book build() {
            // Валидация в одном месте, до создания объекта
            if (title == null || author == null) {
                throw new IllegalStateException("Название и автор обязательны");
            }
            return new Book(this);
        }
    }
}

// Использование читается как обычное предложение:
// Book book = Book.builder().title("Чистый код").author("Роберт Мартин").year(2008).build();
// Вывод: Чистый код — Роберт Мартин (2008), ISBN: не указан
```

Отдельная выгода: `Book` получается **неизменяемым** (все поля `final`, сеттеров нет), а такие объекты безопасны в многопоточной среде.

**Где встречается.** В JDK: `StringBuilder`, `Stream.builder()`, `HttpRequest.newBuilder()`, `Locale.Builder`, `Calendar.Builder`. В Spring: `UriComponentsBuilder`, а также вся конфигурация Spring Security через объект `HttpSecurity` — тот же строитель, только собирающий цепочку фильтров.

### 3.5 Prototype (Прототип)

**Задача.** Создавать новые объекты копированием существующего, а не конструированием с нуля. Аналогия — ксерокс: если есть заполненный бланк-образец, проще снять с него копию и поправить пару полей, чем печатать бланк заново.

```java
public class ReportTemplate implements Cloneable {
    private String title;
    private List<String> rows;

    public ReportTemplate(String title, List<String> rows) {
        this.title = title;
        this.rows = new ArrayList<>(rows);
    }

    // Конструктор копирования — современная альтернатива clone()
    public ReportTemplate(ReportTemplate other) { this(other.title, other.rows); }

    public void addRow(String row) { rows.add(row); }

    @Override public ReportTemplate clone() {
        try {
            ReportTemplate copy = (ReportTemplate) super.clone();
            // Глубокое копирование: иначе копия и оригинал
            // будут делить один и тот же список
            copy.rows = new ArrayList<>(this.rows);
            return copy;
        } catch (CloneNotSupportedException e) {
            throw new AssertionError("Cloneable реализован, этого не случится", e);
        }
    }

    @Override public String toString() { return title + " " + rows; }
}
```

Главная ловушка — **поверхностное копирование (shallow copy)**. `Object.clone()` копирует поля «как есть», то есть ссылки на вложенные объекты остаются общими. Изменили список в копии — изменился и в оригинале. Поэтому строку `copy.rows = new ArrayList<>(this.rows)` пропускать нельзя.

**Где встречается.** В JDK: `Object.clone()`, `ArrayList.clone()`, `Date.clone()`. В Spring идея отражена в scope `prototype`: бин с `@Scope("prototype")` создаётся заново на каждый запрос из контейнера.

---

## Часть 4: Структурные паттерны

Структурные паттерны отвечают на вопрос «как собрать из объектов более крупную конструкцию, сохранив гибкость». Общая аналогия — конструктор LEGO: одни детали соединяют несовместимое (переходники), другие оборачивают деталь, добавляя ей свойства, третьи собирают деревья из одинаковых элементов.

### 4.1 Adapter (Адаптер)

**Задача.** Заставить работать вместе классы с несовместимыми интерфейсами. Аналогия прямо в названии: адаптер для розетки. Вилка европейская, розетка британская, менять ни то ни другое вы не можете — берёте переходник.

```java
// Три файла пакета ru.fa.patterns.structural; в каждом — своя строка package ru.fa.patterns.structural; и нужные импорты
// Чужая библиотека. Исходники недоступны, менять нельзя
public class LegacyXmlLogger {
    public void writeXml(String xml) { System.out.println("<log>" + xml + "</log>"); }
}

// Интерфейс, которого ждёт наше приложение
public interface AppLogger { void log(String message); }

// Адаптер: снаружи AppLogger, внутри LegacyXmlLogger
public class XmlLoggerAdapter implements AppLogger {
    private final LegacyXmlLogger legacy;

    public XmlLoggerAdapter(LegacyXmlLogger legacy) { this.legacy = legacy; }

    @Override public void log(String message) {
        legacy.writeXml("<message>" + message + "</message>");
    }
}
```

**Где встречается.** В JDK: `InputStreamReader` — адаптер байтового потока к символьному (эту пару мы разбирали в Лекции 5); `Arrays.asList()` — адаптер массива к `List`; `Collections.list(Enumeration)` — адаптер старого `Enumeration` к `List`. В Spring: `HandlerAdapter` в Spring MVC, позволяющий диспетчеру единообразно работать с контроллерами разных типов.

### 4.2 Bridge (Мост)

**Задача.** Разделить абстракцию и её реализацию так, чтобы их можно было развивать независимо.

Паттерн решает проблему «комбинаторного взрыва наследования». Пусть есть обычные и срочные уведомления, а отправлять их можно по e-mail и в Telegram. Через наследование получится четыре класса. Добавили SMS — шесть. Добавили отложенные уведомления — девять. Аналогия — пульт и техника: пультов бывает несколько видов (простой, с таймером), техники тоже (телевизор, кондиционер). Их не сваривают в один предмет: между ними «мост» — стандарт сигналов.

```java
// Пять файлов пакета ru.fa.patterns.structural; в каждом — своя строка package ru.fa.patterns.structural; и нужные импорты
// Сторона реализации
public interface MessageSender { void send(String title, String body); }

public class EmailSender implements MessageSender {
    @Override public void send(String t, String body) { System.out.println("E-mail | " + t + " | " + body); }
}

public class TelegramSender implements MessageSender {
    @Override public void send(String t, String body) { System.out.println("Telegram | " + t + " | " + body); }
}

// Сторона абстракции: ссылка на реализацию и есть «мост»
public abstract class Notification {
    protected final MessageSender sender;
    protected Notification(MessageSender sender) { this.sender = sender; }
    public abstract void notifyUser(String text);
}

public class UrgentNotification extends Notification {
    public UrgentNotification(MessageSender sender) { super(sender); }
    @Override public void notifyUser(String text) { sender.send("СРОЧНО", text); }
}
```

Теперь виды уведомлений и каналы отправки растут независимо: 3 + 3 класса вместо 9.

**Где встречается.** В JDK: архитектура JDBC — интерфейсы `Connection` и `Statement` являются абстракцией, а драйвер конкретной СУБД (`java.sql.Driver`) — реализацией. Приложение пишется один раз, а драйвер подставляется под нужную базу. Мы этим пользовались в Лекции 6.

### 4.3 Composite (Компоновщик)

**Задача.** Работать с деревом объектов так же, как с отдельным объектом. Аналогия — файловая система: папка содержит файлы и другие папки, но когда вы спрашиваете «сколько это весит», вам всё равно, папка перед вами или файл — ответ приходит в тех же мегабайтах.

```java
// Три файла пакета ru.fa.patterns.structural; в каждом — своя строка package ru.fa.patterns.structural; и нужные импорты
public interface FileNode {
    String name();
    long size();
}

// Лист дерева: record сам реализует name() и size()
public record TextFile(String name, long size) implements FileNode { }

// Составной узел
public class Folder implements FileNode {
    private final String name;
    private final List<FileNode> children = new ArrayList<>();

    public Folder(String name) { this.name = name; }
    public Folder add(FileNode node) { children.add(node); return this; }

    @Override public String name() { return name; }

    @Override public long size() {
        long total = 0;
        for (FileNode child : children) {
            total += child.size();     // рекурсия по дереву
        }
        return total;
    }
}

// Клиент не различает лист и ветку:
// FileNode root = new Folder("проект")
//         .add(new TextFile("pom.xml", 2_048))
//         .add(new Folder("src")
//                 .add(new TextFile("Main.java", 1_024))
//                 .add(new TextFile("Service.java", 4_096)));
// root.size() вернёт 7168
```

**Где встречается.** В JavaFX: граф сцены (`Node`, `Parent`) — контейнер сам является узлом, поэтому вложенность произвольная; в AWT — `Component` и `Container`.

### 4.4 Decorator (Декоратор)

**Задача.** Динамически добавлять объекту новые обязанности, не меняя его класс и не плодя подклассы. Аналогия — кофе: есть эспрессо, добавили молоко — латте, добавили сироп — латте с сиропом. Каждая добавка оборачивает напиток, но напиток остаётся напитком: его по-прежнему можно выпить.

```java
// Пять файлов пакета ru.fa.patterns.structural; в каждом — своя строка package ru.fa.patterns.structural; и нужные импорты
public interface DataSource { String read(); }

public class FileDataSource implements DataSource {
    @Override public String read() { return "данные отчёта"; }
}

// Базовый декоратор: реализует тот же интерфейс и хранит вложенный объект
public abstract class DataSourceDecorator implements DataSource {
    protected final DataSource wrappee;
    protected DataSourceDecorator(DataSource wrappee) { this.wrappee = wrappee; }
}

public class UpperCaseDecorator extends DataSourceDecorator {
    public UpperCaseDecorator(DataSource wrappee) { super(wrappee); }
    @Override public String read() { return wrappee.read().toUpperCase(); }
}

public class BracketsDecorator extends DataSourceDecorator {
    public BracketsDecorator(DataSource wrappee) { super(wrappee); }
    @Override public String read() { return "[" + wrappee.read() + "]"; }
}

// Обёртки складываются как матрёшка:
// new BracketsDecorator(new UpperCaseDecorator(new FileDataSource())).read()
// вернёт [ДАННЫЕ ОТЧЁТА]
```

**Где встречается.** Самый узнаваемый паттерн в JDK. Строка `new BufferedReader(new FileReader("data.txt"))` — это Декоратор в чистом виде: `BufferedReader` добавляет буферизацию и метод `readLine()`, оставаясь `Reader`. Так же устроены `BufferedInputStream`, `DataOutputStream`, `GZIPOutputStream`. Ещё примеры: `Collections.unmodifiableList()` — декоратор, отнимающий возможность изменения; `HttpServletRequestWrapper` в сервлетах.

**Отличие от наследования.** Декоратор собирается в рантайме и складывается в любом порядке. Наследованием пришлось бы завести класс `BufferedGzipFileReader` и все прочие комбинации.

### 4.5 Facade (Фасад)

**Задача.** Предоставить простой интерфейс к сложной подсистеме. Аналогия — оператор колл-центра банка: за ним стоят десятки систем (скоринг, платёжный процессинг, антифрод, документооборот), а вы говорите «хочу оформить карту» и не знаете об этих системах ничего.

```java
// Четыре файла пакета ru.fa.patterns.structural; в каждом — своя строка package ru.fa.patterns.structural; и нужные импорты
// Три независимые подсистемы
public class InventoryService {
    public void reserve(long bookId) { System.out.println("Книга " + bookId + " зарезервирована"); }
}
public class PaymentService {
    public void charge(String client, double amount) { System.out.println("Списано " + amount); }
}
public class DeliveryService {
    public void schedule(long bookId, String address) { System.out.println("Доставка в " + address); }
}

// Фасад: одна понятная операция вместо трёх вызовов в правильном порядке
public class OrderFacade {
    private final InventoryService inventory;
    private final PaymentService payment;
    private final DeliveryService delivery;

    // Подсистемы приходят извне: фасад прячет сложность, но не создаёт зависимости сам
    public OrderFacade(InventoryService inventory, PaymentService payment, DeliveryService delivery) {
        this.inventory = inventory;
        this.payment = payment;
        this.delivery = delivery;
    }

    public void placeOrder(String client, long bookId, double price, String address) {
        inventory.reserve(bookId);
        payment.charge(client, price);
        delivery.schedule(bookId, address);
    }
}
```

Обратите внимание на конструктор: соблазн написать `new InventoryService()` прямо в поле велик, но это ровно тот симптом нарушения DIP, который мы разбирали в части 2. Фасад от внедрения зависимостей фасадом быть не перестаёт, зато его становится возможно протестировать с заглушками вместо трёх настоящих подсистем.

Важно: Фасад не запрещает обращаться к подсистемам напрямую. Он лишь предлагает удобный путь для типового сценария.

**Где встречается.** В JDK: `java.net.URL` с методом `openStream()` прячет сокеты, протоколы и кодировки. В Spring: `JdbcTemplate` — фасад над громоздким JDBC API (вспомните Лекцию 6, где мы вручную открывали `Connection`, готовили `PreparedStatement` и закрывали `ResultSet`); `RestTemplate` и `WebClient` — фасады над HTTP.

### 4.6 Flyweight (Приспособленец)

**Задача.** Экономить память, разделяя общее (неизменяемое) состояние между множеством объектов. Аналогия — типографская касса букв: чтобы набрать книгу на 300 страниц, не отливают отдельную литеру для каждой буквы «а» в тексте, берут одну и ставят в нужные места. Внешнее состояние (позиция на странице) хранится отдельно, внутреннее (форма буквы) — общее.

```java
// Два файла пакета ru.fa.patterns.structural; в каждом — своя строка package ru.fa.patterns.structural; и нужные импорты
// Внутреннее состояние: неизменяемое и разделяемое
public record CharStyle(String font, int size, String color) { }

public final class StyleFactory {
    private static final Map<String, CharStyle> CACHE = new HashMap<>();

    private StyleFactory() { }

    public static CharStyle of(String font, int size, String color) {
        String key = font + "|" + size + "|" + color;
        // Одинаковые стили не создаются повторно
        return CACHE.computeIfAbsent(key, k -> new CharStyle(font, size, color));
    }

    public static int cacheSize() { return CACHE.size(); }
}
```

На документе в миллион символов, где используется пять стилей, в памяти будет пять объектов `CharStyle`, а не миллион.

**Где встречается.** В JDK: кеш `Integer.valueOf()` для значений от −128 до 127 (именно поэтому `Integer a = 127, b = 127; a == b` даёт `true`, а для 128 — `false`); пул строковых литералов; `Boolean.valueOf()`.

### 4.7 Proxy (Заместитель)

**Задача.** Подставить вместо объекта его дублёра с тем же интерфейсом, чтобы контролировать доступ к оригиналу. Аналогия — секретарь руководителя: для посетителя он говорит от лица начальника, часть вопросов решает сам, часть откладывает, а до начальника доводит только нужное.

```java
// Три файла пакета ru.fa.patterns.structural; в каждом — своя строка package ru.fa.patterns.structural; и нужные импорты
public interface BookRepository { String findTitle(long id); }

public class RealBookRepository implements BookRepository {
    @Override public String findTitle(long id) {
        System.out.println("Тяжёлый запрос в БД, id=" + id);
        return "Книга №" + id;
    }
}

// Кеширующий заместитель: тот же интерфейс, дополнительное поведение
public class CachingBookProxy implements BookRepository {
    private final BookRepository target;
    private final Map<Long, String> cache = new HashMap<>();

    public CachingBookProxy(BookRepository target) { this.target = target; }

    @Override public String findTitle(long id) {
        return cache.computeIfAbsent(id, target::findTitle);
    }
}
```

Разновидности заместителя: кеширующий (как выше), защитный (проверяет права), ленивый (создаёт тяжёлый объект при первом обращении), удалённый (прячет сетевой вызов), логирующий.

**Где встречается.** Это ключевой паттерн всего Spring. В JDK: `java.lang.reflect.Proxy` — динамическое создание заместителя по интерфейсу в рантайме. В Spring на нём построены `@Transactional`, `@Cacheable`, `@Async`, `@PreAuthorize` и вся аспектно-ориентированная механика. Мы говорили в Лекции 7, что `@Transactional` не срабатывает при вызове метода изнутри того же класса — теперь понятно почему: внутренний вызов `this.method()` идёт мимо заместителя, потому что заместитель является отдельным объектом-обёрткой.

**Отличие от Декоратора.** Технически они похожи (оба реализуют интерфейс и держат ссылку на объект), но различаются намерением: Декоратор **добавляет возможности** и применяется клиентом осознанно, а Заместитель **контролирует доступ**, и клиент часто даже не знает о его существовании.

---

## Часть 5: Поведенческие паттерны

Поведенческие паттерны — про распределение обязанностей и способы общения объектов. Общая аналогия — организация работы в компании: кто кому подчиняется, как передаётся заявка по инстанциям, кто кого уведомляет об изменениях, кто решает, каким способом выполнять задачу.

### 5.1 Chain of Responsibility (Цепочка обязанностей)

**Задача.** Передавать запрос по цепочке обработчиков, пока один из них его не обработает. Аналогия — заявление в вузе: сначала оно попадает в деканат, оттуда в учебную часть, оттуда к проректору. Каждая инстанция либо решает вопрос сама, либо передаёт дальше.

```java
// Три файла пакета ru.fa.patterns.behavioral; в каждом — своя строка package ru.fa.patterns.behavioral; и нужные импорты
public abstract class Validator {
    private Validator next;

    // Возвращаем next, чтобы звенья можно было сцеплять подряд:
    // head.linkWith(second).linkWith(third). Внимание: в переменной нужно
    // держать ПЕРВОЕ звено — именно ему потом отправляют запрос
    public Validator linkWith(Validator next) { this.next = next; return next; }

    public final boolean validate(String login, String password) {
        if (!check(login, password)) return false;
        return next == null || next.validate(login, password);
    }

    protected abstract boolean check(String login, String password);
}

public class NotEmptyValidator extends Validator {
    @Override protected boolean check(String login, String password) {
        boolean ok = !login.isBlank() && !password.isBlank();
        if (!ok) System.out.println("Логин и пароль не должны быть пустыми");
        return ok;
    }
}

public class LengthValidator extends Validator {
    @Override protected boolean check(String login, String password) {
        boolean ok = password.length() >= 8;
        if (!ok) System.out.println("Пароль короче 8 символов");
        return ok;
    }
}

// Сборка цепочки:
// Validator chain = new NotEmptyValidator();
// chain.linkWith(new LengthValidator());
// chain.validate("ivanov", "12345") вернёт false
```

**Где встречается.** В JDK: цепочка фильтров сервлетов (`Filter` и `FilterChain`). В Spring: `SecurityFilterChain` — буквально цепочка обязанностей, где каждый фильтр либо обрабатывает запрос, либо пропускает дальше; `HandlerInterceptor` в Spring MVC.

### 5.2 Command (Команда)

**Задача.** Превратить запрос в объект, чтобы его можно было передать, поставить в очередь, залогировать или отменить. Аналогия — заказ в ресторане: официант не готовит блюдо сам, он записывает заказ на бумажке. Бумажка — объект-команда: её можно передать повару, положить в очередь заказов, а при ошибке отменить.

```java
// Три файла пакета ru.fa.patterns.behavioral; в каждом — своя строка package ru.fa.patterns.behavioral; и нужные импорты
public interface Command {
    void execute();
    void undo();
}

public class AddBookCommand implements Command {
    private final List<String> shelf;
    private final String title;

    public AddBookCommand(List<String> shelf, String title) {
        this.shelf = shelf;
        this.title = title;
    }

    @Override public void execute() {
        shelf.add(title);
        System.out.println("Добавлена книга: " + title);
    }

    @Override public void undo() {
        shelf.remove(title);
        System.out.println("Отменено добавление: " + title);
    }
}

// Хранитель истории — то, ради чего обычно и вводят Команду
public class CommandHistory {
    private final Deque<Command> history = new ArrayDeque<>();

    public void run(Command command) {
        command.execute();
        history.push(command);
    }

    public void undoLast() {
        if (!history.isEmpty()) history.pop().undo();
    }
}
```

**Где встречается.** В JDK: `Runnable` и `Callable` — это и есть команды, которые вы кладёте в `ExecutorService.submit()` (Лекция 5). Пул потоков ставит их в очередь и выполняет позже — ровно то, ради чего паттерн придуман. В Swing — интерфейс `Action`.

### 5.3 Interpreter (Интерпретатор)

**Задача.** Задать грамматику языка и вычислять выражения этого языка, представляя их деревом объектов. Аналогия — калькулятор, разбирающий формулу «x + 5»: каждый элемент формулы становится объектом, а вычисление — обходом дерева.

```java
// Четыре файла пакета ru.fa.patterns.behavioral; в каждом — своя строка package ru.fa.patterns.behavioral; и нужные импорты
public interface Expr { int evaluate(Map<String, Integer> context); }

public record Num(int value) implements Expr {
    @Override public int evaluate(Map<String, Integer> context) { return value; }
}

public record Var(String name) implements Expr {
    @Override public int evaluate(Map<String, Integer> context) {
        Integer value = context.get(name);
        if (value == null) throw new IllegalArgumentException("Переменная не задана: " + name);
        return value;
    }
}

public record Plus(Expr left, Expr right) implements Expr {
    @Override public int evaluate(Map<String, Integer> context) {
        return left.evaluate(context) + right.evaluate(context);
    }
}

// new Plus(new Var("x"), new Num(5)).evaluate(Map.of("x", 10)) вернёт 15
```

**Где встречается.** В JDK: `java.util.regex.Pattern` — интерпретатор языка регулярных выражений; `java.text.MessageFormat`. В Spring: SpEL (Spring Expression Language) и класс `SpelExpressionParser`, выполняющий выражения вида `#{systemProperties['user.name']}` в аннотациях.

**Осторожно.** Паттерн применим только для простых грамматик. Для настоящего языка пишут парсер с помощью генераторов (ANTLR), а не вручную по этому паттерну.

### 5.4 Iterator (Итератор)

**Задача.** Дать последовательный доступ к элементам составного объекта, не раскрывая его внутреннее устройство. Аналогия — экскурсовод в музее: вы не изучаете план здания и систему нумерации залов, а идёте за экскурсоводом, который знает, что показать следующим.

```java
public class Shelf implements Iterable<String> {
    private final String[] books;

    public Shelf(String... books) { this.books = books; }

    @Override public Iterator<String> iterator() {
        return new Iterator<>() {
            private int index = 0;

            @Override public boolean hasNext() { return index < books.length; }

            @Override public String next() {
                if (!hasNext()) throw new NoSuchElementException();
                return books[index++];
            }
        };
    }
}

// Класс реализует Iterable, поэтому сразу работает в цикле for-each:
// for (String book : new Shelf("Чистый код", "Рефакторинг")) { System.out.println(book); }
```

**Где встречается.** Весь Java Collections Framework (Лекция 5): `Iterator`, `ListIterator`, `Iterable`. Цикл `for-each` — синтаксический сахар над итератором. Также `Scanner`, `Spliterator` (основа Stream API) и `Files.newDirectoryStream()`.

### 5.5 Mediator (Посредник)

**Задача.** Убрать прямые связи «каждый с каждым», заставив объекты общаться через единый объект-посредник. Аналогия — диспетчер аэропорта: самолёты не договариваются о посадке напрямую друг с другом, это была бы катастрофа. Все общаются с диспетчерской вышкой.

```java
// Три файла пакета ru.fa.patterns.behavioral; в каждом — своя строка package ru.fa.patterns.behavioral; и нужные импорты
public interface ChatMediator {
    void register(User user);
    void send(String from, String text);
}

public class ChatRoom implements ChatMediator {
    private final List<User> users = new ArrayList<>();

    @Override public void register(User user) {
        users.add(user);
        user.setMediator(this);
    }

    @Override public void send(String from, String text) {
        for (User user : users) {
            if (!user.getName().equals(from)) user.receive(from, text);
        }
    }
}

public class User {
    private final String name;
    private ChatMediator mediator;

    public User(String name) { this.name = name; }
    public String getName() { return name; }
    public void setMediator(ChatMediator mediator) { this.mediator = mediator; }

    // Не знаем о других участниках ничего
    public void say(String text) { mediator.send(name, text); }

    public void receive(String from, String text) {
        System.out.println(name + " получил от " + from + ": " + text);
    }
}
```

**Где встречается.** В JDK: `ExecutorService` выступает посредником между задачами и потоками. В Spring: `ApplicationEventPublisher` — бины публикуют события, не зная о подписчиках; `DispatcherServlet` посредничает между запросом, контроллерами и представлениями.

### 5.6 Memento (Снимок)

**Задача.** Сохранить состояние объекта, чтобы позже его восстановить, не нарушая инкапсуляцию. Аналогия — сохранение в компьютерной игре: вы делаете «сейв» перед сложным боем и при неудаче возвращаетесь к нему, при этом файл сохранения остаётся чёрным ящиком.

```java
public class TextEditor {
    private String text = "";

    public void type(String part) { text += part; }
    public String getText() { return text; }

    // Снимок неизменяем: изменить состояние «задним числом» нельзя
    public record Snapshot(String text) { }

    public Snapshot save() { return new Snapshot(text); }
    public void restore(Snapshot snapshot) { this.text = snapshot.text(); }
}

// Хранитель истории (в терминах паттерна — caretaker) складывает снимки в стек:
// Deque<TextEditor.Snapshot> history = new ArrayDeque<>();
// editor.type("Привет"); history.push(editor.save()); editor.type(", мир!");
// editor.restore(history.pop());  // getText() снова вернёт «Привет»
```

Обратите внимание на связку с Командой: метод `undo()` из пункта 5.2 очень часто реализуется именно через снимки.

**Где встречается.** В чистом виде в JDK паттерн почти не представлен. Ближайший аналог — сериализация объекта (`Serializable`), тоже сохраняющая состояние во внешнее представление. В работе с БД той же идее соответствуют точки сохранения (savepoint) внутри транзакции.

### 5.7 Observer (Наблюдатель)

**Задача.** Оповещать множество объектов об изменении состояния другого объекта, не связывая их жёстко. Аналогия — подписка на канал: автор публикует ролик и не знает поимённо, кто его посмотрит, а подписчики получают уведомление автоматически и могут отписаться в любой момент.

```java
// Два файла пакета ru.fa.patterns.behavioral; в каждом — своя строка package ru.fa.patterns.behavioral; и нужные импорты
public interface OrderListener { void onOrderCreated(String orderId); }

public class OrderService {
    private final List<OrderListener> listeners = new ArrayList<>();

    public void subscribe(OrderListener listener) { listeners.add(listener); }
    public void unsubscribe(OrderListener listener) { listeners.remove(listener); }

    public void createOrder(String orderId) {
        System.out.println("Заказ " + orderId + " создан");
        for (OrderListener listener : listeners) {
            listener.onOrderCreated(orderId);   // рассылка уведомлений
        }
    }
}

// OrderListener — функциональный интерфейс, поэтому подписчики пишутся лямбдами (Лекция 2):
// service.subscribe(id -> System.out.println("Письмо клиенту по заказу " + id));
// service.subscribe(id -> System.out.println("Списание со склада по заказу " + id));
// service.createOrder("A-100");
```

Ключевая выгода: чтобы добавить новую реакцию на событие, класс `OrderService` менять не нужно. Это принцип OCP в действии.

**Где встречается.** В JDK: `PropertyChangeListener` в JavaBeans, слушатели событий в Swing и JavaFX (`ActionListener`, `EventHandler`), интерфейсы `java.util.concurrent.Flow` (реактивные потоки). Старые классы `java.util.Observer` и `Observable` объявлены устаревшими начиная с Java 9 — не используйте их. В Spring: `@EventListener` и `ApplicationEventPublisher`.

### 5.8 State (Состояние)

**Задача.** Позволить объекту менять поведение при изменении внутреннего состояния — так, будто он меняет класс. Аналогия — турникет в метро: пока карту не приложили, он на толчок отвечает «заблокировано», а после оплаты тот же толчок пропускает пассажира. Действие одно, реакция зависит от состояния.

```java
// Пять файлов пакета ru.fa.patterns.behavioral; в каждом — своя строка package ru.fa.patterns.behavioral; и нужные импорты
public interface OrderState {
    OrderState pay();
    OrderState cancel();
    String title();
}

public class NewState implements OrderState {
    @Override public OrderState pay() { return new PaidState(); }
    @Override public OrderState cancel() { return new CancelledState(); }
    @Override public String title() { return "НОВЫЙ"; }
}

public class PaidState implements OrderState {
    @Override public OrderState pay() { throw new IllegalStateException("Заказ уже оплачен"); }
    @Override public OrderState cancel() {
        System.out.println("Возврат средств");   // из оплаченного — только с возвратом
        return new CancelledState();
    }
    @Override public String title() { return "ОПЛАЧЕН"; }
}

public class CancelledState implements OrderState {
    @Override public OrderState pay() { throw new IllegalStateException("Заказ отменён"); }
    @Override public OrderState cancel() { return this; }
    @Override public String title() { return "ОТМЕНЁН"; }
}

public class Order {
    private OrderState state = new NewState();

    public void pay() { state = state.pay(); }
    public void cancel() { state = state.cancel(); }
    public String status() { return state.title(); }
}
```

Сравните с альтернативой: поле `int status` и метод `pay()`, начинающийся с `if (status == 1) ... else if (status == 2) ...`. Такой код растёт при каждом новом статусе и склонен к ошибкам: что если статусов уже семь, а условие проверяет пять?

**Где встречается.** В JDK перечисление `Thread.State` описывает состояния потока, но переходами управляет сама JVM. В экосистеме Spring есть отдельный проект Spring State Machine, реализующий этот паттерн для бизнес-процессов.

### 5.9 Strategy (Стратегия)

**Задача.** Вынести семейство взаимозаменяемых алгоритмов в отдельные классы и позволить подменять их на лету. Аналогия — навигатор: маршрут до одной и той же точки строится по-разному («самый быстрый», «без платных дорог», «пешком»). Пункт назначения общий, алгоритм сменный.

```java
// Два файла пакета ru.fa.patterns.behavioral; в каждом — своя строка package ru.fa.patterns.behavioral; и нужные импорты
@FunctionalInterface
public interface DiscountStrategy { double apply(double amount); }

public class Cart {
    // Стратегия по умолчанию: без скидки
    private DiscountStrategy strategy = amount -> amount;

    public void setStrategy(DiscountStrategy strategy) { this.strategy = strategy; }
    public double total(double amount) { return strategy.apply(amount); }
}

// Cart cart = new Cart();
// cart.total(1000)                          вернёт 1000.0
// cart.setStrategy(amount -> amount * 0.9); скидка 10%,      total(1000) вернёт 900.0
// cart.setStrategy(amount -> amount - 150); фиксированная,   total(1000) вернёт 850.0
```

**Отличие от Состояния.** Структурно паттерны почти идентичны: и там, и там объект делегирует работу вложенному объекту. Разница в намерении. В Стратегии алгоритм выбирает **клиент** извне, и стратегии не знают друг о друге. В Состоянии переход выбирает **сам объект состояния**, и состояния знают о соседях по автомату.

**Где встречается.** В JDK: `Comparator`, передаваемый в `list.sort(...)` — классическая стратегия сортировки; `RejectedExecutionHandler` в `ThreadPoolExecutor`. В Spring: `PasswordEncoder` (BCrypt, Argon2, Pbkdf2 — сменные реализации), `TaskExecutor`, `ViewResolver`, `CacheManager`. Более того: **любой бин, внедряемый через интерфейс, — это Стратегия**, а Spring выступает механизмом её подстановки.

### 5.10 Template Method (Шаблонный метод)

**Задача.** Задать скелет алгоритма в базовом классе, позволив подклассам переопределять отдельные шаги, не меняя структуру алгоритма. Аналогия — рецепт горячего напитка: шаги всегда одни (вскипятить воду, заварить, налить в чашку, добавить приправы), но «заварить» для чая и кофе означает разное.

```java
// Два файла пакета ru.fa.patterns.behavioral; в каждом — своя строка package ru.fa.patterns.behavioral; и нужные импорты
public abstract class DataImporter {

    // Шаблонный метод: final, чтобы структуру алгоритма не переопределили
    public final void importData(String source) {
        open(source);
        try {
            List<String> rows = readRows();
            for (String row : rows) process(row);
            System.out.println("Импортировано строк: " + rows.size());
        } finally {
            close();
        }
    }

    // Обязательные шаги
    protected abstract void open(String source);
    protected abstract List<String> readRows();
    protected abstract void process(String row);

    // Хук (hook): необязательный шаг с реализацией по умолчанию
    protected void close() { }
}

public class CsvImporter extends DataImporter {
    private String path;

    @Override protected void open(String source) {
        this.path = source;
        System.out.println("Открыт CSV-файл: " + path);
    }
    @Override protected List<String> readRows() { return List.of("1;Чистый код", "2;Рефакторинг"); }
    @Override protected void process(String row) { System.out.println("Строка: " + row); }
    @Override protected void close() { System.out.println("Файл закрыт: " + path); }
}
```

Ключевое слово `final` на шаблонном методе — не формальность. Оно защищает инвариант: порядок шагов и обработка ошибок остаются под контролем базового класса.

**Где встречается.** В JDK: `AbstractList` и `AbstractMap` (наследнику достаточно реализовать пару методов, остальное работает); `HttpServlet.service()`, вызывающий `doGet()` или `doPost()` в зависимости от метода запроса. В Spring это несущая конструкция: `JdbcTemplate`, `RestTemplate`, `TransactionTemplate`, `AbstractApplicationContext.refresh()`.

### 5.11 Visitor (Посетитель)

**Задача.** Добавить новую операцию над объектами структуры, не меняя классы этих объектов. Аналогия — ревизор, обходящий отделы компании: отделы не переписывают свои регламенты под каждую проверку, они просто «принимают» ревизора, а тот сам знает, что проверять в бухгалтерии, а что на складе.

```java
// Пять файлов пакета ru.fa.patterns.behavioral; в каждом — своя строка package ru.fa.patterns.behavioral; и нужные импорты
public interface NodeVisitor {
    void visit(TextNode node);
    void visit(ImageNode node);
}

public interface DocNode { void accept(NodeVisitor visitor); }

public record TextNode(String text) implements DocNode {
    @Override public void accept(NodeVisitor visitor) { visitor.visit(this); }
}

public record ImageNode(String url) implements DocNode {
    @Override public void accept(NodeVisitor visitor) { visitor.visit(this); }
}

// Новая операция = новый класс. Узлы не трогаем
public class HtmlRenderer implements NodeVisitor {
    private final StringBuilder result = new StringBuilder();

    @Override public void visit(TextNode node) {
        result.append("<p>").append(node.text()).append("</p>");
    }
    @Override public void visit(ImageNode node) {
        result.append("<img src=\"").append(node.url()).append("\">");
    }

    public String html() { return result.toString(); }
}

// List<DocNode> document = List.of(new TextNode("Заголовок"), new ImageNode("logo.png"));
// HtmlRenderer renderer = new HtmlRenderer();
// document.forEach(node -> node.accept(renderer));
// renderer.html() вернёт <p>Заголовок</p><img src="logo.png">
```

**Цена паттерна.** Добавить операцию легко, а вот добавить новый тип узла тяжело: придётся править интерфейс `NodeVisitor` и все его реализации. Выбирайте Посетитель, когда набор типов стабилен, а операций много.

**Современная альтернатива в Java 21.** Запечатанные (`sealed`) интерфейсы из Лекции 3 вместе с сопоставлением с образцом в `switch` дают тот же результат короче:

```java
// Четыре файла пакета ru.fa.patterns.behavioral; в каждом — своя строка package ru.fa.patterns.behavioral; и нужные импорты
public sealed interface Node permits Text, Image { }
public record Text(String value) implements Node { }
public record Image(String url) implements Node { }

public class Renderer {
    public String render(Node node) {
        return switch (node) {
            case Text t -> "<p>" + t.value() + "</p>";
            case Image i -> "<img src=\"" + i.url() + "\">";
        };
    }
}
```

Компилятор сам проверит, что вы обработали все варианты: `sealed` гарантирует, что других наследников нет, поэтому ветка `default` не нужна.

**Где встречается.** В JDK: `java.nio.file.FileVisitor` вместе с `Files.walkFileTree()` — обход дерева каталогов; `javax.lang.model.element.ElementVisitor` в обработчиках аннотаций.

---

## Часть 6: Паттерны вокруг нас — JDK и Spring

Так узнают знакомое лицо в толпе. Пока вы не знали имён, весь JDK был для вас ровным фоном: «ну, обёртка какая-то, так принято писать». Стоит выучить имена — и в каждой второй строке проступает знакомый силуэт: вот Декоратор, вот Адаптер, а вот Заместитель, который всё это время стоял у вас за спиной и открывал транзакции.

Отдельная ценность этой темы в том, что она задним числом объясняет весь предыдущий курс. Разберём три знакомых фрагмента кода и увидим за ними паттерны.

### 6.1 Цепочка потоков ввода-вывода

```java
try (BufferedReader reader = new BufferedReader(
        new InputStreamReader(
                new FileInputStream("data.txt"), StandardCharsets.UTF_8))) {
    System.out.println(reader.readLine());
}
```

Здесь два паттерна в одном выражении. `FileInputStream` — источник байтов, паттерна за ним нет. `InputStreamReader` — **Адаптер**: превращает байтовый поток в символьный. `BufferedReader` — **Декоратор**: добавляет буферизацию и метод `readLine()`, оставаясь `Reader`. А `try-with-resources` опирается на интерфейс `AutoCloseable` — это уже не паттерн, а иллюстрация ISP: интерфейс описывает ровно одну роль.

### 6.2 JdbcTemplate — Шаблонный метод плюс Фасад

```java
List<String> titles = jdbcTemplate.query(
        "SELECT title FROM books WHERE year > ?",
        (rs, rowNum) -> rs.getString("title"),   // ваш шаг алгоритма
        2000);
```

`JdbcTemplate` выполняет неизменную часть алгоритма: берёт соединение из пула, готовит `PreparedStatement`, подставляет параметры, перебирает `ResultSet`, закрывает всё в `finally` и превращает `SQLException` в непроверяемое исключение Spring. Вам остаётся один шаг — `RowMapper`, лямбда, превращающая строку результата в объект. Это **Шаблонный метод**. Одновременно `JdbcTemplate` является **Фасадом** над громоздким JDBC API, а `RowMapper` — **Стратегией** отображения строки.

### 6.3 @Transactional — Заместитель

```java
@Service
public class BookService {

    @Transactional
    public void moveToArchive(long bookId) {
        // бизнес-логика без единого упоминания транзакций
    }
}
```

Когда контейнер поднимает бин `BookService`, он кладёт в контекст не ваш объект, а сгенерированный **Заместитель** — либо JDK-прокси по интерфейсу, либо CGLIB-подкласс. Заместитель перед вызовом открывает транзакцию, после коммитит, при непроверяемом исключении откатывает. Ваш класс о транзакциях ничего не знает: это SRP на уровне инфраструктуры.

Сводку «какой паттерн где искать в JDK и Spring» вы найдёте в итоговой таблице Части 9 — это удобная шпаргалка при подготовке к экзамену.

---

## Часть 7: Антипаттерны

**Антипаттерн** — типовое решение, которое выглядит удобным в момент написания и приносит проблемы позже. От обычной ошибки он отличается тем, что воспроизводится систематически и разными людьми независимо друг от друга.

Аналогия для всей части — беспорядок в квартире. Ни одна отдельно брошенная вещь не создаёт проблемы. Но привычка «положу пока сюда», повторённая триста раз, превращает квартиру в место, где ничего невозможно найти. Антипаттерны — такие же привычки в коде.

### 7.1 God Object (Божественный объект)

**Признаки.** Класс на 1500–3000 строк. В имени слова `Manager`, `Util`, `Helper`, `Processor`. Двадцать полей и полсотни методов, между которыми нет ничего общего. Все правки проекта так или иначе задевают этот файл.

```java
// Плохо: этот класс делает вообще всё
public class LibraryManager {
    public void addBook(String title) { }
    public void registerReader(String name) { }
    public void issueBook(long bookId, long readerId) { }
    public String buildMonthlyReportHtml() { return ""; }
    public void sendOverdueEmails() { }
    public void backupDatabase() { }
    public double calculateFine(long readerId) { return 0; }
}
```

**Чем вреден.** Такой класс невозможно понять целиком, невозможно протестировать по частям и невозможно менять параллельно двум разработчикам без конфликтов слияния. Это прямое нарушение SRP.

**Как рефакторить.** Сгруппируйте методы по данным, с которыми они работают, и вынесите каждую группу в свой класс (`Extract Class`): `BookCatalog`, `ReaderRegistry`, `LoanService`, `ReportService`, `NotificationService`. Затем передайте их друг другу через конструктор — DIP из части 2 в чистом виде.

### 7.2 Spaghetti Code (Спагетти-код)

**Признаки.** Вложенность условий на пять-шесть уровней, методы по 200 строк, поток управления, который невозможно проследить глазами, флаги вида `boolean isProcessed`, меняющие поведение дальше по коду.

```java
// Плохо: логика утоплена в четырёх уровнях вложенности
public String checkOrder(Order order) {
    if (order != null) {
        if (order.getItems() != null) {
            if (!order.getItems().isEmpty()) {
                if (order.getTotal() > 0) {
                    return "ok";
                } else { return "нулевая сумма"; }
            } else { return "пустой заказ"; }
        } else { return "нет позиций"; }
    }
    return "нет заказа";
}
```

**Как рефакторить.** Ранние возвраты (guard clauses) и извлечение методов:

```java
public String checkOrder(Order order) {
    if (order == null) return "нет заказа";
    if (order.getItems() == null) return "нет позиций";
    if (order.getItems().isEmpty()) return "пустой заказ";
    if (order.getTotal() <= 0) return "нулевая сумма";
    return "ok";
}
```

Тот же смысл, вложенность нулевая. Практическое правило: если метод не помещается на экран, его нужно разбивать.

### 7.3 Lava Flow (Застывшая лава)

**Признаки.** Мёртвый код, который никто не решается удалить. Закомментированные блоки «на всякий случай». Классы с комментарием «не трогать, кажется, используется в отчётах». Конфигурационные флаги, назначения которых никто не помнит.

**Чем вреден.** Такой код читают, в нём ищут ошибки, его переносят при рефакторинге и обновляют при смене API — то есть платят за него постоянно, ничего не получая взамен. Вдобавок он вводит в заблуждение новых разработчиков.

**Как рефакторить.** Удалять. Ваша страховка — система контроля версий: любой удалённый код восстанавливается из истории Git (Лекция 12). Перед удалением убедитесь, что код действительно мёртв: поиск по проекту, анализ неиспользуемого кода в IDE, покрытие тестами. Закомментированный код удаляйте без раздумий — это ровно то, для чего существует Git.

### 7.4 Golden Hammer (Золотой молоток)

**Признаки.** «Если единственный инструмент, который у вас есть, — молоток, всё вокруг начинает выглядеть как гвоздь». Один и тот же приём применяется ко всем задачам: всё через рефлексию, всё через наследование, любая структура данных — `HashMap<String, Object>`, любой класс — Singleton.

**Пример из практики.** Разработчик, влюбившийся в паттерны, заводит фабрику, стратегию и наблюдателя ради класса, который складывает два числа. Или наоборот: команда, знающая только Hibernate, тянет ORM в задачу, где нужно за ночь агрегировать 50 миллионов строк, — а там нужен обычный SQL.

**Как лечить.** Держать в голове альтернативы и явно их сравнивать. Перед выбором технологии сформулируйте, какую конкретную проблему она решает и чем вы за это платите. Мы делали такое сравнение в Лекции 6 (JDBC против Hibernate) — это и есть противоядие.

### 7.5 Magic Numbers (Магические числа)

**Признаки.** Числовые и строковые литералы в коде без объяснения смысла.

```java
// Плохо: что такое 3? что такое 0.13? почему 30?
public double calculateFine(int status, int daysOverdue) {
    if (status == 3) {
        return daysOverdue * 0.13 * 30;
    }
    return 0;
}
```

**Чем вреден.** Через месяц ни автор, ни тем более коллега не скажут, что означает `3`. При изменении ставки придётся искать `0.13` по всему проекту — и легко пропустить одно вхождение или заменить не то.

**Как рефакторить.** Именованные константы и перечисления:

```java
// Два файла пакета ru.fa.patterns.antipatterns.refactored; в каждом — своя строка package ru.fa.patterns.antipatterns.refactored; и нужные импорты
public enum LoanStatus { ACTIVE, RETURNED, OVERDUE }

public class FineCalculator {
    private static final double DAILY_RATE = 0.13;
    private static final int DAYS_IN_BILLING_PERIOD = 30;

    public double calculateFine(LoanStatus status, int daysOverdue) {
        if (status != LoanStatus.OVERDUE) return 0;
        return daysOverdue * DAILY_RATE * DAYS_IN_BILLING_PERIOD;
    }
}
```

Теперь код объясняет сам себя, а ставка меняется в одном месте. Исключения из правила есть: `0`, `1`, `-1` в очевидном контексте константами обычно не оформляют.

### 7.6 Shotgun Surgery (Выстрел дробью)

**Признаки.** Одно логическое изменение требует мелких правок в десятке файлов. Добавили читателю поле «телефон» — правьте сущность, DTO, маппер, форму, валидатор, три отчёта и два теста.

**Чем вреден.** Растёт вероятность что-то забыть, а забытое место обнаруживается в продакшене. Это симптом того, что одна ответственность размазана по системе.

**Как рефакторить.** Собрать разбросанную логику в одном месте: `Move Method` и `Move Field` в тот класс, который «в теме», ввести класс-владелец правила. Если после правок изменение затрагивает один-два файла — рефакторинг удался.

Заметьте связь: **Shotgun Surgery — обратная сторона God Object**. В первом случае ответственность размазана слишком тонко, во втором — собрана слишком густо. Здоровое проектирование лежит посередине: связанное вместе, несвязанное — врозь.

### 7.7 Copy-Paste Programming (Программирование копированием)

**Признаки.** Одинаковые блоки в пяти местах, отличающиеся одной переменной. Найденная ошибка исправляется в одном месте и остаётся в четырёх остальных.

```java
// Плохо: два почти одинаковых метода
public double averageOfBooks(List<Book> books) {
    double sum = 0;
    for (Book b : books) sum += b.getPages();
    return books.isEmpty() ? 0 : sum / books.size();
}

public double averageOfReaders(List<Reader> readers) {
    double sum = 0;
    for (Reader r : readers) sum += r.getBooksTaken();
    return readers.isEmpty() ? 0 : sum / readers.size();
}
```

**Как рефакторить.** Принцип **DRY (Don't Repeat Yourself)** — обобщить через параметр, обобщения или функцию:

```java
public <T> double average(List<T> items, ToDoubleFunction<T> metric) {
    return items.stream().mapToDouble(metric).average().orElse(0);
}
// Вызовы: average(books, Book::getPages) и average(readers, Reader::getBooksTaken)
```

Один метод вместо двух, ошибка исправляется в одном месте. Важная оговорка: DRY — про дублирование **знания**, а не про совпадение символов. Два куска кода, выглядящих одинаково, но меняющихся по разным причинам, объединять не нужно — иначе вы получите Shotgun Surgery.

### 7.8 Feature Envy (Завистливые функции)

**Признаки.** Метод одного класса больше интересуется данными другого класса, чем своими. Длинные цепочки геттеров: `order.getClient().getAddress().getCity()`.

```java
// Плохо: метод живёт в OrderPrinter, а данные тянет из Order
public class OrderPrinter {
    public String describe(Order order) {
        return order.getClient().getName() + ", "
                + order.getClient().getAddress().getCity() + ", сумма "
                + (order.getPrice() * order.getQuantity());
    }
}
```

**Чем вреден.** Логика оторвана от данных: любое изменение структуры `Order` ломает чужой класс. Нарушается инкапсуляция.

**Как рефакторить.** Переместить метод туда, где живут данные (`Move Method`), и следовать правилу **«tell, don't ask»** — не спрашивайте объект о его внутренностях, а просите его сделать работу:

```java
public class Order {
    public double total() { return price * quantity; }
    public String clientCity() { return client.city(); }
}
```

### 7.9 Premature Optimization (Преждевременная оптимизация)

**Признаки.** Кеши, ручные пулы объектов, битовые трюки и отказ от читаемых конструкций «ради скорости» — до того, как хоть что-то измерено. Замена `stream()` на цикл «потому что потоки медленные». Собственная коллекция «потому что `ArrayList` неэффективен».

Дональду Кнуту приписывают формулировку о том, что преждевременная оптимизация — корень многих зол в программировании. Смысл не в том, что оптимизировать не надо, а в том, что оптимизировать надо **измеренное** узкое место, а не то, которое кажется узким.

**Чем вреден.** Вы платите читаемостью и надёжностью за выигрыш, которого может не быть вовсе. Реальное узкое место в типичном веб-приложении — почти всегда база данных и сеть, а не арифметика в Java. Классический пример — проблема N+1 запросов: чтобы показать список из ста заказов, ORM делает один запрос за самими заказами и ещё сто — за клиентом к каждому из них. Никакая микрооптимизация Java-кода не компенсирует эту сотню лишних походов в базу; лечится она одним запросом с `join`, а не переписыванием потока в цикл.

**Как лечить.** Порядок работы: сначала корректно и читаемо, затем измерить профилировщиком, затем оптимизировать конкретное место, затем измерить снова. Оптимизация без замеров — это гадание.

### 7.10 Big Ball of Mud (Большой ком грязи)

**Признаки.** Архитектуры нет. Слои перемешаны: SQL-запрос в контроллере, генерация HTML в репозитории, бизнес-правила в шаблоне страницы. Все классы зависят от всех, между пакетами циклические зависимости. Никто в команде не может нарисовать схему системы на доске.

**Чем вреден.** Это финальная стадия, к которой приводит накопление всех предыдущих антипаттернов. Стоимость любого изменения становится непредсказуемой, а оценка сроков — невозможной.

**Как рефакторить.** Одномоментно — никак: переписывание с нуля почти всегда проваливается. Работающая стратегия:

1. Провести границы: выделить слои (контроллер → сервис → репозиторий) и договориться, что новый код пишется только по этим правилам.
2. Покрыть тестами то, что собираетесь трогать, — без тестов рефакторинг превращается в лотерею.
3. Постепенно вытеснять старый код: новая функциональность пишется в новой структуре, старая переносится по кусочкам.
4. Следить за метриками: цикломатическая сложность, размер классов, циклические зависимости (SonarQube, ArchUnit).

---

## Часть 8: Рефакторинг и применение паттернов в реальном проекте

Квартиру не ремонтируют, снося стены наугад. Сначала фотографируют, как было, потом делают по одной комнате, и после каждой проверяют, что вода течёт, а свет горит. Тот, кто разбирает всю квартиру за один вечер, живёт среди мешков со штукатуркой до весны. Рефакторинг устроен ровно так же: снимок текущего поведения, один маленький шаг, проверка — и только потом следующий шаг.

### 8.1 Разбор одного рефакторинга целиком

Посмотрим, как несколько антипаттернов лечатся паттернами на одном примере. Исходный код содержит магические числа, спагетти-логику и нарушение OCP:

```java
// Было
public class PriceCalculator {
    public double calculate(String clientType, double amount) {
        if (clientType.equals("1")) {
            return amount;
        } else if (clientType.equals("2")) {
            return amount * 0.95;
        } else if (clientType.equals("3")) {
            return amount > 10000 ? amount * 0.85 : amount * 0.9;
        }
        throw new IllegalArgumentException("Неизвестный тип: " + clientType);
    }
}
```

Проблемы: тип клиента закодирован строками-числами; при добавлении четвёртого типа придётся править этот метод; логику скидки нельзя протестировать отдельно.

Шаг 1 — убираем магические значения перечислением. Шаг 2 — выносим каждый вариант расчёта в отдельную стратегию. Шаг 3 — связываем их так, чтобы новый тип клиента не требовал правки калькулятора:

```java
// Три файла пакета ru.fa.patterns.behavioral; в каждом — своя строка package ru.fa.patterns.behavioral; и нужные импорты
// Стало
@FunctionalInterface
public interface PricingRule { double apply(double amount); }

public enum ClientType {
    REGULAR(amount -> amount),
    LOYAL(amount -> amount * 0.95),
    VIP(ClientType::vipPrice);

    private static final double VIP_THRESHOLD = 10_000;

    private final PricingRule rule;

    ClientType(PricingRule rule) { this.rule = rule; }

    // Правило вынесено в метод: статическое поле нельзя читать
    // прямо из объявления константы перечисления
    private static double vipPrice(double amount) {
        return amount > VIP_THRESHOLD ? amount * 0.85 : amount * 0.90;
    }

    public double priceFor(double amount) { return rule.apply(amount); }
}

public class PriceCalculator {
    // Метод не изменится, сколько бы типов клиентов ни добавили
    public double calculate(ClientType type, double amount) { return type.priceFor(amount); }
}
```

Что мы получили: невозможный тип клиента отсекается компилятором, а не исключением в рантайме; каждое правило проверяется отдельным тестом; добавление типа `PARTNER` требует одной строки в перечислении и не трогает `PriceCalculator` (OCP). Здесь одновременно применены Стратегия и типичный для Java приём «перечисление с поведением».

### 8.2 Порядок действий при рефакторинге

1. **Тесты первыми.** Пока поведение не зафиксировано тестами (Лекция 10: JUnit 5, Mockito), любой рефакторинг — риск. Тесты пишутся на текущее поведение, включая странное.
2. **Мелкими шагами.** Извлекли метод — запустили тесты. Переименовали — запустили. Большой рефакторинг одним коммитом почти всегда заканчивается откатом.
3. **Один рефакторинг за раз.** Не смешивайте изменение поведения с изменением структуры в одном коммите: при поиске регрессии вы не поймёте, что именно сломалось.
4. **Пользуйтесь автоматикой IDE.** `Extract Method`, `Rename`, `Move`, `Introduce Parameter` в IntelliJ IDEA выполняются безопасно и за секунду.

### 8.3 Как выбирать паттерн

| Что болит | Что попробовать |
|-----------|-----------------|
| Длинный `if`/`switch` по типу или статусу | Стратегия, Состояние, полиморфизм |
| Конструктор с восемью параметрами | Строитель |
| Класс зависит от конкретной реализации | DIP, внедрение зависимостей |
| Нужно добавить поведение, не меняя класс | Декоратор, Посетитель |
| Нужны логирование, кеш, права доступа поверх вызова | Заместитель, AOP |
| Несовместимый сторонний API | Адаптер |
| Сложная подсистема, а нужен один сценарий | Фасад |
| «Кто-то должен узнать, что произошло событие» | Наблюдатель |
| Общий скелет алгоритма с разными шагами | Шаблонный метод |
| Древовидная структура, обрабатываемая единообразно | Компоновщик |
| Нужны отмена операции и история | Команда, Снимок |
| Много одинаковых объектов, не хватает памяти | Приспособленец |

И главное правило, которым стоит закончить: **паттерн вводят в ответ на реальную боль, а не заранее**. Хороший код чаще получается рефакторингом простого решения, чем проектированием сложного с нуля.

---

## Часть 9: Итоги

От принципов SOLID до конкретных паттернов и антипаттернов — сводная таблица по всей лекции:

| Технология | Ключевые концепции |
|------------|-------------------|
| Паттерны GoF | 23 паттерна, три группы: порождающие, структурные, поведенческие; общий словарь проектирования; риск over-engineering |
| SOLID | SRP (одна ответственность), OCP (расширение без изменения), LSP (подстановка), ISP (узкие интерфейсы), DIP (зависимость от абстракций) |
| Singleton | Приватный конструктор, `volatile` + double-checked locking, вариант через `enum`; в Spring — scope `singleton` |
| Factory Method | Подкласс решает, какой продукт создать; `Collection.iterator()`, `FactoryBean` |
| Abstract Factory | Семейство согласованных продуктов; `DocumentBuilderFactory` |
| Builder | Пошаговая сборка, неизменяемый объект, валидация в `build()`; `StringBuilder`, `HttpRequest.newBuilder()` |
| Prototype | Копирование объекта, глубокое против поверхностного, конструктор копирования; scope `prototype` |
| Adapter | Переходник между несовместимыми интерфейсами; `InputStreamReader`, `Arrays.asList()` |
| Bridge | Разделение абстракции и реализации; архитектура JDBC |
| Composite | Единообразная работа с деревом; граф сцены JavaFX |
| Decorator | Обёртка, добавляющая поведение; `BufferedReader`, `Collections.unmodifiableList()` |
| Facade | Простой вход в сложную подсистему; `JdbcTemplate`, `RestTemplate` |
| Flyweight | Разделение неизменяемого состояния; кеш `Integer.valueOf()`, пул строк |
| Proxy | Контроль доступа через объект-дублёр; `java.lang.reflect.Proxy`, `@Transactional`, AOP |
| Chain of Responsibility | Цепочка обработчиков; фильтры сервлетов, `SecurityFilterChain` |
| Command | Запрос как объект, отмена и очередь; `Runnable` в `ExecutorService` |
| Interpreter | Грамматика как дерево объектов; `Pattern`, SpEL |
| Iterator | Обход без раскрытия структуры; Collections Framework, `for-each` |
| Mediator | Общение через посредника; `ApplicationEventPublisher`, `DispatcherServlet` |
| Memento | Снимок состояния и восстановление; сериализация, savepoint |
| Observer | Подписка на события; `@EventListener`, слушатели JavaFX, `Flow` |
| State | Поведение зависит от состояния; переходы вместо `if` по статусу |
| Strategy | Взаимозаменяемые алгоритмы; `Comparator`, `PasswordEncoder`, любой внедряемый бин |
| Template Method | Скелет алгоритма в `final`-методе, шаги в подклассах; `JdbcTemplate`, `HttpServlet` |
| Visitor | Новая операция без правки классов; `FileVisitor`; альтернатива — `sealed` + `switch` |
| God Object | Класс делает всё; лечится `Extract Class` и SRP |
| Spaghetti Code | Глубокая вложенность; лечится guard clauses и `Extract Method` |
| Lava Flow | Мёртвый и закомментированный код; удалять, история хранится в Git |
| Golden Hammer | Один инструмент на все задачи; явно сравнивать альтернативы |
| Magic Numbers | Литералы без смысла; именованные константы и `enum` |
| Shotgun Surgery | Одно изменение — правки в десятке файлов; собрать ответственность вместе |
| Copy-Paste Programming | Дублирование знания; DRY, обобщения, `Extract Method` |
| Feature Envy | Метод тянет чужие данные; `Move Method`, «tell, don't ask» |
| Premature Optimization | Оптимизация без замеров; сначала профилировать, потом оптимизировать |
| Big Ball of Mud | Отсутствие архитектуры; слои, тесты, постепенное вытеснение |
| Рефакторинг | Тесты первыми, мелкие шаги, автоматика IDE, один рефакторинг за раз |
