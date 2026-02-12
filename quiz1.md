# Тест: Введение в Java (Лекция 1 + Практика 1)

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
</style>

<div class="quiz-container" id="quiz">

<div class="quiz-question" data-correct="2">
<h4>Вопрос 1. Что означает девиз Java?</h4>
<div class="quiz-option" data-index="0">Compile once — debug everywhere</div>
<div class="quiz-option" data-index="1">Code once — deploy anywhere</div>
<div class="quiz-option" data-index="2">Write once — run anywhere</div>
<div class="quiz-option" data-index="3">Build once — test anywhere</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 2. Во что компилятор <code>javac</code> превращает исходный код Java?</h4>
<div class="quiz-option" data-index="0">В машинный код (.exe)</div>
<div class="quiz-option" data-index="1">В байт-код (.class)</div>
<div class="quiz-option" data-index="2">В ассемблерный код (.asm)</div>
<div class="quiz-option" data-index="3">В JavaScript (.js)</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 3. Какое соотношение между JDK, JRE и JVM верно?</h4>
<div class="quiz-option" data-index="0">JVM содержит JRE, JRE содержит JDK</div>
<div class="quiz-option" data-index="1">JRE содержит JDK, JDK содержит JVM</div>
<div class="quiz-option" data-index="2">JDK и JRE — это одно и то же</div>
<div class="quiz-option" data-index="3">JDK содержит JRE, JRE содержит JVM</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 4. Какой загрузчик классов загружает класс <code>String</code>?</h4>
<div class="quiz-option" data-index="0">Bootstrap ClassLoader</div>
<div class="quiz-option" data-index="1">Platform ClassLoader</div>
<div class="quiz-option" data-index="2">Application ClassLoader</div>
<div class="quiz-option" data-index="3">Custom ClassLoader</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 5. Что вернёт <code>String.class.getClassLoader()</code>?</h4>
<div class="quiz-option" data-index="0">PlatformClassLoader</div>
<div class="quiz-option" data-index="1">AppClassLoader</div>
<div class="quiz-option" data-index="2">null</div>
<div class="quiz-option" data-index="3">BootstrapClassLoader</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 6. Что выведет <code>System.out.println(10 / 3)</code>?</h4>
<div class="quiz-option" data-index="0">3.33</div>
<div class="quiz-option" data-index="1">3</div>
<div class="quiz-option" data-index="2">3.0</div>
<div class="quiz-option" data-index="3">4</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 7. Что произойдёт при выполнении: <code>byte b = 127; b++;</code>?</h4>
<div class="quiz-option" data-index="0">Ошибка компиляции</div>
<div class="quiz-option" data-index="1">b станет 128</div>
<div class="quiz-option" data-index="2">Будет выброшено исключение</div>
<div class="quiz-option" data-index="3">b станет -128 (переполнение)</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 8. Почему <code>0.1 + 0.2 == 0.3</code> возвращает <code>false</code>?</h4>
<div class="quiz-option" data-index="0">Оператор == не работает с типом double</div>
<div class="quiz-option" data-index="1">Нужно использовать float вместо double</div>
<div class="quiz-option" data-index="2">Из-за погрешности формата IEEE 754</div>
<div class="quiz-option" data-index="3">Java округляет дробные числа при сложении</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 9. Каков размер типа <code>int</code> в Java?</h4>
<div class="quiz-option" data-index="0">32 бита</div>
<div class="quiz-option" data-index="1">16 бит</div>
<div class="quiz-option" data-index="2">64 бита</div>
<div class="quiz-option" data-index="3">Зависит от платформы</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 10. Что выведет следующий код?</h4>

```java
int x = 5;
System.out.println(x++);
```

<div class="quiz-option" data-index="0">6</div>
<div class="quiz-option" data-index="1">5</div>
<div class="quiz-option" data-index="2">4</div>
<div class="quiz-option" data-index="3">Ошибка компиляции</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 11. Что выведет следующий код?</h4>

```java
String s1 = new String("Hello");
String s2 = new String("Hello");
System.out.println(s1 == s2);
```

<div class="quiz-option" data-index="0">true</div>
<div class="quiz-option" data-index="1">Ошибка компиляции</div>
<div class="quiz-option" data-index="2">false</div>
<div class="quiz-option" data-index="3">Hello</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 12. Какой метод является точкой входа в Java-программу?</h4>
<div class="quiz-option" data-index="0">public static void main(String[] args)</div>
<div class="quiz-option" data-index="1">public void main(String[] args)</div>
<div class="quiz-option" data-index="2">static void main()</div>
<div class="quiz-option" data-index="3">public static int main(String[] args)</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 13. Что хранит переменная ссылочного типа?</h4>
<div class="quiz-option" data-index="0">Само значение объекта</div>
<div class="quiz-option" data-index="1">Копию объекта</div>
<div class="quiz-option" data-index="2">Имя класса объекта</div>
<div class="quiz-option" data-index="3">Адрес (ссылку) на объект в памяти</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 14. Какой результат выражения <code>5 & 3</code> (побитовое И)?</h4>
<div class="quiz-option" data-index="0">7</div>
<div class="quiz-option" data-index="1">1</div>
<div class="quiz-option" data-index="2">6</div>
<div class="quiz-option" data-index="3">8</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 15. Где хранятся объекты в JVM?</h4>
<div class="quiz-option" data-index="0">В стеке (Stack)</div>
<div class="quiz-option" data-index="1">В Metaspace</div>
<div class="quiz-option" data-index="2">В куче (Heap)</div>
<div class="quiz-option" data-index="3">В PC Register</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 16. Сколько примитивных типов данных в Java?</h4>
<div class="quiz-option" data-index="0">6</div>
<div class="quiz-option" data-index="1">8</div>
<div class="quiz-option" data-index="2">10</div>
<div class="quiz-option" data-index="3">12</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 17. Что выведет следующий код?</h4>

```java
String s1 = "Java";
String s2 = "Java";
System.out.println(s1 == s2);
```

<div class="quiz-option" data-index="0">true</div>
<div class="quiz-option" data-index="1">false</div>
<div class="quiz-option" data-index="2">Ошибка компиляции</div>
<div class="quiz-option" data-index="3">Java</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 18. Какой инструмент JDK используется для интерактивных экспериментов с кодом?</h4>
<div class="quiz-option" data-index="0">javac</div>
<div class="quiz-option" data-index="1">javadoc</div>
<div class="quiz-option" data-index="2">jshell</div>
<div class="quiz-option" data-index="3">jdb</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 19. Какое значение по умолчанию у переменной типа <code>boolean</code> (поле класса)?</h4>
<div class="quiz-option" data-index="0">true</div>
<div class="quiz-option" data-index="1">null</div>
<div class="quiz-option" data-index="2">0</div>
<div class="quiz-option" data-index="3">false</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 20. Что означает запись <code>0b101010</code> в Java?</h4>
<div class="quiz-option" data-index="0">Восьмеричное число</div>
<div class="quiz-option" data-index="1">Двоичное число</div>
<div class="quiz-option" data-index="2">Шестнадцатеричное число</div>
<div class="quiz-option" data-index="3">Десятичное число</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 21. Какой суффикс обязателен для литерала типа <code>long</code>?</h4>
<div class="quiz-option" data-index="0">L</div>
<div class="quiz-option" data-index="1">D</div>
<div class="quiz-option" data-index="2">F</div>
<div class="quiz-option" data-index="3">Суффикс не нужен</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 22. Что делает Garbage Collector в JVM?</h4>
<div class="quiz-option" data-index="0">Компилирует байт-код в машинный код</div>
<div class="quiz-option" data-index="1">Загружает классы в память</div>
<div class="quiz-option" data-index="2">Автоматически освобождает память от неиспользуемых объектов</div>
<div class="quiz-option" data-index="3">Проверяет байт-код на безопасность</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 23. Что выведет следующий код?</h4>

```java
int x = 5;
System.out.println(++x);
```

<div class="quiz-option" data-index="0">5</div>
<div class="quiz-option" data-index="1">6</div>
<div class="quiz-option" data-index="2">4</div>
<div class="quiz-option" data-index="3">Ошибка компиляции</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 24. Какой результат выражения <code>5 | 3</code> (побитовое ИЛИ)?</h4>
<div class="quiz-option" data-index="0">1</div>
<div class="quiz-option" data-index="1">3</div>
<div class="quiz-option" data-index="2">5</div>
<div class="quiz-option" data-index="3">7</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 25. Что такое JIT-компилятор?</h4>
<div class="quiz-option" data-index="0">Компилирует часто выполняемый байт-код в машинный код для ускорения</div>
<div class="quiz-option" data-index="1">Компилирует .java файлы в .class файлы</div>
<div class="quiz-option" data-index="2">Загружает классы из JAR-файлов</div>
<div class="quiz-option" data-index="3">Проверяет код на ошибки перед запуском</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 26. Какой результат выражения <code>5 ^ 3</code> (побитовое XOR)?</h4>
<div class="quiz-option" data-index="0">1</div>
<div class="quiz-option" data-index="1">7</div>
<div class="quiz-option" data-index="2">6</div>
<div class="quiz-option" data-index="3">8</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 27. Какое правило действует для имени файла и публичного класса в Java?</h4>
<div class="quiz-option" data-index="0">Имя файла может быть любым</div>
<div class="quiz-option" data-index="1">Имя файла должно совпадать с именем публичного класса</div>
<div class="quiz-option" data-index="2">Имя класса должно начинаться с маленькой буквы</div>
<div class="quiz-option" data-index="3">В файле может быть только один класс</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 28. Что произойдёт при выполнении <code>false && someMethod()</code>?</h4>
<div class="quiz-option" data-index="0">someMethod() выполнится и вернёт false</div>
<div class="quiz-option" data-index="1">Ошибка компиляции</div>
<div class="quiz-option" data-index="2">someMethod() выполнится и результат будет false</div>
<div class="quiz-option" data-index="3">someMethod() не будет вызван (короткое замыкание)</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 29. Какой размер типа <code>char</code> в Java?</h4>
<div class="quiz-option" data-index="0">16 бит (Unicode)</div>
<div class="quiz-option" data-index="1">8 бит (ASCII)</div>
<div class="quiz-option" data-index="2">32 бита</div>
<div class="quiz-option" data-index="3">Зависит от символа</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 30. Что такое Metaspace в JVM?</h4>
<div class="quiz-option" data-index="0">Область для хранения объектов</div>
<div class="quiz-option" data-index="1">Стек вызовов методов</div>
<div class="quiz-option" data-index="2">Область для хранения метаданных классов (замена PermGen с Java 8)</div>
<div class="quiz-option" data-index="3">Кэш для JIT-компилятора</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 31. Какой результат выражения <code>5 << 2</code> (сдвиг влево)?</h4>
<div class="quiz-option" data-index="0">10</div>
<div class="quiz-option" data-index="1">20</div>
<div class="quiz-option" data-index="2">2</div>
<div class="quiz-option" data-index="3">25</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 32. Какой класс рекомендуется использовать для точных финансовых расчётов?</h4>
<div class="quiz-option" data-index="0">BigDecimal</div>
<div class="quiz-option" data-index="1">double</div>
<div class="quiz-option" data-index="2">float</div>
<div class="quiz-option" data-index="3">long</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 33. Из каких трёх подсистем состоит JVM?</h4>
<div class="quiz-option" data-index="0">Compiler, Linker, Debugger</div>
<div class="quiz-option" data-index="1">JRE, JDK, JAR</div>
<div class="quiz-option" data-index="2">Stack, Heap, Metaspace</div>
<div class="quiz-option" data-index="3">Class Loader, Runtime Data Areas, Execution Engine</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 34. Какое ключевое слово используется для объявления нативного метода (JNI)?</h4>
<div class="quiz-option" data-index="0">extern</div>
<div class="quiz-option" data-index="1">foreign</div>
<div class="quiz-option" data-index="2">native</div>
<div class="quiz-option" data-index="3">jni</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 35. Какая команда jshell показывает все объявленные переменные?</h4>
<div class="quiz-option" data-index="0">/list</div>
<div class="quiz-option" data-index="1">/vars</div>
<div class="quiz-option" data-index="2">/show</div>
<div class="quiz-option" data-index="3">/variables</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 36. Что выведет следующий код?</h4>

```java
int a = 10;
int b = 3;
System.out.println(10.0 / 3);
```

<div class="quiz-option" data-index="0">3.3333333333333335</div>
<div class="quiz-option" data-index="1">3</div>
<div class="quiz-option" data-index="2">3.0</div>
<div class="quiz-option" data-index="3">3.33</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 37. Какой принцип используют загрузчики классов при поиске класса?</h4>
<div class="quiz-option" data-index="0">Каждый загрузчик ищет класс самостоятельно</div>
<div class="quiz-option" data-index="1">Класс всегда загружает Application ClassLoader</div>
<div class="quiz-option" data-index="2">Загрузчики ищут класс снизу вверх и сверху вниз одновременно</div>
<div class="quiz-option" data-index="3">Делегирование «снизу вверх» (parent-first delegation)</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 38. Чему равно значение <code>Integer.MAX_VALUE + 1</code>?</h4>
<div class="quiz-option" data-index="0">2147483648</div>
<div class="quiz-option" data-index="1">0</div>
<div class="quiz-option" data-index="2">-2147483648 (Integer.MIN_VALUE)</div>
<div class="quiz-option" data-index="3">Будет выброшено исключение</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 39. Что делает подчёркивание в числовом литерале <code>1_000_000</code>?</h4>
<div class="quiz-option" data-index="0">Превращает число в строку</div>
<div class="quiz-option" data-index="1">Улучшает читаемость, не влияя на значение</div>
<div class="quiz-option" data-index="2">Разделяет число на части для вычисления</div>
<div class="quiz-option" data-index="3">Это синтаксическая ошибка</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 40. Какой метод нужно использовать для сравнения содержимого двух строк?</h4>
<div class="quiz-option" data-index="0">.equals()</div>
<div class="quiz-option" data-index="1">==</div>
<div class="quiz-option" data-index="2">.compare()</div>
<div class="quiz-option" data-index="3">.match()</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 41. Для чего используется ключевое слово <code>package</code> в Java?</h4>
<div class="quiz-option" data-index="0">Для импорта внешних библиотек</div>
<div class="quiz-option" data-index="1">Для группировки связанных классов по логическим папкам</div>
<div class="quiz-option" data-index="2">Для создания JAR-архива</div>
<div class="quiz-option" data-index="3">Для указания версии Java</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 42. Чем отличается <code>System.out.println()</code> от <code>System.out.print()</code>?</h4>
<div class="quiz-option" data-index="0">println выводит числа, print — строки</div>
<div class="quiz-option" data-index="1">print добавляет перенос строки, println — нет</div>
<div class="quiz-option" data-index="2">Ничем не отличаются</div>
<div class="quiz-option" data-index="3">println добавляет перенос строки после вывода, print — нет</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 43. Зачем метод <code>main</code> объявлен как <code>static</code>?</h4>
<div class="quiz-option" data-index="0">Чтобы JVM могла вызвать его без создания объекта класса</div>
<div class="quiz-option" data-index="1">Чтобы метод работал быстрее</div>
<div class="quiz-option" data-index="2">Чтобы метод был доступен из других классов</div>
<div class="quiz-option" data-index="3">Это необязательно, просто соглашение</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 44. Что содержит параметр <code>String[] args</code> в методе <code>main</code>?</h4>
<div class="quiz-option" data-index="0">Имена всех переменных программы</div>
<div class="quiz-option" data-index="1">Список импортированных пакетов</div>
<div class="quiz-option" data-index="2">Аргументы, переданные из командной строки</div>
<div class="quiz-option" data-index="3">Пути к файлам .class</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 45. Какие три этапа проходит класс при загрузке в JVM?</h4>
<div class="quiz-option" data-index="0">Compilation, Optimization, Execution</div>
<div class="quiz-option" data-index="1">Loading, Linking, Initialization</div>
<div class="quiz-option" data-index="2">Reading, Parsing, Running</div>
<div class="quiz-option" data-index="3">Verification, Preparation, Resolution</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 46. Что происходит на этапе Verification при загрузке класса?</h4>
<div class="quiz-option" data-index="0">Выделяется память для статических переменных</div>
<div class="quiz-option" data-index="1">Выполняются статические блоки инициализации</div>
<div class="quiz-option" data-index="2">Символические ссылки заменяются на прямые</div>
<div class="quiz-option" data-index="3">JVM проверяет корректность и безопасность байт-кода</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 47. Что хранится в стеке (Stack) потока?</h4>
<div class="quiz-option" data-index="0">Локальные переменные, параметры методов, адреса возврата</div>
<div class="quiz-option" data-index="1">Все объекты программы</div>
<div class="quiz-option" data-index="2">Метаданные загруженных классов</div>
<div class="quiz-option" data-index="3">Скомпилированный машинный код</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 48. Чем отличается <code>System.load()</code> от <code>System.loadLibrary()</code>?</h4>
<div class="quiz-option" data-index="0">load() загружает Java-классы, loadLibrary() — нативные библиотеки</div>
<div class="quiz-option" data-index="1">Ничем, это синонимы</div>
<div class="quiz-option" data-index="2">load() принимает полный путь к файлу, loadLibrary() ищет по имени в java.library.path</div>
<div class="quiz-option" data-index="3">loadLibrary() работает только на Windows</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 49. Что такое JAR-файл?</h4>
<div class="quiz-option" data-index="0">Исходный код Java в текстовом формате</div>
<div class="quiz-option" data-index="1">ZIP-архив, содержащий скомпилированные .class файлы и ресурсы</div>
<div class="quiz-option" data-index="2">Конфигурационный файл JVM</div>
<div class="quiz-option" data-index="3">Лог-файл компилятора javac</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 50. Чему эквивалентна запись <code>x += 3</code>?</h4>
<div class="quiz-option" data-index="0">x = x + 3</div>
<div class="quiz-option" data-index="1">x = 3</div>
<div class="quiz-option" data-index="2">x = x * 3</div>
<div class="quiz-option" data-index="3">x + 3</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 51. Какой результат выражения <code>10 >= 10</code>?</h4>
<div class="quiz-option" data-index="0">false</div>
<div class="quiz-option" data-index="1">Ошибка компиляции</div>
<div class="quiz-option" data-index="2">true</div>
<div class="quiz-option" data-index="3">10</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 52. Кто создал язык Java и в каком году?</h4>
<div class="quiz-option" data-index="0">Линус Торвальдс, 1991</div>
<div class="quiz-option" data-index="1">Бьярне Страуструп, 1985</div>
<div class="quiz-option" data-index="2">Гвидо ван Россум, 1991</div>
<div class="quiz-option" data-index="3">Джеймс Гослинг, 1995</div>
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
    'Вопрос 1': 'Девиз Java — «Write once — run anywhere» (Напиши один раз — запускай везде), благодаря байт-коду и JVM.',
    'Вопрос 2': 'Компилятор javac создаёт файлы .class с байт-кодом, который выполняет JVM.',
    'Вопрос 3': 'JDK — самая большая «матрёшка»: JDK содержит JRE, а JRE содержит JVM.',
    'Вопрос 4': 'Bootstrap ClassLoader загружает базовые классы Java (java.lang, java.util и др.).',
    'Вопрос 5': 'Bootstrap ClassLoader написан на C/C++, поэтому getClassLoader() возвращает null.',
    'Вопрос 6': 'При делении двух целых чисел результат тоже целое число — дробная часть отбрасывается.',
    'Вопрос 7': 'Максимальное значение byte = 127. При инкременте происходит переполнение: 127 + 1 = -128.',
    'Вопрос 8': '0.1 нельзя точно представить в двоичном формате IEEE 754, поэтому 0.1 + 0.2 = 0.30000000000000004.',
    'Вопрос 9': 'Тип int в Java всегда 32 бита (4 байта), независимо от платформы.',
    'Вопрос 10': 'x++ — постфиксный инкремент: сначала возвращает текущее значение (5), потом увеличивает.',
    'Вопрос 11': 'Оператор == сравнивает адреса объектов. new создаёт разные объекты, поэтому результат false.',
    'Вопрос 12': 'Точка входа должна быть именно public static void main(String[] args) — JVM ищет эту сигнатуру.',
    'Вопрос 13': 'Ссылочные переменные хранят адрес объекта в куче, а не сам объект.',
    'Вопрос 14': '5 = 0101, 3 = 0011. Побитовое И: 0101 & 0011 = 0001 = 1.',
    'Вопрос 15': 'Все объекты создаются в куче (Heap), которая доступна всем потокам программы.',
    'Вопрос 16': 'В Java 8 примитивных типов: byte, short, int, long, float, double, char, boolean.',
    'Вопрос 17': 'Строковые литералы хранятся в String Pool. Оба указывают на один объект, поэтому == возвращает true.',
    'Вопрос 18': 'jshell (REPL) — интерактивная консоль для экспериментов с кодом, появилась в Java 9.',
    'Вопрос 19': 'Значение по умолчанию для boolean — false. Для числовых типов — 0, для ссылочных — null.',
    'Вопрос 20': 'Префикс 0b означает двоичное число. 0x — шестнадцатеричное, 0 — восьмеричное.',
    'Вопрос 21': 'Суффикс L обязателен для long, f — для float. Без L число считается int.',
    'Вопрос 22': 'Garbage Collector автоматически находит и удаляет объекты, на которые нет ссылок, освобождая память.',
    'Вопрос 23': '++x — префиксный инкремент: сначала увеличивает (5→6), потом возвращает значение (6).',
    'Вопрос 24': '5 = 0101, 3 = 0011. Побитовое ИЛИ: 0101 | 0011 = 0111 = 7.',
    'Вопрос 25': 'JIT (Just-In-Time) компилятор находит «горячие точки» — часто выполняемый код — и компилирует его в машинный код.',
    'Вопрос 26': '5 = 0101, 3 = 0011. XOR: 0101 ^ 0011 = 0110 = 6. XOR даёт 1, если биты разные.',
    'Вопрос 27': 'Имя файла .java должно совпадать с именем публичного класса: класс Main → файл Main.java.',
    'Вопрос 28': 'Оператор && — «ленивый»: если первый операнд false, результат уже известен (false), и второй не вычисляется.',
    'Вопрос 29': 'char в Java — 16 бит (2 байта), хранит символы Unicode. В C/C++ char обычно 8 бит (ASCII).',
    'Вопрос 30': 'Metaspace (с Java 8) хранит метаданные классов в нативной памяти ОС, заменив PermGen с фиксированным размером.',
    'Вопрос 31': 'Сдвиг влево на 2 = умножение на 2² = 4. Значит 5 << 2 = 5 × 4 = 20.',
    'Вопрос 32': 'BigDecimal обеспечивает точные вычисления. float/double имеют погрешности из-за формата IEEE 754.',
    'Вопрос 33': 'JVM состоит из: Class Loader (загрузка классов), Runtime Data Areas (память), Execution Engine (выполнение).',
    'Вопрос 34': 'Ключевое слово native говорит JVM, что реализация метода написана на другом языке (C/C++).',
    'Вопрос 35': 'Команда /vars показывает все переменные, /list — весь введённый код, /exit — выход из jshell.',
    'Вопрос 36': 'Если хотя бы один операнд дробный (10.0), деление даёт дробный результат: 3.3333333333333335.',
    'Вопрос 37': 'Каждый загрузчик сначала делегирует запрос родителю. Только если родитель не нашёл класс, загрузчик ищет сам.',
    'Вопрос 38': 'При переполнении int «оборачивается»: MAX_VALUE + 1 = MIN_VALUE. Java не выбрасывает исключение!',
    'Вопрос 39': 'Подчёркивания в числах (с Java 7) только для читаемости: 1_000_000 = 1000000.',
    'Вопрос 40': 'Метод .equals() сравнивает содержимое строк. Оператор == сравнивает адреса (ссылки) объектов.',
    'Вопрос 41': 'Пакеты группируют классы по логическим папкам. Имя пакета соответствует структуре каталогов (lecture.one.hello → lecture/one/hello/).',
    'Вопрос 42': 'println (print line) выводит текст и переходит на новую строку. print выводит текст без переноса.',
    'Вопрос 43': 'static означает, что метод принадлежит классу, а не объекту. JVM вызывает main без создания экземпляра класса.',
    'Вопрос 44': 'String[] args — массив строк, в который передаются аргументы командной строки при запуске программы.',
    'Вопрос 45': 'Три этапа: Loading (чтение .class), Linking (проверка, подготовка, разрешение), Initialization (статические блоки).',
    'Вопрос 46': 'Verification — JVM проверяет, что байт-код корректен и безопасен (нет обращений к чужой памяти и т.д.).',
    'Вопрос 47': 'Стек хранит фреймы методов: локальные переменные, параметры и адреса возврата. У каждого потока свой стек.',
    'Вопрос 48': 'System.load() принимает полный путь к библиотеке, а System.loadLibrary() ищет по имени в java.library.path.',
    'Вопрос 49': 'JAR (Java ARchive) — это ZIP-архив с .class файлами и ресурсами. Позволяет упаковать приложение в один файл.',
    'Вопрос 50': 'Составные операторы присваивания: x += 3 эквивалентно x = x + 3. Аналогично работают -=, *=, /=, %=.',
    'Вопрос 51': 'Оператор >= возвращает true, если левый операнд больше или равен правому. 10 >= 10 → true.',
    'Вопрос 52': 'Java создан Джеймсом Гослингом в Sun Microsystems в 1995 году. Изначально для интерактивного телевидения.'
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
