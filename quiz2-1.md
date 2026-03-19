# Тест 2.1: Основные конструкции языка Java — Часть 1 (Лекция 2)

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

<!-- ===== ЧАСТЬ 1: КЛАССЫ (1-10) ===== -->

<div class="quiz-question" data-correct="1">
<h4>Вопрос 1. Что такое класс в Java?</h4>
<div class="quiz-option" data-index="0">Готовый объект в памяти</div>
<div class="quiz-option" data-index="1">Шаблон (чертёж), по которому создаются объекты</div>
<div class="quiz-option" data-index="2">Набор статических методов</div>
<div class="quiz-option" data-index="3">Файл с расширением .class</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 2. Сколько классов может наследовать Java-класс через <code>extends</code>?</h4>
<div class="quiz-option" data-index="0">Неограниченное количество</div>
<div class="quiz-option" data-index="1">Два</div>
<div class="quiz-option" data-index="2">Ноль — наследование запрещено</div>
<div class="quiz-option" data-index="3">Только один</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 3. Когда выполняется статический блок инициализации?</h4>
<div class="quiz-option" data-index="0">Один раз при загрузке класса в память</div>
<div class="quiz-option" data-index="1">При каждом создании объекта</div>
<div class="quiz-option" data-index="2">При вызове конструктора</div>
<div class="quiz-option" data-index="3">При вызове любого метода класса</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 4. Чем отличается поле экземпляра от статического поля?</h4>
<div class="quiz-option" data-index="0">Поле экземпляра доступно только в конструкторе</div>
<div class="quiz-option" data-index="1">Статическое поле существует только во время вызова метода</div>
<div class="quiz-option" data-index="2">Поле экземпляра принадлежит каждому объекту отдельно, статическое — общее для всех объектов</div>
<div class="quiz-option" data-index="3">Статическое поле может быть только типа int</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 5. Какой модификатор доступа делает поле видимым только внутри своего класса?</h4>
<div class="quiz-option" data-index="0">protected</div>
<div class="quiz-option" data-index="1">private</div>
<div class="quiz-option" data-index="2">default (без модификатора)</div>
<div class="quiz-option" data-index="3">public</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 6. Что означает модификатор доступа по умолчанию (без ключевого слова)?</h4>
<div class="quiz-option" data-index="0">Доступ только внутри того же пакета (package-private)</div>
<div class="quiz-option" data-index="1">Доступ отовсюду (как public)</div>
<div class="quiz-option" data-index="2">Доступ только внутри класса (как private)</div>
<div class="quiz-option" data-index="3">Доступ только для подклассов</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 7. Когда выполняется блок инициализации экземпляра (instance block)?</h4>
<div class="quiz-option" data-index="0">Один раз при загрузке класса</div>
<div class="quiz-option" data-index="1">Только при первом создании объекта</div>
<div class="quiz-option" data-index="2">Только при вызове метода</div>
<div class="quiz-option" data-index="3">При каждом создании нового объекта класса</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 8. Что объявляет конструкция <code>public static final String NAME = "Test";</code>?</h4>
<div class="quiz-option" data-index="0">Изменяемое статическое поле</div>
<div class="quiz-option" data-index="1">Локальную переменную</div>
<div class="quiz-option" data-index="2">Константу класса</div>
<div class="quiz-option" data-index="3">Метод, возвращающий строку</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 9. Где можно использовать ключевое слово <code>var</code> в Java?</h4>
<div class="quiz-option" data-index="0">В полях класса и параметрах методов</div>
<div class="quiz-option" data-index="1">Только для локальных переменных с инициализацией</div>
<div class="quiz-option" data-index="2">Везде, где допустимо объявление переменной</div>
<div class="quiz-option" data-index="3">Только в возвращаемых типах методов</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 10. Является ли <code>var</code> в Java динамической типизацией?</h4>
<div class="quiz-option" data-index="0">Нет, тип фиксируется при компиляции (выведение типа)</div>
<div class="quiz-option" data-index="1">Да, тип определяется во время выполнения</div>
<div class="quiz-option" data-index="2">Да, переменная может менять тип после присваивания</div>
<div class="quiz-option" data-index="3">Нет, var — это просто псевдоним для Object</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== ЧАСТЬ 2: АБСТРАКТНЫЕ КЛАССЫ (11-17) ===== -->

<div class="quiz-question" data-correct="3">
<h4>Вопрос 11. Можно ли создать экземпляр абстрактного класса?</h4>
<div class="quiz-option" data-index="0">Да, через new</div>
<div class="quiz-option" data-index="1">Да, но только внутри самого класса</div>
<div class="quiz-option" data-index="2">Да, если все методы имеют реализацию</div>
<div class="quiz-option" data-index="3">Нет, нельзя создать экземпляр абстрактного класса</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 12. Может ли абстрактный класс содержать обычные методы с реализацией?</h4>
<div class="quiz-option" data-index="0">Да, может содержать и абстрактные, и обычные методы</div>
<div class="quiz-option" data-index="1">Нет, все методы должны быть абстрактными</div>
<div class="quiz-option" data-index="2">Только статические методы</div>
<div class="quiz-option" data-index="3">Только private-методы</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 13. Может ли абстрактный класс иметь конструктор?</h4>
<div class="quiz-option" data-index="0">Нет, абстрактные классы не имеют конструкторов</div>
<div class="quiz-option" data-index="1">Только конструктор по умолчанию (без параметров)</div>
<div class="quiz-option" data-index="2">Да, конструктор вызывается через super() в подклассах</div>
<div class="quiz-option" data-index="3">Только private-конструкторы</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 14. Что обязан сделать подкласс абстрактного класса?</h4>
<div class="quiz-option" data-index="0">Переопределить все методы, включая обычные</div>
<div class="quiz-option" data-index="1">Реализовать все абстрактные методы (или сам стать абстрактным)</div>
<div class="quiz-option" data-index="2">Объявить те же поля, что и в абстрактном классе</div>
<div class="quiz-option" data-index="3">Иметь конструктор без параметров</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 15. Что такое полиморфизм в контексте абстрактных классов?</h4>
<div class="quiz-option" data-index="0">Возможность создавать несколько конструкторов</div>
<div class="quiz-option" data-index="1">Возможность изменять модификаторы доступа при наследовании</div>
<div class="quiz-option" data-index="2">Возможность класса реализовать несколько интерфейсов</div>
<div class="quiz-option" data-index="3">Переменная типа базового класса может хранить объект любого подкласса</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 16. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
abstract class Shape { abstract double area(); }
class Circle extends Shape {
    double r = 5;
    double area() { return Math.PI * r * r; }
}
Shape s = new Circle();
System.out.println(s instanceof Shape);
```

<div class="quiz-option" data-index="0">true</div>
<div class="quiz-option" data-index="1">false</div>
<div class="quiz-option" data-index="2">Ошибка компиляции</div>
<div class="quiz-option" data-index="3">Ошибка времени выполнения</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 17. Чем абстрактный класс похож на обычный класс?</h4>
<div class="quiz-option" data-index="0">Оба можно инстанцировать через new</div>
<div class="quiz-option" data-index="1">Оба не могут содержать реализацию методов</div>
<div class="quiz-option" data-index="2">Оба могут содержать поля, конструкторы и методы с реализацией</div>
<div class="quiz-option" data-index="3">Оба могут наследовать несколько классов</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== ЧАСТЬ 2.5: SEALED-КЛАССЫ (18-22) ===== -->

<div class="quiz-question" data-correct="1">
<h4>Вопрос 18. Что делает ключевое слово <code>sealed</code>?</h4>
<div class="quiz-option" data-index="0">Запрещает наследование полностью (как final)</div>
<div class="quiz-option" data-index="1">Ограничивает список допустимых наследников через permits</div>
<div class="quiz-option" data-index="2">Делает все поля класса неизменяемыми</div>
<div class="quiz-option" data-index="3">Запрещает создание экземпляров класса</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 19. Каким должен быть наследник sealed-класса?</h4>
<div class="quiz-option" data-index="0">final, sealed или non-sealed</div>
<div class="quiz-option" data-index="1">Только final</div>
<div class="quiz-option" data-index="2">Только abstract</div>
<div class="quiz-option" data-index="3">Любым — ограничений нет</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 20. Что означает модификатор <code>non-sealed</code> у наследника sealed-класса?</h4>
<div class="quiz-option" data-index="0">Запрещает дальнейшее наследование</div>
<div class="quiz-option" data-index="1">Делает класс абстрактным</div>
<div class="quiz-option" data-index="2">Ограничивает наследников по permits</div>
<div class="quiz-option" data-index="3">Снимает ограничение — любой класс может наследовать дальше</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 21. В какой версии Java появились sealed-классы?</h4>
<div class="quiz-option" data-index="0">Java 8</div>
<div class="quiz-option" data-index="1">Java 11</div>
<div class="quiz-option" data-index="2">Java 17</div>
<div class="quiz-option" data-index="3">Java 21</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 22. Почему record неявно является допустимым наследником sealed-типа?</h4>
<div class="quiz-option" data-index="0">Потому что record — это abstract</div>
<div class="quiz-option" data-index="1">Потому что record неявно final</div>
<div class="quiz-option" data-index="2">Потому что record — это non-sealed</div>
<div class="quiz-option" data-index="3">Потому что record — это интерфейс</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== ЧАСТЬ 3: ИНТЕРФЕЙСЫ (23-34) ===== -->

<div class="quiz-question" data-correct="2">
<h4>Вопрос 23. Какие поля может содержать интерфейс?</h4>
<div class="quiz-option" data-index="0">Любые поля, как у обычного класса</div>
<div class="quiz-option" data-index="1">Только private static final</div>
<div class="quiz-option" data-index="2">Только public static final (константы)</div>
<div class="quiz-option" data-index="3">Интерфейсы не могут содержать полей</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 24. Сколько интерфейсов может реализовать один класс?</h4>
<div class="quiz-option" data-index="0">Любое количество</div>
<div class="quiz-option" data-index="1">Только один</div>
<div class="quiz-option" data-index="2">Не более трёх</div>
<div class="quiz-option" data-index="3">Не более двух</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 25. Что такое default-метод в интерфейсе?</h4>
<div class="quiz-option" data-index="0">Метод с модификатором package-private</div>
<div class="quiz-option" data-index="1">Абстрактный метод, вызываемый по умолчанию</div>
<div class="quiz-option" data-index="2">Метод, который обязан переопределить каждый класс</div>
<div class="quiz-option" data-index="3">Метод с реализацией по умолчанию, который можно переопределить в классе</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 26. Как вызвать статический метод интерфейса?</h4>
<div class="quiz-option" data-index="0">Через экземпляр класса, реализующего интерфейс</div>
<div class="quiz-option" data-index="1">Напрямую на интерфейсе: ИмяИнтерфейса.метод()</div>
<div class="quiz-option" data-index="2">Только через super</div>
<div class="quiz-option" data-index="3">Статические методы в интерфейсах не поддерживаются</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 27. С какой версии Java доступны private-методы в интерфейсах?</h4>
<div class="quiz-option" data-index="0">Java 9</div>
<div class="quiz-option" data-index="1">Java 8</div>
<div class="quiz-option" data-index="2">Java 11</div>
<div class="quiz-option" data-index="3">Java 17</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 28. Что такое маркерный интерфейс?</h4>
<div class="quiz-option" data-index="0">Интерфейс с одним абстрактным методом</div>
<div class="quiz-option" data-index="1">Интерфейс с только default-методами</div>
<div class="quiz-option" data-index="2">Интерфейс без методов и полей, обозначающий принадлежность к категории</div>
<div class="quiz-option" data-index="3">Интерфейс, помеченный аннотацией @Marker</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 29. Что такое функциональный интерфейс?</h4>
<div class="quiz-option" data-index="0">Интерфейс, который содержит только static-методы</div>
<div class="quiz-option" data-index="1">Интерфейс без методов</div>
<div class="quiz-option" data-index="2">Любой интерфейс, помеченный @FunctionalInterface</div>
<div class="quiz-option" data-index="3">Интерфейс ровно с одним абстрактным методом</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 30. Может ли интерфейс наследовать другие интерфейсы?</h4>
<div class="quiz-option" data-index="0">Нет, интерфейсы не поддерживают наследование</div>
<div class="quiz-option" data-index="1">Да, и даже несколько — через extends</div>
<div class="quiz-option" data-index="2">Только один через implements</div>
<div class="quiz-option" data-index="3">Только один через extends</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 31. Когда лучше использовать интерфейс, а не абстрактный класс?</h4>
<div class="quiz-option" data-index="0">Когда нужно определить контракт поведения для разнородных классов (отношение «умеет»)</div>
<div class="quiz-option" data-index="1">Когда классы связаны отношением «является» и имеют общий код</div>
<div class="quiz-option" data-index="2">Когда нужно хранить изменяемое состояние</div>
<div class="quiz-option" data-index="3">Когда нужны конструкторы в базовом типе</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 32. Может ли интерфейс хранить изменяемое состояние (нестатические поля)?</h4>
<div class="quiz-option" data-index="0">Да, как обычный класс</div>
<div class="quiz-option" data-index="1">Да, но только protected-поля</div>
<div class="quiz-option" data-index="2">Нет, интерфейсы не хранят состояние</div>
<div class="quiz-option" data-index="3">Только через default-методы</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 33. Какой модификатор доступа имеют методы интерфейса по умолчанию?</h4>
<div class="quiz-option" data-index="0">private</div>
<div class="quiz-option" data-index="1">protected</div>
<div class="quiz-option" data-index="2">package-private (default)</div>
<div class="quiz-option" data-index="3">public abstract</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 34. Может ли интерфейс содержать конструктор?</h4>
<div class="quiz-option" data-index="0">Нет, конструкторы в интерфейсах не допускаются</div>
<div class="quiz-option" data-index="1">Да, по аналогии с абстрактными классами</div>
<div class="quiz-option" data-index="2">Только private-конструкторы</div>
<div class="quiz-option" data-index="3">Только конструктор по умолчанию</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== ЧАСТЬ 4: МАССИВЫ (35-42) ===== -->

<div class="quiz-question" data-correct="2">
<h4>Вопрос 35. С какого индекса начинается нумерация элементов массива в Java?</h4>
<div class="quiz-option" data-index="0">С 1</div>
<div class="quiz-option" data-index="1">С -1</div>
<div class="quiz-option" data-index="2">С 0</div>
<div class="quiz-option" data-index="3">Зависит от типа массива</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 36. Можно ли изменить размер массива после его создания?</h4>
<div class="quiz-option" data-index="0">Да, через метод resize()</div>
<div class="quiz-option" data-index="1">Нет, размер массива фиксирован при создании</div>
<div class="quiz-option" data-index="2">Да, через поле length</div>
<div class="quiz-option" data-index="3">Только для массивов объектов</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 37. Что произойдёт при обращении к <code>arr[arr.length]</code>? <span class="jshell-hint">Попробуй в jshell!</span></h4>
<div class="quiz-option" data-index="0">ArrayIndexOutOfBoundsException</div>
<div class="quiz-option" data-index="1">Вернётся null</div>
<div class="quiz-option" data-index="2">Вернётся значение последнего элемента</div>
<div class="quiz-option" data-index="3">Ошибка компиляции</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 38. Что такое зубчатый (jagged) массив?</h4>
<div class="quiz-option" data-index="0">Массив с отрицательными индексами</div>
<div class="quiz-option" data-index="1">Массив, хранящий разные типы данных</div>
<div class="quiz-option" data-index="2">Массив фиксированной прямоугольной формы</div>
<div class="quiz-option" data-index="3">Массив массивов, где строки могут иметь разную длину</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 39. Какое значение по умолчанию у элементов <code>String[] arr = new String[3]</code>? <span class="jshell-hint">Попробуй в jshell!</span></h4>
<div class="quiz-option" data-index="0">Пустая строка ""</div>
<div class="quiz-option" data-index="1">0</div>
<div class="quiz-option" data-index="2">null</div>
<div class="quiz-option" data-index="3">"null"</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 40. Какой рекомендуемый стиль объявления массива в Java?</h4>
<div class="quiz-option" data-index="0">int numbers[] (C-стиль)</div>
<div class="quiz-option" data-index="1">int[] numbers (Java-стиль)</div>
<div class="quiz-option" data-index="2">Array&lt;int&gt; numbers</div>
<div class="quiz-option" data-index="3">int numbers[5]</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 41. Какова сложность доступа к элементу массива по индексу?</h4>
<div class="quiz-option" data-index="0">O(1) — постоянная</div>
<div class="quiz-option" data-index="1">O(n) — линейная</div>
<div class="quiz-option" data-index="2">O(log n) — логарифмическая</div>
<div class="quiz-option" data-index="3">O(n²) — квадратичная</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 42. Что произойдёт при выполнении <code>names[0].length()</code>, если <code>String[] names = new String[3]</code>? <span class="jshell-hint">Попробуй в jshell!</span></h4>
<div class="quiz-option" data-index="0">Вернётся 0</div>
<div class="quiz-option" data-index="1">Вернётся 3</div>
<div class="quiz-option" data-index="2">Ошибка компиляции</div>
<div class="quiz-option" data-index="3">NullPointerException</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== ЧАСТЬ 5: СТРОКИ (43-54) ===== -->

<div class="quiz-question" data-correct="1">
<h4>Вопрос 43. Являются ли строки в Java изменяемыми (mutable)?</h4>
<div class="quiz-option" data-index="0">Да, строки можно изменять</div>
<div class="quiz-option" data-index="1">Нет, String — неизменяемый (immutable) класс</div>
<div class="quiz-option" data-index="2">Только при использовании new String()</div>
<div class="quiz-option" data-index="3">Зависит от версии Java</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 44. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
String s = "hello";
s.toUpperCase();
System.out.println(s);
```

<div class="quiz-option" data-index="0">hello</div>
<div class="quiz-option" data-index="1">HELLO</div>
<div class="quiz-option" data-index="2">Hello</div>
<div class="quiz-option" data-index="3">Ошибка компиляции</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 45. Что такое String Pool?</h4>
<div class="quiz-option" data-index="0">Массив всех строк программы</div>
<div class="quiz-option" data-index="1">Стек для хранения строковых переменных</div>
<div class="quiz-option" data-index="2">Специальная область памяти в куче для хранения уникальных строковых литералов</div>
<div class="quiz-option" data-index="3">Пул потоков для обработки строковых операций</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 46. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
String s1 = "Test";
String s2 = "Test";
String s3 = new String("Test");
System.out.println(s1 == s2);
System.out.println(s1 == s3);
```

<div class="quiz-option" data-index="0">false, false</div>
<div class="quiz-option" data-index="1">true, true</div>
<div class="quiz-option" data-index="2">false, true</div>
<div class="quiz-option" data-index="3">true, false</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 47. Что делает метод <code>intern()</code> у строки?</h4>
<div class="quiz-option" data-index="0">Преобразует строку в массив символов</div>
<div class="quiz-option" data-index="1">Помещает строку в String Pool или возвращает ссылку на уже существующую</div>
<div class="quiz-option" data-index="2">Удаляет пробелы из строки</div>
<div class="quiz-option" data-index="3">Делает строку изменяемой</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 48. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
String s1 = "Hello";
String s2 = "Hel" + "lo";
System.out.println(s1 == s2);
```

<div class="quiz-option" data-index="0">true — компилятор склеит литералы в один</div>
<div class="quiz-option" data-index="1">false — конкатенация создаёт новый объект</div>
<div class="quiz-option" data-index="2">Ошибка компиляции</div>
<div class="quiz-option" data-index="3">Зависит от JVM</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 49. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
String s1 = "Hello";
String s3 = "Hel";
String s4 = s3 + "lo";
System.out.println(s1 == s4);
```

<div class="quiz-option" data-index="0">true</div>
<div class="quiz-option" data-index="1">Ошибка компиляции</div>
<div class="quiz-option" data-index="2">false — конкатенация переменной создаёт объект в куче, не в Pool</div>
<div class="quiz-option" data-index="3">true — JVM оптимизирует конкатенацию</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 50. Чем <code>StringBuilder</code> отличается от <code>StringBuffer</code>?</h4>
<div class="quiz-option" data-index="0">StringBuilder неизменяемый, StringBuffer изменяемый</div>
<div class="quiz-option" data-index="1">StringBuilder не потокобезопасен (быстрее), StringBuffer потокобезопасен (synchronized)</div>
<div class="quiz-option" data-index="2">StringBuffer устарел и не используется</div>
<div class="quiz-option" data-index="3">StringBuilder для строк, StringBuffer для чисел</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 51. Почему конкатенация строк в цикле через <code>+=</code> неэффективна?</h4>
<div class="quiz-option" data-index="0">Потому что += не работает со строками</div>
<div class="quiz-option" data-index="1">Потому что компилятор не может оптимизировать цикл</div>
<div class="quiz-option" data-index="2">Потому что строки хранятся в стеке</div>
<div class="quiz-option" data-index="3">Потому что каждая операция создаёт новый объект String</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 52. Что вернёт <code>"Java".substring(1, 3)</code>? <span class="jshell-hint">Попробуй в jshell!</span></h4>
<div class="quiz-option" data-index="0">"av"</div>
<div class="quiz-option" data-index="1">"ava"</div>
<div class="quiz-option" data-index="2">"Ja"</div>
<div class="quiz-option" data-index="3">"Jav"</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 53. С какой версии Java доступны текстовые блоки (text blocks)?</h4>
<div class="quiz-option" data-index="0">Java 8</div>
<div class="quiz-option" data-index="1">Java 11</div>
<div class="quiz-option" data-index="2">Java 15</div>
<div class="quiz-option" data-index="3">Java 17</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 54. Чем отличается <code>isEmpty()</code> от <code>isBlank()</code>? <span class="jshell-hint">Попробуй в jshell!</span></h4>
<div class="quiz-option" data-index="0">isEmpty() проверяет пробелы, isBlank() — длину</div>
<div class="quiz-option" data-index="1">isEmpty() проверяет длину == 0, isBlank() — что строка пуста или содержит только пробелы</div>
<div class="quiz-option" data-index="2">Ничем — это синонимы</div>
<div class="quiz-option" data-index="3">isBlank() доступен только для StringBuilder</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== ЧАСТЬ 6: ЗАПИСИ — RECORDS (55-61) ===== -->

<div class="quiz-question" data-correct="3">
<h4>Вопрос 55. Что автоматически генерируется для record?</h4>
<div class="quiz-option" data-index="0">Только конструктор</div>
<div class="quiz-option" data-index="1">Конструктор и toString()</div>
<div class="quiz-option" data-index="2">Конструктор, геттеры и toString()</div>
<div class="quiz-option" data-index="3">Конструктор, геттеры, equals(), hashCode() и toString()</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 56. Может ли record наследоваться от другого класса?</h4>
<div class="quiz-option" data-index="0">Нет, record не может наследоваться от классов</div>
<div class="quiz-option" data-index="1">Да, от любого класса</div>
<div class="quiz-option" data-index="2">Только от абстрактного класса</div>
<div class="quiz-option" data-index="3">Только от другого record</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 57. Как называются геттеры в record?</h4>
<div class="quiz-option" data-index="0">getИмяПоля()</div>
<div class="quiz-option" data-index="1">getИмяПоля() или isИмяПоля()</div>
<div class="quiz-option" data-index="2">Совпадают с именем поля: имяПоля()</div>
<div class="quiz-option" data-index="3">Геттеры не генерируются автоматически</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 58. Что такое компактный конструктор record?</h4>
<div class="quiz-option" data-index="0">Конструктор без тела</div>
<div class="quiz-option" data-index="1">Конструктор без параметров в скобках, для валидации и нормализации данных</div>
<div class="quiz-option" data-index="2">Статический фабричный метод</div>
<div class="quiz-option" data-index="3">Конструктор с аннотацией @Compact</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 59. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
record Point(int x, int y) {}
Point p1 = new Point(3, 4);
Point p2 = new Point(3, 4);
System.out.println(p1.equals(p2));
```

<div class="quiz-option" data-index="0">false — это разные объекты</div>
<div class="quiz-option" data-index="1">Ошибка компиляции</div>
<div class="quiz-option" data-index="2">Зависит от реализации</div>
<div class="quiz-option" data-index="3">true — equals() в record сравнивает по содержимому полей</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 60. Может ли record реализовать интерфейс?</h4>
<div class="quiz-option" data-index="0">Да, record может реализовать интерфейсы</div>
<div class="quiz-option" data-index="1">Нет, record не может реализовать интерфейсы</div>
<div class="quiz-option" data-index="2">Только маркерные интерфейсы</div>
<div class="quiz-option" data-index="3">Только функциональные интерфейсы</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 61. Нужно ли писать <code>this.name = name;</code> в компактном конструкторе record?</h4>
<div class="quiz-option" data-index="0">Да, всегда нужно присваивать поля вручную</div>
<div class="quiz-option" data-index="1">Да, иначе поля будут null</div>
<div class="quiz-option" data-index="2">Нет, присваивание происходит автоматически после завершения тела конструктора</div>
<div class="quiz-option" data-index="3">Только для полей ссылочного типа</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== ЧАСТЬ 7: ПЕРЕЧИСЛЕНИЯ — ENUMS (62-69) ===== -->

<div class="quiz-question" data-correct="1">
<h4>Вопрос 62. Что такое enum в Java?</h4>
<div class="quiz-option" data-index="0">Массив строковых констант</div>
<div class="quiz-option" data-index="1">Специальный тип с фиксированным набором именованных констант-объектов</div>
<div class="quiz-option" data-index="2">Синоним для static final</div>
<div class="quiz-option" data-index="3">Целочисленный тип данных</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 63. Что возвращает метод <code>values()</code> у enum?</h4>
<div class="quiz-option" data-index="0">Массив всех констант перечисления</div>
<div class="quiz-option" data-index="1">Количество констант</div>
<div class="quiz-option" data-index="2">Первую константу</div>
<div class="quiz-option" data-index="3">Строковое представление всех констант</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 64. Что возвращает <code>Color.RED.ordinal()</code>, если <code>enum Color { RED, GREEN, BLUE }</code>? <span class="jshell-hint">Попробуй в jshell!</span></h4>
<div class="quiz-option" data-index="0">1</div>
<div class="quiz-option" data-index="1">3</div>
<div class="quiz-option" data-index="2">"RED"</div>
<div class="quiz-option" data-index="3">0</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 65. Может ли enum наследовать другой класс?</h4>
<div class="quiz-option" data-index="0">Да, от любого класса</div>
<div class="quiz-option" data-index="1">Только от абстрактного класса</div>
<div class="quiz-option" data-index="2">Нет, enum неявно расширяет java.lang.Enum</div>
<div class="quiz-option" data-index="3">Только от другого enum</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 66. Может ли enum содержать абстрактные методы?</h4>
<div class="quiz-option" data-index="0">Нет, enum не поддерживает абстрактные методы</div>
<div class="quiz-option" data-index="1">Да, каждая константа должна предоставить реализацию</div>
<div class="quiz-option" data-index="2">Только один абстрактный метод</div>
<div class="quiz-option" data-index="3">Только если enum помечен как abstract</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 67. Чем <code>EnumSet</code> лучше обычного <code>HashSet</code> для хранения enum-значений?</h4>
<div class="quiz-option" data-index="0">Реализован через битовый вектор — O(1) и минимум памяти</div>
<div class="quiz-option" data-index="1">Поддерживает null-элементы</div>
<div class="quiz-option" data-index="2">Хранит элементы в алфавитном порядке</div>
<div class="quiz-option" data-index="3">Ничем — это одно и то же</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 68. Как <code>EnumMap</code> хранит данные внутри?</h4>
<div class="quiz-option" data-index="0">Как хэш-таблицу</div>
<div class="quiz-option" data-index="1">Как связный список</div>
<div class="quiz-option" data-index="2">Как бинарное дерево</div>
<div class="quiz-option" data-index="3">Как массив по ordinal() — O(1) доступ</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 69. Что делает метод <code>valueOf("NORTH")</code> у <code>enum Direction { NORTH, SOUTH }</code>? <span class="jshell-hint">Попробуй в jshell!</span></h4>
<div class="quiz-option" data-index="0">Возвращает порядковый номер NORTH</div>
<div class="quiz-option" data-index="1">Создаёт новую константу NORTH</div>
<div class="quiz-option" data-index="2">Возвращает константу NORTH по её строковому имени</div>
<div class="quiz-option" data-index="3">Проверяет, существует ли NORTH</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== ЧАСТЬ 8: АННОТАЦИИ (70-75) ===== -->

<div class="quiz-question" data-correct="1">
<h4>Вопрос 70. Что такое аннотация в Java?</h4>
<div class="quiz-option" data-index="0">Многострочный комментарий</div>
<div class="quiz-option" data-index="1">Специальная конструкция, добавляющая метаданные к элементам кода</div>
<div class="quiz-option" data-index="2">Условная инструкция компилятора</div>
<div class="quiz-option" data-index="3">Декоратор, изменяющий поведение метода</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 71. Что означает <code>@Retention(RetentionPolicy.RUNTIME)</code>?</h4>
<div class="quiz-option" data-index="0">Аннотация доступна во время выполнения через Reflection</div>
<div class="quiz-option" data-index="1">Аннотация существует только в исходном коде</div>
<div class="quiz-option" data-index="2">Аннотация хранится только в .class файле</div>
<div class="quiz-option" data-index="3">Аннотация наследуется подклассами</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 72. Для чего используется аннотация <code>@Override</code>?</h4>
<div class="quiz-option" data-index="0">Для создания нового метода</div>
<div class="quiz-option" data-index="1">Для запрета наследования метода</div>
<div class="quiz-option" data-index="2">Для указания, что метод устарел</div>
<div class="quiz-option" data-index="3">Для проверки, что метод действительно переопределяет родительский</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 73. Что указывает мета-аннотация <code>@Target</code>?</h4>
<div class="quiz-option" data-index="0">Время жизни аннотации</div>
<div class="quiz-option" data-index="1">Значение по умолчанию для параметра аннотации</div>
<div class="quiz-option" data-index="2">К каким элементам кода можно применять аннотацию (METHOD, FIELD, TYPE и т.д.)</div>
<div class="quiz-option" data-index="3">Имя целевого класса</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 74. Что делает аннотация <code>@FunctionalInterface</code>?</h4>
<div class="quiz-option" data-index="0">Превращает класс в функцию</div>
<div class="quiz-option" data-index="1">Проверяет, что интерфейс содержит ровно один абстрактный метод</div>
<div class="quiz-option" data-index="2">Запрещает добавлять default-методы</div>
<div class="quiz-option" data-index="3">Делает интерфейс совместимым с лямбдами (обязательно)</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 75. Какой <code>RetentionPolicy</code> означает, что аннотация существует только в исходном коде?</h4>
<div class="quiz-option" data-index="0">SOURCE</div>
<div class="quiz-option" data-index="1">CLASS</div>
<div class="quiz-option" data-index="2">RUNTIME</div>
<div class="quiz-option" data-index="3">COMPILE</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== ЧАСТЬ 9: АНОНИМНЫЕ КЛАССЫ (76-79) ===== -->

<div class="quiz-question" data-correct="2">
<h4>Вопрос 76. Что такое анонимный класс?</h4>
<div class="quiz-option" data-index="0">Класс без полей</div>
<div class="quiz-option" data-index="1">Класс, объявленный внутри другого класса</div>
<div class="quiz-option" data-index="2">Класс без имени, создаваемый и инстанцируемый одновременно</div>
<div class="quiz-option" data-index="3">Класс, доступный только через Reflection</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 77. К каким переменным из окружающего метода имеет доступ анонимный класс?</h4>
<div class="quiz-option" data-index="0">К любым переменным</div>
<div class="quiz-option" data-index="1">Только к final или effectively final переменным</div>
<div class="quiz-option" data-index="2">Только к статическим переменным</div>
<div class="quiz-option" data-index="3">Анонимный класс не имеет доступа к внешним переменным</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 78. Как обратиться к приватному полю внешнего класса из анонимного класса при конфликте имён?</h4>
<div class="quiz-option" data-index="0">Через super.поле</div>
<div class="quiz-option" data-index="1">Через this.поле</div>
<div class="quiz-option" data-index="2">Невозможно при конфликте</div>
<div class="quiz-option" data-index="3">Через ВнешнийКласс.this.поле</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 79. Сколько интерфейсов может реализовать анонимный класс?</h4>
<div class="quiz-option" data-index="0">Только один (или расширить один класс)</div>
<div class="quiz-option" data-index="1">Неограниченное количество</div>
<div class="quiz-option" data-index="2">Два</div>
<div class="quiz-option" data-index="3">Ноль — анонимные классы не могут реализовать интерфейсы</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== ЧАСТЬ 10: ЛОКАЛЬНЫЕ КЛАССЫ (80-82) ===== -->

<div class="quiz-question" data-correct="2">
<h4>Вопрос 80. Чем локальный класс отличается от анонимного?</h4>
<div class="quiz-option" data-index="0">Локальный класс не может иметь методов</div>
<div class="quiz-option" data-index="1">Анонимный класс можно использовать повторно</div>
<div class="quiz-option" data-index="2">Локальный класс имеет имя и может создавать несколько экземпляров</div>
<div class="quiz-option" data-index="3">Локальный класс виден во всём внешнем классе</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 81. Где объявляется локальный класс?</h4>
<div class="quiz-option" data-index="0">В теле другого класса на уровне полей</div>
<div class="quiz-option" data-index="1">Внутри метода, конструктора или блока</div>
<div class="quiz-option" data-index="2">В отдельном файле</div>
<div class="quiz-option" data-index="3">В интерфейсе</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 82. Что доступно локальному классу внутри статического метода?</h4>
<div class="quiz-option" data-index="0">Все поля внешнего класса, включая нестатические</div>
<div class="quiz-option" data-index="1">Ничего из внешнего класса</div>
<div class="quiz-option" data-index="2">Только поля с модификатором public</div>
<div class="quiz-option" data-index="3">Только статические члены внешнего класса и final/effectively final локальные переменные</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== ЧАСТЬ 11: ЛЯМБДА-ВЫРАЖЕНИЯ (83-91) ===== -->

<div class="quiz-question" data-correct="0">
<h4>Вопрос 83. Что такое лямбда-выражение в Java?</h4>
<div class="quiz-option" data-index="0">Анонимная функция, реализующая функциональный интерфейс</div>
<div class="quiz-option" data-index="1">Специальный вид цикла</div>
<div class="quiz-option" data-index="2">Метод, объявленный без модификаторов доступа</div>
<div class="quiz-option" data-index="3">Способ создания анонимного класса</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 84. Какой функциональный интерфейс принимает аргумент типа <code>T</code> и возвращает <code>boolean</code>?</h4>
<div class="quiz-option" data-index="0">Function&lt;T, Boolean&gt;</div>
<div class="quiz-option" data-index="1">Consumer&lt;T&gt;</div>
<div class="quiz-option" data-index="2">Predicate&lt;T&gt;</div>
<div class="quiz-option" data-index="3">Supplier&lt;T&gt;</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 85. Какой функциональный интерфейс не принимает аргументов и возвращает значение?</h4>
<div class="quiz-option" data-index="0">Consumer&lt;T&gt;</div>
<div class="quiz-option" data-index="1">Supplier&lt;T&gt;</div>
<div class="quiz-option" data-index="2">Runnable</div>
<div class="quiz-option" data-index="3">Predicate&lt;T&gt;</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 86. Какой функциональный интерфейс принимает аргумент и ничего не возвращает?</h4>
<div class="quiz-option" data-index="0">Supplier&lt;T&gt;</div>
<div class="quiz-option" data-index="1">Function&lt;T, R&gt;</div>
<div class="quiz-option" data-index="2">Predicate&lt;T&gt;</div>
<div class="quiz-option" data-index="3">Consumer&lt;T&gt;</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 87. Что выведет следующий код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
Function<String, Integer> len = s -> s.length();
System.out.println(len.apply("Java"));
```

<div class="quiz-option" data-index="0">4</div>
<div class="quiz-option" data-index="1">Java</div>
<div class="quiz-option" data-index="2">Ошибка компиляции</div>
<div class="quiz-option" data-index="3">true</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 88. На что указывает <code>this</code> внутри лямбда-выражения?</h4>
<div class="quiz-option" data-index="0">На саму лямбду</div>
<div class="quiz-option" data-index="1">На функциональный интерфейс</div>
<div class="quiz-option" data-index="2">На объект внешнего класса (содержащий лямбду)</div>
<div class="quiz-option" data-index="3">this нельзя использовать в лямбда-выражениях</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 89. Может ли лямбда-выражение захватывать изменяемую локальную переменную?</h4>
<div class="quiz-option" data-index="0">Да, любую переменную</div>
<div class="quiz-option" data-index="1">Нет, только final или effectively final переменные</div>
<div class="quiz-option" data-index="2">Только статические переменные</div>
<div class="quiz-option" data-index="3">Только примитивные типы</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 90. Что делает <code>BinaryOperator&lt;Integer&gt;</code>?</h4>
<div class="quiz-option" data-index="0">Принимает Integer и возвращает boolean</div>
<div class="quiz-option" data-index="1">Принимает два аргумента разных типов и возвращает Integer</div>
<div class="quiz-option" data-index="2">Не принимает аргументов и возвращает Integer</div>
<div class="quiz-option" data-index="3">Принимает два Integer и возвращает Integer</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 91. Какой правильный синтаксис лямбда-выражения для Runnable?</h4>
<div class="quiz-option" data-index="0">() -> System.out.println("Hi")</div>
<div class="quiz-option" data-index="1">-> System.out.println("Hi")</div>
<div class="quiz-option" data-index="2">() => System.out.println("Hi")</div>
<div class="quiz-option" data-index="3">lambda: System.out.println("Hi")</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== ЧАСТЬ 12: ССЫЛКИ НА МЕТОДЫ (92-96) ===== -->

<div class="quiz-question" data-correct="2">
<h4>Вопрос 92. Что является эквивалентом лямбды <code>s -> s.toUpperCase()</code>?</h4>
<div class="quiz-option" data-index="0">toUpperCase::String</div>
<div class="quiz-option" data-index="1">s::toUpperCase</div>
<div class="quiz-option" data-index="2">String::toUpperCase</div>
<div class="quiz-option" data-index="3">String.toUpperCase()</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 93. Какая ссылка на метод соответствует лямбде <code>(a, b) -> Math.max(a, b)</code>?</h4>
<div class="quiz-option" data-index="0">Math.max::static</div>
<div class="quiz-option" data-index="1">Math::max</div>
<div class="quiz-option" data-index="2">max::Math</div>
<div class="quiz-option" data-index="3">Math::max()</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 94. Какая ссылка на метод соответствует лямбде <code>() -> new ArrayList<>()</code>?</h4>
<div class="quiz-option" data-index="0">ArrayList::new</div>
<div class="quiz-option" data-index="1">ArrayList::create</div>
<div class="quiz-option" data-index="2">new::ArrayList</div>
<div class="quiz-option" data-index="3">ArrayList.new()</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 95. Сколько видов ссылок на методы существует в Java?</h4>
<div class="quiz-option" data-index="0">Два</div>
<div class="quiz-option" data-index="1">Три</div>
<div class="quiz-option" data-index="2">Пять</div>
<div class="quiz-option" data-index="3">Четыре</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 96. Когда следует использовать ссылку на метод вместо лямбды?</h4>
<div class="quiz-option" data-index="0">Всегда — ссылки на методы лучше</div>
<div class="quiz-option" data-index="1">Когда лямбда содержит сложную логику</div>
<div class="quiz-option" data-index="2">Когда лямбда просто вызывает существующий метод без дополнительной логики</div>
<div class="quiz-option" data-index="3">Только для статических методов</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== ЧАСТЬ 13-15: ПАКЕТЫ И МОДУЛИ (97-100) ===== -->

<div class="quiz-question" data-correct="1">
<h4>Вопрос 97. Для чего используется ключевое слово <code>package</code>?</h4>
<div class="quiz-option" data-index="0">Для импорта классов из другого пакета</div>
<div class="quiz-option" data-index="1">Для указания, к какому пакету принадлежит класс</div>
<div class="quiz-option" data-index="2">Для создания JAR-архива</div>
<div class="quiz-option" data-index="3">Для объявления модуля</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 98. Что соответствует имени пакета на файловой системе?</h4>
<div class="quiz-option" data-index="0">Структура каталогов (lecture.two.classes → lecture/two/classes/)</div>
<div class="quiz-option" data-index="1">Имя JAR-файла</div>
<div class="quiz-option" data-index="2">Имя модуля</div>
<div class="quiz-option" data-index="3">Ничего — имя произвольное</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 99. В какой версии Java появилась модульная система JPMS?</h4>
<div class="quiz-option" data-index="0">Java 8</div>
<div class="quiz-option" data-index="1">Java 11</div>
<div class="quiz-option" data-index="2">Java 17</div>
<div class="quiz-option" data-index="3">Java 9</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 100. Как называется файл-дескриптор модуля в Java?</h4>
<div class="quiz-option" data-index="0">module.xml</div>
<div class="quiz-option" data-index="1">module-descriptor.java</div>
<div class="quiz-option" data-index="2">module-info.java</div>
<div class="quiz-option" data-index="3">META-INF/module.java</div>
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
    'Вопрос 1': 'Класс — это шаблон (чертёж), по которому создаются объекты. Из одного класса можно создать множество объектов.',
    'Вопрос 2': 'Java поддерживает одиночное наследование классов — через extends можно унаследовать только один класс.',
    'Вопрос 3': 'Статический блок (static { ... }) выполняется один раз при первой загрузке класса в память JVM.',
    'Вопрос 4': 'Поле экземпляра принадлежит каждому объекту отдельно, статическое поле — одно на весь класс.',
    'Вопрос 5': 'private — самый строгий модификатор: поле/метод доступны только внутри класса, где объявлены.',
    'Вопрос 6': 'Без модификатора — package-private: доступ только внутри своего пакета. Это НЕ то же самое, что public!',
    'Вопрос 7': 'Блок инициализации экземпляра { ... } выполняется при каждом создании объекта, перед конструктором.',
    'Вопрос 8': 'static final объявляет константу класса — неизменяемое значение, общее для всех объектов.',
    'Вопрос 9': 'var доступен только для локальных переменных и обязательно с инициализацией. Не для полей, параметров или возвращаемых типов.',
    'Вопрос 10': 'var — это выведение типа (type inference): тип определяется компилятором и фиксируется. Переменная не может менять тип.',
    'Вопрос 11': 'Нельзя создать экземпляр абстрактного класса через new. Нужно создать подкласс, реализующий все абстрактные методы.',
    'Вопрос 12': 'Абстрактный класс может содержать и обычные методы с реализацией (sleep()), и абстрактные (makeSound()).',
    'Вопрос 13': 'Абстрактный класс может иметь конструктор, который вызывается через super() из подклассов.',
    'Вопрос 14': 'Подкласс обязан реализовать все абстрактные методы, иначе сам должен быть объявлен abstract.',
    'Вопрос 15': 'Полиморфизм: переменная типа Animal может хранить Dog или Bird, а вызываемый метод определяется типом объекта.',
    'Вопрос 16': 'Circle наследует Shape, поэтому объект Circle является и Shape. Оператор instanceof возвращает true.',
    'Вопрос 17': 'Абстрактные классы, как и обычные, могут содержать поля, конструкторы и методы с реализацией.',
    'Вопрос 18': 'sealed ограничивает наследников через permits, в отличие от final (полный запрет) и обычного класса (без ограничений).',
    'Вопрос 19': 'Каждый наследник sealed-класса обязан быть: final (цепочка заканчивается), sealed (сам ограничивает) или non-sealed (ограничение снимается).',
    'Вопрос 20': 'non-sealed снимает ограничение: любой класс может наследовать дальше от этого наследника.',
    'Вопрос 21': 'Sealed-классы стали стабильной функцией в Java 17 (превью — с Java 15).',
    'Вопрос 22': 'Record неявно является final, поэтому удовлетворяет требованию sealed-типа к наследникам. На практике record чаще реализует sealed-интерфейс, так как не может наследовать другие классы (неявно расширяет java.lang.Record).',
    'Вопрос 23': 'Поля интерфейса — только public static final (константы). Нестатических полей быть не может.',
    'Вопрос 24': 'Класс может реализовать любое количество интерфейсов через implements, разделяя запятой.',
    'Вопрос 25': 'Default-метод (Java 8+) — метод с реализацией по умолчанию в интерфейсе. Класс может его переопределить.',
    'Вопрос 26': 'Статические методы интерфейса вызываются напрямую: Movable.info(). Их нельзя вызвать через экземпляр.',
    'Вопрос 27': 'Private-методы в интерфейсах появились в Java 9. Они используются для внутренней логики default-методов.',
    'Вопрос 28': 'Маркерный интерфейс — пустой интерфейс (без методов), отмечающий класс. Примеры: Serializable, Cloneable.',
    'Вопрос 29': 'Функциональный интерфейс содержит ровно один абстрактный метод. @FunctionalInterface — рекомендация, не обязательна.',
    'Вопрос 30': 'Интерфейс может наследовать несколько интерфейсов через extends (не implements).',
    'Вопрос 31': 'Интерфейс — для контракта «умеет» (Robot умеет двигаться). Абстрактный класс — для «является» (Dog является Animal).',
    'Вопрос 32': 'Интерфейсы не хранят состояние: все поля — public static final. Для состояния используйте абстрактные классы.',
    'Вопрос 33': 'Методы интерфейса по умолчанию public abstract. Указывать эти модификаторы явно необязательно.',
    'Вопрос 34': 'Интерфейсы не могут содержать конструкторы. Это одно из ключевых отличий от абстрактных классов.',
    'Вопрос 35': 'Индексация массивов в Java начинается с 0. Последний элемент имеет индекс length - 1.',
    'Вопрос 36': 'Размер массива фиксирован при создании. Для динамического размера используйте ArrayList.',
    'Вопрос 37': 'arr.length — это размер массива. Допустимые индексы: 0..length-1. Обращение к arr[length] вызовет ArrayIndexOutOfBoundsException.',
    'Вопрос 38': 'Зубчатый (jagged) массив — массив массивов с разной длиной строк. Каждая строка — отдельный объект.',
    'Вопрос 39': 'Элементы массива ссылочного типа (String, Object и т.д.) по умолчанию равны null.',
    'Вопрос 40': 'Java-стиль (int[] numbers) рекомендуется, т.к. тип «массив целых чисел» читается слитно.',
    'Вопрос 41': 'Массивы хранятся в непрерывной области памяти, поэтому доступ по индексу — O(1).',
    'Вопрос 42': 'Элементы String[] по умолчанию null. Вызов метода на null вызовет NullPointerException.',
    'Вопрос 43': 'String — immutable. Любая «модификация» создаёт новый объект. Для частых изменений — StringBuilder.',
    'Вопрос 44': 'toUpperCase() не изменяет строку, а возвращает новую. Результат не сохранён, поэтому s остаётся "hello".',
    'Вопрос 45': 'String Pool — область в Heap для уникальных литералов. Если "Hello" встречается 100 раз — объект один.',
    'Вопрос 46': 's1 и s2 — литералы, указывают на один объект в Pool (true). s3 создан через new — другой объект (false).',
    'Вопрос 47': 'intern() помещает строку в String Pool или возвращает ссылку на уже существующую в Pool.',
    'Вопрос 48': 'Компилятор объединяет литералы "Hel" + "lo" в один "Hello" на этапе компиляции. Обе переменные указывают на один объект в Pool.',
    'Вопрос 49': 'Конкатенация с переменной происходит в runtime и создаёт объект в обычной куче, не в Pool.',
    'Вопрос 50': 'StringBuilder — быстрее (не потокобезопасен). StringBuffer — потокобезопасен (synchronized), но медленнее.',
    'Вопрос 51': 'String неизменяем: каждая += создаёт новый объект. В цикле на 10000 итераций — ~10000 промежуточных объектов.',
    'Вопрос 52': 'substring(1, 3) возвращает символы с индекса 1 до 3 (не включая): "av".',
    'Вопрос 53': 'Текстовые блоки (тройные кавычки """) стали стабильной функцией в Java 15.',
    'Вопрос 54': 'isEmpty() — длина == 0. isBlank() (Java 11+) — пусто или только пробельные символы.',
    'Вопрос 55': 'Record автоматически генерирует: публичный конструктор, геттеры (name(), age()), equals(), hashCode(), toString().',
    'Вопрос 56': 'Record не может наследоваться от других классов, но может реализовать интерфейсы.',
    'Вопрос 57': 'Геттеры record совпадают с именами полей: name(), age(). Не getИмяПоля(), как в обычных классах.',
    'Вопрос 58': 'Компактный конструктор — public Person { ... } (без скобок). Присваивание полей происходит автоматически.',
    'Вопрос 59': 'equals() в record автоматически сравнивает все поля. Одинаковые значения → true.',
    'Вопрос 60': 'Record может реализовать интерфейсы. Например: record Person(...) implements Comparable<Person>.',
    'Вопрос 61': 'В компактном конструкторе присваивание полей (this.name = name) происходит автоматически после тела конструктора.',
    'Вопрос 62': 'Enum — фиксированный набор именованных констант. Каждая константа — объект класса enum.',
    'Вопрос 63': 'values() возвращает массив всех констант перечисления в порядке объявления.',
    'Вопрос 64': 'ordinal() возвращает порядковый номер с 0. RED объявлен первым, значит ordinal() == 0.',
    'Вопрос 65': 'Enum неявно расширяет java.lang.Enum, а Java не поддерживает множественное наследование классов.',
    'Вопрос 66': 'Enum может содержать абстрактные методы. Каждая константа обязана предоставить свою реализацию.',
    'Вопрос 67': 'EnumSet реализован через битовый вектор (long) — O(1) операции, минимум памяти.',
    'Вопрос 68': 'EnumMap использует массив, индексированный по ordinal(). Это быстрее и компактнее HashMap.',
    'Вопрос 69': 'valueOf() возвращает константу enum по её строковому имени. При несовпадении — IllegalArgumentException.',
    'Вопрос 70': 'Аннотация добавляет метаданные, не влияя на поведение напрямую. Используется компилятором, фреймворками или Reflection.',
    'Вопрос 71': 'RUNTIME — аннотация сохраняется в .class и доступна через Reflection во время выполнения.',
    'Вопрос 72': '@Override проверяет при компиляции, что метод переопределяет родительский. Если нет — ошибка компиляции.',
    'Вопрос 73': '@Target указывает, к каким элементам кода применима аннотация: METHOD, FIELD, TYPE, PARAMETER и др.',
    'Вопрос 74': '@FunctionalInterface — проверяет (но не обязателен), что интерфейс содержит ровно один абстрактный метод.',
    'Вопрос 75': 'SOURCE — аннотация существует только в .java файле. В .class не попадает. Пример: @SuppressWarnings.',
    'Вопрос 76': 'Анонимный класс не имеет имени. Он создаётся и инстанцируется в одном выражении через new Интерфейс() { ... }.',
    'Вопрос 77': 'Анонимный класс может использовать только final или effectively final переменные из окружающего метода.',
    'Вопрос 78': 'При конфликте имён: ВнешнийКласс.this.поле обращается к полю внешнего класса.',
    'Вопрос 79': 'Анонимный класс может наследовать один класс ИЛИ реализовать один интерфейс, но не оба.',
    'Вопрос 80': 'Локальный класс имеет имя и может создавать несколько экземпляров в пределах метода. Анонимный — одноразовый. Локальный класс виден только в том блоке, где объявлен, а не во всём внешнем классе.',
    'Вопрос 81': 'Локальный класс объявляется внутри метода, конструктора или блока. Виден только в этой области.',
    'Вопрос 82': 'В статическом методе нет экземпляра внешнего класса, поэтому доступны только static-члены.',
    'Вопрос 83': 'Лямбда — компактная запись анонимной функции, реализующей функциональный интерфейс (интерфейс с одним абстрактным методом).',
    'Вопрос 84': 'Predicate<T> — метод test(T) возвращает boolean. Пример: Predicate<String> isEmpty = s -> s.isEmpty();',
    'Вопрос 85': 'Supplier<T> — метод get() без аргументов, возвращает T. Runnable тоже без аргументов, но возвращает void.',
    'Вопрос 86': 'Consumer<T> — метод accept(T) принимает аргумент и ничего не возвращает (void).',
    'Вопрос 87': 'Function<String, Integer> преобразует String в Integer. "Java".length() == 4.',
    'Вопрос 88': 'В лямбде this указывает на объект внешнего класса, а не на саму лямбду (в отличие от анонимного класса).',
    'Вопрос 89': 'Лямбда может захватывать только final/effectively final переменные. Изменяемые — нельзя.',
    'Вопрос 90': 'BinaryOperator<T> принимает два аргумента типа T и возвращает T. Это специализация BiFunction<T, T, T>.',
    'Вопрос 91': 'Runnable не принимает аргументов: () -> { тело }. Стрелка -> (не =>), скобки () обязательны.',
    'Вопрос 92': 'String::toUpperCase — ссылка на метод экземпляра по типу. Эквивалент: s -> s.toUpperCase().',
    'Вопрос 93': 'Math::max — ссылка на статический метод. Двойное двоеточие :: без скобок и аргументов.',
    'Вопрос 94': 'ArrayList::new — ссылка на конструктор. Эквивалент: () -> new ArrayList<>().',
    'Вопрос 95': 'Четыре вида: static (Math::max), конкретный объект (obj::method), по типу (String::toUpperCase), конструктор (Cls::new).',
    'Вопрос 96': 'Ссылку на метод используют, когда лямбда просто делегирует вызов. При дополнительной логике — оставляйте лямбду.',
    'Вопрос 97': 'package указывается в начале файла и определяет принадлежность класса к пакету.',
    'Вопрос 98': 'Имя пакета соответствует структуре каталогов: lecture.two.classes → папка lecture/two/classes/.',
    'Вопрос 99': 'JPMS (Java Platform Module System) появилась в Java 9 как Project Jigsaw.',
    'Вопрос 100': 'module-info.java — дескриптор модуля, находится в корне исходного кода модуля.'
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
    else scoreDetail.textContent = 'Нужно повторить материал лекции.';

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
