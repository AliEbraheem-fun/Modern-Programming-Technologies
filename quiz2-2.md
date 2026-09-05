# Тест 2.2: Основные конструкции языка Java — Часть 2 (Лекция 2)

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

<!-- ===== ВОПРОСЫ 1-5: МОДУЛИ И ПАКЕТЫ ===== -->

<div class="quiz-question" data-correct="1">
<h4>Вопрос 1. Что делает директива <code>exports</code> в module-info.java?</h4>
<div class="quiz-option" data-index="0">Импортирует пакет из другого модуля</div>
<div class="quiz-option" data-index="1">Делает пакет доступным для других модулей</div>
<div class="quiz-option" data-index="2">Открывает пакет для рефлексии</div>
<div class="quiz-option" data-index="3">Удаляет пакет из модуля</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 2. Что делает директива <code>requires</code> в module-info.java?</h4>
<div class="quiz-option" data-index="0">Указывает зависимость от другого модуля</div>
<div class="quiz-option" data-index="1">Экспортирует пакет</div>
<div class="quiz-option" data-index="2">Открывает пакет для рефлексии</div>
<div class="quiz-option" data-index="3">Объявляет сервис</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 3. Что делает директива <code>opens</code> в module-info.java?</h4>
<div class="quiz-option" data-index="0">Экспортирует пакет для компиляции</div>
<div class="quiz-option" data-index="1">Указывает зависимость от другого модуля</div>
<div class="quiz-option" data-index="2">Делает модуль публичным</div>
<div class="quiz-option" data-index="3">Открывает пакет для рефлексии во время выполнения</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 4. Какую проблему JPMS решает в отношении classpath?</h4>
<div class="quiz-option" data-index="0">Ускоряет компиляцию</div>
<div class="quiz-option" data-index="1">Удаляет неиспользуемые классы</div>
<div class="quiz-option" data-index="2">JAR-Hell — конфликты библиотек с одноимёнными классами</div>
<div class="quiz-option" data-index="3">Автоматически загружает зависимости из интернета</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 5. Для чего используется файл <code>package-info.java</code>?</h4>
<div class="quiz-option" data-index="0">Для объявления модуля</div>
<div class="quiz-option" data-index="1">Для документирования и аннотирования пакета</div>
<div class="quiz-option" data-index="2">Для указания зависимостей пакета</div>
<div class="quiz-option" data-index="3">Для настройки компилятора</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== СМЕШАННЫЕ/КОМПЛЕКСНЫЕ ВОПРОСЫ (6-10) ===== -->

<div class="quiz-question" data-correct="0">
<h4>Вопрос 6. Какой результат вызова <code>String.join("-", "A", "B", "C")</code>?</h4>
<div class="quiz-option" data-index="0">"A-B-C"</div>
<div class="quiz-option" data-index="1">"-A-B-C-"</div>
<div class="quiz-option" data-index="2">"ABC-"</div>
<div class="quiz-option" data-index="3">"A B C"</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 7. Что такое <code>protected</code> модификатор доступа?</h4>
<div class="quiz-option" data-index="0">Доступ только внутри класса</div>
<div class="quiz-option" data-index="1">Доступ только внутри пакета</div>
<div class="quiz-option" data-index="2">Доступ отовсюду</div>
<div class="quiz-option" data-index="3">Доступ внутри пакета и в подклассах из других пакетов</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 8. Что произойдёт при конфликте default-методов из двух интерфейсов?</h4>
<div class="quiz-option" data-index="0">Компилятор выберет метод из первого интерфейса</div>
<div class="quiz-option" data-index="1">Класс обязан переопределить конфликтующий метод</div>
<div class="quiz-option" data-index="2">Ошибка времени выполнения</div>
<div class="quiz-option" data-index="3">Оба метода будут доступны</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 9. Что выведет <code>"Ha".repeat(3)</code>?</h4>
<div class="quiz-option" data-index="0">"Ha 3"</div>
<div class="quiz-option" data-index="1">"Ha3"</div>
<div class="quiz-option" data-index="2">"HaHaHa"</div>
<div class="quiz-option" data-index="3">"Ha, Ha, Ha"</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 10. Какое ключевое различие между вложенным static-классом и внутренним (non-static) классом?</h4>
<div class="quiz-option" data-index="0">Static-класс не имеет неявной ссылки на внешний объект и не требует его экземпляра</div>
<div class="quiz-option" data-index="1">Static-класс не может иметь методов</div>
<div class="quiz-option" data-index="2">Внутренний класс не может обращаться к полям внешнего</div>
<div class="quiz-option" data-index="3">Ничем — это одно и то же</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== УГЛУБЛЁННЫЕ ВОПРОСЫ: КЛАССЫ И ИНИЦИАЛИЗАЦИЯ (11-20) ===== -->

<div class="quiz-question" data-correct="3">
<h4>Вопрос 11. В каком порядке выполняются блоки при создании объекта?</h4>
<div class="quiz-option" data-index="0">Конструктор → статический блок → блок экземпляра</div>
<div class="quiz-option" data-index="1">Блок экземпляра → конструктор → статический блок</div>
<div class="quiz-option" data-index="2">Конструктор → блок экземпляра → статический блок</div>
<div class="quiz-option" data-index="3">Статический блок (при первой загрузке) → блок экземпляра → конструктор</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 12. Что выведет этот код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
class Demo {
    static { System.out.print("A "); }
    { System.out.print("B "); }
    Demo() { System.out.print("C "); }
}
new Demo(); new Demo();
```

<div class="quiz-option" data-index="0">A B C A B C</div>
<div class="quiz-option" data-index="1">A B C B C</div>
<div class="quiz-option" data-index="2">B C B C A</div>
<div class="quiz-option" data-index="3">A A B C B C</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 13. Что делает ключевое слово <code>this</code> в конструкторе?</h4>
<div class="quiz-option" data-index="0">Ссылается на текущий объект и позволяет различать поле и параметр с одинаковым именем</div>
<div class="quiz-option" data-index="1">Вызывает конструктор родительского класса</div>
<div class="quiz-option" data-index="2">Создаёт новый экземпляр класса</div>
<div class="quiz-option" data-index="3">Возвращает значение из конструктора</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 14. Можно ли обратиться к статическому полю через экземпляр объекта?</h4>
<div class="quiz-option" data-index="0">Нет, только через имя класса</div>
<div class="quiz-option" data-index="1">Нет, это вызовет ошибку компиляции</div>
<div class="quiz-option" data-index="2">Да, но это плохая практика — рекомендуется обращаться через имя класса</div>
<div class="quiz-option" data-index="3">Да, и это рекомендуемый способ</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 15. Какой модификатор виден в подклассах из других пакетов, но не виден обычным классам других пакетов?</h4>
<div class="quiz-option" data-index="0">default (package-private)</div>
<div class="quiz-option" data-index="1">protected</div>
<div class="quiz-option" data-index="2">private</div>
<div class="quiz-option" data-index="3">public</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 16. Что произойдёт при компиляции? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
var x;
x = 10;
```

<div class="quiz-option" data-index="0">Код скомпилируется, x будет int</div>
<div class="quiz-option" data-index="1">Код скомпилируется, x будет Object</div>
<div class="quiz-option" data-index="2">Ошибка выполнения</div>
<div class="quiz-option" data-index="3">Ошибка компиляции — var требует инициализации при объявлении</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 17. Может ли статический метод обращаться к полям экземпляра?</h4>
<div class="quiz-option" data-index="0">Нет, статический метод не имеет доступа к нестатическим полям</div>
<div class="quiz-option" data-index="1">Да, без ограничений</div>
<div class="quiz-option" data-index="2">Только к public-полям экземпляра</div>
<div class="quiz-option" data-index="3">Только через this</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 18. Что означает объявление <code>public static int deviceCount = 0;</code> в контексте класса?</h4>
<div class="quiz-option" data-index="0">Каждый объект будет иметь свою копию deviceCount</div>
<div class="quiz-option" data-index="1">Поле нельзя изменить после инициализации</div>
<div class="quiz-option" data-index="2">Поле общее для всех объектов — одна переменная на весь класс</div>
<div class="quiz-option" data-index="3">Поле доступно только через методы-геттеры</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 19. Для чего нужны геттеры и сеттеры?</h4>
<div class="quiz-option" data-index="0">Для увеличения производительности программы</div>
<div class="quiz-option" data-index="1">Для инкапсуляции — контролируемого доступа к private-полям</div>
<div class="quiz-option" data-index="2">Для вызова конструктора</div>
<div class="quiz-option" data-index="3">Для объявления статических полей</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 20. Может ли абстрактный класс реализовать интерфейс, не реализуя все его методы?</h4>
<div class="quiz-option" data-index="0">Нет, обязан реализовать все методы</div>
<div class="quiz-option" data-index="1">Нет, это вызовет ошибку компиляции</div>
<div class="quiz-option" data-index="2">Только если интерфейс маркерный</div>
<div class="quiz-option" data-index="3">Да, нереализованные методы остаются абстрактными для подклассов</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== УГЛУБЛЁННЫЕ ВОПРОСЫ: ИНТЕРФЕЙСЫ И АБСТРАКЦИИ (21-32) ===== -->

<div class="quiz-question" data-correct="0">
<h4>Вопрос 21. Может ли абстрактный класс не содержать ни одного абстрактного метода?</h4>
<div class="quiz-option" data-index="0">Да, это допустимо — abstract просто запрещает создание экземпляра</div>
<div class="quiz-option" data-index="1">Нет, абстрактный класс обязан иметь хотя бы один абстрактный метод</div>
<div class="quiz-option" data-index="2">Да, но тогда он автоматически становится обычным классом</div>
<div class="quiz-option" data-index="3">Нет, компилятор выдаст ошибку</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 22. Что произойдёт, если два интерфейса имеют одинаковый default-метод, и класс реализует оба?</h4>
<div class="quiz-option" data-index="0">Компилятор выберет метод из первого интерфейса</div>
<div class="quiz-option" data-index="1">Оба метода будут доступны через разные имена</div>
<div class="quiz-option" data-index="2">Ошибка компиляции — класс обязан переопределить конфликтующий метод</div>
<div class="quiz-option" data-index="3">Ошибка времени выполнения</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 23. Зачем нужны private-методы в интерфейсе (Java 9+)?</h4>
<div class="quiz-option" data-index="0">Для реализации в классах</div>
<div class="quiz-option" data-index="1">Для выноса общей логики из нескольких default-методов без раскрытия наружу</div>
<div class="quiz-option" data-index="2">Для создания конструкторов интерфейса</div>
<div class="quiz-option" data-index="3">Для обращения к полям экземпляра</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 24. Можно ли изменить значение поля интерфейса? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
interface Config { int MAX = 100; }
Config.MAX = 200;
```

<div class="quiz-option" data-index="0">Да, значение изменится на 200</div>
<div class="quiz-option" data-index="1">Да, но только из класса, реализующего интерфейс</div>
<div class="quiz-option" data-index="2">Да, через рефлексию</div>
<div class="quiz-option" data-index="3">Нет — поля интерфейса неявно public static final (константы)</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 25. Может ли default-метод интерфейса вызвать абстрактный метод того же интерфейса?</h4>
<div class="quiz-option" data-index="0">Да, абстрактный метод будет реализован в классе, и вызов сработает</div>
<div class="quiz-option" data-index="1">Нет, default-метод не знает о других методах интерфейса</div>
<div class="quiz-option" data-index="2">Только через super</div>
<div class="quiz-option" data-index="3">Нет, это вызовет StackOverflowError</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 26. Чем sealed-интерфейс отличается от sealed-класса?</h4>
<div class="quiz-option" data-index="0">sealed нельзя применять к интерфейсам</div>
<div class="quiz-option" data-index="1">sealed-интерфейс не может иметь default-методы</div>
<div class="quiz-option" data-index="2">sealed-интерфейс ограничивает, какие классы/интерфейсы могут его реализовать/расширить</div>
<div class="quiz-option" data-index="3">Ничем — они работают одинаково</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 27. Какое преимущество даёт sealed-класс при использовании <code>switch</code> (Java 21+)?</h4>
<div class="quiz-option" data-index="0">switch работает быстрее</div>
<div class="quiz-option" data-index="1">Компилятор проверяет, что учтены все наследники — default не нужен</div>
<div class="quiz-option" data-index="2">switch автоматически вызывает нужный метод</div>
<div class="quiz-option" data-index="3">switch может принимать несколько аргументов</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 28. Что такое «отношение "является"» vs «отношение "умеет"» при выборе между абстрактным классом и интерфейсом?</h4>
<div class="quiz-option" data-index="0">«является» (Dog IS-A Animal) → абстрактный класс; «умеет» (Robot CAN Move) → интерфейс</div>
<div class="quiz-option" data-index="1">«является» → интерфейс; «умеет» → абстрактный класс</div>
<div class="quiz-option" data-index="2">Оба отношения подходят для интерфейсов</div>
<div class="quiz-option" data-index="3">Оба отношения подходят для абстрактных классов</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 29. Что такое effectively final переменная?</h4>
<div class="quiz-option" data-index="0">Переменная, объявленная с ключевым словом final</div>
<div class="quiz-option" data-index="1">Статическая константа</div>
<div class="quiz-option" data-index="2">Поле класса, которое не меняется</div>
<div class="quiz-option" data-index="3">Локальная переменная, значение которой не изменяется после инициализации (даже без ключевого слова final)</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 30. Может ли аннотация <code>@FunctionalInterface</code> быть применена к интерфейсу с несколькими default-методами?</h4>
<div class="quiz-option" data-index="0">Нет, допускается только один метод любого вида</div>
<div class="quiz-option" data-index="1">Нет, default-методы считаются абстрактными</div>
<div class="quiz-option" data-index="2">Да, если абстрактный метод ровно один — default-методы не считаются</div>
<div class="quiz-option" data-index="3">Только если default-методов не более двух</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 31. Какой пример является маркерным интерфейсом из стандартной библиотеки Java?</h4>
<div class="quiz-option" data-index="0">Comparable</div>
<div class="quiz-option" data-index="1">Serializable</div>
<div class="quiz-option" data-index="2">Runnable</div>
<div class="quiz-option" data-index="3">Iterable</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 32. Может ли абстрактный класс быть <code>final</code>?</h4>
<div class="quiz-option" data-index="0">Нет — abstract требует наследования, а final запрещает. Это противоречие.</div>
<div class="quiz-option" data-index="1">Да, это создаёт класс-синглтон</div>
<div class="quiz-option" data-index="2">Да, но только если все методы реализованы</div>
<div class="quiz-option" data-index="3">Да, это стандартная практика</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== УГЛУБЛЁННЫЕ ВОПРОСЫ: МАССИВЫ (33-38) ===== -->

<div class="quiz-question" data-correct="2">
<h4>Вопрос 33. Что произойдёт при выполнении этого кода? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
int[] arr = {1, 2, 3};
int[] arr2 = arr;
arr2[0] = 99;
System.out.println(arr[0]);
```

<div class="quiz-option" data-index="0">1 — массивы копируются при присваивании</div>
<div class="quiz-option" data-index="1">Ошибка компиляции</div>
<div class="quiz-option" data-index="2">99 — arr и arr2 ссылаются на один массив</div>
<div class="quiz-option" data-index="3">0 — значение сбрасывается</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 34. Какое значение по умолчанию у элементов <code>int[] arr = new int[5]</code>? <span class="jshell-hint">Попробуй в jshell!</span></h4>
<div class="quiz-option" data-index="0">Случайное число</div>
<div class="quiz-option" data-index="1">0</div>
<div class="quiz-option" data-index="2">null</div>
<div class="quiz-option" data-index="3">-1</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 35. Какое значение по умолчанию у элементов <code>boolean[] flags = new boolean[3]</code>? <span class="jshell-hint">Попробуй в jshell!</span></h4>
<div class="quiz-option" data-index="0">true</div>
<div class="quiz-option" data-index="1">null</div>
<div class="quiz-option" data-index="2">0</div>
<div class="quiz-option" data-index="3">false</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 36. Как узнать длину второй строки зубчатого массива <code>int[][] jagged</code>?</h4>
<div class="quiz-option" data-index="0">jagged[1].length</div>
<div class="quiz-option" data-index="1">jagged.length[1]</div>
<div class="quiz-option" data-index="2">jagged.length(1)</div>
<div class="quiz-option" data-index="3">jagged.rowLength(1)</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 37. Является ли массив в Java объектом?</h4>
<div class="quiz-option" data-index="0">Нет, это примитивная структура данных</div>
<div class="quiz-option" data-index="1">Только массивы объектов (String[], Object[])</div>
<div class="quiz-option" data-index="2">Да, все массивы являются объектами с полем .length</div>
<div class="quiz-option" data-index="3">Зависит от типа элементов</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 38. Какой цикл рекомендуется для простого перебора всех элементов массива?</h4>
<div class="quiz-option" data-index="0">while</div>
<div class="quiz-option" data-index="1">for-each (for (тип x : массив))</div>
<div class="quiz-option" data-index="2">do-while</div>
<div class="quiz-option" data-index="3">Рекурсивный обход</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== УГЛУБЛЁННЫЕ ВОПРОСЫ: СТРОКИ (39-50) ===== -->

<div class="quiz-question" data-correct="3">
<h4>Вопрос 39. Что выведет этот код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
String s1 = "Test";
String s3 = new String("Test");
String s5 = s3.intern();
System.out.println(s1 == s5);
```

<div class="quiz-option" data-index="0">false — разные объекты</div>
<div class="quiz-option" data-index="1">Ошибка компиляции</div>
<div class="quiz-option" data-index="2">Зависит от JVM</div>
<div class="quiz-option" data-index="3">true — intern() вернул ссылку на объект из Pool, где уже есть "Test"</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 40. Что вернёт <code>"Java".indexOf("a")</code>? <span class="jshell-hint">Попробуй в jshell!</span></h4>
<div class="quiz-option" data-index="0">1</div>
<div class="quiz-option" data-index="1">2</div>
<div class="quiz-option" data-index="2">3</div>
<div class="quiz-option" data-index="3">0</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 41. Что вернёт <code>"Java".lastIndexOf("a")</code>? <span class="jshell-hint">Попробуй в jshell!</span></h4>
<div class="quiz-option" data-index="0">0</div>
<div class="quiz-option" data-index="1">1</div>
<div class="quiz-option" data-index="2">3</div>
<div class="quiz-option" data-index="3">4</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 42. Что произойдёт при выполнении? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
String s = null;
s.length();
```

<div class="quiz-option" data-index="0">Вернётся 0</div>
<div class="quiz-option" data-index="1">NullPointerException</div>
<div class="quiz-option" data-index="2">Ошибка компиляции</div>
<div class="quiz-option" data-index="3">Вернётся null</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 43. Что вернёт <code>"Java".equalsIgnoreCase("java")</code>? <span class="jshell-hint">Попробуй в jshell!</span></h4>
<div class="quiz-option" data-index="0">true</div>
<div class="quiz-option" data-index="1">false</div>
<div class="quiz-option" data-index="2">Ошибка компиляции</div>
<div class="quiz-option" data-index="3">"java"</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 44. Чему равен результат <code>"Hello".replace("l", "r")</code>? <span class="jshell-hint">Попробуй в jshell!</span></h4>
<div class="quiz-option" data-index="0">"Herlo"</div>
<div class="quiz-option" data-index="1">"Hello" — строка не изменится</div>
<div class="quiz-option" data-index="2">"Herro" — но только первое вхождение</div>
<div class="quiz-option" data-index="3">"Herro" — заменяются все вхождения</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 45. Как правильно создать строку из массива символов?</h4>
<div class="quiz-option" data-index="0">String.valueOf(charArray).toString()</div>
<div class="quiz-option" data-index="1">charArray.toString()</div>
<div class="quiz-option" data-index="2">new String(charArray)</div>
<div class="quiz-option" data-index="3">(String) charArray</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 46. Как безопасно сравнить строку с null?</h4>
<div class="quiz-option" data-index="0">s.equals(null) — всегда безопасно</div>
<div class="quiz-option" data-index="1">s == null — оператор == безопасен для проверки null</div>
<div class="quiz-option" data-index="2">null.equals(s) — вызов на null допустим</div>
<div class="quiz-option" data-index="3">s.compareTo(null) == 0</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 47. Какой метод StringBuilder позволяет добавлять текст?</h4>
<div class="quiz-option" data-index="0">append()</div>
<div class="quiz-option" data-index="1">add()</div>
<div class="quiz-option" data-index="2">concat()</div>
<div class="quiz-option" data-index="3">push()</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 48. Что особенного в текстовых блоках (text blocks)?</h4>
<div class="quiz-option" data-index="0">Они изменяемые, в отличие от обычных строк</div>
<div class="quiz-option" data-index="1">Они хранятся вне String Pool</div>
<div class="quiz-option" data-index="2">Они поддерживают только ASCII-символы</div>
<div class="quiz-option" data-index="3">Они могут содержать переносы строк, кавычки и табуляции без экранирования</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 49. Что вернёт <code>"  пробелы  ".trim()</code>? <span class="jshell-hint">Попробуй в jshell!</span></h4>
<div class="quiz-option" data-index="0">"  пробелы  " — trim не работает с кириллицей</div>
<div class="quiz-option" data-index="1">"пробелы  " — удаляет только ведущие пробелы</div>
<div class="quiz-option" data-index="2">"пробелы" — удаляет пробелы с обоих концов</div>
<div class="quiz-option" data-index="3">"пробелы" — удаляет все пробелы, включая внутренние</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 50. Можно ли вызвать метод StringBuilder по цепочке (chaining)? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
var sb = new StringBuilder("Hello");
sb.append(" ").append("World").append("!");
```

<div class="quiz-option" data-index="0">Нет, каждый вызов нужно делать отдельной строкой</div>
<div class="quiz-option" data-index="1">Да, append() возвращает тот же StringBuilder</div>
<div class="quiz-option" data-index="2">Да, но только для append()</div>
<div class="quiz-option" data-index="3">Нет, это вызовет ошибку компиляции</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== УГЛУБЛЁННЫЕ ВОПРОСЫ: RECORDS И ENUMS (51-60) ===== -->

<div class="quiz-question" data-correct="0">
<h4>Вопрос 51. Можно ли добавить собственные поля экземпляра в record?</h4>
<div class="quiz-option" data-index="0">Нет, record может содержать только поля, объявленные в заголовке</div>
<div class="quiz-option" data-index="1">Да, как в обычном классе</div>
<div class="quiz-option" data-index="2">Только static поля</div>
<div class="quiz-option" data-index="3">Только transient-поля</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 52. Можно ли добавить статические поля и методы в record?</h4>
<div class="quiz-option" data-index="0">Нет, record не поддерживает статические члены</div>
<div class="quiz-option" data-index="1">Только static final</div>
<div class="quiz-option" data-index="2">Только статические методы, не поля</div>
<div class="quiz-option" data-index="3">Да, можно добавлять статические поля и методы</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 53. Что произойдёт в компактном конструкторе record при выбросе исключения? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
record Age(int value) {
    Age {
        if (value < 0) throw new IllegalArgumentException("Отрицательный возраст");
    }
}
new Age(-5);
```

<div class="quiz-option" data-index="0">Объект будет создан с value = 0</div>
<div class="quiz-option" data-index="1">Объект будет создан с value = -5</div>
<div class="quiz-option" data-index="2">IllegalArgumentException — объект не будет создан</div>
<div class="quiz-option" data-index="3">Ошибка компиляции</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 54. Можно ли сравнивать константы enum через <code>==</code>?</h4>
<div class="quiz-option" data-index="0">Нет, нужно использовать .equals()</div>
<div class="quiz-option" data-index="1">Да, == безопасен для enum, т.к. каждая константа — единственный экземпляр</div>
<div class="quiz-option" data-index="2">Только для простых enum без полей</div>
<div class="quiz-option" data-index="3">Зависит от JVM</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 55. Какой модификатор имеет конструктор enum?</h4>
<div class="quiz-option" data-index="0">Всегда private (явно или неявно)</div>
<div class="quiz-option" data-index="1">public</div>
<div class="quiz-option" data-index="2">protected</div>
<div class="quiz-option" data-index="3">Любой модификатор</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 56. Что произойдёт при вызове <code>Direction.valueOf("NORTH_EAST")</code>, если такой константы нет?</h4>
<div class="quiz-option" data-index="0">Вернётся null</div>
<div class="quiz-option" data-index="1">Вернётся первая константа</div>
<div class="quiz-option" data-index="2">Ошибка компиляции</div>
<div class="quiz-option" data-index="3">IllegalArgumentException</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 57. Какой метод enum возвращает имя константы в виде строки?</h4>
<div class="quiz-option" data-index="0">toString() — всегда</div>
<div class="quiz-option" data-index="1">getString()</div>
<div class="quiz-option" data-index="2">name() — всегда возвращает точное имя, даже если toString() переопределён</div>
<div class="quiz-option" data-index="3">label()</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 58. Что создаёт <code>EnumSet.complementOf(readOnly)</code>?</h4>
<div class="quiz-option" data-index="0">Копию readOnly</div>
<div class="quiz-option" data-index="1">Множество всех констант, кроме содержащихся в readOnly</div>
<div class="quiz-option" data-index="2">Пустое множество</div>
<div class="quiz-option" data-index="3">Пересечение с readOnly</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 59. Являются ли поля record неизменяемыми (immutable)?</h4>
<div class="quiz-option" data-index="0">Да, поля record — private final, их нельзя переназначить</div>
<div class="quiz-option" data-index="1">Нет, их можно изменить через сеттеры</div>
<div class="quiz-option" data-index="2">Только примитивные поля</div>
<div class="quiz-option" data-index="3">Нет, если поле ссылочного типа</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 60. Что отличает <code>EnumMap.getOrDefault(key, defaultValue)</code> от обычного <code>get(key)</code>?</h4>
<div class="quiz-option" data-index="0">getOrDefault выбрасывает исключение при отсутствии ключа</div>
<div class="quiz-option" data-index="1">Ничем — это синонимы</div>
<div class="quiz-option" data-index="2">getOrDefault работает только с null-ключами</div>
<div class="quiz-option" data-index="3">getOrDefault возвращает defaultValue вместо null, если ключ не найден</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== УГЛУБЛЁННЫЕ ВОПРОСЫ: АННОТАЦИИ И ВЛОЖЕННЫЕ КЛАССЫ (61-66) ===== -->

<div class="quiz-question" data-correct="2">
<h4>Вопрос 61. Что означает <code>@Retention(RetentionPolicy.CLASS)</code>?</h4>
<div class="quiz-option" data-index="0">Аннотация доступна через Reflection во время выполнения</div>
<div class="quiz-option" data-index="1">Аннотация существует только в исходном коде</div>
<div class="quiz-option" data-index="2">Аннотация сохраняется в .class файле, но не доступна через Reflection</div>
<div class="quiz-option" data-index="3">Аннотация применяется только к классам</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 62. Что делает аннотация <code>@Deprecated</code>?</h4>
<div class="quiz-option" data-index="0">Запрещает использование метода</div>
<div class="quiz-option" data-index="1">Помечает элемент как устаревший — компилятор выдаст предупреждение при его использовании</div>
<div class="quiz-option" data-index="2">Удаляет метод при компиляции</div>
<div class="quiz-option" data-index="3">Заменяет метод на более новую версию</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 63. Может ли аннотация иметь значения параметров по умолчанию?</h4>

```java
@interface Info {
    String author();
    int version() default 1;
}
```

<div class="quiz-option" data-index="0">Да, через ключевое слово default — при использовании параметр можно не указывать</div>
<div class="quiz-option" data-index="1">Нет, все параметры обязательны</div>
<div class="quiz-option" data-index="2">Только для параметров типа String</div>
<div class="quiz-option" data-index="3">Да, но только для одного параметра</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 64. Может ли анонимный класс иметь собственный конструктор?</h4>
<div class="quiz-option" data-index="0">Да, как обычный класс</div>
<div class="quiz-option" data-index="1">Да, но только приватный</div>
<div class="quiz-option" data-index="2">Да, через ключевое слово super</div>
<div class="quiz-option" data-index="3">Нет — у него нет имени, поэтому нельзя объявить конструктор</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 65. Может ли анонимный класс обращаться к private-полям внешнего класса?</h4>
<div class="quiz-option" data-index="0">Нет, только к public-полям</div>
<div class="quiz-option" data-index="1">Нет, только к protected и public</div>
<div class="quiz-option" data-index="2">Да, анонимный класс имеет доступ ко всем членам внешнего класса, включая private</div>
<div class="quiz-option" data-index="3">Только через геттеры</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 66. Может ли локальный класс реализовать несколько интерфейсов?</h4>
<div class="quiz-option" data-index="0">Нет, только один (как анонимный)</div>
<div class="quiz-option" data-index="1">Да, в отличие от анонимного класса, он может реализовать несколько интерфейсов</div>
<div class="quiz-option" data-index="2">Только маркерные интерфейсы</div>
<div class="quiz-option" data-index="3">Только функциональные интерфейсы</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== УГЛУБЛЁННЫЕ ВОПРОСЫ: ЛЯМБДЫ И ССЫЛКИ НА МЕТОДЫ (67-78) ===== -->

<div class="quiz-question" data-correct="0">
<h4>Вопрос 67. Чем отличается поведение <code>this</code> в лямбде от анонимного класса?</h4>
<div class="quiz-option" data-index="0">В лямбде this указывает на внешний объект, в анонимном классе — на сам анонимный объект</div>
<div class="quiz-option" data-index="1">Наоборот: в анонимном — внешний, в лямбде — саму лямбду</div>
<div class="quiz-option" data-index="2">Ничем — this одинаково работает</div>
<div class="quiz-option" data-index="3">this нельзя использовать ни в лямбде, ни в анонимном классе</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 68. Почему этот код не скомпилируется? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
int count = 0;
Runnable r = () -> count++;
```

<div class="quiz-option" data-index="0">Runnable не поддерживает лямбды</div>
<div class="quiz-option" data-index="1">count не инициализирован</div>
<div class="quiz-option" data-index="2">Лямбда не может возвращать void</div>
<div class="quiz-option" data-index="3">count изменяется (count++) — переменная не effectively final</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 69. Какой тип у лямбды <code>(a, b) -> a + b</code>, если она присвоена <code>BinaryOperator&lt;Integer&gt;</code>?</h4>
<div class="quiz-option" data-index="0">Function&lt;Integer, Integer&gt;</div>
<div class="quiz-option" data-index="1">BinaryOperator&lt;Integer&gt; — принимает два Integer, возвращает Integer</div>
<div class="quiz-option" data-index="2">BiConsumer&lt;Integer, Integer&gt;</div>
<div class="quiz-option" data-index="3">Predicate&lt;Integer&gt;</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 70. Что такое <code>Function&lt;T, R&gt;</code>?</h4>
<div class="quiz-option" data-index="0">Принимает T и R, ничего не возвращает</div>
<div class="quiz-option" data-index="1">Не принимает аргументов, возвращает T</div>
<div class="quiz-option" data-index="2">Принимает аргумент типа T и возвращает результат типа R</div>
<div class="quiz-option" data-index="3">Принимает два аргумента типа T</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 71. Можно ли использовать <code>super</code> внутри лямбда-выражения?</h4>
<div class="quiz-option" data-index="0">Нет, в лямбда-выражениях нельзя использовать super</div>
<div class="quiz-option" data-index="1">Да, super указывает на родительский класс</div>
<div class="quiz-option" data-index="2">Да, super указывает на функциональный интерфейс</div>
<div class="quiz-option" data-index="3">Только в default-методах интерфейса</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 72. Что является ссылкой на метод конкретного объекта?</h4>
<div class="quiz-option" data-index="0">String::toUpperCase</div>
<div class="quiz-option" data-index="1">Math::max</div>
<div class="quiz-option" data-index="2">ArrayList::new</div>
<div class="quiz-option" data-index="3">System.out::println</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 73. Что делает <code>BiConsumer&lt;String, Integer&gt;</code>?</h4>
<div class="quiz-option" data-index="0">Принимает String, возвращает Integer</div>
<div class="quiz-option" data-index="1">Принимает String и Integer, ничего не возвращает (void)</div>
<div class="quiz-option" data-index="2">Принимает Integer, возвращает String</div>
<div class="quiz-option" data-index="3">Принимает два Integer</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 74. Когда лямбду НЕЛЬЗЯ заменить ссылкой на метод?</h4>

```java
names.forEach(name -> System.out.println("Name: " + name));
```

<div class="quiz-option" data-index="0">Лямбды всегда можно заменить ссылкой на метод</div>
<div class="quiz-option" data-index="1">Только если метод статический</div>
<div class="quiz-option" data-index="2">Когда лямбда содержит дополнительную логику, а не просто вызывает метод</div>
<div class="quiz-option" data-index="3">Когда тип аргумента — String</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 75. Чем <code>UnaryOperator&lt;T&gt;</code> отличается от <code>Function&lt;T, R&gt;</code>?</h4>
<div class="quiz-option" data-index="0">UnaryOperator — частный случай Function, где тип аргумента и результата совпадают (T → T)</div>
<div class="quiz-option" data-index="1">UnaryOperator принимает два аргумента</div>
<div class="quiz-option" data-index="2">Ничем — это синонимы</div>
<div class="quiz-option" data-index="3">UnaryOperator возвращает void</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 76. Что выведет этот код? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
Predicate<String> p = s -> s.length() > 3;
System.out.println(p.test("Hi"));
System.out.println(p.test("Java"));
```

<div class="quiz-option" data-index="0">true, true</div>
<div class="quiz-option" data-index="1">true, false</div>
<div class="quiz-option" data-index="2">Ошибка компиляции</div>
<div class="quiz-option" data-index="3">false, true</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 77. Какой метод <code>Consumer&lt;T&gt;</code> используется для выполнения действия?</h4>
<div class="quiz-option" data-index="0">apply()</div>
<div class="quiz-option" data-index="1">accept()</div>
<div class="quiz-option" data-index="2">test()</div>
<div class="quiz-option" data-index="3">get()</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 78. Какой метод <code>Supplier&lt;T&gt;</code> используется для получения значения?</h4>
<div class="quiz-option" data-index="0">apply()</div>
<div class="quiz-option" data-index="1">accept()</div>
<div class="quiz-option" data-index="2">get()</div>
<div class="quiz-option" data-index="3">supply()</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== УГЛУБЛЁННЫЕ ВОПРОСЫ: МОДУЛИ И ПАКЕТЫ (79-85) ===== -->

<div class="quiz-question" data-correct="0">
<h4>Вопрос 79. Что такое <code>requires transitive</code> в module-info.java?</h4>
<div class="quiz-option" data-index="0">Транзитивная зависимость — модули, зависящие от текущего, автоматически получают доступ к указанному модулю</div>
<div class="quiz-option" data-index="1">Зависимость, которая нужна только при компиляции</div>
<div class="quiz-option" data-index="2">Зависимость от конкретной версии модуля</div>
<div class="quiz-option" data-index="3">Необязательная зависимость</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 80. Что делает <code>exports lecture.two.annotations to module.test</code>?</h4>
<div class="quiz-option" data-index="0">Экспортирует пакет для всех модулей</div>
<div class="quiz-option" data-index="1">Открывает пакет для рефлексии</div>
<div class="quiz-option" data-index="2">Запрещает доступ к пакету из module.test</div>
<div class="quiz-option" data-index="3">Экспортирует пакет только для указанного модуля module.test</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 81. Зачем нужна директива <code>opens</code>, если уже есть <code>exports</code>?</h4>
<div class="quiz-option" data-index="0">opens и exports — синонимы</div>
<div class="quiz-option" data-index="1">exports даёт доступ при компиляции, opens — дополнительно открывает для рефлексии (Reflection) во время выполнения</div>
<div class="quiz-option" data-index="2">opens экспортирует только интерфейсы</div>
<div class="quiz-option" data-index="3">opens работает быстрее exports</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 82. Что такое <code>open module</code>?</h4>
<div class="quiz-option" data-index="0">Модуль без зависимостей</div>
<div class="quiz-option" data-index="1">Модуль, доступный только для тестирования</div>
<div class="quiz-option" data-index="2">Модуль, в котором все пакеты открыты для рефлексии</div>
<div class="quiz-option" data-index="3">Модуль с публичным API</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 83. Что означает <code>import java.util.*</code>?</h4>
<div class="quiz-option" data-index="0">Импортирует все классы из пакета java.util (но не подпакеты)</div>
<div class="quiz-option" data-index="1">Импортирует все классы из java.util и всех его подпакетов</div>
<div class="quiz-option" data-index="2">Создаёт пакет java.util</div>
<div class="quiz-option" data-index="3">Удаляет все импорты</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 84. Для чего аннотация <code>@ParametersAreNonnullByDefault</code> в package-info.java?</h4>
<div class="quiz-option" data-index="0">Все параметры становятся final</div>
<div class="quiz-option" data-index="1">Все параметры инициализируются нулём</div>
<div class="quiz-option" data-index="2">Запрещает передачу null в статические методы</div>
<div class="quiz-option" data-index="3">Все параметры методов в пакете считаются ненулевыми — инструменты анализа предупредят о передаче null</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 85. Какую проблему решает <code>jlink</code> совместно с JPMS?</h4>
<div class="quiz-option" data-index="0">Компилирует модули в машинный код</div>
<div class="quiz-option" data-index="1">Создаёт минимальный runtime-образ с только необходимыми модулями</div>
<div class="quiz-option" data-index="2">Линкует C-библиотеки с Java-модулями</div>
<div class="quiz-option" data-index="3">Объединяет несколько модулей в один</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== КОМПЛЕКСНЫЕ ВОПРОСЫ НА ПОНИМАНИЕ (86-95) ===== -->

<div class="quiz-question" data-correct="2">
<h4>Вопрос 86. Что произойдёт при выполнении? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
interface A { default void hello() { System.out.println("A"); } }
interface B { default void hello() { System.out.println("B"); } }
class C implements A, B {
    // нет переопределения hello()
}
```

<div class="quiz-option" data-index="0">Выведет "A"</div>
<div class="quiz-option" data-index="1">Выведет "B"</div>
<div class="quiz-option" data-index="2">Ошибка компиляции — класс C обязан переопределить hello()</div>
<div class="quiz-option" data-index="3">Ошибка времени выполнения</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 87. Чем <code>BiPredicate&lt;T, U&gt;</code> отличается от <code>Predicate&lt;T&gt;</code>?</h4>
<div class="quiz-option" data-index="0">BiPredicate принимает два аргумента и возвращает boolean</div>
<div class="quiz-option" data-index="1">BiPredicate возвращает два boolean</div>
<div class="quiz-option" data-index="2">BiPredicate — это два Predicate</div>
<div class="quiz-option" data-index="3">BiPredicate не возвращает значение</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 88. В какой версии Java появились default-методы в интерфейсах?</h4>
<div class="quiz-option" data-index="0">Java 7</div>
<div class="quiz-option" data-index="1">Java 8</div>
<div class="quiz-option" data-index="2">Java 9</div>
<div class="quiz-option" data-index="3">Java 11</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 89. В какой версии Java появились записи (records)?</h4>
<div class="quiz-option" data-index="0">Java 11</div>
<div class="quiz-option" data-index="1">Java 14</div>
<div class="quiz-option" data-index="2">Java 15</div>
<div class="quiz-option" data-index="3">Java 16 (стабильная версия)</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 90. В какой версии Java появилось ключевое слово <code>var</code>?</h4>
<div class="quiz-option" data-index="0">Java 10</div>
<div class="quiz-option" data-index="1">Java 8</div>
<div class="quiz-option" data-index="2">Java 11</div>
<div class="quiz-option" data-index="3">Java 9</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 91. Какой результат <code>"Hello".charAt(4)</code>? <span class="jshell-hint">Попробуй в jshell!</span></h4>
<div class="quiz-option" data-index="0">'l'</div>
<div class="quiz-option" data-index="1">StringIndexOutOfBoundsException</div>
<div class="quiz-option" data-index="2">'o'</div>
<div class="quiz-option" data-index="3">'H'</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 92. Что вернёт <code>"Hello".startsWith("He")</code>? <span class="jshell-hint">Попробуй в jshell!</span></h4>
<div class="quiz-option" data-index="0">false</div>
<div class="quiz-option" data-index="1">true</div>
<div class="quiz-option" data-index="2">"He"</div>
<div class="quiz-option" data-index="3">2</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 93. Можно ли создать массив абстрактного типа? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
abstract class Animal {}
class Dog extends Animal {}
Animal[] animals = new Animal[3];
animals[0] = new Dog();
```

<div class="quiz-option" data-index="0">Нет, массивы абстрактного типа запрещены</div>
<div class="quiz-option" data-index="1">Ошибка компиляции на строке new Animal[3]</div>
<div class="quiz-option" data-index="2">Ошибка времени выполнения при присваивании</div>
<div class="quiz-option" data-index="3">Да, массив ссылок типа Animal допустим, элементами будут объекты подклассов</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 94. Что произойдёт при сортировке списка через лямбду? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
List<String> names = Arrays.asList("Zara", "Liam", "Alex");
names.sort((a, b) -> a.compareToIgnoreCase(b));
System.out.println(names);
```

<div class="quiz-option" data-index="0">[Alex, Liam, Zara] — отсортировано по алфавиту без учёта регистра</div>
<div class="quiz-option" data-index="1">[Zara, Liam, Alex] — порядок не изменится</div>
<div class="quiz-option" data-index="2">Ошибка компиляции</div>
<div class="quiz-option" data-index="3">[Alex, Liam, Zara] — отсортировано в обратном порядке</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 95. Какой метод вызывается для чтения RUNTIME-аннотации через Reflection?</h4>
<div class="quiz-option" data-index="0">method.getAnnotations().find()</div>
<div class="quiz-option" data-index="1">method.readAnnotation()</div>
<div class="quiz-option" data-index="2">method.getAnnotation(Info.class) — после проверки isAnnotationPresent()</div>
<div class="quiz-option" data-index="3">method.annotation()</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== ВОПРОСЫ 96-105: ДАТЫ И ВРЕМЯ (JAVA.TIME) ===== -->

<div class="quiz-question" data-correct="3">
<h4>Вопрос 96. Что произойдёт, если вызвать <code>date.plusDays(10)</code> и не присвоить результат обратно в переменную?</h4>
<div class="quiz-option" data-index="0">Изменяет объект date и возвращает ссылку на него же</div>
<div class="quiz-option" data-index="1">Бросает исключение UnsupportedOperationException</div>
<div class="quiz-option" data-index="2">Ничего не делает, потому что дни можно прибавлять только через withDayOfMonth</div>
<div class="quiz-option" data-index="3">Создаёт и возвращает новый объект LocalDate, а исходный date остаётся без изменений</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 97. В чём принципиальное отличие <code>LocalDateTime</code> от <code>ZonedDateTime</code>?</h4>
<div class="quiz-option" data-index="0">LocalDateTime не знает про часовой пояс, поэтому не определяет конкретный момент времени; ZonedDateTime добавляет ZoneId и указывает на реальный момент</div>
<div class="quiz-option" data-index="1">LocalDateTime хранит только дату, а ZonedDateTime — только время</div>
<div class="quiz-option" data-index="2">Это два названия одного и того же класса, оставленные для совместимости</div>
<div class="quiz-option" data-index="3">ZonedDateTime нельзя сравнивать через isBefore() и isAfter()</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 98. Какой класс java.time хранит момент как секунды и наносекунды от 1970-01-01T00:00Z и вообще не содержит информации о часовом поясе?</h4>
<div class="quiz-option" data-index="0">LocalDateTime</div>
<div class="quiz-option" data-index="1">Instant</div>
<div class="quiz-option" data-index="2">ZonedDateTime</div>
<div class="quiz-option" data-index="3">OffsetDateTime</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 99. С какими классами работает <code>Period</code>, а с какими — <code>Duration</code>?</h4>
<div class="quiz-option" data-index="0">Period и Duration взаимозаменяемы для любых временных типов</div>
<div class="quiz-option" data-index="1">Period работает только с Instant, Duration — только с ZonedDateTime</div>
<div class="quiz-option" data-index="2">Period — с LocalDate, измеряет годы, месяцы и дни; Duration — с LocalTime, LocalDateTime и Instant, измеряет часы, минуты и секунды</div>
<div class="quiz-option" data-index="3">Period измеряет секунды, а Duration — календарные месяцы</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 100. Что именно вычисляет <code>ChronoUnit.DAYS.between(birthDate, today)</code>?</h4>
<div class="quiz-option" data-index="0">Общее количество дней между двумя датами одним числом, без разбивки на годы и месяцы</div>
<div class="quiz-option" data-index="1">Число полных месяцев между датами</div>
<div class="quiz-option" data-index="2">Возраст в формате «20 лет 6 месяцев»</div>
<div class="quiz-option" data-index="3">День недели даты today</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 101. Для чего в java.time нужен класс <code>TemporalAdjusters</code>?</h4>
<div class="quiz-option" data-index="0">Для перевода даты и времени между часовыми поясами</div>
<div class="quiz-option" data-index="1">Для форматирования даты в строку по шаблону</div>
<div class="quiz-option" data-index="2">Для потокобезопасного разбора строк в дату</div>
<div class="quiz-option" data-index="3">Для готовых «умных» сдвигов дат — например, «первый понедельник месяца» или «последний день месяца» — без ручных циклов</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 102. В шаблоне <code>DateTimeFormatter.ofPattern()</code> перепутали буквы <code>MM</code> и <code>mm</code>. Что произойдёт?</h4>
<div class="quiz-option" data-index="0">Ничего, обе буквы означают одно и то же — месяц</div>
<div class="quiz-option" data-index="1">MM отвечает за месяц, а mm — за минуты; при перепутывании дата отформатируется неверно, но ошибка не будет заметна сразу, только по неправильному значению в выводе</div>
<div class="quiz-option" data-index="2">Компилятор не даст скомпилировать такой код</div>
<div class="quiz-option" data-index="3">Программа сразу бросит DateTimeParseException при запуске</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 103. Почему <code>DateTimeFormatter</code> можно спокойно держать в поле <code>static final</code> и использовать из нескольких потоков, а <code>SimpleDateFormat</code> — нельзя?</h4>
<div class="quiz-option" data-index="0">DateTimeFormatter быстрее работает, но тоже не потокобезопасен</div>
<div class="quiz-option" data-index="1">Разницы нет, оба класса можно свободно использовать в static final</div>
<div class="quiz-option" data-index="2">DateTimeFormatter неизменяем (immutable) и потокобезопасен по конструкции; SimpleDateFormat хранит промежуточное состояние разбора внутри себя, и параллельные вызовы портят это состояние</div>
<div class="quiz-option" data-index="3">SimpleDateFormat можно безопасно использовать из нескольких потоков, если синхронизировать метод main</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 104. Почему момент времени в базе данных обычно хранят как <code>Instant</code>, а не как <code>LocalDateTime</code>?</h4>
<div class="quiz-option" data-index="0">Instant занимает меньше места в памяти, и только это имеет значение</div>
<div class="quiz-option" data-index="1">LocalDateTime сам умеет определять часовой пояс сервера, поэтому Instant не нужен</div>
<div class="quiz-option" data-index="2">Instant нельзя сохранить в колонку TIMESTAMP, поэтому его не используют в реальных проектах</div>
<div class="quiz-option" data-index="3">LocalDateTime не хранит часовой пояс, поэтому по значению «14:30» нельзя восстановить, какой момент имелся в виду; Instant — точка на шкале времени, одинаковая для всех наблюдателей</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 105. Строка <code>"2026-03-08 14:00"</code> не подходит под шаблон <code>"dd.MM.yyyy HH:mm"</code>. Что произойдёт при вызове <code>LocalDateTime.parse(text, formatter)</code>?</h4>
<div class="quiz-option" data-index="0">Метод молча вернёт null</div>
<div class="quiz-option" data-index="1">Будет выброшено непроверяемое исключение DateTimeParseException, которое можно поймать в try-catch</div>
<div class="quiz-option" data-index="2">Java автоматически подберёт формат по содержимому строки</div>
<div class="quiz-option" data-index="3">Программа зависнет в бесконечном цикле разбора</div>
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
    'Вопрос 1': 'exports делает пакет доступным для других модулей. Без exports пакет скрыт.',
    'Вопрос 2': 'requires указывает, что текущий модуль зависит от другого модуля.',
    'Вопрос 3': 'opens открывает пакет для рефлексии во время выполнения (для фреймворков типа Spring).',
    'Вопрос 4': 'JPMS решает JAR-Hell: явные зависимости через requires и управление экспортом через exports.',
    'Вопрос 5': 'package-info.java — для Javadoc-документации и аннотаций на уровне пакета.',
    'Вопрос 6': 'String.join("-", "A", "B", "C") соединяет строки через разделитель: "A-B-C".',
    'Вопрос 7': 'protected — доступ в своём пакете + в подклассах из других пакетов. Шире default, уже public.',
    'Вопрос 8': 'При конфликте default-методов из двух интерфейсов класс обязан явно переопределить метод.',
    'Вопрос 9': 'repeat(3) повторяет строку 3 раза: "Ha".repeat(3) → "HaHaHa" (Java 11+).',
    'Вопрос 10': 'Вложенный static-класс не хранит ссылку на внешний объект. Внутренний (non-static) — хранит.',
    'Вопрос 11': 'Порядок: статический блок (один раз при загрузке класса) → блок экземпляра → конструктор.',
    'Вопрос 12': 'static-блок "A" выполняется один раз. При каждом new — блок экземпляра "B" и конструктор "C". Итого: A B C B C.',
    'Вопрос 13': 'this ссылается на текущий объект. В конструкторе this.modelName отличает поле от параметра modelName.',
    'Вопрос 14': 'Обращаться можно (obj.staticField), но компилятор выдаст предупреждение. Правильно: ClassName.staticField.',
    'Вопрос 15': 'protected виден внутри пакета и в подклассах из других пакетов. default (без модификатора) в подклассах других пакетов не виден.',
    'Вопрос 16': 'var требует инициализации при объявлении. Без неё компилятор не может вывести тип.',
    'Вопрос 17': 'Статический метод не имеет this и не может обращаться к нестатическим полям и методам.',
    'Вопрос 18': 'public static — поле принадлежит классу, а не объекту. Все объекты разделяют одну переменную.',
    'Вопрос 19': 'Геттеры и сеттеры — основа инкапсуляции: поля private, доступ через контролируемые методы.',
    'Вопрос 20': 'Абстрактный класс может не реализовать методы интерфейса — они останутся абстрактными для подклассов.',
    'Вопрос 21': 'Допустимо: abstract class Config {} — просто запрещает new Config(). Абстрактные методы необязательны.',
    'Вопрос 22': 'Diamond problem: при конфликте default-методов из двух интерфейсов класс обязан явно переопределить метод.',
    'Вопрос 23': 'Private-методы в интерфейсе позволяют избежать дублирования кода между default-методами, не раскрывая helper-логику.',
    'Вопрос 24': 'Поля интерфейса неявно public static final. Присваивание значения вызовет ошибку компиляции.',
    'Вопрос 25': 'Да, default-метод может вызвать абстрактный метод. Реализация будет предоставлена классом.',
    'Вопрос 26': 'sealed применяется и к классам, и к интерфейсам. Ограничивает, кто может реализовать/расширить.',
    'Вопрос 27': 'Компилятор знает все варианты sealed-класса и проверяет полноту switch — default не нужен.',
    'Вопрос 28': 'IS-A (является) → наследование/абстрактный класс. CAN-DO (умеет) → интерфейс. Это ключевое правило выбора.',
    'Вопрос 29': 'Effectively final — переменная без слова final, но значение которой не меняется после инициализации.',
    'Вопрос 30': 'Функциональный интерфейс = ровно один абстрактный метод. default и static методы не считаются.',
    'Вопрос 31': 'Serializable — пустой интерфейс, отмечающий класс как сериализуемый. Comparable содержит compareTo().',
    'Вопрос 32': 'abstract final — противоречие: abstract требует наследования, final запрещает. Компилятор выдаст ошибку.',
    'Вопрос 33': 'Массивы — объекты. Присваивание копирует ссылку, а не данные. arr и arr2 указывают на один массив.',
    'Вопрос 34': 'Элементы int[] по умолчанию 0. Для double — 0.0, для boolean — false, для ссылок — null.',
    'Вопрос 35': 'Значение по умолчанию для boolean — false. Это касается и полей класса, и элементов массива.',
    'Вопрос 36': 'jagged[1] — это вторая строка (массив), .length — её длина. Каждая строка зубчатого массива — отдельный массив.',
    'Вопрос 37': 'Все массивы в Java — объекты, даже int[]. У них есть поле length и методы класса Object.',
    'Вопрос 38': 'for-each (enhanced for) — простой и безопасный способ перебора. Не нужен индекс, нет риска выйти за границы.',
    'Вопрос 39': 'intern() ищет "Test" в Pool, находит (s1 уже создал его) и возвращает ту же ссылку. s1 == s5 → true.',
    'Вопрос 40': 'indexOf() возвращает индекс первого вхождения. "Java": J=0, a=1. Первая "a" — индекс 1.',
    'Вопрос 41': 'lastIndexOf() возвращает индекс последнего вхождения. "Java": последняя "a" — индекс 3.',
    'Вопрос 42': 'Вызов метода на null вызывает NullPointerException. Проверяйте: if (s != null) s.length();',
    'Вопрос 43': 'equalsIgnoreCase() сравнивает содержимое строк без учёта регистра. "Java" и "java" одинаковы.',
    'Вопрос 44': 'replace() заменяет все вхождения. "Hello" → "Herro". Результат — новая строка (String immutable).',
    'Вопрос 45': 'new String(charArray) создаёт строку из массива символов. charArray.toString() вернёт адрес объекта.',
    'Вопрос 46': 'Для проверки на null используйте ==: s == null. У null нельзя вызвать .equals().',
    'Вопрос 47': 'append() — основной метод StringBuilder для добавления текста в конец.',
    'Вопрос 48': 'Text blocks (тройные кавычки) поддерживают многострочный текст без экранирования кавычек и переносов.',
    'Вопрос 49': 'trim() удаляет пробельные символы только с начала и конца строки, не затрагивая внутренние.',
    'Вопрос 50': 'append() возвращает тот же StringBuilder, что позволяет вызывать методы по цепочке (method chaining).',
    'Вопрос 51': 'Record не допускает дополнительных полей экземпляра. Все поля объявляются в заголовке: record Name(поля).',
    'Вопрос 52': 'Record может содержать статические поля, методы и вложенные типы. Ограничение — только на поля экземпляра.',
    'Вопрос 53': 'Исключение в компактном конструкторе прерывает создание объекта. Объект не будет создан.',
    'Вопрос 54': 'Каждая enum-константа — единственный экземпляр (singleton). Сравнение через == безопасно и рекомендовано.',
    'Вопрос 55': 'Конструктор enum — всегда private (явно или неявно). Нельзя создать экземпляр enum через new снаружи.',
    'Вопрос 56': 'valueOf() выбрасывает IllegalArgumentException, если строка не соответствует ни одной константе.',
    'Вопрос 57': 'name() всегда возвращает точное имя константы. toString() может быть переопределён.',
    'Вопрос 58': 'complementOf() возвращает дополнение: все константы enum, которых нет в указанном множестве.',
    'Вопрос 59': 'Поля record — private final. Сама ссылка неизменяема, но содержимое объекта по ссылке может меняться.',
    'Вопрос 60': 'getOrDefault() возвращает defaultValue при отсутствии ключа, а get() вернёт null.',
    'Вопрос 61': 'CLASS — аннотация сохраняется в .class, но невидима через Reflection. Используется инструментами обработки байт-кода.',
    'Вопрос 62': '@Deprecated не запрещает использование, а предупреждает: компилятор выдаст warning.',
    'Вопрос 63': 'default в аннотации задаёт значение по умолчанию. Параметр с default можно не указывать при использовании.',
    'Вопрос 64': 'У анонимного класса нет имени, а конструктор должен называться как класс. Поэтому конструктор невозможен.',
    'Вопрос 65': 'Анонимный класс имеет полный доступ ко всем членам внешнего класса, включая private.',
    'Вопрос 66': 'Локальный класс может наследовать класс и реализовать несколько интерфейсов, в отличие от анонимного.',
    'Вопрос 67': 'В лямбде this = внешний объект. В анонимном классе this = сам анонимный объект. Ключевое отличие!',
    'Вопрос 68': 'count++ изменяет переменную, значит count не effectively final. Лямбда не может захватить её.',
    'Вопрос 69': 'BinaryOperator<T> — BiFunction<T, T, T>. Принимает два значения одного типа и возвращает тот же тип.',
    'Вопрос 70': 'Function<T, R> — метод apply(T) → R. Преобразует значение типа T в значение типа R.',
    'Вопрос 71': 'В лямбда-выражениях this и super имеют то же значение, что и в окружающем контексте (JLS §15.27.2). super указывает на суперкласс объемлющего класса, потому что лямбда не создаёт новую область видимости.',
    'Вопрос 72': 'System.out::println — ссылка на метод конкретного объекта System.out. String::toUpperCase — по типу.',
    'Вопрос 73': 'BiConsumer<T, U> — accept(T, U), void. Принимает два аргумента разных типов, ничего не возвращает.',
    'Вопрос 74': 'Ссылка на метод — только когда лямбда просто вызывает метод. Здесь есть конкатенация "Name: " + name.',
    'Вопрос 75': 'UnaryOperator<T> extends Function<T, T>. Входной и выходной тип одинаковы. Пример: s -> s.trim().',
    'Вопрос 76': '"Hi".length() = 2, не > 3 → false. "Java".length() = 4, > 3 → true.',
    'Вопрос 77': 'Consumer<T>.accept(T) — выполняет действие над значением. Не путать с apply() (Function) и test() (Predicate).',
    'Вопрос 78': 'Supplier<T>.get() — возвращает значение без входных аргументов. «Поставщик» данных.',
    'Вопрос 79': 'requires transitive — модули, зависящие от текущего, автоматически получат доступ к транзитивно указанному модулю.',
    'Вопрос 80': 'exports ... to — квалифицированный экспорт: пакет доступен только указанным модулям.',
    'Вопрос 81': 'exports — доступ при компиляции и выполнении. opens — дополнительно открывает для deep reflection (setAccessible).',
    'Вопрос 82': 'open module — все пакеты открыты для рефлексии. Упрощает миграцию, но снижает инкапсуляцию.',
    'Вопрос 83': 'Звёздочка * импортирует все классы пакета, но НЕ подпакеты. java.util.* не включает java.util.stream.*.',
    'Вопрос 84': '@ParametersAreNonnullByDefault — все параметры считаются non-null. Инструменты (IDE, FindBugs) предупредят о null.',
    'Вопрос 85': 'jlink + JPMS создают минимальный runtime: только нужные модули. Уменьшает размер приложения.',
    'Вопрос 86': 'Diamond problem: два интерфейса с одинаковым default-методом. Класс C обязан переопределить hello().',
    'Вопрос 87': 'BiPredicate<T, U> — test(T, U) → boolean. Проверяет условие для двух аргументов разных типов.',
    'Вопрос 88': 'Default-методы в интерфейсах появились в Java 8 вместе с лямбда-выражениями.',
    'Вопрос 89': 'Records появились как превью в Java 14, стали стабильной функцией в Java 16.',
    'Вопрос 90': 'Ключевое слово var для локальных переменных появилось в Java 10.',
    'Вопрос 91': 'charAt(4): H=0, e=1, l=2, l=3, o=4. Индекс 4 — символ "o".',
    'Вопрос 92': 'startsWith("He") проверяет, начинается ли строка с "He". "Hello" начинается с "He" → true.',
    'Вопрос 93': 'Массив типа Animal[] допустим — он хранит ссылки. Элементами могут быть объекты подклассов (Dog, Bird).',
    'Вопрос 94': 'sort с компаратором через лямбду сортирует список по алфавиту без учёта регистра.',
    'Вопрос 95': 'method.getAnnotation(Info.class) возвращает объект аннотации. isAnnotationPresent() проверяет наличие.',
    'Вопрос 96': 'Все объекты java.time неизменяемы (immutable): plusDays() не трогает исходный объект, а возвращает новый. Результат обязательно нужно присвоить: date = date.plusDays(10).',
    'Вопрос 97': '"8 марта, 14:30" одинаково верно и для Москвы, и для Токио — LocalDateTime не различает эти случаи. ZonedDateTime добавляет часовой пояс и превращает запись в конкретный момент времени.',
    'Вопрос 98': 'Instant — это точка на шкале времени: число секунд и наносекунд от начала эпохи. Он не хранит ни города, ни смещения — одно и то же значение одинаково для Москвы, Токио и Лондона.',
    'Вопрос 99': 'Period — «человеческое» время в календарных единицах (годы, месяцы, дни), работает с LocalDate. Duration — «машинное» время (часы, минуты, секунды, наносекунды), работает с LocalTime, LocalDateTime и Instant.',
    'Вопрос 100': 'ChronoUnit считает разницу одним числом в выбранных единицах. Если нужен результат для показа человеку («20 лет 6 месяцев»), берут Period; если результат идёт в вычисления («сколько всего дней прошло») — ChronoUnit.',
    'Вопрос 101': 'TemporalAdjusters даёт готовые корректировщики вроде firstInMonth() и lastDayOfMonth(), которые применяются через date.with(...). TemporalAdjuster — функциональный интерфейс, поэтому можно написать и свой.',
    'Вопрос 102': 'Это одна из двух главных ловушек шаблонов DateTimeFormatter: MM (заглавные) — месяц, mm (строчные) — минуты. Перепутать легко, а ошибка проявится только в неверном выводе, а не в исключении при компиляции или запуске.',
    'Вопрос 103': 'SimpleDateFormat хранит промежуточное состояние разбора внутри объекта: один общий экземпляр на приложение при параллельных вызовах даёт перепутанные даты или исключение. DateTimeFormatter неизменяем, поэтому один экземпляр безопасно делят все потоки.',
    'Вопрос 104': 'Пользователи сидят в разных поясах, сервер может переехать в другой дата-центр, а правила перехода на летнее время меняются законом. Instant хранит саму точку на шкале, а перевод в местное время делают на границе — при показе пользователю.',
    'Вопрос 105': 'Если строка не подходит под ожидаемый формат, parse() бросает DateTimeParseException — это непроверяемое исключение, наследник RuntimeException, которое нужно ловить явно, если разбор может не удаться.'
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
