# Тест 11: Паттерны и антипаттерны проектирования (Лекция 11)

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

<!-- ===== РАЗДЕЛ 1: Паттерны проектирования и принципы SOLID (Вопросы 1–13) ===== -->

<div class="quiz-question" data-correct="1">
<h4>Вопрос 1. Что такое паттерн проектирования?</h4>

<div class="quiz-option" data-index="0">Готовый фрагмент кода, который копируют в проект без изменений</div>
<div class="quiz-option" data-index="1">Проверенное решение типовой задачи проектирования: описание структуры классов и их взаимодействия</div>
<div class="quiz-option" data-index="2">Стандартная библиотека классов, входящая в состав JDK</div>
<div class="quiz-option" data-index="3">Формальное правило, соблюдение которого проверяет компилятор при сборке</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 2. Какими четырьмя элементами формально описывается любой паттерн?</h4>

<div class="quiz-option" data-index="0">Название, задача, решение, последствия</div>
<div class="quiz-option" data-index="1">Название, автор, год публикации, язык реализации</div>
<div class="quiz-option" data-index="2">Интерфейс, абстрактный класс, реализация, тест</div>
<div class="quiz-option" data-index="3">Входные данные, алгоритм, выходные данные, сложность</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 3. Что описано в книге «банды четырёх» (Gang of Four)?</h4>

<div class="quiz-option" data-index="0">12 паттернов, разделённых на классовые и объектные</div>
<div class="quiz-option" data-index="1">23 паттерна, разделённых на порождающие и поведенческие</div>
<div class="quiz-option" data-index="2">23 паттерна, разделённых на порождающие, структурные и поведенческие</div>
<div class="quiz-option" data-index="3">5 принципов SOLID и 18 паттернов уровня архитектуры</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 4. К какой группе относятся Наблюдатель, Стратегия и Шаблонный метод?</h4>

<div class="quiz-option" data-index="0">К порождающим</div>
<div class="quiz-option" data-index="1">К структурным</div>
<div class="quiz-option" data-index="2">К архитектурным</div>
<div class="quiz-option" data-index="3">К поведенческим</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 5. Что утверждает «правило трёх», защищающее от избыточного усложнения?</h4>

<div class="quiz-option" data-index="0">У класса должно быть не более трёх зависимостей</div>
<div class="quiz-option" data-index="1">Не выносите абстракцию, пока не увидели три реальных случая её использования</div>
<div class="quiz-option" data-index="2">Каждый паттерн нужно применить хотя бы трижды, чтобы его освоить</div>
<div class="quiz-option" data-index="3">Метод не должен иметь более трёх уровней вложенности</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 6. По какому признаку можно понять, что паттерн введён уместно?</h4>

<div class="quiz-option" data-index="0">Количество классов в проекте выросло</div>
<div class="quiz-option" data-index="1">У каждого класса появился собственный интерфейс</div>
<div class="quiz-option" data-index="2">Код стало легче менять</div>
<div class="quiz-option" data-index="3">Общее число строк кода уменьшилось</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 7. Класс SalesReport считает сумму продаж, формирует HTML-отчёт и отправляет его по почте. Какой принцип нарушен?</h4>

<div class="quiz-option" data-index="0">SRP — принцип единственной ответственности</div>
<div class="quiz-option" data-index="1">OCP — принцип открытости/закрытости</div>
<div class="quiz-option" data-index="2">LSP — принцип подстановки Лисков</div>
<div class="quiz-option" data-index="3">DIP — принцип инверсии зависимостей</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 8. Метод area(Object shape) состоит из длинной цепочки if (shape instanceof ...). Симптом нарушения какого принципа?</h4>

<div class="quiz-option" data-index="0">SRP — класс делает слишком много</div>
<div class="quiz-option" data-index="1">ISP — интерфейс навязывает лишние методы</div>
<div class="quiz-option" data-index="2">LSP — подкласс не подставим вместо родителя</div>
<div class="quiz-option" data-index="3">OCP — класс не закрыт для изменения</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 9. Для классов Rectangle и Square из лекции (Square переопределяет оба сеттера) выполнили: <code>Rectangle r = new Square(); r.setWidth(5); r.setHeight(4);</code> Что вернёт <code>r.area()</code>?</h4>

<div class="quiz-option" data-index="0">20</div>
<div class="quiz-option" data-index="1">16</div>
<div class="quiz-option" data-index="2">25</div>
<div class="quiz-option" data-index="3">Код не скомпилируется</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 10. Почему наследование Square от Rectangle нарушает LSP?</h4>

<div class="quiz-option" data-index="0">Потому что у квадрата меньше полей, чем у прямоугольника</div>
<div class="quiz-option" data-index="1">Потому что метод area() не переопределён в подклассе</div>
<div class="quiz-option" data-index="2">Потому что подкласс меняет смысл унаследованных сеттеров и ломает ожидания кода, написанного под родителя</div>
<div class="quiz-option" data-index="3">Потому что в Java нельзя наследовать классы с protected-полями</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 11. В реализации интерфейса три метода из пяти бросают UnsupportedOperationException. Нарушение какого принципа это выдаёт?</h4>

<div class="quiz-option" data-index="0">ISP — принцип разделения интерфейсов</div>
<div class="quiz-option" data-index="1">SRP — принцип единственной ответственности</div>
<div class="quiz-option" data-index="2">DIP — принцип инверсии зависимостей</div>
<div class="quiz-option" data-index="3">OCP — принцип открытости/закрытости</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 12. О чём говорит вызов new MySqlOrderRepository() прямо внутри класса OrderService?</h4>

<div class="quiz-option" data-index="0">Это корректное применение Фабричного метода</div>
<div class="quiz-option" data-index="1">Это нарушение принципа единственной ответственности</div>
<div class="quiz-option" data-index="2">Это нарушение принципа подстановки Лисков</div>
<div class="quiz-option" data-index="3">Это нарушение принципа инверсии зависимостей: бизнес-логика привязана к конкретной реализации</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 13. Как соотносятся DIP, DI и IoC?</h4>

<div class="quiz-option" data-index="0">Это три равнозначных названия одного и того же принципа</div>
<div class="quiz-option" data-index="1">DI — принцип, DIP — его реализация в Spring, IoC — название контейнера</div>
<div class="quiz-option" data-index="2">DIP — принцип зависеть от абстракций, DI — техника получения зависимостей извне, IoC — более общий принцип, частным случаем которого является DI</div>
<div class="quiz-option" data-index="3">IoC — принцип, DI — его нарушение, DIP — паттерн из каталога GoF</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 2: Порождающие паттерны (Вопросы 14–23) ===== -->

<div class="quiz-question" data-correct="1">
<h4>Вопрос 14. Зачем поле instance в Одиночке с двойной проверкой блокировки объявляют volatile?</h4>

<div class="quiz-option" data-index="0">Чтобы поле стало доступно из других пакетов</div>
<div class="quiz-option" data-index="1">Чтобы запретить переупорядочение операций: иначе другой поток может увидеть ссылку на ещё не достроенный объект</div>
<div class="quiz-option" data-index="2">Чтобы поле хранилось в стеке потока, а не в куче</div>
<div class="quiz-option" data-index="3">Чтобы синхронизировать доступ и обойтись без блока synchronized</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 15. Почему реализацию Одиночки через enum считают лучшей?</h4>

<div class="quiz-option" data-index="0">Перечисление занимает меньше памяти, чем обычный класс</div>
<div class="quiz-option" data-index="1">Перечисление позволяет при необходимости создать второй экземпляр</div>
<div class="quiz-option" data-index="2">Перечисление не требует ключевого слова static для полей</div>
<div class="quiz-option" data-index="3">JVM сама гарантирует единственность и потокобезопасность создания константы, а дубликат нельзя получить ни рефлексией, ни сериализацией</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 16. Какой scope у бина Spring по умолчанию и чем такой Одиночка отличается от классического?</h4>

<div class="quiz-option" data-index="0">singleton; экземпляр живёт в контейнере, а не в статическом поле, поэтому его легко подменить в тестах</div>
<div class="quiz-option" data-index="1">prototype; на каждый запрос из контекста создаётся новый экземпляр</div>
<div class="quiz-option" data-index="2">request; экземпляр создаётся на каждый HTTP-запрос</div>
<div class="quiz-option" data-index="3">singleton; экземпляр хранится в статическом поле самого класса-бина</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 17. Чем Абстрактная фабрика отличается от Фабричного метода?</h4>

<div class="quiz-option" data-index="0">Фабричный метод создаёт объекты рефлексией, Абстрактная фабрика — через конструктор</div>
<div class="quiz-option" data-index="1">Фабричный метод относится к структурным паттернам, Абстрактная фабрика — к порождающим</div>
<div class="quiz-option" data-index="2">Фабричный метод создаёт один продукт и передаёт выбор класса подклассу, Абстрактная фабрика создаёт согласованное семейство продуктов</div>
<div class="quiz-option" data-index="3">Разницы нет, это два названия одного паттерна</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 18. Какой из перечисленных методов JDK является настоящим Фабричным методом GoF?</h4>

<div class="quiz-option" data-index="0">Calendar.getInstance(): выбор класса спрятан внутри одного статического метода</div>
<div class="quiz-option" data-index="1">Collection.iterator(): конкретный класс итератора выбирает подкласс-коллекция</div>
<div class="quiz-option" data-index="2">Integer.valueOf(): метод возвращает объект из кеша</div>
<div class="quiz-option" data-index="3">HttpRequest.newBuilder(): метод возвращает строитель</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 19. Какую проблему решает Строитель?</h4>

<div class="quiz-option" data-index="0">Телескопический конструктор: десяток перегрузок под разные наборы необязательных параметров</div>
<div class="quiz-option" data-index="1">Невозможность создать более одного экземпляра класса</div>
<div class="quiz-option" data-index="2">Несовместимость интерфейсов двух библиотек</div>
<div class="quiz-option" data-index="3">Расход памяти на множество одинаковых объектов</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 20. Что выведет <code>System.out.println(Book.builder().title("Чистый код").author("Роберт Мартин").year(2008).build())</code> для класса Book из лекции?</h4>

<div class="quiz-option" data-index="0">Чистый код — Роберт Мартин (2008), ISBN: null</div>
<div class="quiz-option" data-index="1">Чистый код — Роберт Мартин (0), ISBN: не указан</div>
<div class="quiz-option" data-index="2">IllegalStateException: Название и автор обязательны</div>
<div class="quiz-option" data-index="3">Чистый код — Роберт Мартин (2008), ISBN: не указан</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 21. Что произойдёт при вызове <code>Book.builder().title("Рефакторинг").build()</code>?</h4>

<div class="quiz-option" data-index="0">Код не скомпилируется: вызов author() обязателен</div>
<div class="quiz-option" data-index="1">Метод build() бросит IllegalStateException, потому что автор не задан</div>
<div class="quiz-option" data-index="2">Создастся объект Book с полем author, равным «не указан»</div>
<div class="quiz-option" data-index="3">Создастся объект Book с полем author, равным null</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 22. Почему в методе clone() класса ReportTemplate обязательна строка copy.rows = new ArrayList&lt;&gt;(this.rows)?</h4>

<div class="quiz-option" data-index="0">Иначе clone() бросит CloneNotSupportedException</div>
<div class="quiz-option" data-index="1">Иначе копия получится неизменяемой</div>
<div class="quiz-option" data-index="2">Иначе сработает поверхностное копирование и копия с оригиналом будут делить один и тот же список</div>
<div class="quiz-option" data-index="3">Иначе clone() вернёт null вместо объекта</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 23. Что означает аннотация @Scope("prototype") у бина Spring?</h4>

<div class="quiz-option" data-index="0">Контейнер создаёт новый экземпляр бина на каждый запрос из контекста</div>
<div class="quiz-option" data-index="1">Контейнер клонирует существующий бин методом clone()</div>
<div class="quiz-option" data-index="2">Бин создаётся лениво при первом обращении, дальше переиспользуется</div>
<div class="quiz-option" data-index="3">Бин создаётся заново на каждый HTTP-запрос</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 3: Структурные паттерны (Вопросы 24–33) ===== -->

<div class="quiz-question" data-correct="3">
<h4>Вопрос 24. Какую задачу решает Адаптер?</h4>

<div class="quiz-option" data-index="0">Динамически добавляет объекту новые обязанности</div>
<div class="quiz-option" data-index="1">Даёт простой интерфейс к сложной подсистеме</div>
<div class="quiz-option" data-index="2">Разделяет абстракцию и реализацию, чтобы развивать их независимо</div>
<div class="quiz-option" data-index="3">Заставляет работать вместе классы с несовместимыми интерфейсами</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 25. Какая пара методов JDK является примером Адаптера?</h4>

<div class="quiz-option" data-index="0">BufferedReader и BufferedInputStream</div>
<div class="quiz-option" data-index="1">Arrays.asList() и Collections.list(Enumeration)</div>
<div class="quiz-option" data-index="2">StringBuilder и Stream.builder()</div>
<div class="quiz-option" data-index="3">Integer.valueOf() и пул строковых литералов</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 26. Видов уведомлений три, каналов отправки тоже три; наследование даёт девять классов. Какой паттерн решает эту проблему?</h4>

<div class="quiz-option" data-index="0">Компоновщик: девять классов объединяются в дерево</div>
<div class="quiz-option" data-index="1">Приспособленец: объекты кешируются и переиспользуются</div>
<div class="quiz-option" data-index="2">Мост: абстракция хранит ссылку на реализацию, поэтому виды и каналы растут независимо — 3 + 3 класса</div>
<div class="quiz-option" data-index="3">Одиночка: остаётся один экземпляр на все комбинации</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 27. Интерфейсы Connection и Statement плюс подставляемый драйвер конкретной СУБД — пример какого паттерна?</h4>

<div class="quiz-option" data-index="0">Фасад</div>
<div class="quiz-option" data-index="1">Адаптер</div>
<div class="quiz-option" data-index="2">Абстрактная фабрика</div>
<div class="quiz-option" data-index="3">Мост</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 28. Дерево собрано из файла pom.xml (2048 байт) и папки src с файлами Main.java (1024) и Service.java (4096). Что вернёт <code>root.size()</code> для Компоновщика из лекции?</h4>

<div class="quiz-option" data-index="0">7168</div>
<div class="quiz-option" data-index="1">2048</div>
<div class="quiz-option" data-index="2">5120</div>
<div class="quiz-option" data-index="3">3 — количество узлов в дереве</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 29. Что вернёт <code>new BracketsDecorator(new UpperCaseDecorator(new FileDataSource())).read()</code>, если FileDataSource.read() возвращает «данные отчёта»?</h4>

<div class="quiz-option" data-index="0">данные отчёта</div>
<div class="quiz-option" data-index="1">[ДАННЫЕ ОТЧЁТА]</div>
<div class="quiz-option" data-index="2">[данные отчёта]</div>
<div class="quiz-option" data-index="3">ДАННЫЕ ОТЧЁТА</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 30. Чем Декоратор отличается от Заместителя?</h4>

<div class="quiz-option" data-index="0">Декоратор реализует интерфейс, а Заместитель обязательно наследует класс</div>
<div class="quiz-option" data-index="1">Декоратор работает в рантайме, а Заместитель существует только на этапе компиляции</div>
<div class="quiz-option" data-index="2">Декоратор добавляет возможности и применяется клиентом осознанно, а Заместитель контролирует доступ и часто незаметен клиенту</div>
<div class="quiz-option" data-index="3">Декоратор применим только к интерфейсам, Заместитель — только к финальным классам</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 31. Какое утверждение о Фасаде верно?</h4>

<div class="quiz-option" data-index="0">Фасад запрещает обращаться к подсистемам напрямую</div>
<div class="quiz-option" data-index="1">Фасад обязан реализовывать тот же интерфейс, что и каждая подсистема</div>
<div class="quiz-option" data-index="2">Фасад создаёт объекты подсистем строго через абстрактную фабрику</div>
<div class="quiz-option" data-index="3">Фасад даёт удобный вход для типового сценария, но не запрещает прямой доступ к подсистемам</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 32. Почему для <code>Integer a = 127, b = 127</code> сравнение a == b даёт true, а для 128 — false?</h4>

<div class="quiz-option" data-index="0">Integer.valueOf() кеширует объекты для значений от −128 до 127 — это Приспособленец</div>
<div class="quiz-option" data-index="1">Значения до 127 умещаются в байт и потому сравниваются по значению</div>
<div class="quiz-option" data-index="2">Автоупаковка для чисел меньше 128 не выполняется</div>
<div class="quiz-option" data-index="3">JVM специально оптимизирует оператор == для малых чисел</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 33. Как в Приспособленце распределяется состояние объекта?</h4>

<div class="quiz-option" data-index="0">Всё состояние копируется в каждый объект, а экономия достигается сжатием</div>
<div class="quiz-option" data-index="1">Внутреннее — неизменяемое и общее — хранится в разделяемом объекте, внешнее (например, позиция) хранится отдельно</div>
<div class="quiz-option" data-index="2">Внутреннее состояние выносится в базу данных, внешнее остаётся в памяти</div>
<div class="quiz-option" data-index="3">Внешнее состояние делается статическим полем класса</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 4: Поведенческие паттерны (Вопросы 34–46) ===== -->

<div class="quiz-question" data-correct="2">
<h4>Вопрос 34. Цепочка собрана так: <code>Validator chain = new NotEmptyValidator(); chain.linkWith(new LengthValidator());</code> Что вернёт <code>chain.validate("ivanov", "12345")</code>?</h4>

<div class="quiz-option" data-index="0">true, в консоль ничего не выводится</div>
<div class="quiz-option" data-index="1">false, в консоль выводится «Логин и пароль не должны быть пустыми»</div>
<div class="quiz-option" data-index="2">false, в консоль выводится «Пароль короче 8 символов»</div>
<div class="quiz-option" data-index="3">true, но в консоль выводится предупреждение о длине пароля</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 35. Цепочка фильтров сервлетов и SecurityFilterChain в Spring Security — реализация какого паттерна?</h4>

<div class="quiz-option" data-index="0">Цепочка обязанностей</div>
<div class="quiz-option" data-index="1">Посредник</div>
<div class="quiz-option" data-index="2">Наблюдатель</div>
<div class="quiz-option" data-index="3">Компоновщик</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 36. Ради чего запрос превращают в объект в паттерне Команда?</h4>

<div class="quiz-option" data-index="0">Чтобы уменьшить число классов в проекте</div>
<div class="quiz-option" data-index="1">Чтобы гарантировать единственность обработчика запроса</div>
<div class="quiz-option" data-index="2">Чтобы скрыть сложную подсистему за простым интерфейсом</div>
<div class="quiz-option" data-index="3">Чтобы запрос можно было передать, поставить в очередь, залогировать и отменить</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 37. Объекты Runnable и Callable, передаваемые в ExecutorService.submit(), — пример какого паттерна?</h4>

<div class="quiz-option" data-index="0">Наблюдатель</div>
<div class="quiz-option" data-index="1">Команда</div>
<div class="quiz-option" data-index="2">Стратегия</div>
<div class="quiz-option" data-index="3">Посредник</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 38. Что верно об Интерпретаторе?</h4>

<div class="quiz-option" data-index="0">Он пригоден для языков любой сложности и заменяет генераторы парсеров</div>
<div class="quiz-option" data-index="1">Он превращает запрос в объект, чтобы операцию можно было отменить</div>
<div class="quiz-option" data-index="2">Он представляет выражение деревом объектов: в JDK так устроен Pattern, в Spring — SpEL, но для сложных грамматик берут ANTLR</div>
<div class="quiz-option" data-index="3">Он кеширует уже разобранные выражения, экономя память</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 39. Что даёт классу Shelf реализация интерфейса Iterable?</h4>

<div class="quiz-option" data-index="0">Объекты класса сразу работают в цикле for-each</div>
<div class="quiz-option" data-index="1">Класс становится потокобезопасным</div>
<div class="quiz-option" data-index="2">Класс получает метод stream() без дополнительного кода</div>
<div class="quiz-option" data-index="3">Класс автоматически получает реализации equals() и hashCode()</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 40. Какую задачу решает Посредник?</h4>

<div class="quiz-option" data-index="0">Сохраняет состояние объекта, чтобы позже его восстановить</div>
<div class="quiz-option" data-index="1">Передаёт запрос по цепочке обработчиков до первого подходящего</div>
<div class="quiz-option" data-index="2">Подставляет вместо объекта дублёра с тем же интерфейсом</div>
<div class="quiz-option" data-index="3">Убирает связи «каждый с каждым», заставляя объекты общаться через единый объект-посредник</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 41. Выполнено: <code>editor.type("Привет"); history.push(editor.save()); editor.type(", мир!"); editor.restore(history.pop());</code> Что вернёт editor.getText()?</h4>

<div class="quiz-option" data-index="0">Привет, мир!</div>
<div class="quiz-option" data-index="1">, мир!</div>
<div class="quiz-option" data-index="2">Привет</div>
<div class="quiz-option" data-index="3">Пустую строку</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 42. Что нужно сделать, чтобы при создании заказа выполнялось ещё одно действие — списание со склада?</h4>

<div class="quiz-option" data-index="0">Добавить в метод createOrder новую ветку if</div>
<div class="quiz-option" data-index="1">Подписать ещё одного слушателя; класс OrderService при этом не меняется</div>
<div class="quiz-option" data-index="2">Создать наследника OrderService и переопределить createOrder</div>
<div class="quiz-option" data-index="3">Заменить список слушателей на массив фиксированного размера</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 43. Какова цена паттерна Посетитель?</h4>

<div class="quiz-option" data-index="0">Новую операцию добавить легко, а новый тип узла тяжело: придётся править интерфейс посетителя и все его реализации</div>
<div class="quiz-option" data-index="1">Новый тип узла добавить легко, а новую операцию тяжело</div>
<div class="quiz-option" data-index="2">Паттерн требует рефлексии и потому работает медленно</div>
<div class="quiz-option" data-index="3">Паттерн применим только к неизменяемым объектам</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 44. Чем Состояние отличается от Стратегии, если структурно они почти одинаковы?</h4>

<div class="quiz-option" data-index="0">Стратегия — структурный паттерн, Состояние — поведенческий</div>
<div class="quiz-option" data-index="1">Стратегия построена на наследовании, Состояние — только на композиции</div>
<div class="quiz-option" data-index="2">Состояние применимо лишь к перечислениям, Стратегия — к любым классам</div>
<div class="quiz-option" data-index="3">В Стратегии алгоритм задаёт клиент извне, а в Состоянии следующий переход выбирает сам объект состояния</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 45. Для объекта Order из лекции выполнили <code>order.pay(); order.cancel();</code> Что вернёт order.status()?</h4>

<div class="quiz-option" data-index="0">ОПЛАЧЕН</div>
<div class="quiz-option" data-index="1">ОТМЕНЁН</div>
<div class="quiz-option" data-index="2">НОВЫЙ</div>
<div class="quiz-option" data-index="3">Будет брошено IllegalStateException</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 46. Зачем шаблонный метод importData() объявлен final?</h4>

<div class="quiz-option" data-index="0">Чтобы его можно было вызвать без создания объекта</div>
<div class="quiz-option" data-index="1">Чтобы JVM смогла заинлайнить вызов и ускорить импорт</div>
<div class="quiz-option" data-index="2">Чтобы подклассы не переопределили структуру алгоритма: порядок шагов и обработка ошибок остаются за базовым классом</div>
<div class="quiz-option" data-index="3">Чтобы подклассы были обязаны реализовать все его шаги</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 5: Паттерны в JDK и Spring (Вопросы 47–50) ===== -->

<div class="quiz-question" data-correct="0">
<h4>Вопрос 47. В выражении <code>new BufferedReader(new InputStreamReader(new FileInputStream("data.txt"), StandardCharsets.UTF_8))</code> какую роль играет InputStreamReader?</h4>

<div class="quiz-option" data-index="0">Адаптера: превращает байтовый поток в символьный</div>
<div class="quiz-option" data-index="1">Декоратора: добавляет буферизацию и метод readLine()</div>
<div class="quiz-option" data-index="2">Фасада: прячет работу с файловой системой</div>
<div class="quiz-option" data-index="3">Заместителя: контролирует доступ к файлу</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 48. Чем является JdbcTemplate с точки зрения паттернов?</h4>

<div class="quiz-option" data-index="0">Только Адаптером JDBC к типам Spring</div>
<div class="quiz-option" data-index="1">Только Одиночкой, поскольку это бин со scope singleton</div>
<div class="quiz-option" data-index="2">Абстрактной фабрикой соединений с базой данных</div>
<div class="quiz-option" data-index="3">Шаблонным методом и одновременно Фасадом над JDBC, а RowMapper выступает Стратегией</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 49. Почему @Transactional не срабатывает при вызове метода изнутри того же класса?</h4>

<div class="quiz-option" data-index="0">Потому что аннотации не наследуются подклассами</div>
<div class="quiz-option" data-index="1">Потому что вызов this.method() идёт мимо объекта-заместителя, который и открывает транзакцию</div>
<div class="quiz-option" data-index="2">Потому что Spring не проксирует методы, возвращающие void</div>
<div class="quiz-option" data-index="3">Потому что вложенные транзакции в Spring запрещены</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 50. Утверждение «любой бин, внедряемый через интерфейс, — это ...» завершается словом:</h4>

<div class="quiz-option" data-index="0">Стратегия, а Spring выступает механизмом её подстановки</div>
<div class="quiz-option" data-index="1">Одиночка, потому что бины по умолчанию имеют scope singleton</div>
<div class="quiz-option" data-index="2">Прототип, потому что бин можно создать заново</div>
<div class="quiz-option" data-index="3">Компоновщик, потому что контекст хранит дерево бинов</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 6: Антипаттерны и рефакторинг (Вопросы 51–60) ===== -->

<div class="quiz-question" data-correct="2">
<h4>Вопрос 51. Класс LibraryManager на 2000 строк добавляет книги, регистрирует читателей, верстает отчёты, шлёт письма и делает бэкап базы. Какой это антипаттерн и как его лечить?</h4>

<div class="quiz-option" data-index="0">Spaghetti Code; лечится ранними возвратами</div>
<div class="quiz-option" data-index="1">Lava Flow; лечится удалением мёртвого кода</div>
<div class="quiz-option" data-index="2">God Object; лечится Extract Class — разбиением по группам данных и передачей зависимостей через конструктор</div>
<div class="quiz-option" data-index="3">Golden Hammer; лечится сравнением альтернативных технологий</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 52. Метод checkOrder переписан через ранние возвраты (guard clauses). Что он вернёт, если order не null, order.getItems() не null, но список позиций пуст?</h4>

<div class="quiz-option" data-index="0">нет заказа</div>
<div class="quiz-option" data-index="1">нет позиций</div>
<div class="quiz-option" data-index="2">ok</div>
<div class="quiz-option" data-index="3">пустой заказ</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 53. Что делать с большими закомментированными блоками кода, оставленными «на всякий случай»?</h4>

<div class="quiz-option" data-index="0">Оставить, снабдив комментарием с датой и автором</div>
<div class="quiz-option" data-index="1">Удалить: история хранится в Git, а мёртвый код обходится дорого при каждом чтении и рефакторинге</div>
<div class="quiz-option" data-index="2">Перенести в отдельный класс DeprecatedUtils</div>
<div class="quiz-option" data-index="3">Заменить на методы-заглушки, бросающие UnsupportedOperationException</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 54. Команда, знающая только Hibernate, тянет ORM в задачу ночной агрегации 50 миллионов строк. Какой это антипаттерн?</h4>

<div class="quiz-option" data-index="0">Golden Hammer — один привычный инструмент применяется ко всем задачам подряд</div>
<div class="quiz-option" data-index="1">Premature Optimization — оптимизация без предварительных замеров</div>
<div class="quiz-option" data-index="2">Feature Envy — метод тянет данные чужого класса</div>
<div class="quiz-option" data-index="3">Shotgun Surgery — одно изменение задевает десяток файлов</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 55. В коде встретилось <code>if (status == 3) return daysOverdue * 0.13 * 30;</code> Как правильно это исправить?</h4>

<div class="quiz-option" data-index="0">Добавить комментарий, поясняющий смысл каждого числа</div>
<div class="quiz-option" data-index="1">Вынести метод в отдельный класс-утилиту</div>
<div class="quiz-option" data-index="2">Ввести перечисление статусов и именованные константы для ставки и расчётного периода</div>
<div class="quiz-option" data-index="3">Сделать числа параметрами метода, чтобы их передавал вызывающий код</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 56. Добавление одного поля требует правок в сущности, DTO, маппере, форме, валидаторе и трёх отчётах. Что это и как связано с God Object?</h4>

<div class="quiz-option" data-index="0">Это God Object; Shotgun Surgery — его частный случай</div>
<div class="quiz-option" data-index="1">Это Copy-Paste Programming; лечится обобщениями</div>
<div class="quiz-option" data-index="2">Это Big Ball of Mud; лечится переписыванием с нуля</div>
<div class="quiz-option" data-index="3">Это Shotgun Surgery — обратная сторона God Object: ответственность размазана слишком тонко</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 57. Что на самом деле утверждает принцип DRY?</h4>

<div class="quiz-option" data-index="0">Не дублируйте знание: куски, меняющиеся по одной причине, объединяют, а внешне похожие, но независимые — нет</div>
<div class="quiz-option" data-index="1">В проекте не должно быть двух одинаковых строк кода</div>
<div class="quiz-option" data-index="2">Любой повторяющийся блок нужно вынести в статический метод-утилиту</div>
<div class="quiz-option" data-index="3">Каждый класс должен использоваться минимум в двух местах</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 58. Метод OrderPrinter.describe() собирает данные цепочками вида order.getClient().getAddress().getCity(). Как это лечить?</h4>

<div class="quiz-option" data-index="0">Добавить в OrderPrinter кеш полученных значений</div>
<div class="quiz-option" data-index="1">Переместить метод туда, где живут данные (Move Method), и следовать правилу «tell, don't ask»</div>
<div class="quiz-option" data-index="2">Сделать поля Order публичными, чтобы избавиться от геттеров</div>
<div class="quiz-option" data-index="3">Внедрить Order в OrderPrinter через конструктор</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 59. Какой порядок работы над производительностью правильный?</h4>

<div class="quiz-option" data-index="0">Сразу заменить стримы на циклы и завести пулы объектов, а логику писать потом</div>
<div class="quiz-option" data-index="1">Оптимизировать всё, что выглядит медленным, ещё на этапе проектирования</div>
<div class="quiz-option" data-index="2">Сначала написать корректно и читаемо, затем измерить профилировщиком, оптимизировать найденное узкое место и измерить снова</div>
<div class="quiz-option" data-index="3">Оптимизировать только после жалоб пользователей и без всяких замеров</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 60. SQL-запросы в контроллерах, генерация HTML в репозиториях, циклические зависимости пакетов. Что делать с такой системой?</h4>

<div class="quiz-option" data-index="0">Переписать с нуля — только это даёт гарантированный результат</div>
<div class="quiz-option" data-index="1">Ввести Одиночку для доступа к базе, чтобы централизовать работу со слоями</div>
<div class="quiz-option" data-index="2">Сначала оптимизировать самые медленные места, архитектура подтянется следом</div>
<div class="quiz-option" data-index="3">Провести границы слоёв, покрыть тестами изменяемые участки и постепенно вытеснять старый код, следя за метриками</div>
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
    'Вопрос 1': 'Паттерн — это идея структуры, а не код для копирования: в каждом проекте и на каждом языке она реализуется по-своему.',
    'Вопрос 2': 'Описание паттерна всегда включает и цену применения — раздел «Последствия»: что вы получаете и чем за это платите.',
    'Вопрос 3': 'Деление идёт по вопросу, на который отвечает паттерн: откуда взялся объект, из чего он состоит, как объекты договариваются между собой.',
    'Вопрос 4': 'Поведенческие паттерны отвечают за распределение обязанностей и способы общения объектов, а не за их создание или сборку в структуры.',
    'Вопрос 5': 'Один случай пишут прямо, на двух терпят и только на третьем обобщают — так абстракция появляется из реальной потребности, а не из фантазии о будущем.',
    'Вопрос 6': 'Паттерн — лекарство от конкретной боли: если читать стало сложнее, а менять легче не стало, вы усложнили код на пустом месте.',
    'Вопрос 7': 'У класса три независимые причины для изменения — правила расчёта, вёрстка и почтовый сервис, — а по SRP причина должна быть одна.',
    'Вопрос 8': 'Каждая новая фигура требует править работающий метод, тогда как OCP требует расширять систему добавлением кода, а не правкой существующего.',
    'Вопрос 9': 'Square.setHeight приравнивает ширину к высоте, поэтому обе стороны равны 4 и площадь равна 16, хотя код, написанный под Rectangle, ожидал 20.',
    'Вопрос 10': 'Наследование — это обещание вести себя как родитель; квадрат его не выполняет. У неизменяемых объектов такой проблемы обычно не возникает, потому что рассогласовываться нечему.',
    'Вопрос 11': 'Интерфейс оказался «толстым»: клиента заставили зависеть от методов, которых он не умеет выполнять. Лечится разбиением на интерфейсы-роли.',
    'Вопрос 12': 'По DIP модуль верхнего уровня должен зависеть от интерфейса OrderRepository и получать реализацию извне, а не создавать её сам.',
    'Вопрос 13': 'Внедрение через конструктор — это техника (DI), которой достигают принципа DIP, а инверсия управления охватывает не только зависимости, но и управление жизненным циклом.',
    'Вопрос 14': 'Без volatile JVM вправе сделать ссылку ненулевой раньше, чем закончится конструктор, и второй поток получит полуготовый объект.',
    'Вопрос 15': 'Ручные реализации приходится защищать от рефлексии и десериализации отдельно, а для enum эти гарантии даёт сама виртуальная машина.',
    'Вопрос 16': 'Контейнер создаёт один экземпляр на контекст приложения, но глобального статического состояния не появляется: зависимость по-прежнему внедряется и подменяется.',
    'Вопрос 17': 'Абстрактная фабрика не даст смешать тёмную кнопку со светлым чекбоксом: клиент получает набор объектов строго из одного семейства.',
    'Вопрос 18': 'Настоящий Фабричный метод — только Collection.iterator(): каждая коллекция сама решает, какой класс итератора вернуть. А Calendar.getInstance() и NumberFormat.getInstance() — статические фабрики, а не паттерн GoF: выбор класса спрятан в одном методе, подкласс в нём не участвует.',
    'Вопрос 19': 'Строитель заменяет перегрузки именованными шагами и позволяет один раз проверить обязательные поля в методе build().',
    'Вопрос 20': 'Поле isbn инициализировано прямо в строителе значением по умолчанию «не указан», поэтому null в готовый объект не попадёт.',
    'Вопрос 21': 'Валидация вынесена в build() и выполняется до создания объекта, поэтому недостроенный Book в систему не попадёт.',
    'Вопрос 22': 'Object.clone() копирует поля «как есть», то есть ссылки: изменение списка в копии тут же отразилось бы на оригинале.',
    'Вопрос 23': 'Это спринговое отражение идеи Прототипа: вместо одного разделяемого экземпляра каждый потребитель получает свой. Привязка к HTTP-запросу — это уже scope request.',
    'Вопрос 24': 'Ни чужую библиотеку, ни собственный интерфейс менять нельзя, поэтому между ними ставят переходник — как между европейской вилкой и британской розеткой.',
    'Вопрос 25': 'Оба превращают чужую форму представления данных — массив или Enumeration — в ожидаемый интерфейс List, не меняя сам источник.',
    'Вопрос 26': 'Мост разрывает комбинаторный взрыв наследования, вынося вторую ось изменений в отдельную иерархию.',
    'Вопрос 27': 'Абстракция (JDBC API) и реализация (драйвер) развиваются независимо: приложение пишется один раз, а база данных меняется подстановкой драйвера.',
    'Вопрос 28': 'Folder.size() рекурсивно суммирует размеры детей, поэтому клиент получает вес всего поддерева и не различает файл и папку.',
    'Вопрос 29': 'Обёртки срабатывают изнутри наружу: сначала внутренний декоратор переводит текст в верхний регистр, затем внешний добавляет скобки.',
    'Вопрос 30': 'Структурно паттерны почти одинаковы — оба реализуют интерфейс и хранят ссылку на объект, — поэтому различают их по намерению.',
    'Вопрос 31': 'Задача Фасада — упростить частый путь, а не закрыть подсистему: для нестандартной задачи с ней по-прежнему работают напрямую.',
    'Вопрос 32': 'Кеш возвращает один и тот же разделяемый объект, поэтому ссылки совпадают; за границей кеша создаются разные объекты и == даёт false.',
    'Вопрос 33': 'Разделять можно только то, что не меняется: типографская литера общая для всех вхождений буквы, а её позиция на странице у каждого вхождения своя.',
    'Вопрос 34': 'Первый обработчик проверку проходит и передаёт запрос дальше, а второй видит пароль из пяти символов и обрывает цепочку значением false.',
    'Вопрос 35': 'Каждый фильтр либо обрабатывает запрос сам, либо передаёт его следующему звену — это буквальное описание паттерна.',
    'Вопрос 36': 'Пока действие остаётся вызовом метода, его нельзя сохранить в истории; став объектом, оно поддерживает и очередь, и отмену.',
    'Вопрос 37': 'Задача упакована в объект, который пул складывает в очередь и выполняет позже, — ровно та цель, ради которой паттерн придуман.',
    'Вопрос 38': 'Каждый элемент грамматики становится классом, а вычисление — обходом дерева; при росте грамматики число классов становится неуправляемым.',
    'Вопрос 39': 'Цикл for-each — синтаксический сахар над итератором, поэтому достаточно вернуть Iterator из метода iterator().',
    'Вопрос 40': 'Участники чата не знают друг о друге — они знают только ChatRoom, как самолёты знают только диспетчерскую вышку.',
    'Вопрос 41': 'Снимок сделан до второго ввода и хранит текст «Привет», поэтому восстановление откатывает редактор именно к этому моменту.',
    'Вопрос 42': 'За это Наблюдателя и ценят: новая реакция добавляется без правки источника события — принцип OCP в действии.',
    'Вопрос 43': 'Поэтому Посетитель выбирают, когда набор типов стабилен, а операций много; в Java 21 ту же задачу часто решают sealed-интерфейс и switch с сопоставлением с образцом.',
    'Вопрос 44': 'Разница в намерении и в том, кто принимает решение: стратегии не знают друг о друге, а состояния знают соседей по автомату.',
    'Вопрос 45': 'Из состояния «оплачен» отмена разрешена и выполняется с возвратом средств, переводя заказ в «отменён»; исключение бросила бы повторная оплата.',
    'Вопрос 46': 'Подклассам оставлены отдельные шаги, а инвариант — открыть, прочитать, обработать, закрыть в finally — защищён от переопределения.',
    'Вопрос 47': 'Байты и символы — несовместимые интерфейсы, и переходник между ними и есть Адаптер; буферизацию добавляет уже BufferedReader, а он Декоратор.',
    'Вопрос 48': 'Неизменную часть работы — соединение, PreparedStatement, обход ResultSet, закрытие — выполняет шаблон, а сменный шаг отображения строки передаётся снаружи.',
    'Вопрос 49': 'В контекст контейнер кладёт не ваш объект, а прокси-обёртку; внутренний вызов через неё не проходит, поэтому транзакционный код не выполняется.',
    'Вопрос 50': 'Клиент работает с абстракцией, а конкретный алгоритм подставляется извне — это ровно определение Стратегии, только подстановкой занимается контейнер.',
    'Вопрос 51': 'Признак божественного объекта — несвязанные обязанности в одном классе, который задевает любая правка; это прямое нарушение SRP.',
    'Вопрос 52': 'Проверки идут по порядку: первые две пройдены, срабатывает третья — isEmpty(). Ранние возвраты дают тот же результат, что и вложенные if, но при нулевой вложенности.',
    'Вопрос 53': 'Это антипаттерн Lava Flow: за такой код платят при каждом обновлении API и вводят в заблуждение новых разработчиков, а страховкой служит система контроля версий.',
    'Вопрос 54': 'Противоядие — явно сравнивать альтернативы: формулировать, какую конкретную проблему технология решает и чем вы за это платите.',
    'Вопрос 55': 'Именованные константы и enum делают код самообъясняющим, а ставка меняется в одном месте; комментарий устаревает и не защищает от пропущенного вхождения числа.',
    'Вопрос 56': 'В God Object ответственность собрана слишком густо, здесь — рассеяна; лечение по смыслу одно: собрать связанную логику в классе-владельце правила.',
    'Вопрос 57': 'Объединение кусков, которые совпали случайно и меняются по разным причинам, порождает Shotgun Surgery, поэтому речь идёт о знании, а не о совпадении символов.',
    'Вопрос 58': 'Это Feature Envy: логика оторвана от данных, поэтому любое изменение структуры Order ломает чужой класс и нарушает инкапсуляцию.',
    'Вопрос 59': 'Оптимизация без замеров — гадание: в типичном веб-приложении узким местом оказываются база и сеть, а не арифметика в Java.',
    'Вопрос 60': 'Это Big Ball of Mud — финальная стадия накопления антипаттернов; переписывание с нуля почти всегда проваливается, работает постепенное вытеснение под защитой тестов.'
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
