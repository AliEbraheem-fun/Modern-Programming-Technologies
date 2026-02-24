# Тест 3: Ветвление, Циклы и ООП (Лекция 3)

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

<!-- ===== РАЗДЕЛ 1: ВЕТВЛЕНИЕ (Вопросы 1–12) ===== -->

<div class="quiz-question" data-correct="2">
<h4>Вопрос 1. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
int x = 10;
if (x > 5)
    System.out.print("A");
    System.out.print("B");
```

<div class="quiz-option" data-index="0">A</div>
<div class="quiz-option" data-index="1">B</div>
<div class="quiz-option" data-index="2">AB</div>
<div class="quiz-option" data-index="3">Ошибка компиляции</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 2. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
int x = 5;
String result = (x > 3) ? "больше" : "меньше";
System.out.println(result);
```

<div class="quiz-option" data-index="0">меньше</div>
<div class="quiz-option" data-index="1">больше</div>
<div class="quiz-option" data-index="2">Ошибка компиляции</div>
<div class="quiz-option" data-index="3">5</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 3. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
int day = 2;
switch (day) {
    case 1:
        System.out.print("Пн");
    case 2:
        System.out.print("Вт");
    case 3:
        System.out.print("Ср");
        break;
    default:
        System.out.print("?");
}
```

<div class="quiz-option" data-index="0">Вт</div>
<div class="quiz-option" data-index="1">ПнВт</div>
<div class="quiz-option" data-index="2">ПнВтСр</div>
<div class="quiz-option" data-index="3">ВтСр</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 4. Какое главное преимущество стрелочного switch (Java 14+) перед классическим?</h4>
<div class="quiz-option" data-index="0">Отсутствие fall-through — не нужен break</div>
<div class="quiz-option" data-index="1">Он работает быстрее</div>
<div class="quiz-option" data-index="2">Он поддерживает больше типов данных</div>
<div class="quiz-option" data-index="3">Он может использоваться только как выражение</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 5. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
int x = 3;
String s = switch (x) {
    case 1 -> "один";
    case 2 -> "два";
    case 3 -> "три";
    default -> "другое";
};
System.out.println(s);
```

<div class="quiz-option" data-index="0">один</div>
<div class="quiz-option" data-index="1">другое</div>
<div class="quiz-option" data-index="2">три</div>
<div class="quiz-option" data-index="3">Ошибка компиляции</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 6. Для чего используется ключевое слово <code>yield</code> в switch-выражении?</h4>
<div class="quiz-option" data-index="0">Для прерывания выполнения switch</div>
<div class="quiz-option" data-index="1">Для возврата значения из блока кода в switch-выражении</div>
<div class="quiz-option" data-index="2">Для перехода к следующему case</div>
<div class="quiz-option" data-index="3">Для создания генератора</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 7. Какой тип данных НЕЛЬЗЯ использовать в switch?</h4>
<div class="quiz-option" data-index="0">String</div>
<div class="quiz-option" data-index="1">int</div>
<div class="quiz-option" data-index="2">enum</div>
<div class="quiz-option" data-index="3">long</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 8. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
int score = 85;
if (score >= 90) {
    System.out.print("A");
} else if (score >= 75) {
    System.out.print("B");
} else if (score >= 60) {
    System.out.print("C");
} else {
    System.out.print("F");
}
```

<div class="quiz-option" data-index="0">B</div>
<div class="quiz-option" data-index="1">A</div>
<div class="quiz-option" data-index="2">BC</div>
<div class="quiz-option" data-index="3">C</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 9. Что такое pattern matching в switch (Java 17+)?</h4>
<div class="quiz-option" data-index="0">Использование регулярных выражений в case</div>
<div class="quiz-option" data-index="1">Автоматическое сравнение строк по шаблону</div>
<div class="quiz-option" data-index="2">Возможность проверять тип объекта и сразу приводить его к нужному типу в case</div>
<div class="quiz-option" data-index="3">Сравнение объектов с помощью equals()</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 10. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
Object obj = "Привет";
String result = switch (obj) {
    case Integer i -> "Число: " + i;
    case String s -> "Строка: " + s;
    default -> "Неизвестно";
};
System.out.println(result);
```

<div class="quiz-option" data-index="0">Неизвестно</div>
<div class="quiz-option" data-index="1">Строка: Привет</div>
<div class="quiz-option" data-index="2">Число: Привет</div>
<div class="quiz-option" data-index="3">Ошибка компиляции</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 11. Для чего используется ключевое слово <code>when</code> (guard) в switch с pattern matching (Java 21+)?</h4>
<div class="quiz-option" data-index="0">Для замены default</div>
<div class="quiz-option" data-index="1">Для указания таймаута выполнения</div>
<div class="quiz-option" data-index="2">Для группировки нескольких case</div>
<div class="quiz-option" data-index="3">Для добавления дополнительного условия к паттерну</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 12. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
int x = 0;
if (x != 0) {
    if (10 / x > 1) {
        System.out.print("A");
    }
} else {
    System.out.print("B");
}
```

<div class="quiz-option" data-index="0">A</div>
<div class="quiz-option" data-index="1">ArithmeticException</div>
<div class="quiz-option" data-index="2">B</div>
<div class="quiz-option" data-index="3">Ничего не выведет</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 2: ЦИКЛЫ (Вопросы 13–21) ===== -->

<div class="quiz-question" data-correct="1">
<h4>Вопрос 13. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
int i = 5;
while (i > 0) {
    i -= 2;
}
System.out.println(i);
```

<div class="quiz-option" data-index="0">0</div>
<div class="quiz-option" data-index="1">-1</div>
<div class="quiz-option" data-index="2">1</div>
<div class="quiz-option" data-index="3">Бесконечный цикл</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 14. Чем цикл <code>do-while</code> отличается от <code>while</code>?</h4>
<div class="quiz-option" data-index="0">do-while выполняется быстрее</div>
<div class="quiz-option" data-index="1">do-while не поддерживает break</div>
<div class="quiz-option" data-index="2">do-while проверяет условие перед телом цикла</div>
<div class="quiz-option" data-index="3">do-while гарантирует выполнение тела хотя бы один раз</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 15. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
int x = 10;
do {
    System.out.print(x + " ");
    x += 10;
} while (x < 10);
```

<div class="quiz-option" data-index="0">10 </div>
<div class="quiz-option" data-index="1">Ничего не выведет</div>
<div class="quiz-option" data-index="2">10 20 </div>
<div class="quiz-option" data-index="3">Бесконечный цикл</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 16. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
int sum = 0;
for (int i = 1; i <= 5; i++) {
    if (i % 2 == 0) continue;
    sum += i;
}
System.out.println(sum);
```

<div class="quiz-option" data-index="0">15</div>
<div class="quiz-option" data-index="1">6</div>
<div class="quiz-option" data-index="2">9</div>
<div class="quiz-option" data-index="3">5</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 17. Какой цикл предназначен для перебора элементов массива или коллекции?</h4>
<div class="quiz-option" data-index="0">while</div>
<div class="quiz-option" data-index="1">for-each (расширенный for)</div>
<div class="quiz-option" data-index="2">do-while</div>
<div class="quiz-option" data-index="3">switch</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 18. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
for (int i = 0; i < 5; i++) {
    if (i == 3) break;
    System.out.print(i + " ");
}
```

<div class="quiz-option" data-index="0">0 1 2 </div>
<div class="quiz-option" data-index="1">0 1 2 3 </div>
<div class="quiz-option" data-index="2">0 1 2 4 </div>
<div class="quiz-option" data-index="3">0 1 2 3 4 </div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 19. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
outer:
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        if (j == 1) continue outer;
        System.out.print(i + "" + j + " ");
    }
}
```

<div class="quiz-option" data-index="0">00 01 10 11 20 21 </div>
<div class="quiz-option" data-index="1">00 01 10 11 20 21 22 </div>
<div class="quiz-option" data-index="2">00 10 20 </div>
<div class="quiz-option" data-index="3">00 01 02 10 11 12 20 21 22 </div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 20. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
outer:
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        if (i == 1 && j == 1) break outer;
        System.out.print(i + "" + j + " ");
    }
}
```

<div class="quiz-option" data-index="0">00 01 02 </div>
<div class="quiz-option" data-index="1">00 01 02 10 </div>
<div class="quiz-option" data-index="2">00 01 02 10 11 </div>
<div class="quiz-option" data-index="3">00 </div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 21. Из каких трёх частей состоит заголовок цикла <code>for</code>?</h4>
<div class="quiz-option" data-index="0">условие, тело, возврат</div>
<div class="quiz-option" data-index="1">объявление, вызов, очистка</div>
<div class="quiz-option" data-index="2">начало, проверка, перезапуск</div>
<div class="quiz-option" data-index="3">инициализация, условие, шаг (обновление)</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 3: ООП — Наследование (Вопросы 22–30) ===== -->

<div class="quiz-question" data-correct="0">
<h4>Вопрос 22. Какое ключевое слово используется для наследования класса в Java?</h4>
<div class="quiz-option" data-index="0">extends</div>
<div class="quiz-option" data-index="1">implements</div>
<div class="quiz-option" data-index="2">inherits</div>
<div class="quiz-option" data-index="3">super</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 23. Сколько классов может наследовать один класс в Java?</h4>
<div class="quiz-option" data-index="0">Неограниченное количество</div>
<div class="quiz-option" data-index="1">Два</div>
<div class="quiz-option" data-index="2">Только один (одиночное наследование)</div>
<div class="quiz-option" data-index="3">Три, если они в одном пакете</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 24. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
class Animal {
    Animal() { System.out.print("Animal "); }
}
class Dog extends Animal {
    Dog() { System.out.print("Dog "); }
}
new Dog();
```

<div class="quiz-option" data-index="0">Dog </div>
<div class="quiz-option" data-index="1">Animal Dog </div>
<div class="quiz-option" data-index="2">Dog Animal </div>
<div class="quiz-option" data-index="3">Ошибка компиляции</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 25. Для чего используется вызов <code>super()</code> в конструкторе подкласса?</h4>
<div class="quiz-option" data-index="0">Для вызова метода суперкласса</div>
<div class="quiz-option" data-index="1">Для обращения к полю суперкласса</div>
<div class="quiz-option" data-index="2">Для создания нового объекта суперкласса</div>
<div class="quiz-option" data-index="3">Для вызова конструктора суперкласса</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 26. Для чего используется вызов <code>this()</code> в конструкторе?</h4>
<div class="quiz-option" data-index="0">Для вызова метода текущего объекта</div>
<div class="quiz-option" data-index="1">Для создания нового объекта того же класса</div>
<div class="quiz-option" data-index="2">Для делегирования вызова другому конструктору того же класса</div>
<div class="quiz-option" data-index="3">Для обращения к статическому полю класса</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 27. Какое утверждение об абстрактных классах ВЕРНО?</h4>
<div class="quiz-option" data-index="0">Абстрактный класс может содержать только абстрактные методы</div>
<div class="quiz-option" data-index="1">Абстрактный класс может содержать как абстрактные, так и обычные методы</div>
<div class="quiz-option" data-index="2">Можно создать экземпляр абстрактного класса</div>
<div class="quiz-option" data-index="3">Абстрактный класс не может иметь конструктор</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 28. Чем интерфейс отличается от абстрактного класса?</h4>
<div class="quiz-option" data-index="0">Интерфейс не может содержать методы с реализацией</div>
<div class="quiz-option" data-index="1">Абстрактный класс можно инстанцировать, а интерфейс — нет</div>
<div class="quiz-option" data-index="2">Интерфейс не может содержать константы</div>
<div class="quiz-option" data-index="3">Класс может реализовать несколько интерфейсов, но наследовать только один класс</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 29. Как разрешить конфликт default-методов из двух интерфейсов?</h4>
<div class="quiz-option" data-index="0">Переопределить метод в классе и вызвать нужную версию через InterfaceName.super.method()</div>
<div class="quiz-option" data-index="1">Java автоматически выбирает метод первого интерфейса в списке implements</div>
<div class="quiz-option" data-index="2">Использовать аннотацию @Primary</div>
<div class="quiz-option" data-index="3">Это невозможно — будет ошибка времени выполнения</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 30. Где должен располагаться вызов <code>super()</code> или <code>this()</code> в конструкторе?</h4>
<div class="quiz-option" data-index="0">В любом месте конструктора</div>
<div class="quiz-option" data-index="1">В последней строке конструктора</div>
<div class="quiz-option" data-index="2">В первой строке конструктора</div>
<div class="quiz-option" data-index="3">После инициализации полей</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 4: ООП — final и sealed (Вопросы 31–35) ===== -->

<div class="quiz-question" data-correct="1">
<h4>Вопрос 31. Что означает ключевое слово <code>final</code> перед переменной?</h4>
<div class="quiz-option" data-index="0">Переменная будет удалена после использования</div>
<div class="quiz-option" data-index="1">Значение переменной нельзя изменить после присваивания</div>
<div class="quiz-option" data-index="2">Переменная доступна только в текущем методе</div>
<div class="quiz-option" data-index="3">Переменная будет автоматически инициализирована нулём</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 32. Что произойдёт при попытке наследовать <code>final</code> класс?</h4>
<div class="quiz-option" data-index="0">Наследование пройдёт успешно</div>
<div class="quiz-option" data-index="1">Будет предупреждение компилятора</div>
<div class="quiz-option" data-index="2">Будет ошибка времени выполнения</div>
<div class="quiz-option" data-index="3">Будет ошибка компиляции</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 33. Что делает ключевое слово <code>sealed</code> перед классом (Java 17+)?</h4>
<div class="quiz-option" data-index="0">Ограничивает список классов, которые могут наследовать данный класс (через permits)</div>
<div class="quiz-option" data-index="1">Запрещает наследование полностью, как final</div>
<div class="quiz-option" data-index="2">Делает все поля класса private</div>
<div class="quiz-option" data-index="3">Запрещает создание экземпляров класса</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 34. Какие модификаторы обязан иметь подкласс sealed-класса?</h4>
<div class="quiz-option" data-index="0">Только public или private</div>
<div class="quiz-option" data-index="1">abstract или static</div>
<div class="quiz-option" data-index="2">final, sealed или non-sealed</div>
<div class="quiz-option" data-index="3">Никаких специальных модификаторов не требуется</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 35. Почему в switch по sealed-классу можно обойтись без default?</h4>
<div class="quiz-option" data-index="0">Потому что sealed-класс не может быть null</div>
<div class="quiz-option" data-index="1">Потому что компилятор знает все возможные подклассы и может проверить полноту перебора</div>
<div class="quiz-option" data-index="2">Потому что default автоматически добавляется компилятором</div>
<div class="quiz-option" data-index="3">Это неверно — default всегда обязателен</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 5: ООП — Инкапсуляция (Вопросы 36–40) ===== -->

<div class="quiz-question" data-correct="2">
<h4>Вопрос 36. Какой модификатор доступа делает поле видимым для классов в том же пакете и для подклассов?</h4>
<div class="quiz-option" data-index="0">private</div>
<div class="quiz-option" data-index="1">public</div>
<div class="quiz-option" data-index="2">protected</div>
<div class="quiz-option" data-index="3">default (package-private)</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 37. Какой модификатор доступа имеет поле, если модификатор не указан явно?</h4>
<div class="quiz-option" data-index="0">package-private (доступ только внутри пакета)</div>
<div class="quiz-option" data-index="1">private</div>
<div class="quiz-option" data-index="2">protected</div>
<div class="quiz-option" data-index="3">public</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 38. Зачем используют getter и setter вместо прямого доступа к полям?</h4>
<div class="quiz-option" data-index="0">Для увеличения скорости работы программы</div>
<div class="quiz-option" data-index="1">Для уменьшения объёма кода</div>
<div class="quiz-option" data-index="2">Потому что Java не позволяет обращаться к полям напрямую</div>
<div class="quiz-option" data-index="3">Для инкапсуляции: контроль доступа и возможность добавить валидацию</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 39. Какой порядок модификаторов доступа от самого ограниченного к самому открытому?</h4>
<div class="quiz-option" data-index="0">public, protected, package-private, private</div>
<div class="quiz-option" data-index="1">private, package-private, protected, public</div>
<div class="quiz-option" data-index="2">private, protected, package-private, public</div>
<div class="quiz-option" data-index="3">package-private, private, protected, public</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 40. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
class Account {
    private int balance = 100;
    public void setBalance(int b) {
        if (b >= 0) balance = b;
    }
    public int getBalance() { return balance; }
}
Account acc = new Account();
acc.setBalance(-50);
System.out.println(acc.getBalance());
```

<div class="quiz-option" data-index="0">-50</div>
<div class="quiz-option" data-index="1">0</div>
<div class="quiz-option" data-index="2">100</div>
<div class="quiz-option" data-index="3">Ошибка компиляции</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 6: ООП — Полиморфизм (Вопросы 41–48) ===== -->

<div class="quiz-question" data-correct="1">
<h4>Вопрос 41. Что такое переопределение (overriding) метода?</h4>
<div class="quiz-option" data-index="0">Создание метода с тем же именем, но другими параметрами в том же классе</div>
<div class="quiz-option" data-index="1">Определение метода с такой же сигнатурой в подклассе, заменяющее реализацию суперкласса</div>
<div class="quiz-option" data-index="2">Вызов метода суперкласса из подкласса</div>
<div class="quiz-option" data-index="3">Создание нового метода в интерфейсе</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 42. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
class Animal {
    String speak() { return "..."; }
}
class Cat extends Animal {
    @Override
    String speak() { return "Мяу"; }
}
Animal a = new Cat();
System.out.println(a.speak());
```

<div class="quiz-option" data-index="0">...</div>
<div class="quiz-option" data-index="1">Ошибка компиляции</div>
<div class="quiz-option" data-index="2">null</div>
<div class="quiz-option" data-index="3">Мяу</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 43. Чем перегрузка (overloading) отличается от переопределения (overriding)?</h4>
<div class="quiz-option" data-index="0">Перегрузка — методы с одним именем, но разными параметрами в одном классе; переопределение — та же сигнатура в подклассе</div>
<div class="quiz-option" data-index="1">Перегрузка происходит в подклассе, а переопределение — в одном классе</div>
<div class="quiz-option" data-index="2">Перегрузка работает только со статическими методами</div>
<div class="quiz-option" data-index="3">Перегрузка и переопределение — это синонимы</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 44. Какое из правил переопределения метода ВЕРНО?</h4>
<div class="quiz-option" data-index="0">Можно сузить видимость метода (например, public -> private)</div>
<div class="quiz-option" data-index="1">Можно добавить новые проверяемые исключения</div>
<div class="quiz-option" data-index="2">Тип возвращаемого значения может быть ковариантным (более узким подтипом)</div>
<div class="quiz-option" data-index="3">Сигнатура метода может отличаться по количеству параметров</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 45. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
class Calc {
    int add(int a, int b) { return a + b; }
    double add(double a, double b) { return a + b; }
}
Calc c = new Calc();
System.out.println(c.add(2, 3));
System.out.println(c.add(2.5, 3.5));
```

<div class="quiz-option" data-index="0">5 и 5</div>
<div class="quiz-option" data-index="1">5 и 6.0</div>
<div class="quiz-option" data-index="2">5.0 и 6.0</div>
<div class="quiz-option" data-index="3">Ошибка компиляции</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 46. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
Object obj = "Текст";
if (obj instanceof String s) {
    System.out.println(s.length());
} else {
    System.out.println("Не строка");
}
```

<div class="quiz-option" data-index="0">Не строка</div>
<div class="quiz-option" data-index="1">Ошибка компиляции</div>
<div class="quiz-option" data-index="2">0</div>
<div class="quiz-option" data-index="3">5</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 47. Что произойдёт при выполнении следующего кода? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
Object obj = Integer.valueOf(42);
String s = (String) obj;
```

<div class="quiz-option" data-index="0">ClassCastException во время выполнения</div>
<div class="quiz-option" data-index="1">s будет равно "42"</div>
<div class="quiz-option" data-index="2">Ошибка компиляции</div>
<div class="quiz-option" data-index="3">s будет равно null</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 48. Какой вид приведения типов является безопасным и не требует явного оператора приведения?</h4>
<div class="quiz-option" data-index="0">Downcasting (приведение к подклассу)</div>
<div class="quiz-option" data-index="1">Приведение между несвязанными классами</div>
<div class="quiz-option" data-index="2">Upcasting (приведение к суперклассу)</div>
<div class="quiz-option" data-index="3">Приведение интерфейса к классу</div>
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
    'Вопрос 1': 'Без фигурных скобок if управляет только одной следующей строкой. System.out.print("B") выполнится всегда, поэтому результат — AB.',
    'Вопрос 2': 'Условие x > 3 истинно (5 > 3), поэтому тернарный оператор возвращает "больше".',
    'Вопрос 3': 'Выполнение начинается с case 2 и «проваливается» (fall-through) в case 3, где break останавливает. Результат: ВтСр.',
    'Вопрос 4': 'Стрелочный switch (->) не имеет fall-through, что устраняет частую ошибку с забытым break.',
    'Вопрос 5': 'x равно 3, поэтому switch-выражение возвращает "три". Стрелочный switch не требует break.',
    'Вопрос 6': 'yield используется в switch-выражении для возврата значения из блока кода (когда ветка содержит несколько строк).',
    'Вопрос 7': 'Тип long нельзя использовать в классическом switch (допустимы: byte, short, char, int, String, enum, а в pattern matching — Object).',
    'Вопрос 8': 'score = 85 попадает в ветку score >= 75 (первая истинная), остальные else-if не проверяются.',
    'Вопрос 9': 'Pattern matching в switch позволяет писать case Integer i или case String s, совмещая проверку типа и приведение.',
    'Вопрос 10': 'Объект obj имеет тип String, поэтому сработает ветка case String s, и s будет равно "Привет".',
    'Вопрос 11': 'Ключевое слово when (Java 21+) добавляет guard-условие к паттерну, например: case String s when s.length() > 5.',
    'Вопрос 12': 'Внешний if проверяет x != 0 (false), поэтому выполняется ветка else, которая выводит "B". Деления на ноль не происходит.',
    'Вопрос 13': 'i = 5 → 3 → 1 → -1. Когда i = -1, условие i > 0 ложно — цикл завершается, и выводится -1.',
    'Вопрос 14': 'В do-while тело выполняется до проверки условия, поэтому оно гарантированно выполнится хотя бы один раз.',
    'Вопрос 15': 'do-while выполняет тело (выводит 10), затем проверяет условие x < 10 (20 < 10 — false) и завершается.',
    'Вопрос 16': 'continue пропускает чётные числа (2, 4). Складываются только нечётные: 1 + 3 + 5 = 9.',
    'Вопрос 17': 'for-each (расширенный for) — специальный цикл для перебора массивов и коллекций: for (Type x : collection).',
    'Вопрос 18': 'Когда i == 3, break прерывает цикл. Выводятся значения 0, 1, 2.',
    'Вопрос 19': 'continue outer переходит к следующей итерации внешнего цикла. Для каждого i выводится только j=0: 00 10 20.',
    'Вопрос 20': 'break outer прерывает оба цикла при i=1, j=1. До этого напечатались: 00 01 02 (весь внутренний цикл при i=0) и 10 (j=0 при i=1).',
    'Вопрос 21': 'Заголовок for состоит из трёх частей: инициализация (int i = 0), условие (i < n), шаг (i++).',
    'Вопрос 22': 'Ключевое слово extends используется для наследования класса: class Child extends Parent.',
    'Вопрос 23': 'В Java поддерживается только одиночное наследование классов. Множественное наследование возможно только через интерфейсы.',
    'Вопрос 24': 'Конструктор суперкласса всегда вызывается первым. Сначала выполнится конструктор Animal, затем Dog.',
    'Вопрос 25': 'super() вызывает конструктор суперкласса. Если вызов не написан явно, компилятор вставляет super() без аргументов.',
    'Вопрос 26': 'this() делегирует вызов другому конструктору того же класса, позволяя избежать дублирования кода инициализации.',
    'Вопрос 27': 'Абстрактный класс может содержать обычные методы с реализацией и абстрактные методы без реализации.',
    'Вопрос 28': 'Класс может implements несколько интерфейсов, но extends только один класс — это ключевое отличие.',
    'Вопрос 29': 'При конфликте default-методов нужно переопределить метод и явно вызвать нужный через InterfaceName.super.method().',
    'Вопрос 30': 'Вызов super() или this() должен быть первой инструкцией в конструкторе, иначе будет ошибка компиляции.',
    'Вопрос 31': 'final переменная (константа) — её значение можно присвоить только один раз. Повторное присваивание приведёт к ошибке компиляции.',
    'Вопрос 32': 'final класс нельзя наследовать. Попытка extends от final класса приведёт к ошибке компиляции. Пример: класс String является final.',
    'Вопрос 33': 'sealed класс разрешает наследование только перечисленным в permits классам, обеспечивая контролируемую иерархию.',
    'Вопрос 34': 'Каждый подкласс sealed-класса обязан быть final (нельзя наследовать), sealed (контролируемое наследование) или non-sealed (открыт для наследования).',
    'Вопрос 35': 'Компилятор знает полный список подклассов sealed-класса, поэтому может убедиться, что switch покрывает все варианты без default.',
    'Вопрос 36': 'protected даёт доступ классам того же пакета И подклассам (даже в других пакетах). Package-private — только в том же пакете.',
    'Вопрос 37': 'Если модификатор не указан, поле имеет package-private доступ — видимо только для классов в том же пакете.',
    'Вопрос 38': 'Getter/setter позволяют контролировать доступ к данным, добавлять валидацию и изменять внутреннюю реализацию без изменения внешнего API.',
    'Вопрос 39': 'От самого закрытого к самому открытому: private → package-private → protected → public.',
    'Вопрос 40': 'Сеттер содержит валидацию: if (b >= 0). Значение -50 не пройдёт проверку, поэтому balance останется 100.',
    'Вопрос 41': 'Переопределение — подкласс предоставляет свою реализацию метода с точно такой же сигнатурой, как в суперклассе.',
    'Вопрос 42': 'Переменная a типа Animal ссылается на объект Cat. Вызывается переопределённый метод speak() класса Cat — это и есть полиморфизм.',
    'Вопрос 43': 'Перегрузка (overloading) — compile-time полиморфизм (разные параметры), переопределение (overriding) — runtime полиморфизм (та же сигнатура в подклассе).',
    'Вопрос 44': 'Ковариантный тип возврата: переопределённый метод может возвращать более узкий подтип. Нельзя сужать видимость и добавлять checked-исключения.',
    'Вопрос 45': 'Перегрузка: add(2,3) вызывает int-версию (результат 5), add(2.5,3.5) вызывает double-версию (результат 6.0).',
    'Вопрос 46': 'Pattern matching instanceof (Java 16+): obj проверяется на String, и сразу создаётся переменная s. "Текст".length() = 5.',
    'Вопрос 47': 'Компилятор допускает приведение Object к String, но Integer не является String, поэтому в runtime выбрасывается ClassCastException.',
    'Вопрос 48': 'Upcasting (приведение к суперклассу) всегда безопасно и выполняется неявно. Downcasting требует явного оператора и может вызвать ClassCastException.'
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