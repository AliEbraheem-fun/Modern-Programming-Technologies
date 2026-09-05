# Тест 6: Системы сборки, JDBC, Hibernate, Stream API и транзакции (Лекция 6)

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

<!-- ===== РАЗДЕЛ 1: СИСТЕМЫ СБОРКИ — MAVEN (Вопросы 1–10) ===== -->

<div class="quiz-question" data-correct="2">
<h4>Вопрос 1. Какую основную проблему решают системы сборки (Maven, Gradle)?</h4>

<div class="quiz-option" data-index="0">Запуск IDE и подключение к серверу</div>
<div class="quiz-option" data-index="1">Написание исходного кода на Java</div>
<div class="quiz-option" data-index="2">Автоматизация компиляции, управления зависимостями, тестирования и упаковки</div>
<div class="quiz-option" data-index="3">Создание графического интерфейса пользователя</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 2. В стандартной структуре Maven-проекта, где размещаются исходные Java-файлы приложения?</h4>

<div class="quiz-option" data-index="0">src/test/java</div>
<div class="quiz-option" data-index="1">src/main/java</div>
<div class="quiz-option" data-index="2">src/main/resources</div>
<div class="quiz-option" data-index="3">target/classes</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 3. Куда Maven помещает скомпилированные файлы и результаты сборки?</h4>

<div class="quiz-option" data-index="0">src/main/java</div>
<div class="quiz-option" data-index="1">src/main/resources</div>
<div class="quiz-option" data-index="2">lib/</div>
<div class="quiz-option" data-index="3">target/</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 4. Что такое GAV-координаты в Maven?</h4>

<div class="quiz-option" data-index="0">groupId, artifactId, version — уникальный идентификатор проекта или зависимости</div>
<div class="quiz-option" data-index="1">goal, action, value — параметры запуска плагинов</div>
<div class="quiz-option" data-index="2">gradle, ant, version — совместимость систем сборки</div>
<div class="quiz-option" data-index="3">git, archive, validate — команды контроля версий</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 5. Какой фрагмент pom.xml корректно описывает зависимость с областью видимости только для тестов?</h4>

```xml
<!-- Вариант A -->
<dependency>
  <groupId>org.junit.jupiter</groupId>
  <artifactId>junit-jupiter</artifactId>
  <version>5.10.0</version>
</dependency>

<!-- Вариант B -->
<dependency>
  <groupId>org.junit.jupiter</groupId>
  <artifactId>junit-jupiter</artifactId>
  <version>5.10.0</version>
  <scope>test</scope>
</dependency>
```

<div class="quiz-option" data-index="0">Вариант A — scope по умолчанию подходит для тестов</div>
<div class="quiz-option" data-index="1">Оба варианта — scope не влияет на видимость</div>
<div class="quiz-option" data-index="2">Вариант B — scope test ограничивает зависимость фазой тестирования</div>
<div class="quiz-option" data-index="3">Ни один — для тестов нужен scope=provided</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 6. Что произойдёт при выполнении команды `mvn package`?</h4>

<div class="quiz-option" data-index="0">Выполнится только упаковка в JAR без компиляции и тестирования</div>
<div class="quiz-option" data-index="1">Последовательно выполнятся фазы validate, compile, test, package</div>
<div class="quiz-option" data-index="2">Выполнится только фаза package и фаза deploy</div>
<div class="quiz-option" data-index="3">Будет загружен JAR-файл в Maven Central</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 7. Какая команда Maven устанавливает артефакт в локальный репозиторий ~/.m2/repository?</h4>

<div class="quiz-option" data-index="0">mvn deploy</div>
<div class="quiz-option" data-index="1">mvn package</div>
<div class="quiz-option" data-index="2">mvn compile</div>
<div class="quiz-option" data-index="3">mvn install</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 8. В каком порядке Maven ищет зависимости?</h4>

<div class="quiz-option" data-index="0">Локальный репозиторий (~/.m2/repository) → Maven Central → пользовательские репозитории</div>
<div class="quiz-option" data-index="1">Maven Central → локальный репозиторий → пользовательские репозитории</div>
<div class="quiz-option" data-index="2">Пользовательские репозитории → Maven Central → локальный репозиторий</div>
<div class="quiz-option" data-index="3">Всегда скачивает заново из Maven Central</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 9. Какая область видимости (scope) зависимости используется в Maven по умолчанию, если scope не указан?</h4>

<div class="quiz-option" data-index="0">test</div>
<div class="quiz-option" data-index="1">provided</div>
<div class="quiz-option" data-index="2">compile</div>
<div class="quiz-option" data-index="3">runtime</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 10. Какая команда Maven показывает дерево зависимостей проекта?</h4>

<div class="quiz-option" data-index="0">mvn dependencies:list</div>
<div class="quiz-option" data-index="1">mvn dependency:tree</div>
<div class="quiz-option" data-index="2">mvn show:dependencies</div>
<div class="quiz-option" data-index="3">mvn tree:dependencies</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 2: СИСТЕМЫ СБОРКИ — GRADLE (Вопросы 11–16) ===== -->

<div class="quiz-question" data-correct="3">
<h4>Вопрос 11. Какое ключевое преимущество Gradle перед Maven?</h4>

<div class="quiz-option" data-index="0">Gradle использует XML, что более стандартно</div>
<div class="quiz-option" data-index="1">Gradle не поддерживает управление зависимостями</div>
<div class="quiz-option" data-index="2">Gradle не требует JDK для работы</div>
<div class="quiz-option" data-index="3">Gradle использует DSL (Groovy/Kotlin) вместо XML и выполняет инкрементальные сборки быстрее</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 12. Как называется основной файл конфигурации сборки в Gradle-проекте на Kotlin DSL?</h4>

<div class="quiz-option" data-index="0">build.gradle.kts</div>
<div class="quiz-option" data-index="1">pom.xml</div>
<div class="quiz-option" data-index="2">settings.xml</div>
<div class="quiz-option" data-index="3">gradle.config</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 13. Что делает Gradle Wrapper (gradlew/gradlew.bat)?</h4>

<div class="quiz-option" data-index="0">Шифрует исходный код перед сборкой</div>
<div class="quiz-option" data-index="1">Упаковывает проект в Docker-контейнер</div>
<div class="quiz-option" data-index="2">Позволяет запускать сборку без предварительной установки Gradle — автоматически скачивает нужную версию</div>
<div class="quiz-option" data-index="3">Создаёт оболочку вокруг Maven для совместимости</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 14. Какая конфигурация зависимостей в Gradle аналогична scope test в Maven?</h4>

<div class="quiz-option" data-index="0">implementation</div>
<div class="quiz-option" data-index="1">testImplementation</div>
<div class="quiz-option" data-index="2">compileOnly</div>
<div class="quiz-option" data-index="3">runtimeOnly</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 15. Какая команда Gradle полностью пересобирает проект, предварительно удалив результаты предыдущей сборки?</h4>

<div class="quiz-option" data-index="0">./gradlew build</div>
<div class="quiz-option" data-index="1">./gradlew rebuild</div>
<div class="quiz-option" data-index="2">./gradlew test</div>
<div class="quiz-option" data-index="3">./gradlew clean build</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 16. Какой фрагмент build.gradle.kts корректно добавляет зависимость для основного кода?</h4>

```kotlin
// Вариант A
dependencies {
    implementation("com.google.guava:guava:32.1.2-jre")
}

// Вариант B
dependencies {
    testImplementation("com.google.guava:guava:32.1.2-jre")
}
```

<div class="quiz-option" data-index="0">Вариант A — implementation подключает зависимость для основного кода</div>
<div class="quiz-option" data-index="1">Вариант B — testImplementation подходит для любого кода</div>
<div class="quiz-option" data-index="2">Оба варианта эквивалентны</div>
<div class="quiz-option" data-index="3">Ни один — нужно использовать compile вместо implementation</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 3: JDBC (Вопросы 17–32) ===== -->

<div class="quiz-question" data-correct="2">
<h4>Вопрос 17. Какова правильная последовательность компонентов в архитектуре JDBC?</h4>

<div class="quiz-option" data-index="0">Java-приложение → База данных → JDBC Driver → DriverManager</div>
<div class="quiz-option" data-index="1">JDBC Driver → DriverManager → Java-приложение → База данных</div>
<div class="quiz-option" data-index="2">Java-приложение → JDBC API → DriverManager → JDBC Driver → База данных</div>
<div class="quiz-option" data-index="3">База данных → JDBC API → Java-приложение → DriverManager</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 18. Какой метод используется для получения соединения с базой данных через JDBC?</h4>

<div class="quiz-option" data-index="0">Connection.open(url)</div>
<div class="quiz-option" data-index="1">DriverManager.getConnection(url)</div>
<div class="quiz-option" data-index="2">Database.connect(url)</div>
<div class="quiz-option" data-index="3">JDBC.createConnection(url)</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 19. Какой формат URL используется для подключения к in-memory базе H2?</h4>

<div class="quiz-option" data-index="0">jdbc:h2:mem:testdb</div>
<div class="quiz-option" data-index="1">h2://memory/testdb</div>
<div class="quiz-option" data-index="2">jdbc:memory:h2:testdb</div>
<div class="quiz-option" data-index="3">database:h2:mem:testdb</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 20. Чем PreparedStatement отличается от Statement?</h4>

<div class="quiz-option" data-index="0">PreparedStatement работает только с SELECT-запросами</div>
<div class="quiz-option" data-index="1">Statement быстрее, так как не требует компиляции</div>
<div class="quiz-option" data-index="2">PreparedStatement не поддерживает параметры</div>
<div class="quiz-option" data-index="3">PreparedStatement использует параметризованные запросы и предотвращает SQL-инъекции</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 21. Что такое SQL-инъекция? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
// Опасный код:
String name = "'; DROP TABLE users; --";
String sql = "SELECT * FROM users WHERE name = '" + name + "'";
System.out.println(sql);
```

<div class="quiz-option" data-index="0">Ошибка компиляции при работе с SQL</div>
<div class="quiz-option" data-index="1">Атака, при которой злоумышленник внедряет SQL-код через конкатенацию пользовательского ввода в SQL-запрос</div>
<div class="quiz-option" data-index="2">Способ ускорения SQL-запросов через инъекцию индексов</div>
<div class="quiz-option" data-index="3">Метод оптимизации PreparedStatement</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 22. Какой код корректно использует PreparedStatement для вставки данных?</h4>

```java
// Вариант A
PreparedStatement ps = conn.prepareStatement(
    "INSERT INTO users VALUES ('" + name + "', " + age + ")");
ps.executeUpdate();

// Вариант B
PreparedStatement ps = conn.prepareStatement(
    "INSERT INTO users (name, age) VALUES (?, ?)");
ps.setString(1, name);
ps.setInt(2, age);
ps.executeUpdate();
```

<div class="quiz-option" data-index="0">Вариант A — прямая конкатенация быстрее</div>
<div class="quiz-option" data-index="1">Оба варианта одинаково безопасны</div>
<div class="quiz-option" data-index="2">Вариант B — параметры через ? и set-методы предотвращают SQL-инъекции</div>
<div class="quiz-option" data-index="3">Ни один — нужно использовать CallableStatement</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 23. Какой метод ResultSet используется для перехода к следующей строке результата?</h4>

<div class="quiz-option" data-index="0">next()</div>
<div class="quiz-option" data-index="1">moveNext()</div>
<div class="quiz-option" data-index="2">hasNext()</div>
<div class="quiz-option" data-index="3">advance()</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 24. Какой паттерн итерации по ResultSet является стандартным?</h4>

<div class="quiz-option" data-index="0">for (int i = 0; i < rs.size(); i++) { rs.get(i); }</div>
<div class="quiz-option" data-index="1">for (Row row : rs) { row.getString("name"); }</div>
<div class="quiz-option" data-index="2">rs.forEach(row -> row.getString("name"));</div>
<div class="quiz-option" data-index="3">while (rs.next()) { rs.getString("name"); }</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 25. Какой метод PreparedStatement используется для выполнения SELECT-запроса?</h4>

<div class="quiz-option" data-index="0">executeUpdate()</div>
<div class="quiz-option" data-index="1">executeQuery()</div>
<div class="quiz-option" data-index="2">execute()</div>
<div class="quiz-option" data-index="3">runQuery()</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 26. Какой метод PreparedStatement используется для выполнения INSERT, UPDATE или DELETE?</h4>

<div class="quiz-option" data-index="0">executeQuery()</div>
<div class="quiz-option" data-index="1">runUpdate()</div>
<div class="quiz-option" data-index="2">executeUpdate()</div>
<div class="quiz-option" data-index="3">executeModify()</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 27. Что делает вызов connection.setAutoCommit(false)?</h4>

<div class="quiz-option" data-index="0">Отключает автоматическую фиксацию — изменения требуют явного вызова commit()</div>
<div class="quiz-option" data-index="1">Запрещает любые изменения в базе данных</div>
<div class="quiz-option" data-index="2">Включает режим только для чтения</div>
<div class="quiz-option" data-index="3">Автоматически откатывает все транзакции</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 28. Что произойдёт, если после setAutoCommit(false) вызвать rollback() вместо commit()?</h4>

<div class="quiz-option" data-index="0">Все изменения будут сохранены</div>
<div class="quiz-option" data-index="1">Программа завершится с ошибкой</div>
<div class="quiz-option" data-index="2">Изменения будут сохранены частично</div>
<div class="quiz-option" data-index="3">Все изменения текущей транзакции будут отменены</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 29. Какой интерфейс JDBC используется для вызова хранимых процедур базы данных?</h4>

<div class="quiz-option" data-index="0">Statement</div>
<div class="quiz-option" data-index="1">CallableStatement</div>
<div class="quiz-option" data-index="2">PreparedStatement</div>
<div class="quiz-option" data-index="3">StoredProcedure</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 30. Какой код корректно считывает имя и возраст из ResultSet? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
// Предположим: таблица users(name VARCHAR, age INT)
// Вариант A
String name = rs.getString(0);
int age = rs.getInt(1);

// Вариант B
String name = rs.getString("name");
int age = rs.getInt("age");
```

<div class="quiz-option" data-index="0">Вариант A — индексация с нуля стандартна в Java</div>
<div class="quiz-option" data-index="1">Оба варианта корректны</div>
<div class="quiz-option" data-index="2">Вариант B — в JDBC индексация столбцов начинается с 1, а не с 0; по имени — безопаснее</div>
<div class="quiz-option" data-index="3">Ни один — нужно использовать rs.getColumn("name")</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 31. Какой URL используется для подключения к PostgreSQL через JDBC?</h4>

<div class="quiz-option" data-index="0">jdbc:postgresql://localhost:5432/mydb</div>
<div class="quiz-option" data-index="1">postgresql://localhost:5432/mydb</div>
<div class="quiz-option" data-index="2">jdbc:postgres:localhost:5432:mydb</div>
<div class="quiz-option" data-index="3">db:postgresql://localhost/mydb</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 32. Какой код выполняет CRUD-операцию «обновление» (UPDATE) через JDBC?</h4>

```java
// Вариант A
ps = conn.prepareStatement("SELECT * FROM users WHERE id = ?");
ps.setInt(1, userId);
ResultSet rs = ps.executeQuery();

// Вариант B
ps = conn.prepareStatement("UPDATE users SET name = ? WHERE id = ?");
ps.setString(1, newName);
ps.setInt(2, userId);
int rows = ps.executeUpdate();
```

<div class="quiz-option" data-index="0">Вариант A — SELECT обновляет данные при чтении</div>
<div class="quiz-option" data-index="1">Оба варианта выполняют обновление</div>
<div class="quiz-option" data-index="2">Ни один — обновление возможно только через Statement</div>
<div class="quiz-option" data-index="3">Вариант B — UPDATE-запрос через executeUpdate() изменяет данные в таблице</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 4: DAO PATTERN (Вопросы 33–36) ===== -->

<div class="quiz-question" data-correct="1">
<h4>Вопрос 33. Что такое паттерн DAO (Data Access Object)?</h4>

<div class="quiz-option" data-index="0">Фреймворк для создания графического интерфейса</div>
<div class="quiz-option" data-index="1">Паттерн, отделяющий логику доступа к данным от бизнес-логики приложения</div>
<div class="quiz-option" data-index="2">Альтернативное название для JDBC API</div>
<div class="quiz-option" data-index="3">Способ хранения данных в оперативной памяти</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 34. Какие методы обычно содержит интерфейс DAO?</h4>

<div class="quiz-option" data-index="0">CRUD: create (save), findById, findAll, update, delete</div>
<div class="quiz-option" data-index="1">Только select и insert</div>
<div class="quiz-option" data-index="2">open, close, read, write</div>
<div class="quiz-option" data-index="3">connect, disconnect, execute</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 35. Какое преимущество даёт использование паттерна DAO?</h4>

<div class="quiz-option" data-index="0">Ускоряет выполнение SQL-запросов</div>
<div class="quiz-option" data-index="1">Автоматически создаёт таблицы в базе данных</div>
<div class="quiz-option" data-index="2">Исключает необходимость использования JDBC</div>
<div class="quiz-option" data-index="3">Чистое разделение слоёв, тестируемость и возможность замены реализации доступа к данным</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 36. Какой фрагмент кода демонстрирует правильную структуру DAO-интерфейса?</h4>

```java
// Вариант A
public class UserDAO {
    public void save(User user) {
        // прямой SQL в бизнес-логике
    }
}

// Вариант B
public interface UserDao {
    void save(User user);
    User findById(long id);
    List<User> findAll();
    void update(User user);
    void delete(long id);
}
```

<div class="quiz-option" data-index="0">Вариант A — класс с конкретной реализацией</div>
<div class="quiz-option" data-index="1">Оба варианта одинаково правильные</div>
<div class="quiz-option" data-index="2">Вариант B — интерфейс с CRUD-методами, реализация в отдельном классе</div>
<div class="quiz-option" data-index="3">Ни один — DAO должен наследовать абстрактный класс Database</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 5: ORM И HIBERNATE (Вопросы 37–50) ===== -->

<div class="quiz-question" data-correct="1">
<h4>Вопрос 37. Что такое ORM (Object-Relational Mapping)?</h4>

<div class="quiz-option" data-index="0">Язык запросов для реляционных баз данных</div>
<div class="quiz-option" data-index="1">Технология отображения Java-объектов на таблицы реляционной базы данных</div>
<div class="quiz-option" data-index="2">Формат хранения объектов в файловой системе</div>
<div class="quiz-option" data-index="3">Протокол сетевого взаимодействия с СУБД</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 38. Какое отношение между Hibernate и JPA?</h4>

<div class="quiz-option" data-index="0">Hibernate — это реализация (провайдер) спецификации JPA</div>
<div class="quiz-option" data-index="1">JPA — это реализация Hibernate</div>
<div class="quiz-option" data-index="2">Hibernate и JPA — это разные названия одного продукта</div>
<div class="quiz-option" data-index="3">JPA заменил Hibernate и является его преемником</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 39. Какая JPA-аннотация помечает класс как сущность, отображаемую на таблицу?</h4>

<div class="quiz-option" data-index="0">@Table</div>
<div class="quiz-option" data-index="1">@Column</div>
<div class="quiz-option" data-index="2">@Id</div>
<div class="quiz-option" data-index="3">@Entity</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 40. Какой набор аннотаций минимально необходим для корректной JPA-сущности?</h4>

```java
// Вариант A
@Entity
public class User {
    @Id
    private Long id;
    private String name;
    // конструктор без аргументов, геттеры/сеттеры
}

// Вариант B
@Table
public class User {
    @Column
    private Long id;
    private String name;
}
```

<div class="quiz-option" data-index="0">Вариант B — @Table и @Column обязательны</div>
<div class="quiz-option" data-index="1">Оба варианта эквивалентны</div>
<div class="quiz-option" data-index="2">Вариант A — минимально необходимы @Entity и @Id, плюс конструктор без аргументов</div>
<div class="quiz-option" data-index="3">Ни один — обязательна аннотация @Hibernate</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 41. Что делает аннотация @GeneratedValue(strategy = GenerationType.IDENTITY)?</h4>

<div class="quiz-option" data-index="0">Генерирует UUID для первичного ключа</div>
<div class="quiz-option" data-index="1">Указывает, что значение первичного ключа генерируется базой данных (AUTO_INCREMENT)</div>
<div class="quiz-option" data-index="2">Создаёт последовательность (sequence) в базе данных</div>
<div class="quiz-option" data-index="3">Копирует идентификатор из другой таблицы</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 42. Какое значение hbm2ddl.auto в hibernate.cfg.xml автоматически создаёт таблицы при запуске, удаляя существующие?</h4>

<div class="quiz-option" data-index="0">create</div>
<div class="quiz-option" data-index="1">update</div>
<div class="quiz-option" data-index="2">validate</div>
<div class="quiz-option" data-index="3">none</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 43. В чём различие между SessionFactory и Session в Hibernate?</h4>

<div class="quiz-option" data-index="0">SessionFactory — легковесный объект, Session — тяжёлый</div>
<div class="quiz-option" data-index="1">Оба создаются для каждой операции с базой</div>
<div class="quiz-option" data-index="2">Session создаётся один раз на всё приложение</div>
<div class="quiz-option" data-index="3">SessionFactory — тяжёлый (создаётся один раз), Session — легковесный (создаётся для каждой операции)</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 44. Какой метод Hibernate используется для сохранения новой сущности в базу данных?</h4>

<div class="quiz-option" data-index="0">session.save(entity) — только в старых версиях</div>
<div class="quiz-option" data-index="1">session.store(entity)</div>
<div class="quiz-option" data-index="2">session.persist(entity)</div>
<div class="quiz-option" data-index="3">session.insert(entity)</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 45. Какой метод Hibernate используется для получения сущности по первичному ключу?</h4>

<div class="quiz-option" data-index="0">session.find(User.class, id)</div>
<div class="quiz-option" data-index="1">session.get(User.class, id)</div>
<div class="quiz-option" data-index="2">session.load(id)</div>
<div class="quiz-option" data-index="3">session.select(User.class, id)</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 46. Чем HQL (Hibernate Query Language) отличается от SQL?</h4>

<div class="quiz-option" data-index="0">HQL оперирует именами классов и полей Java, а не именами таблиц и столбцов</div>
<div class="quiz-option" data-index="1">HQL быстрее SQL, так как не требует обращения к базе</div>
<div class="quiz-option" data-index="2">HQL не поддерживает условия WHERE</div>
<div class="quiz-option" data-index="3">HQL — это расширение SQL с поддержкой JavaScript</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 47. Какой HQL-запрос корректно выбирает всех пользователей с возрастом больше 18? <span class="jshell-hint">Попробуй в jshell!</span></h4>

```java
// Вариант A (SQL)
"SELECT * FROM users WHERE age > 18"

// Вариант B (HQL)
"FROM User WHERE age > 18"

// Вариант C (HQL)
"FROM User u WHERE u.age > :minAge"
```

<div class="quiz-option" data-index="0">Только вариант A — стандартный SQL</div>
<div class="quiz-option" data-index="1">Только вариант B</div>
<div class="quiz-option" data-index="2">Варианты B и C — HQL использует имя класса User, а не таблицы users</div>
<div class="quiz-option" data-index="3">Все три варианта одинаково корректны в HQL</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 48. Чем createQuery() отличается от createMutationQuery() в Hibernate 6?</h4>

<div class="quiz-option" data-index="0">Это одно и то же — синонимы</div>
<div class="quiz-option" data-index="1">createQuery() — для SELECT-запросов (чтение), createMutationQuery() — для UPDATE/DELETE (изменение данных)</div>
<div class="quiz-option" data-index="2">createMutationQuery() используется только для INSERT</div>
<div class="quiz-option" data-index="3">createQuery() устарел и не должен использоваться</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 49. Что такое Criteria API в Hibernate?</h4>

<div class="quiz-option" data-index="0">Язык запросов, аналогичный SQL</div>
<div class="quiz-option" data-index="1">Утилита для миграции баз данных</div>
<div class="quiz-option" data-index="2">Аннотация для валидации сущностей</div>
<div class="quiz-option" data-index="3">Типобезопасный API для построения запросов на Java-коде через CriteriaBuilder, CriteriaQuery и Root</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 50. Какая аннотация указывает связь «один ко многим» и на какой стороне обычно ставится mappedBy?</h4>

```java
@Entity
public class Department {
    @Id private Long id;
    @OneToMany(mappedBy = "department", cascade = CascadeType.ALL,
               fetch = FetchType.LAZY)
    private List<Employee> employees;
}

@Entity
public class Employee {
    @Id private Long id;
    @ManyToOne
    private Department department;
}
```

<div class="quiz-option" data-index="0">@OneToMany с mappedBy ставится на стороне «один» (Department), указывая поле-владельца на стороне «много»</div>
<div class="quiz-option" data-index="1">mappedBy ставится на стороне @ManyToOne (Employee)</div>
<div class="quiz-option" data-index="2">mappedBy не нужен — Hibernate определяет связь автоматически</div>
<div class="quiz-option" data-index="3">@OneToMany и @ManyToOne не могут использоваться вместе</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 6: LOMBOK (Вопросы 51–53) ===== -->

<div class="quiz-question" data-correct="0">
<h4>Вопрос 51. Какой набор аннотаций Lombok даёт геттеры, сеттеры и оба конструктора (пустой и полный) для JPA-сущности, но НЕ трогает equals()/hashCode() и toString()?</h4>

<div class="quiz-option" data-index="0">@Getter, @Setter, @NoArgsConstructor, @AllArgsConstructor</div>
<div class="quiz-option" data-index="1">@Data</div>
<div class="quiz-option" data-index="2">@Value</div>
<div class="quiz-option" data-index="3">@Builder</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 52. Почему @NoArgsConstructor обязателен именно для JPA-сущностей, а не просто удобен для сокращения кода?</h4>

<div class="quiz-option" data-index="0">Потому что Java требует конструктор без аргументов у любого класса</div>
<div class="quiz-option" data-index="1">Потому что аннотация @Entity не компилируется без конструктора без аргументов</div>
<div class="quiz-option" data-index="2">Потому что без него Spring Boot не найдёт класс при сканировании компонентов</div>
<div class="quiz-option" data-index="3">Потому что Hibernate создаёт объект сущности через рефлексию до заполнения полей, и ему нужен доступный конструктор без параметров</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 53. Что генерирует Lombok-аннотация @RequiredArgsConstructor, применённая к Spring-сервису с единственным final-полем StudentRepository repository?</h4>

<div class="quiz-option" data-index="0">Сеттер setRepository(...) для внедрения через Setter Injection</div>
<div class="quiz-option" data-index="1">Статический фабричный метод create(repository)</div>
<div class="quiz-option" data-index="2">Конструктор с одним параметром repository — эквивалент написанного вручную конструктора для Constructor Injection</div>
<div class="quiz-option" data-index="3">Поле помечается @Autowired, включается Field Injection</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 7: ТРАНЗАКЦИИ И УРОВНИ ИЗОЛЯЦИИ (Вопросы 54–58) ===== -->

<div class="quiz-question" data-correct="2">
<h4>Вопрос 54. Какое свойство ACID отвечает за то, что параллельные транзакции не мешают друг другу?</h4>

<div class="quiz-option" data-index="0">Atomicity (атомарность)</div>
<div class="quiz-option" data-index="1">Consistency (согласованность)</div>
<div class="quiz-option" data-index="2">Isolation (изолированность)</div>
<div class="quiz-option" data-index="3">Durability (долговечность)</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 55. Что называют грязным чтением (dirty read)?</h4>

<div class="quiz-option" data-index="0">Чтение данных, которые другая транзакция изменила, но ещё не зафиксировала</div>
<div class="quiz-option" data-index="1">Повторное чтение одной строки, вернувшее разные значения</div>
<div class="quiz-option" data-index="2">Появление новых строк в выборке при повторном запросе</div>
<div class="quiz-option" data-index="3">Чтение строки, которую другая транзакция уже удалила и зафиксировала</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 56. Какой минимальный уровень изоляции гарантирует, что повторное чтение одной и той же строки внутри транзакции вернёт то же значение?</h4>

<div class="quiz-option" data-index="0">READ UNCOMMITTED</div>
<div class="quiz-option" data-index="1">READ COMMITTED</div>
<div class="quiz-option" data-index="2">REPEATABLE READ</div>
<div class="quiz-option" data-index="3">SERIALIZABLE</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 57. Как в JDBC задать уровень изоляции для транзакции?</h4>

<div class="quiz-option" data-index="0">Передать уровень третьим параметром в DriverManager.getConnection()</div>
<div class="quiz-option" data-index="1">Вызвать conn.setTransactionIsolation(Connection.TRANSACTION_REPEATABLE_READ) до начала транзакции</div>
<div class="quiz-option" data-index="2">Вызвать statement.setIsolation("REPEATABLE READ") перед executeQuery()</div>
<div class="quiz-option" data-index="3">Указать уровень при создании ResultSet</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 58. Что делает аннотация @Version в сущности Hibernate?</h4>

<div class="quiz-option" data-index="0">Хранит номер версии схемы базы данных для миграций</div>
<div class="quiz-option" data-index="1">Включает пессимистичную блокировку: строка блокируется сразу при чтении</div>
<div class="quiz-option" data-index="2">Задаёт версию Hibernate, с которой совместима сущность</div>
<div class="quiz-option" data-index="3">Включает оптимистичную блокировку: Hibernate добавляет версию в условие UPDATE и замечает конфликт</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 8: STREAM API (Вопросы 59–63) ===== -->

<div class="quiz-question" data-correct="1">
<h4>Вопрос 59. Что напечатает этот код?</h4>

```java
List<String> cities = List.of("Москва", "Казань", "Сочи");
cities.stream()
      .peek(c -> System.out.println("peek: " + c))
      .filter(c -> c.length() > 4);
```

<div class="quiz-option" data-index="0">Три строки: peek: Москва, peek: Казань, peek: Сочи</div>
<div class="quiz-option" data-index="1">Ничего: без терминальной операции конвейер не запускается</div>
<div class="quiz-option" data-index="2">Только строку «peek: Москва» — конвейер останавливается на первом элементе</div>
<div class="quiz-option" data-index="3">Ошибку компиляции: результат конвейера не присвоен переменной</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 60. Какая из перечисленных операций Stream API является терминальной?</h4>

<div class="quiz-option" data-index="0">filter(predicate)</div>
<div class="quiz-option" data-index="1">map(function)</div>
<div class="quiz-option" data-index="2">sorted()</div>
<div class="quiz-option" data-index="3">collect(Collectors.toList())</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 61. Что окажется в списке result?</h4>

```java
List<List<String>> teams = List.of(
        List.of("Анна", "Борис"),
        List.of("Вера")
);
List<String> result = teams.stream()
        .flatMap(List::stream)
        .toList();
```

<div class="quiz-option" data-index="0">[[Анна, Борис], [Вера]] — вложенность сохранится</div>
<div class="quiz-option" data-index="1">[Анна, Вера] — по первому элементу каждого списка</div>
<div class="quiz-option" data-index="2">Пустой список: flatMap работает только с Optional</div>
<div class="quiz-option" data-index="3">[Анна, Борис, Вера]</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 62. Что окажется в переменной result?</h4>

```java
List<String> empty = List.of();
boolean result = empty.stream().allMatch(s -> s.length() > 100);
```

<div class="quiz-option" data-index="0">true</div>
<div class="quiz-option" data-index="1">false</div>
<div class="quiz-option" data-index="2">NoSuchElementException</div>
<div class="quiz-option" data-index="3">Optional.empty()</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 63. Что произойдёт при выполнении этого кода?</h4>

```java
Stream<String> stream = List.of("a", "b").stream();
stream.forEach(System.out::println);
stream.forEach(System.out::println);
```

<div class="quiz-option" data-index="0">Оба вызова напечатают по два элемента</div>
<div class="quiz-option" data-index="1">Второй вызов ничего не напечатает, но и ошибки не будет</div>
<div class="quiz-option" data-index="2">Второй вызов бросит IllegalStateException: поток уже использован</div>
<div class="quiz-option" data-index="3">Ошибка компиляции: поток нельзя присвоить переменной</div>
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
    'Вопрос 1': 'Системы сборки автоматизируют рутинные задачи: компиляцию исходного кода, управление внешними зависимостями, запуск тестов и упаковку приложения в JAR/WAR.',
    'Вопрос 2': 'В стандартной структуре Maven исходный код приложения хранится в src/main/java, а тесты — в src/test/java. Ресурсы (конфигурации, файлы) — в src/main/resources.',
    'Вопрос 3': 'Каталог target/ создаётся Maven автоматически и содержит скомпилированные классы, результаты тестов и упакованные артефакты (JAR/WAR). Он не хранится в системе контроля версий.',
    'Вопрос 4': 'GAV-координаты (groupId, artifactId, version) однозначно идентифицируют каждый артефакт в экосистеме Maven — как проект, так и любую его зависимость.',
    'Вопрос 5': 'Scope test означает, что зависимость доступна только при компиляции и выполнении тестов (src/test/java) и не включается в итоговый артефакт приложения.',
    'Вопрос 6': 'Жизненный цикл Maven последователен: каждая фаза включает все предыдущие. Команда mvn package выполнит validate → compile → test → package.',
    'Вопрос 7': 'Команда mvn install выполняет все фазы вплоть до install, которая копирует собранный артефакт в локальный репозиторий ~/.m2/repository для использования другими проектами.',
    'Вопрос 8': 'Maven сначала ищет зависимость в локальном кеше (~/.m2/repository), затем в Maven Central, и наконец в пользовательских репозиториях, указанных в pom.xml.',
    'Вопрос 9': 'Если scope не указан в pom.xml, используется compile — зависимость доступна на всех этапах: компиляция, тестирование, выполнение и включается в итоговый артефакт.',
    'Вопрос 10': 'Команда mvn dependency:tree выводит полное дерево зависимостей проекта, включая транзитивные зависимости, что помогает диагностировать конфликты версий.',
    'Вопрос 11': 'Gradle использует DSL на Groovy или Kotlin вместо XML, поддерживает инкрементальные сборки и кеширование, что делает его быстрее и гибче Maven.',
    'Вопрос 12': 'В Gradle-проекте на Kotlin DSL файл конфигурации называется build.gradle.kts (.kts означает Kotlin Script). Для Groovy DSL используется build.gradle.',
    'Вопрос 13': 'Gradle Wrapper — скрипты gradlew (Unix) и gradlew.bat (Windows), которые автоматически загружают и используют указанную версию Gradle без ручной установки.',
    'Вопрос 14': 'Конфигурация testImplementation в Gradle аналогична scope test в Maven — зависимость доступна только для тестового кода и не включается в production-сборку.',
    'Вопрос 15': 'Команда ./gradlew clean build сначала удаляет каталог build/ (clean), а затем выполняет полную сборку заново, гарантируя отсутствие устаревших артефактов.',
    'Вопрос 16': 'Конфигурация implementation подключает зависимость для основного кода (src/main), а testImplementation — только для тестов (src/test).',
    'Вопрос 17': 'Архитектура JDBC: Java-приложение обращается к JDBC API, который через DriverManager загружает нужный JDBC Driver, а драйвер взаимодействует с конкретной базой данных.',
    'Вопрос 18': 'DriverManager.getConnection(url, user, password) — статический метод, который подбирает подходящий JDBC-драйвер по URL и возвращает объект Connection.',
    'Вопрос 19': 'URL для H2 in-memory базы имеет формат jdbc:h2:mem:testdb, где jdbc:h2: — префикс драйвера, mem: — режим в памяти, testdb — имя базы.',
    'Вопрос 20': 'PreparedStatement поддерживает параметризованные запросы с заполнителями (?), что предотвращает SQL-инъекции и позволяет СУБД кешировать план выполнения.',
    'Вопрос 21': 'SQL-инъекция — это атака, при которой злоумышленник внедряет вредоносный SQL через конкатенацию строк. PreparedStatement экранирует параметры и делает инъекцию невозможной.',
    'Вопрос 22': 'Вариант B использует параметризованный запрос с ? и методы setString/setInt, что безопасно. Вариант A с конкатенацией уязвим для SQL-инъекций.',
    'Вопрос 23': 'Метод next() перемещает курсор ResultSet на следующую строку и возвращает true, если строка существует, или false при достижении конца результата.',
    'Вопрос 24': 'Стандартный паттерн: while (rs.next()) { ... } — цикл вызывает next() для перехода к каждой строке, а внутри цикла извлекаются данные через getString/getInt.',
    'Вопрос 25': 'Метод executeQuery() выполняет SELECT-запрос и возвращает ResultSet с результатами. Для INSERT/UPDATE/DELETE используется executeUpdate().',
    'Вопрос 26': 'Метод executeUpdate() выполняет DML-операции (INSERT, UPDATE, DELETE) и возвращает int — количество затронутых строк.',
    'Вопрос 27': 'setAutoCommit(false) отключает автоматическую фиксацию каждого SQL-запроса. Изменения накапливаются в транзакции и применяются только при явном вызове commit().',
    'Вопрос 28': 'rollback() отменяет все изменения, сделанные в рамках текущей транзакции с момента последнего commit() или начала соединения. Данные в базе не изменяются.',
    'Вопрос 29': 'CallableStatement предназначен для вызова хранимых процедур и функций базы данных. Statement — для простых запросов, PreparedStatement — для параметризованных.',
    'Вопрос 30': 'В JDBC индексация столбцов ResultSet начинается с 1, а не с 0 (как в массивах Java). Обращение по имени столбца (getString("name")) более читаемо и устойчиво к изменениям схемы.',
    'Вопрос 31': 'URL для PostgreSQL имеет формат jdbc:postgresql://host:port/database. Префикс jdbc: обязателен, далее указывается тип СУБД, хост, порт и имя базы.',
    'Вопрос 32': 'UPDATE-запрос изменяет существующие данные в таблице. PreparedStatement с executeUpdate() выполняет изменение и возвращает количество обновлённых строк.',
    'Вопрос 33': 'DAO (Data Access Object) — паттерн проектирования, инкапсулирующий всю логику работы с хранилищем данных в отдельном слое, изолируя бизнес-логику от деталей доступа к БД.',
    'Вопрос 34': 'DAO-интерфейс обычно содержит CRUD-методы: создание (save/create), чтение по ID (findById), получение всех (findAll), обновление (update) и удаление (delete).',
    'Вопрос 35': 'DAO обеспечивает чистое разделение ответственности: бизнес-логика не зависит от способа хранения данных. Это упрощает тестирование (mock-объекты) и позволяет заменить реализацию.',
    'Вопрос 36': 'DAO описывается как интерфейс с CRUD-методами, а конкретная реализация (JDBC, Hibernate и др.) создаётся отдельно. Это позволяет легко подменять реализации.',
    'Вопрос 37': 'ORM (Object-Relational Mapping) автоматически отображает Java-классы на таблицы, поля — на столбцы, объекты — на строки, избавляя от ручного написания SQL.',
    'Вопрос 38': 'JPA (Jakarta Persistence API) — это спецификация (набор интерфейсов и аннотаций). Hibernate — наиболее популярная реализация этой спецификации.',
    'Вопрос 39': 'Аннотация @Entity помечает Java-класс как сущность JPA, которая будет отображена на таблицу. @Table задаёт имя таблицы (необязательно), @Id — первичный ключ.',
    'Вопрос 40': 'Минимальные требования к JPA-сущности: аннотация @Entity на классе, аннотация @Id на поле первичного ключа и наличие конструктора без аргументов.',
    'Вопрос 41': 'GenerationType.IDENTITY означает, что база данных сама генерирует значение первичного ключа (обычно через AUTO_INCREMENT в MySQL или SERIAL в PostgreSQL).',
    'Вопрос 42': 'Значение create удаляет существующие таблицы и создаёт их заново при каждом запуске. update — дополняет схему без удаления, validate — только проверяет, none — ничего не делает.',
    'Вопрос 43': 'SessionFactory — тяжёлый потокобезопасный объект, создаётся один раз при старте приложения. Session — легковесный, создаётся для каждой единицы работы и не потокобезопасен.',
    'Вопрос 44': 'Метод session.persist(entity) сохраняет новую сущность в базу данных. Это стандартный JPA-метод, рекомендуемый вместо устаревшего session.save().',
    'Вопрос 45': 'Метод session.get(Class, id) загружает сущность по первичному ключу, выполняя SELECT-запрос. Возвращает null, если сущность не найдена.',
    'Вопрос 46': 'HQL работает с Java-классами и их полями (FROM User WHERE age > 18), а не с таблицами и столбцами SQL (FROM users WHERE age > 18). Hibernate транслирует HQL в SQL.',
    'Вопрос 47': 'В HQL используется имя Java-класса (User), а не имя таблицы (users). Вариант C с именованным параметром :minAge — предпочтительный способ параметризации.',
    'Вопрос 48': 'В Hibernate 6 createQuery() предназначен для SELECT-запросов и возвращает типизированный результат. createMutationQuery() — для UPDATE и DELETE, возвращает количество изменённых строк.',
    'Вопрос 49': 'Criteria API позволяет строить запросы программно через Java-код (CriteriaBuilder, CriteriaQuery, Root), обеспечивая типобезопасность и обнаружение ошибок на этапе компиляции.',
    'Вопрос 50': 'mappedBy на стороне @OneToMany указывает, что связью владеет другая сторона (Employee.department). Это предотвращает дублирование внешнего ключа. FetchType.LAZY загружает коллекцию по требованию.',
    'Вопрос 51': '@Data генерирует сразу всё, включая equals()/hashCode() и toString() по всем полям — а это опасно для сущности со связями (лишние SQL-запросы, LazyInitializationException). Перечисленные по отдельности @Getter, @Setter, @NoArgsConstructor, @AllArgsConstructor дают ровно геттеры/сеттеры/конструкторы и ничего лишнего.',
    'Вопрос 52': 'Hibernate инстанцирует сущность рефлексией (обычно через Unsafe или конструктор без аргументов), а уже потом заполняет поля через рефлексию же — конструктор с параметрами тут не годится, так как значения полей ещё не считаны из ResultSet.',
    'Вопрос 53': '@RequiredArgsConstructor генерирует конструктор по всем final-полям класса. Для Spring результат неотличим от конструктора, написанного вручную: контейнер видит единственный конструктор и внедряет через него зависимости — Constructor Injection, а не Setter или Field Injection.',
    'Вопрос 54': 'Isolation — та самая буква, степень которой регулируется уровнем изоляции. Atomicity отвечает за принцип «всё или ничего», Consistency — за соблюдение ограничений базы, Durability — за сохранность данных после commit.',
    'Вопрос 55': 'Грязное чтение — это чтение чужих незафиксированных изменений: если та транзакция откатится, вы приняли решение на основе данных, которых никогда не существовало. Второй и третий варианты описывают неповторяющееся и фантомное чтение.',
    'Вопрос 56': 'Неповторяющееся чтение запрещено начиная с REPEATABLE READ. SERIALIZABLE тоже его запрещает, но он строже, чем требуется, и обходится дороже; READ COMMITTED защищает только от грязного чтения.',
    'Вопрос 57': 'Уровень изоляции — свойство соединения: его задают методом setTransactionIsolation с константой из интерфейса Connection, причём до setAutoCommit(false) и до первого запроса. Поддержку конкретного уровня стоит проверять через DatabaseMetaData.',
    'Вопрос 58': 'С полем @Version каждый UPDATE выполняется с условием WHERE id = ? AND version = ?. Если параллельная транзакция уже изменила строку, обновится 0 строк и коммит завершится исключением (StaleObjectStateException или OptimisticLockException) — данные нужно перечитать и повторить операцию.',
    'Вопрос 59': 'Промежуточные операции ленивы: peek и filter лишь достраивают описание конвейера. Пока не вызвана терминальная операция (toList(), forEach(), count() и т. п.), ни один элемент через конвейер не проходит.',
    'Вопрос 60': 'Терминальная операция возвращает не Stream, а результат (или ничего) и запускает вычисление всего конвейера. filter, map и sorted возвращают новый Stream, то есть являются промежуточными.',
    'Вопрос 61': 'flatMap превращает каждый элемент в поток и склеивает эти потоки в один — вложенные списки «расплющиваются» в плоский. Обычный map в этой ситуации вернул бы Stream<List<String>>, а не Stream<String>.',
    'Вопрос 62': 'На пустом потоке allMatch и noneMatch возвращают true, а anyMatch — false: утверждение обо всех элементах пустого множества опровергнуть нечем. Поэтому проверку allMatch почти всегда дополняют проверкой, что данные вообще есть.',
    'Вопрос 63': 'Поток одноразовый: после терминальной операции он закрыт, и повторное обращение бросает IllegalStateException со словами «stream has already been operated upon or closed». Переиспользовать нужно источник или Supplier<Stream<T>>.'
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
