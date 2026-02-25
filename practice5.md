# Практическое занятие 5: Коллекции, Потоки ввода/вывода и Многопоточность

## Часть 1: Коллекции

### Задание 1.1: List — Управление списком задач

Реализуйте класс `TaskManager`, хранящий список задач в `ArrayList<String>`. Реализуйте методы:
- `addTask(String task)` — добавить задачу в конец.
- `addTaskAtPosition(String task, int position)` — вставить на указанную позицию; если позиция недопустима — добавить в конец.
- `removeTask(String task)` — удалить задачу по имени, вернуть `true` если удалено.
- `getTask(int index)` — получить по индексу или `null` если вне диапазона.
- `searchTasks(String keyword)` — найти задачи, содержащие ключевое слово (без учёта регистра).
- `sortTasks()` — сортировка по алфавиту.
- `printAll()` — вывод с нумерацией.

Протестируйте: добавьте 4 задачи, вставьте срочную задачу в начало, найдите по ключевому слову «тест», отсортируйте.

---

### Задание 1.2: Set — Анализ текста

Реализуйте класс `TextAnalyzer` со статическими методами:
- `getUniqueWords(String text)` → `Set<String>` — все уникальные слова (в нижнем регистре, через `TreeSet` для сортировки), разделённые по `[\\s.,!?;:\"'()-]+`.
- `commonWords(String text1, String text2)` → `Set<String>` — пересечение уникальных слов обоих текстов.
- `uniqueToFirst(String text1, String text2)` → `Set<String>` — слова, есть только в первом тексте.
- `wordFrequency(String text)` → `Map<String, Integer>` — частота каждого слова.
- `topWords(String text, int n)` → `List<Map.Entry<String, Integer>>` — топ-N слов по убыванию частоты.

Протестируйте на двух текстах про Java и Python из условия. Выведите уникальные слова текста 1, общие слова, слова только в тексте 1, топ-5 частых слов текста 1.

---

### Задание 1.3: Map — Телефонная книга

Реализуйте класс `PhoneBook`, где `contacts` — это `TreeMap<String, List<String>>` (имя → список номеров). Реализуйте методы:
- `addContact(String name, String phone)` — добавить номер (если имя уже есть — добавить номер к списку, иначе создать новую запись).
- `findByName(String name)` → список номеров или пустой список.
- `searchByName(String partialName)` → `Map<String, List<String>>` — все записи, где имя содержит `partialName` (без учёта регистра).
- `removePhone(String name, String phone)` — удалить конкретный номер; если больше нет номеров — удалить контакт. Вернуть `true` при успехе.
- `findDuplicatePhones()` → `List<String>` — номера, встречающиеся у нескольких контактов.
- `printStats()` — всего контактов, всего номеров, среднее номеров на контакт.

Протестируйте: добавьте 5 контактов (включая дублирующий номер), найдите по «анна», найдите дублирующие номера, выведите статистику.

---

### Задание 1.4: Stream API — Обработка данных студентов

Изучите и запустите программу анализа данных студентов. Убедитесь в правильности вывода для каждого из 6 заданий. Ответьте: (1) чем `Collectors.groupingBy` отличается от ручной группировки циклом? (2) что возвращает `summaryStatistics()`?

```java
import java.util.*;
import java.util.stream.*;

public class StudentAnalytics {

    record Student(String name, String faculty, int grade, int year) {}

    public static void main(String[] args) {
        List<Student> students = List.of(
            new Student("Анна Иванова", "ИТ", 95, 2),
            new Student("Борис Петров", "Математика", 78, 3),
            new Student("Вера Сидорова", "ИТ", 88, 1),
            new Student("Геннадий Козлов", "ИТ", 92, 2),
            new Student("Дина Новикова", "Математика", 65, 1),
            new Student("Егор Федоров", "Физика", 85, 3),
            new Student("Жанна Морозова", "ИТ", 71, 1),
            new Student("Зоя Лебедева", "Физика", 90, 2)
        );

        // Задание 1: Отфильтровать студентов ИТ с оценкой >= 85, отсортировать по имени
        System.out.println("=== Лучшие студенты ИТ (>=85) ===");
        students.stream()
            .filter(s -> s.faculty().equals("ИТ") && s.grade() >= 85)
            .sorted(Comparator.comparing(Student::name))
            .map(s -> s.name() + ": " + s.grade())
            .forEach(System.out::println);

        // Задание 2: Средняя оценка по факультетам
        System.out.println("\n=== Средний балл по факультетам ===");
        Map<String, Double> avgByFaculty = students.stream()
            .collect(Collectors.groupingBy(
                Student::faculty,
                Collectors.averagingInt(Student::grade)
            ));
        avgByFaculty.entrySet().stream()
            .sorted(Map.Entry.comparingByKey())
            .forEach(e -> System.out.printf("%s: %.1f%n", e.getKey(), e.getValue()));

        // Задание 3: Количество студентов каждого курса
        System.out.println("\n=== Студентов по курсам ===");
        students.stream()
            .collect(Collectors.groupingBy(Student::year, Collectors.counting()))
            .entrySet().stream()
            .sorted(Map.Entry.comparingByKey())
            .forEach(e -> System.out.println("Курс " + e.getKey() + ": " + e.getValue() + " студентов"));

        // Задание 4: Лучший студент каждого факультета
        System.out.println("\n=== Лучший студент каждого факультета ===");
        Map<String, Optional<Student>> bestByFaculty = students.stream()
            .collect(Collectors.groupingBy(
                Student::faculty,
                Collectors.maxBy(Comparator.comparingInt(Student::grade))
            ));
        bestByFaculty.forEach((faculty, student) ->
            student.ifPresent(s ->
                System.out.printf("%s: %s (%d)%n", faculty, s.name(), s.grade())
            )
        );

        // Задание 5: Все имена студентов в одну строку через запятую
        System.out.println("\n=== Все студенты ===");
        String allNames = students.stream()
            .map(Student::name)
            .sorted()
            .collect(Collectors.joining(", "));
        System.out.println(allNames);

        // Задание 6: Статистика оценок
        System.out.println("\n=== Статистика оценок ===");
        IntSummaryStatistics stats = students.stream()
            .mapToInt(Student::grade)
            .summaryStatistics();
        System.out.printf("Мин: %d, Макс: %d, Среднее: %.1f, Всего: %d%n",
            stats.getMin(), stats.getMax(), stats.getAverage(), stats.getCount());
    }
}
```

---

## Часть 2: Потоки ввода/вывода

### Задание 2.1: Работа с текстовыми файлами

Реализуйте класс `FileOperations` со статическими методами:
- `writeLines(String filename, List<String> lines)` — запись всех строк в файл через `PrintWriter(BufferedWriter(FileWriter(...)))`.
- `readLines(String filename)` → `List<String>` — чтение всех строк через `BufferedReader`.
- `printFileStats(String filename)` — вывести число строк, слов и символов (слова считайте через `split("\\s+")`).
- `grep(String filename, String keyword)` → `List<String>` — строки, содержащие ключевое слово.
- `copyFile(String source, String destination)` — побайтовое копирование через `FileInputStream`/`FileOutputStream` с буфером.

Все методы бросают `IOException`. Используйте `try-with-resources`. Протестируйте: запишите 5 строк, прочитайте их, выведите статистику, найдите строки с «Java», скопируйте файл.

---

### Задание 2.2: Сериализация объектов

```java
import java.io.*;
import java.util.*;

public class SerializationDemo {

    // Класс должен реализовывать Serializable для сериализации
    static class StudentRecord implements Serializable {
        private static final long serialVersionUID = 1L;

        private String name;
        private int grade;
        private String faculty;
        private transient String password; // transient — не сериализуется

        public StudentRecord(String name, int grade, String faculty, String password) {
            this.name = name;
            this.grade = grade;
            this.faculty = faculty;
            this.password = password;
        }

        // Геттеры
        public String getName() { return name; }
        public int getGrade() { return grade; }
        public String getFaculty() { return faculty; }
        public String getPassword() { return password; } // null после десериализации

        @Override
        public String toString() {
            return String.format("StudentRecord{name='%s', grade=%d, faculty='%s', password=%s}",
                name, grade, faculty, password);
        }
    }

    // Сохранить список объектов в файл
    public static void saveStudents(String filename, List<StudentRecord> students) throws IOException {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(filename))) {
            oos.writeObject(students);
        }
    }

    // Загрузить список объектов из файла
    @SuppressWarnings("unchecked")
    public static List<StudentRecord> loadStudents(String filename) throws IOException, ClassNotFoundException {
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(filename))) {
            return (List<StudentRecord>) ois.readObject();
        }
    }

    public static void main(String[] args) throws IOException, ClassNotFoundException {
        List<StudentRecord> students = new ArrayList<>();
        students.add(new StudentRecord("Анна", 95, "ИТ", "secret123"));
        students.add(new StudentRecord("Борис", 78, "Математика", "pass456"));

        System.out.println("До сериализации:");
        students.forEach(System.out::println);

        String filename = "students.ser";
        saveStudents(filename, students);
        System.out.println("\nСохранено в " + filename);

        List<StudentRecord> loaded = loadStudents(filename);
        System.out.println("\nПосле десериализации:");
        loaded.forEach(System.out::println);
        // Обратите внимание: password == null (transient поле!)

        new File(filename).delete();
    }
}
```

---

## Часть 3: Многопоточность

### Задание 3.1: Создание и запуск потоков

Изучите и запустите программу параллельной загрузки. Объясните: (1) почему строки прогресса разных потоков могут перемежаться? (2) что произойдёт, если убрать `join()`? (3) чем отличается `extends Thread` от `implements Runnable`?

```java
public class ThreadBasics {

    static class DownloadSimulator extends Thread {
        private String filename;
        private int sizeKB;
        private int downloadedKB = 0;

        public DownloadSimulator(String filename, int sizeKB) {
            super("Downloader-" + filename);
            this.filename = filename;
            this.sizeKB = sizeKB;
        }

        @Override
        public void run() {
            System.out.printf("[%s] Начало загрузки %s (%d KB)%n",
                getName(), filename, sizeKB);

            while (downloadedKB < sizeKB) {
                try {
                    Thread.sleep(100); // Симулируем задержку
                    downloadedKB = Math.min(downloadedKB + 100, sizeKB);
                    System.out.printf("[%s] Загружено: %d/%d KB (%.0f%%)%n",
                        getName(), downloadedKB, sizeKB,
                        (double) downloadedKB / sizeKB * 100);
                } catch (InterruptedException e) {
                    System.out.printf("[%s] Загрузка прервана!%n", getName());
                    return;
                }
            }

            System.out.printf("[%s] Загрузка %s завершена!%n", getName(), filename);
        }
    }

    public static void main(String[] args) throws InterruptedException {
        System.out.println("Запускаем параллельные загрузки...\n");

        Thread t1 = new DownloadSimulator("document.pdf", 300);
        Thread t2 = new DownloadSimulator("image.jpg", 500);
        Thread t3 = new DownloadSimulator("video.mp4", 1000);

        t1.start();
        t2.start();
        t3.start();

        System.out.println("Все загрузки запущены параллельно!");

        t1.join();
        t2.join();
        t3.join();

        System.out.println("\nВсе загрузки завершены!");
    }
}
```

---

### Задание 3.2: Синхронизация — Безопасный счётчик

Изучите и запустите обе версии счётчика. Объясните: (1) почему небезопасный счётчик даёт неверный результат? (2) что гарантирует ключевое слово `synchronized`? (3) запустите тест несколько раз — всегда ли небезопасный счётчик ошибается?

```java
public class SynchronizationDemo {

    // Небезопасный счётчик
    static class UnsafeCounter {
        private int count = 0;
        public void increment() { count++; }
        public int getCount() { return count; }
    }

    static class SafeCounter {
        private int count = 0;

        public synchronized void increment() {
            count++;
        }

        public synchronized int getCount() {
            return count;
        }
    }

    static void testCounter(Object counter, int threads, int incrementsPerThread)
            throws InterruptedException {
        Thread[] threadArray = new Thread[threads];
        for (int i = 0; i < threads; i++) {
            threadArray[i] = new Thread(() -> {
                for (int j = 0; j < incrementsPerThread; j++) {
                    if (counter instanceof UnsafeCounter uc) uc.increment();
                    else if (counter instanceof SafeCounter sc) sc.increment();
                }
            });
        }

        for (Thread t : threadArray) t.start();
        for (Thread t : threadArray) t.join();

        int expected = threads * incrementsPerThread;
        int actual = counter instanceof UnsafeCounter uc ? uc.getCount()
                   : counter instanceof SafeCounter sc ? sc.getCount() : -1;
        System.out.printf("Ожидаем: %d, Получили: %d, %s%n",
            expected, actual,
            actual == expected ? "КОРРЕКТНО" : "ОШИБКА (потеряно " + (expected - actual) + ")");
    }

    public static void main(String[] args) throws InterruptedException {
        System.out.println("=== Небезопасный счётчик ===");
        for (int i = 0; i < 5; i++) {
            testCounter(new UnsafeCounter(), 10, 1000);
        }

        System.out.println("\n=== Безопасный счётчик ===");
        for (int i = 0; i < 5; i++) {
            testCounter(new SafeCounter(), 10, 1000);
        }
    }
}
```

---

### Задание 3.3: Производитель-Потребитель (Producer-Consumer)

Изучите две реализации паттерна Производитель-Потребитель. Запустите программу с `BlockingQueue`. Объясните: (1) зачем в ручной реализации `while` вместо `if` при проверке условия? (2) почему `BlockingQueue` предпочтительнее? (3) что произойдёт, если производитель быстрее потребителя?

```java
import java.util.LinkedList;
import java.util.Queue;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.ArrayBlockingQueue;

public class ProducerConsumerDemo {

    // Вариант 1: Ручная реализация с synchronized/wait/notify
    static class SharedBuffer {
        private final Queue<Integer> buffer = new LinkedList<>();
        private final int capacity;

        public SharedBuffer(int capacity) {
            this.capacity = capacity;
        }

        public synchronized void put(int item) throws InterruptedException {
            while (buffer.size() >= capacity) {
                wait();
            }
            buffer.offer(item);
            notifyAll();
        }

        public synchronized int take() throws InterruptedException {
            while (buffer.isEmpty()) {
                wait();
            }
            int item = buffer.poll();
            notifyAll();
            return item;
        }
    }

    // Вариант 2: Используя BlockingQueue (рекомендуемый подход)
    static void demonstrateBlockingQueue() throws InterruptedException {
        BlockingQueue<String> queue = new ArrayBlockingQueue<>(5);

        // Производитель
        Thread producer = new Thread(() -> {
            for (int i = 1; i <= 10; i++) {
                try {
                    String task = "Задача-" + i;
                    queue.put(task); // Блокирует если очередь полна
                    System.out.println("[Производитель] Добавил: " + task
                        + " (в очереди: " + queue.size() + ")");
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            }
        });

        // Потребитель
        Thread consumer = new Thread(() -> {
            for (int i = 0; i < 10; i++) {
                try {
                    String task = queue.take(); // Блокирует если очередь пуста
                    System.out.println("[Потребитель] Обработал: " + task);
                    Thread.sleep(200); // Потребитель медленнее
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            }
        });

        producer.start();
        consumer.start();
        producer.join();
        consumer.join();
        System.out.println("Все задачи обработаны!");
    }

    public static void main(String[] args) throws InterruptedException {
        System.out.println("=== BlockingQueue Producer-Consumer ===");
        demonstrateBlockingQueue();
    }
}
```

---

### Задание 3.4: Прерывание потоков

Изучите и запустите программу с прерыванием потока. Объясните: (1) чем `thread.interrupt()` отличается от немедленной остановки? (2) почему в `catch (InterruptedException)` вызывается `Thread.currentThread().interrupt()`? (3) что означает `isInterrupted()`?

```java
public class InterruptionDemo {

    static class LongRunningTask implements Runnable {
        private final String taskName;
        private final int totalSteps;

        public LongRunningTask(String taskName, int totalSteps) {
            this.taskName = taskName;
            this.totalSteps = totalSteps;
        }

        @Override
        public void run() {
            System.out.printf("[%s] Старт, шагов: %d%n", taskName, totalSteps);

            for (int step = 1; step <= totalSteps; step++) {
                if (Thread.currentThread().isInterrupted()) {
                    System.out.printf("[%s] Обнаружено прерывание, завершение%n", taskName);
                    return;
                }

                System.out.printf("[%s] Шаг %d/%d%n", taskName, step, totalSteps);

                try {
                    Thread.sleep(500);
                } catch (InterruptedException e) {
                    System.out.printf("[%s] Прервано на шаге %d%n", taskName, step);
                    Thread.currentThread().interrupt();
                    return;
                }
            }

            System.out.printf("[%s] Завершено!%n", taskName);
        }
    }

    public static void main(String[] args) throws InterruptedException {
        Thread task1 = new Thread(new LongRunningTask("Задача-А", 10), "Thread-A");
        Thread task2 = new Thread(new LongRunningTask("Задача-Б", 10), "Thread-B");

        task1.start();
        task2.start();

        Thread.sleep(1500); // Ждём 1.5 секунды

        System.out.println("\n--- Прерываем Задачу-А ---");
        task1.interrupt(); // Прерываем один поток

        task1.join();
        task2.join();

        System.out.printf("Задача-А прервана: %s%n", !task1.isAlive());
        System.out.printf("Задача-Б завершена: %s%n", !task2.isAlive());
    }
}
```

---

## Часть 4: Комплексное задание

### Задание 4.1: Параллельный поиск в файлах

Реализуйте параллельный поиск текста в нескольких файлах:
- Класс `FileSearchTask implements Callable<List<String>>`: ищет `keyword` в файле построчно, возвращает список строк в формате `«filename:номер_строки: текст_строки»`. Если файл не найден — добавляет `«filename: файл не найден»`.
- Метод `searchInFiles(List<String> files, String keyword)`: создаёт `ExecutorService` с фиксированным пулом потоков, запускает `FileSearchTask` через `executor.submit()`, собирает результаты через `Future.get()`, выводит все найденные строки, закрывает executor.

Создайте 3 тестовых файла с содержимым из условия, выполните поиск по «java», удалите файлы.

---

## Часть 5: Контрольные вопросы

Ответьте письменно:

1. В чём разница между `ArrayList` и `LinkedList`? Когда использовать каждый?
2. Почему `HashSet` не гарантирует порядок элементов?
3. Что такое `equals()` и `hashCode()` и почему их нужно переопределять вместе для ключей `HashMap`?
4. Чем `Stream API` отличается от `for-each`? Можно ли изменять коллекцию через Stream?
5. В чём разница между `BufferedReader` и `FileReader`?
6. Почему нужно закрывать потоки ввода/вывода? Что произойдёт, если не закрыть?
7. В чём разница между `Thread` и `Runnable`? Почему `Runnable` предпочтительнее?
8. Почему `t.run()` не создаёт новый поток, а `t.start()` — создаёт?
9. Что такое "состояние гонки" (race condition)? Приведите пример.
10. Чем `BlockingQueue` удобнее чем ручная реализация с `wait`/`notify`?
11. Что происходит с потоком при вызове `Thread.sleep()`? Освобождает ли он монитор?
12. Что такое `transient` поле при сериализации?

---

## Результаты занятия

К концу занятия вы должны сдать:
1. Реализованные Java-файлы для всех заданий
2. Ответы на контрольные вопросы

**Критерии оценки:**
- Правильный выбор коллекции для каждой задачи
- Корректное закрытие ресурсов (try-with-resources)
- Безопасная работа с потоками (synchronized или concurrent API)
- Корректная обработка InterruptedException
- Программы работают предсказуемо при многократном запуске
