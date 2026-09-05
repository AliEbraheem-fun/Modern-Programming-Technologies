# Тест 9: Реализация графических интерфейсов: JavaFX (Лекция 9)

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

<!-- ===== РАЗДЕЛ 1: Платформа JavaFX и подключение (Вопросы 1–10) ===== -->

<div class="quiz-question" data-correct="0">
<h4>Вопрос 1. Какими были компоненты библиотеки AWT и в чём это ограничивало разработчика?</h4>

<div class="quiz-option" data-index="0">Тяжеловесными: их создавала операционная система, поэтому набор элементов пришлось урезать до общего знаменателя всех платформ</div>
<div class="quiz-option" data-index="1">Легковесными: Java рисовала их сама, поэтому они работали заметно медленнее системных</div>
<div class="quiz-option" data-index="2">Аппаратно ускоренными: их рисовала видеокарта, поэтому AWT не работал на серверах без графики</div>
<div class="quiz-option" data-index="3">Описанными в XML: разметка была отделена от кода, но не поддерживала стилизацию</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 2. Что принципиально нового появилось в JavaFX по сравнению со Swing?</h4>

<div class="quiz-option" data-index="0">Только более быстрая отрисовка, набор возможностей остался прежним</div>
<div class="quiz-option" data-index="1">Возможность запускать настольные приложения без установленной JVM</div>
<div class="quiz-option" data-index="2">Тяжеловесные системные компоненты, как в AWT, вместо легковесных</div>
<div class="quiz-option" data-index="3">Разметка в отдельном файле FXML, оформление через CSS, свойства и привязки, аппаратное ускорение</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 3. Начиная с какой версии JDK JavaFX больше не поставляется вместе с JDK?</h4>

<div class="quiz-option" data-index="0">JDK 8</div>
<div class="quiz-option" data-index="1">JDK 9</div>
<div class="quiz-option" data-index="2">JDK 11</div>
<div class="quiz-option" data-index="3">JDK 17</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 4. Как называется открытый проект, в котором JavaFX развивается сегодня?</h4>

<div class="quiz-option" data-index="0">OpenJDK</div>
<div class="quiz-option" data-index="1">OpenJFX</div>
<div class="quiz-option" data-index="2">Gluon Mobile</div>
<div class="quiz-option" data-index="3">GraalVM</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 5. В каком модуле JavaFX лежат элементы управления <code>Button</code>, <code>Label</code> и <code>TableView</code>?</h4>

<div class="quiz-option" data-index="0">javafx-base</div>
<div class="quiz-option" data-index="1">javafx-graphics</div>
<div class="quiz-option" data-index="2">javafx-controls</div>
<div class="quiz-option" data-index="3">javafx-fxml</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 6. Какие зависимости достаточно объявить в pom.xml для приложения с обычными элементами управления и разметкой FXML?</h4>

<div class="quiz-option" data-index="0">javafx-base и javafx-media</div>
<div class="quiz-option" data-index="1">javafx-graphics и javafx-web</div>
<div class="quiz-option" data-index="2">Все семь модулей JavaFX, иначе приложение не запустится</div>
<div class="quiz-option" data-index="3">javafx-controls и javafx-fxml</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 7. Почему у зависимостей <code>org.openjfx</code> в pom.xml обычно не указывают classifier (win, mac, linux)?</h4>

<div class="quiz-option" data-index="0">Потому что JavaFX целиком написан на Java и от операционной системы не зависит</div>
<div class="quiz-option" data-index="1">Потому что их POM сам определяет текущую операционную систему и подставляет нужную сборку</div>
<div class="quiz-option" data-index="2">Потому что classifier поддерживается только в Gradle, а в Maven игнорируется</div>
<div class="quiz-option" data-index="3">Потому что нативные библиотеки скачиваются при первом запуске приложения</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 8. Какой командой запускается JavaFX-приложение, если в pom.xml подключён <code>javafx-maven-plugin</code>?</h4>

<div class="quiz-option" data-index="0">mvn spring-boot:run</div>
<div class="quiz-option" data-index="1">mvn javafx:run</div>
<div class="quiz-option" data-index="2">mvn exec:exec</div>
<div class="quiz-option" data-index="3">mvn package, а затем java -jar target/app.jar</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 9. При запуске из IDE появляется «Error: JavaFX runtime components are missing, and are required to run this application». Какой обход считается надёжным?</h4>

<div class="quiz-option" data-index="0">Создать отдельный класс-запускалку, который не наследует Application, и запускать его</div>
<div class="quiz-option" data-index="1">Перейти на JDK 8, где JavaFX ещё входил в состав JDK</div>
<div class="quiz-option" data-index="2">Добавить в зависимости classifier своей операционной системы</div>
<div class="quiz-option" data-index="3">Заменить наследование Application на реализацию интерфейса Runnable</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 10. Какой компонент архитектуры JavaFX отвечает за отрисовку через Direct3D или OpenGL?</h4>

<div class="quiz-option" data-index="0">Glass</div>
<div class="quiz-option" data-index="1">Quantum Toolkit</div>
<div class="quiz-option" data-index="2">Prism</div>
<div class="quiz-option" data-index="3">WebKit</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 2: Application и жизненный цикл (Вопросы 11–18) ===== -->

<div class="quiz-question" data-correct="2">
<h4>Вопрос 11. С чего начинается любое JavaFX-приложение?</h4>

<div class="quiz-option" data-index="0">С класса, помеченного аннотацией @JavaFXApplication</div>
<div class="quiz-option" data-index="1">С класса, реализующего интерфейс Runnable</div>
<div class="quiz-option" data-index="2">С класса, наследующего <code>javafx.application.Application</code> и реализующего метод <code>start(Stage)</code></div>
<div class="quiz-option" data-index="3">С класса, наследующего Stage и переопределяющего метод show()</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 12. В каком порядке выполняются шаги жизненного цикла JavaFX-приложения?</h4>

<div class="quiz-option" data-index="0">init() → launch() → start() → stop()</div>
<div class="quiz-option" data-index="1">launch() → start() → init() → stop()</div>
<div class="quiz-option" data-index="2">start() → init() → stop() → launch()</div>
<div class="quiz-option" data-index="3">launch() → init() → start() → stop()</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 13. Методы <code>init()</code>, <code>start()</code> и <code>stop()</code> печатают буквы A, B и C соответственно. Что появится в консоли, если запустить приложение и затем закрыть единственное окно?</h4>

<div class="quiz-option" data-index="0">ABC</div>
<div class="quiz-option" data-index="1">BAC</div>
<div class="quiz-option" data-index="2">AB — метод stop() при закрытии окна не вызывается</div>
<div class="quiz-option" data-index="3">ACB</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 14. В каком потоке выполняется метод <code>init()</code>?</h4>

<div class="quiz-option" data-index="0">В JavaFX Application Thread, как и start()</div>
<div class="quiz-option" data-index="1">В потоке main</div>
<div class="quiz-option" data-index="2">В общем пуле ForkJoinPool.commonPool()</div>
<div class="quiz-option" data-index="3">В отдельном потоке JavaFX-Launcher</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 15. Почему в <code>init()</code> нельзя создавать <code>Stage</code> и <code>Scene</code>?</h4>

<div class="quiz-option" data-index="0">Потому что эти объекты умеет создавать только загрузчик FXML</div>
<div class="quiz-option" data-index="1">Потому что init() выполняется не в потоке интерфейса и до того, как окно вообще создано</div>
<div class="quiz-option" data-index="2">Потому что init() может быть вызван несколько раз подряд</div>
<div class="quiz-option" data-index="3">Потому что в init() ещё не разобраны аргументы командной строки</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 16. Чем <code>System.exit(0)</code> отличается от <code>Platform.exit()</code> в JavaFX-приложении?</h4>

<div class="quiz-option" data-index="0">Ничем: оба корректно завершают среду выполнения и вызывают stop()</div>
<div class="quiz-option" data-index="1">Platform.exit() закрывает только текущее окно, а приложение продолжает работать</div>
<div class="quiz-option" data-index="2">System.exit(0) убивает JVM немедленно, поэтому метод stop() не выполняется</div>
<div class="quiz-option" data-index="3">System.exit(0) вызывает stop(), а Platform.exit() завершает работу без него</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 17. Фоновый поток выполняет <code>statusLabel.setText("Готово")</code> напрямую. Что произойдёт?</h4>

<div class="quiz-option" data-index="0">Текст обновится: JavaFX сам переключится в нужный поток</div>
<div class="quiz-option" data-index="1">Ничего не произойдёт, вызов будет молча проигнорирован</div>
<div class="quiz-option" data-index="2">Будет выброшено IllegalStateException: Not on FX application thread</div>
<div class="quiz-option" data-index="3">Приложение зависнет до завершения фонового потока</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 18. Почему классу-наследнику <code>Application</code> нужен public-конструктор без аргументов?</h4>

<div class="quiz-option" data-index="0">Этого требует спецификация FXML</div>
<div class="quiz-option" data-index="1">launch() создаёт экземпляр приложения через рефлексию</div>
<div class="quiz-option" data-index="2">Иначе не заработает механизм привязок</div>
<div class="quiz-option" data-index="3">Так требует сборщик мусора при выгрузке приложения</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 3: Stage, Scene и граф сцены (Вопросы 19–28) ===== -->

<div class="quiz-question" data-correct="0">
<h4>Вопрос 19. Что такое <code>Stage</code> в терминологии JavaFX?</h4>

<div class="quiz-option" data-index="0">Окно верхнего уровня операционной системы: рама, заголовок, кнопки свернуть и закрыть</div>
<div class="quiz-option" data-index="1">Всё содержимое окна: корневой узел вместе с потомками</div>
<div class="quiz-option" data-index="2">Отдельный узел графа сцены, отвечающий за отрисовку</div>
<div class="quiz-option" data-index="3">Таблица стилей, применяемая ко всему приложению</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 20. Чем <code>show()</code> отличается от <code>showAndWait()</code> у <code>Stage</code>?</h4>

<div class="quiz-option" data-index="0">show() показывает окно модально, а showAndWait() — обычным</div>
<div class="quiz-option" data-index="1">show() возвращает управление сразу, а showAndWait() блокирует выполнение до закрытия окна</div>
<div class="quiz-option" data-index="2">show() показывает окно, а showAndWait() только готовит его к показу</div>
<div class="quiz-option" data-index="3">Отличий нет: showAndWait() — устаревший синоним show()</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 21. Какое значение блокирует все окна приложения, пока открыт диалог?</h4>

<div class="quiz-option" data-index="0">Modality.NONE</div>
<div class="quiz-option" data-index="1">Modality.APPLICATION_MODAL</div>
<div class="quiz-option" data-index="2">Modality.WINDOW_MODAL</div>
<div class="quiz-option" data-index="3">StageStyle.UTILITY</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 22. Как отменить закрытие окна крестиком, если в форме остались несохранённые данные?</h4>

<div class="quiz-option" data-index="0">Вызвать stage.setResizable(false)</div>
<div class="quiz-option" data-index="1">Переопределить метод stop() и вернуть из него false</div>
<div class="quiz-option" data-index="2">Вызвать Platform.setImplicitExit(false)</div>
<div class="quiz-option" data-index="3">В обработчике <code>setOnCloseRequest</code> вызвать <code>event.consume()</code></div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 23. Каким должен быть корневой узел, передаваемый в конструктор <code>Scene</code>?</h4>

<div class="quiz-option" data-index="0">Любым наследником Node</div>
<div class="quiz-option" data-index="1">Обязательно объектом класса Group</div>
<div class="quiz-option" data-index="2">Наследником <code>Parent</code> — то есть узлом, способным иметь потомков</div>
<div class="quiz-option" data-index="3">Обязательно объектом класса AnchorPane</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 24. Что произойдёт, если одну и ту же <code>Scene</code> установить сразу в два разных <code>Stage</code>?</h4>

<div class="quiz-option" data-index="0">Так делать нельзя: одна сцена может принадлежать только одному окну</div>
<div class="quiz-option" data-index="1">Оба окна покажут одинаковое содержимое и будут синхронизированы</div>
<div class="quiz-option" data-index="2">Второе окно покажет независимую копию сцены</div>
<div class="quiz-option" data-index="3">Сцена отрисуется в первом окне, а события начнут приходить во второе</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 25. Чем <code>javafx.scene.text.Text</code> отличается от <code>javafx.scene.control.Label</code>?</h4>

<div class="quiz-option" data-index="0">Text — устаревший синоним Label</div>
<div class="quiz-option" data-index="1">Text поддерживает CSS, а Label оформляется только из кода</div>
<div class="quiz-option" data-index="2">Text — это фигура (Shape) для графики, а Label — элемент управления (Control) для подписей в интерфейсе</div>
<div class="quiz-option" data-index="3">Text умеет показывать картинку рядом с текстом, а Label — только строку</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 26. Кнопку добавили в две панели подряд: <code>vbox.getChildren().add(button); hbox.getChildren().add(button);</code> Что окажется на экране?</h4>

<div class="quiz-option" data-index="0">Кнопка появится сразу в обеих панелях</div>
<div class="quiz-option" data-index="1">Кнопка останется в VBox, а второе добавление будет проигнорировано</div>
<div class="quiz-option" data-index="2">Будет выброшено IllegalArgumentException: duplicate children</div>
<div class="quiz-option" data-index="3">Кнопка окажется только в HBox — из VBox она исчезнет</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 27. Чем в JavaFX определяется, какой узел окажется поверх других?</h4>

<div class="quiz-option" data-index="0">Свойством -fx-z-index в таблице стилей</div>
<div class="quiz-option" data-index="1">Позицией узла в списке <code>getChildren()</code>: чем позже добавлен, тем выше</div>
<div class="quiz-option" data-index="2">Значением setOpacity(): непрозрачные узлы рисуются поверх полупрозрачных</div>
<div class="quiz-option" data-index="3">Порядком объявления полей в классе-контроллере</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 28. Метку спрятали вызовом <code>setVisible(false)</code>, но на её месте осталась пустая «дырка». Что нужно сделать?</h4>

<div class="quiz-option" data-index="0">Дополнительно вызвать <code>setManaged(false)</code>, чтобы узел перестал занимать место в раскладке</div>
<div class="quiz-option" data-index="1">Вызвать setOpacity(0) — это освободит место</div>
<div class="quiz-option" data-index="2">Удалить узел из графа сцены, других способов нет</div>
<div class="quiz-option" data-index="3">Вызвать setDisable(true) вместо setVisible(false)</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 4: Компоновки и элементы управления (Вопросы 29–40) ===== -->

<div class="quiz-question" data-correct="0">
<h4>Вопрос 29. Какая панель компоновки располагает потомков в строку слева направо?</h4>

<div class="quiz-option" data-index="0">HBox</div>
<div class="quiz-option" data-index="1">VBox</div>
<div class="quiz-option" data-index="2">TilePane</div>
<div class="quiz-option" data-index="3">BorderPane</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 30. Как <code>BorderPane</code> распределяет место между своими зонами?</h4>

<div class="quiz-option" data-index="0">Делит окно на пять равных прямоугольников</div>
<div class="quiz-option" data-index="1">Все зоны получают размер по содержимому, а лишнее место остаётся пустым</div>
<div class="quiz-option" data-index="2">Зоны top, bottom, left и right занимают место по содержимому, а центр забирает всё оставшееся</div>
<div class="quiz-option" data-index="3">Место делится пропорционально значениям Priority, заданным для каждой зоны</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 31. Какая панель кладёт все потомки друг на друга по центру — например, индикатор загрузки поверх содержимого?</h4>

<div class="quiz-option" data-index="0">FlowPane</div>
<div class="quiz-option" data-index="1">AnchorPane</div>
<div class="quiz-option" data-index="2">TilePane</div>
<div class="quiz-option" data-index="3">StackPane</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 32. Куда попадёт узел после вызова <code>grid.add(new Label("Пароль:"), 0, 1);</code>?</h4>

<div class="quiz-option" data-index="0">В столбец 0, строку 1</div>
<div class="quiz-option" data-index="1">В строку 0, столбец 1</div>
<div class="quiz-option" data-index="2">В первую свободную ячейку: числа задают отступы, а не координаты</div>
<div class="quiz-option" data-index="3">В ячейку (1, 1), потому что нумерация начинается с единицы</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 33. Чем padding отличается от margin в JavaFX?</h4>

<div class="quiz-option" data-index="0">padding задаётся в пикселях, а margin — в процентах от размера окна</div>
<div class="quiz-option" data-index="1">padding — внутренний отступ панели от её краёв до потомков, а margin — внешний отступ конкретного потомка, задаваемый статическим методом панели</div>
<div class="quiz-option" data-index="2">padding применяется к элементам управления, а margin — только к панелям компоновки</div>
<div class="quiz-option" data-index="3">Это синонимы: setPadding() и setMargin() делают одно и то же</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 34. Как заставить поле ввода забирать всё свободное место в <code>HBox</code>, оставив кнопке её собственный размер?</h4>

<div class="quiz-option" data-index="0">Вызвать field.setPrefWidth(Double.MAX_VALUE) — других способов нет</div>
<div class="quiz-option" data-index="1">Вызвать hbox.setAlignment(Pos.CENTER)</div>
<div class="quiz-option" data-index="2">Вызвать <code>HBox.setHgrow(field, Priority.ALWAYS)</code></div>
<div class="quiz-option" data-index="3">Вызвать hbox.setSpacing(0) и field.setPrefColumnCount(100)</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 35. Что верно про компонент <code>Label</code>?</h4>

<div class="quiz-option" data-index="0">Не принимает ввод и по умолчанию не получает фокус, зато умеет показывать картинку (graphic) и переносить текст по словам (wrapText)</div>
<div class="quiz-option" data-index="1">Это упрощённый TextField с запретом редактирования</div>
<div class="quiz-option" data-index="2">Может содержать только строку: картинку приходится добавлять отдельным узлом</div>
<div class="quiz-option" data-index="3">Не поддерживает CSS, потому что рисуется средствами AWT</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 36. Когда сработает обработчик из строки <code>field.setOnAction(e -&gt; System.out.println(field.getText()));</code> для <code>TextField</code>?</h4>

<div class="quiz-option" data-index="0">При каждом нажатии любой клавиши в поле</div>
<div class="quiz-option" data-index="1">Один раз при создании поля</div>
<div class="quiz-option" data-index="2">Никогда: у TextField нет свойства onAction</div>
<div class="quiz-option" data-index="3">Когда пользователь нажмёт Enter в этом поле</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 37. Что вернёт метод <code>getText()</code> у <code>PasswordField</code>?</h4>

<div class="quiz-option" data-index="0">Строку из точек, которую видит пользователь</div>
<div class="quiz-option" data-index="1">Настоящий введённый текст — скрыты только символы на экране</div>
<div class="quiz-option" data-index="2">null: пароль доступен лишь через отдельный метод getPassword()</div>
<div class="quiz-option" data-index="3">Хеш введённого пароля</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 38. Чем <code>setDefaultButton(true)</code> отличается от <code>setCancelButton(true)</code>?</h4>

<div class="quiz-option" data-index="0">Первая кнопка становится единственной активной, вторая — отключённой</div>
<div class="quiz-option" data-index="1">Первая срабатывает по Escape, а вторая по Enter</div>
<div class="quiz-option" data-index="2">Первая закрывает окно с сохранением, вторая — без сохранения</div>
<div class="quiz-option" data-index="3">Первая срабатывает по Enter в любом месте окна, вторая — по Escape</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 39. Откуда столбец <code>TableColumn</code> берёт значение для ячейки?</h4>

<div class="quiz-option" data-index="0">Из метода toString() объекта строки</div>
<div class="quiz-option" data-index="1">Из порядка полей класса модели: первый столбец — первое поле</div>
<div class="quiz-option" data-index="2">Из <code>cellValueFactory</code>: либо PropertyValueFactory по имени свойства, либо лямбда, возвращающая свойство объекта</div>
<div class="quiz-option" data-index="3">Из cellFactory, который задаёт и значение, и его формат</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 40. Почему в новом коде вместо <code>PropertyValueFactory</code> предпочитают лямбду?</h4>

<div class="quiz-option" data-index="0">PropertyValueFactory не умеет работать с числовыми столбцами</div>
<div class="quiz-option" data-index="1">PropertyValueFactory ищет метод через рефлексию, поэтому опечатка в имени свойства не вызовет ошибку компиляции: столбец просто останется пустым</div>
<div class="quiz-option" data-index="2">PropertyValueFactory объявлен устаревшим и удалён в JavaFX 21</div>
<div class="quiz-option" data-index="3">Лямбда не требует, чтобы модель хранила данные в свойствах JavaFX</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 5: События и привязка данных (Вопросы 41–48) ===== -->

<div class="quiz-question" data-correct="0">
<h4>Вопрос 41. Что представляет собой обработчик события в JavaFX?</h4>

<div class="quiz-option" data-index="0">Реализацию функционального интерфейса <code>EventHandler</code> с единственным методом handle(), которую обычно пишут лямбдой</div>
<div class="quiz-option" data-index="1">Наследника класса Event с переопределённым методом run()</div>
<div class="quiz-option" data-index="2">Метод, помеченный аннотацией @EventListener</div>
<div class="quiz-option" data-index="3">Отдельный поток, который слушает очередь событий окна</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 42. Кнопка лежит в <code>VBox</code>. На VBox добавлен фильтр (addEventFilter), на кнопке задан setOnAction, на VBox — ещё и addEventHandler. В каком порядке они сработают при нажатии?</h4>

<div class="quiz-option" data-index="0">Обработчик кнопки, фильтр VBox, обработчик VBox</div>
<div class="quiz-option" data-index="1">Фильтр VBox, обработчик VBox, обработчик кнопки</div>
<div class="quiz-option" data-index="2">Фильтр VBox, обработчик кнопки, обработчик VBox</div>
<div class="quiz-option" data-index="3">Все три сработают одновременно, порядок не определён</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 43. Что произойдёт, если вызвать <code>event.consume()</code> в фильтре, установленном на контейнере?</h4>

<div class="quiz-option" data-index="0">Действие, уже выполненное обработчиком, будет отменено</div>
<div class="quiz-option" data-index="1">Событие немедленно перейдёт в фазу всплытия</div>
<div class="quiz-option" data-index="2">Событие будет скопировано в очередь окна для повторной обработки</div>
<div class="quiz-option" data-index="3">Распространение события остановится: целевой узел его вообще не получит</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 44. Чем <code>setOnAction</code> отличается от <code>addEventHandler</code>?</h4>

<div class="quiz-option" data-index="0">setOnAction у узла один и новый вызов затирает предыдущий, а addEventHandler можно вызывать сколько угодно раз — выполнятся все обработчики</div>
<div class="quiz-option" data-index="1">setOnAction работает в фазе захвата, а addEventHandler — в фазе всплытия</div>
<div class="quiz-option" data-index="2">setOnAction доступен только у Button, а addEventHandler — у любого узла</div>
<div class="quiz-option" data-index="3">setOnAction принимает лямбду, а addEventHandler — только анонимный класс</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 45. Чем свойство (Property) отличается от обычного поля класса?</h4>

<div class="quiz-option" data-index="0">Свойство занимает меньше памяти за счёт упаковки значения</div>
<div class="quiz-option" data-index="1">Свойство доступно только для чтения</div>
<div class="quiz-option" data-index="2">Свойство хранит значение в базе данных, а поле — в оперативной памяти</div>
<div class="quiz-option" data-index="3">Свойство хранит значение и умеет сообщать слушателям о каждом его изменении</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 46. Что произойдёт при выполнении кода <code>label.textProperty().bind(field.textProperty()); label.setText("Готово");</code>?</h4>

<div class="quiz-option" data-index="0">Метка покажет «Готово», а привязка автоматически разорвётся</div>
<div class="quiz-option" data-index="1">Метка покажет «Готово», а затем вернётся к тексту поля</div>
<div class="quiz-option" data-index="2">Вызов setText() выбросит RuntimeException: связанное значение изменять нельзя</div>
<div class="quiz-option" data-index="3">Код не скомпилируется</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 47. Когда нужен <code>bindBidirectional()</code>, а не <code>bind()</code>?</h4>

<div class="quiz-option" data-index="0">Когда типы связываемых свойств различаются</div>
<div class="quiz-option" data-index="1">Когда нужно связать больше двух свойств сразу</div>
<div class="quiz-option" data-index="2">Когда приёмник должен остаться доступным для записи, а изменения идти в обе стороны</div>
<div class="quiz-option" data-index="3">Когда источник изменяется из другого потока</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 48. Почему <code>TableView</code> обновляется сама, когда в модель добавили новую запись?</h4>

<div class="quiz-option" data-index="0">Потому что таблица раз в секунду перечитывает источник данных</div>
<div class="quiz-option" data-index="1">Потому что таблица связана с <code>ObservableList</code>, который сообщает подписчикам о добавлении и удалении элементов</div>
<div class="quiz-option" data-index="2">Потому что контроллер обязан вызывать table.refresh() после каждого действия</div>
<div class="quiz-option" data-index="3">Потому что PropertyValueFactory отслеживает изменения через рефлексию</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 6: FXML, контроллеры и Scene Builder (Вопросы 49–55) ===== -->

<div class="quiz-question" data-correct="2">
<h4>Вопрос 49. Как узел из FXML попадает в поле контроллера?</h4>

<div class="quiz-option" data-index="0">По совпадению типа: загрузчик ищет поле подходящего класса</div>
<div class="quiz-option" data-index="1">Через конструктор контроллера, куда FXMLLoader передаёт все созданные узлы</div>
<div class="quiz-option" data-index="2">По имени: <code>fx:id</code> в разметке должен совпадать с именем поля, помеченного <code>@FXML</code></div>
<div class="quiz-option" data-index="3">Через метод getNamespace(), который нужно вызвать вручную</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 50. Где в FXML-файле указывается класс-контроллер?</h4>

<div class="quiz-option" data-index="0">Атрибутом <code>fx:controller</code> на корневом элементе, один раз на файл</div>
<div class="quiz-option" data-index="1">Атрибутом fx:id на каждом узле, которому нужен обработчик</div>
<div class="quiz-option" data-index="2">Инструкцией &lt;?import?&gt; в начале файла</div>
<div class="quiz-option" data-index="3">Атрибутом onAction="#Контроллер.метод" у каждой кнопки</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 51. Почему настройку интерфейса пишут в <code>initialize()</code>, а не в конструкторе контроллера?</h4>

<div class="quiz-option" data-index="0">Потому что конструктор выполняется в другом потоке</div>
<div class="quiz-option" data-index="1">Потому что в конструкторе поля <code>@FXML</code> ещё равны null: загрузчик заполняет их позже</div>
<div class="quiz-option" data-index="2">Потому что конструктор вызывается один раз, а initialize() — при каждом показе окна</div>
<div class="quiz-option" data-index="3">Потому что в конструкторе запрещено обращаться к классам модели</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 52. Чем статический вызов <code>FXMLLoader.load(url)</code> хуже создания объекта <code>FXMLLoader</code>?</h4>

<div class="quiz-option" data-index="0">Он не поддерживает вложенные файлы через fx:include</div>
<div class="quiz-option" data-index="1">Он разбирает разметку заметно медленнее</div>
<div class="quiz-option" data-index="2">Он не вызывает метод initialize() у контроллера</div>
<div class="quiz-option" data-index="3">Он возвращает только корневой узел, и получить контроллер у него нельзя</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 53. <code>FXMLLoader</code> падает с сообщением «Location is required». В чём причина?</h4>

<div class="quiz-option" data-index="0">getResource() вернул null: файл лежит не в resources, перепутан путь или проект не пересобран</div>
<div class="quiz-option" data-index="1">В FXML не указан атрибут fx:controller</div>
<div class="quiz-option" data-index="2">В классе-контроллере нет метода initialize()</div>
<div class="quiz-option" data-index="3">В pom.xml не подключён модуль javafx-controls</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 54. Что делает Scene Builder?</h4>

<div class="quiz-option" data-index="0">Генерирует Java-код построения интерфейса по нарисованному окну</div>
<div class="quiz-option" data-index="1">Визуально редактирует FXML-файлы: вы рисуете мышью, он сохраняет разметку, и наоборот</div>
<div class="quiz-option" data-index="2">Компилирует и запускает JavaFX-приложение вместо среды разработки</div>
<div class="quiz-option" data-index="3">Преобразует готовые формы Swing в разметку JavaFX</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 55. В какой вкладке Inspector в Scene Builder задают <code>fx:id</code> узла и имя метода-обработчика?</h4>

<div class="quiz-option" data-index="0">Properties</div>
<div class="quiz-option" data-index="1">Layout</div>
<div class="quiz-option" data-index="2">Library</div>
<div class="quiz-option" data-index="3">Code</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 7: CSS и шаблон MVC (Вопросы 56–60) ===== -->

<div class="quiz-question" data-correct="3">
<h4>Вопрос 56. Почему все свойства в JavaFX CSS начинаются с префикса <code>-fx-</code>?</h4>

<div class="quiz-option" data-index="0">Чтобы браузер мог отличить их от стандартных при экспорте интерфейса в HTML</div>
<div class="quiz-option" data-index="1">Этого требует стандарт W3C для любых нестандартных свойств</div>
<div class="quiz-option" data-index="2">Так помечаются только те свойства, которые поддерживает тема Modena</div>
<div class="quiz-option" data-index="3">Чтобы не путать их со свойствами W3C: набор свойств и их поведение в JavaFX свои</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 57. Какого свойства в JavaFX CSS нет вовсе?</h4>

<div class="quiz-option" data-index="0">margin — внешний отступ задаёт панель компоновки, например VBox.setMargin()</div>
<div class="quiz-option" data-index="1">-fx-padding</div>
<div class="quiz-option" data-index="2">-fx-opacity</div>
<div class="quiz-option" data-index="3">-fx-background-color</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 58. Как правильно подключить таблицу стилей ко всей сцене?</h4>

<div class="quiz-option" data-index="0">scene.getStylesheets().add(getClass().getResource("styles.css"))</div>
<div class="quiz-option" data-index="1">scene.setStyle("styles.css")</div>
<div class="quiz-option" data-index="2">scene.setStylesheet(new File("styles.css"))</div>
<div class="quiz-option" data-index="3">scene.getStylesheets().add(getClass().getResource("styles.css").toExternalForm())</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 59. Как распределяются роли шаблона MVC в JavaFX-приложении?</h4>

<div class="quiz-option" data-index="0">Model — FXML-разметка, View — контроллер, Controller — сервис</div>
<div class="quiz-option" data-index="1">Model — данные и бизнес-логика, View — FXML и CSS, Controller — класс с полями @FXML и обработчиками</div>
<div class="quiz-option" data-index="2">Model — база данных, View — Scene Builder, Controller — класс Application</div>
<div class="quiz-option" data-index="3">Model — класс Stage, View — класс Scene, Controller — граф сцены</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 60. Какое правило MVC нарушено, если в классе модели <code>Student</code> появился <code>import javafx.scene.control.Label</code>?</h4>

<div class="quiz-option" data-index="0">Модель не должна знать об интерфейсе; при этом импорт javafx.beans.property в ней вполне допустим</div>
<div class="quiz-option" data-index="1">Модель не должна импортировать никакие классы JavaFX, включая свойства</div>
<div class="quiz-option" data-index="2">Никакое: модель обязана уметь отображать себя на экране</div>
<div class="quiz-option" data-index="3">Нарушено правило «одно окно — один контроллер»</div>
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
    'Вопрос 1': 'AWT не рисовал элементы сам, а просил ОС создать настоящий системный элемент. Из-за этого в библиотеке остались только те компоненты, которые есть на всех платформах сразу.',
    'Вопрос 2': 'JavaFX взял у Swing легковесные компоненты и добавил то, что к тому времени стало нормой в вебе: отдельный файл разметки, каскадные стили, реактивные привязки и графический конвейер Prism.',
    'Вопрос 3': 'С JDK 11 (2018) JavaFX вынесен из JDK, поэтому на чистом JDK 21 строка import javafx.application.Application не скомпилируется, пока библиотека не подключена как зависимость.',
    'Вопрос 4': 'JavaFX вынесен из JDK в самостоятельный проект OpenJFX. Gluon — это компания, которая развивает Scene Builder, а не саму платформу.',
    'Вопрос 5': 'За готовые элементы управления отвечает javafx-controls, и он сам подтягивает javafx-graphics и javafx-base как транзитивные зависимости.',
    'Вопрос 6': 'javafx-controls транзитивно приносит graphics и base, а javafx-fxml добавляет загрузчик разметки. Этих двух зависимостей хватает для подавляющего большинства задач.',
    'Вопрос 7': 'Нативные части у JavaFX есть, но POM зависимости сам выбирает сборку под текущую ОС. Поэтому один и тот же pom.xml без правок работает и на Windows, и на Linux.',
    'Вопрос 8': 'Плагин сам вычисляет module-path и подключает нужные модули. Вручную то же самое делается ключами --module-path и --add-modules.',
    'Вопрос 9': 'Эту проверку выполняет сам класс Application при старте, если JavaFX попал в classpath, а не в module-path. Класс-обёртка Application не наследует, поэтому проверка не срабатывает.',
    'Вопрос 10': 'Prism — это графический конвейер платформы. Glass отвечает за окна, мышь и клавиатуру, Quantum связывает граф сцены с отрисовкой, WebKit — движок компонента WebView.',
    'Вопрос 11': 'start(Stage) — единственный абстрактный метод класса Application, поэтому реализовать его обязан каждый наследник.',
    'Вопрос 12': 'launch() запускает среду выполнения, создаёт экземпляр приложения и вызывает init(), затем платформа создаёт primary Stage и передаёт его в start(); stop() выполняется при завершении.',
    'Вопрос 13': 'init() отрабатывает до появления окна, start() строит и показывает интерфейс, а закрытие последнего окна завершает среду выполнения с вызовом stop().',
    'Вопрос 14': 'init() вызывается из потока JavaFX-Launcher ещё до создания окна. Именно поэтому в нём нельзя трогать графические объекты.',
    'Вопрос 15': 'Граф сцены живёт в JavaFX Application Thread, а init() работает в другом потоке и раньше создания primary Stage: зал ещё физически не готов принимать гостей.',
    'Вопрос 16': 'Platform.exit() завершает среду выполнения корректно и даёт stop() сохранить настройки, а System.exit(0) обрывает JVM сразу, и всё несохранённое теряется.',
    'Вопрос 17': 'Граф сцены не синхронизирован и принадлежит только JavaFX Application Thread, поэтому платформа отвергает такое изменение исключением. Обновление нужно завернуть в Platform.runLater().',
    'Вопрос 18': 'Объект вашего класса создаёте не вы, а launch() — через рефлексию. Для этого нужен доступный конструктор без параметров.',
    'Вопрос 19': 'Stage — рама, Scene — то, что в эту раму вставлено. Первый (primary) Stage платформа создаёт сама и передаёт в start().',
    'Вопрос 20': 'showAndWait() останавливает код на строке вызова, пока окно не закроют. Поэтому им пользуются для диалогов, от которых нужен ответ пользователя.',
    'Вопрос 21': 'WINDOW_MODAL блокирует только окно-владельца, заданное через initOwner(), а APPLICATION_MODAL — все окна приложения. StageStyle отвечает не за модальность, а за оформление рамы.',
    'Вопрос 22': 'consume() останавливает дальнейшее распространение события, поэтому команда на закрытие до окна не доходит. setImplicitExit влияет лишь на завершение среды выполнения, а stop() возвращает void.',
    'Вопрос 23': 'Сцена хранит дерево, а ветвиться умеет только Parent: именно у него есть список getChildren(). Обычный Node потомков не имеет и корнем быть не может.',
    'Вопрос 24': 'Сцена привязана к одному окну. Зато сцену внутри окна можно менять сколько угодно — вызов stage.setScene(other) и есть самый простой переход между экранами.',
    'Вопрос 25': 'Text наследует Shape и нужен при рисовании, а Label наследует Control и умеет wrapText, graphic и labelFor. Для подписи в интерфейсе берут именно Label.',
    'Вопрос 26': 'У узла может быть только один родитель, поэтому добавление в новую панель молча удаляет узел из старой. Нужны две одинаковые кнопки — создайте два объекта.',
    'Вопрос 27': 'Свойства z-index в JavaFX нет: порядок наложения задаёт список потомков, как стопка прозрачных плёнок. Изменить его на лету помогают toFront() и toBack().',
    'Вопрос 28': 'setVisible(false) только прячет узел, а панель компоновки продолжает резервировать под него место. Убирает узел из раскладки setManaged(false), поэтому оба свойства часто связывают привязкой.',
    'Вопрос 29': 'HBox выстраивает потомков в строку, VBox — в столбик. Расстояние между ними задаётся первым аргументом конструктора или методом setSpacing().',
    'Вопрос 30': 'Зоны top, bottom, left и right получают ровно столько места, сколько нужно их содержимому, а всё остальное отдаётся центру. Поэтому BorderPane и берут каркасом главного окна: таблица в центре растягивается, шапка и строка состояния сохраняют высоту, а незанятые зоны не занимают места вовсе.',
    'Вопрос 31': 'StackPane накладывает потомков слоями в порядке добавления, поэтому индикатор, добавленный последним, оказывается сверху.',
    'Вопрос 32': 'Сигнатура метода — add(узел, номерСтолбца, номерСтроки), нумерация идёт с нуля. Порядок этих двух аргументов путают чаще всего.',
    'Вопрос 33': 'pane.setPadding(new Insets(16)) отодвигает от краёв сразу всё содержимое, а VBox.setMargin(child, new Insets(10)) добавляет свободное место вокруг одного потомка.',
    'Вопрос 34': 'Приоритет роста задаётся статическим методом панели: Priority.ALWAYS означает, что именно этот потомок получает всё свободное место при изменении размера окна.',
    'Вопрос 35': 'Label наследует Labeled и, кроме текста, умеет graphic, wrapText, alignment и labelFor. Редактирование в нём не предусмотрено вовсе — это чистый вывод.',
    'Вопрос 36': 'setOnAction у TextField срабатывает по Enter. Чтобы реагировать на каждое изменение текста, слушателя вешают на textProperty().',
    'Вопрос 37': 'PasswordField наследует TextField и лишь маскирует символы при отрисовке. Значение остаётся обычной строкой, доступной через getText().',
    'Вопрос 38': 'Это два «горячих» назначения: кнопка по умолчанию отвечает на Enter, кнопка отмены — на Escape. В остальном обе остаются обычными кнопками с обработчиком onAction.',
    'Вопрос 39': 'cellValueFactory отвечает за то, ЧТО показать, а cellFactory — за то, КАК это отформатировать. Эти две фабрики регулярно путают.',
    'Вопрос 40': 'Лямбда data -> data.getValue().authorProperty() проверяется компилятором, а строка «author» — нет. Вдобавок в модульном проекте для рефлексии придётся открывать пакет модели через opens.',
    'Вопрос 41': 'EventHandler — функциональный интерфейс, поэтому обработчик записывают лямбдой или ссылкой на метод. Аннотация @EventListener относится к Spring, а не к JavaFX.',
    'Вопрос 42': 'Событие сначала идёт сверху вниз по дереву — это фаза захвата, в которой работают фильтры. Дойдя до цели, оно поднимается обратно, и на обратном пути срабатывают обработчики.',
    'Вопрос 43': 'consume() означает «событие обработано, дальше не передавать». На фильтре это позволяет централизованно блокировать ввод, например на время загрузки данных.',
    'Вопрос 44': 'setOnAction — удобная обёртка над одним свойством onAction, и значение там всегда одно. addEventHandler добавляет обработчик в список, ничего не затирая.',
    'Вопрос 45': 'Обычное поле — листок с записанным курсом валюты, свойство — табло в обменнике: поменялось значение, и все, кто на него смотрит, узнали об этом сами. На этом построены привязки.',
    'Вопрос 46': 'bind() создаёт одностороннюю связь и делает приёмник доступным только для чтения. Чтобы снова управлять текстом вручную, связь разрывают вызовом unbind().',
    'Вопрос 47': 'Двусторонняя привязка работает как сообщающиеся сосуды и оставляет оба свойства доступными для записи, но требует совпадения типов. Односторонняя связь типы допускает разные — через выражения.',
    'Вопрос 48': 'Вызов setItems(ObservableList) подписывает таблицу на изменения списка: добавили элемент — строка появилась на экране, и перерисовывать ничего вручную не нужно.',
    'Вопрос 49': 'Связывает узел и поле именно совпадение fx:id с именем поля, а аннотация @FXML разрешает загрузчику записать значение даже в приватное поле.',
    'Вопрос 50': 'Атрибут fx:controller допустим только на корневом элементе. По нему FXMLLoader создаёт экземпляр контроллера и заполняет его поля.',
    'Вопрос 51': 'FXMLLoader сначала создаёт контроллер, затем записывает узлы в поля @FXML и только потом вызывает initialize(). До этого момента поля пусты.',
    'Вопрос 52': 'Метод getController() есть только у объекта FXMLLoader, а контроллер нужен почти всегда, как только между окнами начинают передавать данные.',
    'Вопрос 53': 'Загрузчику передали null вместо адреса разметки. Поэтому результат getResource() полезно оборачивать в Objects.requireNonNull с внятным сообщением об ошибке.',
    'Вопрос 54': 'Scene Builder работает ровно с одним типом файлов — FXML. Java-кода он не создаёт и средой разработки не является: любой корректный FXML открывается в нём как готовое окно.',
    'Вопрос 55': 'Вкладка Code содержит поля fx:id и On Action; Properties отвечает за тексты и внешний вид, Layout — за размеры и отступы. Заготовку контроллера даёт команда View → Show Sample Controller Skeleton.',
    'Вопрос 56': 'Синтаксис почти совпадает с веб-CSS, а свойства другие, поэтому префикс сделан намеренно: -fx-text-fill вместо color, -fx-background-radius вместо border-radius.',
    'Вопрос 57': 'Раскладка в JavaFX — задача панелей компоновки, поэтому display, float, flex и margin из веб-CSS отсутствуют. Внутренний отступ -fx-padding при этом работает как обычно.',
    'Вопрос 58': 'getStylesheets() хранит строки-адреса, а getResource() возвращает объект URL, поэтому вызов toExternalForm() обязателен. Метод setStyle() задаёт инлайн-стиль одного узла, а не файл.',
    'Вопрос 59': 'Кухня (модель) готовит, зал (представление) показывает, официант (контроллер) ходит между ними. Поменяли интерьер зала — кухню переделывать не нужно.',
    'Вопрос 60': 'Model отвечает за данные и бизнес-логику и ничего не знает про Button и TextField. Свойства из javafx.beans.property относятся к модулю javafx.base и с интерфейсом не связаны, поэтому их использовать можно.'
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
