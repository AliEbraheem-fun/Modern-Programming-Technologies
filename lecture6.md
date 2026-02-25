# Лекция 6: Системы сборки, Базы данных и ORM

## Введение

Добро пожаловать на шестую лекцию курса "Современные технологии программирования". До сих пор мы писали код, компилировали его вручную и работали с данными прямо в памяти программы. Но реальные проекты устроены сложнее: в них десятки зависимостей, которые нужно подключать, тесты, которые нужно запускать, и данные, которые нужно надёжно хранить в базе данных. Сегодня мы разберём, как системы сборки (Maven и Gradle) автоматизируют рутину разработки, как Java-приложения взаимодействуют с базами данных через JDBC, что такое паттерн DAO и как ORM-фреймворк Hibernate избавляет нас от ручного написания SQL-запросов.

---

## Часть 1: Системы автоматической сборки

### 1.1 Зачем нужны системы сборки?

Реальный Java-проект содержит:
- Десятки или сотни классов
- Зависимости от сторонних библиотек (библиотека логирования, HTTP-клиент, СУБД-драйвер)
- Тесты
- Ресурсы (конфигурационные файлы, изображения)

Без системы сборки всё это нужно вручную:
- Скачивать JAR-файлы зависимостей
- Прописывать classpath при компиляции
- Вручную запускать тесты
- Упаковывать всё в JAR для деплоя

Представьте, что вы готовите сложное блюдо, и вам приходится каждый раз самому ходить на ферму за яйцами, молоть муку и вручную разводить огонь. Система сборки — это ваша автоматизированная кухня, где все ингредиенты доставляются сами, а духовка включается по расписанию.

**Системы сборки автоматизируют всё это** + управление зависимостями.

### 1.2 Apache Maven

Maven — наиболее распространённая система сборки Java-проектов. Давайте разберём её ключевые концепции.

#### Стандартная структура проекта

```
project/
├── pom.xml                    # Файл конфигурации (Project Object Model)
├── src/
│   ├── main/
│   │   ├── java/              # Исходный код приложения
│   │   └── resources/         # Конфигурационные файлы, свойства
│   └── test/
│       ├── java/              # Тестовый код
│       └── resources/         # Тестовые ресурсы
└── target/                    # Результаты сборки (игнорируется git)
    ├── classes/               # Скомпилированные .class файлы
    └── project-1.0.jar        # Итоговый JAR
```

#### Файл pom.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
         http://maven.apache.org/xsd/maven-4.0.0.xsd">

    <modelVersion>4.0.0</modelVersion>

    <!-- GAV-координаты проекта -->
    <groupId>com.example</groupId>    <!-- Организация/группа -->
    <artifactId>my-app</artifactId>   <!-- Имя артефакта -->
    <version>1.0-SNAPSHOT</version>   <!-- Версия -->
    <packaging>jar</packaging>        <!-- Тип упаковки (jar/war/pom) -->

    <properties>
        <maven.compiler.source>21</maven.compiler.source>
        <maven.compiler.target>21</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <!-- Зависимость от H2 базы данных -->
        <dependency>
            <groupId>com.h2database</groupId>
            <artifactId>h2</artifactId>
            <version>2.2.224</version>
        </dependency>

        <!-- Зависимость от Hibernate -->
        <dependency>
            <groupId>org.hibernate.orm</groupId>
            <artifactId>hibernate-core</artifactId>
            <version>6.4.0.Final</version>
        </dependency>

        <!-- Тестовая зависимость (только для тестов) -->
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>5.10.0</version>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <!-- Плагин для создания исполняемого JAR -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-jar-plugin</artifactId>
                <configuration>
                    <archive>
                        <manifest>
                            <mainClass>com.example.Main</mainClass>
                        </manifest>
                    </archive>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

#### Жизненный цикл Maven

Это важный момент: Maven имеет предопределённые фазы. Каждая фаза включает все предыдущие — то есть, если вы запускаете `test`, Maven автоматически выполнит `validate` и `compile` перед этим:

| Фаза | Действие |
|------|----------|
| `validate` | Проверка корректности проекта |
| `compile` | Компиляция исходного кода |
| `test` | Запуск юнит-тестов |
| `package` | Упаковка в JAR/WAR |
| `verify` | Проверка качества пакета |
| `install` | Установка в локальный репозиторий |
| `deploy` | Публикация в удалённый репозиторий |

```bash
# Запуск команд Maven:
mvn compile          # Скомпилировать
mvn test             # Скомпилировать + запустить тесты
mvn package          # compile + test + создать JAR
mvn clean package    # Очистить target/, затем package
mvn install          # package + установить в ~/.m2/repository
mvn dependency:tree  # Показать дерево зависимостей
```

#### Область видимости зависимостей (scope)

```xml
<dependency>
    <scope>compile</scope>   <!-- По умолчанию — везде -->
    <scope>test</scope>      <!-- Только для тестов -->
    <scope>provided</scope>  <!-- Есть в рантайме (сервер), не включать в JAR -->
    <scope>runtime</scope>   <!-- Только в рантайме, не нужна при компиляции -->
</dependency>
```

#### Репозитории Maven

Maven ищет зависимости в порядке:
1. **Локальный репозиторий** (`~/.m2/repository`) — кэш на компьютере
2. **Центральный репозиторий** (Maven Central, `repo.maven.apache.org`)
3. **Дополнительные репозитории** (корпоративные, Spring repo и т.д.)

```xml
<repositories>
    <repository>
        <id>spring-releases</id>
        <url>https://repo.spring.io/release</url>
    </repository>
</repositories>
```

### 1.3 Gradle

Gradle — более современная система сборки, использующая Groovy или Kotlin DSL вместо XML. Если Maven можно сравнить с подробной инструкцией, где каждый шаг расписан в XML, то Gradle — это лаконичный скрипт, в котором вы описываете только то, что действительно важно.

#### Стандартная структура (аналогична Maven)

```
project/
├── build.gradle (или build.gradle.kts для Kotlin DSL)
├── settings.gradle
├── gradlew / gradlew.bat  (Gradle wrapper)
├── gradle/wrapper/
└── src/...
```

**Gradle Wrapper (`gradlew` / `gradlew.bat`)** — скрипт, который позволяет запускать сборку **без предварительной установки Gradle** на машине. Wrapper автоматически скачивает нужную версию Gradle, указанную в `gradle/wrapper/gradle-wrapper.properties`. Это гарантирует, что все разработчики в команде используют одинаковую версию Gradle.

#### build.gradle (Groovy DSL)

```groovy
plugins {
    id 'java'
    id 'application'
}

group = 'com.example'
version = '1.0-SNAPSHOT'

java {
    sourceCompatibility = JavaVersion.VERSION_21
    targetCompatibility = JavaVersion.VERSION_21
}

repositories {
    mavenCentral()  // Maven Central репозиторий
}

dependencies {
    implementation 'com.h2database:h2:2.2.224'
    implementation 'org.hibernate.orm:hibernate-core:6.4.0.Final'
    testImplementation 'org.junit.jupiter:junit-jupiter:5.10.0'
}

application {
    mainClass = 'com.example.Main'
}

test {
    useJUnitPlatform()
}
```

#### build.gradle.kts (Kotlin DSL — рекомендуется в новых проектах)

```kotlin
plugins {
    java
    application
}

group = "com.example"
version = "1.0-SNAPSHOT"

java {
    sourceCompatibility = JavaVersion.VERSION_21
    targetCompatibility = JavaVersion.VERSION_21
}

repositories {
    mavenCentral()
}

dependencies {
    implementation("com.h2database:h2:2.2.224")
    implementation("org.hibernate.orm:hibernate-core:6.4.0.Final")
    testImplementation("org.junit.jupiter:junit-jupiter:5.10.0")
}

application {
    mainClass = "com.example.Main"
}

tasks.test {
    useJUnitPlatform()
}
```

#### Жизненный цикл Gradle

```bash
./gradlew tasks         # Список всех задач
./gradlew compileJava   # Компиляция
./gradlew test          # Тесты
./gradlew build         # Полная сборка (compile + test + jar)
./gradlew clean build   # Очистка + сборка
./gradlew run           # Запуск приложения (с плагином application)
./gradlew dependencies  # Показать зависимости
```

Обратите внимание, как отличаются Maven и Gradle на практике:

**Maven vs Gradle:**

| | Maven | Gradle |
|---|---|---|
| Конфигурация | XML (verbose) | Groovy/Kotlin DSL (лаконичный) |
| Производительность | Медленнее | Быстрее (инкрементальная сборка) |
| Гибкость | Конвенционный | Очень гибкий |
| Распространённость | Широко используется | Растёт, Android обязателен |

---

Теперь, когда мы умеем собирать проекты, давайте перейдём к тому, без чего не обходится практически ни одно серьёзное приложение — работе с базами данных.

## Часть 2: Базы данных и JDBC

### 2.1 Что такое JDBC?

**JDBC (Java Database Connectivity)** — стандартный Java API для работы с реляционными базами данных. Он определяет интерфейсы, а конкретная реализация (драйвер) предоставляется производителем СУБД.

Представьте, что JDBC — это универсальная розетка. Стандарт один, а вилки (драйверы) у каждого производителя свои. Вашему приложению не нужно знать, как именно устроена конкретная база данных — достаточно «воткнуть» нужный драйвер.

**Архитектура JDBC:**
```
Java-приложение
      ↓
JDBC API (java.sql.*)         ← Стандартные интерфейсы
      ↓
JDBC Driver Manager           ← Управляет драйверами
      ↓
JDBC Driver (MySQL, H2, PG...) ← Специфичный для СУБД
      ↓
База данных
```

**Основные классы и интерфейсы:**

| Класс/Интерфейс | Назначение |
|-----------------|------------|
| `DriverManager` | Управление соединениями |
| `Connection` | Соединение с БД |
| `Statement` | Выполнение SQL-запросов |
| `PreparedStatement` | Предкомпилированный запрос с параметрами |
| `CallableStatement` | Вызов хранимых процедур |
| `ResultSet` | Результат запроса SELECT |

### 2.2 Базовая работа с JDBC

Давайте разберём пошагово, как выглядит типичная работа с базой данных через JDBC — от подключения до CRUD-операций.

```java
import java.sql.*;

// Строка подключения (Connection URL)
// H2 в памяти: jdbc:h2:mem:testdb
// H2 файловый: jdbc:h2:./data/mydb
// PostgreSQL:   jdbc:postgresql://localhost:5432/mydb
// MySQL:        jdbc:mysql://localhost:3306/mydb

String url = "jdbc:h2:mem:myapp;DB_CLOSE_DELAY=-1";

try (Connection conn = DriverManager.getConnection(url, "sa", "")) {
    System.out.println("Подключено к: " + conn.getMetaData().getURL());

    // 1. Создание таблицы
    String createSQL = """
        CREATE TABLE users (
            id      INT AUTO_INCREMENT PRIMARY KEY,
            name    VARCHAR(100) NOT NULL,
            email   VARCHAR(200) UNIQUE,
            age     INT
        )
        """;
    try (Statement stmt = conn.createStatement()) {
        stmt.execute(createSQL);
    }

    // 2. Вставка с PreparedStatement (защита от SQL Injection!)
    String insertSQL = "INSERT INTO users (name, email, age) VALUES (?, ?, ?)";
    try (PreparedStatement pstmt = conn.prepareStatement(insertSQL)) {
        pstmt.setString(1, "Иван Петров");
        pstmt.setString(2, "ivan@example.com");
        pstmt.setInt(3, 25);
        pstmt.executeUpdate();

        pstmt.setString(1, "Мария Сидорова");
        pstmt.setString(2, "maria@example.com");
        pstmt.setInt(3, 30);
        pstmt.executeUpdate();
    }

    // 3. Запрос SELECT
    // Важно: индексация столбцов в ResultSet начинается с 1, а не с 0!
    // Рекомендуется использовать имена столбцов (getString("name")) —
    // это безопаснее и читаемее, чем числовые индексы (getString(2))
    String selectSQL = "SELECT * FROM users WHERE age > ?";
    try (PreparedStatement pstmt = conn.prepareStatement(selectSQL)) {
        pstmt.setInt(1, 20);
        ResultSet rs = pstmt.executeQuery();
        while (rs.next()) {
            int id = rs.getInt("id");       // или rs.getInt(1)
            String name = rs.getString("name"); // или rs.getString(2)
            int age = rs.getInt("age");     // или rs.getInt(4)
            System.out.printf("id=%d, name=%s, age=%d%n", id, name, age);
        }
    }

    // 4. Обновление
    String updateSQL = "UPDATE users SET age = ? WHERE name = ?";
    try (PreparedStatement pstmt = conn.prepareStatement(updateSQL)) {
        pstmt.setInt(1, 26);
        pstmt.setString(2, "Иван Петров");
        int rows = pstmt.executeUpdate();
        System.out.println("Обновлено строк: " + rows);
    }

    // 5. Удаление
    String deleteSQL = "DELETE FROM users WHERE id = ?";
    try (PreparedStatement pstmt = conn.prepareStatement(deleteSQL)) {
        pstmt.setInt(1, 1);
        pstmt.executeUpdate();
    }
}
```

### 2.3 SQL Injection — почему нужен PreparedStatement?

Это важный момент: если вы подставляете пользовательский ввод прямо в SQL-строку, злоумышленник может выполнить произвольный SQL-код в вашей базе данных.

```java
// ОПАСНО — SQL Injection!
String userInput = "'; DROP TABLE users; --";
String badSQL = "SELECT * FROM users WHERE name = '" + userInput + "'";
// Результирующий SQL: SELECT * FROM users WHERE name = ''; DROP TABLE users; --'
// Это уничтожит таблицу!

// БЕЗОПАСНО — PreparedStatement экранирует параметры:
String safeSQL = "SELECT * FROM users WHERE name = ?";
try (PreparedStatement pstmt = conn.prepareStatement(safeSQL)) {
    pstmt.setString(1, userInput); // userInput обрабатывается как данные, не код
    ResultSet rs = pstmt.executeQuery();
    // Запрос выполнится безопасно — вернёт пустой результат
}
```

### 2.4 Транзакции

Транзакции гарантируют, что группа операций выполняется как единое целое: либо все успешно, либо ни одна. Классический пример — перевод денег между счетами.

```java
conn.setAutoCommit(false); // Начало транзакции
try {
    // Перевод денег — должно выполниться всё или ничего
    PreparedStatement debit = conn.prepareStatement(
        "UPDATE accounts SET balance = balance - ? WHERE id = ?"
    );
    debit.setDouble(1, 1000.0);
    debit.setInt(2, fromAccount);
    debit.executeUpdate();

    PreparedStatement credit = conn.prepareStatement(
        "UPDATE accounts SET balance = balance + ? WHERE id = ?"
    );
    credit.setDouble(1, 1000.0);
    credit.setInt(2, toAccount);
    credit.executeUpdate();

    conn.commit(); // Фиксируем транзакцию
    System.out.println("Перевод выполнен");
} catch (SQLException e) {
    conn.rollback(); // Откатываем при ошибке
    System.out.println("Ошибка, откат: " + e.getMessage());
} finally {
    conn.setAutoCommit(true); // Восстанавливаем автокоммит
}
```

### 2.5 DAO-паттерн (Data Access Object)

Вы могли заметить, что в примерах выше SQL-код перемешан с основной логикой программы. В небольшом примере это не проблема, но в реальном приложении такой подход быстро приводит к хаосу. DAO — паттерн проектирования, отделяющий логику доступа к данным от бизнес-логики.

**Преимущества DAO:**
- **Чистое разделение слоёв** — бизнес-логика не знает о SQL и JDBC
- **Тестируемость** — можно подменить реализацию DAO заглушкой (mock) в тестах
- **Заменяемость реализации** — можно переключиться с JDBC на Hibernate без изменения бизнес-логики

```java
// Модель (Entity)
public class Movie {
    private int id;
    private String title;
    private String genre;
    private int year;

    // Конструктор, геттеры, сеттеры...
}

// Интерфейс DAO
public interface MovieDAO {
    void createTable() throws SQLException;
    void insert(Movie movie) throws SQLException;
    Optional<Movie> findById(int id) throws SQLException;
    List<Movie> findAll() throws SQLException;
    List<Movie> findByGenre(String genre) throws SQLException;
    void update(Movie movie) throws SQLException;
    void delete(int id) throws SQLException;
}

// Реализация DAO
public class MovieDAOImpl implements MovieDAO {
    private final Connection connection;

    public MovieDAOImpl(Connection connection) {
        this.connection = connection;
    }

    @Override
    public void createTable() throws SQLException {
        String sql = """
            CREATE TABLE IF NOT EXISTS movies (
                id    INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(200) NOT NULL,
                genre VARCHAR(100),
                year  INT
            )
            """;
        try (Statement stmt = connection.createStatement()) {
            stmt.execute(sql);
        }
    }

    @Override
    public void insert(Movie movie) throws SQLException {
        String sql = "INSERT INTO movies (title, genre, year) VALUES (?, ?, ?)";
        try (PreparedStatement pstmt = connection.prepareStatement(sql,
                Statement.RETURN_GENERATED_KEYS)) {
            pstmt.setString(1, movie.getTitle());
            pstmt.setString(2, movie.getGenre());
            pstmt.setInt(3, movie.getYear());
            pstmt.executeUpdate();

            // Получаем сгенерированный ID
            try (ResultSet keys = pstmt.getGeneratedKeys()) {
                if (keys.next()) {
                    movie.setId(keys.getInt(1));
                }
            }
        }
    }

    @Override
    public Optional<Movie> findById(int id) throws SQLException {
        String sql = "SELECT * FROM movies WHERE id = ?";
        try (PreparedStatement pstmt = connection.prepareStatement(sql)) {
            pstmt.setInt(1, id);
            ResultSet rs = pstmt.executeQuery();
            if (rs.next()) {
                return Optional.of(mapRow(rs));
            }
        }
        return Optional.empty();
    }

    @Override
    public List<Movie> findAll() throws SQLException {
        List<Movie> movies = new ArrayList<>();
        String sql = "SELECT * FROM movies ORDER BY year";
        try (Statement stmt = connection.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
            while (rs.next()) {
                movies.add(mapRow(rs));
            }
        }
        return movies;
    }

    @Override
    public List<Movie> findByGenre(String genre) throws SQLException {
        List<Movie> movies = new ArrayList<>();
        String sql = "SELECT * FROM movies WHERE LOWER(genre) = LOWER(?)";
        try (PreparedStatement pstmt = connection.prepareStatement(sql)) {
            pstmt.setString(1, genre);
            ResultSet rs = pstmt.executeQuery();
            while (rs.next()) {
                movies.add(mapRow(rs));
            }
        }
        return movies;
    }

    @Override
    public void update(Movie movie) throws SQLException {
        String sql = "UPDATE movies SET title=?, genre=?, year=? WHERE id=?";
        try (PreparedStatement pstmt = connection.prepareStatement(sql)) {
            pstmt.setString(1, movie.getTitle());
            pstmt.setString(2, movie.getGenre());
            pstmt.setInt(3, movie.getYear());
            pstmt.setInt(4, movie.getId());
            pstmt.executeUpdate();
        }
    }

    @Override
    public void delete(int id) throws SQLException {
        String sql = "DELETE FROM movies WHERE id = ?";
        try (PreparedStatement pstmt = connection.prepareStatement(sql)) {
            pstmt.setInt(1, id);
            pstmt.executeUpdate();
        }
    }

    // Вспомогательный метод маппинга ResultSet -> Movie
    private Movie mapRow(ResultSet rs) throws SQLException {
        Movie movie = new Movie();
        movie.setId(rs.getInt("id"));
        movie.setTitle(rs.getString("title"));
        movie.setGenre(rs.getString("genre"));
        movie.setYear(rs.getInt("year"));
        return movie;
    }
}
```

---

Мы научились работать с базами данных через JDBC, но вы наверняка заметили, сколько повторяющегося кода приходится писать: создание `PreparedStatement`, установка параметров, маппинг `ResultSet` в объекты. Давайте посмотрим, как ORM-фреймворки решают эту проблему.

## Часть 3: ORM и Hibernate

### 3.1 Что такое ORM?

**ORM (Object-Relational Mapping)** — технология отображения между объектами Java и таблицами реляционной БД.

**Проблема без ORM:** Разработчик вручную пишет SQL для каждой операции CRUD, вручную маппит ResultSet в объекты и обратно. Это скучно, трудоёмко и источник ошибок.

**С ORM:** Вы описываете маппинг между классом и таблицей, а ORM-фреймворк генерирует SQL автоматически.

```
Java класс Movie   ←→   Таблица movies
   поле id         ←→   столбец id (PRIMARY KEY)
   поле title      ←→   столбец title
   поле genre      ←→   столбец genre
   поле year       ←→   столбец year
```

### 3.2 Hibernate — главный ORM для Java

Hibernate — самый популярный ORM-фреймворк для Java, реализующий стандарт JPA (Jakarta Persistence API). Давайте разберём, как он устроен.

#### Entity-класс с JPA-аннотациями

```java
import jakarta.persistence.*;

@Entity                         // Этот класс является сущностью JPA
@Table(name = "movies")         // Маппинг на таблицу movies
public class Movie {

    @Id                         // Первичный ключ
    @GeneratedValue(strategy = GenerationType.IDENTITY) // AUTO_INCREMENT
    private Integer id;

    @Column(name = "title", nullable = false, length = 200)
    private String title;

    @Column(name = "genre", length = 100)
    private String genre;

    @Column(name = "year")
    private Integer year;

    // Обязательный конструктор без аргументов для JPA
    public Movie() {}

    public Movie(String title, String genre, int year) {
        this.title = title;
        this.genre = genre;
        this.year = year;
    }

    // Геттеры и сеттеры...

    @Override
    public String toString() {
        return String.format("Movie{id=%d, title='%s', genre='%s', year=%d}",
            id, title, genre, year);
    }
}
```

#### Конфигурация Hibernate (hibernate.cfg.xml)

```xml
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE hibernate-configuration PUBLIC
        "-//Hibernate/Hibernate Configuration DTD 3.0//EN"
        "http://www.hibernate.org/dtd/hibernate-configuration-3.0.dtd">
<hibernate-configuration>
    <session-factory>
        <!-- Параметры подключения к H2 -->
        <property name="hibernate.connection.driver_class">org.h2.Driver</property>
        <property name="hibernate.connection.url">jdbc:h2:mem:moviedb;DB_CLOSE_DELAY=-1</property>
        <property name="hibernate.connection.username">sa</property>
        <property name="hibernate.connection.password"></property>

        <!-- Диалект H2 -->
        <property name="hibernate.dialect">org.hibernate.dialect.H2Dialect</property>

        <!-- Автоматическое создание таблиц -->
        <!-- create: удалить и создать заново при каждом запуске -->
        <!-- update: обновить схему если нужно -->
        <!-- validate: только проверить схему -->
        <!-- none: ничего не делать -->
        <property name="hibernate.hbm2ddl.auto">create</property>

        <!-- Вывод SQL в консоль (для разработки) -->
        <property name="hibernate.show_sql">true</property>
        <property name="hibernate.format_sql">true</property>

        <!-- Регистрация сущностей -->
        <mapping class="com.example.Movie"/>
    </session-factory>
</hibernate-configuration>
```

#### Основная работа с Hibernate

Обратите внимание на два ключевых объекта в Hibernate: `SessionFactory` и `Session`. `SessionFactory` — это тяжеловесная «фабрика», которая создаётся один раз при старте приложения. `Session` — это легковесный объект для одной единицы работы, подобно тому, как вы открываете и закрываете отдельные транзакции в банке.

```java
import org.hibernate.*;
import org.hibernate.cfg.Configuration;

public class HibernateDemo {
    public static void main(String[] args) {
        // Создание SessionFactory — дорогая операция, делать ОДИН РАЗ на приложение.
        // SessionFactory — потокобезопасный (thread-safe), тяжеловесный объект.
        SessionFactory sessionFactory = new Configuration()
            .configure("hibernate.cfg.xml")
            .buildSessionFactory();

        // Session — легковесный объект, создаётся для каждой единицы работы.
        // Session НЕ потокобезопасна (not thread-safe) — нельзя разделять между потоками.

        // СОХРАНЕНИЕ (CREATE)
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = session.beginTransaction();

            Movie m1 = new Movie("Матрица", "Фантастика", 1999);
            Movie m2 = new Movie("Начало", "Фантастика", 2010);
            Movie m3 = new Movie("Волк с Уолл-стрит", "Драма", 2013);

            session.persist(m1); // Hibernate создаёт INSERT
            session.persist(m2);
            session.persist(m3);

            tx.commit();
            System.out.println("Фильмы сохранены");
        }

        // ПОИСК ПО ID (READ)
        try (Session session = sessionFactory.openSession()) {
            Movie movie = session.get(Movie.class, 1); // SELECT WHERE id=1
            System.out.println("Найден: " + movie);
        }

        // ОБНОВЛЕНИЕ ЧЕРЕЗ HQL
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = session.beginTransaction();

            int updated = session.createMutationQuery(
                "UPDATE Movie SET year = :year WHERE title = :title"
            )
            .setParameter("year", 1998)
            .setParameter("title", "Матрица")
            .executeUpdate();

            tx.commit();
            System.out.println("Обновлено: " + updated);
        }

        // ПОИСК ЧЕРЕЗ HQL (Hibernate Query Language)
        try (Session session = sessionFactory.openSession()) {
            List<Movie> scifiMovies = session.createQuery(
                "FROM Movie WHERE genre = :genre ORDER BY year",
                Movie.class
            )
            .setParameter("genre", "Фантастика")
            .list();

            System.out.println("Фантастика:");
            scifiMovies.forEach(System.out::println);
        }

        // CRITERIA API (типобезопасный, без строк)
        try (Session session = sessionFactory.openSession()) {
            CriteriaBuilder cb = session.getCriteriaBuilder();
            CriteriaQuery<Movie> cq = cb.createQuery(Movie.class);
            Root<Movie> root = cq.from(Movie.class);

            // WHERE year > 2000 AND genre = 'Фантастика'
            cq.select(root).where(
                cb.and(
                    cb.greaterThan(root.get("year"), 2000),
                    cb.equal(root.get("genre"), "Фантастика")
                )
            ).orderBy(cb.asc(root.get("year")));

            List<Movie> result = session.createQuery(cq).list();
            System.out.println("Новая фантастика: " + result);
        }

        // УДАЛЕНИЕ
        try (Session session = sessionFactory.openSession()) {
            Transaction tx = session.beginTransaction();
            Movie toDelete = session.get(Movie.class, 3);
            if (toDelete != null) {
                session.remove(toDelete);
                System.out.println("Удалён: " + toDelete);
            }
            tx.commit();
        }

        sessionFactory.close();
    }
}
```

### 3.3 HQL vs JPQL vs Criteria API

У Hibernate есть два основных способа строить запросы. Давайте сравним их.

| | HQL/JPQL | Criteria API |
|---|---|---|
| Синтаксис | Строки (как SQL, но с именами классов) | Java-код (типобезопасный) |
| Ошибки | В рантайме | На этапе компиляции |
| Читаемость | Выше для простых запросов | Сложнее для сложных |
| Динамические запросы | Сложно | Легко |

```java
// HQL — строки, опечатки обнаружатся в рантайме
session.createQuery("FROM Moive WHERE genre = :genre", Movie.class) // Опечатка!

// Criteria API — типобезопасно, опечатки найдёт компилятор
cq.from(Movie.class) // Movie — имя класса, не строка
root.get("gendre")   // Ошибка обнаружится в рантайме при первом запросе
```

### 3.4 Связи между сущностями

В реляционных базах данных таблицы связаны друг с другом через внешние ключи. Hibernate позволяет описывать эти связи прямо в Java-классах с помощью аннотаций.

```java
// Один ко многим: Режиссёр -> Фильмы
@Entity
public class Director {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;
    private String name;

    @OneToMany(mappedBy = "director", cascade = CascadeType.ALL)
    private List<Movie> movies = new ArrayList<>();
}

@Entity
public class Movie {
    // ... поля ...

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "director_id")
    private Director director;
}
```

---

## Часть 4: Итоги

Давайте подведём итог всему, что мы рассмотрели на этой лекции:

| Технология | Ключевые концепции |
|------------|-------------------|
| Maven | pom.xml, GAV-координаты, жизненный цикл, репозитории |
| Gradle | build.gradle, DSL, tasks, buildscript |
| JDBC | Connection, PreparedStatement, ResultSet, транзакции |
| SQL Injection | PreparedStatement как защита |
| DAO | Паттерн разделения логики доступа к данным |
| Hibernate/JPA | @Entity, Session, HQL, Criteria API, связи |
| ORM | Маппинг Java-объектов на таблицы БД |

---

## Часть 5: Практические советы

### Выбор между Maven и Gradle

- **Maven**: Предпочтительно для энтерпрайз-проектов, богатая экосистема, конвенции
- **Gradle**: Предпочтительно для Android, быстрая сборка, гибкость

### Выбор между JDBC и Hibernate

- **Чистый JDBC**: Когда нужен полный контроль над SQL, высокая производительность
- **Hibernate/JPA**: Когда важна скорость разработки, объектная модель, переносимость между СУБД

### Connection Pool

В производственном коде не создавайте `Connection` напрямую — используйте пул соединений. Пул соединений работает как библиотека: вместо того чтобы каждый раз покупать новую книгу (открывать соединение), вы берёте её на время и возвращаете обратно.

```xml
<!-- HikariCP — самый быстрый пул соединений для Java -->
<dependency>
    <groupId>com.zaxxer</groupId>
    <artifactId>HikariCP</artifactId>
    <version>5.0.1</version>
</dependency>
```

```java
HikariConfig config = new HikariConfig();
config.setJdbcUrl("jdbc:h2:mem:test");
config.setMaximumPoolSize(10);
HikariDataSource dataSource = new HikariDataSource(config);

// Получение соединения из пула (автоматически возвращается при close)
try (Connection conn = dataSource.getConnection()) {
    // ...
}
```
