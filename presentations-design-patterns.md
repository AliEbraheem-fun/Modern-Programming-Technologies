# Темы презентаций: Паттерны проектирования

Данный раздел содержит темы групповых презентаций, посвящённых классическим паттернам проектирования (GoF) и связанным архитектурным концепциям. Каждая тема рассчитана на группу из 2–3 студентов.

---

## Общая информация

| Параметр | Значение |
|----------|----------|
| **Формат работы** | Групповая презентация (2–3 человека) |
| **Продолжительность выступления** | 10-15 минут |
| **Количество слайдов** | 15–25 слайдов |
| **Язык презентации** | Русский |
| **Формат файла** | PDF или PPTX |

> **Важно:** Все участники группы должны принимать участие в выступлении и быть готовы ответить на вопросы по любой части презентации.

---

## Требования к презентации

- Презентация **обязательно должна содержать примеры кода на двух языках — C++ и Java** (для каждого паттерна приводится пара эквивалентных реализаций, чтобы показать различия в идиомах: шаблоны и RAII в C++ vs generics и GC в Java; использование стандартной библиотеки STL vs JDK)
- Студент должен **чётко объяснить сценарии применения паттерна**: конкретные задачи и контексты, в которых паттерн уместен; признаки, указывающие на необходимость его применения; когда паттерн **не следует** использовать (over-engineering); реальные примеры из промышленных библиотек и фреймворков (STL, Boost, Qt — для C++; JDK, Spring, Hibernate — для Java)
- Для каждого паттерна обязательно раскрыть: **назначение**, **структуру**, **участников**, **применимость**, **плюсы и минусы**
- Рекомендуется показать **анти-пример** (код без паттерна) и **рефакторинг** к целевому паттерну

> **Внимание:** Использование мобильного телефона во время выступления, а также чтение текста со слайдов, распечаток или сторонних источников без демонстрации реального понимания материала будет приводить к **снижению оценки**. Оценивается именно владение темой: умение отвечать на вопросы, объяснять код своими словами и обосновывать выбор паттерна в конкретном сценарии.

---

## Темы презентаций

| № | Тема |
|:-:|------|
| 1 | **Singleton** (Одиночка) |
| 2 | **Factory Method и Abstract Factory** (Фабричный метод и Абстрактная фабрика) |
| 3 | **Builder и Prototype** (Строитель и Прототип) |
| 4 | **Adapter и Bridge** (Адаптер и Мост) |
| 5 | **Composite и Decorator** (Компоновщик и Декоратор) |
| 6 | **Facade и Proxy** (Фасад и Заместитель) |
| 7 | **Flyweight** (Приспособленец) |
| 8 | **Observer** (Наблюдатель) |
| 9 | **Strategy и State** (Стратегия и Состояние) |
| 10 | **Command и Chain of Responsibility** (Команда и Цепочка обязанностей) |
| 11 | **Template Method и Iterator** (Шаблонный метод и Итератор) |
| 12 | **Mediator и Memento** (Посредник и Снимок) |
| 13 | **Visitor** (Посетитель) |
| 14 | **Архитектурные паттерны: MVC, MVP, MVVM** |
| 15 | **Dependency Injection и Inversion of Control** |
| 16 | **SOLID, GRASP и антипаттерны проектирования** |
| 17 | **Repository и Unit of Work** (Корпоративные паттерны доступа к данным) |
| 18 | **Паттерны многопоточности** (Concurrency Patterns) |

---

## Распределение тем

| № | Тема | Группа | Участники | Дата выступления |
|:-:|------|--------|-----------|:----------------:|
| 1 | Singleton | — | — | — |
| 2 | Factory Method и Abstract Factory | — | — | — |
| 3 | Builder и Prototype | — | — | — |
| 4 | Adapter и Bridge | — | — | — |
| 5 | Composite и Decorator | — | — | — |
| 6 | Facade и Proxy | — | — | — |
| 7 | Flyweight | — | — | — |
| 8 | Observer | — | — | — |
| 9 | Strategy и State | — | — | — |
| 10 | Command и Chain of Responsibility | — | — | — |
| 11 | Template Method и Iterator | — | — | — |
| 12 | Mediator и Memento | — | — | — |
| 13 | Visitor | — | — | — |
| 14 | Архитектурные паттерны: MVC, MVP, MVVM | — | — | — |
| 15 | Dependency Injection и Inversion of Control | — | — | — |
| 16 | SOLID, GRASP и антипаттерны проектирования | — | — | — |
| 17 | Repository и Unit of Work | — | — | — |
| 18 | Паттерны многопоточности | — | — | — |

> **Порядок выбора:** Темы выбираются в порядке очереди. Каждая тема может быть выбрана только одной группой. Для регистрации темы обратитесь к преподавателю.

---

## Полезные ресурсы

### Книги

- **Design Patterns: Elements of Reusable Object-Oriented Software** — Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides (GoF, 1994) — классическая книга-первоисточник
- **Head First Design Patterns** — Eric Freeman, Elisabeth Robson (2nd Edition) — наглядное введение с примерами на Java
- **Effective Java** — Joshua Bloch (3rd Edition) — идиоматические паттерны в Java (Items 1–9 особенно актуальны)
- **Refactoring: Improving the Design of Existing Code** — Martin Fowler (2nd Edition) — рефакторинги, ведущие к паттернам
- **Patterns of Enterprise Application Architecture** — Martin Fowler — архитектурные паттерны (Repository, Unit of Work, MVC и др.)
- **Clean Code** и **Clean Architecture** — Robert C. Martin — SOLID и архитектурные принципы

### Онлайн-ресурсы

- [Refactoring Guru — Design Patterns](https://refactoring.guru/design-patterns) — каталог паттернов с примерами на Java (есть русская версия)
- [SourceMaking — Design Patterns](https://sourcemaking.com/design_patterns) — подробное описание паттернов GoF
- [Java Design Patterns (iluwatar)](https://java-design-patterns.com/) — открытая коллекция реализаций паттернов на Java (GitHub: iluwatar/java-design-patterns)
- [Baeldung — Design Patterns](https://www.baeldung.com/design-patterns-series) — статьи по паттернам и их применению в Spring/Java EE
- [Martin Fowler's Blog](https://martinfowler.com/) — статьи по архитектуре и паттернам
- [Spring Framework Reference](https://docs.spring.io/spring-framework/reference/) — живые примеры DI, Proxy, Template Method и других паттернов
