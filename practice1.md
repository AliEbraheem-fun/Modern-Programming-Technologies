# Практическое занятие 1: Основы Java

## Часть 1: Первая программа

### Задание 1.1: Hello World

1. Создайте файл `HelloWorld.java`
2. Напишите программу, которая выводит ваше имя и группу:

```
Привет! Меня зовут [Ваше имя]
Я студент группы [Номер группы]
```

**Подсказка:** Используйте `System.out.println()` для каждой строки.

### Задание 1.2: Компиляция и запуск

Выполните в терминале:

```bash
# Скомпилируйте программу
javac HelloWorld.java

# Запустите программу
java HelloWorld
```

**Вопрос:** Какой файл появился после компиляции? Что в нём содержится?

### Задание 1.3: Ошибки компиляции

Попробуйте скомпилировать код с ошибками. Исправьте их:

```java
public class Errors {
    public static void main(String[] args) {
        System.out.println("Привет мир!")
        system.out.println("Вторая строка");
        System.out.println(Без кавычек);
    }
}
```

**Запишите:** Какие ошибки выдал компилятор? Как вы их исправили?

---

## Часть 2: Знакомство с jshell

### Задание 2.1: Запуск jshell

Откройте терминал и введите:

```bash
jshell
```

Выполните следующие команды и запишите результаты:

```
jshell> 2 + 2
jshell> 10 / 3
jshell> 10.0 / 3
jshell> "Hello" + " " + "World"
jshell> Math.sqrt(16)
jshell> Math.PI
```

### Задание 2.2: Переменные в jshell

Создайте переменные и выполните операции:

```
jshell> int age = 20
jshell> String name = "Студент"
jshell> System.out.println("Имя: " + name + ", Возраст: " + age)
```

**Команды для изучения:**
- `/vars` — показать все переменные
- `/list` — показать введённый код
- `/exit` — выйти из jshell

---

## Часть 3: Примитивные типы данных

### Задание 3.1: Объявление переменных

Создайте файл `DataTypes.java` и объявите переменные всех примитивных типов:

```java
public class DataTypes {
    public static void main(String[] args) {
        // Целочисленные типы
        byte myByte = ____;      // от -128 до 127
        short myShort = ____;    // от -32768 до 32767
        int myInt = ____;        // от -2.1 млрд до 2.1 млрд
        long myLong = ____L;     // большие числа (не забудьте L!)

        // Дробные типы
        float myFloat = ____f;   // не забудьте f!
        double myDouble = ____;

        // Символ и логический тип
        char myChar = '____';
        boolean myBoolean = ____;

        // Выведите все переменные
        System.out.println("byte: " + myByte);
        // ... продолжите для остальных
    }
}
```

### Задание 3.2: Переполнение (Overflow)

Выполните в jshell и объясните результаты:

```
jshell> byte b = 127
jshell> b++
jshell> b

jshell> int max = Integer.MAX_VALUE
jshell> max + 1
```

**Вопрос:** Почему `127 + 1` для `byte` даёт `-128`?

### Задание 3.3: Точность дробных чисел

Проверьте в jshell:

```
jshell> 0.1 + 0.2
jshell> 0.1 + 0.2 == 0.3
```

**Вопрос:** Почему результат не равен 0.3? Как это учитывать при написании программ?

### Задание 3.4: Литералы в разных системах счисления

Создайте файл `NumberSystems.java`:

```java
public class NumberSystems {
    public static void main(String[] args) {
        int decimal = 42;           // десятичная
        int hex = 0x2A;             // шестнадцатеричная (0x)
        int octal = 052;            // восьмеричная (0)
        int binary = 0b101010;      // двоичная (0b)

        System.out.println("Десятичная: " + decimal);
        System.out.println("Шестнадцатеричная: " + hex);
        System.out.println("Восьмеричная: " + octal);
        System.out.println("Двоичная: " + binary);

        // Все ли значения равны?
        System.out.println("Все равны: " + (decimal == hex && hex == octal && octal == binary));
    }
}
```

---

## Часть 4: Операторы

### Задание 4.1: Арифметические операторы

Создайте файл `Calculator.java`:

```java
public class Calculator {
    public static void main(String[] args) {
        int a = 17;
        int b = 5;

        System.out.println("a = " + a + ", b = " + b);
        System.out.println("a + b = " + (a + b));
        System.out.println("a - b = " + ____);
        System.out.println("a * b = " + ____);
        System.out.println("a / b = " + ____);  // Что будет?
        System.out.println("a % b = " + ____);  // Остаток от деления

        // Как получить 3.4 при делении 17 на 5?
        System.out.println("a / b (дробный результат) = " + ____);
    }
}
```

### Задание 4.2: Инкремент и декремент

Предскажите результат, затем проверьте в jshell:

```java
int x = 5;
System.out.println(x++);  // Что выведет? ____
System.out.println(x);    // Что выведет? ____
System.out.println(++x);  // Что выведет? ____
System.out.println(x);    // Что выведет? ____
```

### Задание 4.3: Операторы сравнения и логические

Создайте файл `Comparison.java`:

```java
public class Comparison {
    public static void main(String[] args) {
        int age = 20;
        boolean hasLicense = true;

        // Заполните пропуски, чтобы получить true
        System.out.println(age ____ 18);           // age >= 18
        System.out.println(age ____ 25);           // age < 25
        System.out.println(age >= 18 ____ hasLicense);  // оба условия истинны

        // Может ли человек водить машину?
        boolean canDrive = (age >= 18) && hasLicense;
        System.out.println("Может водить: " + canDrive);
    }
}
```

### Задание 4.4: Побитовые операторы

Выполните в jshell:

```
jshell> int a = 5        // в двоичной: 0101
jshell> int b = 3        // в двоичной: 0011

jshell> a & b            // побитовое И
jshell> a | b            // побитовое ИЛИ
jshell> a ^ b            // побитовое исключающее ИЛИ

jshell> a << 1           // сдвиг влево (умножение на 2)
jshell> a >> 1           // сдвиг вправо (деление на 2)
```

**Задание:** Переведите числа в двоичную систему и объясните результаты.

---

## Часть 5: Строки и сравнение объектов

### Задание 5.1: == vs .equals()

Создайте файл `StringComparison.java`:

```java
public class StringComparison {
    public static void main(String[] args) {
        String s1 = "Hello";
        String s2 = "Hello";
        String s3 = new String("Hello");
        String s4 = new String("Hello");

        System.out.println("s1 == s2: " + (s1 == s2));
        System.out.println("s1 == s3: " + (s1 == s3));
        System.out.println("s3 == s4: " + (s3 == s4));

        System.out.println("s1.equals(s2): " + s1.equals(s2));
        System.out.println("s1.equals(s3): " + s1.equals(s3));
        System.out.println("s3.equals(s4): " + s3.equals(s4));
    }
}
```

**Вопросы:**
1. Почему `s1 == s2` возвращает `true`?
2. Почему `s3 == s4` возвращает `false`?
3. Какой метод нужно использовать для сравнения содержимого строк?

### Задание 5.2: String Pool

Нарисуйте схему памяти для следующего кода:

```java
String a = "Java";
String b = "Java";
String c = new String("Java");
```

Покажите, где находятся объекты в памяти (String Pool и Heap).

---

## Часть 6: Самостоятельная работа

### Задание 6.1: Калькулятор BMI

Напишите программу `BMICalculator.java`, которая:
1. Объявляет переменные для роста (в метрах) и веса (в кг)
2. Вычисляет индекс массы тела: BMI = вес / (рост * рост)
3. Выводит результат

```java
public class BMICalculator {
    public static void main(String[] args) {
        double weight = 70.0;  // кг
        double height = 1.75;  // метры

        // Вычислите BMI
        double bmi = ____;

        System.out.println("Вес: " + weight + " кг");
        System.out.println("Рост: " + height + " м");
        System.out.println("BMI: " + bmi);
    }
}
```

### Задание 6.2: Конвертер температуры

Напишите программу `TemperatureConverter.java`, которая:
1. Переводит температуру из Цельсия в Фаренгейт: F = C * 9/5 + 32
2. Переводит из Фаренгейта в Цельсий: C = (F - 32) * 5/9

```java
public class TemperatureConverter {
    public static void main(String[] args) {
        double celsius = 25.0;
        double fahrenheit = 77.0;

        // Конвертируйте и выведите результаты
        double celsiusToF = ____;
        double fahrenheitToC = ____;

        System.out.println(celsius + "°C = " + celsiusToF + "°F");
        System.out.println(fahrenheit + "°F = " + fahrenheitToC + "°C");
    }
}
```

### Задание 6.3: Обмен значений переменных

Напишите программу, которая меняет местами значения двух переменных **без использования третьей переменной** (используйте побитовые операции или арифметику):

```java
public class SwapValues {
    public static void main(String[] args) {
        int a = 10;
        int b = 25;

        System.out.println("До обмена: a = " + a + ", b = " + b);

        // Обменяйте значения без третьей переменной
        // ____
        // ____
        // ____

        System.out.println("После обмена: a = " + a + ", b = " + b);
    }
}
```

---

## Часть 7: Дополнительные задания

### Задание 7.1: Проверка чётности без условных операторов

Напишите выражение, которое возвращает `true`, если число чётное, используя только побитовые операции:

```java
int n = 42;
boolean isEven = ____; // используйте побитовое И
```

### Задание 7.2: Абсолютное значение без Math.abs()

Найдите способ получить абсолютное значение числа без использования `Math.abs()` и условных операторов:

```java
int n = -42;
int abs = ____; // только арифметика и побитовые операции
```

---

## Часть 8: Контрольные вопросы

Ответьте письменно:

1. Чем отличается JDK от JRE?
2. Что такое байт-код и зачем он нужен?
3. Какие 8 примитивных типов есть в Java?
4. Почему `0.1 + 0.2 != 0.3` в Java?
5. В чём разница между `++x` и `x++`?
6. Когда нужно использовать `.equals()` вместо `==`?
7. Что такое String Pool?
8. Что произойдёт при переполнении типа `int`?

---

## Результаты занятия

К концу занятия вы должны сдать:
1. Файлы `.java` со всеми выполненными заданиями
2. Ответы на контрольные вопросы
3. Заметки о результатах экспериментов в jshell

**Критерии оценки:**
- Все программы компилируются без ошибок
- Правильные результаты выполнения
- Ответы на контрольные вопросы демонстрируют понимание материала
