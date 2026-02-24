# Лекция 3: Ветвление, Циклы и ООП

## Введение

Добро пожаловать на третью лекцию курса "Современные технологии программирования". На прошлых занятиях мы познакомились с основами Java — архитектурой, типами данных, операторами, а также классами и интерфейсами. Сегодня мы сделаем следующий важный шаг: научимся управлять потоком выполнения программы с помощью ветвлений и циклов, а затем погрузимся в три фундаментальных принципа объектно-ориентированного программирования — наследование, инкапсуляцию и полиморфизм. Также мы познакомимся с современным синтаксисом `switch` (Java 14+), паттерн-матчингом (Java 17+, 21+), ключевыми словами `super`, `this`, `final`, `sealed` и модификаторами доступа. К концу лекции вы будете свободно ориентироваться во всех этих конструкциях.

---

## Часть 1: Ветвление (Branching)

Любая реальная программа должна принимать решения. Представьте навигатор: если дорога перекрыта — поехать в объезд, если свободна — ехать прямо. Именно для таких "развилок" в коде существуют операторы ветвления. Давайте разберём их по порядку.

### 1.1 Оператор if/else

`if/else` — основной оператор ветвления, выполняет блок кода при истинности условия:

```java
// 1. Простой if и if-else
public static void simpleIfElse(int number) {
    if (number > 0) {
        System.out.println("Положительное число");
    } else {
        System.out.println("Неположительное число");
    }
}

// 2. Цепочка if-else-if
public static void ifElseIf(int score) {
    if (score >= 90) {
        System.out.println("Оценка A");
    } else if (score >= 75) {
        System.out.println("Оценка B");
    } else if (score >= 60) {
        System.out.println("Оценка C");
    } else {
        System.out.println("Неудовлетворительно");
    }
}
```

**Правила:**
- Условие в `if` должно быть типа `boolean`
- Блоки `{}` не обязательны для одного оператора, но **рекомендуются** всегда
- `else if` и `else` — опциональны

> **Попробуй в jshell!** Откройте `jshell` и поэкспериментируйте с условиями:
> ```
> jshell> int score = 82
> jshell> if (score >= 90) System.out.println("A"); else if (score >= 75) System.out.println("B"); else System.out.println("C");
> ```

### 1.2 Тернарный оператор

Краткая форма `if/else` для присваивания:

```java
// 3. Тернарный оператор
public static void ternaryOperator(int age) {
    String result = (age >= 18) ? "Совершеннолетний" : "Несовершеннолетний";
    System.out.println(result);
}
```

Обратите внимание: тернарный оператор удобен, когда нужно выбрать одно из двух значений. Но если логика сложнее — лучше использовать обычный `if/else`, чтобы код оставался читаемым.

### 1.3 Оператор switch

Когда вариантов выбора больше двух-трёх, цепочка `if-else if` становится громоздкой. Здесь на помощь приходит `switch` — он позволяет элегантно обработать множество случаев.

#### Классический switch (до Java 14)

```java
// 4. Классический switch
public static void classicSwitch(int day) {
    switch (day) {
        case 1:
            System.out.println("Понедельник");
            break;
        case 2:
        case 3:
            System.out.println("Вторник или среда");
            break;
        case 4:
            System.out.println("Четверг");
            break;
        default:
            System.out.println("Другой день");
            break;
    }
}
```

**Важно:** Без `break` выполнение "проваливается" (fall-through) в следующий `case`. Это иногда используется намеренно, но чаще является ошибкой.

#### Стрелочный switch (Java 14+ — без fall-through)

Стрелочный синтаксис устраняет fall-through. Может использоваться как **оператор** (выполняет действие) или как **выражение** (возвращает значение).

**Switch как оператор (statement) — без возврата значения:**
```java
// 5. Switch с оператором -> (Java 14+)
public static void arrowSwitch(int level) {
    switch (level) {
        case 1 -> System.out.println("Начинающий");
        case 2, 3 -> System.out.println("Средний уровень");
        case 4 -> System.out.println("Продвинутый");
        default -> System.out.println("Неизвестный уровень");
    }
```

**Switch как выражение (expression) — присваивание результата:**
```java
    String str = switch (level) {
        case 1 -> "Один";
        default -> "Другое";
    };
}
```

**Switch как выражение с блоком и `yield` (для многострочного кода):**
```java
// 6. Switch с yield (Java 14+)
public static void switchWithYield(String code) {
    String result = switch (code) {
        case "A" -> {
            System.out.println("Обработка кода A");
            yield "Результат A";
        }
        case "B", "C" -> {
            yield "Результат B или C";
        }
        default -> {
            yield "Неизвестный код";
        }
    };
    System.out.println(result);
}
```

#### Паттерн-матчинг в switch (Java 17+)

Вы могли заметить, что классический `switch` работает только с конкретными значениями. Начиная с Java 17, появилась возможность сопоставления по типу, а в Java 21 добавился оператор `when` для дополнительных условий. Это делает `switch` по-настоящему мощным инструментом.

```java
// 7. Switch с сопоставлением по типу (Java 17+)
public static void patternSwitch(Object obj) {
    switch (obj) {
        case String s -> System.out.println("Это строка: " + s);
        case Integer i -> System.out.println("Это целое число: " + i);
        case null -> System.out.println("Это null");
        default -> System.out.println("Неизвестный тип");
    }
}

// 8. Switch с оператором when (Java 21+)
public static void patternSwitchWithWhen(Object obj) {
    switch (obj) {
        case String s when s.length() > 5 -> System.out.println("Длинная строка: " + s);
        case String s -> System.out.println("Короткая строка: " + s);
        case Integer i when i > 100 -> System.out.println("Большое число: " + i);
        default -> System.out.println("Другое значение");
    }
}
```

**switch может работать с:**
- `int`, `byte`, `short`, `char` (и их обёртками)
- `String` (с Java 7)
- `enum`
- `Object` (с Java 21, при паттерн-матчинге)

---

## Часть 2: Циклы (Loops)

Теперь, когда мы разобрались с ветвлением, перейдём к циклам. Если ветвление — это "развилка на дороге", то цикл — это "круговое движение": программа повторяет одни и те же действия, пока не будет выполнено условие выхода. В Java есть несколько видов циклов, каждый из которых удобен в своей ситуации.

### 2.1 Цикл while

Выполняется **пока** условие истинно. Условие проверяется **до** тела:

```java
// 1. Цикл while
public static void exampleWhile() {
    int i = 0;
    while (i < 5) {
        System.out.println("Итерация while: " + i);
        i++;
    }
}
```

### 2.2 Цикл do-while

Тело выполняется **хотя бы один раз**, затем проверяется условие:

```java
// 2. Цикл do-while
public static void exampleDoWhile() {
    int i = 0;
    do {
        System.out.println("Итерация do-while: " + i);
        i++;
    } while (i < 5);
}
```

Это важный момент: если вам нужно гарантировать хотя бы одно выполнение тела цикла (например, запросить ввод от пользователя и проверить его), `do-while` — ваш выбор.

### 2.3 Цикл for

Наиболее компактный цикл — инициализация, условие и шаг в одной строке:

```java
// 3. Классический цикл for
public static void exampleFor() {
    for (int i = 0; i < 5; i++) {
        System.out.println("Итерация for: " + i);
    }
}
```

> **Попробуй в jshell!** Циклы отлично подходят для экспериментов:
> ```
> jshell> for (int i = 1; i <= 5; i++) System.out.print(i + " ")
> ```

### 2.4 Цикл for-each (расширенный for)

Предназначен для итерации по массивам и коллекциям:

```java
// 4. Расширенный цикл for (foreach)
public static void exampleForEach() {
    int[] numbers = {10, 20, 30, 40};
    for (int num : numbers) {
        System.out.println("Элемент массива: " + num);
    }
}
```

Давайте подчеркнём: `for-each` — самый безопасный и читаемый способ пройтись по коллекции, когда вам не нужен индекс элемента.

### 2.5 Управление циклами: break, continue, метки

Иногда цикл нужно прервать досрочно или пропустить одну итерацию. Для этого в Java есть `break`, `continue` и механизм меток для вложенных циклов.

```java
// 5. Прерывание цикла с помощью break
public static void exampleBreak() {
    for (int i = 0; i < 10; i++) {
        if (i == 5) {
            System.out.println("Прерывание цикла при i = 5");
            break;
        }
        System.out.println("Итерация: " + i);
    }
}

// 6. Пропуск итерации с помощью continue
public static void exampleContinue() {
    for (int i = 0; i < 5; i++) {
        if (i == 2) {
            System.out.println("Пропущена итерация при i = 2");
            continue;
        }
        System.out.println("Итерация: " + i);
    }
}

// 7. Использование метки с break и continue
public static void exampleLabeledLoops() {
    outerLoop:
    for (int i = 1; i <= 3; i++) {
        for (int j = 1; j <= 3; j++) {
            if (i == 2 && j == 2) {
                System.out.println("Выход из внешнего цикла при i = 2, j = 2");
                break outerLoop;
            }
            System.out.println("i = " + i + ", j = " + j);
        }
    }

    System.out.println("Пример continue с меткой:");
    outer:
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (j == 1) {
                continue outer;
            }
            System.out.println("i = " + i + ", j = " + j);
        }
    }
}
```

---

## Часть 3: Объектно-Ориентированное Программирование

Мы освоили ветвление и циклы — теперь перейдём к самой главной теме этой лекции. Объектно-ориентированное программирование (ООП) — это парадигма, вокруг которой построена вся Java. На первой лекции мы уже упоминали, что Java — объектно-ориентированный язык, а на второй — работали с классами и интерфейсами. Сегодня мы разберём три фундаментальных принципа, на которых стоит ООП:

| Принцип | Суть |
|---------|------|
| **Наследование** | Класс-потомок расширяет класс-родитель |
| **Инкапсуляция** | Скрытие внутреннего состояния, доступ только через методы |
| **Полиморфизм** | Один интерфейс — разное поведение |
| Абстракция | Выделение существенных характеристик |

### 3.1 Наследование (Inheritance)

Наследование позволяет создавать **иерархию классов**, где потомок получает (наследует) все поля и методы родителя.

**Важно:** Java поддерживает только **одиночное наследование классов** — класс может наследовать (`extends`) только один класс. Однако класс может реализовывать (`implements`) несколько интерфейсов.

**Аналогия:** В природе все животные имеют общие черты (дышат, едят, двигаются). Конкретные виды (собаки, кошки) уточняют эти черты. Класс `Animal` — родитель, `Dog` и `Cat` — потомки. Точно так же в реальном коде: общее поведение описывается в родительском классе, а каждый потомок добавляет свою специфику.

```java
class Animal {
    String name;

    public Animal(String name) {
        this.name = name;
    }

    public void speak() {
        System.out.println(name + " издаёт звук.");
    }

    public final void sleep() {
        System.out.println(name + " спит.");
    }
}

interface Movable {
    void move();

    default void description() {
        System.out.println("Этот объект может двигаться.");
    }
}

abstract class Bird extends Animal {
    public Bird(String name) {
        super(name);
    }

    public abstract void fly();
}

class Dog extends Animal implements Movable {

    public Dog(String name) {
        super(name);
    }

    @Override
    public void speak() {
        System.out.println(name + " лает.");
    }

    @Override
    public void move() {
        System.out.println(name + " бежит.");
    }
}
```

Обратите внимание на метод `sleep()` — он помечен как `final`, а значит, ни один подкласс не сможет его переопределить. Мы подробнее поговорим о `final` чуть ниже.

**Ключевое слово `super`:**

**Правило:** Вызов `super()` должен быть **первой инструкцией** в конструкторе подкласса. Аналогично, `this()` должен быть первой инструкцией при делегировании конструктора. Нельзя использовать `super()` и `this()` в одном конструкторе одновременно.

```java
public class Dog extends Animal {
    public Dog(String name, int age) {
        super(name, age);  // super() — вызов конструктора родителя (ОБЯЗАТЕЛЬНО первая строка!)
    }

    @Override
    public void eat() {
        super.eat();  // super.methodName() — вызов метода родителя
        System.out.println("(И ещё просит добавки)");
    }

    public String getInfo() {
        return super.toString() + " - собака";
    }

    public void showParentName() {
        System.out.println(super.name);  // super.fieldName — доступ к полю родителя
    }
}
```

**`InterfaceName.super.methodName()`** — нужен при конфликте default-методов двух интерфейсов:
```java
interface A { default void hello() { System.out.println("Привет от A"); } }
interface B { default void hello() { System.out.println("Привет от B"); } }

class C implements A, B {
    @Override
    public void hello() {
        A.super.hello(); // Явно указываем, метод какого интерфейса вызвать
    }
}
```

**Ключевое слово `this`:**
```java
public class Circle {
    private double radius;

    // this() — делегирование конструктора
    public Circle() {
        this(1.0);  // Вызывает другой конструктор этого же класса
    }

    public Circle(double radius) {
        this.radius = radius;  // this.поле — обращение к полю класса
    }

    // this как ссылка на текущий объект
    public Circle setRadius(double radius) {
        this.radius = radius;
        return this;  // Возвращает сам объект (Fluent API)
    }
}
```

### 3.2 Запрет наследования: final и sealed

Теперь разберём, как ограничить наследование. Иногда вы хотите, чтобы ваш класс или метод нельзя было изменить в подклассах — для этого существуют ключевые слова `final` и `sealed`.

**`final` переменная** — значение нельзя изменить после присваивания:
```java
final int MAX = 100;    // Константа — нельзя присвоить другое значение
// MAX = 200;           // Ошибка компиляции!
```

**`final` параметр метода** — параметр нельзя переназначить внутри метода. Важно: это не делает объект неизменяемым — только ссылку нельзя изменить:
```java
public void process(final String name, final List<String> items) {
    // name = "другое";      // Ошибка! Нельзя переназначить ссылку
    items.add("новый");      // OK! Объект изменяем, только ссылка final
}
```

**`final` класс** — от него нельзя наследоваться:
```java
public final class String { ... }   // Нельзя: class MyString extends String
public final class Math { ... }     // Нельзя: class MyMath extends Math
```

**`final` метод** — нельзя переопределить:
```java
public class Base {
    public final void criticalMethod() {
        // Гарантированно не будет переопределён
    }
}
```

**`sealed` класс (Java 17+)** — ограничивает, какие классы могут наследоваться. Каждый подкласс `sealed`-класса **обязан** иметь один из модификаторов: `final` (запрет дальнейшего наследования), `sealed` (ограниченное наследование) или `non-sealed` (снятие ограничения):

```java
sealed class Vehicle permits Car, Bicycle {
    public void start() {
        System.out.println("Транспортное средство начинает движение.");
    }
}

final class Car extends Vehicle {
    // final — нельзя наследовать от Car
}

non-sealed class Bicycle extends Vehicle {
}

class MountainBike extends Bicycle {
}
```

`sealed` удобен вместе с паттерн-матчингом:
```java
double area = switch (shape) {
    case Circle c -> Math.PI * c.radius() * c.radius();
    case Rectangle r -> r.width() * r.height();
    case Triangle t -> 0.5 * t.base() * t.height();
    // default не нужен — компилятор знает все подтипы Shape!
};
```

### 3.3 Инкапсуляция (Encapsulation)

Перейдём к следующему столпу ООП. Инкапсуляция — это **сокрытие внутреннего состояния** объекта и предоставление доступа к нему только через **контролируемые методы**.

**Аналогия:** Автомобиль скрывает сложный двигатель за педалями и рулём. Вы не можете напрямую управлять клапанами двигателя — только через педаль газа (публичный интерфейс). Точно так же в коде: поля объекта скрыты (`private`), а доступ к ним идёт через getter- и setter-методы, которые могут проверять корректность данных.

#### Модификаторы доступа

| Модификатор | Тот же класс | Тот же пакет | Подкласс | Все |
|-------------|:---:|:---:|:---:|:---:|
| `private` | ✅ | ❌ | ❌ | ❌ |
| (package-private) | ✅ | ✅ | ❌ | ❌ |
| `protected` | ✅ | ✅ | ✅ | ❌ |
| `public` | ✅ | ✅ | ✅ | ✅ |

Давайте разберём пример, где инкапсуляция защищает данные от некорректных значений:

```java
public class EncapsulationExamples {
    private String name;
    private int age;

    public EncapsulationExamples(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        if (name != null && !name.isEmpty()) {
            this.name = name;
        }
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        if (age >= 0) {
            this.age = age;
        }
    }

    public void printInfo() {
        System.out.println("Имя: " + name + ", возраст: " + age);
    }

    public static void main(String[] args) {
        EncapsulationExamples person = new EncapsulationExamples("Анна", 25);
        person.printInfo();

        person.setName("Мария");
        person.setAge(30);
        person.printInfo();

        person.setName("");
        person.setAge(-10);
        person.printInfo();
    }
}
```

### 3.4 Полиморфизм (Polymorphism)

Полиморфизм — способность одного интерфейса работать с разными типами данных. Это, пожалуй, самый мощный принцип ООП.

**Аналогия:** Кнопка "Сохранить" работает одинаково для документа, таблицы и презентации. Один интерфейс (`save()`) — разная реализация. Пользователь нажимает одну и ту же кнопку, но под капотом каждый тип файла сохраняется по-своему.

В Java полиморфизм реализуется двумя способами:
1. **Переопределение методов (Override)** — полиморфизм времени выполнения
2. **Перегрузка методов (Overload)** — полиморфизм времени компиляции

#### Переопределение (Method Overriding)

```java
interface Shape {
    void draw();
}

class Circle implements Shape {
    @Override
    public void draw() {
        System.out.println("Рисуется круг");
    }

    public void draw(String color) {
        System.out.println("Рисуется круг цвета: " + color);
    }
}

class Rectangle implements Shape {
    @Override
    public void draw() {
        System.out.println("Рисуется прямоугольник");
    }
}

public class Main {
    public static void main(String[] args) {
        Shape s1 = new Circle();
        Shape s2 = new Rectangle();

        s1.draw();
        s2.draw();

        Circle c = new Circle();
        c.draw();
        c.draw("красный");

        if (s1 instanceof Circle) {
            Circle realCircle = (Circle) s1;
            realCircle.draw("синий");
        }

        if (s2 instanceof Circle) {
            Circle notACircle = (Circle) s2;
        }
    }
}
```

**Правила переопределения:**
- Имя метода и параметры должны совпадать
- Тип возвращаемого значения должен быть тем же или более узким (ковариантный тип)
- Нельзя сужать видимость (`public` нельзя переопределить как `private`)
- Нельзя бросать новые checked исключения

#### Перегрузка (Method Overloading)

```java
public class Printer {
    // Один и тот же метод — разные сигнатуры
    public void print(String text) {
        System.out.println(text);
    }

    public void print(int number) {
        System.out.println("Число: " + number);
    }

    public void print(String text, int times) {
        for (int i = 0; i < times; i++) {
            System.out.println(text);
        }
    }

    public void print(double... values) { // Varargs
        for (double v : values) {
            System.out.printf("%.2f ", v);
        }
        System.out.println();
    }
}

// Компилятор выбирает нужный метод по типам аргументов:
Printer p = new Printer();
p.print("Привет");          // вызывает print(String)
p.print(42);                // вызывает print(int)
p.print("Привет", 3);      // вызывает print(String, int)
p.print(1.1, 2.2, 3.3);   // вызывает print(double...)
```

**Разница Override vs Overload:**

| | Override (переопределение) | Overload (перегрузка) |
|---|---|---|
| Когда | Время выполнения (runtime) | Время компиляции |
| Сигнатура | Одинаковая | Разные параметры |
| Класс | В подклассе | В том же классе |
| `@Override` | Рекомендуется | Нельзя использовать |

---

## Часть 4: Instanceof и приведение типов

Работая с полиморфизмом, вы часто будете сталкиваться с ситуацией, когда нужно определить реальный тип объекта. Для этого в Java существует оператор `instanceof` и механизм приведения типов.

В Java приведение типов делится на два вида:
- **Восходящее (upcasting)** — от подкласса к родительскому классу. Выполняется **неявно** и всегда безопасно: `Animal a = new Dog("Рекс");`
- **Нисходящее (downcasting)** — от родительского класса к подклассу. Требует **явного** приведения и может вызвать `ClassCastException`, если объект не является экземпляром целевого типа: `Dog d = (Dog) animal;`

```java
Animal animal = new Dog("Рекс", 3);

// Проверка типа перед downcasting (нисходящим приведением)
if (animal instanceof Dog) {
    Dog dog = (Dog) animal; // Явное приведение типа (downcasting)
    dog.fetch();
}
// Без проверки — рискованно:
// String s = (String) animal; // ClassCastException в рантайме!

// Паттерн-матчинг instanceof (Java 16+) — объединяет проверку и приведение:
if (animal instanceof Dog dog) {   // dog уже имеет тип Dog
    dog.fetch();
}

// Пример с полиморфизмом:
Animal[] zoo = {
    new Dog("Рекс", 3),
    new Cat("Мурка", 5),
    new Dog("Бобик", 2)
};

for (Animal a : zoo) {
    if (a instanceof Dog d) {
        System.out.println(d.name + " умеет приносить!");
        d.fetch();
    }
}
```

---

## Часть 5: Абстрактные классы vs Интерфейсы

Один из частых вопросов у начинающих Java-разработчиков: когда использовать абстрактный класс, а когда — интерфейс? Давайте разберём их различия и посмотрим, как они работают вместе.

| Критерий | Абстрактный класс | Интерфейс |
|----------|-------------------|-----------|
| `extends`/`implements` | `extends` (один) | `implements` (несколько) |
| Конструктор | Есть | Нет |
| Поля | Любые | `public static final` |
| Методы | Любые | `public` (default/static — с Java 8) |
| Когда | Частичная реализация, общее состояние | Контракт, множественное наследование |

```java
// Абстрактный класс — частичная реализация
abstract class Vehicle {
    protected String brand;
    protected int year;

    public Vehicle(String brand, int year) {
        this.brand = brand;
        this.year = year;
    }

    // Реализованный метод
    public void start() {
        System.out.println(brand + " запускается...");
    }

    // Абстрактный — подкласс ОБЯЗАН реализовать
    public abstract int getSpeed();
}

// Интерфейс — контракт
interface Electric {
    int getBatteryLevel();
    void charge();
}

interface GPS {
    double[] getCoordinates();
}

// Класс наследует Vehicle и реализует два интерфейса
class TeslaModelS extends Vehicle implements Electric, GPS {
    private int batteryLevel;

    public TeslaModelS(int batteryLevel) {
        super("Tesla", 2024);
        this.batteryLevel = batteryLevel;
    }

    @Override
    public int getSpeed() { return 250; }

    @Override
    public int getBatteryLevel() { return batteryLevel; }

    @Override
    public void charge() { batteryLevel = 100; }

    @Override
    public double[] getCoordinates() { return new double[]{55.75, 37.61}; }
}
```

---

## Часть 6: Итоги

Подведём итоги. В этой лекции мы прошли большой путь — от простых условных конструкций до фундаментальных принципов ООП:

| Конструкция | Назначение |
|-------------|------------|
| `if/else` | Условное ветвление |
| Тернарный `?:` | Краткая форма if/else для выражений |
| `switch` (классический) | Множественное ветвление, fall-through |
| `switch` (стрелочный) | Множественное ветвление без fall-through, Java 14+ |
| `while` | Цикл с проверкой условия до тела |
| `do-while` | Цикл с гарантированным первым выполнением |
| `for` | Счётный цикл |
| `for-each` | Итерация по коллекциям и массивам |
| `break`/`continue` | Управление потоком в циклах |
| `extends` | Наследование класса |
| `super` | Обращение к родительскому классу |
| `final` | Запрет изменения (переменная/параметр), переопределения (метод), наследования (класс) |
| `sealed` | Ограничение иерархии наследования |
| `@Override` | Аннотация переопределения метода |
| Модификаторы доступа | Инкапсуляция |

---

## Часть 7: Дополнительные примеры

Для закрепления материала рассмотрим комплексный пример, в котором наследование, инкапсуляция и полиморфизм работают вместе.

### Иерархия фигур с полиморфизмом

```java
abstract class Shape {
    protected String color;

    public Shape(String color) { this.color = color; }

    public abstract double area();
    public abstract double perimeter();

    @Override
    public String toString() {
        return String.format("%s[цвет=%s, площадь=%.2f, периметр=%.2f]",
            getClass().getSimpleName(), color, area(), perimeter());
    }
}

class Circle extends Shape {
    private double radius;

    public Circle(String color, double radius) {
        super(color);
        this.radius = radius;
    }

    @Override public double area() { return Math.PI * radius * radius; }
    @Override public double perimeter() { return 2 * Math.PI * radius; }
}

class Rectangle extends Shape {
    private double width, height;

    public Rectangle(String color, double width, double height) {
        super(color);
        this.width = width;
        this.height = height;
    }

    @Override public double area() { return width * height; }
    @Override public double perimeter() { return 2 * (width + height); }
}

// Использование полиморфизма:
List<Shape> shapes = List.of(
    new Circle("red", 5),
    new Rectangle("blue", 4, 6),
    new Circle("green", 3)
);

// Всё работает через полиморфизм:
shapes.forEach(System.out::println);
double totalArea = shapes.stream().mapToDouble(Shape::area).sum();
System.out.printf("Общая площадь: %.2f%n", totalArea);
```
