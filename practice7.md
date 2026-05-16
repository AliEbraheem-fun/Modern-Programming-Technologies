# Практическое занятие 7: Spring Framework и Spring Boot

## Часть 1: Создание проекта Spring Boot

### Задание 1.1: Spring Initializr

Откройте [https://start.spring.io](https://start.spring.io) и сгенерируйте проект со следующими параметрами:

- **Project:** Maven
- **Language:** Java
- **Spring Boot:** 3.5.x
- **Group:** `mpt.it`
- **Artifact:** `student`
- **Name:** `student`
- **Package name:** `lecture.seven.student`
- **Packaging:** Jar
- **Java:** 21 (или 24, если установлена)

**Зависимости (Dependencies):**
- Spring Web
- Spring Data JPA
- Spring Security
- Thymeleaf
- H2 Database
- Spring Boot DevTools

Скачайте архив, распакуйте его. Откройте проект в IDE и убедитесь, что он собирается:

```bash
./mvnw clean compile      # Linux / macOS
mvnw.cmd clean compile    # Windows
```

Запустите приложение:

```bash
./mvnw spring-boot:run
```

В консоли вы должны увидеть баннер Spring Boot и сообщение о старте Tomcat на порту 8080.

---

### Задание 1.2: Анализ pom.xml

Откройте сгенерированный `pom.xml`. Ответьте письменно:

1. Что находится в секции `<parent>` и зачем она нужна?
2. Почему у большинства зависимостей нет версий?
3. Что делает плагин `spring-boot-maven-plugin`?
4. Какие транзитивные зависимости подключает `spring-boot-starter-web`? Выполните `mvn dependency:tree` и опишите 3–5 самых важных.

---

## Часть 2: IoC и DI — простой пример

### Задание 2.1: Создание бинов и внедрение зависимостей

Создайте пакет `lecture.seven.student.greet` и в нём три файла:

```java
// GreetingService.java — интерфейс
package lecture.seven.student.greet;

public interface GreetingService {
    String greet(String name);
}
```

```java
// EnglishGreetingService.java — реализация
package lecture.seven.student.greet;

import org.springframework.stereotype.Service;

@Service
public class EnglishGreetingService implements GreetingService {
    @Override
    public String greet(String name) {
        return "Hello, " + name + "!";
    }
}
```

```java
// GreetingController.java — REST-контроллер
package lecture.seven.student.greet;

import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/greet")
public class GreetingController {

    private final GreetingService greetingService;

    // Конструкторное внедрение — Spring сам передаст бин EnglishGreetingService
    public GreetingController(GreetingService greetingService) {
        this.greetingService = greetingService;
    }

    @GetMapping("/{name}")
    public String greet(@PathVariable String name) {
        return greetingService.greet(name);
    }
}
```

Запустите приложение и перейдите в браузере по адресу `http://localhost:8080/api/greet/World`. Должно вернуться `Hello, World!`.

**Объясните письменно:**
1. Каким образом Spring «знает», что `EnglishGreetingService` нужно подставить в `GreetingController`?
2. Что произойдёт, если убрать аннотацию `@Service` с класса `EnglishGreetingService`?
3. Что произойдёт, если создать **вторую** реализацию `GreetingService` (например, `RussianGreetingService`) и тоже пометить её `@Service` — без дополнительной настройки?

---

### Задание 2.2: Три способа внедрения

В пакете `lecture.seven.student.greet` создайте три класса, демонстрирующие разные способы DI:

```java
@Component
public class ConstructorInjectionDemo {
    private final GreetingService service;

    public ConstructorInjectionDemo(GreetingService service) {
        this.service = service;
    }
}

@Component
public class SetterInjectionDemo {
    private GreetingService service;

    @Autowired
    public void setService(GreetingService service) {
        this.service = service;
    }
}

@Component
public class FieldInjectionDemo {
    @Autowired
    private GreetingService service;
}
```

**Ответьте письменно:**
1. Какой способ предпочтительнее и почему?
2. Почему поле в `ConstructorInjectionDemo` может быть `final`, а в двух других — нет?
3. Какой способ труднее всего тестировать без Spring-контекста?

---

## Часть 3: REST-контроллер с CRUD

### Задание 3.1: Сущность Student

Создайте пакет `lecture.seven.student.model` и в нём JPA-сущность:

```java
package lecture.seven.student.model;

import jakarta.persistence.*;

@Entity
@Table(name = "students")
public class Student {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "name", nullable = false, length = 100)
    private String name;

    @Column(name = "surname", nullable = false, length = 100)
    private String surname;

    public Student() {}

    public Student(String name, String surname) {
        this.name = name;
        this.surname = surname;
    }

    // Геттеры и сеттеры для всех полей
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getSurname() { return surname; }
    public void setSurname(String surname) { this.surname = surname; }
}
```

В `src/main/resources/application.properties`:

```properties
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=
spring.jpa.hibernate.ddl-auto=update
spring.h2.console.enabled=true
```

### Задание 3.2: Репозиторий и сервис

Создайте пакет `lecture.seven.student.repository`:

```java
package lecture.seven.student.repository;

import lecture.seven.student.model.Student;
import org.springframework.data.jpa.repository.JpaRepository;

public interface StudentRepository extends JpaRepository<Student, Long> {
}
```

Создайте пакет `lecture.seven.student.service`:

```java
// StudentService.java
package lecture.seven.student.service;

import lecture.seven.student.model.Student;
import java.util.List;

public interface StudentService {
    List<Student> findAll();
    Student save(Student student);
    Student findById(Long id);
    void deleteById(Long id);
}

// StudentServiceImpl.java
package lecture.seven.student.service;

import lecture.seven.student.model.Student;
import lecture.seven.student.repository.StudentRepository;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class StudentServiceImpl implements StudentService {

    private final StudentRepository repository;

    public StudentServiceImpl(StudentRepository repository) {
        this.repository = repository;
    }

    @Override
    public List<Student> findAll() {
        return repository.findAll();
    }

    @Override
    public Student save(Student student) {
        return repository.save(student);
    }

    @Override
    public Student findById(Long id) {
        return repository.findById(id).orElse(null);
    }

    @Override
    public void deleteById(Long id) {
        repository.deleteById(id);
    }
}
```

### Задание 3.3: REST-контроллер

Создайте пакет `lecture.seven.student.controller`:

```java
package lecture.seven.student.controller;

import lecture.seven.student.model.Student;
import lecture.seven.student.service.StudentService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/students")
public class StudentRestController {

    private final StudentService studentService;

    public StudentRestController(StudentService studentService) {
        this.studentService = studentService;
    }

    @GetMapping
    public List<Student> getAll() {
        return studentService.findAll();
    }

    @GetMapping("/{id}")
    public ResponseEntity<Student> getById(@PathVariable Long id) {
        Student s = studentService.findById(id);
        return s != null ? ResponseEntity.ok(s) : ResponseEntity.notFound().build();
    }

    @PostMapping
    public ResponseEntity<Student> create(@RequestBody Student student) {
        return ResponseEntity.status(HttpStatus.CREATED).body(studentService.save(student));
    }

    @PutMapping("/{id}")
    public ResponseEntity<Student> update(@PathVariable Long id, @RequestBody Student student) {
        if (studentService.findById(id) == null) {
            return ResponseEntity.notFound().build();
        }
        student.setId(id);
        return ResponseEntity.ok(studentService.save(student));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable Long id) {
        if (studentService.findById(id) == null) {
            return ResponseEntity.notFound().build();
        }
        studentService.deleteById(id);
        return ResponseEntity.noContent().build();
    }
}
```

### Задание 3.4: Тестирование REST API

Запустите приложение. Используя браузер, **Postman** или `curl`, выполните:

```bash
# Создание студента
curl -X POST http://localhost:8080/api/students \
    -H "Content-Type: application/json" \
    -d '{"name":"Ali","surname":"Hasan"}'

# Получение всех
curl http://localhost:8080/api/students

# Получение по id
curl http://localhost:8080/api/students/1

# Обновление
curl -X PUT http://localhost:8080/api/students/1 \
    -H "Content-Type: application/json" \
    -d '{"name":"Ivan","surname":"Petrov"}'

# Удаление
curl -X DELETE http://localhost:8080/api/students/1
```

Запишите ответы (включая HTTP-коды) для каждого запроса.

---

## Часть 4: Веб-интерфейс с Thymeleaf

### Задание 4.1: Web-контроллер

Создайте `StudentWebController`:

```java
package lecture.seven.student.controller;

import lecture.seven.student.model.Student;
import lecture.seven.student.service.StudentService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
@RequestMapping("/students")
public class StudentWebController {

    private final StudentService service;

    public StudentWebController(StudentService service) {
        this.service = service;
    }

    @GetMapping
    public String list(Model model) {
        model.addAttribute("students", service.findAll());
        model.addAttribute("student", new Student());
        return "students";
    }

    @PostMapping("/save")
    public String save(@ModelAttribute Student student) {
        service.save(student);
        return "redirect:/students";
    }

    @GetMapping("/delete/{id}")
    public String delete(@PathVariable Long id) {
        service.deleteById(id);
        return "redirect:/students";
    }
}
```

### Задание 4.2: Шаблон students.html

Создайте `src/main/resources/templates/students.html`:

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>Students</title>
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body class="container mt-4">

<h2 class="mb-4">Список студентов</h2>

<form th:action="@{/students/save}" th:object="${student}" method="post"
      class="row g-2 mb-4">
    <div class="col-md-4">
        <input type="text" th:field="*{name}" class="form-control"
               placeholder="Имя" required/>
    </div>
    <div class="col-md-4">
        <input type="text" th:field="*{surname}" class="form-control"
               placeholder="Фамилия" required/>
    </div>
    <div class="col-md-4">
        <button type="submit" class="btn btn-primary">Добавить</button>
    </div>
</form>

<table class="table table-striped">
    <thead>
    <tr><th>ID</th><th>Имя</th><th>Фамилия</th><th>Действия</th></tr>
    </thead>
    <tbody>
    <tr th:each="s : ${students}">
        <td th:text="${s.id}"></td>
        <td th:text="${s.name}"></td>
        <td th:text="${s.surname}"></td>
        <td>
            <a th:href="@{/students/delete/{id}(id=${s.id})}"
               class="btn btn-danger btn-sm"
               onclick="return confirm('Удалить?')">Удалить</a>
        </td>
    </tr>
    </tbody>
</table>

</body>
</html>
```

Перейдите в браузере на `http://localhost:8080/students`. Добавьте несколько студентов, удалите одного. Объясните: (1) что делает атрибут `th:object`? (2) как Thymeleaf привязывает поля формы к объекту через `th:field="*{name}"`? (3) что делает `redirect:` в значении возвращаемой строки?

---

## Часть 5: Spring Security

### Задание 5.1: Базовая безопасность

Добавьте конфигурацию безопасности. Создайте пакет `lecture.seven.student.config` и в нём:

```java
package lecture.seven.student.config;

import org.springframework.context.annotation.*;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configurers.AbstractHttpConfigurer;
import org.springframework.security.core.userdetails.*;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.provisioning.InMemoryUserDetailsManager;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
public class SecurityConfig {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/api/students").hasAnyRole("USER", "ADMIN")
                .requestMatchers("/api/students/**").hasRole("ADMIN")
                .requestMatchers("/students/**").authenticated()
                .anyRequest().permitAll()
            )
            .formLogin(form -> form.permitAll())
            .logout(logout -> logout.permitAll())
            .csrf(AbstractHttpConfigurer::disable);

        return http.build();
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }

    @Bean
    public UserDetailsService userDetailsService(PasswordEncoder encoder) {
        UserDetails user = User.withUsername("user")
            .password(encoder.encode("password"))
            .roles("USER")
            .build();

        UserDetails admin = User.withUsername("admin")
            .password(encoder.encode("password"))
            .roles("ADMIN")
            .build();

        return new InMemoryUserDetailsManager(user, admin);
    }
}
```

Перезапустите приложение. Откройте `/students` — должна появиться форма входа.

**Проверьте:**
1. Войдите как `user / password`. Можете ли вы добавить нового студента через REST (`POST /api/students`)? Какой код ответа?
2. Войдите как `admin / password`. Получится ли теперь?
3. Что происходит при попытке `GET /api/students` без аутентификации?

### Задание 5.2: Защита методов через @PreAuthorize

Добавьте в `SecurityConfig`:

```java
@EnableMethodSecurity   // на уровне класса
```

В контроллер `StudentRestController` добавьте `@PreAuthorize`:

```java
@GetMapping
@PreAuthorize("hasAnyRole('USER', 'ADMIN')")
public List<Student> getAll() { ... }

@DeleteMapping("/{id}")
@PreAuthorize("hasRole('ADMIN')")
public ResponseEntity<Void> delete(@PathVariable Long id) { ... }
```

**Объясните:**
1. В чём различие между `requestMatchers(...).hasRole(...)` в `SecurityConfig` и `@PreAuthorize` на методе?
2. Что произойдёт при двух конфликтующих правилах (например, в `SecurityConfig` разрешено `USER`, а на методе `@PreAuthorize("hasRole('ADMIN')")`)?

---

## Часть 6: Дополнительные задания

### Задание 6.1: Кастомные методы в JpaRepository

Расширьте `StudentRepository`:

```java
public interface StudentRepository extends JpaRepository<Student, Long> {
    List<Student> findByNameContainingIgnoreCase(String namePart);
    List<Student> findBySurnameContainingIgnoreCase(String surnamePart);
    long countByName(String name);
}
```

Добавьте в REST-контроллер эндпоинты, использующие новые методы. Например:

```java
@GetMapping("/search")
public List<Student> search(@RequestParam String q) {
    return repository.findByNameContainingIgnoreCase(q);
}
```

### Задание 6.2: Аспект логирования

Добавьте зависимость:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-aop</artifactId>
</dependency>
```

Создайте логирующий аспект:

```java
package lecture.seven.student.aspect;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.*;
import org.springframework.stereotype.Component;

@Aspect
@Component
public class LoggingAspect {

    @Before("execution(* lecture.seven.student.service.*.*(..))")
    public void logBefore(JoinPoint joinPoint) {
        System.out.println(">>> " + joinPoint.getSignature().toShortString());
    }

    @AfterReturning(pointcut = "execution(* lecture.seven.student.service.*.*(..))",
                    returning = "result")
    public void logAfter(JoinPoint joinPoint, Object result) {
        System.out.println("<<< " + joinPoint.getSignature().getName() + " => " + result);
    }
}
```

Выполните любой запрос. В логе должны появиться записи о вызовах методов сервиса.

### Задание 6.3: AppInitializer

Добавьте автоматическое создание тестовых данных при старте приложения:

```java
package lecture.seven.student.config;

import jakarta.annotation.PostConstruct;
import lecture.seven.student.model.Student;
import lecture.seven.student.repository.StudentRepository;
import org.springframework.stereotype.Component;

@Component
public class AppInitializer {

    private final StudentRepository repository;

    public AppInitializer(StudentRepository repository) {
        this.repository = repository;
    }

    @PostConstruct
    public void init() {
        if (repository.count() == 0) {
            repository.save(new Student("Ali", "Hasan"));
            repository.save(new Student("Fatima", "Kassem"));
            repository.save(new Student("Ivan", "Petrov"));
            repository.save(new Student("Ekaterina", "Sidorova"));
            System.out.println("Созданы тестовые студенты");
        }
    }
}
```

Что произойдёт, если убрать `@PostConstruct`? А если убрать `@Component`?

### Задание 6.4: Тест контроллера

Добавьте интеграционный тест с использованием `@WebMvcTest`:

```java
package lecture.seven.student.controller;

import lecture.seven.student.model.Student;
import lecture.seven.student.service.StudentService;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.*;
import org.springframework.security.test.context.support.WithMockUser;
import org.springframework.test.context.bean.override.mockito.MockitoBean;
import org.springframework.test.web.servlet.MockMvc;

import java.util.List;

import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@WebMvcTest(StudentRestController.class)
@AutoConfigureMockMvc(addFilters = false)
class StudentRestControllerTest {

    @Autowired
    private MockMvc mvc;

    @MockitoBean
    private StudentService service;

    @Test
    @WithMockUser(roles = "ADMIN")
    void getAll_ok() throws Exception {
        when(service.findAll()).thenReturn(List.of(new Student("A", "B")));
        mvc.perform(get("/api/students"))
           .andExpect(status().isOk());
    }
}
```

Запустите: `./mvnw test`. Объясните: (1) что делает `@WebMvcTest`? (2) зачем нужен `@MockitoBean`? (3) что делает `@WithMockUser`?

---

## Часть 7: Production-ready практики

В этой части вы соедините четыре техники, которые отличают учебный пример от реального сервиса: валидацию, DTO, централизованную обработку ошибок и транзакции.

### Задание 7.1: Валидация входных данных

1. Добавьте в `pom.xml`:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-validation</artifactId>
</dependency>
```

2. Создайте пакет `lecture.seven.student.dto` и в нём DTO с валидацией:

```java
package lecture.seven.student.dto;

import jakarta.validation.constraints.*;

public record StudentRequest(
    @NotBlank(message = "Имя обязательно")
    @Size(min = 2, max = 100, message = "Имя 2–100 символов")
    String name,

    @NotBlank(message = "Фамилия обязательна")
    @Size(min = 2, max = 100)
    String surname
) {}
```

3. В `StudentRestController` замените параметр `@RequestBody Student student` на `@Valid @RequestBody StudentRequest request` в POST и PUT.

4. Проверьте через `curl`:

```bash
# Невалидные данные
curl -i -X POST http://localhost:8080/api/students \
    -H "Content-Type: application/json" \
    -d '{"name":"","surname":"A"}'

# Должно вернуть HTTP 400 (а после задания 7.3 — структурированную ошибку)
```

**Ответьте письменно:** (1) Что произойдёт, если убрать `@Valid` с параметра? (2) Чем `@NotNull` отличается от `@NotBlank` для типа `String`? (3) Где валидация запускается во времени — до входа в метод контроллера или после?

---

### Задание 7.2: DTO и Mapper

1. Добавьте Response DTO в тот же пакет:

```java
package lecture.seven.student.dto;

public record StudentResponse(
    Long id,
    String name,
    String surname
) {}
```

2. Создайте `StudentMapper`:

```java
package lecture.seven.student.dto;

import lecture.seven.student.model.Student;
import org.springframework.stereotype.Component;

@Component
public class StudentMapper {

    public Student toEntity(StudentRequest request) {
        Student s = new Student();
        s.setName(request.name());
        s.setSurname(request.surname());
        return s;
    }

    public StudentResponse toResponse(Student s) {
        return new StudentResponse(s.getId(), s.getName(), s.getSurname());
    }
}
```

3. Перепишите `StudentRestController`, чтобы он работал только с DTO:

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

    @GetMapping("/{id}")
    public ResponseEntity<StudentResponse> getById(@PathVariable Long id) {
        Student s = service.findById(id);
        return s != null
            ? ResponseEntity.ok(mapper.toResponse(s))
            : ResponseEntity.notFound().build();
    }

    @PostMapping
    public ResponseEntity<StudentResponse> create(
            @Valid @RequestBody StudentRequest request) {
        Student saved = service.save(mapper.toEntity(request));
        return ResponseEntity.status(HttpStatus.CREATED)
            .body(mapper.toResponse(saved));
    }

    @PutMapping("/{id}")
    public ResponseEntity<StudentResponse> update(
            @PathVariable Long id,
            @Valid @RequestBody StudentRequest request) {
        if (service.findById(id) == null) {
            return ResponseEntity.notFound().build();
        }
        Student entity = mapper.toEntity(request);
        entity.setId(id);
        return ResponseEntity.ok(mapper.toResponse(service.save(entity)));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable Long id) {
        if (service.findById(id) == null) {
            return ResponseEntity.notFound().build();
        }
        service.deleteById(id);
        return ResponseEntity.noContent().build();
    }
}
```

4. Запустите приложение, выполните CRUD-запросы и убедитесь, что в JSON-ответах нет полей entity, которых нет в `StudentResponse`.

**Ответьте письменно:** (1) Зачем нужно разделять Entity и DTO? (2) Что произойдёт, если у entity есть `@ManyToOne Group` с `fetch = FetchType.LAZY`, и контроллер возвращает entity напрямую вне транзакции? (3) Какие преимущества даёт `record` по сравнению с обычным классом для DTO?

---

### Задание 7.3: Глобальная обработка ошибок через @RestControllerAdvice

1. Создайте пакет `lecture.seven.student.exception` и в нём:

```java
package lecture.seven.student.exception;

import jakarta.persistence.EntityNotFoundException;
import jakarta.servlet.http.HttpServletRequest;
import org.springframework.http.*;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.*;

import java.time.Instant;
import java.util.*;

@RestControllerAdvice
public class GlobalExceptionHandler {

    public record ErrorResponse(
        Instant timestamp,
        int status,
        String error,
        String message,
        String path,
        Map<String, String> fieldErrors
    ) {}

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

    @ExceptionHandler(EntityNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleNotFound(
            EntityNotFoundException ex,
            HttpServletRequest request) {
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(new ErrorResponse(
            Instant.now(), 404, "Not Found",
            ex.getMessage(), request.getRequestURI(), null
        ));
    }

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

2. Перезапустите приложение и снова попробуйте невалидный POST:

```bash
curl -i -X POST http://localhost:8080/api/students \
    -H "Content-Type: application/json" \
    -d '{"name":"","surname":"A"}'
```

В теле ответа должны увидеть структурированный JSON с `fieldErrors`, указывающими на конкретные ошибки.

3. Измените `StudentService.findById`, чтобы при отсутствии бросать `EntityNotFoundException`:

```java
@Override
public Student findById(Long id) {
    return repository.findById(id)
        .orElseThrow(() -> new EntityNotFoundException(
            "Student with id " + id + " not found"));
}
```

Проверьте `GET /api/students/999` — должен прийти 404 с понятным сообщением.

**Ответьте письменно:** (1) Чем `@RestControllerAdvice` отличается от `@ControllerAdvice`? (2) В каком порядке Spring выбирает обработчик, если у нас определены `@ExceptionHandler(EntityNotFoundException.class)` и `@ExceptionHandler(Exception.class)`? (3) Почему обработчик для `Exception.class` должен стоять последним в логическом смысле (и почему на практике порядок методов не важен)?

---

### Задание 7.4: Транзакции и подводные камни

1. Добавьте `@Transactional` в методы `StudentServiceImpl`:

```java
import org.springframework.transaction.annotation.Transactional;

@Service
public class StudentServiceImpl implements StudentService {

    private final StudentRepository repository;

    public StudentServiceImpl(StudentRepository repository) {
        this.repository = repository;
    }

    @Transactional(readOnly = true)
    public List<Student> findAll() {
        return repository.findAll();
    }

    @Transactional(readOnly = true)
    public Student findById(Long id) {
        return repository.findById(id).orElse(null);
    }

    @Transactional
    public Student save(Student student) {
        return repository.save(student);
    }

    @Transactional
    public void deleteById(Long id) {
        repository.deleteById(id);
    }

    // Демонстрация: метод, бросающий исключение посередине
    @Transactional
    public void saveTwoOneBroken(Student good, Student bad) {
        repository.save(good);
        if (bad.getName() == null || bad.getName().isBlank()) {
            throw new IllegalStateException("Имя не может быть пустым");
        }
        repository.save(bad);
    }
}
```

2. Вызовите `saveTwoOneBroken` через временный REST-эндпоинт или CommandLineRunner, передав `bad` с пустым именем. Проверьте через H2-консоль или `GET /api/students`: первый студент должен **не сохраниться** благодаря откату транзакции. Сравните поведение, если убрать `@Transactional`.

3. Изучите подводные камни (self-invocation). Создайте такой класс:

```java
@Service
public class TxPitfallService {

    private final StudentRepository repository;
    public TxPitfallService(StudentRepository r) { this.repository = r; }

    public void outerWithoutAnnotation(Student good, Student bad) {
        // ВНИМАНИЕ: this.innerWithTransaction(...) не создаст транзакцию,
        // потому что вызов идёт через this, минуя Spring-прокси
        this.innerWithTransaction(good, bad);
    }

    @Transactional
    public void innerWithTransaction(Student good, Student bad) {
        repository.save(good);
        if (bad.getName().isBlank()) {
            throw new IllegalStateException("Bad student");
        }
        repository.save(bad);
    }
}
```

Запустите и наблюдайте: при self-invocation первый студент **сохранится**, потому что транзакция не открылась.

**Ответьте письменно:** (1) Где правильно ставить `@Transactional` — на контроллере, сервисе или репозитории, и почему? (2) Что значит `readOnly = true`? (3) Какие три типичные ловушки `@Transactional`-прокси? (4) При каких исключениях по умолчанию транзакция откатывается, а при каких — нет?

---

## Часть 8: Контрольные вопросы

Ответьте письменно:

1. Сформулируйте принцип IoC своими словами. Чем он отличается от обычного процедурного подхода?
2. Назовите три способа DI в Spring. Какой из них предпочтителен и почему?
3. Чем отличаются `@Component`, `@Service`, `@Repository`, `@Controller`?
4. Чем `@RestController` отличается от `@Controller`?
5. Что делает аннотация `@SpringBootApplication`?
6. Что такое starter-модуль? Приведите 3 примера и опишите, что они подключают.
7. Что такое `ApplicationContext` и чем он отличается от `BeanFactory`?
8. Какие scope бинов вы знаете и в чём их различие?
9. Объясните принципы AOP: Aspect, JoinPoint, Pointcut, Advice.
10. Что делает `@PathVariable` и чем отличается от `@RequestParam`?
11. Объясните цепочку `Controller → Service → Repository`. Зачем нужны эти слои?
12. Что такое `JpaRepository`? Как Spring Data сам генерирует реализацию методов вида `findByNameContainingIgnoreCase`?
13. Как Thymeleaf получает данные от контроллера и подставляет их в шаблон?
14. Что такое `SecurityFilterChain` в Spring Security?
15. Зачем нужен `PasswordEncoder` и почему пароли нельзя хранить в открытом виде?
16. Опишите алгоритм работы JWT-аутентификации.
17. В чём преимущество JWT перед стандартной session-based аутентификацией для REST API?
18. Зачем нужна аннотация `@Valid` на параметре контроллера? Что случится, если её убрать?
19. Перечислите 5 проблем, которые возникают при возврате `@Entity` напрямую из REST-контроллера.
20. Чем `@RestControllerAdvice` отличается от `@ControllerAdvice`? Когда какой использовать?
21. Почему `@Transactional` рекомендуется ставить на сервисном слое, а не на контроллере?
22. Что такое self-invocation в контексте `@Transactional` и почему это проблема?
23. Откатится ли транзакция по умолчанию, если метод бросает checked-исключение (например, `IOException`)?

---

## Результаты занятия

К концу занятия вы должны сдать:
1. Spring Boot проект с REST-контроллером (CRUD для `Student`).
2. Веб-интерфейс на Thymeleaf для управления студентами.
3. Spring Security с двумя пользователями (`user` и `admin`) и разграничением доступа.
4. Минимум один тест для REST-контроллера через `MockMvc`.
5. **Production-ready доработки:**
   - `StudentRequest` / `StudentResponse` DTO с Bean Validation.
   - `StudentMapper` (`@Component`), контроллер работает только с DTO.
   - `GlobalExceptionHandler` через `@RestControllerAdvice` с единым `ErrorResponse`.
   - `@Transactional` на сервисном слое (с разделением `readOnly` для запросов).
6. Ответы на контрольные вопросы (1–23).

**Критерии оценки:**
- Приложение запускается командой `./mvnw spring-boot:run` без ошибок.
- REST-эндпоинты корректно отвечают на CRUD-запросы.
- Невалидный POST/PUT возвращает HTTP 400 с структурированным телом и списком `fieldErrors`.
- GET по несуществующему id возвращает HTTP 404 с понятным сообщением.
- В JSON-ответах нет полей entity, которых нет в Response DTO.
- Web-страница `/students` отображает список и позволяет добавлять/удалять студентов.
- Доступ к защищённым ресурсам ограничен по ролям.
- Все компоненты подключены через DI (без ручного `new ...` для сервисов/репозиториев).
- Транзакции на сервисном слое; ошибка посередине метода откатывает все изменения.
- Тесты проходят (`./mvnw test`).
