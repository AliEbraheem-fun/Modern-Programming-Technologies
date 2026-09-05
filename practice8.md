# Практическое занятие 8: Веб-архитектура

Сегодня мы не будем прятаться за фреймворк. Всё занятие — про то, что происходит на уровне протокола: вы своими глазами увидите текст HTTP-запроса, отправите руками все основные методы, напишете сервер, который отвечает правильными кодами, и спроектируете REST API для библиотеки.

Врач слушает пациента стетоскопом, а не гадает по цвету лица. `curl` — ваш стетоскоп: он показывает, что реально ушло с вашей машины и что реально вернулось. Все задания выполняются **строго по порядку**: каждое следующее опирается на файлы и инструменты, настроенные в предыдущем.

---

## Часть 1: Структура HTTP-запроса и ответа

### Задание 1.1: Подготовка рабочего места

Создайте каталог `http-lab` — в нём будут жить все файлы этого занятия — и проверьте, что нужные инструменты на месте.

```bash
mkdir http-lab
cd http-lab
curl --version          # в Windows PowerShell: curl.exe --version
java -version
```

В Windows добавьте ещё одну команду — она переключает консоль на UTF-8:

```powershell
chcp 65001
```

Три замечания для Windows, без которых половина команд этого занятия сломается:

1. В PowerShell слово `curl` — это псевдоним командлета `Invoke-WebRequest` с совершенно другими ключами. **Всегда пишите `curl.exe`.**
2. Команда `chcp 65001` переключает консоль на UTF-8, иначе русский текст в ответах превратится в «кракозябры».
3. Одинарные кавычки вокруг JSON в PowerShell не работают так, как в bash: двойные кавычки внутри съедаются, и на сервер уходит битое тело. Для всех запросов с JSON мы будем класть тело в файл — этот приём работает одинаково везде.

Ожидаемый результат: `curl` версии 7.x или 8.x и Java версии 21 или новее. Если `java -version` показывает версию младше 21, установите JDK 21 — код из Части 3 использует записи (`record`) и переключатели-выражения.

**Ответьте письменно:**
1. Какая версия curl и какая версия JDK у вас установлены?
2. Какие протоколы поддерживает ваш curl (строка `Protocols:` в выводе `--version`)? Есть ли среди них `https`?
3. Почему в PowerShell нужно писать именно `curl.exe`, а не `curl`?

---

### Задание 1.2: Сырой обмен под микроскопом

Ключ `-v` (verbose) показывает и запрос, и ответ целиком. Строки, начинающиеся с `>`, — это то, что отправили вы. Строки с `<` — то, что прислал сервер. Строки с `*` — служебные сообщения самого curl (установка соединения, TLS-рукопожатие).

```bash
curl -v "https://postman-echo.com/get?course=java&topic=http"     # в PowerShell: curl.exe
```

Кавычки вокруг адреса обязательны в обеих системах: в bash символ `&` без кавычек отправит команду в фоновый режим, а в PowerShell вызовет синтаксическую ошибку.

Скопируйте вывод в отчёт и **разметьте его**, подписав четыре части запроса и четыре части ответа из лекции:

| Часть сообщения | Строка из вашего вывода |
|-----------------|-------------------------|
| Стартовая строка запроса | |
| Заголовки запроса (все) | |
| Пустая строка-разделитель | |
| Тело запроса | |
| Строка состояния ответа | |
| Заголовки ответа (5 любых) | |
| Тело ответа | |

**Ответьте письменно:**
1. Сколько заголовков curl добавил в ваш запрос самостоятельно, хотя вы их не указывали? Перечислите их и объясните назначение каждого.
2. Почему в GET-запросе нет тела и нет заголовка `Content-Type`, зато в ответе `Content-Type` есть?
3. Найдите в теле ответа объект `args`. Откуда сервер взял его содержимое?

---

### Задание 1.3: Разбор URL по частям

Возьмите адрес `https://library.example.com:8443/api/v1/books/42?genre=drama&sort=year#reviews` и заполните таблицу:

| Часть URL | Значение | Уходит ли на сервер |
|-----------|----------|---------------------|
| Схема | | |
| Хост | | |
| Порт | | |
| Путь | | |
| Строка запроса | | |
| Фрагмент | | |

Теперь проверьте свою последнюю строчку экспериментом:

```bash
curl -v "https://postman-echo.com/get?token=abc123#secret-part"
```

Посмотрите на стартовую строку запроса (строка с `>` в начале) и на объект `args` в ответе.

**Ответьте письменно:**
1. Попал ли фрагмент `#secret-part` в стартовую строку запроса? Кто и на каком этапе его отбросил?
2. Значение `token=abc123` видно в стартовой строке. Перечислите три места, где оно осядет в открытом виде даже при использовании HTTPS.
3. Куда нужно было положить этот токен, чтобы он не попал в журналы?

---

## Часть 2: Серия запросов к postman-echo.com

Сервис `https://postman-echo.com` — эхо-сервер: он возвращает JSON с описанием того, что получил. Это зеркало в примерочной. Вы не гадаете, как на вас сидит рубашка, — вы смотрите и видите. Точно так же здесь вы не гадаете, что ушло с вашей машины, а читаете это в ответе. Заведите в отчёте журнал: для каждой команды записывайте её саму, код ответа и одну-две строки о том, что нового вы увидели. Сводную таблицу соберёте в задании 2.7.

### Задание 2.1: GET с параметрами и собственными заголовками

Ключ `-i` показывает заголовки ответа вместе с телом: в отличие от `-v`, он не печатает ваш запрос, зато вывод короче.

```bash
curl -i "https://postman-echo.com/get?group=PI24&topic=http&year=2025"
curl -i -H "X-Student: Ivanov" -H "Accept-Language: ru-RU" -H "Accept: application/json" https://postman-echo.com/headers
```

Дальше в этой части команды даны в синтаксисе bash. На Windows подставляйте `curl.exe` и пишите каждую команду в одну строку: символ `\` для переноса в PowerShell не работает.

**Ответьте письменно:**
1. В каком поле ответа оказались `group`, `topic` и `year`? Почему сервер сумел разложить их по отдельным ключам?
2. Какие из заголовков в ответе `/headers` вы задали сами, а какие добавил curl?
3. Заголовок `Host` вы не указывали. Откуда он взялся и почему в HTTP/1.1 он обязателен?

---

### Задание 2.2: POST с телом в формате JSON

Сначала создайте файл `body.json` в каталоге `http-lab`.

**Linux / macOS:**

```bash
cat > body.json <<'EOF'
{"title":"Война и мир","author":"Толстой","year":1869}
EOF
```

**Windows PowerShell** (`Out-File` в Windows PowerShell 5.1 по умолчанию сохраняет файл в UTF-16, а `Set-Content` — в системной ANSI-кодировке; в обоих случаях сервер не разберёт такой JSON, поэтому пишем файл явно в UTF-8 без BOM):

```powershell
[System.IO.File]::WriteAllText("$PWD/body.json", '{"title":"Война и мир","author":"Толстой","year":1869}', (New-Object System.Text.UTF8Encoding($false)))
```

Файл можно создать и вручную в IDE — главное, сохранить в кодировке UTF-8 без BOM.

Теперь отправьте его (в PowerShell — `curl.exe`):

```bash
curl -i -X POST "https://postman-echo.com/post" -H "Content-Type: application/json" -d "@body.json"
```

Кавычки вокруг `"@body.json"` обязательны: в PowerShell символ `@` в начале аргумента имеет специальное значение. И обратите внимание, что тело мы не набирали в командной строке — именно поэтому команда работает одинаково в обеих системах.

Найдите в ответе поля `json` и `data`. Теперь повторите ту же команду, заменив тип на текстовый:

```bash
curl -i -X POST "https://postman-echo.com/post" -H "Content-Type: text/plain" -d "@body.json"
```

**Ответьте письменно:**
1. Что содержали поля `json` и `data` в первом случае и что — во втором? Объясните разницу.
2. Байты, ушедшие на сервер, в обоих запросах абсолютно одинаковы. Почему тогда результат разный?
3. Как этот эксперимент объясняет происхождение кода `415 Unsupported Media Type`?

---

### Задание 2.3: Форма против JSON

Те же данные, но в формате HTML-формы. Ключ `--data-urlencode` сам кодирует спецсимволы и заодно подставляет нужный `Content-Type`:

```bash
curl -i -X POST "https://postman-echo.com/post" --data-urlencode "title=War and Peace" --data-urlencode "author=Leo Tolstoy" -d "year=1869"
```

И третий способ передать то же самое — через строку запроса. Ключ `-G` превращает данные в query string, а `-v` покажет получившуюся стартовую строку:

```bash
curl -v -G "https://postman-echo.com/get" --data-urlencode "title=War and Peace" --data-urlencode "note=a&b=c"
```

Ищите строку вида `> GET /get?title=War+and+Peace&note=a%26b%3Dc HTTP/1.1`.

**Ответьте письменно:**
1. В какие три разных поля ответа попали данные при трёх способах отправки (`json`, `form`, `args`)?
2. Что такое процентное кодирование (percent-encoding)? Почему пробел превратился в `+`, символ `&` внутри значения — в `%26`, а знак `=` — в `%3D`? Что случилось бы, отправь мы их как есть?
3. Какой из трёх способов нельзя использовать для передачи пароля и почему?

---

### Задание 2.4: Остальные методы

```bash
curl -i -X PUT    "https://postman-echo.com/put"    -H "Content-Type: application/json" -d "@body.json"
curl -i -X PATCH  "https://postman-echo.com/patch"  -H "Content-Type: application/json" -d "@body.json"
curl -i -X DELETE "https://postman-echo.com/delete"
curl -i -X GET    "https://postman-echo.com/get"
curl -I           "https://postman-echo.com/get"
```

Последняя команда (`-I`, заглавная буква «i») отправляет метод `HEAD`.

**Ответьте письменно:**
1. Сравните вывод `curl -I` и `curl -i` для одного и того же адреса. Что общего и в чём разница?
2. Заголовок `Content-Length` в ответе на `HEAD` есть, а тела нет. Зачем сервер сообщает длину того, чего не прислал? Приведите практический сценарий использования.
3. Для каждого из пяти методов из этого задания укажите, является ли он безопасным (safe) и идемпотентным (idempotent). Оформите таблицей.

---

### Задание 2.5: Коды состояний и аутентификация

Адрес `/status/{code}` заставляет сервер вернуть любой код, который вы попросите:

```bash
curl -i "https://postman-echo.com/status/200"
curl -i "https://postman-echo.com/status/201"
curl -i "https://postman-echo.com/status/204"
curl -i "https://postman-echo.com/status/301"
curl -i "https://postman-echo.com/status/400"
curl -i "https://postman-echo.com/status/404"
curl -i "https://postman-echo.com/status/418"
curl -i "https://postman-echo.com/status/500"
```

Теперь Basic-аутентификация. Логин `postman`, пароль `password`:

```bash
curl -i "https://postman-echo.com/basic-auth"
curl -v -u postman:password "https://postman-echo.com/basic-auth"
```

Во втором выводе найдите заголовок `Authorization: Basic cG9zdG1hbjpwYXNzd29yZA==` и раскодируйте его значение:

```bash
echo "cG9zdG1hbjpwYXNzd29yZA==" | base64 -d      # Linux / macOS
```

```powershell
[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String("cG9zdG1hbjpwYXNzd29yZA=="))
```

**Ответьте письменно:**
1. У каких кодов из первого списка тело ответа отсутствует в принципе? Сверьтесь со значением `Content-Length`.
2. Какой код и какой заголовок вернул сервер на запрос к `/basic-auth` без учётных данных? Что этот заголовок сообщает клиенту?
3. Что получилось после раскодирования Base64? Является ли Base64 шифрованием и какой вывод отсюда следует про допустимость Basic-аутентификации поверх обычного HTTP?

---

### Задание 2.6: Cookie, перенаправления и тайм-ауты

```bash
curl -i    "https://postman-echo.com/cookies/set?token=abc123"
curl -i -L "https://postman-echo.com/cookies/set?token=abc123"
curl -c cookies.txt "https://postman-echo.com/cookies/set?token=abc123"
curl -b cookies.txt "https://postman-echo.com/cookies"
# теперь тайм-ауты
curl -i "https://postman-echo.com/delay/3"
curl -i --max-time 1 "https://postman-echo.com/delay/3"
```

Между третьей и четвёртой командой откройте файл `cookies.txt` любым текстовым редактором и посмотрите, что именно там сохранилось.

**Ответьте письменно:**
1. Какой код вернула первая команда и какой заголовок подсказал curl, куда идти дальше? Что изменилось после добавления ключа `-L`?
2. Что лежит в файле `cookies.txt`? Какие атрибуты cookie вы там видите и что означает каждый?
3. Чем закончилась команда с `--max-time 1` и что в реальном приложении произойдёт, если у HTTP-клиента не выставлен тайм-аут, а внешний сервис «подвис»?

---

### Задание 2.7: Журнал запросов

Соберите результаты всей Части 2 в одну таблицу. Минимум 12 строк — по одной на каждую выполненную команду:

| № | Метод | Адрес | Заголовки запроса, которые задали вы | Код ответа | Ключевое поле ответа |
|---|-------|-------|--------------------------------------|-----------|----------------------|
| 1 | GET | `/get?group=PI24...` | нет | 200 | `args` |
| 2 | GET | `/headers` | `X-Student`, `Accept-Language` | 200 | `headers` |
| 3 | POST | `/post` | `Content-Type: application/json` | 200 | `json` |
| ... | | | | | |

Эта таблица — обязательная часть отчёта.

---

## Часть 3: Свой сервер — от голого сокета до сервлета

Пока вы только отправляли запросы. Теперь встанем на другую сторону. Порядок в этой части не случаен: сначала мы соберём «лампочку от велосипедного генератора» — сервер на голом сокете, где всё крутите вы сами; потом подключимся к «домашней розетке» — готовому серверу из JDK; и только в конце придём в «бизнес-центр» — контейнер сервлетов, где электричество, охрана и уборка уже есть, а вы просто занимаетесь своим делом.

**Важно про порты.** Два сервера на одном порту не уживаются: прежде чем занять порт, освободите его — остановите предыдущий сервер сочетанием `Ctrl+C` в его окне терминала, иначе получите ошибку `Address already in use`. Порт 8080 занимают `RawHttpServer` и Spring Boot из задания 3.4, порт 8081 — `LibraryServer`, поэтому серверы с разных портов могут работать одновременно.

### Задание 3.1: Сервер на голом сокете

Внутри `http-lab` создайте каталоги `ru/fa/web` — они соответствуют пакету `ru.fa.web`, в котором будут лежать все Java-классы этого занятия:

```bash
mkdir -p ru/fa/web                                    # Linux / macOS
```

```powershell
New-Item -ItemType Directory -Force -Path ru/fa/web
```

Возьмите класс `RawHttpServer` из раздела 3.5 Лекции 8 (сервер на голом TCP-сокете, слушает порт 8080) и сохраните его без изменений в файл `ru/fa/web/RawHttpServer.java`.

Скомпилируйте и запустите (команды одинаковы в bash и в PowerShell, выполнять из каталога `http-lab`):

```bash
javac -encoding UTF-8 -d out ru/fa/web/RawHttpServer.java
java -cp out ru.fa.web.RawHttpServer
```

В **другом** окне терминала выполните два запроса и сравните то, что напечатал сервер:

```bash
curl -v http://localhost:8080/hello
```

Затем откройте в браузере `http://localhost:8080/hello` и снова посмотрите в консоль сервера.

Остановите сервер по `Ctrl+C`.

**Ответьте письменно:**
1. Выпишите наборы заголовков, которые прислали curl и браузер. Каких заголовков браузера нет у curl и зачем они нужны?
2. Сервер отдаёт одно и то же на любой путь. Какие строки кода нужно было бы добавить, чтобы `/hello` и `/goodbye` отвечали по-разному? Где в коде вы уже располагаете нужной информацией?
3. Запустите две команды `curl` одновременно из двух терминалов. Почему этот сервер обслуживает клиентов по очереди и чем это опасно в реальной жизни?

---

### Задание 3.2: REST-сервер «Библиотека» на HttpServer из JDK

Разбирать HTTP руками мы больше не будем — в JDK есть готовый лёгкий сервер `com.sun.net.httpserver.HttpServer`. Он не требует ни Maven, ни Tomcat, ни единой внешней зависимости, а работает по той же схеме, что и контейнер сервлетов: разбирает запрос и передаёт вам объект с готовыми методом, путём, заголовками и телом. Создайте файл `ru/fa/web/LibraryServer.java`:

```java
package ru.fa.web;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpServer;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;
import java.util.Comparator;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.Executors;
import java.util.concurrent.atomic.AtomicLong;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

/**
 * Мини-REST-сервис «Библиотека» без единой внешней зависимости.
 *
 * GET    /api/books      — список книг            -> 200
 * POST   /api/books      — создать книгу          -> 201 + Location
 * GET    /api/books/{id} — прочитать книгу        -> 200 или 404
 * PUT    /api/books/{id} — заменить книгу целиком -> 200 или 404
 * DELETE /api/books/{id} — удалить книгу          -> 204 или 404
 */
public class LibraryServer {

    private static final String BASE = "/api/books";

    /** Хранилище в памяти. Запросы обрабатываются в разных потоках, поэтому структура потокобезопасная. */
    private static final Map<Long, Book> STORAGE = new ConcurrentHashMap<>();
    private static final AtomicLong ID = new AtomicLong();

    /** Наивный разбор JSON регулярными выражениями. В реальном коде берут Jackson или Gson. */
    private static final Pattern TITLE = Pattern.compile("\"title\"\\s*:\\s*\"([^\"]*)\"");
    private static final Pattern YEAR = Pattern.compile("\"year\"\\s*:\\s*(\\d{1,4})");

    /** Ресурс «книга». Представление — JSON, который собираем вручную. */
    record Book(long id, String title, int year) {
        String toJson() {
            return "{\"id\":" + id + ",\"title\":\"" + title + "\",\"year\":" + year + "}";
        }
    }

    public static void main(String[] args) throws IOException {
        HttpServer server = HttpServer.create(new InetSocketAddress(8081), 0);
        server.createContext(BASE, LibraryServer::handle);
        // Пул потоков — то же, что делает контейнер сервлетов: много клиентов одновременно
        server.setExecutor(Executors.newFixedThreadPool(8));
        server.start();
        System.out.println("Библиотека слушает http://localhost:8081" + BASE + " — стоп по Ctrl+C");
    }

    /** Разбор пути и метода — ровно та работа, которую в Spring делает DispatcherServlet. */
    private static void handle(HttpExchange exchange) throws IOException {
        try {
            String method = exchange.getRequestMethod();
            // «хвост» после /api/books: пустой для коллекции, "/42" для одного ресурса
            String tail = exchange.getRequestURI().getPath().substring(BASE.length());

            if (tail.isEmpty() || tail.equals("/")) {
                switch (method) {
                    case "GET" -> list(exchange);
                    case "POST" -> save(exchange, null);
                    default -> methodNotAllowed(exchange, "GET, POST");
                }
                return;
            }

            long id;
            try {
                id = Long.parseLong(tail.substring(1));
            } catch (NumberFormatException e) {
                send(exchange, 400, "{\"error\":\"идентификатор должен быть числом\"}");
                return;
            }

            switch (method) {
                case "GET" -> readOne(exchange, id);
                case "PUT" -> save(exchange, id);
                case "DELETE" -> delete(exchange, id);
                default -> methodNotAllowed(exchange, "GET, PUT, DELETE");
            }
        } catch (RuntimeException e) {
            // Ошибка в нашем коде — это 500, а не 400: клиент ни в чём не виноват
            send(exchange, 500, "{\"error\":\"внутренняя ошибка сервера\"}");
        }
    }

    private static void list(HttpExchange exchange) throws IOException {
        send(exchange, 200, STORAGE.values().stream()
                .sorted(Comparator.comparingLong(Book::id))
                .map(Book::toJson)
                .collect(Collectors.joining(",", "[", "]")));
    }

    private static void readOne(HttpExchange exchange, long id) throws IOException {
        Book book = STORAGE.get(id);
        if (book == null) {
            send(exchange, 404, "{\"error\":\"книга не найдена\"}");
            return;
        }
        send(exchange, 200, book.toJson());
    }

    /**
     * Создание (POST, existingId == null) и полная замена (PUT, existingId задан).
     * Разница ровно одна: кто назначает идентификатор — сервер или клиент.
     */
    private static void save(HttpExchange exchange, Long existingId) throws IOException {
        String contentType = exchange.getRequestHeaders().getFirst("Content-Type");
        if (contentType == null || !contentType.toLowerCase().startsWith("application/json")) {
            send(exchange, 415, "{\"error\":\"ожидается Content-Type: application/json\"}");
            return;
        }
        if (existingId != null && !STORAGE.containsKey(existingId)) {
            send(exchange, 404, "{\"error\":\"книга не найдена\"}");
            return;
        }

        String body;
        try (InputStream in = exchange.getRequestBody()) {
            body = new String(in.readAllBytes(), StandardCharsets.UTF_8);
        }

        Matcher title = TITLE.matcher(body);
        if (!title.find()) {
            // Синтаксис разобран, но данные не проходят проверку предметной области
            send(exchange, 422, "{\"error\":\"поле title обязательно\"}");
            return;
        }
        Matcher year = YEAR.matcher(body);

        long id = existingId != null ? existingId : ID.incrementAndGet();
        Book book = new Book(id, title.group(1), year.find() ? Integer.parseInt(year.group(1)) : 0);
        STORAGE.put(id, book);

        if (existingId != null) {
            send(exchange, 200, book.toJson());
            return;
        }
        // 201 Created обязан сопровождаться заголовком Location с адресом нового ресурса
        exchange.getResponseHeaders().set("Location", BASE + "/" + id);
        send(exchange, 201, book.toJson());
    }

    private static void delete(HttpExchange exchange, long id) throws IOException {
        if (STORAGE.remove(id) == null) {
            send(exchange, 404, "{\"error\":\"книга не найдена\"}");
            return;
        }
        // У кода 204 тела быть не должно, длина -1 говорит серверу «тела нет»
        exchange.sendResponseHeaders(204, -1);
        exchange.close();
    }

    private static void methodNotAllowed(HttpExchange exchange, String allowed) throws IOException {
        // Вместе с 405 спецификация требует заголовок Allow
        exchange.getResponseHeaders().set("Allow", allowed);
        send(exchange, 405, "{\"error\":\"метод не поддерживается\"}");
    }

    /** Единая точка отправки: сначала заголовки и код, потом тело. Порядок менять нельзя. */
    private static void send(HttpExchange exchange, int status, String json) throws IOException {
        byte[] body = json.getBytes(StandardCharsets.UTF_8);
        exchange.getResponseHeaders().set("Content-Type", "application/json; charset=UTF-8");
        exchange.sendResponseHeaders(status, body.length);
        try (OutputStream out = exchange.getResponseBody()) {
            out.write(body);
        }
    }
}
```

Скомпилируйте и запустите:

```bash
javac -encoding UTF-8 -d out ru/fa/web/LibraryServer.java
java -cp out ru.fa.web.LibraryServer
```

Сервер слушает порт **8081**, чтобы не конфликтовать с `RawHttpServer` и со Spring Boot из задания 3.4.

**Ответьте письменно:**
1. Какая строка кода отвечает за то, что сервер обслуживает нескольких клиентов одновременно? Чем это отличается от `RawHttpServer`?
2. Почему поле `STORAGE` объявлено как `ConcurrentHashMap`, а не как обычный `HashMap`?
3. Метод `save` обслуживает и `POST`, и `PUT`. Найдите три места, где эти два случая расходятся, и объясните, как каждое связано с разницей между созданием и заменой ресурса. Какая из этих строк отвечает на вопрос, кто назначает идентификатор?

---

### Задание 3.3: Проверка своего API

Сервер из задания 3.2 должен быть запущен. Откройте второй терминал в каталоге `http-lab` и выполните полный цикл жизни ресурса. Команды приведены для Linux и macOS; в Windows PowerShell выполняйте их же, заменив `curl` на `curl.exe`.

```bash
# 1. Пустая коллекция
curl -i http://localhost:8081/api/books

# 2. Создание книги — ожидаем 201 и заголовок Location
curl -i -X POST http://localhost:8081/api/books -H "Content-Type: application/json" -d "@body.json"

# 3. Чтение созданной книги — ожидаем 200
curl -i http://localhost:8081/api/books/1

# 4. Замена целиком — ожидаем 200
curl -i -X PUT http://localhost:8081/api/books/1 -H "Content-Type: application/json" -d "@body.json"

# 5. Удаление — ожидаем 204 без тела
curl -i -X DELETE http://localhost:8081/api/books/1

# 6. Повторное чтение — ожидаем 404
curl -i http://localhost:8081/api/books/1
```

Теперь намеренно сломайте четыре вещи и запишите, каким кодом сервер ответил на каждую. Для проверки «б» нужен второй файл с телом — создайте его так же, как `body.json`:

**Linux / macOS:**

```bash
cat > bad.json <<'EOF'
{"year":1869}
EOF
```

**Windows PowerShell:**

```powershell
[System.IO.File]::WriteAllText("$PWD/bad.json", '{"year":1869}', (New-Object System.Text.UTF8Encoding($false)))
```

```bash
# а) не задали Content-Type — curl подставит свой, application/x-www-form-urlencoded
curl -i -X POST http://localhost:8081/api/books -d "@body.json"

# б) тело без обязательного поля title (файл bad.json создайте так же, как body.json)
curl -i -X POST http://localhost:8081/api/books -H "Content-Type: application/json" -d "@bad.json"

# в) метод, которого у коллекции нет
curl -i -X DELETE http://localhost:8081/api/books

# г) нечисловой идентификатор
curl -i http://localhost:8081/api/books/abc
```

Почему тело снова в файле, а не в командной строке? В bash можно написать `-d '{"year":1869}'` и всё сработает. В PowerShell же вариант с экранированными кавычками `-d "{\"year\":1869}"` разбирается не в один аргумент, а в два — `{\` и `year\:1869}`. Curl примет за тело только первый кусок, а второй попытается открыть как ещё один адрес и упадёт с ошибкой. Вы увидите одновременно и невнятное сообщение curl, и код 422, и не поймёте, что именно проверяли. Файл снимает вопрос целиком.

Обратите внимание на проверку «а»: заголовок `Content-Type` вы не задавали, но он всё равно ушёл на сервер — curl подставил `application/x-www-form-urlencoded`. Убедитесь в этом, повторив команду с ключом `-v`. Оформите результаты таблицей:

| Проверка | Метод | URI | Ожидаемый код | Полученный код | Заголовки ответа |
|----------|-------|-----|---------------|----------------|------------------|
| Пустая коллекция | GET | `/api/books` | 200 | | |
| Создание | POST | `/api/books` | 201 | | `Location` |
| ... | | | | | |

**Ответьте письменно:**

К этому моменту книга с id=1 уже удалена шагом 5 сценария, а хранилище пусто. Сначала создайте книгу заново:

```bash
curl -i -X POST http://localhost:8081/api/books -H "Content-Type: application/json" -d "@body.json"
```

Она получит id=2 — счётчик идентификаторов сдвинулся ещё на шаге 2 сценария и не откатывается назад при удалении. Теперь выполните `curl -i -X DELETE http://localhost:8081/api/books/2` дважды подряд.

1. Какие коды вернулись на два запроса `DELETE /api/books/2` подряд? Является ли `DELETE` идемпотентным, несмотря на разные коды? Обоснуйте.
2. Почему на проверку «а» сервер отвечает 415, а на проверку «б» — 422? В чём принципиальная разница между этими ситуациями?
3. Какой заголовок сервер обязан прислать вместе с кодом 405 и что он сообщает клиенту? Проверьте, есть ли он в вашем ответе.

Остановите сервер по `Ctrl+C`.

---

### Задание 3.4: Настоящий сервлет в контейнере

Теперь запустим сервлет внутри настоящего контейнера и посмотрим, что берёт на себя Tomcat: серверный сокет, разбор текста запроса, пул потоков, жизненный цикл объекта. В заданиях 3.1 и 3.2 всё это писали и настраивали вы сами — здесь не будет ни `ServerSocket`, ни `Executors.newFixedThreadPool`, ни ручной склейки заголовков.

1. Откройте [https://start.spring.io](https://start.spring.io) и сгенерируйте проект:
   - **Project:** Maven, **Language:** Java, **Spring Boot:** 3.5.x
   - **Group:** `mpt.it`, **Artifact:** `webapp`, **Package name:** `lecture.eight.webapp`
   - **Packaging:** Jar, **Java:** 21
   - **Dependencies:** только **Spring Web**

2. Распакуйте архив, откройте в IDE. Зависимость `spring-boot-starter-web` уже приносит встроенный Tomcat и API сервлетов (`jakarta.servlet`) — ничего добавлять в `pom.xml` не нужно.

3. В классе приложения `lecture.eight.webapp.WebappApplication` добавьте импорт `org.springframework.boot.web.servlet.ServletComponentScan` и аннотацию `@ServletComponentScan` рядом с `@SpringBootApplication` — без неё Spring Boot не найдёт классы, помеченные `@WebServlet`, `@WebFilter` и `@WebListener`.

4. Создайте пакет `lecture.eight.webapp.servlet` и перенесите в него класс `HelloServlet` из раздела 7.5 Лекции 8 — целиком, изменив только первую строку на `package lecture.eight.webapp.servlet;`. Сервлет отвечает на `GET /hello`, считает обращения в `AtomicInteger` и печатает сообщения в `init()` и `destroy()`.

5. Запустите приложение (из каталога проекта):

```bash
./mvnw spring-boot:run      # Linux / macOS
```

```powershell
.\mvnw.cmd spring-boot:run  # Windows
```

6. Проверьте:

```bash
curl -i "http://localhost:8080/hello?name=%D0%98%D0%B2%D0%B0%D0%BD"
curl -i "http://localhost:8080/hello"
curl -i -X POST "http://localhost:8080/hello"
```

В первой команде «Иван» записан процентным кодированием: в стартовой строке запроса разрешены только символы ASCII. Браузер кодирует кириллицу сам, а curl отправляет строку как есть — и Tomcat отвечает `400 Bad Request: Invalid character found in the request target`. Попробуйте написать `?name=Иван` без кодирования и убедитесь в этом сами. Кодировать вручную не обязательно — можно поручить это curl:

```bash
curl -i -G "http://localhost:8080/hello" --data-urlencode "name=Иван"
```

**Ответьте письменно:**
1. Сколько раз в консоли появилось сообщение «HelloServlet инициализирован» после десяти запросов? Что это доказывает про количество экземпляров сервлета?
2. Значение заголовка `X-Hit-Number` растёт от запроса к запросу. Что случилось бы, объяви мы счётчик как `private int hits`, и почему?
3. Какой код вернул `POST /hello`? Какой метод класса `HttpServlet` его сформировал, если `doPost` мы не переопределяли?

---

### Задание 3.5: Клиент на Java вместо curl

То же самое, но программой: встроенный `java.net.http.HttpClient` появился в Java 11 и не требует внешних библиотек. Возьмите класс `EchoClient` из раздела 11.6 Лекции 8 и сохраните его без изменений в файл `ru/fa/web/EchoClient.java` — в лекции у него объявлен ровно тот же пакет `ru.fa.web`, что и у двух предыдущих классов, поэтому путь и команда запуска совпадают.

Компилируйте и запускайте из каталога `http-lab`:

```bash
javac -encoding UTF-8 -d out ru/fa/web/EchoClient.java
java -cp out ru.fa.web.EchoClient
```

Доработайте программу самостоятельно: добавьте вывод **всех** заголовков ответа (подсказка — `getResponse.headers().map()`) и направьте её на ваш собственный сервер `http://localhost:8081/api/books` вместо эхо-сервера.

Для второй части задания снова запустите `LibraryServer` из задания 3.2 — вы остановили его в конце задания 3.3. Откройте отдельное окно терминала в каталоге `http-lab` и выполните:

```bash
java -cp out ru.fa.web.LibraryServer
```

Порты не конфликтуют: Spring Boot из задания 3.4 занимает 8080, библиотека слушает 8081, оба сервера могут работать одновременно. Если этот шаг пропустить, `EchoClient` завершится с `ConnectException: Connection refused` — и это, кстати, полезно увидеть один раз своими глазами.

**Ответьте письменно:**
1. Здесь два разных тайм-аута — `connectTimeout` у клиента и `timeout` у запроса. Чем они отличаются и почему нужны оба?
2. Что делает `HttpResponse.BodyHandlers.ofString()` и какой обработчик вы возьмёте, чтобы скачать файл на 2 гигабайта, не загружая его целиком в память?
3. Метод по умолчанию у `HttpRequest.Builder` — `GET`. Как изменится код, если нужно отправить `DELETE`?

---

## Часть 4: Проектирование REST API «Библиотека»

Теория URI усваивается только на своей предметной области. Спроектируем API библиотеки — той самой, чья картотека была нашей аналогией на лекции: завести карточку, посмотреть карточку, поправить карточку, выбросить карточку. Сущности такие:

- **Книга** (`book`): идентификатор, название, автор, год, жанр, статус (доступна / выдана).
- **Читатель** (`reader`): идентификатор, ФИО, номер билета.
- **Выдача** (`loan`): идентификатор, книга, читатель, дата выдачи, срок возврата.
- **Отзыв** (`review`): идентификатор, книга, читатель, оценка, текст.

### Задание 4.1: Таблица «операция — метод — URI — код ответа»

Спроектируйте API и оформите его таблицей. Первые три строки заполнены как образец, остальные — ваша работа. Минимум **16 строк**, все четыре сущности должны быть покрыты.

| № | Операция (что нужно пользователю) | Метод | URI | Успешный код | Возможные коды ошибок |
|---|-----------------------------------|-------|-----|--------------|-----------------------|
| 1 | Получить список всех книг | `GET` | `/api/v1/books` | 200 | 500 |
| 2 | Создать книгу | `POST` | `/api/v1/books` | 201 + `Location` | 400, 415, 422 |
| 3 | Получить книгу по идентификатору | `GET` | `/api/v1/books/{id}` | 200 | 404 |
| 4 | Заменить книгу целиком | | | | |
| 5 | Изменить только жанр книги | | | | |
| 6 | Удалить книгу | | | | |
| 7 | Найти книги жанра «драма» | | | | |
| 8 | Получить вторую страницу списка по 20 книг | | | | |
| 9 | Отсортировать книги по году по убыванию | | | | |
| 10 | Получить список отзывов на книгу 42 | | | | |
| 11 | Добавить отзыв к книге 42 | | | | |
| 12 | Удалить отзыв 7 | | | | |
| 13 | Получить список читателей | | | | |
| 14 | Зарегистрировать читателя | | | | |
| 15 | Узнать, какие методы поддерживает `/api/v1/books/42` | | | | |
| 16 | Проверить, изменилась ли книга 42, не скачивая её | | | | |

**Ответьте письменно:**
1. Почему операции 7, 8 и 9 попали в строку запроса, а не в путь? Сформулируйте критерий, по которому вы это решили.
2. Какие коды вы поставили для операции 6 и почему именно их? Что вернёт повторное удаление той же книги?
3. Операция 5 — это `PUT` или `PATCH`? Объясните разницу применительно к этому конкретному случаю.

---

### Задание 4.2: Разбор плохих URI

Перед вами фрагмент документации API, написанного без оглядки на REST. Для каждой строки укажите, какое правило нарушено, и предложите корректный вариант.

```
POST /api/getBookById?id=42
GET  /api/BookReviews
POST /api/books/42/doDelete
GET  /api/book/42.json
GET  /api/books/genre/drama/year/1869
POST /api/updateReaderEmail
GET  /api/books/42/
POST /api/books/42/setStatus?status=borrowed
```

Оформите таблицей:

| Как в документации | Какое правило нарушено | Как правильно |
|--------------------|------------------------|---------------|
| `POST /api/getBookById?id=42` | | |
| ... | | |

**Ответьте письменно:**
1. Какие два нарушения встречаются в этом списке чаще всего?
2. Строка `GET /api/books/42/` отличается от `/api/books/42` одним символом. Почему это всё-таки проблема?
3. Что не так с `/api/book/42.json` с точки зрения согласования содержимого (content negotiation)? Как получить тот же результат правильно?

---

### Задание 4.3: Операции, которые не сводятся к CRUD

В библиотеке есть действия, которые не описываются словами «создать / прочитать / изменить / удалить»: выдать книгу, вернуть её, продлить срок, напомнить о просрочке, собрать отчёт. Соблазн велик — написать `POST /api/books/42/borrow`. Это глагол в URI, то самое, что мы запретили в задании 4.2.

Главный приём проектирования REST API: **найти в действии существительное**. «Выдача» — это не действие, а сущность: у неё есть книга, читатель, дата и срок. Значит, «выдать книгу» — это создать ресурс «выдача». Проделайте то же самое с остальными действиями:

| Действие | Ресурс, который вы нашли | Метод | URI | Код успеха |
|----------|--------------------------|-------|-----|-----------|
| Выдать книгу 42 читателю 7 | выдача (loan) | `POST` | `/api/v1/loans` | 201 + `Location` |
| Вернуть книгу 42 | | | | |
| Продлить срок выдачи 17 | | | | |
| Отправить напоминание читателю 7 | | | | |
| Отчёт за март 2025 | | | | |

**Ответьте письменно:**
1. Почему выдача создаётся как `POST /api/v1/loans`, а не как `POST /api/v1/books/42/borrow`? Назовите два практических преимущества.
2. Напоминание плохо ложится на ресурсную модель. Какой код ответа вы выберете, если письмо отправляется в фоновой очереди и в момент ответа ещё не ушло?
3. Отчёт за март — это ресурс или действие? Обоснуйте свой ответ и приведите URI.

---

### Задание 4.4: Проверка на шесть ограничений

Четыре решения из некоторого «REST API». Для каждого укажите нарушенное ограничение REST и способ исправления, оформив таблицей «номер — ограничение — как исправить».

1. После входа сервер кладёт роль пользователя в `HttpSession` и при каждом следующем запросе достаёт её оттуда. Токен клиенту не выдаётся.
2. Все ответы отдаются с `Cache-Control: no-store`, включая справочник жанров, который меняется раз в год.
3. Чтобы получить книгу, клиент отправляет `POST /api/gateway` с телом `{"entity":"book","action":"read","id":42}`.
4. Клиент зашивает в код, что за адресом `/api/v1` стоит приложение на порту 8080, и при появлении балансировщика перестаёт работать.

**Ответьте письменно:**
1. Какое ограничение нарушено в каждом из четырёх пунктов?
2. Какое из шести ограничений REST необязательное и что оно означает?
3. Нарушение из пункта 1 очень распространено. Какие два способа его устранения вы знаете (подсказка — Лекция 7)?

---

## Часть 5: Уровни зрелости по Ричардсону

Шкала Ричардсона — это лестница. Стоять на первой ступеньке не стыдно; стыдно называть первую ступеньку четвёртой. На практике почти все API живут на втором уровне, и это нормально — важно понимать, где вы находитесь и почему.

### Задание 5.1: Определите уровень

Перед вами четыре фрагмента диалогов «клиент — сервер» (`-->` — запрос, `<--` — ответ). Для каждого определите уровень зрелости (0, 1, 2 или 3) и обоснуйте вывод двумя-тремя признаками.

```
=== Фрагмент А ===
--> POST /api/service            {"method":"deleteBook","params":{"id":42}}
<-- HTTP/1.1 200 OK              {"status":"ok"}

=== Фрагмент Б ===
--> DELETE /api/books/42
<-- HTTP/1.1 204 No Content

=== Фрагмент В ===
--> POST /api/books/42           {"action":"delete"}
<-- HTTP/1.1 200 OK              {"status":"ok"}

=== Фрагмент Г ===
--> GET /api/books/42
    Accept: application/json
<-- HTTP/1.1 200 OK
    Content-Type: application/json

    {"id":42,"title":"Война и мир","status":"available",
     "_links":{"self":{"href":"/api/books/42"},
               "borrow":{"href":"/api/books/42/loans","method":"POST"}}}
```

**Ответьте письменно:**
1. Какой уровень у каждого из четырёх фрагментов? По каким признакам вы это определили?
2. Фрагмент А возвращает `200 OK` даже при ошибке — статус сообщается в теле. Чем это плохо для промежуточных узлов сети (прокси, кеш, балансировщик)?
3. На каком уровне находится API, которое вы спроектировали в задании 4.1? Что нужно добавить, чтобы поднять его на следующий?

---

### Задание 5.2: Поднимите API на второй уровень

Некий сервис «Библиотека» построен по уровню 0: единственный адрес `/api/library`, единственный метод `POST`, всё остальное — в теле.

```
POST /api/library   {"cmd":"listBooks"}
POST /api/library   {"cmd":"getBook","id":42}
POST /api/library   {"cmd":"addBook","title":"Война и мир","year":1869}
POST /api/library   {"cmd":"updateBook","id":42,"title":"Война и миръ"}
POST /api/library   {"cmd":"removeBook","id":42}
POST /api/library   {"cmd":"listReaders"}
POST /api/library   {"cmd":"addReader","name":"Иванов"}
```

Перепишите все семь операций на уровень 2 и оформите таблицей:

| Было (уровень 0) | Стало (уровень 2): метод + URI | Тело запроса | Код успеха |
|------------------|--------------------------------|--------------|-----------|
| `{"cmd":"listBooks"}` | `GET /api/v1/books` | нет | 200 |
| ... | | | |

**Ответьте письменно:**
1. У каких операций после переписывания исчезло тело запроса и почему это хорошо?
2. Какие из семи операций стали кешируемыми и что это даёт?
3. Какие из семи операций стали идемпотентными? Что теперь может безопасно сделать прокси при обрыве соединения?

---

### Задание 5.3: Доведите свой сервер до третьего уровня

Вернитесь к файлу `ru/fa/web/LibraryServer.java` из задания 3.2. Сейчас он находится на уровне 2: у него есть ресурсы, методы и коды. Добавим гипермедиа.

Остановите `LibraryServer`, запущенный в задании 3.5 (`Ctrl+C` в его окне терминала), — иначе порт 8081 останется занят.

Замените объявление записи `Book` целиком на следующее:

```java
    /** Ресурс «книга». Представление включает ссылки на доступные действия — это HATEOAS. */
    record Book(long id, String title, int year) {
        String toJson() {
            return "{\"id\":" + id
                    + ",\"title\":\"" + title + "\""
                    + ",\"year\":" + year
                    + ",\"_links\":{"
                    + "\"self\":{\"href\":\"/api/books/" + id + "\",\"method\":\"GET\"},"
                    + "\"update\":{\"href\":\"/api/books/" + id + "\",\"method\":\"PUT\"},"
                    + "\"delete\":{\"href\":\"/api/books/" + id + "\",\"method\":\"DELETE\"},"
                    + "\"collection\":{\"href\":\"/api/books\",\"method\":\"GET\"}"
                    + "}}";
        }
    }
```

Пересоберите и запустите сервер, затем во втором терминале создайте книгу и прочитайте её:

```bash
javac -encoding UTF-8 -d out ru/fa/web/LibraryServer.java
java -cp out ru.fa.web.LibraryServer
# во втором терминале:
curl -i -X POST http://localhost:8081/api/books -H "Content-Type: application/json" -d "@body.json"
curl -i http://localhost:8081/api/books/1
```

**Ответьте письменно:**
1. Что изменилось в ответе и как теперь клиент узнаёт, какие действия ему доступны?
2. Представьте, что у книги появилось поле «статус». Как сервер должен вести себя со ссылкой `borrow`, если книга уже выдана, и какое бизнес-правило при этом уезжает с клиента на сервер?
3. Назовите две причины, по которым третий уровень редко встречается на практике.

---

## Часть 6: Контрольные вопросы

Ответьте письменно:

1. Чем клиент отличается от сервера в клиент-серверной архитектуре? Кто из них инициирует общение и почему это важно?
2. Сравните двухзвенную и трёхзвенную архитектуры. Назовите три проблемы двухзвенной, которые решает третье звено.
3. Чем веб-сервер (Nginx, Apache) отличается от сервера приложений (Tomcat, WildFly)? Что каждый из них умеет и не умеет?
4. Что такое контейнер сервлетов и какие семь шагов он выполняет между приходом байтов в сокет и вызовом вашего кода?
5. Чем развёртывание в виде WAR-архива отличается от исполняемого JAR со встроенным Tomcat? Почему второй подход победил?
6. Перечислите четыре части HTTP-запроса и четыре части HTTP-ответа. Чем они отличаются друг от друга?
7. Из каких частей состоит URL? Какая часть никогда не отправляется на сервер?
8. Перечислите семь методов HTTP и назначение каждого. В чём разница между `POST` и `PUT`?
9. Что такое безопасный метод и что такое идемпотентный метод? Приведите по два примера каждого.
10. Почему `DELETE` считается идемпотентным, хотя он изменяет состояние сервера? Почему `PATCH` — не считается?
11. Назовите пять классов кодов состояний. Чем принципиально отличаются классы `4xx` и `5xx`?
12. В чём разница между кодами 401 и 403? Между 400 и 422? Между 404 и 405?
13. Когда сервер обязан вернуть 201, и какой заголовок при этом обязателен?
14. Чем отличаются заголовки `Content-Type` и `Accept`? Почему в GET-запросе `Content-Type` не нужен?
15. Что означает свойство stateless и какое преимущество оно даёт при масштабировании? Чем за него платят?
16. Как работает связка cookie и серверной сессии? Зачем нужны атрибуты `HttpOnly`, `Secure` и `SameSite`?
17. Опишите жизненный цикл сервлета. Сколько экземпляров сервлета создаёт контейнер и какое следствие это имеет для полей класса?
18. Назовите по пять методов интерфейсов `HttpServletRequest` и `HttpServletResponse` и объясните, что они делают. Почему тело запроса можно прочитать только один раз?
19. Перечислите шесть ограничений REST. Какое из них необязательное и какое чаще всего нарушают на практике?
20. Чем ресурс отличается от представления? Приведите пример одного ресурса в трёх разных представлениях.
21. Сформулируйте пять правил именования URI. Что должно попадать в путь, а что — в строку запроса?
22. Назовите четыре уровня зрелости Ричардсона. Приведите таблицу соответствия CRUD, SQL, HTTP-методов и кодов ответов.

---

## Результаты занятия

К концу занятия вы должны сдать:

1. **Разбор HTTP-обмена:** размеченный вывод `curl -v` с подписанными частями запроса и ответа (задание 1.2) и таблица разбора URL (задание 1.3).
2. **Журнал запросов к `postman-echo.com`:** сводная таблица минимум из 12 строк с методами, адресами, заголовками и кодами ответов (задание 2.7), а также раскодированное значение заголовка `Authorization` (задание 2.5).
3. **Файлы `body.json` и `bad.json`** и рабочие команды `curl` для вашей операционной системы.
4. **Исходники и результаты запуска трёх серверов:**
   - `RawHttpServer.java` со сравнением заголовков браузера и curl;
   - `LibraryServer.java` с полным CRUD, кодами 200 / 201 / 204 / 400 / 404 / 405 / 415 / 422 и заголовками `Location` и `Allow`;
   - Spring Boot проект `webapp` с `HelloServlet` и `@ServletComponentScan`.
5. **Таблица проверки собственного API** из задания 3.3 с ожидаемыми и полученными кодами, включая четыре сломанных запроса.
6. **`EchoClient.java`**, доработанный так, чтобы выводить все заголовки ответа и обращаться к вашему собственному серверу.
7. **Проект REST API «Библиотека»:** таблица «операция — метод — URI — код ответа» минимум из 16 строк (задание 4.1), таблица исправления плохих URI (задание 4.2), таблица превращения действий в ресурсы (задание 4.3) и разбор четырёх нарушений ограничений REST (задание 4.4).
8. **Анализ по Ричардсону:** уровни четырёх фрагментов с обоснованием (задание 5.1), таблица переписывания API с уровня 0 на уровень 2 (задание 5.2) и `LibraryServer` с ссылками `_links` в ответе (задание 5.3).
9. Ответы на контрольные вопросы (1–22).
