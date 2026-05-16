# Тест 7: Spring Framework и Spring Boot (Лекция 7)

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

<!-- ===== РАЗДЕЛ 1: IoC и DI (Вопросы 1–8) ===== -->

<div class="quiz-question" data-correct="2">
<h4>Вопрос 1. Что такое Inversion of Control (IoC)?</h4>

<div class="quiz-option" data-index="0">Метод оптимизации SQL-запросов в Hibernate</div>
<div class="quiz-option" data-index="1">Шаблон проектирования для реализации многопоточности</div>
<div class="quiz-option" data-index="2">Принцип проектирования, при котором управление жизненным циклом объектов передаётся внешнему фреймворку или контейнеру</div>
<div class="quiz-option" data-index="3">Способ инверсии порядка выполнения методов в стеке вызовов</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 2. Что такое Dependency Injection (DI)?</h4>

<div class="quiz-option" data-index="0">Способ внедрения SQL-запросов в код приложения</div>
<div class="quiz-option" data-index="1">Техника реализации IoC: объект получает свои зависимости извне (от контейнера), а не создаёт их сам</div>
<div class="quiz-option" data-index="2">Метод тестирования, при котором в код «впрыскиваются» проверки</div>
<div class="quiz-option" data-index="3">Алгоритм автоматического разрешения циклических зависимостей в SQL</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 3. Какие три способа DI существуют в Spring?</h4>

<div class="quiz-option" data-index="0">Через рефлексию, через JNI, через сериализацию</div>
<div class="quiz-option" data-index="1">Через REST API, через JMS, через файлы</div>
<div class="quiz-option" data-index="2">Через XML, через JSON, через YAML</div>
<div class="quiz-option" data-index="3">Через конструктор, через сеттер, через поле</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 4. Какой способ DI в Spring рекомендуется как предпочтительный?</h4>

<div class="quiz-option" data-index="0">Конструкторное внедрение (Constructor Injection)</div>
<div class="quiz-option" data-index="1">Внедрение через поле с @Autowired</div>
<div class="quiz-option" data-index="2">Внедрение через сеттер с @Autowired</div>
<div class="quiz-option" data-index="3">Внедрение через статический инициализатор</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 5. Какой код корректно демонстрирует конструкторное внедрение зависимостей?</h4>

```java
// Вариант A
@Service
public class StudentService {
    @Autowired
    private StudentRepository repository;
}

// Вариант B
@Service
public class StudentService {
    private final StudentRepository repository;

    public StudentService(StudentRepository repository) {
        this.repository = repository;
    }
}
```

<div class="quiz-option" data-index="0">Вариант A — поле с @Autowired предпочтительнее</div>
<div class="quiz-option" data-index="1">Оба варианта одинаковы и взаимозаменяемы</div>
<div class="quiz-option" data-index="2">Вариант B — конструкторное внедрение позволяет сделать поле final и упрощает тестирование</div>
<div class="quiz-option" data-index="3">Ни один — нужен XML-файл с описанием бинов</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 6. Почему внедрение зависимостей через поле (@Autowired private ...) считается плохой практикой?</h4>

<div class="quiz-option" data-index="0">Это работает медленнее, чем через конструктор</div>
<div class="quiz-option" data-index="1">Поле нельзя сделать final, зависимости скрыты, юнит-тестирование без Spring-контекста затруднено</div>
<div class="quiz-option" data-index="2">Spring не поддерживает этот способ начиная с версии 3</div>
<div class="quiz-option" data-index="3">Этот способ требует обязательного наличия XML-конфигурации</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 7. Голливудский принцип «не вызывай нас — мы сами тебя позовём» лежит в основе:</h4>

<div class="quiz-option" data-index="0">JDBC API</div>
<div class="quiz-option" data-index="1">Hibernate Session</div>
<div class="quiz-option" data-index="2">REST API</div>
<div class="quiz-option" data-index="3">Inversion of Control (IoC)</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 8. Что произойдёт при наличии двух реализаций интерфейса GreetingService, помеченных @Service, без дополнительной настройки?</h4>

<div class="quiz-option" data-index="0">Spring выберет первую попавшуюся реализацию</div>
<div class="quiz-option" data-index="1">Spring создаст массив всех реализаций и подставит его</div>
<div class="quiz-option" data-index="2">Spring выбросит NoUniqueBeanDefinitionException при попытке внедрить GreetingService</div>
<div class="quiz-option" data-index="3">Приложение запустится, но Service не будет создан</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 2: Spring Framework и Spring Boot (Вопросы 9–16) ===== -->

<div class="quiz-question" data-correct="1">
<h4>Вопрос 9. Что такое Spring Framework?</h4>

<div class="quiz-option" data-index="0">Реляционная СУБД, разработанная компанией VMware</div>
<div class="quiz-option" data-index="1">Универсальный фреймворк с открытым исходным кодом для платформы Java, основанный на принципах IoC и DI</div>
<div class="quiz-option" data-index="2">JavaScript-фреймворк для frontend-разработки</div>
<div class="quiz-option" data-index="3">Стандарт сериализации Java-объектов в JSON</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 10. Что такое Spring Boot?</h4>

<div class="quiz-option" data-index="0">Самостоятельный фреймворк, не связанный со Spring</div>
<div class="quiz-option" data-index="1">Утилита миграции с Spring 2 на Spring 3</div>
<div class="quiz-option" data-index="2">Виртуальная машина, оптимизированная для Spring-приложений</div>
<div class="quiz-option" data-index="3">Расширение Spring Framework, упрощающее разработку: автоконфигурация, встроенные серверы, starter-модули</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 11. Какая аннотация запускает Spring Boot приложение и активирует автоконфигурацию?</h4>

<div class="quiz-option" data-index="0">@SpringBootApplication</div>
<div class="quiz-option" data-index="1">@EnableSpring</div>
<div class="quiz-option" data-index="2">@RunSpringBoot</div>
<div class="quiz-option" data-index="3">@SpringStarter</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 12. Что включает в себя аннотация @SpringBootApplication?</h4>

<div class="quiz-option" data-index="0">@RestController + @Entity + @Repository</div>
<div class="quiz-option" data-index="1">@SpringBootTest + @AutoConfigureMockMvc</div>
<div class="quiz-option" data-index="2">@Configuration + @EnableAutoConfiguration + @ComponentScan</div>
<div class="quiz-option" data-index="3">@Service + @Component + @Bean</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 13. Что такое Spring Initializr?</h4>

<div class="quiz-option" data-index="0">Утилита для тестирования Spring-приложений</div>
<div class="quiz-option" data-index="1">Веб-сервис от команды Spring (start.spring.io) для генерации шаблона проекта Spring Boot</div>
<div class="quiz-option" data-index="2">Класс инициализации базы данных при старте приложения</div>
<div class="quiz-option" data-index="3">Аннотация для запуска кода при старте приложения</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 14. Что такое starter-модуль в Spring Boot?</h4>

<div class="quiz-option" data-index="0">Главный класс приложения с методом main()</div>
<div class="quiz-option" data-index="1">Класс, реализующий ApplicationRunner для запуска кода при старте</div>
<div class="quiz-option" data-index="2">Скрипт автозапуска сервера приложений</div>
<div class="quiz-option" data-index="3">Зависимость, подключающая группу связанных библиотек с согласованными версиями</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 15. Какой starter подключает Spring MVC и встроенный Tomcat для веб-приложений?</h4>

<div class="quiz-option" data-index="0">spring-boot-starter-web</div>
<div class="quiz-option" data-index="1">spring-boot-starter-tomcat</div>
<div class="quiz-option" data-index="2">spring-boot-starter-mvc</div>
<div class="quiz-option" data-index="3">spring-boot-starter-http</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 16. Почему в Spring Boot pom.xml у большинства зависимостей не указаны версии?</h4>

<div class="quiz-option" data-index="0">Spring Boot не использует Maven для управления зависимостями</div>
<div class="quiz-option" data-index="1">Maven автоматически берёт самые свежие версии</div>
<div class="quiz-option" data-index="2">Родительский pom spring-boot-starter-parent (или BOM) задаёт согласованные версии всех зависимостей</div>
<div class="quiz-option" data-index="3">Версии указываются на сайте Maven Central и подключаются автоматически</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 3: IoC Container и Bean (Вопросы 17–24) ===== -->

<div class="quiz-question" data-correct="2">
<h4>Вопрос 17. Что такое Spring IoC Container?</h4>

<div class="quiz-option" data-index="0">Контейнер сериализованных Java-объектов</div>
<div class="quiz-option" data-index="1">Docker-контейнер для запуска Spring-приложений</div>
<div class="quiz-option" data-index="2">Ядро фреймворка Spring, управляющее созданием, конфигурацией и жизненным циклом бинов</div>
<div class="quiz-option" data-index="3">Хранилище SQL-запросов для Hibernate</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 18. Чем ApplicationContext отличается от BeanFactory?</h4>

<div class="quiz-option" data-index="0">ApplicationContext расширяет BeanFactory, добавляя поддержку интернационализации, событий и интеграцию с Spring AOP</div>
<div class="quiz-option" data-index="1">ApplicationContext — устаревший интерфейс, BeanFactory — современный</div>
<div class="quiz-option" data-index="2">BeanFactory работает только с XML, ApplicationContext — только с аннотациями</div>
<div class="quiz-option" data-index="3">ApplicationContext и BeanFactory — синонимы</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 19. Что такое Spring Bean?</h4>

<div class="quiz-option" data-index="0">Сериализованный Java-объект с интерфейсом Serializable</div>
<div class="quiz-option" data-index="1">Объект, создаваемый, настраиваемый и управляемый Spring IoC Container'ом</div>
<div class="quiz-option" data-index="2">Класс, наследующий специальный SpringBean</div>
<div class="quiz-option" data-index="3">Поле класса, помеченное аннотацией @Bean</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 20. Какой scope используется для Spring Bean по умолчанию?</h4>

<div class="quiz-option" data-index="0">prototype</div>
<div class="quiz-option" data-index="1">request</div>
<div class="quiz-option" data-index="2">session</div>
<div class="quiz-option" data-index="3">singleton</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 21. Какие аннотации делают класс Spring-бином при сканировании пакетов?</h4>

<div class="quiz-option" data-index="0">@Entity, @Table, @Column</div>
<div class="quiz-option" data-index="1">@Override, @Deprecated, @SuppressWarnings</div>
<div class="quiz-option" data-index="2">@Component, @Service, @Repository, @Controller, @RestController</div>
<div class="quiz-option" data-index="3">@Public, @Private, @Internal</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 22. Какое отличие между @Service, @Repository и @Component с точки зрения контейнера?</h4>

<div class="quiz-option" data-index="0">Все они — специализации @Component; функционально для контейнера почти равнозначны, но несут смысловую нагрузку, а @Repository дополнительно преобразует исключения в DataAccessException</div>
<div class="quiz-option" data-index="1">@Service обязателен для всех бизнес-классов, без него код не скомпилируется</div>
<div class="quiz-option" data-index="2">@Repository может применяться только к JPA-сущностям</div>
<div class="quiz-option" data-index="3">@Component не сканируется автоматически, его нужно регистрировать вручную</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 23. Какой код корректно регистрирует бин PasswordEncoder через Java-конфигурацию?</h4>

```java
// Вариант A
@Component
public class PasswordEncoderHolder {
    public PasswordEncoder encoder = new BCryptPasswordEncoder();
}

// Вариант B
@Configuration
public class AppConfig {
    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}
```

<div class="quiz-option" data-index="0">Вариант A — поле автоматически становится бином</div>
<div class="quiz-option" data-index="1">Оба варианта одинаково корректны</div>
<div class="quiz-option" data-index="2">Ни один — бины нужно регистрировать через XML</div>
<div class="quiz-option" data-index="3">Вариант B — метод с @Bean в @Configuration возвращает объект, который становится бином в контейнере</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 24. Какая аннотация вызывает метод сразу после создания бина и внедрения зависимостей?</h4>

<div class="quiz-option" data-index="0">@PreDestroy</div>
<div class="quiz-option" data-index="1">@PostConstruct</div>
<div class="quiz-option" data-index="2">@Init</div>
<div class="quiz-option" data-index="3">@AfterCreation</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 4: AOP (Вопросы 25–28) ===== -->

<div class="quiz-question" data-correct="2">
<h4>Вопрос 25. Что такое AOP (Aspect-Oriented Programming)?</h4>

<div class="quiz-option" data-index="0">Парадигма, позволяющая писать асинхронный код через async/await</div>
<div class="quiz-option" data-index="1">Стиль программирования, основанный на массивах и операциях над ними</div>
<div class="quiz-option" data-index="2">Парадигма, выделяющая сквозную функциональность (логирование, транзакции, безопасность) в отдельные модули — аспекты</div>
<div class="quiz-option" data-index="3">Технология обмена данными между сервисами через очереди сообщений</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 26. Какое понятие AOP описывает «конкретную точку выполнения программы, где можно вмешаться»?</h4>

<div class="quiz-option" data-index="0">JoinPoint</div>
<div class="quiz-option" data-index="1">Pointcut</div>
<div class="quiz-option" data-index="2">Advice</div>
<div class="quiz-option" data-index="3">Aspect</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 27. Что такое Pointcut в AOP?</h4>

<div class="quiz-option" data-index="0">Класс, содержащий советы (advice)</div>
<div class="quiz-option" data-index="1">Сам код, выполняемый при срабатывании аспекта</div>
<div class="quiz-option" data-index="2">Точка остановки в отладчике</div>
<div class="quiz-option" data-index="3">Выражение, определяющее, какие JoinPoint'ы будут перехвачены аспектом</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 28. На каких возможностях Spring «под капотом» построен AOP?</h4>

<div class="quiz-option" data-index="0">Только на компиляции байткода через AspectJ</div>
<div class="quiz-option" data-index="1">@Transactional, @PreAuthorize, @Cacheable — все они работают через прокси и AOP</div>
<div class="quiz-option" data-index="2">JDBC и Hibernate ResultSet</div>
<div class="quiz-option" data-index="3">JNI и нативный код</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 5: Spring MVC (Вопросы 29–40) ===== -->

<div class="quiz-question" data-correct="2">
<h4>Вопрос 29. Какие три компонента включает паттерн MVC в Spring?</h4>

<div class="quiz-option" data-index="0">Model, Validator, Controller</div>
<div class="quiz-option" data-index="1">Module, View, Component</div>
<div class="quiz-option" data-index="2">Model, View, Controller</div>
<div class="quiz-option" data-index="3">Manager, Variable, Class</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 30. Чем @RestController отличается от @Controller?</h4>

<div class="quiz-option" data-index="0">@RestController работает только с XML, @Controller — с JSON</div>
<div class="quiz-option" data-index="1">@RestController предназначен для статических ресурсов</div>
<div class="quiz-option" data-index="2">@Controller не поддерживает GET-запросы</div>
<div class="quiz-option" data-index="3">@RestController = @Controller + @ResponseBody на всех методах; возвращаемые значения сериализуются в JSON/XML напрямую в тело ответа</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 31. Какой код корректно объявляет REST-эндпоинт GET /api/students/{id}?</h4>

```java
// Вариант A
@Controller
@RequestMapping("/api/students")
public class StudentController {
    @GetMapping("/{id}")
    public Student getById(int id) { ... }
}

// Вариант B
@RestController
@RequestMapping("/api/students")
public class StudentController {
    @GetMapping("/{id}")
    public Student getById(@PathVariable long id) { ... }
}
```

<div class="quiz-option" data-index="0">Вариант A — @Controller подходит для всех контроллеров</div>
<div class="quiz-option" data-index="1">Вариант B — @RestController сериализует ответ в JSON, @PathVariable извлекает {id} из URL</div>
<div class="quiz-option" data-index="2">Оба варианта эквивалентны</div>
<div class="quiz-option" data-index="3">Ни один — путь нужно задавать через @RequestParam</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 32. Какая аннотация извлекает значение переменной из части пути URL?</h4>

<div class="quiz-option" data-index="0">@PathVariable</div>
<div class="quiz-option" data-index="1">@RequestParam</div>
<div class="quiz-option" data-index="2">@RequestBody</div>
<div class="quiz-option" data-index="3">@PathParam</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 33. Какая аннотация извлекает параметры из строки запроса (после ?)?</h4>

<div class="quiz-option" data-index="0">@PathVariable</div>
<div class="quiz-option" data-index="1">@RequestBody</div>
<div class="quiz-option" data-index="2">@RequestParam</div>
<div class="quiz-option" data-index="3">@QueryString</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 34. Какая аннотация десериализует тело HTTP-запроса (например, JSON) в Java-объект?</h4>

<div class="quiz-option" data-index="0">@PathVariable</div>
<div class="quiz-option" data-index="1">@RequestParam</div>
<div class="quiz-option" data-index="2">@RequestHeader</div>
<div class="quiz-option" data-index="3">@RequestBody</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 35. Какая сокращённая аннотация эквивалентна @RequestMapping(method = RequestMethod.POST)?</h4>

<div class="quiz-option" data-index="0">@GetMapping</div>
<div class="quiz-option" data-index="1">@PostMapping</div>
<div class="quiz-option" data-index="2">@PutMapping</div>
<div class="quiz-option" data-index="3">@DeleteMapping</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 36. Что означает шаблон URL `/admin/**`?</h4>

<div class="quiz-option" data-index="0">Любое количество сегментов пути после /admin/</div>
<div class="quiz-option" data-index="1">Только сегменты, состоящие из звёздочек</div>
<div class="quiz-option" data-index="2">Только корневой путь /admin/</div>
<div class="quiz-option" data-index="3">Только два сегмента после /admin/</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 37. Какой HTTP-статус принято возвращать после успешного POST /api/students, создавшего новую запись?</h4>

<div class="quiz-option" data-index="0">200 OK</div>
<div class="quiz-option" data-index="1">204 No Content</div>
<div class="quiz-option" data-index="2">201 Created</div>
<div class="quiz-option" data-index="3">302 Found</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 38. Какой HTTP-статус возвращают после успешного DELETE без содержимого в ответе?</h4>

<div class="quiz-option" data-index="0">200 OK</div>
<div class="quiz-option" data-index="1">201 Created</div>
<div class="quiz-option" data-index="2">404 Not Found</div>
<div class="quiz-option" data-index="3">204 No Content</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 39. Что делает класс ResponseEntity?</h4>

<div class="quiz-option" data-index="0">Сериализует объекты в формат XML</div>
<div class="quiz-option" data-index="1">Обёртка над HTTP-ответом: позволяет задать статус, заголовки и тело</div>
<div class="quiz-option" data-index="2">Базовый класс всех JPA-сущностей</div>
<div class="quiz-option" data-index="3">Маркерный интерфейс для классов, возвращаемых из контроллера</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 40. Какой код корректно возвращает 404, если студент с таким id не найден?</h4>

```java
// Вариант A
@GetMapping("/{id}")
public ResponseEntity<Student> getById(@PathVariable Long id) {
    Student s = service.findById(id);
    return s != null
        ? ResponseEntity.ok(s)
        : ResponseEntity.notFound().build();
}

// Вариант B
@GetMapping("/{id}")
public Student getById(@PathVariable Long id) {
    return service.findById(id);
}
```

<div class="quiz-option" data-index="0">Вариант A — явная проверка и возврат notFound() при отсутствии</div>
<div class="quiz-option" data-index="1">Вариант B — Spring автоматически возвращает 404 при null</div>
<div class="quiz-option" data-index="2">Оба варианта работают одинаково</div>
<div class="quiz-option" data-index="3">Ни один — нужно бросать исключение NullPointerException</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 6: Spring Data JPA, Thymeleaf, Security (Вопросы 41–50) ===== -->

<div class="quiz-question" data-correct="2">
<h4>Вопрос 41. Что делает интерфейс JpaRepository?</h4>

<div class="quiz-option" data-index="0">Предоставляет только метод save()</div>
<div class="quiz-option" data-index="1">Является внутренней реализацией Hibernate Session</div>
<div class="quiz-option" data-index="2">Расширяет CrudRepository и PagingAndSortingRepository, добавляя сортировку, пагинацию и batch-операции</div>
<div class="quiz-option" data-index="3">Заменяет Spring IoC Container</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 42. Что произойдёт, если объявить в интерфейсе JpaRepository метод `List<Student> findByNameContainingIgnoreCase(String part);`?</h4>

<div class="quiz-option" data-index="0">Spring выбросит исключение во время компиляции</div>
<div class="quiz-option" data-index="1">Spring Data JPA сама сгенерирует реализацию, разобрав имя метода в SQL-запрос с LIKE и LOWER</div>
<div class="quiz-option" data-index="2">Метод вернёт пустой список без выполнения запроса</div>
<div class="quiz-option" data-index="3">Запрос придётся написать вручную через @Query</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 43. Что такое шаблонизатор Thymeleaf?</h4>

<div class="quiz-option" data-index="0">JavaScript-фреймворк для frontend</div>
<div class="quiz-option" data-index="1">Альтернатива Spring Framework</div>
<div class="quiz-option" data-index="2">Расширение SQL для генерации HTML</div>
<div class="quiz-option" data-index="3">Серверный шаблонизатор для Java, поддерживающий Natural Templates (валидный HTML)</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 44. Где Spring Boot ищет шаблоны Thymeleaf по умолчанию?</h4>

<div class="quiz-option" data-index="0">src/main/resources/templates</div>
<div class="quiz-option" data-index="1">src/main/webapp/WEB-INF/views</div>
<div class="quiz-option" data-index="2">src/main/resources/static</div>
<div class="quiz-option" data-index="3">src/main/java/templates</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 45. Какой атрибут Thymeleaf используется для итерации по коллекции?</h4>

<div class="quiz-option" data-index="0">th:for</div>
<div class="quiz-option" data-index="1">th:repeat</div>
<div class="quiz-option" data-index="2">th:each</div>
<div class="quiz-option" data-index="3">th:loop</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 46. Что такое Spring Security?</h4>

<div class="quiz-option" data-index="0">Утилита для шифрования файлов на диске</div>
<div class="quiz-option" data-index="1">Фреймворк для реализации аутентификации, авторизации и защиты от уязвимостей (CSRF, session fixation и др.)</div>
<div class="quiz-option" data-index="2">Расширение JDBC для шифрования SQL-запросов</div>
<div class="quiz-option" data-index="3">Антивирус для проверки артефактов сборки</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 47. Через какой механизм работает Spring Security?</h4>

<div class="quiz-option" data-index="0">Через перехват аннотаций во время компиляции</div>
<div class="quiz-option" data-index="1">Через middleware-обработчик на уровне БД</div>
<div class="quiz-option" data-index="2">Через перехват вызовов методов через JNI</div>
<div class="quiz-option" data-index="3">Через цепочку фильтров SecurityFilterChain, обрабатывающих каждый HTTP-запрос</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 48. Какой код корректно ограничивает метод доступом только для роли ADMIN?</h4>

```java
// Вариант A
@DeleteMapping("/{id}")
@PreAuthorize("hasRole('ADMIN')")
public ResponseEntity<Void> delete(@PathVariable Long id) { ... }

// Вариант B
@DeleteMapping("/{id}")
@Role("ADMIN")
public ResponseEntity<Void> delete(@PathVariable Long id) { ... }
```

<div class="quiz-option" data-index="0">Вариант A — аннотация @PreAuthorize с SpEL-выражением hasRole('ADMIN')</div>
<div class="quiz-option" data-index="1">Вариант B — аннотация @Role существует в Spring Security</div>
<div class="quiz-option" data-index="2">Оба варианта одинаково корректны</div>
<div class="quiz-option" data-index="3">Ни один — ограничения настраиваются только через SecurityFilterChain</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 49. Зачем в Spring Security используется BCryptPasswordEncoder?</h4>

<div class="quiz-option" data-index="0">Для шифрования JWT-токенов</div>
<div class="quiz-option" data-index="1">Для подписания HTTPS-сертификатов</div>
<div class="quiz-option" data-index="2">Для безопасного хеширования паролей с солью; пароли никогда не хранятся в открытом виде</div>
<div class="quiz-option" data-index="3">Для сжатия пользовательских данных перед сохранением в БД</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 50. Как клиент передаёт JWT-токен при обращении к защищённым REST-эндпоинтам?</h4>

<div class="quiz-option" data-index="0">В параметре запроса ?token=...</div>
<div class="quiz-option" data-index="1">В HTTP-заголовке Authorization: Bearer &lt;token&gt;</div>
<div class="quiz-option" data-index="2">В cookie JSESSIONID</div>
<div class="quiz-option" data-index="3">В теле каждого запроса как JSON-поле "token"</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 7: Валидация, DTO, обработка ошибок, транзакции (Вопросы 51–60) ===== -->

<div class="quiz-question" data-correct="2">
<h4>Вопрос 51. Какая аннотация запускает валидацию тела запроса в REST-контроллере?</h4>

<div class="quiz-option" data-index="0">@Validate</div>
<div class="quiz-option" data-index="1">@CheckValid</div>
<div class="quiz-option" data-index="2">@Valid</div>
<div class="quiz-option" data-index="3">@RequestBody автоматически валидирует</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 52. Чем @NotBlank отличается от @NotNull для типа String?</h4>

<div class="quiz-option" data-index="0">Они полностью эквивалентны</div>
<div class="quiz-option" data-index="1">@NotBlank запрещает null, пустую строку и строку только из пробелов; @NotNull запрещает только null</div>
<div class="quiz-option" data-index="2">@NotBlank применяется к коллекциям, @NotNull — к строкам</div>
<div class="quiz-option" data-index="3">@NotBlank проверяет только regex-формат, @NotNull — пустоту</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 53. Какое исключение выбрасывает Spring, когда @Valid-валидация не проходит?</h4>

<div class="quiz-option" data-index="0">MethodArgumentNotValidException</div>
<div class="quiz-option" data-index="1">ValidationException</div>
<div class="quiz-option" data-index="2">BadRequestException</div>
<div class="quiz-option" data-index="3">ConstraintViolationException всегда</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 54. Почему рекомендуется использовать отдельные DTO для REST API, а не возвращать @Entity напрямую?</h4>

<div class="quiz-option" data-index="0">DTO работают быстрее, чем entity</div>
<div class="quiz-option" data-index="1">Spring запрещает возвращать entity из контроллеров</div>
<div class="quiz-option" data-index="2">DTO компактнее, чем entity, и занимают меньше памяти</div>
<div class="quiz-option" data-index="3">DTO защищают от утечки внутренних полей, LazyInitializationException, сцепления API с БД и циклических ссылок</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 55. Чем @RestControllerAdvice отличается от @ControllerAdvice?</h4>

<div class="quiz-option" data-index="0">@RestControllerAdvice работает только с XML, @ControllerAdvice — с JSON</div>
<div class="quiz-option" data-index="1">@RestControllerAdvice устарел и не должен использоваться</div>
<div class="quiz-option" data-index="2">@RestControllerAdvice = @ControllerAdvice + @ResponseBody; возвращаемое значение сериализуется в JSON</div>
<div class="quiz-option" data-index="3">@ControllerAdvice не поддерживает @ExceptionHandler</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 56. Какой код корректно обрабатывает MethodArgumentNotValidException?</h4>

```java
// Вариант A
@Controller
public class ValidationHandler {
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public String handle() {
        return "error";
    }
}

// Вариант B
@RestControllerAdvice
public class GlobalExceptionHandler {
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ErrorResponse> handleValidation(
            MethodArgumentNotValidException ex,
            HttpServletRequest request) {
        // собираем fieldErrors и возвращаем 400
        ...
    }
}
```

<div class="quiz-option" data-index="0">Вариант A — @Controller подходит для глобальной обработки</div>
<div class="quiz-option" data-index="1">Вариант B — @RestControllerAdvice глобально обрабатывает исключения и возвращает JSON</div>
<div class="quiz-option" data-index="2">Оба варианта одинаково корректны</div>
<div class="quiz-option" data-index="3">Ни один — нужно использовать try/catch в каждом контроллере</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 57. Где правильно ставить @Transactional?</h4>

<div class="quiz-option" data-index="0">На сервисном слое — там, где заключается бизнес-логика и единица работы с БД</div>
<div class="quiz-option" data-index="1">На контроллере — для удобства, чтобы транзакция держалась всё время обработки запроса</div>
<div class="quiz-option" data-index="2">На репозитории — JpaRepository требует явного @Transactional</div>
<div class="quiz-option" data-index="3">На главном классе приложения, чтобы применить ко всем методам</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 58. Почему @Transactional на private-методе не работает?</h4>

<div class="quiz-option" data-index="0">Java запрещает аннотации на private-методах</div>
<div class="quiz-option" data-index="1">Это работает, но только в режиме отладки</div>
<div class="quiz-option" data-index="2">Spring AOP создаёт прокси, который перехватывает только публичные методы; вызовы private обходят прокси</div>
<div class="quiz-option" data-index="3">PrivateTransactionManager не входит в стандартный Spring</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 59. Что произойдёт при self-invocation @Transactional-метода (вызове через this.method() из того же класса)?</h4>

```java
@Service
public class StudentService {
    public void outer() {
        this.inner();   // вызываем @Transactional-метод
    }

    @Transactional
    public void inner() { /* ... */ }
}
```

<div class="quiz-option" data-index="0">Транзакция корректно создаётся для inner()</div>
<div class="quiz-option" data-index="1">Транзакция НЕ создаётся, потому что вызов идёт через this, минуя Spring-прокси</div>
<div class="quiz-option" data-index="2">Spring выбросит исключение во время компиляции</div>
<div class="quiz-option" data-index="3">Транзакция создаётся для outer(), а не для inner()</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 60. При каких исключениях по умолчанию откатывается транзакция, помеченная @Transactional?</h4>

<div class="quiz-option" data-index="0">При любом исключении, включая checked</div>
<div class="quiz-option" data-index="1">Только при ошибках БД (SQLException)</div>
<div class="quiz-option" data-index="2">Транзакция никогда не откатывается автоматически — нужно вызывать rollback() вручную</div>
<div class="quiz-option" data-index="3">Только при unchecked-исключениях (RuntimeException и Error); для checked-исключений нужно явно указать rollbackFor</div>
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
    'Вопрос 1': 'IoC (Inversion of Control) — принцип проектирования, при котором управление жизненным циклом объектов и их взаимодействием передаётся внешнему фреймворку или контейнеру. Реализует «голливудский принцип»: фреймворк сам вызывает ваш код, а не наоборот.',
    'Вопрос 2': 'Dependency Injection (DI) — конкретная техника реализации IoC: объект не создаёт сам свои зависимости, а получает их извне (от контейнера) через конструктор, сеттер или поле.',
    'Вопрос 3': 'Spring поддерживает три способа DI: через конструктор (Constructor Injection), через сеттер (Setter Injection) и через поле (Field Injection). Все три механизма доступны, но не равноценны.',
    'Вопрос 4': 'Конструкторное внедрение — рекомендуемый способ: позволяет сделать поле final, гарантирует, что зависимости заданы при создании объекта, и упрощает юнит-тестирование без Spring-контекста.',
    'Вопрос 5': 'Конструкторное внедрение (вариант B) предпочтительнее: оно делает зависимости явными в сигнатуре конструктора, позволяет финализировать поле и удобнее всего для тестов.',
    'Вопрос 6': 'Field Injection считается плохой практикой: нельзя сделать поле final, зависимости не видны в сигнатуре класса, тестирование без Spring-контекста требует рефлексии. Многие линтеры выдают предупреждение.',
    'Вопрос 7': 'Голливудский принцип «не вызывай нас — мы сами тебя позовём» — это описание Inversion of Control. Фреймворк управляет жизненным циклом ваших объектов, а не наоборот.',
    'Вопрос 8': 'При двух реализациях интерфейса с @Service Spring не знает, какую выбрать, и выбрасывает NoUniqueBeanDefinitionException. Решения: @Primary, @Qualifier или внедрение List<Service>.',
    'Вопрос 9': 'Spring Framework — универсальный open-source фреймворк для Java, упрощающий разработку корпоративных приложений. Основан на IoC и DI, работает с обычными POJO без обязательного наследования.',
    'Вопрос 10': 'Spring Boot — это расширение Spring Framework, упрощающее запуск самостоятельных приложений: автоконфигурация, встроенные серверы (Tomcat/Jetty), starter-модули, минимум XML.',
    'Вопрос 11': '@SpringBootApplication — основная аннотация Spring Boot, которая включает автоконфигурацию, сканирование компонентов и регистрацию класса как @Configuration.',
    'Вопрос 12': '@SpringBootApplication — это композиционная аннотация: она включает @Configuration (регистрация бинов), @EnableAutoConfiguration (автоконфигурация по classpath) и @ComponentScan (поиск @Component-классов).',
    'Вопрос 13': 'Spring Initializr (start.spring.io) — веб-сервис для генерации стартового шаблона Spring Boot проекта с выбором языка, версии Spring Boot, зависимостей и системы сборки.',
    'Вопрос 14': 'Starter — специальная зависимость в pom.xml, которая подключает группу связанных библиотек с согласованными версиями. Например, spring-boot-starter-web подключает Spring MVC, Jackson, Tomcat и др.',
    'Вопрос 15': 'spring-boot-starter-web подключает Spring MVC, Jackson (JSON), Tomcat (встроенный сервер) и всё необходимое для разработки веб-приложений и REST API.',
    'Вопрос 16': 'spring-boot-starter-parent (или BOM) централизованно задаёт версии всех зависимостей Spring Boot, что предотвращает конфликты и обеспечивает совместимость библиотек.',
    'Вопрос 17': 'Spring IoC Container — ядро Spring: создаёт бины, внедряет зависимости, управляет их жизненным циклом. Реализован через интерфейсы BeanFactory и ApplicationContext.',
    'Вопрос 18': 'ApplicationContext — наследник BeanFactory, добавляющий поддержку интернационализации (i18n), событий ApplicationEvent, ресурсов и интеграцию с Spring AOP. В современных приложениях используют именно его.',
    'Вопрос 19': 'Spring Bean — это объект, создаваемый, настраиваемый и управляемый Spring IoC Container'+"'"+'ом. Бины определяются через аннотации (@Component и др.), @Bean-методы или XML.',
    'Вопрос 20': 'По умолчанию бины в Spring — singleton: на весь контейнер существует один экземпляр. Другие scope: prototype, request, session, application.',
    'Вопрос 21': '@Component, @Service, @Repository, @Controller, @RestController — стереотипные аннотации, при сканировании пакетов превращающие класс в Spring Bean. Все они — специализации @Component.',
    'Вопрос 22': 'Для контейнера @Service/@Repository/@Component функционально почти равнозначны, но несут семантику: @Service — бизнес-логика, @Repository — DAO (плюс перехват исключений в DataAccessException), @Controller — слой контроллеров.',
    'Вопрос 23': 'Метод с @Bean внутри класса с @Configuration возвращает объект, который Spring регистрирует как бин. Это способ создавать бины из «не своих» классов (например, PasswordEncoder).',
    'Вопрос 24': '@PostConstruct (из jakarta.annotation) вызывается после создания бина и внедрения зависимостей — удобно для инициализационной логики (например, заполнения тестовых данных).',
    'Вопрос 25': 'AOP (Aspect-Oriented Programming) — парадигма, отделяющая сквозную функциональность (логирование, транзакции, безопасность) от бизнес-логики в отдельные модули — аспекты.',
    'Вопрос 26': 'JoinPoint — конкретная точка выполнения программы (обычно вызов метода), где можно «врезаться» дополнительной логикой через аспект.',
    'Вопрос 27': 'Pointcut — выражение (часто на AspectJ-синтаксисе), определяющее множество JoinPoint'+"'"+'ов, которые будут перехвачены. Например: execution(* com.example.service.*.*(..)).',
    'Вопрос 28': 'Многие фундаментальные возможности Spring построены на AOP: @Transactional оборачивает методы в транзакцию, @PreAuthorize — в проверку прав, @Cacheable — в кеширование. Всё это работает через прокси.',
    'Вопрос 29': 'MVC (Model–View–Controller): Model — бизнес-данные и логика (Entity/Service); View — отображение (HTML/Thymeleaf/JSON); Controller — обработка HTTP-запросов и координация.',
    'Вопрос 30': '@RestController = @Controller + @ResponseBody на всех методах. Возвращаемые значения автоматически сериализуются в JSON/XML и записываются в тело HTTP-ответа. Подходит для REST API.',
    'Вопрос 31': 'Вариант B корректен: @RestController автоматически возвращает JSON, @PathVariable извлекает значение {id} из URL и присваивает параметру метода.',
    'Вопрос 32': '@PathVariable извлекает переменные из части URL-пути. Например, для /students/{id} аннотация @PathVariable Long id даст значение id из URL.',
    'Вопрос 33': '@RequestParam извлекает параметры из строки запроса URL (после знака ?). Например, /students?genre=Drama → @RequestParam String genre. Поддерживает defaultValue и required.',
    'Вопрос 34': '@RequestBody десериализует тело HTTP-запроса (обычно JSON) в Java-объект через Jackson. Используется для POST/PUT-эндпоинтов, принимающих сущность от клиента.',
    'Вопрос 35': '@PostMapping — сокращение для @RequestMapping(method = RequestMethod.POST). Аналогично есть @GetMapping, @PutMapping, @DeleteMapping, @PatchMapping.',
    'Вопрос 36': '`**` означает любое количество сегментов пути. `/admin/**` сопоставится с /admin/, /admin/users, /admin/users/5 и т.д. `*` — один сегмент.',
    'Вопрос 37': '201 Created — стандартный HTTP-статус для успешного создания нового ресурса через POST. Часто сопровождается заголовком Location с URL созданного ресурса.',
    'Вопрос 38': '204 No Content — стандартный HTTP-статус для успешного запроса, который не возвращает тело ответа (например, DELETE или некоторые PUT).',
    'Вопрос 39': 'ResponseEntity<T> — это обёртка над HTTP-ответом, позволяющая контроллеру задавать статус, заголовки и тело: ResponseEntity.ok(...), .notFound().build(), .status(HttpStatus.CREATED).body(...).',
    'Вопрос 40': 'Вариант A — правильный паттерн: явная проверка null и возврат ResponseEntity.notFound().build() для 404. Spring не возвращает 404 автоматически при null.',
    'Вопрос 41': 'JpaRepository<T, ID> расширяет CrudRepository (save, findById, findAll, delete, count, exists) и PagingAndSortingRepository (Sort, Pageable), добавляя saveAll, deleteInBatch, flush и др.',
    'Вопрос 42': 'Spring Data JPA парсит имя метода и сама генерирует SQL-запрос. findByNameContainingIgnoreCase превратится в WHERE LOWER(name) LIKE LOWER(?), реализацию писать не нужно.',
    'Вопрос 43': 'Thymeleaf — серверный шаблонизатор для Java. Главная особенность — Natural Templates: шаблон остаётся валидным HTML, что позволяет дизайнерам открывать его в браузере без запуска приложения.',
    'Вопрос 44': 'Spring Boot ищет шаблоны Thymeleaf в src/main/resources/templates/. Статические ресурсы (CSS, JS, картинки) — в src/main/resources/static/.',
    'Вопрос 45': 'th:each — атрибут Thymeleaf для итерации по коллекции, аналог for-each. Пример: <tr th:each="s : ${students}">. Внутри доступна переменная s.',
    'Вопрос 46': 'Spring Security — мощный фреймворк для аутентификации (кто пользователь) и авторизации (что ему разрешено). Из коробки даёт защиту от CSRF, session fixation, clickjacking и других уязвимостей.',
    'Вопрос 47': 'Spring Security перехватывает каждый HTTP-запрос через SecurityFilterChain — цепочку фильтров, отвечающих за аутентификацию, проверку прав, защиту от CSRF и др.',
    'Вопрос 48': '@PreAuthorize("hasRole(\'ADMIN\')") — аннотация защиты на уровне метода: Spring проверяет SpEL-выражение перед вызовом. Требует @EnableMethodSecurity в конфигурации.',
    'Вопрос 49': 'BCryptPasswordEncoder использует алгоритм BCrypt: пароль хешируется с автоматической солью. Пароли в БД хранятся в виде хеша, исходное значение невозможно восстановить.',
    'Вопрос 50': 'JWT передаётся в HTTP-заголовке Authorization в формате "Bearer <token>". Фильтр JwtAuthenticationFilter извлекает токен, валидирует подпись и устанавливает аутентификацию в SecurityContextHolder.',
    'Вопрос 51': '@Valid — стандартная аннотация Bean Validation, запускающая проверку аннотаций (@NotBlank, @Size и др.) на объекте, помеченном @RequestBody. Без @Valid аннотации на DTO игнорируются.',
    'Вопрос 52': '@NotNull запрещает только значение null. @NotBlank (для String) запрещает null, пустую строку "" и строку, состоящую только из whitespace ("   "). Также есть @NotEmpty — для String, Collection, Map, Array — запрещает null и пустоту, но допускает строку из пробелов.',
    'Вопрос 53': 'При непрошедшей валидации @Valid @RequestBody Spring выбрасывает MethodArgumentNotValidException. Информация о полях с ошибками доступна через ex.getBindingResult().getFieldErrors(). Без обработчика клиент получит 400 с мусорным телом — обрабатывайте через @RestControllerAdvice.',
    'Вопрос 54': 'Возврат entity напрямую опасен: (1) утечка внутренних полей (password и т.п.), (2) LazyInitializationException при сериализации lazy-связей вне транзакции, (3) сцепление API с моделью БД — любое переименование ломает клиентов, (4) циклические ссылки в JSON.',
    'Вопрос 55': '@RestControllerAdvice = @ControllerAdvice + @ResponseBody. Применяется для REST API: возвращаемые значения автоматически сериализуются в JSON. @ControllerAdvice без @ResponseBody возвращает имя представления (для Thymeleaf/JSP).',
    'Вопрос 56': 'Вариант B — стандартный паттерн обработки ошибок валидации: @RestControllerAdvice глобально перехватывает MethodArgumentNotValidException, собирает поля с ошибками через getBindingResult() и возвращает структурированный ResponseEntity с кодом 400.',
    'Вопрос 57': '@Transactional ставится на сервисном слое (бизнес-логика и атомарность операций). Не на контроллере — иначе транзакция держится во время сериализации JSON, удлиняя блокировки. Не на репозитории — JpaRepository уже сам управляет транзакциями на уровне отдельных методов.',
    'Вопрос 58': 'Spring AOP реализован через прокси: вокруг бина создаётся подкласс или CGLIB-прокси, перехватывающий ТОЛЬКО публичные методы. Private-методы вызываются напрямую и обходят прокси, поэтому @Transactional на них игнорируется (то же касается final-методов).',
    'Вопрос 59': 'При self-invocation вызов идёт через this, минуя прокси. Поэтому AOP-аспекты (@Transactional, @Cacheable, @PreAuthorize и т.д.) не срабатывают. Решения: внедрить сервис в самого себя через провайдер/ApplicationContext, или вынести inner-метод в отдельный бин.',
    'Вопрос 60': 'По умолчанию Spring откатывает транзакцию только при unchecked-исключениях (RuntimeException, Error). Checked-исключения (IOException и т.д.) НЕ вызывают откат — транзакция коммитится! Для отката на checked используйте @Transactional(rollbackFor = Exception.class).'
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
