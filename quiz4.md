# Тест 4: Вложенные классы, Обобщения, Исключения и Отладка (Лекция 4)

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

<!-- ===== РАЗДЕЛ 1: ВЛОЖЕННЫЕ КЛАССЫ (Вопросы 1–9) ===== -->

<div class="quiz-question" data-correct="1">
<h4>Вопрос 1. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
class Outer {
    int x = 10;
    class Inner {
        int x = 20;
        void show() {
            System.out.println(Outer.this.x + " " + this.x);
        }
    }
}
Outer outer = new Outer();
Outer.Inner inner = outer.new Inner();
inner.show();
```

<div class="quiz-option" data-index="0">20 10</div>
<div class="quiz-option" data-index="1">10 20</div>
<div class="quiz-option" data-index="2">10 10</div>
<div class="quiz-option" data-index="3">Ошибка компиляции</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 2. Как правильно создать экземпляр нестатического внутреннего класса Inner, если он объявлен внутри класса Outer?</h4>

<div class="quiz-option" data-index="0">Inner i = new Inner();</div>
<div class="quiz-option" data-index="1">Outer.Inner i = new Outer.Inner();</div>
<div class="quiz-option" data-index="2">Inner i = Outer.new Inner();</div>
<div class="quiz-option" data-index="3">Outer o = new Outer(); Outer.Inner i = o.new Inner();</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 3. Какое ограничение имеет нестатический внутренний класс (inner class)?</h4>

<div class="quiz-option" data-index="0">Не может существовать без экземпляра внешнего класса</div>
<div class="quiz-option" data-index="1">Не имеет доступа к private полям внешнего класса</div>
<div class="quiz-option" data-index="2">Может существовать без экземпляра внешнего класса</div>
<div class="quiz-option" data-index="3">Не может реализовывать интерфейсы</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 4. Как правильно создать экземпляр статического вложенного класса StaticNested, объявленного внутри класса Outer?</h4>

<div class="quiz-option" data-index="0">Outer o = new Outer(); Outer.StaticNested sn = o.new StaticNested();</div>
<div class="quiz-option" data-index="1">StaticNested sn = new StaticNested();</div>
<div class="quiz-option" data-index="2">Outer.StaticNested sn = new Outer.StaticNested();</div>
<div class="quiz-option" data-index="3">Outer.StaticNested sn = Outer.new StaticNested();</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 5. К каким членам внешнего класса имеет доступ статический вложенный класс?</h4>

<div class="quiz-option" data-index="0">Ко всем членам, включая private нестатические</div>
<div class="quiz-option" data-index="1">Только к статическим членам внешнего класса</div>
<div class="quiz-option" data-index="2">Только к public членам внешнего класса</div>
<div class="quiz-option" data-index="3">Ни к каким — он полностью изолирован</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 6. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
class Outer {
    private static int count = 42;
    static class Nested {
        void printCount() {
            System.out.println(count);
        }
    }
}
new Outer.Nested().printCount();
```

<div class="quiz-option" data-index="0">Ошибка компиляции: нет доступа к private полю</div>
<div class="quiz-option" data-index="1">Ошибка компиляции: нельзя создать Nested без Outer</div>
<div class="quiz-option" data-index="2">0</div>
<div class="quiz-option" data-index="3">42</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 7. Почему паттерн Builder часто реализуется как статический вложенный класс?</h4>

<div class="quiz-option" data-index="0">Потому что Builder не нуждается в экземпляре внешнего класса — он сам создаёт этот экземпляр</div>
<div class="quiz-option" data-index="1">Потому что только статический класс может иметь конструктор</div>
<div class="quiz-option" data-index="2">Потому что статический класс автоматически реализует Serializable</div>
<div class="quiz-option" data-index="3">Потому что нестатический класс не может возвращать объекты</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 8. Что произойдёт при компиляции данного кода? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
class Outer {
    int value = 5;
    static class Nested {
        void print() {
            System.out.println(value);
        }
    }
}
```

<div class="quiz-option" data-index="0">Выведет 5</div>
<div class="quiz-option" data-index="1">Выведет 0</div>
<div class="quiz-option" data-index="2">Ошибка компиляции: статический класс не может обращаться к нестатическому полю</div>
<div class="quiz-option" data-index="3">Ошибка выполнения</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 9. Какой из четырёх типов вложенных классов НЕ привязан к экземпляру внешнего класса?</h4>

<div class="quiz-option" data-index="0">Статический вложенный класс (static nested class)</div>
<div class="quiz-option" data-index="1">Нестатический внутренний класс (inner class)</div>
<div class="quiz-option" data-index="2">Локальный класс (local class)</div>
<div class="quiz-option" data-index="3">Анонимный класс (anonymous class)</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 2: ВЛОЖЕННЫЕ ИНТЕРФЕЙСЫ (Вопросы 10–13) ===== -->

<div class="quiz-question" data-correct="1">
<h4>Вопрос 10. Какой модификатор доступа может иметь интерфейс, объявленный внутри класса?</h4>

<div class="quiz-option" data-index="0">Только public</div>
<div class="quiz-option" data-index="1">Любой: public, protected, package-private или private</div>
<div class="quiz-option" data-index="2">Только public или private</div>
<div class="quiz-option" data-index="3">Только public или protected</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 11. Какие неявные модификаторы получает интерфейс, объявленный внутри другого интерфейса?</h4>

<div class="quiz-option" data-index="0">private abstract</div>
<div class="quiz-option" data-index="1">protected abstract</div>
<div class="quiz-option" data-index="2">public static</div>
<div class="quiz-option" data-index="3">public abstract</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 12. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
class Container {
    interface Printable {
        void print();
    }
}
class MyPrinter implements Container.Printable {
    public void print() { System.out.println("Работает!"); }
}
new MyPrinter().print();
```

<div class="quiz-option" data-index="0">Ошибка компиляции: нельзя реализовать вложенный интерфейс</div>
<div class="quiz-option" data-index="1">Ошибка компиляции: интерфейс Printable не виден</div>
<div class="quiz-option" data-index="2">Ошибка выполнения</div>
<div class="quiz-option" data-index="3">Работает!</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 13. Может ли внешний класс сам реализовать свой вложенный интерфейс?</h4>

<div class="quiz-option" data-index="0">Да, внешний класс может реализовать свой собственный вложенный интерфейс</div>
<div class="quiz-option" data-index="1">Нет, это вызовет циклическую зависимость</div>
<div class="quiz-option" data-index="2">Только если интерфейс объявлен как static</div>
<div class="quiz-option" data-index="3">Только если интерфейс объявлен как public</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 3: ОБОБЩЕНИЯ / GENERICS (Вопросы 14–29) ===== -->

<div class="quiz-question" data-correct="2">
<h4>Вопрос 14. Какую основную проблему решают обобщения (generics) в Java?</h4>

<div class="quiz-option" data-index="0">Ускоряют выполнение программы за счёт специализации кода</div>
<div class="quiz-option" data-index="1">Позволяют использовать примитивные типы в коллекциях</div>
<div class="quiz-option" data-index="2">Обеспечивают типобезопасность на этапе компиляции и устраняют необходимость явного приведения типов</div>
<div class="quiz-option" data-index="3">Автоматически сериализуют объекты в JSON</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 15. Какие общепринятые имена параметров типов используются в Java?</h4>

<div class="quiz-option" data-index="0">A — Any, B — Base, C — Class, D — Data</div>
<div class="quiz-option" data-index="1">T — Type, E — Element, K — Key, V — Value, N — Number, R — Result</div>
<div class="quiz-option" data-index="2">X — eXtended, Y — tYpe, Z — siZe</div>
<div class="quiz-option" data-index="3">G — Generic, P — Parameter, S — Specific</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 16. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
class Box<T> {
    private T value;
    Box(T value) { this.value = value; }
    T get() { return value; }
}
Box<String> box = new Box<>("Hello");
System.out.println(box.get().length());
```

<div class="quiz-option" data-index="0">Ошибка компиляции</div>
<div class="quiz-option" data-index="1">Hello</div>
<div class="quiz-option" data-index="2">0</div>
<div class="quiz-option" data-index="3">5</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 17. Что означает запись T extends Number в объявлении обобщённого класса?</h4>

<div class="quiz-option" data-index="0">T может быть только Number или его подклассом (Integer, Double и т.д.)</div>
<div class="quiz-option" data-index="1">T должен быть точно Number, без подклассов</div>
<div class="quiz-option" data-index="2">T может быть любым классом, который содержит число</div>
<div class="quiz-option" data-index="3">T наследует Number и получает новые методы</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 18. Какая запись корректна для задания множественных границ типового параметра?</h4>

<div class="quiz-option" data-index="0">T extends Comparable&lt;T&gt;, Cloneable</div>
<div class="quiz-option" data-index="1">T implements Comparable&lt;T&gt; & Cloneable</div>
<div class="quiz-option" data-index="2">T extends Comparable&lt;T&gt; & Cloneable</div>
<div class="quiz-option" data-index="3">T super Comparable&lt;T&gt; & Cloneable</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 19. Как объявить обобщённый метод, принимающий массив элементов типа T и возвращающий список?</h4>

<div class="quiz-option" data-index="0">List&lt;T&gt; toList(T[] arr) — параметр T определён на уровне класса</div>
<div class="quiz-option" data-index="1">&lt;T&gt; List&lt;T&gt; toList(T[] arr) — параметр T объявлен перед возвращаемым типом</div>
<div class="quiz-option" data-index="2">List&lt;T&gt; &lt;T&gt; toList(T[] arr) — параметр T после возвращаемого типа</div>
<div class="quiz-option" data-index="3">generic T List&lt;T&gt; toList(T[] arr)</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 20. Что происходит с обобщёнными типами в процессе стирания типов (type erasure)?</h4>

<div class="quiz-option" data-index="0">Параметры типов сохраняются в байткоде для проверки во время выполнения</div>
<div class="quiz-option" data-index="1">Типы заменяются на void</div>
<div class="quiz-option" data-index="2">Компилятор создаёт отдельный класс для каждого параметра типа</div>
<div class="quiz-option" data-index="3">Параметры типов существуют только при компиляции и заменяются на Object (или на границу, если указана) в байткоде</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 21. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
List<String> strings = new ArrayList<>();
List<Integer> ints = new ArrayList<>();
System.out.println(strings.getClass() == ints.getClass());
```

<div class="quiz-option" data-index="0">true</div>
<div class="quiz-option" data-index="1">false</div>
<div class="quiz-option" data-index="2">Ошибка компиляции</div>
<div class="quiz-option" data-index="3">Ошибка выполнения</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 22. Какое из следующих действий НЕВОЗМОЖНО из-за стирания типов?</h4>

<div class="quiz-option" data-index="0">Объявить переменную типа T</div>
<div class="quiz-option" data-index="1">Привести объект к типу T</div>
<div class="quiz-option" data-index="2">Создать экземпляр new T() или массив new T[]</div>
<div class="quiz-option" data-index="3">Передать объект типа T как параметр метода</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 23. Какой класс корректно наследует обобщённый Box&lt;T&gt; с фиксированным типом String?</h4>

```java
class Box<T> { T value; }
```

<div class="quiz-option" data-index="0">class StringBox&lt;String&gt; extends Box&lt;String&gt; {}</div>
<div class="quiz-option" data-index="1">class StringBox extends Box&lt;String&gt; {}</div>
<div class="quiz-option" data-index="2">class StringBox extends Box&lt;T&gt; {}</div>
<div class="quiz-option" data-index="3">class StringBox implements Box&lt;String&gt; {}</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 24. Что означает подстановочный знак ? (wildcard) в обобщениях?</h4>

<div class="quiz-option" data-index="0">Означает тип Object</div>
<div class="quiz-option" data-index="1">Означает отсутствие типа</div>
<div class="quiz-option" data-index="2">Означает ошибку в типе</div>
<div class="quiz-option" data-index="3">Означает неизвестный тип — может быть любым</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 25. Какой параметр метода позволит принять List&lt;Integer&gt;, List&lt;Double&gt; и List&lt;Number&gt;?</h4>

<div class="quiz-option" data-index="0">List&lt;? extends Number&gt;</div>
<div class="quiz-option" data-index="1">List&lt;? super Number&gt;</div>
<div class="quiz-option" data-index="2">List&lt;Number&gt;</div>
<div class="quiz-option" data-index="3">List&lt;Object&gt;</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 26. Что означает правило PECS (Producer Extends, Consumer Super)?</h4>

<div class="quiz-option" data-index="0">Продюсер должен наследовать Consumer, а Consumer — расширять Producer</div>
<div class="quiz-option" data-index="1">extends используется для записи, super — для чтения</div>
<div class="quiz-option" data-index="2">Если из коллекции только читаем (producer) — используем ? extends T; если только записываем (consumer) — используем ? super T</div>
<div class="quiz-option" data-index="3">Producer и Consumer — стандартные интерфейсы Java</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 27. Почему в сигнатуре Collections.copy(List&lt;? super T&gt; dest, List&lt;? extends T&gt; src) используются именно такие wildcards?</h4>

<div class="quiz-option" data-index="0">Это просто конвенция, можно использовать и наоборот</div>
<div class="quiz-option" data-index="1">src — производитель данных (читаем элементы, extends), dest — потребитель данных (записываем элементы, super)</div>
<div class="quiz-option" data-index="2">super всегда используется для источника, extends — для назначения</div>
<div class="quiz-option" data-index="3">Оба параметра можно заменить на List&lt;T&gt; без потери функциональности</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 28. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
class Pair<K, V> {
    K key; V value;
    Pair(K key, V value) { this.key = key; this.value = value; }
}
Pair<String, Integer> p = new Pair<>("age", 25);
System.out.println(p.key + "=" + p.value);
```

<div class="quiz-option" data-index="0">Ошибка компиляции</div>
<div class="quiz-option" data-index="1">age25</div>
<div class="quiz-option" data-index="2">null=null</div>
<div class="quiz-option" data-index="3">age=25</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 29. Какое утверждение верно относительно обобщённых интерфейсов?</h4>

```java
interface Transformer<T, R> {
    R transform(T input);
}
```

<div class="quiz-option" data-index="0">Класс может реализовать интерфейс с конкретными типами: class StringToInt implements Transformer&lt;String, Integer&gt;</div>
<div class="quiz-option" data-index="1">Интерфейс не может иметь более одного параметра типа</div>
<div class="quiz-option" data-index="2">Реализующий класс обязан быть тоже обобщённым</div>
<div class="quiz-option" data-index="3">Обобщённые интерфейсы нельзя использовать с анонимными классами</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 4: ИСКЛЮЧЕНИЯ (Вопросы 30–45) ===== -->

<div class="quiz-question" data-correct="1">
<h4>Вопрос 30. Какая иерархия исключений верна в Java?</h4>

<div class="quiz-option" data-index="0">Object → Exception → Throwable → Error</div>
<div class="quiz-option" data-index="1">Throwable → Error и Exception; Exception → RuntimeException</div>
<div class="quiz-option" data-index="2">Exception → Throwable → Error → RuntimeException</div>
<div class="quiz-option" data-index="3">Throwable → RuntimeException → Exception → Error</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 31. Какое исключение является проверяемым (checked)?</h4>

<div class="quiz-option" data-index="0">NullPointerException</div>
<div class="quiz-option" data-index="1">ArrayIndexOutOfBoundsException</div>
<div class="quiz-option" data-index="2">IOException</div>
<div class="quiz-option" data-index="3">StackOverflowError</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 32. Чем checked-исключения отличаются от unchecked?</h4>

<div class="quiz-option" data-index="0">Checked-исключения должны быть обработаны (try-catch) или объявлены (throws) — иначе код не скомпилируется</div>
<div class="quiz-option" data-index="1">Unchecked-исключения нельзя ловить в catch-блоке</div>
<div class="quiz-option" data-index="2">Checked-исключения возникают только во время выполнения</div>
<div class="quiz-option" data-index="3">Unchecked-исключения наследуют класс Exception напрямую</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 33. К какой категории относится StackOverflowError?</h4>

<div class="quiz-option" data-index="0">Checked exception</div>
<div class="quiz-option" data-index="1">Unchecked exception (RuntimeException)</div>
<div class="quiz-option" data-index="2">Обычная ошибка компиляции</div>
<div class="quiz-option" data-index="3">Error — серьёзная ошибка JVM, которую обычно не следует обрабатывать</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 34. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
try {
    System.out.print("A");
    int x = 1 / 0;
    System.out.print("B");
} catch (ArithmeticException e) {
    System.out.print("C");
} finally {
    System.out.print("D");
}
```

<div class="quiz-option" data-index="0">ABCD</div>
<div class="quiz-option" data-index="1">ACD</div>
<div class="quiz-option" data-index="2">AD</div>
<div class="quiz-option" data-index="3">ACD, но D не выполнится если catch бросит исключение</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 35. Почему порядок catch-блоков имеет значение?</h4>

<div class="quiz-option" data-index="0">Потому что выполняются все подходящие catch-блоки последовательно</div>
<div class="quiz-option" data-index="1">Порядок не имеет значения — JVM сама выбирает наиболее подходящий</div>
<div class="quiz-option" data-index="2">Более конкретные исключения должны стоять раньше, иначе ошибка компиляции: суперкласс перехватит всё до подклассов</div>
<div class="quiz-option" data-index="3">Первый catch всегда обрабатывает все исключения</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 36. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
try {
    System.out.print("1");
    throw new RuntimeException();
} catch (RuntimeException e) {
    System.out.print("2");
} finally {
    System.out.print("3");
}
System.out.print("4");
```

<div class="quiz-option" data-index="0">1234</div>
<div class="quiz-option" data-index="1">123</div>
<div class="quiz-option" data-index="2">12</div>
<div class="quiz-option" data-index="3">134</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 37. Что позволяет конструкция multi-catch, появившаяся в Java 7?</h4>

```java
catch (IOException | SQLException e) { ... }
```

<div class="quiz-option" data-index="0">Ловить исключения, которые являются наследниками друг друга</div>
<div class="quiz-option" data-index="1">Обрабатывать каждое исключение отдельным блоком кода</div>
<div class="quiz-option" data-index="2">Ловить только unchecked-исключения</div>
<div class="quiz-option" data-index="3">Ловить несколько несвязанных типов исключений в одном catch-блоке с общей обработкой</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 38. Какой метод класса Throwable возвращает текстовое описание исключения?</h4>

<div class="quiz-option" data-index="0">toString()</div>
<div class="quiz-option" data-index="1">printStackTrace()</div>
<div class="quiz-option" data-index="2">getMessage()</div>
<div class="quiz-option" data-index="3">getDescription()</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 39. В чём разница между ключевыми словами throw и throws?</h4>

<div class="quiz-option" data-index="0">throw объявляет исключения метода, throws бросает исключение</div>
<div class="quiz-option" data-index="1">throw бросает конкретное исключение, throws объявляет в сигнатуре метода, какие checked-исключения он может выбросить</div>
<div class="quiz-option" data-index="2">throw используется в catch, throws — в try</div>
<div class="quiz-option" data-index="3">Разницы нет, это синонимы</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 40. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
try {
    throw new Exception("Тест");
} catch (Exception e) {
    System.out.println(e.getMessage());
}
```

<div class="quiz-option" data-index="0">Тест</div>
<div class="quiz-option" data-index="1">Exception: Тест</div>
<div class="quiz-option" data-index="2">java.lang.Exception: Тест</div>
<div class="quiz-option" data-index="3">null</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 41. Как правильно создать собственное checked-исключение?</h4>

<div class="quiz-option" data-index="0">class MyException extends RuntimeException {}</div>
<div class="quiz-option" data-index="1">class MyException extends Error {}</div>
<div class="quiz-option" data-index="2">class MyException implements Exception {}</div>
<div class="quiz-option" data-index="3">class MyException extends Exception {}</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 42. Что такое try-with-resources и какой интерфейс должен реализовать ресурс?</h4>

<div class="quiz-option" data-index="0">Конструкция для автоматического открытия ресурсов; интерфейс Openable</div>
<div class="quiz-option" data-index="1">Конструкция для автоматического закрытия ресурсов; интерфейс AutoCloseable</div>
<div class="quiz-option" data-index="2">Конструкция для кеширования ресурсов; интерфейс Cacheable</div>
<div class="quiz-option" data-index="3">Конструкция для логирования ресурсов; интерфейс Loggable</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 43. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
class MyRes implements AutoCloseable {
    public void close() { System.out.print("closed "); }
}
try (MyRes r = new MyRes()) {
    System.out.print("used ");
}
```

<div class="quiz-option" data-index="0">used closed </div>
<div class="quiz-option" data-index="1">closed used </div>
<div class="quiz-option" data-index="2">used </div>
<div class="quiz-option" data-index="3">Ошибка компиляции</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 44. Что такое цепочка исключений (exception chaining)?</h4>

<div class="quiz-option" data-index="0">Перехват нескольких исключений подряд в отдельных try-catch блоках</div>
<div class="quiz-option" data-index="1">Вызов нескольких throw подряд в одном методе</div>
<div class="quiz-option" data-index="2">Использование multi-catch для нескольких типов</div>
<div class="quiz-option" data-index="3">Оборачивание исходного исключения (cause) в новое через throw new HighLevel("msg", cause)</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 45. Какая практика обработки исключений считается ПЛОХОЙ?</h4>

```java
// Вариант A
try { riskyMethod(); }
catch (Exception e) { /* пусто */ }

// Вариант B
try { riskyMethod(); }
catch (SpecificException e) { log.error("Ошибка", e); throw e; }
```

<div class="quiz-option" data-index="0">Вариант B — нельзя бросать перехваченное исключение повторно</div>
<div class="quiz-option" data-index="1">Вариант A — перехват слишком широкого Exception и «проглатывание» исключения без обработки</div>
<div class="quiz-option" data-index="2">Оба варианта являются плохой практикой</div>
<div class="quiz-option" data-index="3">Оба варианта являются хорошей практикой</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 5: ОТЛАДКА (Вопросы 46–52) ===== -->

<div class="quiz-question" data-correct="2">
<h4>Вопрос 46. Чем точка останова (breakpoint) принципиально удобнее вызовов println() при поиске ошибки?</h4>

<div class="quiz-option" data-index="0">Ускоряет выполнение программы за счёт исключения лишних вычислений</div>
<div class="quiz-option" data-index="1">Автоматически записывает весь вывод программы в файл на диске</div>
<div class="quiz-option" data-index="2">Останавливает программу и показывает сразу все переменные текущего кадра, не заставляя заранее угадывать, что печатать</div>
<div class="quiz-option" data-index="3">Позволяет запускать программу без установки JDK</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 47. В чём отличие условной точки останова (Condition) от обычной точки останова (line breakpoint)?</h4>

<div class="quiz-option" data-index="0">Условная останавливает программу только тогда, когда истинно заданное в поле Condition выражение, а обычная — при каждом подходе к строке</div>
<div class="quiz-option" data-index="1">Условная точка останова работает только с примитивными числовыми переменными</div>
<div class="quiz-option" data-index="2">Обычная точка останова доступна только в VS Code, а условная — только в IntelliJ IDEA</div>
<div class="quiz-option" data-index="3">Условную точку останова нельзя снять после установки</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 48. Какая команда пошагового выполнения заходит внутрь вызываемого метода, а не выполняет его целиком?</h4>

<div class="quiz-option" data-index="0">Step Over</div>
<div class="quiz-option" data-index="1">Step Into</div>
<div class="quiz-option" data-index="2">Step Out</div>
<div class="quiz-option" data-index="3">Resume</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 49. Чем Step Over отличается от Step Into?</h4>

<div class="quiz-option" data-index="0">Step Over доступен только для статических методов</div>
<div class="quiz-option" data-index="1">Step Into пропускает выполнение цикла целиком</div>
<div class="quiz-option" data-index="2">Step Over останавливает программу только на исключениях</div>
<div class="quiz-option" data-index="3">Step Over выполняет вызываемый метод целиком, не показывая происходящее внутри, а Step Into заходит внутрь этого метода</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 50. В примере с AverageCalculator из лекции окно Variables в точке останова на return sum / count; показало sum = 60.0 и count = 4, хотя корректных чисел в списке было три. О чём это говорит?</h4>

<div class="quiz-option" data-index="0">Счётчик count увеличивается для каждой строки списка, включая ту, что не разобралась в число</div>
<div class="quiz-option" data-index="1">Переменная sum вычислена неверно и должна быть равна 30.0</div>
<div class="quiz-option" data-index="2">Список rows хранит дублирующиеся элементы</div>
<div class="quiz-option" data-index="3">Метод Double.parseDouble бросает исключение, которое отладчик не может перехватить</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 51. Для чего используется окно Evaluate Expression в отладчике?</h4>

<div class="quiz-option" data-index="0">Чтобы посмотреть историю всех прошлых значений выбранной переменной</div>
<div class="quiz-option" data-index="1">Чтобы автоматически исправить найденную ошибку в коде</div>
<div class="quiz-option" data-index="2">Чтобы разово вычислить произвольное Java-выражение, включая вызовы методов, в контексте уже остановленной программы</div>
<div class="quiz-option" data-index="3">Чтобы заменить точки останова логированием без перезапуска IDE</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 52. Что показывает окно Call Stack (Frames) в отладчике?</h4>

<div class="quiz-option" data-index="0">Список всех точек останова, расставленных в проекте</div>
<div class="quiz-option" data-index="1">Цепочку кадров вызовов методов — от текущей точки остановки до main, то есть кто кого вызвал</div>
<div class="quiz-option" data-index="2">Список переменных, изменённых вручную через F2 с начала сеанса отладки</div>
<div class="quiz-option" data-index="3">Список исключений, которые метод объявляет в throws</div>
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
    'Вопрос 1': 'Outer.this.x обращается к полю внешнего класса (10), а this.x — к полю внутреннего класса (20). Синтаксис Outer.this позволяет различать одноимённые члены.',
    'Вопрос 2': 'Нестатический внутренний класс привязан к экземпляру внешнего класса, поэтому сначала создаётся Outer, а затем через него — Inner: outer.new Inner().',
    'Вопрос 3': 'Нестатический внутренний класс хранит неявную ссылку на экземпляр внешнего класса и не может существовать без него. Для создания объекта Inner нужен объект Outer: outer.new Inner().',
    'Вопрос 4': 'Статический вложенный класс не привязан к экземпляру внешнего класса. Он создаётся через имя внешнего класса: new Outer.StaticNested().',
    'Вопрос 5': 'Статический вложенный класс не имеет ссылки на экземпляр внешнего класса, поэтому может обращаться только к статическим членам Outer, включая private static.',
    'Вопрос 6': 'Статический вложенный класс имеет доступ к private static полям внешнего класса. Поэтому Nested видит count = 42 и выводит его.',
    'Вопрос 7': 'Builder создаёт экземпляр внешнего класса, а не наоборот. Он не нуждается в готовом экземпляре Outer, поэтому логично делать его статическим вложенным классом.',
    'Вопрос 8': 'Статический вложенный класс Nested не имеет ссылки на экземпляр Outer, поэтому обращение к нестатическому полю value невозможно — ошибка компиляции.',
    'Вопрос 9': 'Статический вложенный класс — единственный тип вложенного класса, который не привязан к экземпляру внешнего класса. Inner, local и anonymous классы требуют экземпляр.',
    'Вопрос 10': 'Интерфейс, объявленный внутри класса, может иметь любой модификатор доступа: public, protected, package-private или private.',
    'Вопрос 11': 'Интерфейс, объявленный внутри другого интерфейса, неявно является public static. Это логично, так как все члены интерфейса по умолчанию public.',
    'Вопрос 12': 'Вложенный интерфейс Container.Printable неявно является static и может быть реализован любым классом через implements Container.Printable.',
    'Вопрос 13': 'Да, класс может реализовать собственный вложенный интерфейс. Это не вызывает циклической зависимости и является допустимым паттерном.',
    'Вопрос 14': 'Generics обеспечивают типобезопасность на этапе компиляции: ошибки типов обнаруживаются до запуска, и не нужно явно приводить типы при извлечении из коллекций.',
    'Вопрос 15': 'Общепринятые имена: T (Type), E (Element), K (Key), V (Value), N (Number), R (Result). Это конвенция, облегчающая чтение обобщённого кода.',
    'Вопрос 16': 'Box хранит строку "Hello". Метод get() возвращает String, у которого вызывается length(). "Hello".length() = 5.',
    'Вопрос 17': 'Конструкция T extends Number задаёт верхнюю границу: T может быть Number или любым его подклассом (Integer, Double, BigDecimal и т.д.).',
    'Вопрос 18': 'Множественные границы задаются через &: T extends Comparable<T> & Cloneable. Запятая разделяет параметры типов, а не границы одного параметра.',
    'Вопрос 19': 'Обобщённый метод объявляет параметр типа <T> перед возвращаемым типом: <T> List<T> toList(T[] arr). Это позволяет методу работать с любым типом.',
    'Вопрос 20': 'Type erasure: компилятор проверяет типы, затем стирает параметры, заменяя их на Object (или границу). В runtime информация о типовых параметрах отсутствует.',
    'Вопрос 21': 'Из-за стирания типов List<String> и List<Integer> в runtime имеют один и тот же класс ArrayList. Поэтому getClass() возвращает одинаковый объект.',
    'Вопрос 22': 'Из-за стирания типов T не существует в runtime, поэтому нельзя создать new T() или new T[]. Компилятор не знает конкретный тип для создания экземпляра.',
    'Вопрос 23': 'StringBox extends Box<String> фиксирует тип параметра. Запись StringBox<String> ошибочна: String стало бы именем нового типового параметра, затеняющего класс String.',
    'Вопрос 24': 'Wildcard ? означает «неизвестный тип». Используется когда конкретный тип не важен, например List<?> принимает список с элементами любого типа.',
    'Вопрос 25': 'List<? extends Number> принимает List любого подтипа Number: List<Integer>, List<Double>, List<Number>. List<Number> не примет List<Integer> из-за инвариантности.',
    'Вопрос 26': 'PECS: если коллекция — источник данных (Producer), используем extends для чтения; если коллекция — приёмник данных (Consumer), используем super для записи.',
    'Вопрос 27': 'В Collections.copy() из src читаем элементы (producer → extends), в dest записываем элементы (consumer → super). Это классическое применение PECS.',
    'Вопрос 28': 'Pair создаётся с ключом "age" (String) и значением 25 (Integer). Конкатенация через + выводит age=25.',
    'Вопрос 29': 'Обобщённый интерфейс можно реализовать с конкретными типами. Класс не обязан быть обобщённым — он может зафиксировать типы при implements.',
    'Вопрос 30': 'Throwable — корень иерархии. От него наследуются Error (серьёзные ошибки JVM) и Exception (обрабатываемые исключения). RuntimeException — подкласс Exception.',
    'Вопрос 31': 'IOException — checked-исключение (наследует Exception, но не RuntimeException). NullPointerException и ArrayIndexOutOfBoundsException — unchecked (RuntimeException).',
    'Вопрос 32': 'Checked-исключения обязательно должны быть обработаны в try-catch или объявлены в throws. Unchecked (наследники RuntimeException) не требуют этого.',
    'Вопрос 33': 'StackOverflowError наследует Error → Throwable. Это не исключение, а ошибка JVM (переполнение стека вызовов), которую обычно нет смысла перехватывать.',
    'Вопрос 34': 'Выводится "A", затем деление на ноль вызывает ArithmeticException (B пропускается), catch печатает "C", и finally всегда выполняется — печатает "D". Итого: ACD.',
    'Вопрос 35': 'Catch-блоки проверяются по порядку. Если суперкласс стоит раньше подкласса, подкласс никогда не будет достигнут — компилятор выдаст ошибку "unreachable catch block".',
    'Вопрос 36': 'Выводится "1", выбрасывается RuntimeException, catch ловит его и печатает "2", finally печатает "3", затем выполнение продолжается — печатает "4". Итого: 1234.',
    'Вопрос 37': 'Multi-catch позволяет одним catch-блоком обработать несколько несвязанных типов исключений. Типы разделяются символом |, и они не должны быть наследниками друг друга.',
    'Вопрос 38': 'getMessage() возвращает строку-сообщение, переданную в конструктор исключения. printStackTrace() печатает стек вызовов, toString() — класс + сообщение.',
    'Вопрос 39': 'throw new Exception("msg") бросает конкретный объект исключения. throws Exception в сигнатуре метода предупреждает вызывающий код о возможном checked-исключении.',
    'Вопрос 40': 'getMessage() возвращает строку, переданную в конструктор: "Тест". Метод toString() вернул бы "java.lang.Exception: Тест", а getMessage() — только само сообщение.',
    'Вопрос 41': 'Для создания checked-исключения наследуем от Exception. RuntimeException — для unchecked, Error — для ошибок JVM. Exception не интерфейс, а класс.',
    'Вопрос 42': 'Try-with-resources (Java 7+) автоматически закрывает ресурсы после блока try. Ресурс должен реализовать интерфейс AutoCloseable с методом close().',
    'Вопрос 43': 'Сначала выполняется тело try — "used ", затем ресурс автоматически закрывается — вызывается close(), который печатает "closed ". Итого: used closed.',
    'Вопрос 44': 'Exception chaining — оборачивание исходного исключения (cause) в новое: throw new HighLevel("msg", originalException). Это сохраняет информацию о первопричине.',
    'Вопрос 45': 'Вариант A — двойная ошибка: перехват слишком широкого Exception маскирует конкретные проблемы, а пустой catch «проглатывает» исключение без логирования и обработки.',
    'Вопрос 46': 'Точка останова замораживает выполнение в нужном месте и открывает окно Variables со всеми видимыми переменными сразу, тогда как println() требует заранее решить, какое значение печатать, и переписывать код при новой гипотезе.',
    'Вопрос 47': 'Условие в поле Condition — обычное Java-выражение, доступное в контексте строки; программа остановится только когда оно истинно. Это позволяет поймать одну нужную итерацию из тысячи, не проходя вручную через все остальные.',
    'Вопрос 48': 'Step Into (F7 в IntelliJ IDEA, F11 в VS Code) переводит выполнение внутрь вызываемого метода, тогда как Step Over выполняет вызов целиком, не показывая, что происходит внутри него.',
    'Вопрос 49': 'Step Over — рабочая лошадка отладки: строку с вызовом вроде list.sort(comparator) проходят Step Over, потому что чужой код не интересен. Step Into используют, когда подозревают ошибку именно внутри вызываемого метода.',
    'Вопрос 50': 'sum = 60.0 верна (10+20+30), а вот count не должен был досчитаться до 4: инкремент count стоит вне блока try, поэтому строка "abc", не разобравшаяся в число, всё равно увеличивает счётчик.',
    'Вопрос 51': 'Evaluate Expression (Alt+F8 в IntelliJ IDEA) выполняет введённое выражение прямо в контексте остановленного потока — можно проверить гипотезу вроде sum / (count - 1), не перекомпилируя проект.',
    'Вопрос 52': 'Каждый вызов метода кладёт на стек кадр с его параметрами и локальными переменными. Щелчок по кадру в окне Frames показывает переменные именно того вызова — удобно, когда нужно понять, кто передал методу некорректные данные.'
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
