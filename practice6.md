# Практическое занятие 6: Системы сборки, JDBC и Hibernate

## Часть 1: Maven — настройка проекта

### Задание 1.1: Создание Maven-проекта вручную

Создайте структуру Maven-проекта вручную (без IDE):

```
movie-app/
├── pom.xml
└── src/
    └── main/
        └── java/
            └── com/
                └── movies/
                    └── Main.java
```

1. Создайте `pom.xml` со следующими зависимостями:
   - H2 Database (версия 2.2.224)
   - Добавьте свойство `maven.compiler.source` = 21

2. Создайте класс `Main.java` с методом `main`, который выводит "Movie App Started"

3. Выполните команды и запишите вывод:
   ```bash
   mvn compile          # Должен скомпилировать класс
   mvn package          # Должен создать JAR в target/
   mvn clean            # Удалит target/
   mvn dependency:list  # Покажет все зависимости
   ```

---

### Задание 1.2: Анализ зависимостей

Для проекта с `pom.xml`:
```xml
<dependencies>
    <dependency>
        <groupId>org.hibernate.orm</groupId>
        <artifactId>hibernate-core</artifactId>
        <version>6.4.0.Final</version>
    </dependency>
    <dependency>
        <groupId>com.h2database</groupId>
        <artifactId>h2</artifactId>
        <version>2.2.224</version>
    </dependency>
</dependencies>
```

Выполните `mvn dependency:tree` и ответьте:
1. Сколько прямых зависимостей?
2. Сколько транзитивных зависимостей добавляет Hibernate?
3. Какие зависимости Hibernate потянул за собой?

---

## Часть 2: JDBC — прямая работа с базой данных

### Задание 2.1: CRUD-операции (Задача 1 из задания)

Изучите и запустите программу `MovieJDBC`. Убедитесь, что все операции (создание, вставка, обновление, удаление, поиск) работают корректно. Объясните: (1) почему в `findByTitle` используется `LIKE` с `%`? (2) что такое `PreparedStatement` и чем он безопаснее `Statement`?

```java
import java.sql.*;
import java.util.*;

public class MovieJDBC {

    // URL для H2 в памяти
    private static final String URL = "jdbc:h2:mem:moviedb;DB_CLOSE_DELAY=-1";
    private static final String USER = "sa";
    private static final String PASS = "";

    public static void main(String[] args) throws SQLException {
        try (Connection conn = DriverManager.getConnection(URL, USER, PASS)) {
            System.out.println("Подключение успешно!");

            // 1. Удалить таблицу если существует и создать заново
            dropAndCreateTable(conn);

            // 2. Вставить 4 записи
            insertMovies(conn);

            // 3. Обновить одну запись через PreparedStatement
            updateMovie(conn, 1, "Матрица: Перезагрузка", "Фантастика", 2003);

            // 4. Удалить одну запись
            deleteMovie(conn, 2);

            // 5. Вывести все записи
            System.out.println("\n=== Все фильмы ===");
            printAllMovies(conn);

            // 6. Поиск по году
            System.out.println("\n=== Фильмы после 2000 года ===");
            findByYear(conn, 2000);

            // 7. Поиск по жанру
            System.out.println("\n=== Фантастика ===");
            findByGenre(conn, "Фантастика");

            // 8. Поиск по названию
            System.out.println("\n=== Поиск 'начало' ===");
            findByTitle(conn, "начало");
        }
    }

    static void dropAndCreateTable(Connection conn) throws SQLException {
        try (Statement stmt = conn.createStatement()) {
            stmt.execute("DROP TABLE IF EXISTS movies");
            stmt.execute("""
                CREATE TABLE movies (
                    id    INT AUTO_INCREMENT PRIMARY KEY,
                    title VARCHAR(200) NOT NULL,
                    genre VARCHAR(100),
                    year  INT
                )
            """);
            System.out.println("Таблица movies создана");
        }
    }

    static void insertMovies(Connection conn) throws SQLException {
        String sql = "INSERT INTO movies (title, genre, year) VALUES (?, ?, ?)";
        try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
            Object[][] movies = {
                {"Матрица", "Фантастика", 1999},
                {"Начало", "Фантастика", 2010},
                {"Лев", "Драма", 2016},
                {"Джокер", "Триллер", 2019}
            };
            for (Object[] movie : movies) {
                pstmt.setString(1, (String) movie[0]);
                pstmt.setString(2, (String) movie[1]);
                pstmt.setInt(3, (Integer) movie[2]);
                pstmt.executeUpdate();
                System.out.println("Добавлен: " + movie[0]);
            }
        }
    }

    static void updateMovie(Connection conn, int id, String title, String genre, int year)
            throws SQLException {
        String sql = "UPDATE movies SET title=?, genre=?, year=? WHERE id=?";
        try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setString(1, title);
            pstmt.setString(2, genre);
            pstmt.setInt(3, year);
            pstmt.setInt(4, id);
            pstmt.executeUpdate();
        }
        System.out.println("Обновлён фильм id=" + id);
    }

    static void deleteMovie(Connection conn, int id) throws SQLException {
        String sql = "DELETE FROM movies WHERE id=?";
        try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setInt(1, id);
            pstmt.executeUpdate();
        }
        System.out.println("Удалён фильм id=" + id);
    }

    static void printAllMovies(Connection conn) throws SQLException {
        String sql = "SELECT * FROM movies ORDER BY id";
        try (Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
            while (rs.next()) {
                System.out.printf("id=%d | %-30s | %-15s | %d%n",
                    rs.getInt("id"),
                    rs.getString("title"),
                    rs.getString("genre"),
                    rs.getInt("year"));
            }
        }
    }

    static void findByYear(Connection conn, int minYear) throws SQLException {
        String sql = "SELECT * FROM movies WHERE year > ? ORDER BY year";
        try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setInt(1, minYear);
            try (ResultSet rs = pstmt.executeQuery()) {
                while (rs.next()) {
                    System.out.printf("id=%d | %-30s | %-15s | %d%n",
                        rs.getInt("id"), rs.getString("title"),
                        rs.getString("genre"), rs.getInt("year"));
                }
            }
        }
    }

    static void findByGenre(Connection conn, String genre) throws SQLException {
        String sql = "SELECT * FROM movies WHERE LOWER(genre) = LOWER(?) ORDER BY year";
        try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setString(1, genre);
            try (ResultSet rs = pstmt.executeQuery()) {
                while (rs.next()) {
                    System.out.printf("id=%d | %-30s | %-15s | %d%n",
                        rs.getInt("id"), rs.getString("title"),
                        rs.getString("genre"), rs.getInt("year"));
                }
            }
        }
    }

    static void findByTitle(Connection conn, String titlePart) throws SQLException {
        String sql = "SELECT * FROM movies WHERE LOWER(title) LIKE LOWER(?) ORDER BY id";
        try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setString(1, "%" + titlePart + "%");
            try (ResultSet rs = pstmt.executeQuery()) {
                while (rs.next()) {
                    System.out.printf("id=%d | %-30s | %-15s | %d%n",
                        rs.getInt("id"), rs.getString("title"),
                        rs.getString("genre"), rs.getInt("year"));
                }
            }
        }
    }
}
```

---

### Задание 2.2: DAO-паттерн (Задача 2 из задания)

Реализуйте DAO-паттерн для работы с таблицей `movies`:

1. **Класс `Movie`**: поля `id` (Integer), `title` (String), `genre` (String), `year` (Integer); конструкторы (без аргументов и с `title, genre, year`); геттеры и сеттеры для всех полей; `toString()`.

2. **Интерфейс `MovieDAO`**: методы `createTable()`, `dropTable()`, `insert(Movie)`, `delete(int id)`, `updateTitle(int id, String newTitle)`, `findById(int id)` → `Optional<Movie>`, `findAll()` → `List<Movie>`, `findByTitle(String part)`, `findByGenre(String genre)`, `findByYear(int year)`.

3. **Класс `MovieDAOImpl implements MovieDAO`**: принимает `Connection` в конструкторе. Все методы используют `PreparedStatement`. Метод `insert` получает сгенерированный `id` через `getGeneratedKeys()`. Вспомогательный метод `mapRow(ResultSet rs)` → `Movie`.

4. **Класс `DAOTest`**: создайте H2 in-memory соединение (`jdbc:h2:mem:movietest;DB_CLOSE_DELAY=-1`), вставьте 4 фильма, обновите заголовок, удалите один, выведите все, найдите по id, жанру, году, части названия.

---

## Часть 3: Hibernate ORM (Задача 3)

### Задание 3.1: Настройка Hibernate

Добавьте в `pom.xml` зависимости:

```xml
<dependencies>
    <dependency>
        <groupId>org.hibernate.orm</groupId>
        <artifactId>hibernate-core</artifactId>
        <version>6.4.0.Final</version>
    </dependency>
    <dependency>
        <groupId>com.h2database</groupId>
        <artifactId>h2</artifactId>
        <version>2.2.224</version>
    </dependency>
</dependencies>
```

Создайте `src/main/resources/hibernate.cfg.xml`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE hibernate-configuration PUBLIC
        "-//Hibernate/Hibernate Configuration DTD 3.0//EN"
        "http://www.hibernate.org/dtd/hibernate-configuration-3.0.dtd">
<hibernate-configuration>
    <session-factory>
        <property name="hibernate.connection.driver_class">org.h2.Driver</property>
        <property name="hibernate.connection.url">jdbc:h2:mem:moviedb;DB_CLOSE_DELAY=-1</property>
        <property name="hibernate.connection.username">sa</property>
        <property name="hibernate.connection.password"></property>
        <property name="hibernate.dialect">org.hibernate.dialect.H2Dialect</property>
        <property name="hibernate.hbm2ddl.auto">create</property>
        <property name="hibernate.show_sql">true</property>
        <property name="hibernate.format_sql">false</property>
        <mapping class="com.movies.Movie"/>
    </session-factory>
</hibernate-configuration>
```

---

### Задание 3.2: Entity-класс

Изучите Entity-класс `Movie`. Объясните назначение аннотаций: `@Entity`, `@Table`, `@Id`, `@GeneratedValue`, `@Column`. Что произойдёт если убрать `@Column(nullable = false)` — на уровне кода или базы данных?

```java
package com.movies;

import jakarta.persistence.*;

@Entity
@Table(name = "movies")
public class Movie {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(name = "title", nullable = false, length = 200)
    private String title;

    @Column(name = "genre", length = 100)
    private String genre;

    @Column(name = "year")
    private Integer year;

    public Movie() {}

    public Movie(String title, String genre, int year) {
        this.title = title;
        this.genre = genre;
        this.year = year;
    }

    public Integer getId() { return id; }
    public void setId(Integer id) { this.id = id; }
    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }
    public String getGenre() { return genre; }
    public void setGenre(String genre) { this.genre = genre; }
    public Integer getYear() { return year; }
    public void setYear(Integer year) { this.year = year; }

    @Override
    public String toString() {
        return String.format("Movie{id=%d, title='%s', genre='%s', year=%d}",
            id, title, genre, year);
    }
}
```

---

### Задание 3.3: Работа с Hibernate

Изучите и запустите программу работы с Hibernate. Убедитесь, что все операции работают корректно. Объясните: (1) чем HQL отличается от SQL? (2) когда предпочтительнее Criteria API вместо HQL? (3) что такое сессия (`Session`) в Hibernate?

```java
package com.movies;

import jakarta.persistence.criteria.*;
import org.hibernate.*;
import org.hibernate.cfg.Configuration;

import java.util.List;

public class HibernateMain {

    private static SessionFactory buildSessionFactory() {
        return new Configuration()
            .configure("hibernate.cfg.xml")
            .buildSessionFactory();
    }

    // Сохранение нескольких фильмов
    static void saveMovies(SessionFactory sf) {
        try (Session session = sf.openSession()) {
            Transaction tx = session.beginTransaction();

            session.persist(new Movie("Матрица", "Фантастика", 1999));
            session.persist(new Movie("Начало", "Фантастика", 2010));
            session.persist(new Movie("Тёмный рыцарь", "Боевик", 2008));
            session.persist(new Movie("Паразиты", "Триллер", 2019));
            session.persist(new Movie("Интерстеллар", "Фантастика", 2014));

            tx.commit();
            System.out.println("Фильмы сохранены");
        }
    }

    // Обновление через HQL
    static void updateMovieByHQL(SessionFactory sf, String title, int newYear) {
        try (Session session = sf.openSession()) {
            Transaction tx = session.beginTransaction();

            int updated = session.createMutationQuery(
                "UPDATE Movie SET year = :year WHERE title = :title"
            )
            .setParameter("year", newYear)
            .setParameter("title", title)
            .executeUpdate();

            tx.commit();
            System.out.println("Обновлено записей: " + updated);
        }
    }

    // Удаление по id
    static void deleteById(SessionFactory sf, int id) {
        try (Session session = sf.openSession()) {
            Transaction tx = session.beginTransaction();

            Movie movie = session.get(Movie.class, id);
            if (movie != null) {
                session.remove(movie);
                System.out.println("Удалён: " + movie.getTitle());
            }

            tx.commit();
        }
    }

    // Поиск через HQL
    static List<Movie> findByGenreHQL(SessionFactory sf, String genre) {
        try (Session session = sf.openSession()) {
            return session.createQuery("FROM Movie WHERE genre = :genre ORDER BY year", Movie.class)
                .setParameter("genre", genre)
                .list();
        }
    }

    // Поиск через Criteria API
    static List<Movie> findByYearRange(SessionFactory sf, int fromYear, int toYear) {
        try (Session session = sf.openSession()) {
            CriteriaBuilder cb = session.getCriteriaBuilder();
            CriteriaQuery<Movie> cq = cb.createQuery(Movie.class);
            Root<Movie> root = cq.from(Movie.class);

            cq.select(root)
                .where(cb.between(root.get("year"), fromYear, toYear))
                .orderBy(cb.asc(root.get("year")));

            return session.createQuery(cq).list();
        }
    }

    // Поиск по названию через Criteria API
    static List<Movie> findByTitleLike(SessionFactory sf, String titlePart) {
        try (Session session = sf.openSession()) {
            CriteriaBuilder cb = session.getCriteriaBuilder();
            CriteriaQuery<Movie> cq = cb.createQuery(Movie.class);
            Root<Movie> root = cq.from(Movie.class);

            cq.select(root).where(cb.like(cb.lower(root.get("title")), "%" + titlePart.toLowerCase() + "%"));

            return session.createQuery(cq).list();
        }
    }

    public static void main(String[] args) {
        try (SessionFactory sf = buildSessionFactory()) {
            // Сохранение
            saveMovies(sf);

            System.out.println("\n=== Обновление через HQL ===");
            updateMovieByHQL(sf, "Матрица", 1998);

            System.out.println("\n=== Удаление по id ===");
            deleteById(sf, 3);

            System.out.println("\n=== Поиск фантастики (HQL) ===");
            findByGenreHQL(sf, "Фантастика").forEach(System.out::println);

            System.out.println("\n=== Фильмы 2000-2015 (Criteria API) ===");
            findByYearRange(sf, 2000, 2015).forEach(System.out::println);

            System.out.println("\n=== Поиск 'тёмн' (Criteria API) ===");
            findByTitleLike(sf, "тёмн").forEach(System.out::println);
        }
    }
}
```

---

## Часть 4: Дополнительные задания

### Задание 4.1: Транзакции в JDBC

Реализуйте перевод средств между банковскими счетами с управлением транзакциями JDBC:

1. Создайте таблицу `accounts (id INT PRIMARY KEY, owner VARCHAR(100), balance DECIMAL(10,2))`.
2. Добавьте несколько счетов через `INSERT`.
3. Реализуйте метод `transfer(Connection conn, int fromId, int toId, double amount)`:
   - Установите `conn.setAutoCommit(false)`.
   - Проверьте, что на счёте `fromId` достаточно средств.
   - Если средств хватает: спишите с `fromId`, зачислите на `toId`, вызовите `conn.commit()`.
   - Если средств не хватает или произошла ошибка: вызовите `conn.rollback()`.
   - В блоке `finally` верните `conn.setAutoCommit(true)`.
4. Протестируйте: корректный перевод, перевод при недостатке средств.

---

### Задание 4.2: Пагинация в Hibernate

```java
// Реализуйте метод поиска с пагинацией:
// findPage(SessionFactory sf, int pageNumber, int pageSize)
// pageNumber начинается с 1
// Выведите страницу 1 (3 фильма), страницу 2 (3 фильма)

static List<Movie> findPage(SessionFactory sf, int pageNumber, int pageSize) {
    try (Session session = sf.openSession()) {
        return session.createQuery("FROM Movie ORDER BY id", Movie.class)
            .setFirstResult((pageNumber - 1) * pageSize) // Смещение
            .setMaxResults(pageSize)                     // Количество
            .list();
    }
}
```

---

### Задание 4.3: Агрегация через HQL

Изучите и запустите агрегационные HQL-запросы. Объясните: (1) что возвращает `createQuery` с `SELECT genre, COUNT(*)`? (2) чем `uniqueResult()` отличается от `.list()`?

```java
static void runAggregationQueries(SessionFactory sf) {
    try (Session session = sf.openSession()) {
        // 1. Количество фильмов каждого жанра
        System.out.println("=== Количество фильмов по жанрам ===");
        List<Object[]> byGenre = session.createQuery(
            "SELECT genre, COUNT(*) FROM Movie GROUP BY genre", Object[].class).list();
        byGenre.forEach(row -> System.out.println(row[0] + ": " + row[1]));

        // 2. Средний год выхода
        System.out.println("\n=== Средний год выхода ===");
        Double avgYear = session.createQuery(
            "SELECT AVG(year) FROM Movie", Double.class).uniqueResult();
        System.out.printf("Средний год: %.1f%n", avgYear);

        // 3. Самый новый фильм каждого жанра
        System.out.println("\n=== Новейший фильм каждого жанра ===");
        List<Object[]> newestByGenre = session.createQuery(
            "SELECT genre, MAX(year) FROM Movie GROUP BY genre", Object[].class).list();
        newestByGenre.forEach(row -> System.out.println(row[0] + ": " + row[1]));
    }
}
```

---

## Часть 5: Контрольные вопросы

Ответьте письменно:

1. Что такое GAV-координаты в Maven? Для чего они используются?
2. В чём разница между `<scope>compile</scope>` и `<scope>test</scope>`?
3. Что такое транзитивные зависимости? Может ли это стать проблемой?
4. Чем Gradle отличается от Maven? Назовите 2-3 преимущества каждого.
5. Что такое JDBC Driver? Почему для разных СУБД нужны разные драйверы?
6. Чем `PreparedStatement` отличается от `Statement`? Зачем нужен PreparedStatement?
7. Что такое SQL Injection? Как PreparedStatement защищает от неё?
8. Что такое транзакция? Что означают свойства ACID?
9. Что такое ORM? Какие преимущества и недостатки по сравнению с чистым JDBC?
10. Что такое @Entity и @Table в Hibernate? Что происходит если они отсутствуют?
11. Чем HQL отличается от SQL? Чем HQL отличается от Criteria API?
12. Что означает `hbm2ddl.auto = create` в конфигурации Hibernate?

---

## Результаты занятия

К концу занятия вы должны сдать:
1. Задача 1: `MovieJDBC.java` — CRUD через чистый JDBC
2. Задача 2: `Movie.java`, `MovieDAO.java`, `MovieDAOImpl.java`, `DAOTest.java` — DAO-паттерн
3. Задача 3: `Movie.java` (с аннотациями), `HibernateMain.java`, `hibernate.cfg.xml` — Hibernate
4. Ответы на контрольные вопросы

**Критерии оценки:**
- Все программы запускаются и дают корректные результаты
- Используется PreparedStatement (не конкатенация строк!)
- Ресурсы закрыты через try-with-resources
- DAO реализует все методы интерфейса
- Hibernate-запросы работают корректно (HQL + Criteria API)
