# Практическое занятие 9: Реализация графических интерфейсов: JavaFX

Сегодня вы соберёте настольное приложение с нуля: от пустого окна до менеджера студентов с таблицей, формой, FXML-разметкой и собственной таблицей стилей. Все задания выполняются **в одном Maven-проекте и строго по порядку**: каждое следующее опирается на файлы, созданные в предыдущем.

Понадобятся JDK 21 (или новее), Maven 3.8+ и любая IDE. Проверьте окружение до начала работы:

```bash
java -version
mvn -v
```

Обе команды должны напечатать версии, а не «команда не найдена». Если Maven не установлен, скачайте его с [maven.apache.org](https://maven.apache.org/download.cgi) и добавьте каталог `bin` в переменную `PATH`.

---

## Часть 1: Проект и первое окно

Настройка проекта — это как разложить инструменты перед сменой: пока ящик не собран, к работе не приступишь. Раньше отвёртки лежали в общем ящике (JavaFX внутри JDK), теперь их заказывают отдельной коробкой и указывают, где она лежит.

### Задание 1.1: Maven-проект с подключённым JavaFX

Задание обязательное. Без правильно настроенного проекта не заработает ни одно из остальных: начиная с JDK 11 JavaFX не входит в состав JDK и подключается вручную.

**Шаг 1.** Создайте каталог `student-manager` и внутри него структуру пакетов.

```bash
# Linux / macOS
mkdir student-manager
cd student-manager
mkdir -p src/main/java/com/example/studentmanager/{demo,model,service,controller}
mkdir -p src/main/resources/com/example/studentmanager
```

```powershell
# Windows (PowerShell)
mkdir student-manager
cd student-manager
mkdir src\main\java\com\example\studentmanager\demo
mkdir src\main\java\com\example\studentmanager\model
mkdir src\main\java\com\example\studentmanager\service
mkdir src\main\java\com\example\studentmanager\controller
mkdir src\main\resources\com\example\studentmanager
```

**Шаг 2.** В корне проекта создайте `pom.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
         http://maven.apache.org/xsd/maven-4.0.0.xsd">

    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>student-manager</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.release>21</maven.compiler.release>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <javafx.version>21.0.2</javafx.version>
        <!-- Класс, который запускает javafx:run. Значение можно
             перекрыть из командной строки: -Djavafx.mainClass=... -->
        <javafx.mainClass>com.example.studentmanager.demo.HelloApp</javafx.mainClass>
    </properties>

    <dependencies>
        <!-- Элементы управления; тянет за собой javafx-graphics и javafx-base -->
        <dependency>
            <groupId>org.openjfx</groupId>
            <artifactId>javafx-controls</artifactId>
            <version>${javafx.version}</version>
        </dependency>
        <!-- Загрузка интерфейса из FXML (понадобится в Части 5) -->
        <dependency>
            <groupId>org.openjfx</groupId>
            <artifactId>javafx-fxml</artifactId>
            <version>${javafx.version}</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <!-- Версию компилятора фиксируем явно: у старых версий плагина
                 нет параметра release, и сборка на JDK 21 упала бы -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.13.0</version>
            </plugin>

            <!-- Плагин запускает приложение с правильным module-path -->
            <plugin>
                <groupId>org.openjfx</groupId>
                <artifactId>javafx-maven-plugin</artifactId>
                <version>0.0.8</version>
                <configuration>
                    <!-- Ссылка на свойство, а не литерал: иначе значение
                         из pom.xml всегда перекрывало бы ключ -D -->
                    <mainClass>${javafx.mainClass}</mainClass>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

**Шаг 3.** Создайте `src/main/java/com/example/studentmanager/demo/HelloApp.java`:

```java
package com.example.studentmanager.demo;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class HelloApp extends Application {

    @Override
    public void start(Stage stage) {
        Label label = new Label("JavaFX подключён и работает");

        VBox root = new VBox(12, label);          // корневой узел графа сцены
        root.setAlignment(Pos.CENTER);
        root.setPadding(new Insets(20));

        Scene scene = new Scene(root, 420, 200);  // сцена 420 на 200 пикселей

        stage.setTitle("Проверка окружения");
        stage.setScene(scene);
        stage.show();                            // без этой строки окна не будет
    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

**Шаг 4.** Соберите и запустите:

```bash
mvn clean compile javafx:run
```

Команда одинакова для Windows, Linux и macOS. Должно появиться окно с надписью по центру.

Полезно знать, что цель `javafx:run` сама форкает сборку до фазы `process-classes`: классы компилируются, а ресурсы (FXML, CSS) копируются в `target/classes` автоматически. Явный `compile` в команде безвреден, но не обязателен; `clean` добавляют, когда нужна пересборка с нуля.

Дальше в каждом задании запускается свой класс, и чтобы не править `pom.xml` каждый раз, имя передаётся свойством — тем самым `javafx.mainClass`, на которое ссылается конфигурация плагина:

```bash
mvn compile javafx:run -Djavafx.mainClass=com.example.studentmanager.demo.HelloApp
```

Ключ `-D` перекрывает значение из `<properties>`, поэтому менять `pom.xml` ради запуска другого класса не нужно.

**Ответьте письменно:** (1) Что произойдёт, если удалить обе зависимости `org.openjfx` и выполнить `mvn compile`? Приведите текст ошибки. (2) Почему у зависимостей JavaFX не указан classifier (`win`, `mac`, `linux`) — как Maven понимает, какую сборку скачать? (3) Загляните в `~/.m2/repository/org/openjfx` (Windows: `%USERPROFILE%\.m2\repository\org\openjfx`). Каких модулей там больше двух и откуда они взялись?

---

### Задание 1.2: Жизненный цикл и класс Launcher

**Шаг 1.** Доработайте `HelloApp`. Добавьте импорты `javafx.application.Platform` и `javafx.scene.control.Button`, а к классу — два метода жизненного цикла:

```java
    @Override
    public void init() {
        // Выполняется ДО создания окна. Stage и Scene здесь создавать нельзя
        System.out.println("init()  — поток: " + Thread.currentThread().getName());
    }

    @Override
    public void stop() {
        System.out.println("stop()  — приложение завершается");
    }
```

В начало метода `start()` добавьте такую же печать, а перед `stage.show()` — кнопку выхода:

```java
        // самая первая строка start()
        System.out.println("start() — поток: " + Thread.currentThread().getName());

        // ...перед stage.show()
        Button exitButton = new Button("Выйти");
        exitButton.setOnAction(event -> Platform.exit());  // завершение с вызовом stop()
        root.getChildren().add(exitButton);
```

Запустите (`mvn compile javafx:run`), закройте окно двумя способами — кнопкой и системным крестиком — и сравните вывод консоли.

**Шаг 2.** Теперь запустите `HelloApp` **прямо из IDE** кнопкой Run. С большой вероятностью вы получите:

```
Error: JavaFX runtime components are missing, and are required to run this application
```

Так происходит, когда класс-наследник `Application` стартует с JavaFX в classpath, а не в module-path. Обходится это классом-обёрткой. Создайте `src/main/java/com/example/studentmanager/Launcher.java`:

```java
package com.example.studentmanager;

import com.example.studentmanager.demo.HelloApp;

/**
 * Точка входа-обёртка. Не наследует Application, поэтому проверка
 * JavaFX не срабатывает и приложение стартует даже из IDE.
 */
public class Launcher {

    public static void main(String[] args) {
        HelloApp.main(args);
    }
}
```

Запустите из IDE класс `Launcher` — окно откроется. В Части 7 вы поменяете в нём одну строку.

**Ответьте письменно:** (1) В каких потоках выполнились `init()` и `start()`? Приведите имена потоков из консоли. (2) Вызывается ли `stop()` при закрытии крестиком? А при `Platform.exit()`? Замените `Platform.exit()` на `System.exit(0)`, проверьте и объясните разницу. (3) Почему `Launcher` решает проблему, хотя запускает ровно тот же класс?

---

## Часть 2: Элементы управления и обработка событий

Хороший пульт от телевизора устроен так, что нужную кнопку находят не глядя: громкость — качелька, каналы — цифры, красная кнопка выключает. Плохой — это россыпь одинаковых квадратиков с мелкими подписями. Набор элементов у обоих пультов один и тот же; разница в том, что делает каждый и как он подписан. Дальше вы соберёте свой «пульт» из `Label`, `TextField` и `Button` — и увидите, что половину кнопок можно вообще не программировать, если связать свойства напрямую.

### Задание 2.1: Label, TextField и Button

Соберите окно с подписью, полем ввода и кнопкой; нажатие кнопки выводит приветствие в метку. Создайте `demo/GreetingApp.java`:

```java
package com.example.studentmanager.demo;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.stage.Stage;

public class GreetingApp extends Application {

    @Override
    public void start(Stage stage) {
        Label prompt = new Label("Введите фамилию студента:");

        TextField nameField = new TextField();
        nameField.setPromptText("Иванов");     // серая подсказка в пустом поле
        nameField.setPrefColumnCount(18);

        Button greetButton = new Button("Поздороваться");
        greetButton.setDefaultButton(true);    // срабатывает по Enter
        greetButton.setTooltip(new Tooltip("Выведет приветствие"));

        Label resultLabel = new Label();

        // Обработчик нажатия
        greetButton.setOnAction(event -> {
            String name = nameField.getText().trim();
            if (name.isEmpty()) {
                resultLabel.setText("Поле пустое — вводить нечего");
            } else {
                resultLabel.setText("Здравствуйте, " + name + "!");
            }
        });
        nameField.setOnAction(greetButton.getOnAction());   // то же по Enter в поле

        Button clearButton = new Button("Очистить");
        clearButton.setCancelButton(true);     // срабатывает по Escape
        clearButton.setOnAction(event -> {
            nameField.clear();
            resultLabel.setText("");
        });

        HBox inputRow = new HBox(10, nameField, greetButton, clearButton);
        inputRow.setAlignment(Pos.CENTER_LEFT);

        VBox root = new VBox(12, prompt, inputRow, resultLabel);
        root.setPadding(new Insets(20));

        stage.setTitle("Задание 2.1 — Label, TextField, Button");
        stage.setScene(new Scene(root, 560, 200));
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

```bash
mvn compile javafx:run -Djavafx.mainClass=com.example.studentmanager.demo.GreetingApp
```

Проверьте все три способа запустить действие: щелчок мышью, Enter в поле, Enter в любом месте окна. И Escape для очистки.

**Ответьте письменно:** (1) Чем `setDefaultButton(true)` отличается от `setOnAction`? (2) Перепишите обработчик кнопки «Очистить» анонимным классом `EventHandler<ActionEvent>`. Сколько строк добавилось и почему в реальном коде пишут лямбдой? (3) Что вернёт `getText()` у `PasswordField` — настоящий текст или строку из точек?

---

### Задание 2.2: Привязки вместо обработчиков

Половину обработчиков можно не писать вовсе — достаточно связать свойства. Добавьте в `GreetingApp` импорт `javafx.beans.binding.Bindings` и перед созданием `HBox` вставьте:

```java
        // 1. Метка повторяет содержимое поля. Обработчиков нет вообще
        Label mirror = new Label();
        mirror.textProperty().bind(nameField.textProperty());

        // 2. Привязка к вычисляемому выражению
        Label counter = new Label();
        counter.textProperty().bind(
                Bindings.concat("Введено символов: ", nameField.textProperty().length()));

        // 3. Аналог тернарного оператора в мире привязок
        Label status = new Label();
        status.textProperty().bind(
                Bindings.when(nameField.textProperty().isEmpty())
                        .then("Заполните поле")
                        .otherwise("Можно здороваться"));

        // 4. Кнопка сама выключается, пока поле пустое
        greetButton.disableProperty().bind(nameField.textProperty().isEmpty());
```

Добавьте новые метки в корневой контейнер:

```java
        VBox root = new VBox(12, prompt, inputRow, resultLabel, mirror, counter, status);
```

Запустите и понаблюдайте: три метки и кнопка меняются сами, пока вы печатаете. Затем добавьте в самый конец метода `start` строку `mirror.setText("вручную");` и запустите снова. Строку `mirror.setText("вручную");` после проверки удалите — иначе приложение не будет запускаться.

**Ответьте письменно:** (1) Какое исключение и с каким текстом вы получили на последнем шаге и почему? (2) Какая ветка обработчика перестала выполняться при щелчке по кнопке и почему? Проверьте, останется ли она достижимой, если нажать Enter в пустом поле и если ввести один пробел. Объясните оба случая. (3) Чем `bind()` отличается от `bindBidirectional()`? Можно ли связать двусторонне `Label` и `TextField` — проверьте и объясните результат.

---

## Часть 3: Панели компоновки

Зайдите в любой магазин: товар не расставлен по линейке от стены, он разложен по правилам. Витрина у кассы — узкая полоса, куда кладут мелочь в один ряд (`HBox`). Стеллаж — полки одна под другой (`VBox`). Аптечная выкладка — строгая сетка ячеек (`GridPane`). А планировка зала — крупные отделы по периметру и главный проход посередине (`BorderPane`). Продавец не меряет каждый пакет: он выбирает подходящее место. Ваша задача в этой части — научиться выбирать так же.

### Задание 3.1: Форма на GridPane внутри VBox и BorderPane

Реальное окно почти никогда не строится одной панелью: сетка для формы, столбец для блоков, строка для кнопок, каркас для всего окна. Создайте `demo/FormApp.java`:

```java
package com.example.studentmanager.demo;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.stage.Stage;

public class FormApp extends Application {

    @Override
    public void start(Stage stage) {
        // 1. Сетка «подпись — поле»
        GridPane grid = new GridPane();
        grid.setHgap(10);   // расстояние между столбцами
        grid.setVgap(10);   // расстояние между строками

        TextField loginField = new TextField();
        loginField.setPromptText("ivanov");
        PasswordField passwordField = new PasswordField();
        passwordField.setPromptText("Пароль");

        ComboBox<String> groupBox = new ComboBox<>();
        groupBox.getItems().addAll("ПИ24-1", "ПИ24-2", "ТРПО24-1");
        groupBox.setValue("ПИ24-1");
        groupBox.setMaxWidth(Double.MAX_VALUE);

        // add(узел, номерСтолбца, номерСтроки) — нумерация с нуля
        grid.add(new Label("Логин:"), 0, 0);
        grid.add(loginField, 1, 0);
        grid.add(new Label("Пароль:"), 0, 1);
        grid.add(passwordField, 1, 1);
        grid.add(new Label("Группа:"), 0, 2);
        grid.add(groupBox, 1, 2);

        // Первый столбец фиксирован, второй забирает всё свободное место
        ColumnConstraints labelColumn = new ColumnConstraints(90);
        ColumnConstraints fieldColumn = new ColumnConstraints();
        fieldColumn.setHgrow(Priority.ALWAYS);
        grid.getColumnConstraints().addAll(labelColumn, fieldColumn);

        // 2. Строка кнопок
        Label status = new Label("Заполните форму");

        Button submit = new Button("Зарегистрировать");
        submit.setDefaultButton(true);
        submit.setOnAction(event -> status.setText(
                "Логин: " + loginField.getText() + ", группа: " + groupBox.getValue()));

        Button reset = new Button("Сбросить");
        reset.setOnAction(event -> {
            loginField.clear();
            passwordField.clear();
            status.setText("Заполните форму");
        });

        HBox buttons = new HBox(10, submit, reset);
        buttons.setAlignment(Pos.CENTER_RIGHT);

        // 3. Столбец: сетка, кнопки, строка состояния
        VBox form = new VBox(14, grid, buttons, status);
        form.setPadding(new Insets(20));   // внутренний отступ панели

        // 4. Каркас окна
        Label header = new Label("Регистрация студента");
        BorderPane root = new BorderPane();
        root.setTop(header);
        root.setCenter(form);
        BorderPane.setMargin(header, new Insets(16, 20, 0, 20));   // отступ узла

        stage.setTitle("Задание 3.1 — GridPane, VBox, HBox, BorderPane");
        stage.setScene(new Scene(root, 560, 320));
        stage.setMinWidth(420);
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

```bash
mvn compile javafx:run -Djavafx.mainClass=com.example.studentmanager.demo.FormApp
```

Растяните окно мышью: поля должны растягиваться, подписи — оставаться на месте.

**Проведите три эксперимента и запишите результат:**

1. Добавьте `grid.setGridLinesVisible(true)` и посмотрите на сетку. Уберите перед сдачей.
2. Удалите обе строки с `ColumnConstraints` и снова растяните окно. Что изменилось?
3. Замените `buttons.setAlignment(Pos.CENTER_RIGHT)` на `Pos.CENTER_LEFT`, затем на `Pos.CENTER`.

**Ответьте письменно:** (1) В чём разница между `form.setPadding(...)` и `BorderPane.setMargin(header, ...)`? Какой отступ чей? (2) Зачем нужен `setHgrow(Priority.ALWAYS)` и что происходит без него? (3) Что случится, если добавить `loginField` ещё и в `buttons`? Проверьте и объясните.

---

## Часть 4: TableView и ObservableList

Связка `ObservableList` и `TableView` работает как табло вылетов в аэропорту: диспетчер меняет расписание в одном месте, и все экраны обновляются сами. Никто не бегает по залу с тряпкой и маркером — и вам не придётся вручную перерисовывать таблицу.

### Задание 4.1: Модель Student и сервис StudentService

Чтобы таблица сама реагировала на изменения, поля модели должны быть **свойствами JavaFX**. Создайте `src/main/java/com/example/studentmanager/model/Student.java`:

```java
package com.example.studentmanager.model;

import javafx.beans.property.*;

/**
 * Модель студента. Все поля — свойства JavaFX,
 * поэтому TableView автоматически отслеживает их изменения.
 */
public class Student {

    private final StringProperty fullName = new SimpleStringProperty(this, "fullName", "");
    private final StringProperty group = new SimpleStringProperty(this, "group", "");
    private final DoubleProperty averageGrade =
            new SimpleDoubleProperty(this, "averageGrade", 0.0);

    public Student(String fullName, String group, double averageGrade) {
        this.fullName.set(fullName);
        this.group.set(group);
        this.averageGrade.set(averageGrade);
    }

    public String getFullName() { return fullName.get(); }
    public void setFullName(String value) { fullName.set(value); }
    public StringProperty fullNameProperty() { return fullName; }

    public String getGroup() { return group.get(); }
    public void setGroup(String value) { group.set(value); }
    public StringProperty groupProperty() { return group; }

    public double getAverageGrade() { return averageGrade.get(); }
    public void setAverageGrade(double value) { averageGrade.set(value); }
    public DoubleProperty averageGradeProperty() { return averageGrade; }

    @Override
    public String toString() {
        return fullName.get() + " (" + group.get() + ")";
    }
}
```

На каждое поле — ровно три метода: `getXxx()`, `setXxx()` и `xxxProperty()`. `PropertyValueFactory` сначала ищет `xxxProperty()` и только при его отсутствии берёт `getXxx()`; `setXxx()` нужен для редактирования записи, а `xxxProperty()` — ещё и для привязок.

Создайте `src/main/java/com/example/studentmanager/service/StudentService.java`:

```java
package com.example.studentmanager.service;

import com.example.studentmanager.model.Student;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;

/**
 * Хранилище студентов и бизнес-логика.
 * Об интерфейсе не знает ничего: здесь нет ни одного импорта javafx.scene.
 */
public class StudentService {

    private final ObservableList<Student> students = FXCollections.observableArrayList();

    public StudentService() {
        // Демонстрационные данные
        students.addAll(
                new Student("Петров Иван Сергеевич", "ПИ24-1", 4.6),
                new Student("Смирнова Анна Игоревна", "ПИ24-1", 4.9),
                new Student("Кузнецов Дмитрий Олегович", "ТРПО24-1", 3.8));
    }

    /** Список для привязки к таблице. */
    public ObservableList<Student> getStudents() {
        return students;
    }

    public void add(Student student) {
        students.add(student);
    }

    public void remove(Student student) {
        students.remove(student);
    }

    /** Проверка корректности оценки. */
    public static boolean isValidGrade(double grade) {
        return grade >= 2.0 && grade <= 5.0;
    }
}
```

**Ответьте письменно:** (1) Почему поля-свойства объявлены как `final`, хотя значения меняются? (2) Класс `Student` импортирует `javafx.beans.property`, но не `javafx.scene`. Почему первое в модели допустимо, а второе — нарушение архитектуры? (3) Чем `averageGrade.get()` отличается от `averageGrade.getValue()`?

---

### Задание 4.2: Таблица со списком объектов

Создайте `demo/TableApp.java`:

```java
package com.example.studentmanager.demo;

import com.example.studentmanager.model.Student;
import com.example.studentmanager.service.StudentService;
import javafx.application.Application;
import javafx.beans.binding.Bindings;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.layout.*;
import javafx.stage.Stage;

public class TableApp extends Application {

    private final StudentService service = new StudentService();

    @Override
    public void start(Stage stage) {
        TableView<Student> table = new TableView<>();

        // Способ 1: PropertyValueFactory — по имени свойства, через рефлексию
        TableColumn<Student, String> nameColumn = new TableColumn<>("ФИО");
        nameColumn.setCellValueFactory(new PropertyValueFactory<>("fullName"));
        nameColumn.setPrefWidth(300);

        // Способ 2: лямбда — типобезопасно, ошибку поймает компилятор
        TableColumn<Student, String> groupColumn = new TableColumn<>("Группа");
        groupColumn.setCellValueFactory(data -> data.getValue().groupProperty());
        groupColumn.setPrefWidth(140);

        TableColumn<Student, Double> gradeColumn = new TableColumn<>("Средний балл");
        gradeColumn.setCellValueFactory(
                data -> data.getValue().averageGradeProperty().asObject());
        gradeColumn.setPrefWidth(140);

        table.getColumns().addAll(nameColumn, groupColumn, gradeColumn);
        table.setItems(service.getStudents());   // связь со списком модели
        table.setPlaceholder(new Label("Список пуст"));
        VBox.setVgrow(table, Priority.ALWAYS);   // таблица занимает всю высоту

        // Кнопки меняют только список модели и таблицу не трогают вообще
        Button addButton = new Button("Добавить студента");
        addButton.setOnAction(event -> service.add(
                new Student("Новиков Пётр Андреевич", "ПИ24-2", 4.2)));

        Button deleteButton = new Button("Удалить выбранного");
        deleteButton.setOnAction(event ->
                service.remove(table.getSelectionModel().getSelectedItem()));
        // Кнопка сама выключается, пока строка не выбрана
        deleteButton.disableProperty().bind(
                table.getSelectionModel().selectedItemProperty().isNull());

        // Строка состояния сама показывает количество записей
        Label countLabel = new Label();
        countLabel.textProperty().bind(Bindings.concat(
                "Студентов в списке: ", Bindings.size(service.getStudents())));

        VBox root = new VBox(12, table, new HBox(10, addButton, deleteButton), countLabel);
        root.setPadding(new Insets(18));

        stage.setTitle("Задание 4.2 — TableView и ObservableList");
        stage.setScene(new Scene(root, 820, 500));
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

```bash
mvn compile javafx:run -Djavafx.mainClass=com.example.studentmanager.demo.TableApp
```

Нажмите «Добавить студента» несколько раз, удалите одного, щёлкните по заголовку столбца «Средний балл» — таблица отсортируется. Затем замените в первом столбце `new PropertyValueFactory<>("fullName")` на `new PropertyValueFactory<>("fullNam")` (с опечаткой), пересоберите и запустите. Верните правильное имя свойства `"fullName"` и пересоберите проект.

**Ответьте письменно:** (1) Скомпилировался ли проект с опечаткой? Что показал первый столбец и почему компилятор промолчал? (2) Зачем в третьем столбце вызов `asObject()` — что будет без него? (3) Кто перерисовал таблицу после `service.add(...)` — вы или платформа? Какой механизм за это отвечает?

---

## Часть 5: Перенос интерфейса в FXML

Оркестр не разучивает симфонию со слуха: композитор один раз записывает партитуру, и дальше ноты живут отдельно от музыкантов. Поменялся состав — играют по тем же нотам; поправили партию — переписали строчку, а не переучили весь оркестр. FXML — это партитура вашего окна, контроллер — оркестр, который по ней играет.

### Задание 5.1: Разметка students-view.fxml

Метод `start()` из предыдущего задания разросся до полусотни строк, а окно там простое. Вынесем разметку в отдельный файл. Создайте `src/main/resources/com/example/studentmanager/students-view.fxml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>

<?import javafx.geometry.Insets?>
<?import javafx.scene.control.Button?>
<?import javafx.scene.control.Label?>
<?import javafx.scene.control.TableColumn?>
<?import javafx.scene.control.TableView?>
<?import javafx.scene.control.TextField?>
<?import javafx.scene.layout.BorderPane?>
<?import javafx.scene.layout.GridPane?>
<?import javafx.scene.layout.HBox?>
<?import javafx.scene.layout.VBox?>

<BorderPane xmlns="http://javafx.com/javafx/21"
            xmlns:fx="http://javafx.com/fxml/1"
            fx:controller="com.example.studentmanager.controller.StudentController"
            prefWidth="780" prefHeight="540">

    <top>
        <Label text="Менеджер студентов" styleClass="title-label">
            <BorderPane.margin><Insets top="18" right="18" bottom="10" left="18"/></BorderPane.margin>
        </Label>
    </top>

    <center>
        <TableView fx:id="studentTable">
            <columns>
                <TableColumn fx:id="fullNameColumn" text="ФИО" prefWidth="330"/>
                <TableColumn fx:id="groupColumn" text="Группа" prefWidth="150"/>
                <TableColumn fx:id="gradeColumn" text="Средний балл" prefWidth="150"/>
            </columns>
            <BorderPane.margin><Insets left="18" right="18"/></BorderPane.margin>
        </TableView>
    </center>

    <bottom>
        <VBox spacing="12">
            <padding><Insets top="14" right="18" bottom="18" left="18"/></padding>

            <GridPane hgap="10" vgap="10">
                <!-- Статические свойства панели пишутся как GridPane.rowIndex -->
                <Label text="ФИО:" styleClass="field-label" GridPane.columnIndex="0" GridPane.rowIndex="0"/>
                <TextField fx:id="fullNameField" promptText="Иванов Иван Иванович" prefColumnCount="24"
                           GridPane.columnIndex="1" GridPane.rowIndex="0"/>
                <Label text="Группа:" styleClass="field-label" GridPane.columnIndex="0" GridPane.rowIndex="1"/>
                <TextField fx:id="groupField" promptText="ПИ24-1"
                           GridPane.columnIndex="1" GridPane.rowIndex="1"/>
                <Label text="Средний балл:" styleClass="field-label" GridPane.columnIndex="0" GridPane.rowIndex="2"/>
                <TextField fx:id="gradeField" promptText="4.5"
                           GridPane.columnIndex="1" GridPane.rowIndex="2"/>
            </GridPane>

            <HBox spacing="10">
                <!-- onAction ссылается на метод контроллера; знак # обязателен -->
                <Button fx:id="addButton" text="Добавить"
                        onAction="#handleAdd" styleClass="primary-button"/>
                <Button fx:id="deleteButton" text="Удалить выбранного"
                        onAction="#handleDelete" styleClass="danger-button"/>
                <Button text="Очистить форму" onAction="#handleClear"/>
            </HBox>

            <Label fx:id="statusLabel" styleClass="status-label"/>
        </VBox>
    </bottom>
</BorderPane>
```

Атрибуты `styleClass` пока ни на что не влияют — таблица стилей появится в Части 6.

---

### Задание 5.2: Контроллер и точка входа

Создайте `src/main/java/com/example/studentmanager/controller/StudentController.java`:

```java
package com.example.studentmanager.controller;

import com.example.studentmanager.model.Student;
import com.example.studentmanager.service.StudentService;
import javafx.beans.binding.Bindings;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;

public class StudentController {

    // Имена полей должны СОВПАДАТЬ с fx:id в разметке
    @FXML private TableView<Student> studentTable;
    @FXML private TableColumn<Student, String> fullNameColumn;
    @FXML private TableColumn<Student, String> groupColumn;
    @FXML private TableColumn<Student, Double> gradeColumn;

    @FXML private TextField fullNameField;
    @FXML private TextField groupField;
    @FXML private TextField gradeField;

    @FXML private Button addButton;
    @FXML private Button deleteButton;
    @FXML private Label statusLabel;

    private final StudentService service = new StudentService();

    /** Вызывается после того, как все поля @FXML заполнены. */
    @FXML
    private void initialize() {
        fullNameColumn.setCellValueFactory(new PropertyValueFactory<>("fullName"));
        groupColumn.setCellValueFactory(new PropertyValueFactory<>("group"));
        gradeColumn.setCellValueFactory(
                data -> data.getValue().averageGradeProperty().asObject());

        gradeColumn.setCellFactory(column -> new TableCell<Student, Double>() {
            @Override
            protected void updateItem(Double value, boolean empty) {
                super.updateItem(value, empty);
                setText(empty || value == null ? null : String.format("%.2f", value));
            }
        });

        studentTable.setItems(service.getStudents());
        studentTable.setPlaceholder(new Label("Список пуст — добавьте студента"));

        deleteButton.disableProperty().bind(
                studentTable.getSelectionModel().selectedItemProperty().isNull());

        addButton.disableProperty().bind(fullNameField.textProperty().isEmpty()
                .or(groupField.textProperty().isEmpty())
                .or(gradeField.textProperty().isEmpty()));

        statusLabel.textProperty().bind(Bindings.concat(
                "Студентов в списке: ", Bindings.size(service.getStudents())));
    }

    @FXML
    private void handleAdd() {
        double grade;
        try {
            grade = Double.parseDouble(gradeField.getText().trim().replace(',', '.'));
        } catch (NumberFormatException e) {
            System.out.println("Некорректный средний балл");
            return;
        }
        service.add(new Student(fullNameField.getText().trim(),
                groupField.getText().trim(), grade));
        handleClear();
    }

    @FXML
    private void handleDelete() {
        Student selected = studentTable.getSelectionModel().getSelectedItem();
        if (selected != null) {
            service.remove(selected);
        }
    }

    @FXML
    private void handleClear() {
        studentTable.getSelectionModel().clearSelection();
        fullNameField.clear();
        groupField.clear();
        gradeField.clear();
        fullNameField.requestFocus();
    }
}
```

Создайте `src/main/java/com/example/studentmanager/MainApp.java`:

```java
package com.example.studentmanager;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.Objects;

public class MainApp extends Application {

    @Override
    public void start(Stage stage) throws IOException {
        // Путь без слеша — файл ищется рядом с этим классом,
        // то есть в src/main/resources/com/example/studentmanager/
        FXMLLoader loader = new FXMLLoader(
                Objects.requireNonNull(MainApp.class.getResource("students-view.fxml"),
                        "Не найден файл students-view.fxml"));

        Parent root = loader.load();
        Scene scene = new Scene(root, 780, 540);

        stage.setTitle("Менеджер студентов");
        stage.setScene(scene);
        stage.setMinWidth(700);
        stage.setMinHeight(470);
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

```bash
mvn compile javafx:run -Djavafx.mainClass=com.example.studentmanager.MainApp
```

FXML попадает в classpath не сам по себе: его копирует в `target/classes` фаза `process-resources`. Отдельно её вызывать не нужно — `javafx:run` форкает сборку до `process-classes` и делает это за вас. А вот если запускать приложение в обход Maven, по старому содержимому `target/classes`, вы получите `Location is required`.

**Эксперимент.** Переименуйте в FXML `fx:id="groupField"` в `fx:id="groupFld"`, оставив поле контроллера прежним, и запустите.

**Ответьте письменно:** (1) Какое исключение возникло и что именно `FXMLLoader` не смог сделать? (2) Верните имя обратно и перенесите настройку столбцов из `initialize()` в конструктор контроллера. Что произойдёт и почему? (3) В каком порядке `FXMLLoader` создаёт узлы, заполняет поля `@FXML` и вызывает `initialize()`?

---

### Задание 5.3: Scene Builder

Установите **JavaFX Scene Builder** от Gluon: [gluonhq.com/products/scene-builder](https://gluonhq.com/products/scene-builder/) — установщики есть для Windows, macOS и Linux.

1. Откройте `students-view.fxml` в Scene Builder (в IntelliJ IDEA: правый щелчок по файлу → **Open in SceneBuilder**; путь к программе задаётся в **Settings → Languages & Frameworks → JavaFX**).
2. Найдите в дереве **Document → Hierarchy** кнопку «Добавить» и откройте её вкладку **Inspector → Code**: там видны поля **fx:id** и **On Action**.
3. Перетащите из **Library** новый `Label` в нижний `VBox`, задайте текст «Учебная версия», сохраните файл и запустите приложение — метка появится без единой строки Java-кода.
4. Выполните **View → Show Sample Controller Skeleton** и сравните заготовку со своим `StudentController`.

Если установить Scene Builder не удалось, выполните пункт 3 вручную — добавьте `<Label text="Учебная версия"/>` в конец `VBox` — и опишите, чем ручная правка отличается от визуальной.

**Ответьте письменно:** (1) Генерирует ли Scene Builder Java-код? Какой единственный тип файлов он редактирует? (2) Почему добавление метки не потребовало правки контроллера? (3) Назовите один случай, когда Scene Builder мешает, а не помогает.

---

## Часть 6: Оформление через CSS

В сети магазинов не объясняют каждому новому продавцу отдельно, какого цвета рубашка и где бейдж: один раз утверждают стандарт формы, и вся сеть выглядит одинаково. Решили сменить цвет к юбилею — правят стандарт, а не гардероб каждого сотрудника. Таблица стилей — тот же стандарт формы: одна строка в `styles.css` перекрашивает все кнопки приложения сразу.

### Задание 6.1: Подключение таблицы стилей

Создайте `src/main/resources/com/example/studentmanager/styles.css`:

```css
/* styles.css — оформление менеджера студентов */

.root {
    -fx-font-family: "Segoe UI", "Arial", sans-serif;
    -fx-font-size: 13px;
    -fx-background-color: #f4f6f8;
}

.title-label  { -fx-font-size: 22px; -fx-font-weight: bold; -fx-text-fill: #1f2d3d; }
.field-label  { -fx-text-fill: #55606d; }
.status-label { -fx-text-fill: #6b7684; -fx-font-size: 12px; }

.text-field {
    -fx-background-radius: 5; -fx-border-radius: 5;
    -fx-border-color: #d3dae3; -fx-padding: 6 10 6 10;
}
.text-field:focused { -fx-border-color: #2d7ff9; -fx-border-width: 1.5; }

.button { -fx-background-radius: 5; -fx-padding: 7 16 7 16; -fx-cursor: hand; }

.primary-button { -fx-background-color: #2d7ff9; -fx-text-fill: white; -fx-font-weight: bold; }
.primary-button:hover    { -fx-background-color: derive(#2d7ff9, -12%); }
.primary-button:disabled { -fx-opacity: 0.45; }

.danger-button { -fx-background-color: #e5484d; -fx-text-fill: white; }
.danger-button:hover    { -fx-background-color: derive(#e5484d, -12%); }
.danger-button:disabled { -fx-opacity: 0.45; }

.table-view { -fx-background-radius: 6; -fx-border-radius: 6; -fx-border-color: #d3dae3; }
.table-view .column-header { -fx-background-color: #eaeef3; }
.table-view .table-row-cell:selected { -fx-background-color: #cfe1ff; -fx-text-fill: #1f2d3d; }
```

Подключите её в `MainApp` — добавьте после создания сцены:

```java
        scene.getStylesheets().add(
                Objects.requireNonNull(MainApp.class.getResource("styles.css"),
                        "Не найден файл styles.css").toExternalForm());
```

```bash
mvn compile javafx:run -Djavafx.mainClass=com.example.studentmanager.MainApp
```

Окно должно стать светло-серым, заголовок — крупным, кнопка «Добавить» — синей, «Удалить выбранного» — красной.

**Ответьте письменно:** (1) Зачем нужен вызов `toExternalForm()` и что произойдёт без него? (2) Откуда взялся селектор `.root`, если такого класса стилей вы нигде не задавали? (3) Уберите на время подключение стилей: какая тема осталась и как она называется?

---

### Задание 6.2: Состояния, приоритет и подключение из FXML

**Шаг 1.** Проверьте псевдоклассы: наведите курсор на синюю кнопку (`:hover`), щёлкните по полю ввода (`:focused`), очистите форму — кнопка «Добавить» станет полупрозрачной (`:disabled`), выделите строку таблицы (`:selected`).

**Шаг 2.** Проверьте приоритет. Добавьте в конец `initialize()` строку и запустите:

```java
        addButton.setStyle("-fx-background-color: #16a34a;");
```

Посмотрите, какой цвет победил — зелёный из кода или синий из `styles.css`. Затем уберите строку.

**Шаг 3.** Подключите таблицу стилей не из Java, а прямо из разметки. Уберите `scene.getStylesheets().add(...)` из `MainApp` и добавьте в корневой элемент FXML атрибут `stylesheets="@styles.css"`:

```xml
<BorderPane xmlns="http://javafx.com/javafx/21"
            xmlns:fx="http://javafx.com/fxml/1"
            fx:controller="com.example.studentmanager.controller.StudentController"
            stylesheets="@styles.css"
            prefWidth="780" prefHeight="540">
```

Символ `@` означает «путь относительно этого FXML-файла». Запустите и убедитесь, что оформление сохранилось.

**Шаг 4.** Добавьте в `styles.css` собственное правило — чередующуюся заливку строк:

```css
.table-view .table-row-cell:odd { -fx-background-color: #fbfcfd; }
```

**Ответьте письменно:** (1) Какой цвет оказался у кнопки на шаге 2 и почему? Расставьте по приоритету: инлайн-стиль, ваша таблица стилей, тема Modena. (2) Назовите три отличия JavaFX CSS от веб-CSS (свойства, отступы, раскладка). (3) Какой способ подключения стилей удобнее в проекте с несколькими окнами и почему?

---

## Часть 7: Итоговое мини-приложение — CRUD-менеджер

Создание и чтение записей у вас уже есть. Осталось добавить изменение, заменить «молчаливое» удаление подтверждением и научить таблицу искать. Все детали разложены на столе — дальше сборка по инструкции, как у шкафа из магазина.

### Задание 7.1: Изменение выбранной записи

**Шаг 1.** В FXML, в блоке `<HBox spacing="10">`, вставьте между кнопками «Добавить» и «Удалить выбранного»:

```xml
                <Button fx:id="updateButton" text="Сохранить изменения"
                        onAction="#handleUpdate"/>
```

**Шаг 2.** В `StudentController` добавьте поле:

```java
    @FXML private Button updateButton;
```

**Шаг 3.** В конец `initialize()` добавьте заполнение формы по выбранной строке и привязку кнопки:

```java
        // Выбор строки заполняет форму
        studentTable.getSelectionModel().selectedItemProperty()
                .addListener((observable, oldStudent, newStudent) -> {
                    if (newStudent != null) {
                        fullNameField.setText(newStudent.getFullName());
                        groupField.setText(newStudent.getGroup());
                        gradeField.setText(String.valueOf(newStudent.getAverageGrade()));
                    }
                });

        updateButton.disableProperty().bind(
                studentTable.getSelectionModel().selectedItemProperty().isNull());
```

**Шаг 4.** Замените `handleAdd` и добавьте три метода. Разбор оценки и показ ошибок вынесены отдельно, чтобы не дублировать код:

```java
    @FXML
    private void handleAdd() {
        Double grade = parseGrade();
        if (grade == null) {
            return;
        }
        service.add(new Student(fullNameField.getText().trim(),
                groupField.getText().trim(), grade));
        handleClear();
    }

    @FXML
    private void handleUpdate() {
        Student selected = studentTable.getSelectionModel().getSelectedItem();
        if (selected == null) {
            return;
        }
        Double grade = parseGrade();
        if (grade == null) {
            return;
        }
        // Меняем свойства модели — таблица перерисуется сама
        selected.setFullName(fullNameField.getText().trim());
        selected.setGroup(groupField.getText().trim());
        selected.setAverageGrade(grade);
        handleClear();
    }

    /** Разбор поля «Средний балл». Возвращает null, если значение некорректно. */
    private Double parseGrade() {
        double grade;
        try {
            grade = Double.parseDouble(gradeField.getText().trim().replace(',', '.'));
        } catch (NumberFormatException e) {
            showError("Средний балл должен быть числом, например 4.5");
            return null;
        }
        if (!StudentService.isValidGrade(grade)) {
            showError("Средний балл должен быть в диапазоне от 2.0 до 5.0");
            return null;
        }
        return grade;
    }

    private void showError(String message) {
        Alert alert = new Alert(Alert.AlertType.ERROR);
        alert.setTitle("Ошибка ввода");
        alert.setHeaderText(null);
        alert.setContentText(message);
        alert.showAndWait();
    }
```

Класс `Alert` уже доступен: контроллер импортирует `javafx.scene.control.*`.

Проверьте: выберите строку, поменяйте группу в поле, нажмите «Сохранить изменения» — значение в таблице обновится немедленно.

**Ответьте письменно:** (1) Почему таблица обновилась, хотя вы не вызывали ни `refresh()`, ни `setItems()`? (2) Что произойдёт, если выбрать строку (форма заполнится) и нажать «Добавить»? Ошибка ли это и как бы вы её исправили? (3) Введите в поле оценки «отлично» и нажмите «Сохранить изменения». Чем такое поведение лучше, чем `System.out.println` в первой версии `handleAdd` из задания 5.2?

---

### Задание 7.2: Поиск через FilteredList

**Шаг 1.** Замените в FXML весь блок `<top>` на строку поиска с заголовком:

```xml
    <top>
        <VBox spacing="10">
            <padding>
                <Insets top="18" right="18" bottom="10" left="18"/>
            </padding>
            <Label text="Менеджер студентов" styleClass="title-label"/>
            <HBox spacing="10">
                <Label text="Поиск:" styleClass="field-label"/>
                <TextField fx:id="searchField" promptText="фамилия или группа"
                           prefColumnCount="24"/>
            </HBox>
        </VBox>
    </top>
```

**Шаг 2.** В контроллер добавьте поле и импорты:

```java
    @FXML private TextField searchField;
```

```java
import javafx.collections.transformation.FilteredList;
import javafx.collections.transformation.SortedList;
```

**Шаг 3.** Замените строку `studentTable.setItems(service.getStudents());` на блок:

```java
        // FilteredList — «окно» в исходный список, данные не копируются
        FilteredList<Student> filteredStudents =
                new FilteredList<>(service.getStudents(), student -> true);

        searchField.textProperty().addListener((observable, oldValue, newValue) -> {
            String query = newValue == null ? "" : newValue.trim().toLowerCase();
            filteredStudents.setPredicate(student -> query.isEmpty()
                    || student.getFullName().toLowerCase().contains(query)
                    || student.getGroup().toLowerCase().contains(query));
        });

        // SortedList сохраняет сортировку по щелчку на заголовке столбца
        SortedList<Student> sortedStudents = new SortedList<>(filteredStudents);
        sortedStudents.comparatorProperty().bind(studentTable.comparatorProperty());
        studentTable.setItems(sortedStudents);
```

**Шаг 4.** В уже существующей строке `setPlaceholder` замените текст на «Ничего не найдено». А привязку `statusLabel` в конце `initialize()` замените целиком — пусть строка состояния показывает оба числа:

```java
        statusLabel.textProperty().bind(Bindings.concat(
                "Всего студентов: ", Bindings.size(service.getStudents()),
                "    показано: ", Bindings.size(sortedStudents)));
```

Проверьте: наберите в поиске «ПИ24» — останутся студенты только этих групп; добавьте студента другой группы — счётчик «всего» вырастет, а «показано» нет.

**Ответьте письменно:** (1) Почему при удалении отфильтрованной строки удаляется правильный студент, хотя таблица показывает `SortedList`, а не исходный список? (2) Что произойдёт, если убрать `sortedStudents.comparatorProperty().bind(...)` и щёлкнуть по заголовку столбца? (3) Чем `FilteredList` лучше, чем «собрать новый список через `stream().filter()` и вызвать `setItems`»?

---

### Задание 7.3: Подтверждения и финальная сборка

**Шаг 1.** Замените `handleDelete` на версию с подтверждением:

```java
    @FXML
    private void handleDelete() {
        Student selected = studentTable.getSelectionModel().getSelectedItem();
        if (selected == null) {
            return;   // кнопка и так отключена, но защита не помешает
        }

        Alert confirm = new Alert(Alert.AlertType.CONFIRMATION);
        confirm.setTitle("Удаление");
        confirm.setHeaderText(null);
        confirm.setContentText("Удалить запись: " + selected + "?");

        confirm.showAndWait()
                .filter(button -> button == ButtonType.OK)
                .ifPresent(button -> {
                    service.remove(selected);
                    handleClear();
                });
    }
```

**Шаг 2.** В `MainApp` добавьте импорты `javafx.scene.control.Alert` и `javafx.scene.control.ButtonType`, а перед `stage.show()` — подтверждение закрытия окна:

```java
        stage.setOnCloseRequest(event -> {
            Alert confirm = new Alert(Alert.AlertType.CONFIRMATION);
            confirm.setTitle("Выход");
            confirm.setHeaderText(null);
            confirm.setContentText("Закрыть приложение?");

            boolean agreed = confirm.showAndWait()
                    .filter(button -> button == ButtonType.OK)
                    .isPresent();

            if (!agreed) {
                event.consume();   // отменяем закрытие окна
            }
        });
```

Добавьте туда же метод, чтобы увидеть завершение жизненного цикла:

```java
    @Override
    public void stop() {
        System.out.println("Приложение завершено корректно");
    }
```

**Шаг 3.** Переключите `Launcher` на итоговое приложение (импорт `HelloApp` удалите):

```java
package com.example.studentmanager;

public class Launcher {

    public static void main(String[] args) {
        MainApp.main(args);
    }
}
```

**Шаг 4.** Пропишите итоговый класс в `pom.xml`, чтобы приложение запускалось одной командой. Меняется не конфигурация плагина (там стоит ссылка `${javafx.mainClass}`), а само свойство в блоке `<properties>`:

```xml
        <javafx.mainClass>com.example.studentmanager.MainApp</javafx.mainClass>
```

Финальный прогон:

```bash
mvn clean compile javafx:run
```

Из IDE запускайте класс `Launcher`.

**Проверьте по списку:**

1. Окно открывается со списком из трёх студентов и оформлением из `styles.css`.
2. «Добавить» неактивна, пока не заполнены все три поля; «Сохранить изменения» и «Удалить выбранного» — пока не выбрана строка.
3. Ввод «отлично» в поле оценки даёт диалог с ошибкой, а не падение приложения; оценка 7.5 отвергается проверкой `isValidGrade`.
4. Поиск фильтрует таблицу по мере набора текста.
5. Удаление и закрытие окна спрашивают подтверждение; «Отмена» оставляет всё как было.
6. При выходе в консоль печатается сообщение из `stop()`.

**Ответьте письменно:** (1) Что делает `event.consume()` в обработчике `setOnCloseRequest` и что будет, если его убрать? (2) Найдите в итоговом проекте по одному классу (или файлу) на каждую роль MVC и объясните, почему отнесли его именно туда. (3) Проверьте `Student` и `StudentService`: есть ли в них хоть один импорт `javafx.scene`? Почему его отсутствие — хороший признак?

---

### Задание 7.4: Гистограмма распределения оценок

Модель и сервис для этого не нужно писать заново — `Student` и `StudentService` уже готовы (Часть 4). Постройте отдельным окном гистограмму, показывающую, сколько студентов попадает в каждый диапазон среднего балла.

**Шаг 1.** Создайте `demo/ChartApp.java`:

```java
package com.example.studentmanager.demo;

import com.example.studentmanager.model.Student;
import com.example.studentmanager.service.StudentService;
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.chart.BarChart;
import javafx.scene.chart.CategoryAxis;
import javafx.scene.chart.NumberAxis;
import javafx.scene.chart.XYChart;
import javafx.stage.Stage;

import java.util.Map;
import java.util.TreeMap;
import java.util.stream.Collectors;

public class ChartApp extends Application {

    private final StudentService service = new StudentService();

    @Override
    public void start(Stage stage) {
        CategoryAxis xAxis = new CategoryAxis();
        xAxis.setLabel("Диапазон среднего балла");

        NumberAxis yAxis = new NumberAxis();
        yAxis.setLabel("Количество студентов");
        yAxis.setTickUnit(1);

        BarChart<String, Number> chart = new BarChart<>(xAxis, yAxis);
        chart.setTitle("Распределение оценок");
        chart.setLegendVisible(false);

        // TreeMap сортирует диапазоны по алфавиту — заодно и по возрастанию
        Map<String, Long> byRange = new TreeMap<>(service.getStudents().stream()
                .collect(Collectors.groupingBy(this::rangeOf, Collectors.counting())));

        XYChart.Series<String, Number> series = new XYChart.Series<>();
        byRange.forEach((range, count) -> series.getData().add(new XYChart.Data<>(range, count)));
        chart.getData().add(series);

        stage.setTitle("Задание 7.4 — распределение оценок");
        stage.setScene(new Scene(chart, 640, 420));
        stage.show();
    }

    /** Диапазон, в который попадает средний балл студента. */
    private String rangeOf(Student student) {
        double grade = student.getAverageGrade();
        if (grade < 3.0) return "2.0-2.9";
        if (grade < 4.0) return "3.0-3.9";
        if (grade < 4.5) return "4.0-4.4";
        return "4.5-5.0";
    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

**Шаг 2.** Запустите:

```bash
mvn compile javafx:run -Djavafx.mainClass=com.example.studentmanager.demo.ChartApp
```

Проверьте: в окне ровно один столбец на каждый диапазон, встречающийся среди трёх демонстрационных студентов из `StudentService`; сумма высот столбцов равна количеству студентов.

**Ответьте письменно:** (1) Если добавить в `StudentService` четвёртого студента и перезапустить `ChartApp`, столбец обновится — а если бы `service.add(...)` вызывался уже после `stage.show()`, появился бы новый столбец сам? Почему? (2) Что изменится на диаграмме, если заменить `new TreeMap<>(...)` на обычный `HashMap`, без TreeMap? (3) Метод `rangeOf` — это часть модели (`Student`/`StudentService`) или часть интерфейса? Почему он оказался именно в `ChartApp`, а не в `Student`?

---

## Часть 8: Контрольные вопросы

Ответьте письменно:

1. Почему начиная с JDK 11 JavaFX не входит в состав JDK и что из этого следует для нового проекта?
2. Какие два артефакта `org.openjfx` достаточно объявить для большинства приложений и что даёт каждый из них?
3. Зачем нужен `javafx-maven-plugin`? Что он подставляет при запуске такого, чего не делает обычный `java -cp`?
4. Что означает ошибка «JavaFX runtime components are missing» и почему её обходит класс `Launcher`?
5. Опишите жизненный цикл приложения: `launch()` → `init()` → `start()` → `stop()`. В каких потоках выполняются `init()` и `start()`?
6. Чем `Platform.exit()` отличается от `System.exit(0)`?
7. Что такое JavaFX Application Thread и почему нельзя менять интерфейс из другого потока? Как вернуть в интерфейс результат фоновой работы?
8. Чем `Stage` отличается от `Scene`? Может ли одна и та же сцена стоять в двух окнах?
9. Чем `show()` отличается от `showAndWait()` и где второй метод необходим?
10. Что такое граф сцены? Чем различаются `Node`, `Parent`, `Region` и `Control`?
11. Что произойдёт, если один и тот же объект узла добавить сначала в одну панель, а затем в другую?
12. Как в JavaFX определяется порядок наложения узлов? Чем `setVisible(false)` отличается от `setManaged(false)`?
13. В чём разница между `padding` и `margin` и как задаётся каждый из них?
14. Какую панель компоновки вы выберете для формы «подпись — поле», какую — для каркаса главного окна, и почему?
15. Из каких трёх частей состоит работающий `TableView`? За что отвечает `cellValueFactory`, а за что `cellFactory`?
16. Сравните `PropertyValueFactory` и лямбду в `setCellValueFactory`. Какую ошибку компилятор не поймает в первом случае и почему?
17. Почему таблица обновляется сама при изменении `ObservableList`? Для чего нужны `FilteredList` и `SortedList`?
18. Чем `bind()` отличается от `bindBidirectional()`? Что произойдёт при вызове `setText()` у метки, чей `textProperty()` привязан?
19. Что делают `fx:controller`, `fx:id` и `onAction="#метод"` в FXML? Как они связаны с полями и методами контроллера?
20. Почему настройку компонентов пишут в `initialize()`, а не в конструкторе контроллера?
21. Назовите три отличия JavaFX CSS от веб-CSS. В каком порядке применяются инлайн-стиль, ваша таблица стилей и тема Modena?
22. Как распределяются обязанности между Model, View и Controller? Какой импорт в классе модели сигнализирует о нарушении архитектуры?

---

## Результаты занятия

К концу занятия вы должны сдать:

1. Maven-проект `student-manager` с зависимостями `javafx-controls` и `javafx-fxml`, плагином `javafx-maven-plugin` и классом `Launcher`.
2. Демонстрационные приложения из Частей 1–4: `HelloApp` (с методами `init()` и `stop()`), `GreetingApp` (с привязками из задания 2.2), `FormApp`, `TableApp`.
3. Модель `Student` со свойствами JavaFX и сервис `StudentService` с `ObservableList`.
4. Разметку `students-view.fxml` и контроллер `StudentController` с полями `@FXML`, методом `initialize()` и обработчиками.
5. Таблицу стилей `styles.css`, подключённую к приложению, с псевдоклассами `:hover`, `:focused`, `:disabled`, `:selected`.
6. Итоговое приложение «Менеджер студентов»: добавление, отображение, изменение выбранной записи, удаление с подтверждением, поиск через `FilteredList`, счётчик записей и подтверждение закрытия окна.
7. Скриншоты итогового окна: обычный вид, вид с активным поиском, вид с диалогом подтверждения удаления.
8. Ответы на письменные вопросы из заданий 1.1–7.3.
9. Ответы на контрольные вопросы (1–22).
