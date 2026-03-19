# Лекция 5: Коллекции, Потоки ввода/вывода и Многопоточность

## Введение

Добро пожаловать на пятую лекцию курса "Современные технологии программирования". На предыдущих лекциях мы изучили основы Java, классы, объектно-ориентированное программирование и обработку ошибок. Сегодня мы сделаем большой шаг вперёд и познакомимся сразу с тремя важнейшими темами, без которых невозможно представить реальную Java-разработку: **коллекции** (как хранить и обрабатывать данные гибко и эффективно), **потоки ввода/вывода** (как читать и записывать файлы) и **многопоточность** (как выполнять несколько задач одновременно). Эти темы тесно связаны друг с другом — например, потокобезопасные коллекции объединяют знания из первой и третьей частей, а Stream API позволяет обрабатывать данные из файлов в функциональном стиле.

---

## Часть 1: Коллекции (Java Collections Framework)

Начнём с фундаментальной темы — коллекций. Если вы уже работали с массивами, то наверняка замечали их главное ограничение: размер массива фиксирован. Давайте разберём, как Java решает эту проблему.

### 1.1 Зачем нужны коллекции?

Массивы в Java имеют фиксированный размер. Для динамических наборов данных нужны более гибкие структуры — **коллекции**.

**Аналогия:** Массив — это книжная полка фиксированного размера: купили полку на 10 книг — больше не поставишь, даже если очень хочется. Список (List) — это резиновая полка, которая растёт по мере добавления книг. Множество (Set) — это стопка уникальных книг, где дубликатов нет: попробуйте положить ту же книгу — она просто не добавится. А словарь (Map) — это каталог библиотеки, где по коду книги можно мгновенно найти её на полке.

### 1.2 Иерархия интерфейсов

Прежде чем использовать коллекции, важно понять их архитектуру. Обратите внимание, что `Map` стоит отдельно — он не наследует `Collection`, потому что хранит пары ключ-значение, а не отдельные элементы.

```
Iterable<E>
└── Collection<E>
    ├── List<E>              — Упорядоченный список с дубликатами
    │   ├── ArrayList
    │   ├── LinkedList
    │   └── Vector (устарел)
    │
    ├── Set<E>               — Множество без дубликатов
    │   ├── SortedSet<E>     — Отсортированное множество
    │   │   └── NavigableSet<E>
    │   │       └── TreeSet
    │   ├── HashSet
    │   └── LinkedHashSet
    │
    └── Queue<E>             — Очередь FIFO
        ├── BlockingQueue<E> — Потокобезопасная очередь с блокировкой
        ├── Deque<E>         — Двусторонняя очередь
        │   ├── ArrayDeque
        │   └── LinkedList   — Реализует и List, и Deque
        └── PriorityQueue

Map<K, V>                   — Ключ-значение (не Collection!)
├── SortedMap<K,V>           — Отсортированная Map
│   └── NavigableMap<K,V>
│       └── TreeMap
├── HashMap
├── LinkedHashMap
└── Hashtable (устарел)
```

**Абстрактные базовые классы** (`AbstractList`, `AbstractSet`, `AbstractMap` и др.) упрощают создание собственных коллекций — достаточно реализовать лишь несколько ключевых методов вместо всего интерфейса.

**Правило именования реализаций:** классы-реализации обычно называются по схеме `<СтильРеализации><Интерфейс>`:

| Стиль реализации | Set | List | Deque | Map |
|---|---|---|---|---|
| Hash Table | `HashSet` | — | — | `HashMap` |
| Resizable Array | — | `ArrayList` | `ArrayDeque` | — |
| Balanced Tree | `TreeSet` | — | — | `TreeMap` |
| Linked List | — | `LinkedList` | `LinkedList` | — |
| Hash Table + Linked List | `LinkedHashSet` | — | — | `LinkedHashMap` |

### 1.3 Реализации и их характеристики

Вы могли заметить, что реализаций довольно много. Как выбрать нужную? Следующая таблица поможет вам сориентироваться — обращайте внимание на колонку "Когда использовать":

| Класс | Упорядочен? | Дубликаты | Null? | Thread-safe? | Когда использовать |
|-------|:-----------:|:---------:|:-----:|:------------:|-------------------|
| `ArrayList` | Да (по индексу) | Да | Да | Нет | Частый доступ по индексу |
| `LinkedList` | Да | Да | Да | Нет | Частые вставки/удаления |
| `HashSet` | Нет | Нет | 1 null | Нет | Быстрая проверка наличия |
| `LinkedHashSet` | Да (вставки) | Нет | 1 null | Нет | Уникальные + порядок вставки |
| `TreeSet` | Да (по знач.) | Нет | Нет | Нет | Уникальные + сортировка |
| `HashMap` | Нет | Нет (ключи) | 1 null ключ | Нет | Быстрый поиск по ключу |
| `LinkedHashMap` | Да (вставки) | Нет | Да | Нет | Порядок вставки + ключ-значение |
| `TreeMap` | Да (по ключу) | Нет | Нет | Нет | Сортированные ключи |
| `PriorityQueue` | Нет (heap) | Да | Нет | Нет | Приоритетная очередь |
| `ArrayDeque` | Да | Да | Нет | Нет | Стек/двусторонняя очередь |

### 1.4 Примеры использования основных коллекций

Теперь давайте посмотрим, как эти коллекции выглядят на практике. Начнём с самых часто используемых.

#### List — упорядоченный список

```java
List<String> list = new ArrayList<>();
list.add("Java");
list.add("Python");
list.add("C++");

System.out.println("List: " + list);
```

#### Set — множество без дубликатов

```java
List<String> list = new ArrayList<>();
list.add("Java");
list.add("Python");
list.add("C++");

Set<String> set = new HashSet<>(list);

System.out.println("Set: " + set);
```

#### Map — ключ-значение

```java
Map<String, Integer> map = new HashMap<>();
map.put("Apple", 3);
map.put("Banana", 5);
map.put("Orange", 2);

System.out.println("Map: " + map);
```

#### Queue/Deque — очередь

```java
// Очередь FIFO (первый пришёл — первый вышел)
Queue<String> queue = new LinkedList<>();
queue.offer("первый");
queue.offer("второй");
queue.offer("третий");

System.out.println(queue.peek());  // первый (без удаления)
System.out.println(queue.poll());  // первый (удаляет)
System.out.println(queue.poll());  // второй

// PriorityQueue — реализована на основе мин-кучи (min-heap),
// выдаёт элемент с наименьшим приоритетом первым
PriorityQueue<Integer> pq = new PriorityQueue<>();
pq.offer(5); pq.offer(1); pq.offer(3);
while (!pq.isEmpty()) {
    System.out.print(pq.poll() + " "); // 1 3 5
}
```

### 1.5 Потокобезопасные (Concurrent) коллекции

Обычные коллекции **не безопасны** для использования из нескольких потоков одновременно. Для этого есть специальные реализации:

```java
// Синхронизированные коллекции через Collections.synchronizedXXX()
List<String> syncList = Collections.synchronizedList(new ArrayList<>());
syncList.add("A");
syncList.add("B");

// Важно: при итерации нужна ручная синхронизация
synchronized (syncList) {
    for (String s : syncList) {
        System.out.println(s);
    }
}

// Конкурентные коллекции из java.util.concurrent
CopyOnWriteArrayList<String> cowList = new CopyOnWriteArrayList<>();
cowList.add("X");
cowList.add("Y");

ConcurrentHashMap<String, Integer> cmap = new ConcurrentHashMap<>();
cmap.put("Java", 10);
cmap.put("Python", 20);

System.out.println("CopyOnWriteArrayList: " + cowList);
System.out.println("ConcurrentHashMap: " + cmap);
```

### 1.6 Итерация и сортировка

Давайте разберём, как обходить коллекции и сортировать их. Это одна из самых частых операций в повседневной работе.

```java
List<String> names = Arrays.asList("Anna", "John", "Bella", "Mike");

System.out.println("Original:");
for (String name : names) {
    System.out.println(name);
}

List<String> sorted = new ArrayList<>(names);
Collections.sort(sorted);
System.out.println("Sorted: " + sorted);

sorted.sort(Comparator.reverseOrder());
System.out.println("Reverse sorted: " + sorted);
```

#### Comparable и Comparator

Это важный момент: в Java есть два способа задать порядок сортировки. `Comparable` — когда объект сам знает, как себя сравнивать. `Comparator` — когда логику сравнения определяет внешний код. Используйте `Comparable` для "естественного" порядка (например, студенты по оценке), а `Comparator` — для альтернативных вариантов (по имени, по факультету и т.д.).

```java
// Comparable — объект "знает" как сравнить себя с другим
class Student implements Comparable<Student> {
    String name;
    int grade;

    @Override
    public int compareTo(Student other) {
        return Integer.compare(this.grade, other.grade); // Сортировка по оценке
    }
}

List<Student> students = ...;
Collections.sort(students); // Использует compareTo

// Comparator — внешняя стратегия сравнения
students.sort(Comparator.comparing(s -> s.name));  // По имени
students.sort(Comparator.comparingInt((Student s) -> s.grade).reversed()); // По оценке убыв.
students.sort(Comparator.comparing((Student s) -> s.name).thenComparingInt(s -> s.grade));
```

### 1.7 Stream API

Stream API (Java 8+) позволяет обрабатывать коллекции в функциональном стиле. Вместо того чтобы писать циклы вручную, вы описываете *что* нужно сделать с данными, а не *как* — фильтровать, преобразовывать, собирать результат:

```java
List<Integer> numbers = Arrays.asList(2, 3, 6, 7, 8, 10);

List<Integer> evenSquares = numbers.stream()
        .filter(n -> n % 2 == 0)
        .map(n -> n * n)
        .collect(Collectors.toList());

System.out.println("Even squares: " + evenSquares);
```

---

## Часть 2: Потоки ввода/вывода (I/O Streams)

Теперь перейдём от работы с данными в памяти к работе с внешним миром — файлами, сетью и другими источниками данных. Обратите внимание: слово "поток" здесь означает не поток выполнения (thread), а поток данных (stream) — последовательность байтов или символов, которую можно читать или записывать.

### 2.1 Архитектура I/O в Java

В Java все операции ввода/вывода строятся на **потоках (streams)**. Есть два типа:

| | Байтовые потоки | Символьные потоки |
|---|---|---|
| Базовые классы | `InputStream` / `OutputStream` | `Reader` / `Writer` |
| Единица данных | 1 байт | 1 символ (char, 2 байта) |
| Назначение | Бинарные данные (изображения, архивы) | Текстовые данные |

### 2.2 Байтовые потоки

```
InputStream (абстрактный)
├── FileInputStream      — Чтение из файла
├── ByteArrayInputStream — Чтение из массива байт (из памяти)
├── BufferedInputStream  — Буферизированное чтение (ускоряет)
└── DataInputStream      — Чтение примитивных типов
+ System.in             — Стандартный ввод (клавиатура), тип InputStream

OutputStream (абстрактный)
├── FileOutputStream     — Запись в файл
├── ByteArrayOutputStream — Запись в массив байт (в память)
├── BufferedOutputStream
├── DataOutputStream
└── PrintStream          — Форматированный вывод (printf, println)
+ System.out / System.err — Стандартный вывод / вывод ошибок (консоль), тип PrintStream
```

```java
// Запись байтов в файл
try (FileOutputStream fos = new FileOutputStream("bytes.bin")) {
    fos.write(new byte[]{1, 2, 3, 4});
}

// Чтение байтов из файла
try (FileInputStream fis = new FileInputStream("bytes.bin")) {
    int b;
    System.out.print("Прочитанные байты: ");
    while ((b = fis.read()) != -1) {
        System.out.print(b + " ");
    }
    System.out.println();
}
```

### 2.3 Символьные потоки

Для работы с текстовыми данными байтовых потоков недостаточно — нужно учитывать кодировку символов. Именно для этого существуют символьные потоки.

```
Reader (абстрактный)
├── FileReader           — Чтение текстового файла
├── StringReader         — Чтение из строки
├── BufferedReader       — Буферизированное + readLine()
└── InputStreamReader    — Мост: байты -> символы

Writer (абстрактный)
├── FileWriter           — Запись в текстовый файл
├── StringWriter
├── BufferedWriter       — Буферизированное + newLine()
└── PrintWriter          — printf(), println()
```

```java
// Запись текста в файл (символьный поток)
try (FileWriter writer = new FileWriter("text.txt")) {
    writer.write("Привет, мир!");
}

// Чтение текста из файла
try (FileReader reader = new FileReader("text.txt")) {
    int c;
    System.out.print("Прочитанный текст: ");
    while ((c = reader.read()) != -1) {
        System.out.print((char) c);
    }
    System.out.println();
}

// Буферизированная запись
try (BufferedWriter bw = new BufferedWriter(new FileWriter("buffered.txt"))) {
    bw.write("Первая строка");
    bw.newLine();
    bw.write("Вторая строка");
}

// Буферизированное чтение построчно
try (BufferedReader br = new BufferedReader(new FileReader("buffered.txt"))) {
    String line;
    System.out.println("Содержимое файла:");
    while ((line = br.readLine()) != null) {
        System.out.println(line);
    }
}
```

### 2.4 Объектная сериализация

А что, если нужно сохранить в файл не просто текст или байты, а целый объект со всеми его полями? Для этого в Java есть механизм сериализации. Достаточно реализовать интерфейс `Serializable`, и объект можно записать в поток и прочитать обратно:

```java
// Сохранение объекта в файл:
class Person implements Serializable {
    private String name;
    private int age;
    // ...
}

// Запись:
try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("person.dat"))) {
    oos.writeObject(new Person("Иван", 25));
}

// Чтение:
try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream("person.dat"))) {
    Person p = (Person) ois.readObject();
    System.out.println(p.getName() + ", " + p.getAge());
}
```

### 2.5 NIO.2 (Java 7+) — современный API файловой системы

Классический I/O хорошо справляется со своими задачами, но в Java 7 появился более удобный и мощный API для работы с файловой системой — NIO.2. Давайте посмотрим, как он упрощает типичные операции:

```java
import java.nio.file.*;

// Создание пути:
Path path = Path.of("src", "main", "data.txt");
Path absolute = path.toAbsolutePath();

// Операции с файлами:
Files.createDirectories(Path.of("output/logs"));
Files.copy(source, target, StandardCopyOption.REPLACE_EXISTING);
Files.delete(path);
Files.move(source, target);

// Проверки:
Files.exists(path);
Files.isDirectory(path);
Files.size(path);

// Обход дерева файлов:
Files.walk(Path.of("src"))
    .filter(p -> p.toString().endsWith(".java"))
    .forEach(System.out::println);
```

---

## Часть 3: Многопоточность (Multithreading)

Мы научились хранить данные в коллекциях и работать с файлами. Теперь поговорим о том, как заставить программу делать несколько дел одновременно. Это особенно важно для современных приложений, где пользователь не должен ждать, пока программа выполнит длительную операцию.

### 3.1 Зачем нужна многопоточность?

**Аналогия:** Один повар готовит всё по очереди: сначала режет овощи, потом варит суп, потом жарит мясо. Два повара работают параллельно: один режет, другой варит — блюдо готово быстрее. Точно так же и в программировании: если задач много, имеет смысл распределить их между несколькими потоками выполнения.

Многопоточность позволяет:
- Использовать все ядра процессора
- Не блокировать UI при длительных операциях
- Обрабатывать множество запросов одновременно

### 3.2 Процессы и потоки

Прежде чем создавать потоки, важно понять, чем **процесс** отличается от **потока** — это фундаментальные понятия операционной системы.

**Процесс (Process)** — это запущенная программа с собственным выделенным пространством памяти. Каждый процесс изолирован от других: у него свой стек, своя куча, свои переменные. Когда вы запускаете `java MyApp`, ОС создаёт новый процесс с отдельной JVM.

**Поток (Thread)** — это лёгковесная единица выполнения **внутри** процесса. Все потоки одного процесса **разделяют** общую память (кучу), но имеют **собственный стек вызовов**.

```
┌─────────────────────────────────────────────────────────┐
│                      Процесс (JVM)                      │
│                                                         │
│  ┌─────────────── Общая память (Heap) ───────────────┐  │
│  │  объекты, статические поля, массивы               │  │
│  └───────────────────────────────────────────────────┘  │
│                                                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│  │ Поток 1  │  │ Поток 2  │  │ Поток 3  │              │
│  │ (main)   │  │          │  │          │              │
│  │          │  │          │  │          │              │
│  │ свой стек│  │ свой стек│  │ свой стек│              │
│  └──────────┘  └──────────┘  └──────────┘              │
└─────────────────────────────────────────────────────────┘
```

| Критерий | Процесс | Поток |
|----------|---------|-------|
| **Память** | Собственное адресное пространство | Общая куча, свой стек |
| **Создание** | Дорого (выделение памяти, ресурсов ОС) | Дёшево (только стек) |
| **Коммуникация** | Через IPC (сокеты, файлы, каналы) | Напрямую через общую память |
| **Изоляция** | Полная: падение одного не затрагивает другой | Слабая: ошибка в одном потоке может обрушить весь процесс |
| **Пример** | Два экземпляра `java MyApp` | `new Thread(...)` внутри одной программы |

**Почему Java использует потоки?** Потоки разделяют память → данные доступны сразу, без копирования. Создание потока в десятки раз быстрее, чем создание процесса. Однако общая память — это и преимущество, и источник проблем: если два потока одновременно изменяют одну переменную, возникают **состояния гонки** (об этом — ниже).

---

### 3.3 Создание потоков

В Java есть два базовых способа:

**Способ 1: Расширение класса Thread**
```java
static class MyThread extends Thread {
    public void run() {
        System.out.println("Поток через MyThread");
    }
}

Thread t1 = new MyThread();
t1.start(); // НЕ вызывайте run() напрямую — это не создаст новый поток!
```

**Способ 2: Реализация Runnable (предпочтительно)**
```java
static class MyRunnable implements Runnable {
    public void run() {
        System.out.println("Поток через MyRunnable");
    }
}

Runnable task = new MyRunnable();
Thread t2 = new Thread(task);
t2.start();
```

**Способ 3: Лямбда-выражение**
```java
Thread t3 = new Thread(() -> System.out.println("Поток через лямбду"));
t3.start();

t1.join();
t2.join();
t3.join();
```

**Почему Runnable лучше Thread?**
- Java поддерживает только одиночное наследование — если класс extends Thread, он не может наследовать другой класс
- `Runnable` — только задание; поток (`Thread`) — механизм выполнения. Разделение ответственности.

### 3.4 Жизненный цикл потока

Каждый поток в Java проходит через определённые состояния. Давайте посмотрим на эту схему — она поможет понять, что происходит с потоком от момента создания до завершения:

```
                     start()
            NEW ───────────────> RUNNABLE ─── run() завершён ──> TERMINATED
                                  ▲  ▲  ▲
                                  │  │  │
                 захват монитора ─┘  │  └─ notify()/interrupt()
                                    │        или timeout
                                    │
              ┌─────────────────────┼─────────────────────┐
              │                     │                     │
    ждёт монитор           wait()/join()          sleep()/wait(ms)
    (synchronized)                │                     │
              │                   │                     │
          BLOCKED             WAITING            TIMED_WAITING
```

**Состояния потока (Thread.State):**

| Состояние | Описание |
|-----------|----------|
| `NEW` | Поток создан (`new Thread()`), но ещё не запущен |
| `RUNNABLE` | Поток выполняется или готов к выполнению (ожидает процессорное время) |
| `BLOCKED` | Ожидает захвата монитора (вход в `synchronized`-блок, занятый другим потоком) |
| `WAITING` | Ожидает бессрочно: `wait()`, `join()`, `LockSupport.park()` |
| `TIMED_WAITING` | Ожидает ограниченное время: `sleep(ms)`, `wait(ms)`, `join(ms)` |
| `TERMINATED` | Метод `run()` завершился (нормально или с исключением) |

**Важно:** Из `BLOCKED`, `WAITING` и `TIMED_WAITING` поток всегда возвращается в `RUNNABLE`, а не напрямую в `TERMINATED`.

### 3.5 Основные методы Thread

```java
Thread t = new Thread(() -> {
    try {
        Thread.sleep(1000);
        System.out.println("Выполнение потока");
    } catch (InterruptedException e) {
        System.out.println("Поток прерван");
    }
});

t.start();
t.join();
System.out.println("Главный поток завершён");
```

**Прерывание потока:**
```java
Thread longTask = new Thread(() -> {
    while (!Thread.currentThread().isInterrupted()) {
        // Выполняем работу...
    }
    System.out.println("Завершено по запросу");
});

longTask.start();
Thread.sleep(1000);
longTask.interrupt(); // Устанавливает флаг прерывания
```

**Состояния потока (демонстрация):**
```java
Thread t = new Thread(() -> {
    try {
        Thread.sleep(300);
    } catch (InterruptedException ignored) {}
});

System.out.println("Состояние (NEW): " + t.getState());
t.start();
Thread.sleep(100);
System.out.println("Состояние (RUNNABLE): " + t.getState());
t.join();
System.out.println("Состояние (TERMINATED): " + t.getState());
```

### 3.6 Проблемы многопоточности и синхронизация

Многопоточность даёт скорость, но и создаёт проблемы. Самая коварная из них — **состояние гонки**: когда два потока одновременно изменяют одни и те же данные, результат становится непредсказуемым.

**Состояние гонки (Race Condition):**

```java
// ПРОБЛЕМА: два потока изменяют счётчик одновременно
static class SyncDemo {
    private int counter = 0;

    public void increment() {
        counter++; // НЕ атомарная операция! Это: read + add + write
    }
}

SyncDemo demo = new SyncDemo();

Thread t1 = new Thread(() -> {
    for (int i = 0; i < 1000; i++) demo.increment();
});

Thread t2 = new Thread(() -> {
    for (int i = 0; i < 1000; i++) demo.increment();
});

t1.start();
t2.start();
t1.join();
t2.join();

// Ожидаем 2000, но получаем меньше — данные потеряны!
System.out.println("Счётчик: " + demo.counter);
```

### 3.7 Ключевое слово synchronized

Как решить проблему гонки? Java предоставляет механизм синхронизации.

**Монитор (Monitor)** — встроенный в каждый объект Java механизм синхронизации. Когда поток входит в `synchronized`-блок/метод, он захватывает монитор объекта; другие потоки, пытающиеся захватить тот же монитор, блокируются до его освобождения.

`synchronized` предоставляет **две** гарантии:
1. **Взаимное исключение (mutual exclusion):** только один поток в момент времени выполняет синхронизированный блок/метод
2. **Видимость памяти (memory visibility):** все записи, сделанные потоком до выхода из `synchronized`-блока, гарантированно видны другому потоку при входе в `synchronized`-блок на том же мониторе

Без гарантии видимости один поток мог бы изменить переменную, а другой — продолжать видеть старое значение из-за кэширования в регистрах процессора.

```java
static class SyncDemo {
    private int counter = 0;

    // Синхронизированный метод — блокировка на объекте this
    public synchronized void increment() {
        counter++;
    }
}

// Теперь всегда получим 2000:
SyncDemo demo = new SyncDemo();

Thread t1 = new Thread(() -> {
    for (int i = 0; i < 1000; i++) demo.increment();
});

Thread t2 = new Thread(() -> {
    for (int i = 0; i < 1000; i++) demo.increment();
});

t1.start();
t2.start();
t1.join();
t2.join();

System.out.println("Счётчик: " + demo.counter); // 2000
```

### 3.8 Ключевое слово volatile

`synchronized` обеспечивает и взаимное исключение, и видимость памяти, но иногда нужна **только видимость** — без блокировки. Для этого существует ключевое слово `volatile`.

**Что гарантирует `volatile`:**
- Каждое чтение переменной берёт значение **из основной памяти** (а не из кэша процессора)
- Каждая запись **немедленно сбрасывается** в основную память
- Все потоки видят **актуальное** значение переменной

**Чего `volatile` НЕ гарантирует:**
- **Атомарность составных операций.** Операция `counter++` по-прежнему не атомарна (read → add → write), даже если `counter` объявлена как `volatile`

```java
// volatile подходит для простых флагов:
static class Worker {
    private volatile boolean running = true;

    public void stop() {
        running = false; // Другой поток сразу увидит изменение
    }

    public void work() {
        while (running) {
            // Выполняем работу...
            // Без volatile поток может не увидеть running = false
            // из-за кэширования значения в регистре процессора
        }
        System.out.println("Остановлен");
    }
}
```

```java
// volatile НЕ подходит для счётчиков:
private volatile int counter = 0;

public void increment() {
    counter++; // Всё ещё состояние гонки! volatile не делает ++ атомарным
}
```

**Когда что использовать:**

| Инструмент | Видимость | Атомарность | Блокировка | Когда использовать |
|-----------|-----------|-------------|------------|-------------------|
| `volatile` | ✅ | ❌ | ❌ | Простые флаги, одиночные чтения/записи |
| `synchronized` | ✅ | ✅ | ✅ | Составные операции, критические секции |
| `AtomicInteger` | ✅ | ✅ | ❌ (CAS) | Счётчики, аккумуляторы без блокировки |

### 3.9 wait(), notify() и notifyAll()

Иногда потокам нужно не просто по очереди работать с данными, а **взаимодействовать друг с другом** — один поток ждёт, пока другой подготовит данные. Для этого существуют методы `wait()`, `notify()` и `notifyAll()`.

`wait()`, `notify()` и `notifyAll()` — механизм взаимодействия между потоками. Они определены в классе **`Object`** (не в `Thread!`) и могут вызываться **только внутри `synchronized`-блока или метода**. Вызов вне `synchronized` приведёт к `IllegalMonitorStateException`:
- `wait()` — поток освобождает монитор и переходит в ожидание
- `notify()` — пробуждает **один** поток, ожидающий этого монитора
- `notifyAll()` — пробуждает **все** потоки, ожидающие этого монитора (используйте, когда пробуждение любого из ожидающих имеет смысл)

```java
static class WaitNotifyDemo {
    private static final Object lock = new Object();
    private static boolean ready = false;

    public static void demo() throws InterruptedException {
        Thread producer = new Thread(() -> {
            synchronized (lock) {
                System.out.println("Producer: работа...");
                ready = true;
                lock.notify();
            }
        });

        Thread consumer = new Thread(() -> {
            synchronized (lock) {
                // Важно: именно while, а не if!
                // 1. Возможны «ложные пробуждения» (spurious wakeups) — JVM может
                //    разбудить поток без вызова notify()
                // 2. Если несколько consumer-ов ждут, один из них может уже обработать
                //    сигнал, и условие снова стало false
                while (!ready) {
                    try {
                        lock.wait(); // Освобождает монитор и ждёт notify()
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
                System.out.println("Consumer: получил сигнал");
            }
        });

        consumer.start();
        Thread.sleep(500);
        producer.start();

        producer.join();
        consumer.join();
    }
}
```

### 3.10 Атомарные классы (java.util.concurrent.atomic)

Иногда `synchronized` — это слишком тяжёлый инструмент для простых операций вроде инкремента счётчика. Атомарные классы используют механизм **CAS (Compare-And-Swap)** — аппаратную инструкцию процессора, которая обновляет значение только если оно не изменилось другим потоком. Это позволяет обойтись без блокировок:

```java
import java.util.concurrent.atomic.*;

// AtomicInteger — атомарные операции без synchronized
AtomicInteger atomicCount = new AtomicInteger(0);

Thread t1 = new Thread(() -> {
    for (int i = 0; i < 10000; i++) {
        atomicCount.incrementAndGet(); // Атомарная операция
    }
});

Thread t2 = new Thread(() -> {
    for (int i = 0; i < 10000; i++) {
        atomicCount.incrementAndGet();
    }
});

t1.start();
t2.start();
t1.join();
t2.join();

// Результат всегда 20000 — без synchronized и без блокировок
System.out.println("Атомарный счётчик: " + atomicCount.get());
```

Основные атомарные классы: `AtomicInteger`, `AtomicLong`, `AtomicBoolean`, `AtomicReference<T>`.

### 3.11 Пулы потоков и ExecutorService

В реальных приложениях создавать `new Thread()` на каждую задачу — плохая практика:
- Создание потока занимает время и память (стек ~512 КБ — 1 МБ)
- Нет контроля над количеством одновременных потоков
- При тысячах задач система может исчерпать ресурсы

**Решение** — пулы потоков. Пул создаёт фиксированное количество потоков и переиспользует их для выполнения задач из очереди.

```java
import java.util.concurrent.*;

// Создаём пул из 4 потоков
ExecutorService executor = Executors.newFixedThreadPool(4);

// Отправляем задачи без возврата результата (Runnable)
executor.execute(() -> {
    System.out.println("Задача 1: " + Thread.currentThread().getName());
});

// Отправляем задачу с возвратом результата (Callable)
Future<String> future = executor.submit(() -> {
    Thread.sleep(1000);
    return "Результат вычисления";
});

// Получаем результат (блокирует, пока задача не завершится)
String result = future.get();
System.out.println(result);

// ОБЯЗАТЕЛЬНО завершаем пул после использования
executor.shutdown();
```

**Основные типы пулов:**

| Метод | Описание |
|-------|----------|
| `Executors.newFixedThreadPool(n)` | Фиксированное количество потоков — подходит для стабильной нагрузки |
| `Executors.newCachedThreadPool()` | Создаёт потоки по необходимости, переиспользует простаивающие |
| `Executors.newSingleThreadExecutor()` | Один поток — задачи выполняются строго по очереди |
| `Executors.newScheduledThreadPool(n)` | Поддерживает отложенное и периодическое выполнение |

**`Future<T>`** — «обещание» результата. Основные методы:
- `get()` — блокирует текущий поток до получения результата
- `get(timeout, unit)` — ждёт не дольше указанного времени
- `isDone()` — проверяет, завершена ли задача
- `cancel(mayInterrupt)` — отменяет задачу

**Важно:** Всегда вызывайте `executor.shutdown()` (или `shutdownNow()`) — иначе JVM не завершится, потому что потоки пула продолжают работать.

---

## Часть 4: Итоги

Сегодня мы прошли большой путь — от коллекций через файловый ввод/вывод до многопоточности. Вот краткая сводка ключевых классов и интерфейсов по каждой теме:

| Тема | Ключевые классы/интерфейсы |
|------|---------------------------|
| List | `ArrayList`, `LinkedList` |
| Set | `HashSet`, `LinkedHashSet`, `TreeSet` |
| Map | `HashMap`, `LinkedHashMap`, `TreeMap` |
| Queue | `LinkedList`, `PriorityQueue`, `ArrayDeque` |
| Concurrent | `ConcurrentHashMap`, `CopyOnWriteArrayList`, `BlockingQueue` |
| Сортировка | `Comparable`, `Comparator`, `Collections.sort()` |
| Stream API | `stream()`, `filter()`, `map()`, `collect()`, `reduce()` |
| Байтовые I/O | `InputStream`, `OutputStream`, `FileInputStream`, `BufferedInputStream` |
| Символьные I/O | `Reader`, `Writer`, `FileReader`, `BufferedReader`, `PrintWriter` |
| Процесс vs Поток | Процесс — отдельная JVM с изолированной памятью; Поток — лёгковесная единица внутри процесса с общей кучей |
| Поток | `Thread`, `Runnable`, `start()`, `join()`, `sleep()`, `interrupt()` |
| Синхронизация | `synchronized` (монитор + видимость памяти), `volatile` (только видимость), `wait()`, `notify()`, `notifyAll()` |
| Атомарные классы | `AtomicInteger`, `AtomicLong`, `AtomicBoolean`, `AtomicReference<T>` |
| Пулы потоков | `ExecutorService`, `Executors.newFixedThreadPool()`, `Future<T>`, `Callable<T>` |

---

## Часть 5: Дополнительные примеры

### Полный пример Stream API

В завершение давайте рассмотрим более реалистичный пример использования Stream API — работу с коллекцией студентов. Здесь вы увидите группировку, статистику и параллельную обработку:

```java
record Student(String name, int grade, String faculty) {}

List<Student> students = List.of(
    new Student("Анна", 95, "ИТ"),
    new Student("Борис", 78, "Математика"),
    new Student("Вера", 88, "ИТ"),
    new Student("Геннадий", 92, "ИТ"),
    new Student("Дина", 65, "Математика")
);

// Группировка студентов ИТ по успеваемости
Map<String, Double> itAvg = students.stream()
    .filter(s -> s.faculty().equals("ИТ"))
    .collect(Collectors.groupingBy(
        Student::faculty,
        Collectors.averagingInt(Student::grade)
    ));

// Статистика
IntSummaryStatistics stats = students.stream()
    .mapToInt(Student::grade)
    .summaryStatistics();
System.out.printf("Мин: %d, Макс: %d, Среднее: %.1f%n",
    stats.getMin(), stats.getMax(), stats.getAverage());

// Параллельный стрим для больших данных:
long count = students.parallelStream()
    .filter(s -> s.grade() >= 80)
    .count();
```
