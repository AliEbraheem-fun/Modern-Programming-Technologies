# Лекция 7: Spring Framework и Spring Boot

## Введение

Добро пожаловать на седьмую лекцию курса «Современные технологии программирования». На прошлой лекции мы научились автоматизировать сборку проекта (Maven, Gradle) и работать с базами данных (JDBC, Hibernate). Но если попытаться собрать всё это в реальное веб-приложение — с контроллерами, сервисами, безопасностью, REST API, формами входа — окажется, что вручную «склеивать» все компоненты крайне неудобно. Каждый раз приходится открывать соединения, заботиться о транзакциях, настраивать сервлеты, разруливать зависимости между классами.

Сегодня мы разберём фреймворк **Spring** и его «упрощённую сборку» — **Spring Boot**. Это де-факто стандарт корпоративной Java-разработки. Spring берёт на себя всю инфраструктуру (создание объектов, внедрение зависимостей, транзакции, безопасность, веб-сервер), а вы пишете только бизнес-логику.

Мы пройдём путь от базовых принципов (Inversion of Control и Dependency Injection) до полноценного веб-приложения с REST API, Thymeleaf-шаблонами, Spring Security и JWT-аутентификацией.

---

## Часть 1: Inversion of Control и Dependency Injection

### 1.1 Проблема: ручное управление зависимостями

Представьте, что вы пишете класс `StudentService`, который должен сохранять студентов в базу. Ему нужен `StudentRepository`. А репозиторию — `DataSource`. А `DataSource` нужно настроить с URL, логином, паролем. В классическом подходе вы бы написали так:

```java
public class StudentService {
    private StudentRepository repository;

    public StudentService() {
        // Сервис сам создаёт свои зависимости
        DataSource ds = new HikariDataSource(/* конфиг */);
        this.repository = new StudentRepository(ds);
    }
}
```

Проблемы такого подхода:
- **Жёсткая связность** — `StudentService` намертво привязан к конкретной реализации `StudentRepository`.
- **Тестируемость на нуле** — нельзя подменить репозиторий заглушкой (mock) в юнит-тесте.
- **Дублирование** — в каждом сервисе вы создаёте `DataSource` заново.
- **Жизненный цикл вручную** — закрывать соединения и пулы вы тоже обязаны сами.

### 1.2 Inversion of Control (IoC)

**Inversion of Control (Инверсия управления)** — это принцип проектирования, при котором управление жизненным циклом объектов, их созданием и взаимодействием передаётся внешнему фреймворку или контейнеру, а не выполняется вручную в коде приложения.

Голливудский принцип: **«Не вызывай нас — мы сами тебя позовём»**. Вместо того чтобы ваш код «звал» фреймворк (`new DataSource(...)`, `new Repository(...)`), фреймворк сам инстанцирует ваши классы и подсовывает им нужные зависимости.

### 1.3 Dependency Injection (DI)

**Dependency Injection (Внедрение зависимостей)** — это конкретная техника реализации IoC, при которой объект не создаёт сам свои зависимости, а получает их извне (контейнером или фабрикой).

Существует три способа внедрения:

#### 1. Через конструктор (Constructor Injection) — рекомендуется

```java
@Service
public class StudentService {
    private final StudentRepository repository;

    // Spring сам создаст StudentRepository и передаст его сюда
    public StudentService(StudentRepository repository) {
        this.repository = repository;
    }
}
```

Преимущества: поле может быть `final` (неизменяемое), при отсутствии зависимости объект просто не создастся (ошибка на старте, а не в рантайме).

#### 2. Через сеттер (Setter Injection)

```java
@Service
public class StudentService {
    private StudentRepository repository;

    @Autowired
    public void setRepository(StudentRepository repository) {
        this.repository = repository;
    }
}
```

#### 3. Через поле (Field Injection) — не рекомендуется

```java
@Service
public class StudentService {
    @Autowired
    private StudentRepository repository;  // Скрытая зависимость, тяжело тестировать
}
```

Это важный момент: в современном Spring предпочтительнее **конструктор**. Поле через `@Autowired` усложняет тестирование (нельзя обойтись без рефлексии или Spring-контекста) и скрывает зависимости класса.

---

## Часть 2: Spring Framework и Spring Boot

### 2.1 Spring Framework

**Spring Framework** — универсальный фреймворк с открытым исходным кодом для платформы Java, предназначенный для упрощения разработки корпоративных приложений. Он предоставляет инфраструктурную поддержку: управление объектами, транзакциями, конфигурацией и многим другим. Это освобождает разработчика от ручного контроля этих процессов.

Основой Spring являются принципы **IoC** и **DI**. Они позволяют ослабить связность между компонентами, повышая модульность и тестируемость.

Spring работает с обычными Java-объектами (POJO) и не требует наследования от каких-либо специальных классов или интерфейсов — это делает его ненавязчивым.

### 2.2 Spring Boot

**Spring Boot** — это расширение Spring Framework, упрощающее разработку и запуск самодостаточных (standalone) и production-ready приложений на Java. Он позволяет создавать Spring-приложения **без XML-конфигурации**, с минимальным количеством шаблонного кода.

Основная цель — сократить время настройки и дать разработчику сосредоточиться на бизнес-логике.

**Особенности Spring Boot:**
- **Автоконфигурация** — Spring сам подбирает разумные настройки на основе зависимостей в classpath.
- **Встроенные серверы** (Tomcat, Jetty, Undertow) — приложение запускается через `main()`, отдельный сервер не нужен.
- **Starter-модули** — одна зависимость подключает целый набор связанных библиотек с согласованными версиями.

**Минимальное Spring Boot приложение:**

```java
@SpringBootApplication
public class StudentApplication {
    public static void main(String[] args) {
        SpringApplication.run(StudentApplication.class, args);
    }
}
```

Аннотация `@SpringBootApplication` — это «всё в одном»: `@Configuration` + `@EnableAutoConfiguration` + `@ComponentScan`.

### 2.3 Spring Initializr

**Spring Initializr** — веб-сервис от команды Spring для генерации шаблона проекта Spring Boot. Позволяет выбрать зависимости, версию Java, систему сборки и сразу скачать готовый ZIP-архив.

Адрес: [https://start.spring.io](https://start.spring.io)

В нём вы указываете:
- Систему сборки (Maven / Gradle)
- Язык (Java / Kotlin / Groovy)
- Версию Spring Boot
- Координаты проекта (Group, Artifact)
- Версию Java
- Зависимости (Web, JPA, Security, Thymeleaf и т.д.)

---

## Часть 3: Spring IoC Container и Bean

### 3.1 Spring IoC Container

**Spring IoC Container** — это ядро фреймворка Spring, реализация принципа IoC. Контейнер:
- создаёт, настраивает и соединяет объекты в соответствии с метаданными конфигурации;
- внедряет зависимости (DI) — автоматически передаёт объекты-зависимости в конструкторы, методы или поля других компонентов;
- управляет жизненным циклом бинов, включая инициализацию и уничтожение;
- работает с конфигурацией, заданной через XML, аннотации или Java-классы (`@Configuration` / `@Bean`).

Конфигурация контейнера задаётся в виде `BeanDefinition` — структуры, описывающей класс, зависимости, scope, методы init/destroy и способ создания бина.

**Иерархия контейнеров:**

Самая базовая форма Spring IoC контейнера — это интерфейс `BeanFactory`. В подавляющем большинстве случаев сейчас используют **`ApplicationContext`** (а не `BeanFactory` напрямую) — он добавляет поддержку интернационализации, событий, ресурсов и интеграцию со Spring AOP.

Наиболее частые реализации `ApplicationContext`:
- `AnnotationConfigApplicationContext` — конфигурация через аннотации
- `ClassPathXmlApplicationContext` — XML-конфигурация из classpath
- `FileSystemXmlApplicationContext` — XML-конфигурация из файловой системы
- `AnnotationConfigWebApplicationContext` — для веб-приложений с аннотациями
- `XmlWebApplicationContext` — для веб-приложений с XML

### 3.2 Spring Bean

**Spring Bean** — это объект, который создаётся, настраивается и управляется контейнером Spring IoC. Именно контейнер отвечает за его жизненный цикл, внедрение зависимостей и scope.

Такие объекты определяются через конфигурацию (XML, Java-конфигурация, аннотации) и затем связываются между собой автоматически.

#### Жизненный цикл Spring Bean

1. Контейнер парсит конфигурацию и создаёт `BeanDefinition`.
2. При необходимости (scope singleton) создаёт экземпляр бина.
3. Выполняет внедрение зависимостей (в конструктор, сеттеры или поля).
4. Вызывает методы инициализации (`@PostConstruct`, `init-method`).
5. Бин готов к использованию.
6. При уничтожении контейнера: вызов `destroy` / `@PreDestroy`.

#### Scope бинов

| Scope | Описание |
|-------|----------|
| `singleton` (по умолчанию) | Один экземпляр на весь контейнер |
| `prototype` | Новый экземпляр на каждый запрос бина |
| `request` | Один экземпляр на HTTP-запрос (только web) |
| `session` | Один экземпляр на HTTP-сессию (только web) |
| `application` | Один экземпляр на ServletContext (только web) |

#### Как определяется Spring Bean

```java
// 1. Через стереотипные аннотации — класс автоматически становится бином
@Component  // Общая аннотация
public class MyComponent { }

@Service    // Уровень бизнес-логики
public class StudentService { }

@Repository // Уровень доступа к данным
public class StudentRepository { }

@Controller // Уровень контроллеров MVC
public class StudentController { }
```

Все эти аннотации — это специализации `@Component`. Они равнозначны с точки зрения контейнера, но несут смысловую нагрузку для разработчика и иногда дают дополнительное поведение (например, `@Repository` перехватывает исключения и преобразует их в `DataAccessException`).

```java
// 2. Через @Bean в классе с @Configuration — ручное создание объекта
@Configuration
public class AppConfig {
    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}
```

```xml
<!-- 3. Через XML — традиционное описание (легаси) -->
<bean id="studentService" class="com.example.StudentService"/>
```

---

## Часть 4: Spring Boot Starter-модули

В Spring Boot управление зависимостями устроено через **starter**-модули. Каждый starter подключает группу связанных библиотек с согласованными версиями.

| Стартер | Назначение |
|---------|------------|
| `spring-boot-starter` | Базовый: логирование и конфигурация |
| `spring-boot-starter-web` | Веб-приложения (Spring MVC + встроенный Tomcat) |
| `spring-boot-starter-data-jpa` | Работа с БД через JPA и Hibernate |
| `spring-boot-starter-security` | Безопасность: аутентификация и авторизация |
| `spring-boot-starter-test` | JUnit, Mockito, Spring Test |
| `spring-boot-starter-thymeleaf` | HTML-шаблоны с Thymeleaf |
| `spring-boot-starter-validation` | Валидация через Hibernate Validator |
| `spring-boot-starter-mail` | Отправка email через SMTP |
| `spring-boot-starter-aop` | Аспектно-ориентированное программирование |

Пример `pom.xml` для веб-приложения с БД и безопасностью:

```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>3.5.4</version>
</parent>

<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-jpa</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-security</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-thymeleaf</artifactId>
    </dependency>
    <dependency>
        <groupId>com.h2database</groupId>
        <artifactId>h2</artifactId>
        <scope>runtime</scope>
    </dependency>
</dependencies>
```

Обратите внимание: версии зависимостей не указываются — их задаёт `spring-boot-starter-parent`, что предотвращает конфликты несовместимых версий.

---

## Часть 5: AOP (Aspect-Oriented Programming)

**AOP (Aspect-Oriented Programming, аспектно-ориентированное программирование)** — парадигма, отделяющая сквозную функциональность (логирование, транзакции, безопасность) от бизнес-логики, выделяя её в отдельные модули — **аспекты**. Это повышает модульность и упрощает поддержку приложения.

**Ключевые понятия:**

- **Aspect** — класс, содержащий логику аспектов (advice) и определения точек среза (pointcut).
- **JoinPoint** — конкретная точка выполнения программы, где можно «врезаться» с дополнительной логикой (например, вызов метода).
- **Pointcut** — выражение, определяющее, какие JoinPoint'ы будут перехвачены.
- **Advice** — код, исполняемый в точке JoinPoint.

```java
@Aspect
@Component
public class LoggingAspect {

    // Pointcut: все методы в пакете service
    @Before("execution(* com.example.service.*.*(..))")
    public void logBefore(JoinPoint joinPoint) {
        System.out.println("Вызов метода: " + joinPoint.getSignature().getName());
    }

    @AfterReturning(pointcut = "execution(* com.example.service.*.*(..))", returning = "result")
    public void logAfter(JoinPoint joinPoint, Object result) {
        System.out.println("Метод вернул: " + result);
    }
}
```

Реализации AOP в Java: **Spring AOP** (на прокси-объектах, ограничения по сравнению с AspectJ) и **AspectJ** (полноценное AOP с компиляцией байткода).

В Spring многие фундаментальные возможности построены на AOP «под капотом»: `@Transactional`, `@PreAuthorize`, `@Cacheable`.

---

## Часть 6: Spring MVC

### 6.1 Паттерн MVC

**Spring MVC** — это реализация паттерна Model–View–Controller, который разделяет веб-приложение на три логических компонента:

- **Model (Модель)** — отвечает за бизнес-данные и логику. Обычно представлена Java-классами (POJO, Entity), которые обрабатываются в сервисах и репозиториях.
- **View (Представление)** — отвечает за отображение данных пользователю (HTML, JSP, Thymeleaf, JSON/XML). Генерируется на основе модели, которую контроллер передаёт в представление.
- **Controller (Контроллер)** — обрабатывает входящие HTTP-запросы, вызывает соответствующие сервисы/репозитории и передаёт результат в модель и представление.

```
HTTP запрос
    ↓
Controller (@Controller / @RestController)
    ↓
Service (@Service)
    ↓
Repository (@Repository)
    ↓
База данных
```

### 6.2 @Controller vs @RestController

```java
@Controller
public class StudentWebController {

    @GetMapping("/students")
    public String list(Model model) {
        model.addAttribute("students", studentService.findAll());
        return "students";  // Имя шаблона: src/main/resources/templates/students.html
    }
}
```

- `@Controller` предназначена для традиционных приложений Spring MVC, где целью является возврат **представления** (HTML-страницы, Thymeleaf-шаблона).
- Если метод в `@Controller` возвращает `String`, механизм `ViewResolver` интерпретирует строку как имя представления.
- Чтобы вернуть данные напрямую (JSON), нужно явно добавить `@ResponseBody`.

```java
@RestController
@RequestMapping("/api/students")
public class StudentRestController {

    @GetMapping
    public List<Student> getAll() {
        return studentService.findAll();  // Сериализуется в JSON
    }
}
```

- `@RestController` — это `@Controller` + `@ResponseBody` на всех методах.
- Применяется для создания REST API: возвращаемые значения автоматически сериализуются в JSON/XML и записываются в тело HTTP-ответа.

### 6.3 Mapping — обработка запросов

**`@RequestMapping`** — универсальная аннотация для обработки HTTP-запросов. Применяется к классам и методам.

```java
@RequestMapping(value = "/api/students",
                method = RequestMethod.GET,
                params = "active=true",
                headers = "X-API-Version=1",
                consumes = "application/json",
                produces = "application/json")
```

**Сокращённые аннотации** — специализированные формы `@RequestMapping`, применимы только к методам:

```java
@GetMapping("/students")          // GET
@PostMapping("/students")         // POST
@PutMapping("/students/{id}")     // PUT
@DeleteMapping("/students/{id}")  // DELETE
@PatchMapping("/students/{id}")   // PATCH
```

**URL-шаблоны:**

| Шаблон | Описание | Пример |
|--------|----------|--------|
| `*` | Один сегмент | `/img/*.jpg` |
| `**` | Любые вложенные пути | `/admin/**` |
| `?` | Один символ | `/file?.txt` |

**`@PathVariable`** — извлекает переменные из части пути:

```java
@GetMapping("/students/{id}")
public Student getById(@PathVariable long id) {
    return service.findById(id);
}
```

**`@RequestParam`** — извлекает параметры запроса (после `?` в URL):

```java
// URL: /students?genre=Drama&minYear=2000
@GetMapping("/students")
public List<Student> search(
        @RequestParam String genre,
        @RequestParam(defaultValue = "0") int minYear) {
    // ...
}
```

**`@RequestBody`** — десериализует тело запроса (обычно JSON) в Java-объект:

```java
@PostMapping("/students")
public Student create(@RequestBody Student student) {
    return service.save(student);
}
```

### 6.4 Пример: Полный CRUD REST-контроллер

```java
@RestController
@RequestMapping("/api/students")
public class StudentRestController {

    @Autowired
    private StudentService studentService;

    @GetMapping
    public List<Student> getAllStudents() {
        return studentService.findAll();
    }

    @GetMapping("/{id}")
    public ResponseEntity<Student> getStudentById(@PathVariable long id) {
        Student student = studentService.findById(id);
        return student != null
                ? ResponseEntity.ok(student)
                : ResponseEntity.notFound().build();
    }

    @PostMapping
    public ResponseEntity<Student> addStudent(@RequestBody Student student) {
        Student saved = studentService.save(student);
        return ResponseEntity.status(HttpStatus.CREATED).body(saved);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Student> updateStudent(@PathVariable long id,
                                                  @RequestBody Student student) {
        if (studentService.findById(id) == null) {
            return ResponseEntity.notFound().build();
        }
        student.setId(id);
        return ResponseEntity.ok(studentService.save(student));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteStudent(@PathVariable long id) {
        if (studentService.findById(id) == null) {
            return ResponseEntity.notFound().build();
        }
        studentService.deleteById(id);
        return ResponseEntity.noContent().build();
    }
}
```

---

## Часть 7: Слои @Repository и @Service

### 7.1 @Repository

`@Repository` помечает класс или интерфейс как компонент **DAO (Data Access Object)**. Дополнительно:
- Spring перехватывает исключения, специфичные для конкретной СУБД, и преобразует их в `DataAccessException` — единую иерархию исключений, не зависящую от провайдера.
- Является специализацией `@Component`.

### 7.2 @Service

`@Service` — аннотация уровня бизнес-логики. Компонент, реализующий операции, объединяющие логику и взаимодействие с репозиториями.

```java
public interface StudentService {
    List<Student> findAll();
    Student save(Student student);
    Student findById(Long id);
    void deleteById(Long id);
}

@Service
public class StudentServiceImpl implements StudentService {

    private final StudentRepository studentRepository;

    @Autowired
    public StudentServiceImpl(StudentRepository studentRepository) {
        this.studentRepository = studentRepository;
    }

    @Override
    public List<Student> findAll() {
        return studentRepository.findAll();
    }

    @Override
    public Student save(Student student) {
        return studentRepository.save(student);
    }

    @Override
    public Student findById(Long id) {
        return studentRepository.findById(id).orElse(null);
    }

    @Override
    public void deleteById(Long id) {
        studentRepository.deleteById(id);
    }
}
```

### 7.3 CrudRepository и JpaRepository

Spring Data JPA устраняет даже необходимость писать реализации DAO. Достаточно объявить интерфейс — реализацию сгенерирует Spring.

**`CrudRepository<T, ID>`** — базовый интерфейс для CRUD-операций над сущностями:

```java
save(entity)
findById(id)         // Optional<T>
findAll()
deleteById(id)
existsById(id)
count()
```

**`JpaRepository<T, ID>`** расширяет `CrudRepository` и `PagingAndSortingRepository`. Дополнительно включает:

```java
findAll(Sort sort)            // Сортировка
findAll(Pageable pageable)    // Постраничный вывод
saveAll(entities)             // Пакетное сохранение
deleteInBatch(entities)       // Пакетное удаление
flush()                       // Принудительная синхронизация
```

**Пример:**

```java
public interface StudentRepository extends JpaRepository<Student, Long> {
    // Spring Data сам сгенерирует реализацию по имени метода
    List<Student> findByNameContainingIgnoreCase(String name);
    List<Student> findBySurname(String surname);
}
```

Магия Spring Data: имя метода `findByNameContainingIgnoreCase` парсится фреймворком и превращается в SQL:
```sql
SELECT * FROM students WHERE LOWER(name) LIKE LOWER('%...%')
```

---

## Часть 8: Шаблонизатор Thymeleaf

**Шаблонизатор** — программное обеспечение, которое позволяет создавать документы, используя шаблоны и данные. Основная идея — отделить структуру документа (шаблон) от данных, которые в него вставляются.

Spring Boot делает настройку шаблонизатора простой: достаточно подключить нужный стартер (`spring-boot-starter-thymeleaf`, `spring-boot-starter-freemarker`, `spring-boot-starter-mustache`), положить шаблоны в `src/main/resources/templates` — и всё заработает.

**Thymeleaf** — современный серверный шаблонизатор для Java, поддерживающий HTML, XML, JS, CSS и plain text. Главная особенность — **Natural Templates**: шаблон остаётся валидным HTML и может быть понятен дизайнерам без запуска приложения.

### 8.1 Передача данных в шаблон

Контроллер передаёт данные через объект `org.springframework.ui.Model`:

```java
@GetMapping("/students")
public String list(Model model) {
    model.addAttribute("students", studentService.findAll());
    return "students";  // имя шаблона students.html в /templates
}
```

### 8.2 Основные конструкции Thymeleaf

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<body>

<!-- Вывод значения -->
<h1 th:text="${title}">Заголовок</h1>

<!-- Условный вывод -->
<div th:if="${message}" th:text="${message}"></div>

<!-- Цикл по коллекции -->
<table>
    <tr th:each="student : ${students}">
        <td th:text="${student.name}">Имя</td>
        <td th:text="${student.surname}">Фамилия</td>
    </tr>
</table>

<!-- Формирование URL -->
<a th:href="@{/students/edit/{id}(id=${student.id})}">Редактировать</a>

<!-- Привязка к форме (Form Binding) -->
<form th:action="@{/students/save}" th:object="${student}" method="post">
    <input type="hidden" th:field="*{id}"/>
    <input type="text" th:field="*{name}" placeholder="Name"/>
    <button type="submit">Сохранить</button>
</form>

</body>
</html>
```

### 8.3 Интеграция со Spring Security

С подключением модуля `thymeleaf-extras-springsecurity6` в шаблонах доступны атрибуты `sec:authorize`:

```html
<html xmlns:th="http://www.thymeleaf.org"
      xmlns:sec="http://www.thymeleaf.org/extras/spring-security">

<!-- Кнопка видна только администраторам -->
<a class="btn btn-danger"
   th:href="@{/students/delete/{id}(id=${student.id})}"
   sec:authorize="hasAnyRole('ADMIN', 'SUPER_ADMIN')">
    Delete
</a>
```

---

## Часть 9: Spring Security

**Spring Security** — мощный фреймворк для реализации **Authentication (аутентификации)** и **Authorization (авторизации)** в приложениях на Java/Spring. Обеспечивает также защиту от уязвимостей (CSRF, session fixation, clickjacking и др.) из коробки.

Работает через цепочку фильтров **`SecurityFilterChain`** — каждый входящий запрос проходит по фильтрам, которые отвечают за аутентификацию, авторизацию, защиту от CSRF и т.д.

### 9.1 Базовая конфигурация

```java
@Configuration
public class SecurityConfig {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/login", "/register", "/api/auth/**").permitAll()
                .requestMatchers("/api/students").hasAnyRole("USER", "ADMIN", "SUPER_ADMIN")
                .requestMatchers("/api/students/**").hasAnyRole("ADMIN", "SUPER_ADMIN")
                .anyRequest().authenticated()
            )
            .formLogin(form -> form
                .loginPage("/login")
                .defaultSuccessUrl("/students", true)
                .permitAll()
            )
            .logout(logout -> logout
                .logoutUrl("/logout")
                .logoutSuccessUrl("/login?logout")
                .permitAll()
            )
            .csrf(AbstractHttpConfigurer::disable);

        return http.build();
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}
```

### 9.2 Пользователи и роли

Spring Security ищет пользователей через `UserDetailsService`. Кастомная реализация:

```java
@Service
public class CustomUserDetailsService implements UserDetailsService {

    @Autowired
    private UserRepository userRepository;

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        User u = userRepository.findByEmail(username)
            .orElseThrow(() -> new UsernameNotFoundException("User not found"));

        return org.springframework.security.core.userdetails.User
            .withUsername(u.getEmail())
            .password(u.getPassword())
            .authorities(new SimpleGrantedAuthority("ROLE_" + u.getRole().name()))
            .build();
    }
}
```

### 9.3 Аннотации на методах

Защита на уровне методов с помощью `@PreAuthorize`:

```java
@RestController
@RequestMapping("/api/students")
public class StudentRestController {

    @GetMapping
    @PreAuthorize("hasRole('ADMIN')")
    public List<Student> getAll() {
        return service.findAll();
    }

    @DeleteMapping("/{id}")
    @PreAuthorize("hasAnyRole('ADMIN', 'SUPER_ADMIN')")
    public ResponseEntity<Void> delete(@PathVariable long id) {
        service.deleteById(id);
        return ResponseEntity.noContent().build();
    }
}
```

### 9.4 JWT для REST API

Для REST API session-based аутентификация неудобна. Стандартное решение — **JWT (JSON Web Token)**: компактный самодостаточный токен, содержащий имя пользователя и подпись.

**Утилита для работы с JWT:**

```java
@Component
public class JwtUtil {

    private final String SECRET = "long-random-secret-key-here";

    public String generateToken(UserDetails userDetails) {
        return Jwts.builder()
            .setSubject(userDetails.getUsername())
            .setIssuedAt(new Date())
            .setExpiration(new Date(System.currentTimeMillis() + 1000 * 60 * 60))
            .signWith(SignatureAlgorithm.HS512, SECRET)
            .compact();
    }

    public String extractUsername(String token) {
        return Jwts.parser()
            .setSigningKey(SECRET)
            .parseClaimsJws(token)
            .getBody()
            .getSubject();
    }

    public boolean validateToken(String token, UserDetails userDetails) {
        return extractUsername(token).equals(userDetails.getUsername())
            && !isTokenExpired(token);
    }
}
```

**Фильтр, проверяющий токен в каждом запросе:**

```java
@Component
public class JwtAuthenticationFilter extends OncePerRequestFilter {

    @Autowired private JwtUtil jwtUtil;
    @Autowired private UserDetailsService userDetailsService;

    @Override
    protected void doFilterInternal(HttpServletRequest request,
                                    HttpServletResponse response,
                                    FilterChain filterChain)
            throws ServletException, IOException {

        String header = request.getHeader("Authorization");

        if (header != null && header.startsWith("Bearer ")) {
            String token = header.substring(7);
            String username = jwtUtil.extractUsername(token);

            if (username != null && SecurityContextHolder.getContext().getAuthentication() == null) {
                UserDetails userDetails = userDetailsService.loadUserByUsername(username);
                if (jwtUtil.validateToken(token, userDetails)) {
                    UsernamePasswordAuthenticationToken authToken =
                        new UsernamePasswordAuthenticationToken(
                            userDetails, null, userDetails.getAuthorities());
                    SecurityContextHolder.getContext().setAuthentication(authToken);
                }
            }
        }

        filterChain.doFilter(request, response);
    }
}
```

**Эндпоинт входа, возвращающий токен:**

```java
@RestController
@RequestMapping("/api/auth")
public class AuthRestController {

    @Autowired private AuthenticationManager authManager;
    @Autowired private JwtUtil jwtUtil;

    @PostMapping("/login")
    public ResponseEntity<String> login(@RequestBody User request) {
        Authentication auth = authManager.authenticate(
            new UsernamePasswordAuthenticationToken(
                request.getEmail(), request.getPassword()));

        UserDetails userDetails = (UserDetails) auth.getPrincipal();
        return ResponseEntity.ok(jwtUtil.generateToken(userDetails));
    }
}
```

Клиент сначала вызывает `POST /api/auth/login` с email и паролем, получает JWT-токен, и затем во всех последующих запросах добавляет заголовок `Authorization: Bearer <token>`.

---

## Часть 10: application.properties

В Spring Boot конфигурация задаётся в `src/main/resources/application.properties` (или `application.yml`). Типичный пример:

```properties
# Имя приложения
spring.application.name=student

# Подключение к H2 in-memory базе
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=

# JPA / Hibernate
# none / validate / update / create / create-drop
spring.jpa.hibernate.ddl-auto=update

# H2 веб-консоль (http://localhost:8080/h2-console)
spring.h2.console.enabled=true

# Thymeleaf — отключение кэша для разработки
spring.thymeleaf.cache=false

# Возвращать NoHandlerFoundException вместо 404 по умолчанию
spring.mvc.throw-exception-if-no-handler-found=true
server.error.whitelabel.enabled=false
```

---

## Часть 11: Пример реального приложения

Соберём всё вместе. Рассмотрим архитектуру демонстрационного веб-приложения для управления студентами и пользователями.

### 11.1 Архитектура

- **Контроллеры** — Web-контроллеры (Thymeleaf + MVC) и REST-контроллеры (JSON API).
- **Сервисы** — чёткое разделение на интерфейсы и реализации.
- **Репозитории** — на базе Spring Data JPA, для управления `Student` и `User`.
- **Конфигурации:**
  - Безопасность: `SecurityConfig`, `JwtAuthenticationFilter`, кастомные `AccessDeniedHandler` и `AuthenticationEntryPoint`.
  - Инициализация: `AppInitializer` создаёт базовые учётные записи при запуске.
  - Шаблонизатор: `ThymeleafConfig` с подключением Spring Security Dialect.
- **Модели** — `Student`, `User`, `Role` с JPA-аннотациями.
- **HTML-шаблоны** — оформлены в едином стиле на Bootstrap 5. Реализована отправка REST-запросов напрямую из HTML-страниц (fetch API).

### 11.2 Пользовательский интерфейс

Страницы: `login.html`, `register.html`, `students.html`, `users.html`, `error.html`.

- **Работа со студентами:** просмотр, добавление, редактирование и удаление; валидация форм; flash-сообщения; гибкое переключение между режимами редактирования и просмотра в таблице.
- **Работа с пользователями:** просмотр всех пользователей (`/users`), изменение роли (USER ⇄ ADMIN), удаление; регистрация новых пользователей; роль `SUPER_ADMIN` защищена от редактирования и удаления.

### 11.3 Безопасность и авторизация

- Авторизация на основе ролей: `USER`, `ADMIN`, `SUPER_ADMIN`.
- Ограничение доступа к действиям и маршрутам через аннотации `@PreAuthorize` и `sec:authorize` в шаблонах.
- Форма входа (`/login`) и регистрация (`/register`) с проверкой email.
- REST-защита: генерация и проверка JWT-токенов для API.

### 11.4 REST API и Swagger

Все основные функции доступны и через REST API. **Swagger UI (OpenAPI 3.0)** позволяет:
- изучать и тестировать эндпоинты;
- отправлять запросы с токеном авторизации;
- JWT-токен автоматически передаётся с фронта при работе с REST.

Для подключения Swagger достаточно добавить зависимость:

```xml
<dependency>
    <groupId>org.springdoc</groupId>
    <artifactId>springdoc-openapi-starter-webmvc-ui</artifactId>
    <version>2.8.9</version>
</dependency>
```

После этого Swagger UI доступен по `http://localhost:8080/swagger-ui.html`.

### 11.5 Документация

Все основные классы, интерфейсы и контроллеры снабжены **JavaDoc**. Генерация полной HTML-документации — с помощью Maven Site Plugin. Поддерживается стандартная структура проекта Maven с отчётами (`site`, `javadoc`, `apidocs`).

---

## Часть 12: Production-ready практики

Если предыдущие разделы давали «фундамент», то этот блок — то, без чего реальный REST-сервис на Spring Boot не пускают в продакшен. Здесь мы соединяем четыре техники, которые тесно работают друг с другом: валидацию входных данных, разделение entity и DTO, централизованную обработку ошибок и транзакционность.

### 12.1 Валидация данных (Bean Validation)

Контроллер — это граница доверия: всё, что пришло снаружи, нужно проверить. Без валидации в БД попадают пустые строки, отрицательные возрасты, кривые email — и приложение начинает «течь».

**Bean Validation** — стандарт Java (JSR 380, Jakarta Validation), реализация по умолчанию в Spring Boot — Hibernate Validator. Подключается одним стартером:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-validation</artifactId>
</dependency>
```

**Основные аннотации:**

| Аннотация | Применяется к | Что проверяет |
|-----------|---------------|---------------|
| `@NotNull` | любое | значение не `null` |
| `@NotBlank` | String | не `null`, не пустая, не только пробелы |
| `@NotEmpty` | String, Collection, Map, Array | не `null` и не пустая |
| `@Size(min, max)` | String, Collection | длина в диапазоне |
| `@Min`, `@Max` | числовые | значение в диапазоне |
| `@Email` | String | корректный email-адрес |
| `@Pattern(regexp)` | String | совпадает с regex |
| `@Past`, `@Future` | даты | в прошлом / будущем |
| `@Positive`, `@Negative` | числовые | строго `> 0` или `< 0` |
| `@Valid` | вложенный объект / коллекция | каскадная валидация |

**Применение на DTO:**

```java
public record StudentRequest(
    @NotBlank(message = "Имя обязательно")
    @Size(min = 2, max = 100, message = "Имя должно быть 2–100 символов")
    String name,

    @NotBlank(message = "Фамилия обязательна")
    @Size(min = 2, max = 100)
    String surname,

    @Min(value = 16, message = "Возраст не меньше 16")
    @Max(value = 120)
    int age,

    @Email(message = "Некорректный email")
    String email
) {}
```

**Запуск валидации в контроллере:**

```java
@PostMapping
public ResponseEntity<StudentResponse> create(
        @Valid @RequestBody StudentRequest request) {
    // если валидация не прошла — Spring выбросит
    // MethodArgumentNotValidException ДО входа в этот метод
    Student student = service.create(request);
    return ResponseEntity
        .status(HttpStatus.CREATED)
        .body(mapper.toResponse(student));
}
```

Это важный момент: сами по себе аннотации `@NotBlank` и т.д. на DTO ничего не делают. Валидацию запускает `@Valid` на параметре контроллера.

**Каскадная валидация** для вложенных объектов:

```java
public record EnrollmentRequest(
    @Valid                          // <-- запускает валидацию вложенного объекта
    @NotNull StudentRequest student,

    @NotNull Long courseId
) {}
```

### 12.2 DTO и разделение слоёв

В учебных примерах удобно возвращать `@Entity` напрямую из контроллера. В реальных проектах это четыре проблемы:

1. **Утечка внутреннего состояния.** Поля `password`, `internalNotes`, `deleted` попадают в JSON — даже если не должны.
2. **`LazyInitializationException`.** Jackson пытается сериализовать ленивую коллекцию вне транзакции — приложение падает.
3. **Сцепление API и БД.** Любое переименование поля в `@Entity` ломает клиентов API.
4. **Циклические ссылки.** `Student → Group → List<Student>` — бесконечная JSON-структура.

**Решение — DTO (Data Transfer Object): отдельные классы для границ API.**

```java
// Entity — внутренняя модель домена, маппинг на БД
@Entity
@Table(name = "students")
public class Student {
    @Id @GeneratedValue private Long id;
    private String name;
    private String surname;
    @ManyToOne(fetch = FetchType.LAZY)
    private Group group;        // ленивая связь
    // ...
}

// Request DTO — то, что приходит от клиента (валидируется)
public record StudentRequest(
    @NotBlank String name,
    @NotBlank String surname,
    Long groupId
) {}

// Response DTO — то, что отдаём клиенту
public record StudentResponse(
    Long id,
    String name,
    String surname,
    String groupName
) {}
```

**Маппинг** — простой Java-код в отдельном компоненте:

```java
@Component
public class StudentMapper {

    public Student toEntity(StudentRequest request, Group group) {
        Student s = new Student();
        s.setName(request.name());
        s.setSurname(request.surname());
        s.setGroup(group);
        return s;
    }

    public StudentResponse toResponse(Student s) {
        return new StudentResponse(
            s.getId(),
            s.getName(),
            s.getSurname(),
            s.getGroup() != null ? s.getGroup().getName() : null
        );
    }
}
```

Контроллер теперь работает только с DTO:

```java
@RestController
@RequestMapping("/api/students")
public class StudentRestController {

    private final StudentService service;
    private final StudentMapper mapper;

    public StudentRestController(StudentService service, StudentMapper mapper) {
        this.service = service;
        this.mapper = mapper;
    }

    @GetMapping
    public List<StudentResponse> getAll() {
        return service.findAll().stream()
            .map(mapper::toResponse)
            .toList();
    }

    @PostMapping
    public ResponseEntity<StudentResponse> create(
            @Valid @RequestBody StudentRequest request) {
        Student saved = service.create(request);
        return ResponseEntity
            .status(HttpStatus.CREATED)
            .body(mapper.toResponse(saved));
    }
}
```

**MapStruct** — генератор маппинга на этапе компиляции, без рефлексии:

```java
@Mapper(componentModel = "spring")
public interface StudentMapper {
    StudentResponse toResponse(Student student);
    Student toEntity(StudentRequest request);
}
```

Альтернатива — `ModelMapper` (рефлексия, медленнее, но проще для динамических случаев).

### 12.3 Обработка ошибок: @RestControllerAdvice

Когда `@Valid` не прошёл, Spring выбросит `MethodArgumentNotValidException`. Без обработчика клиент получит мусорный ответ 400 без указания, **какое именно поле** сломалось. Решение — централизованный обработчик.

- `@ControllerAdvice` — глобальный перехватчик исключений и моделей для всех контроллеров.
- `@RestControllerAdvice = @ControllerAdvice + @ResponseBody` — для REST API; возвращаемое значение сериализуется в JSON.

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    // Единый формат ошибки
    public record ErrorResponse(
        Instant timestamp,
        int status,
        String error,
        String message,
        String path,
        Map<String, String> fieldErrors  // только для валидации
    ) {}

    // 1. Валидация не прошла → 400 + список полей и сообщений
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ErrorResponse> handleValidation(
            MethodArgumentNotValidException ex,
            HttpServletRequest request) {

        Map<String, String> fieldErrors = new HashMap<>();
        ex.getBindingResult().getFieldErrors()
            .forEach(err -> fieldErrors.put(err.getField(), err.getDefaultMessage()));

        return ResponseEntity.badRequest().body(new ErrorResponse(
            Instant.now(), 400, "Bad Request",
            "Validation failed",
            request.getRequestURI(),
            fieldErrors
        ));
    }

    // 2. Сущность не найдена → 404
    @ExceptionHandler(EntityNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleNotFound(
            EntityNotFoundException ex,
            HttpServletRequest request) {
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(new ErrorResponse(
            Instant.now(), 404, "Not Found",
            ex.getMessage(), request.getRequestURI(), null
        ));
    }

    // 3. Нарушение бизнес-правила → 409
    @ExceptionHandler(IllegalStateException.class)
    public ResponseEntity<ErrorResponse> handleConflict(
            IllegalStateException ex,
            HttpServletRequest request) {
        return ResponseEntity.status(HttpStatus.CONFLICT).body(new ErrorResponse(
            Instant.now(), 409, "Conflict",
            ex.getMessage(), request.getRequestURI(), null
        ));
    }

    // 4. Общий catch-all — ОБЯЗАТЕЛЬНО последним
    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> handleAll(
            Exception ex, HttpServletRequest request) {
        return ResponseEntity.internalServerError().body(new ErrorResponse(
            Instant.now(), 500, "Internal Server Error",
            ex.getMessage(), request.getRequestURI(), null
        ));
    }
}
```

Теперь при невалидном POST клиент получает читаемый ответ:

```json
{
  "timestamp": "2026-05-15T10:30:00Z",
  "status": 400,
  "error": "Bad Request",
  "message": "Validation failed",
  "path": "/api/students",
  "fieldErrors": {
    "name": "Имя обязательно",
    "age": "Возраст не меньше 16"
  }
}
```

Что даёт `@RestControllerAdvice`:
- Контроллер остаётся чистым — никаких `try/catch` и ручных `ResponseEntity.badRequest()`.
- Единый формат ошибок для всего API.
- Логика обработки изолирована в одном месте — легко добавить логирование, метрики, корреляционные ID.

> **На заметку:** в демо-приложении (`lecture8/.../GlobalExceptionHandler.java`) показан гибридный подход — обработчик различает API-запросы и web-запросы и возвращает либо JSON, либо HTML-шаблон. Это полезно, когда одно приложение обслуживает и REST API, и Thymeleaf-фронтенд.

### 12.4 Транзакции: @Transactional

В части 5 мы упомянули, что `@Transactional` — пример Spring AOP «под капотом». Теперь разберём практику.

**Что делает `@Transactional`:** оборачивает вызов метода в транзакцию БД. Успешное завершение — `commit()`, выброс unchecked-исключения — `rollback()`.

**Главное правило: `@Transactional` ставится на сервисном слое, не на контроллере.** Если поставить на контроллер, транзакция остаётся открытой во время сериализации JSON — удлиняются блокировки в БД и смешиваются HTTP- и БД-концерны.

```java
@Service
public class StudentService {

    private final StudentRepository repository;
    private final GroupRepository groupRepository;

    public StudentService(StudentRepository r, GroupRepository g) {
        this.repository = r;
        this.groupRepository = g;
    }

    // Только чтение — Hibernate оптимизирует
    @Transactional(readOnly = true)
    public List<Student> findAll() {
        return repository.findAll();
    }

    // Обычная транзакция для изменения
    @Transactional
    public Student create(StudentRequest request) {
        Student s = new Student();
        s.setName(request.name());
        s.setSurname(request.surname());
        return repository.save(s);
    }

    // Классический пример, где транзакционность критична:
    // перевод студента между группами — атомарная операция
    @Transactional
    public void transferGroup(Long studentId, Long fromGroupId, Long toGroupId) {
        Group from = groupRepository.findById(fromGroupId)
            .orElseThrow(() -> new EntityNotFoundException("Group not found"));
        Group to = groupRepository.findById(toGroupId)
            .orElseThrow(() -> new EntityNotFoundException("Group not found"));
        Student s = repository.findById(studentId)
            .orElseThrow(() -> new EntityNotFoundException("Student not found"));

        from.removeStudent(s);
        // Если здесь упадёт исключение —
        // removeStudent() будет откачен
        to.addStudent(s);
    }
}
```

**Основные параметры `@Transactional`:**

| Параметр | Описание | Пример |
|----------|----------|--------|
| `readOnly` | Подсказка Hibernate: только чтение, без dirty-checking | `readOnly = true` |
| `propagation` | Поведение при вложенных транзакциях | `REQUIRED` (по умолчанию), `REQUIRES_NEW`, `MANDATORY`, `NESTED` |
| `isolation` | Уровень изоляции БД | `READ_COMMITTED`, `REPEATABLE_READ`, `SERIALIZABLE` |
| `rollbackFor` | Откатывать на указанные исключения (в том числе checked) | `rollbackFor = IOException.class` |
| `noRollbackFor` | НЕ откатывать на указанные исключения | `noRollbackFor = NotFoundException.class` |
| `timeout` | Таймаут в секундах | `timeout = 30` |

**Три классические ловушки:**

**1. `@Transactional` на `private` методе не работает.**
Spring AOP создаёт прокси, а прокси перехватывает только публичные методы. Если внутри одного класса вызвать `this.privateMethod()` — прокси обойдён, транзакции нет.

**2. Self-invocation тоже не работает.**

```java
@Service
public class StudentService {
    public void outer() {
        this.inner();   // ❌ @Transactional на inner() НЕ сработает
    }

    @Transactional
    public void inner() { /* ... */ }
}
```

Прокси перехватывает только внешние вызовы. Решение — внедрить сервис в самого себя (через провайдер или `ApplicationContext`), или вынести `inner` в отдельный бин.

**3. По умолчанию откат только при unchecked-исключении.**
Если метод бросает `IOException` (checked) — транзакция всё равно **успешно коммитится**! Если нужно иначе:

```java
@Transactional(rollbackFor = Exception.class)
public void importStudents() throws IOException { /* ... */ }
```

**Связь с `@RestControllerAdvice`:** когда сервис выбрасывает `EntityNotFoundException`, транзакция откатывается, а `@RestControllerAdvice` превращает исключение в HTTP 404. Все четыре техники из этой части работают как единая цепочка.

---

## Часть 13: Итоги

| Технология | Ключевые концепции |
|------------|-------------------|
| IoC / DI | Конструкторное внедрение, `@Autowired`, `@Qualifier`, `@Primary` |
| Spring Framework | POJO, IoC-контейнер, `ApplicationContext` |
| Spring Boot | Автоконфигурация, starters, `@SpringBootApplication` |
| Spring Bean | `@Component`, `@Service`, `@Repository`, `@Controller`, `@Bean` |
| Spring MVC | `@Controller`, `@RestController`, `@RequestMapping`, `@PathVariable`, `@RequestBody` |
| Валидация | `@Valid`, `@NotBlank`, `@Size`, `@Email`, каскадная валидация |
| DTO | Разделение entity и API, `record`, `@Component`-маппер, MapStruct |
| Обработка ошибок | `@RestControllerAdvice`, `@ExceptionHandler`, единый `ErrorResponse` |
| Транзакции | `@Transactional` на сервисном слое, `readOnly`, propagation, ловушки прокси |
| Spring Data JPA | `JpaRepository`, методы по соглашению об именах |
| Thymeleaf | `th:text`, `th:each`, `th:if`, `th:href`, `th:object`, `sec:authorize` |
| Spring Security | `SecurityFilterChain`, `@PreAuthorize`, `UserDetailsService`, `BCryptPasswordEncoder` |
| JWT | `generateToken`, `validateToken`, фильтр в цепочке |
| AOP | Aspect, JoinPoint, Pointcut, Advice; `@Transactional`, `@Cacheable` |
