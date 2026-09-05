# Тест 8: Веб-архитектура (Лекция 8)

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

<!-- ===== РАЗДЕЛ 1: Протокол HTTP: структура сообщений, URL и заголовки (Вопросы 1–15) ===== -->

<div class="quiz-question" data-correct="1">
<h4>Вопрос 1. Что такое HTTP?</h4>

<div class="quiz-option" data-index="0">Транспортный протокол, который отвечает за надёжную доставку пакетов и их порядок</div>
<div class="quiz-option" data-index="1">Прикладной протокол передачи данных по модели «запрос — ответ», работающий поверх TCP</div>
<div class="quiz-option" data-index="2">Двоичный формат сериализации объектов для передачи по сети</div>
<div class="quiz-option" data-index="3">Протокол сетевого уровня, отвечающий за маршрутизацию пакетов между узлами</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 2. Какие порты HTTP и HTTPS используют по умолчанию?</h4>

<div class="quiz-option" data-index="0">8080 для HTTP и 8443 для HTTPS</div>
<div class="quiz-option" data-index="1">443 для HTTP и 80 для HTTPS</div>
<div class="quiz-option" data-index="2">21 для HTTP и 22 для HTTPS</div>
<div class="quiz-option" data-index="3">80 для HTTP и 443 для HTTPS</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 3. Из каких частей и в каком порядке состоит HTTP-запрос?</h4>

<div class="quiz-option" data-index="0">Заголовки, стартовая строка, пустая строка, тело</div>
<div class="quiz-option" data-index="1">Стартовая строка, тело, пустая строка, заголовки</div>
<div class="quiz-option" data-index="2">Стартовая строка, заголовки, пустая строка, тело</div>
<div class="quiz-option" data-index="3">Строка состояния, заголовки, тело, пустая строка</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 4. Чем первая строка ответа отличается от первой строки запроса?</h4>

<div class="quiz-option" data-index="0">В запросе это «МЕТОД ПУТЬ ВЕРСИЯ», в ответе — «ВЕРСИЯ КОД ПОЯСНЕНИЕ»</div>
<div class="quiz-option" data-index="1">Ничем: обе имеют вид «МЕТОД ПУТЬ ВЕРСИЯ»</div>
<div class="quiz-option" data-index="2">В ответе она содержит только код состояния, без версии протокола</div>
<div class="quiz-option" data-index="3">В ответе первой строки нет вообще, ответ начинается сразу с заголовков</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 5. Какой последовательностью разделяются строки внутри HTTP-сообщения?</h4>

<div class="quiz-option" data-index="0">Только `\n` (LF)</div>
<div class="quiz-option" data-index="1">`\r\n` (CR LF)</div>
<div class="quiz-option" data-index="2">`\n\r` (LF CR)</div>
<div class="quiz-option" data-index="3">Символом `;` без перевода строки</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 6. Сервер собирает ответ вручную: пишет строку `HTTP/1.1 200 OK\r\n`, затем `Content-Type: ...\r\n`, затем `Content-Length: ...\r\n` и сразу же тело. Что здесь не так?</h4>

<div class="quiz-option" data-index="0">После блока заголовков не поставлена пустая строка (`\r\n`), поэтому клиент воспримет тело как продолжение заголовков и будет ждать их окончания</div>
<div class="quiz-option" data-index="1">`Content-Length` должен считаться в символах, а не в байтах</div>
<div class="quiz-option" data-index="2">Строка состояния обязана идти после заголовков, а не до них</div>
<div class="quiz-option" data-index="3">Заголовки нельзя записывать в кодировке US-ASCII</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 7. Зачем в HTTP/1.1 сделали обязательным заголовок `Host`?</h4>

<div class="quiz-option" data-index="0">Он сообщает серверу IP-адрес клиента, чтобы тот знал, куда отправить ответ</div>
<div class="quiz-option" data-index="1">Он задаёт имя пользователя для аутентификации на сервере</div>
<div class="quiz-option" data-index="2">На одном IP-адресе и порту размещаются десятки сайтов, и сервер по нему выбирает нужный виртуальный хост</div>
<div class="quiz-option" data-index="3">Он указывает адрес, на который нужно перенаправить ответ после обработки</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 8. В адресе `https://library.example.com:8443/api/books/42?format=short&lang=ru#reviews` какая часть вообще не отправляется на сервер?</h4>

<div class="quiz-option" data-index="0">Порт `8443`</div>
<div class="quiz-option" data-index="1">Путь `/api/books/42`</div>
<div class="quiz-option" data-index="2">Строка запроса `format=short&lang=ru`</div>
<div class="quiz-option" data-index="3">Фрагмент `#reviews`</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 9. Почему нельзя передавать пароль или токен в строке запроса (query string)?</h4>

<div class="quiz-option" data-index="0">URL целиком попадает в логи веб-сервера и прокси, в историю браузера и в заголовок `Referer` — секрет утекает сразу в несколько мест</div>
<div class="quiz-option" data-index="1">Строка запроса передаётся в открытом виде, даже если используется HTTPS</div>
<div class="quiz-option" data-index="2">Длина строки запроса ограничена 32 символами, и токен туда не поместится</div>
<div class="quiz-option" data-index="3">Серверы приложений технически не умеют читать строку запроса у защищённых соединений</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 10. Чем заголовок `Content-Type` отличается от заголовка `Accept`?</h4>

<div class="quiz-option" data-index="0">`Content-Type` описывает желаемый формат ответа, а `Accept` — формат отправляемого тела</div>
<div class="quiz-option" data-index="1">`Content-Type` описывает формат тела, которое отправляется прямо сейчас, а `Accept` — формат, который клиент хочет получить в ответ</div>
<div class="quiz-option" data-index="2">Это синонимы, `Accept` — устаревшее название того же заголовка</div>
<div class="quiz-option" data-index="3">`Content-Type` встречается только в ответах, а `Accept` — только в запросах</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 11. Как называется механизм, при котором клиент через `Accept` просит формат, а сервер выбирает подходящий, и каким кодом сервер отвечает, если не может выполнить просьбу?</h4>

<div class="quiz-option" data-index="0">Маршрутизация запросов; код 404 Not Found</div>
<div class="quiz-option" data-index="1">Мультиплексирование; код 415 Unsupported Media Type</div>
<div class="quiz-option" data-index="2">Согласование содержимого (content negotiation); код 406 Not Acceptable</div>
<div class="quiz-option" data-index="3">Условный запрос; код 304 Not Modified</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 12. Что означает свойство «отсутствие состояния» (stateless) у HTTP?</h4>

<div class="quiz-option" data-index="0">Сервер не хранит данные на диске, вся информация живёт только в оперативной памяти</div>
<div class="quiz-option" data-index="1">Клиент не сохраняет между запросами ничего, включая cookie</div>
<div class="quiz-option" data-index="2">TCP-соединение обязательно закрывается после каждого запроса и никогда не переиспользуется</div>
<div class="quiz-option" data-index="3">Сервер не хранит контекст клиента между запросами, каждый запрос самодостаточен — поэтому любая из копий сервера может обработать любой запрос</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 13. В чём разница между cookie и сессией?</h4>

<div class="quiz-option" data-index="0">Cookie хранится на сервере, а сессия — в браузере пользователя</div>
<div class="quiz-option" data-index="1">Это одно и то же: `JSESSIONID` и есть сессия</div>
<div class="quiz-option" data-index="2">Cookie — фрагмент данных, который хранит клиент и присылает обратно; сессия — область данных на сервере, которую находят по идентификатору из cookie</div>
<div class="quiz-option" data-index="3">Cookie работает только по HTTPS, а сессия — только по обычному HTTP</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 14. Какой атрибут cookie делает её недоступной из JavaScript и тем самым защищает от кражи через XSS?</h4>

<div class="quiz-option" data-index="0">`Secure`</div>
<div class="quiz-option" data-index="1">`HttpOnly`</div>
<div class="quiz-option" data-index="2">`SameSite`</div>
<div class="quiz-option" data-index="3">`Path`</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 15. Что изменил HTTP/2 по сравнению с HTTP/1.1?</h4>

<div class="quiz-option" data-index="0">Сохранил семантику (методы, коды, заголовки), но перешёл на двоичные кадры, мультиплексирование и сжатие заголовков HPACK</div>
<div class="quiz-option" data-index="1">Ввёл новые методы запросов и новые классы кодов состояний</div>
<div class="quiz-option" data-index="2">Заменил TCP на QUIC поверх UDP</div>
<div class="quiz-option" data-index="3">Отказался от заголовков, перенеся все метаданные в тело сообщения</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 2: Методы HTTP и коды состояний (Вопросы 16–29) ===== -->

<div class="quiz-question" data-correct="2">
<h4>Вопрос 16. Чем POST принципиально отличается от PUT?</h4>

<div class="quiz-option" data-index="0">POST создаёт ресурс, а PUT только читает его</div>
<div class="quiz-option" data-index="1">POST передаёт данные в строке запроса, а PUT — в теле сообщения</div>
<div class="quiz-option" data-index="2">POST отправляется на коллекцию, и идентификатор назначает сервер; PUT отправляется на конкретный ресурс, адрес которого выбрал клиент</div>
<div class="quiz-option" data-index="3">POST идемпотентен, а PUT — нет</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 17. Какой метод одновременно и безопасный (safe), и идемпотентный?</h4>

<div class="quiz-option" data-index="0">POST</div>
<div class="quiz-option" data-index="1">PATCH</div>
<div class="quiz-option" data-index="2">DELETE</div>
<div class="quiz-option" data-index="3">GET</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 18. Почему DELETE считается идемпотентным, хотя он изменяет данные?</h4>

<div class="quiz-option" data-index="0">Потому что он не удаляет запись, а лишь помечает её как скрытую</div>
<div class="quiz-option" data-index="1">Потому что после первого удаления ресурса нет и после второго его тоже нет — состояние сервера одинаково, хотя код ответа может отличаться</div>
<div class="quiz-option" data-index="2">Потому что контейнер сервлетов кеширует ответы на DELETE</div>
<div class="quiz-option" data-index="3">Потому что спецификация прямо запрещает отправлять DELETE повторно</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 19. Почему PATCH в общем случае считается неидемпотентным?</h4>

<div class="quiz-option" data-index="0">Потому что PATCH всегда передаёт представление ресурса целиком</div>
<div class="quiz-option" data-index="1">Потому что ответы на PATCH запрещено кешировать</div>
<div class="quiz-option" data-index="2">Потому что тело патча может описывать относительное изменение («увеличить счётчик выдач на 1»), и каждый повтор будет менять данные заново</div>
<div class="quiz-option" data-index="3">Потому что PATCH не поддерживается контейнерами сервлетов</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 20. Какое практическое следствие имеет идемпотентность для браузеров и промежуточных прокси?</h4>

<div class="quiz-option" data-index="0">При обрыве связи они могут автоматически повторить GET или PUT, но не станут повторять POST</div>
<div class="quiz-option" data-index="1">Они могут повторить любой запрос, потому что все методы HTTP идемпотентны</div>
<div class="quiz-option" data-index="2">Они кешируют ответы на POST так же охотно, как и на GET</div>
<div class="quiz-option" data-index="3">Они блокируют повторную отправку GET после первого выполнения</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 21. Какой метод возвращает только заголовки, без тела, и зачем он нужен?</h4>

<div class="quiz-option" data-index="0">OPTIONS — чтобы узнать список разрешённых для ресурса методов</div>
<div class="quiz-option" data-index="1">TRACE — чтобы проследить путь запроса через цепочку прокси</div>
<div class="quiz-option" data-index="2">CONNECT — чтобы установить туннель до целевого узла</div>
<div class="quiz-option" data-index="3">HEAD — например, чтобы проверить размер и дату большого файла, прежде чем качать его целиком</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 22. Что окажется в переменной `verdict` после выполнения `int code = 404; String verdict = code &lt; 200 ? "информация" : code &lt; 300 ? "успех" : code &lt; 400 ? "перенаправление" : code &lt; 500 ? "ошибка клиента" : "ошибка сервера";`?</h4>

<div class="quiz-option" data-index="0">`ошибка клиента`</div>
<div class="quiz-option" data-index="1">`перенаправление`</div>
<div class="quiz-option" data-index="2">`успех`</div>
<div class="quiz-option" data-index="3">`ошибка сервера`</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 23. Приложение возвращает 500 Internal Server Error в ответ на некорректно заполненную форму. Почему это ошибка проектирования?</h4>

<div class="quiz-option" data-index="0">Код 500 нельзя использовать вместе с телом в формате JSON</div>
<div class="quiz-option" data-index="1">Спецификация HTTP вообще запрещает возвращать код 500</div>
<div class="quiz-option" data-index="2">Класс 5xx означает «виноват сервер, попробуйте позже», поэтому клиент будет повторять заведомо безнадёжный запрос, а в журналах появится несуществующая авария — здесь нужен код класса 4xx</div>
<div class="quiz-option" data-index="3">Код 500 заставляет контейнер сервлетов перезапустить приложение</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 24. Какой код и какой заголовок обязан вернуть сервер после успешного создания ресурса методом POST?</h4>

<div class="quiz-option" data-index="0">200 OK и заголовок `Content-Location`</div>
<div class="quiz-option" data-index="1">204 No Content без дополнительных заголовков</div>
<div class="quiz-option" data-index="2">202 Accepted и заголовок `Retry-After`</div>
<div class="quiz-option" data-index="3">201 Created и заголовок `Location` с адресом созданного ресурса</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 25. Клиент отправил синтаксически корректный JSON, но забыл заголовок `Content-Type`. Какой код вернёт аккуратно написанный сервер?</h4>

<div class="quiz-option" data-index="0">415 Unsupported Media Type</div>
<div class="quiz-option" data-index="1">400 Bad Request</div>
<div class="quiz-option" data-index="2">406 Not Acceptable</div>
<div class="quiz-option" data-index="3">422 Unprocessable Content</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 26. В чём разница между кодами 401 и 403?</h4>

<div class="quiz-option" data-index="0">401 закрывает доступ навсегда, а 403 — временно</div>
<div class="quiz-option" data-index="1">401 означает «вы не представились или токен неверен», а 403 — «мы знаем, кто вы, но вам сюда нельзя», и повторный вход тут не поможет</div>
<div class="quiz-option" data-index="2">401 возвращают только API, а 403 — только обычные веб-страницы</div>
<div class="quiz-option" data-index="3">Разницы нет, это синонимы из разных версий протокола</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 27. Ресурс `/api/books` существует, но удалять разрешено только конкретную книгу. Что вернёт корректный сервер на запрос `DELETE /api/books`?</h4>

<div class="quiz-option" data-index="0">404 Not Found, потому что удалять по этому адресу нечего</div>
<div class="quiz-option" data-index="1">400 Bad Request с описанием ошибки в теле</div>
<div class="quiz-option" data-index="2">405 Method Not Allowed вместе с заголовком `Allow: GET, POST`</div>
<div class="quiz-option" data-index="3">501 Not Implemented</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 28. JSON разобран без единой ошибки, но год издания книги указан как 3025. Какой код точнее всего описывает ситуацию?</h4>

<div class="quiz-option" data-index="0">422 Unprocessable Content</div>
<div class="quiz-option" data-index="1">400 Bad Request</div>
<div class="quiz-option" data-index="2">409 Conflict</div>
<div class="quiz-option" data-index="3">415 Unsupported Media Type</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 29. Перед приложением стоит Nginx, и он не смог достучаться до Tomcat. Какой код увидит клиент?</h4>

<div class="quiz-option" data-index="0">500 Internal Server Error</div>
<div class="quiz-option" data-index="1">502 Bad Gateway</div>
<div class="quiz-option" data-index="2">503 Service Unavailable</div>
<div class="quiz-option" data-index="3">504 Gateway Timeout</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 3: Клиент-серверная архитектура и серверы приложений (Вопросы 30–38) ===== -->

<div class="quiz-question" data-correct="2">
<h4>Вопрос 30. Какое свойство отличает клиент-серверную модель взаимодействия?</h4>

<div class="quiz-option" data-index="0">Обе стороны равноправны, и любая может начать обмен в удобный момент</div>
<div class="quiz-option" data-index="1">Сервер периодически сам отправляет клиенту данные без запроса</div>
<div class="quiz-option" data-index="2">Асимметрия ролей: клиент всегда инициирует общение, сервер всегда ждёт запроса</div>
<div class="quiz-option" data-index="3">Клиент и сервер обязательно работают на разных физических машинах</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 31. Чем плоха двухзвенная архитектура с толстым клиентом?</h4>

<div class="quiz-option" data-index="0">Она вообще не позволяет использовать SQL</div>
<div class="quiz-option" data-index="1">Она требует обязательного применения HTTPS на каждом рабочем месте</div>
<div class="quiz-option" data-index="2">Она принципиально не поддерживает многопользовательскую работу</div>
<div class="quiz-option" data-index="3">Логика размазана по рабочим местам, у каждого клиента есть пароль от базы, и каждый держит собственное соединение с ней</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 32. Как называются три звена трёхзвенной архитектуры?</h4>

<div class="quiz-option" data-index="0">Браузер, веб-сервер, файловая система</div>
<div class="quiz-option" data-index="1">Presentation tier (представление), Application tier (логика), Data tier (данные)</div>
<div class="quiz-option" data-index="2">Контроллер, сервис, репозиторий</div>
<div class="quiz-option" data-index="3">Клиент, прокси, балансировщик нагрузки</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 33. Что умеет веб-сервер вроде Nginx или Apache и чего он не умеет?</h4>

<div class="quiz-option" data-index="0">Умеет отдавать статические файлы, терминировать TLS, сжимать ответы и балансировать нагрузку, но не умеет выполнять вашу бизнес-логику</div>
<div class="quiz-option" data-index="1">Умеет исполнять Java-код и ходить в базу, но не умеет отдавать файлы с диска</div>
<div class="quiz-option" data-index="2">Умеет только шифровать трафик, всё остальное делает контейнер сервлетов</div>
<div class="quiz-option" data-index="3">Умеет ровно то же, что и сервер приложений, разница только в названии</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 34. Чем контейнер сервлетов отличается от полного сервера приложений Jakarta EE?</h4>

<div class="quiz-option" data-index="0">Контейнер сервлетов — это надстройка, которую устанавливают поверх WildFly</div>
<div class="quiz-option" data-index="1">Контейнер сервлетов работает только со статическими файлами</div>
<div class="quiz-option" data-index="2">Различий нет: Tomcat и WildFly — полные серверы приложений</div>
<div class="quiz-option" data-index="3">Контейнер сервлетов реализует только спецификацию Jakarta Servlet (Tomcat, Jetty, Undertow), а полный сервер приложений — всю платформу Jakarta EE, включая JPA, CDI, JTA, JMS и EJB (WildFly, Payara)</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 35. Почему в Spring Boot-проекте вы никогда не пишете `new ServerSocket(8080)`?</h4>

<div class="quiz-option" data-index="0">Потому что Spring использует UDP вместо TCP</div>
<div class="quiz-option" data-index="1">Потому что сокет открывает встроенный контейнер сервлетов: Tomcat слушает порт, читает и разбирает текст HTTP и вызывает нужный компонент</div>
<div class="quiz-option" data-index="2">Потому что Java запрещает создавать серверные сокеты в веб-приложениях</div>
<div class="quiz-option" data-index="3">Потому что порт открывает операционная система при старте JVM</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 36. Зачем в продакшене перед Tomcat ставят Nginx?</h4>

<div class="quiz-option" data-index="0">Чтобы Tomcat вообще смог выполнять Java-код — без прокси он этого не умеет</div>
<div class="quiz-option" data-index="1">Чтобы преобразовывать JSON в HTML перед отправкой браузеру</div>
<div class="quiz-option" data-index="2">Чтобы Nginx отдавал статику, терминировал HTTPS, сжимал ответы и распределял нагрузку, оставив приложению только динамику</div>
<div class="quiz-option" data-index="3">Чтобы обойти ограничение Tomcat на количество зарегистрированных сервлетов</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 37. В чём разница между развёртыванием в виде WAR и в виде исполняемого JAR?</h4>

<div class="quiz-option" data-index="0">WAR содержит исходный код, а JAR — только скомпилированные классы</div>
<div class="quiz-option" data-index="1">WAR работает только под Windows, а JAR — на любой платформе</div>
<div class="quiz-option" data-index="2">В WAR нельзя положить зависимости, а в JAR можно</div>
<div class="quiz-option" data-index="3">WAR кладут в заранее установленный контейнер, а исполняемый JAR несёт встроенный Tomcat внутри себя и запускается командой `java -jar`</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 38. Чем тонкий клиент отличается от толстого?</h4>

<div class="quiz-option" data-index="0">У тонкого клиента логика на сервере, обновление одно на всех и установка не нужна, но он не работает офлайн и сильнее нагружает сервер</div>
<div class="quiz-option" data-index="1">Тонкий клиент просто занимает меньше места на диске сервера</div>
<div class="quiz-option" data-index="2">Тонкий клиент умеет работать офлайн, а толстый — только в сети</div>
<div class="quiz-option" data-index="3">Тонкий клиент — это всегда мобильное приложение, а толстый — веб-страница</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 4: Сервлеты (Вопросы 39–49) ===== -->

<div class="quiz-question" data-correct="3">
<h4>Вопрос 39. Что такое сервлет?</h4>

<div class="quiz-option" data-index="0">Класс, который генерирует SQL-запросы к базе данных</div>
<div class="quiz-option" data-index="1">Отдельный процесс операционной системы, обслуживающий ровно один запрос</div>
<div class="quiz-option" data-index="2">Аннотация Spring, помечающая класс как REST-контроллер</div>
<div class="quiz-option" data-index="3">Java-класс, работающий внутри контейнера сервлетов и обрабатывающий запросы клиентов, обычно по HTTP; описан спецификацией Jakarta Servlet</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 40. От какого класса обычно наследуют сервлет и почему не реализуют интерфейс `Servlet` напрямую?</h4>

<div class="quiz-option" data-index="0">От `HttpServlet` — он уже разбирает HTTP и раскладывает запросы по методам `doGet`, `doPost`, `doPut`, `doDelete`</div>
<div class="quiz-option" data-index="1">От `DispatcherServlet` — только он умеет работать с протоколом HTTP</div>
<div class="quiz-option" data-index="2">От `ServletRequest` — именно от него сервлет получает доступ к данным запроса</div>
<div class="quiz-option" data-index="3">От `GenericServlet` — только он поддерживает аннотацию `@WebServlet`</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 41. Сколько раз контейнер вызывает методы `init()`, `service()` и `destroy()`?</h4>

<div class="quiz-option" data-index="0">`init()` и `destroy()` — на каждый запрос, `service()` — один раз при старте</div>
<div class="quiz-option" data-index="1">Все три — на каждый запрос</div>
<div class="quiz-option" data-index="2">`init()` — один раз при создании, `service()` — на каждый запрос, `destroy()` — один раз при остановке приложения</div>
<div class="quiz-option" data-index="3">Все три — ровно по одному разу за всё время жизни приложения</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 42. В сервлете объявлено поле `private int counter = 0;`, а в `doGet` выполняется `counter++` и результат печатается в ответ. Что произойдёт под нагрузкой?</h4>

<div class="quiz-option" data-index="0">Ничего особенного: контейнер создаёт отдельный экземпляр сервлета на каждый запрос</div>
<div class="quiz-option" data-index="1">Значения будут теряться: экземпляр сервлета один на всё приложение, и все запросы идут через него в разных потоках пула — получается гонка данных</div>
<div class="quiz-option" data-index="2">Поле будет сбрасываться в ноль после каждого запроса</div>
<div class="quiz-option" data-index="3">Контейнер выбросит исключение: объявлять изменяемые поля в сервлетах запрещено</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 43. Что делает атрибут `loadOnStartup` в аннотации `@WebServlet`?</h4>

<div class="quiz-option" data-index="0">Задаёт максимальное число одновременных запросов к сервлету</div>
<div class="quiz-option" data-index="1">Указывает, что класс сервлета нужно перезагружать при каждом запросе</div>
<div class="quiz-option" data-index="2">Определяет порядок вызова фильтров перед сервлетом</div>
<div class="quiz-option" data-index="3">Просит контейнер создать и инициализировать сервлет сразу при старте приложения, а не лениво при первом обращении</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 44. Сервлет зарегистрирован на шаблон `/api/books/*`, контекст приложения — `/app`. Что вернёт `request.getPathInfo()` для запроса `GET /app/api/books/42`?</h4>

<div class="quiz-option" data-index="0">`/42`</div>
<div class="quiz-option" data-index="1">`/api/books`</div>
<div class="quiz-option" data-index="2">`/app`</div>
<div class="quiz-option" data-index="3">`/app/api/books/42`</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 45. В `doPost` сначала вызвали `request.getReader()` и прочитали тело, а затем вызвали `request.getInputStream()`. Что произойдёт?</h4>

<div class="quiz-option" data-index="0">Код отработает: `getReader()` и `getInputStream()` читают из независимых буферов</div>
<div class="quiz-option" data-index="1">Второй вызов выбросит `IllegalStateException`: тело запроса читают только одним способом и только один раз</div>
<div class="quiz-option" data-index="2">Второй вызов вернёт `null`, а ответ окажется пустым</div>
<div class="quiz-option" data-index="3">Код не скомпилируется: метод `getInputStream()` не объявлен для HTTP-запроса</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 46. В каком порядке нужно заполнять `HttpServletResponse`?</h4>

<div class="quiz-option" data-index="0">Сначала записать тело через `getWriter()`, потом вызвать `setStatus()` и `setContentType()`</div>
<div class="quiz-option" data-index="1">Порядок не важен: контейнер сам пересобирает ответ перед отправкой</div>
<div class="quiz-option" data-index="2">Сначала код состояния и заголовки, потом тело: после сброса буфера заголовки уже ушли клиенту и менять их поздно</div>
<div class="quiz-option" data-index="3">Сначала вызвать `flushBuffer()`, затем установить `Content-Type` и записать тело</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 47. Почему `response.setContentType("text/html; charset=UTF-8")` нужно вызывать до первой записи в тело ответа?</h4>

<div class="quiz-option" data-index="0">Иначе контейнер вернёт клиенту 415 Unsupported Media Type</div>
<div class="quiz-option" data-index="1">Иначе кодировка не будет применена к уже отправленным данным, и русский текст превратится в «кракозябры»</div>
<div class="quiz-option" data-index="2">Иначе `getWriter()` вернёт `null`</div>
<div class="quiz-option" data-index="3">Иначе `Content-Length` будет посчитан неверно и запрос завершится тайм-аутом</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 48. Зарегистрированы сервлеты на шаблоны `/`, `/api/books/*` и `/api/books/42`. Какой из них обработает запрос `GET /api/books/42`?</h4>

<div class="quiz-option" data-index="0">Сервлет на `/api/books/42` — точное совпадение имеет наивысший приоритет</div>
<div class="quiz-option" data-index="1">Сервлет на `/api/books/*` — префиксный шаблон всегда приоритетнее</div>
<div class="quiz-option" data-index="2">Сервлет на `/` — он ловит вообще всё</div>
<div class="quiz-option" data-index="3">Контейнер откажется стартовать из-за конфликта шаблонов</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 49. Какое место занимает `DispatcherServlet` в цепочке обработки запроса?</h4>

<div class="quiz-option" data-index="0">Это отдельный сетевой сервер, работающий вместо Tomcat</div>
<div class="quiz-option" data-index="1">Это фильтр, который выполняется до всех сервлетов</div>
<div class="quiz-option" data-index="2">Это обычный сервлет, зарегистрированный на `/`; он по `HandlerMapping` находит нужный метод контроллера и вызывает его через `HandlerAdapter`</div>
<div class="quiz-option" data-index="3">Это аннотация, которой помечают классы контроллеров Spring MVC</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 5: Архитектурный стиль REST, CRUD и сравнение стилей (Вопросы 50–60) ===== -->

<div class="quiz-question" data-correct="1">
<h4>Вопрос 50. Что такое REST?</h4>

<div class="quiz-option" data-index="0">Протокол обмена сообщениями поверх HTTP, описанный отдельной спецификацией</div>
<div class="quiz-option" data-index="1">Архитектурный стиль, описанный Роем Филдингом: набор ограничений, которым система либо соответствует, либо нет</div>
<div class="quiz-option" data-index="2">Библиотека Spring для построения веб-сервисов</div>
<div class="quiz-option" data-index="3">Формат передачи данных, основанный на JSON</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 51. Какое утверждение о REST верно?</h4>

<div class="quiz-option" data-index="0">REST требует использовать JSON: XML или HTML нарушают стиль</div>
<div class="quiz-option" data-index="1">REST — это протокол, конкурирующий с HTTP</div>
<div class="quiz-option" data-index="2">REST допустим только поверх HTTP/2 и выше</div>
<div class="quiz-option" data-index="3">REST ничего не говорит о формате данных: RESTful-сервис можно построить на XML, на HTML и даже на изображениях</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 52. Сколько ограничений у REST и какое из них необязательное?</h4>

<div class="quiz-option" data-index="0">Шесть; необязательное — код по требованию (Code on Demand)</div>
<div class="quiz-option" data-index="1">Четыре; необязательное — кешируемость (Cacheable)</div>
<div class="quiz-option" data-index="2">Шесть; необязательное — отсутствие состояния (Stateless)</div>
<div class="quiz-option" data-index="3">Пять; все обязательные</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 53. Что входит в ограничение «единообразие интерфейса» (Uniform Interface)?</h4>

<div class="quiz-option" data-index="0">Единый формат данных, единый порт, единая версия протокола и единый язык интерфейса</div>
<div class="quiz-option" data-index="1">Идентификация ресурсов через URI, манипуляция ресурсами через представления, самоописываемые сообщения и HATEOAS</div>
<div class="quiz-option" data-index="2">Единый контроллер, единый сервис, единый репозиторий и единая база данных</div>
<div class="quiz-option" data-index="3">Одинаковые коды ответов для всех ресурсов независимо от результата операции</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 54. В чём разница между ресурсом и представлением?</h4>

<div class="quiz-option" data-index="0">Ресурс — это строка таблицы в базе, а представление — SQL-запрос к ней</div>
<div class="quiz-option" data-index="1">Ресурс — это URI, а представление — метод HTTP</div>
<div class="quiz-option" data-index="2">Ресурс — именуемая сущность со своим URI, а представление — её конкретный вид, передаваемый по сети: JSON, XML, HTML, PDF</div>
<div class="quiz-option" data-index="3">Это синонимы, второй термин пришёл из спецификации HTTP/2</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 55. Какой адрес лучше всего соответствует правилам именования URI в REST?</h4>

<div class="quiz-option" data-index="0">`GET /getReviewsOfBook?id=42`</div>
<div class="quiz-option" data-index="1">`POST /books/42/doDeleteReview`</div>
<div class="quiz-option" data-index="2">`GET /BookReviews/42`</div>
<div class="quiz-option" data-index="3">`GET /books/42/reviews`</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 56. Куда по правилам REST помещают фильтр по жанру — в `/books?genre=drama` или в `/books/genre/drama`?</h4>

<div class="quiz-option" data-index="0">В строку запроса: параметр не идентифицирует ресурс, а лишь уточняет выборку — уберите его, и `/books` всё равно вернёт осмысленный список</div>
<div class="quiz-option" data-index="1">В путь: всё, что относится к ресурсу, обязано быть частью пути</div>
<div class="quiz-option" data-index="2">В заголовок `X-Filter`: строка запроса зарезервирована под постраничную выдачу</div>
<div class="quiz-option" data-index="3">В тело GET-запроса в формате JSON</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 57. На каком уровне зрелости Ричардсона находится API, который использует подходящие методы и осмысленные коды ответов, но не присылает ссылок на дальнейшие действия?</h4>

<div class="quiz-option" data-index="0">Уровень 0 — «болото POX»</div>
<div class="quiz-option" data-index="1">Уровень 1 — ресурсы</div>
<div class="quiz-option" data-index="2">Уровень 2 — HTTP-глаголы и коды</div>
<div class="quiz-option" data-index="3">Уровень 3 — гипермедиа (HATEOAS)</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 58. Как операции CRUD правильно соотносятся с методами HTTP и кодами ответов?</h4>

<div class="quiz-option" data-index="0">Create — PUT, Read — GET, Update — POST, Delete — DELETE</div>
<div class="quiz-option" data-index="1">Create — POST и 201 Created с заголовком `Location`; Read — GET и 200 OK; Update — PUT или PATCH и 200 либо 204; Delete — DELETE и 204 No Content</div>
<div class="quiz-option" data-index="2">Все четыре операции выполняются методом POST, а нужное действие указывается в теле запроса</div>
<div class="quiz-option" data-index="3">Create — GET, Read — HEAD, Update — PATCH, Delete — OPTIONS</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 59. Чем REST отличается от SOAP?</h4>

<div class="quiz-option" data-index="0">REST — протокол с обязательным контрактом WSDL, а SOAP — архитектурный стиль</div>
<div class="quiz-option" data-index="1">Оба используют исключительно метод POST и различаются только форматом тела</div>
<div class="quiz-option" data-index="2">SOAP быстрее REST, потому что передаёт данные в двоичном виде</div>
<div class="quiz-option" data-index="3">REST — стиль поверх HTTP с любым форматом данных и полным использованием методов, а SOAP — протокол с обязательным XML-конвертом, контрактом WSDL и передачей всего через POST</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 60. Чем стиль RPC отличается от REST?</h4>

<div class="quiz-option" data-index="0">В RPC адрес указывает на процедуру-глагол (`/api/getBookById`), а в REST — на ресурс-существительное, и действие задаёт метод HTTP</div>
<div class="quiz-option" data-index="1">RPC работает только внутри одной JVM и не выходит в сеть</div>
<div class="quiz-option" data-index="2">RPC принципиально не может использовать HTTP в качестве транспорта</div>
<div class="quiz-option" data-index="3">В RPC обязателен формат JSON, а в REST — XML</div>
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
    'Вопрос 1': 'HTTP живёт на прикладном уровне и описывает только формат запроса и ответа. Надёжную доставку байтов обеспечивает лежащий ниже TCP (а в HTTP/3 — QUIC поверх UDP), маршрутизацией занимается IP.',
    'Вопрос 2': 'Порты 80 и 443 подставляются браузером автоматически, поэтому их не пишут в адресной строке. 8080 и 8443 — просто популярные «пользовательские» порты для разработки, никакого статуса по умолчанию у них нет.',
    'Вопрос 3': 'Порядок жёстко задан спецификацией, и пустая строка обязательна: именно она сообщает получателю, что заголовки закончились и дальше начинается тело. «Строка состояния» бывает только в ответе.',
    'Вопрос 4': 'Структура сообщений зеркальная и отличается ровно одной строкой: запрос начинается со стартовой строки с методом и путём, ответ — со строки состояния, где после версии идёт трёхзначный код и текстовое пояснение вроде `201 Created`.',
    'Вопрос 5': 'Спецификация требует именно пару CR LF. Если вы вручную собираете HTTP-ответ и ставите только `\\n`, часть клиентов и промежуточных прокси такое сообщение не разберут — это классическая ошибка при написании сервера на голом сокете.',
    'Вопрос 6': 'Разделителем между заголовками и телом служит пустая строка, то есть ещё одна пара CR LF. Без неё сообщение синтаксически некорректно: клиент продолжает читать «заголовки» и запрос повисает до тайм-аута.',
    'Вопрос 7': 'Имя домена в IP-пакет не попадает — оно уже превращено в адрес резолвером DNS. Без `Host` сервер, обслуживающий сотни сайтов на одном адресе, не смог бы понять, чей именно сайт у него просят.',
    'Вопрос 8': 'Фрагмент обрабатывается исключительно браузером: он нужен, чтобы прокрутить уже загруженную страницу к нужному месту. Путь и строка запроса уходят в стартовую строку, а хост — в заголовок `Host`.',
    'Вопрос 9': 'TLS шифрует URL в канале, но не мешает ему осесть в журналах, в истории и в `Referer` при переходе на чужой сайт. Поэтому секреты передают только в теле запроса или в заголовке `Authorization`.',
    'Вопрос 10': 'Формула простая: `Content-Type` — «вот что я вам посылаю», `Accept` — «вот что я готов принять». Отсюда следует, что в GET-запросе `Content-Type` не нужен вовсе: тела там нет.',
    'Вопрос 11': 'Согласование содержимого позволяет отдавать один ресурс в разных представлениях. Не путайте 406 (не могу отдать в запрошенном формате, речь про `Accept`) и 415 (не могу разобрать присланное, речь про `Content-Type`).',
    'Вопрос 12': 'Statelessness — свойство протокола, а не хранилища. Именно оно даёт горизонтальное масштабирование: балансировщик волен направить очередной запрос на любой инстанс, и ничего не сломается.',
    'Вопрос 13': 'Cookie — это номерок из гардероба: сам по себе он ничего не весит и ничего не значит. Ценность в том, что по нему сервер находит у себя «пальто» — данные сессии, привязанные к этому идентификатору.',
    'Вопрос 14': '`HttpOnly` запрещает доступ к cookie из скриптов страницы. `Secure` отвечает за передачу только по HTTPS, `SameSite` ограничивает отправку cookie с чужих сайтов (защита от CSRF), а `Path` — просто область действия.',
    'Вопрос 15': 'HTTP/2 поменял только «упаковку» — способ передачи по сети. Смысл методов, кодов и заголовков остался прежним, а на QUIC поверх UDP перешёл уже следующий шаг, HTTP/3.',
    'Вопрос 16': 'Разница в адресации и в том, кто назначает идентификатор: `POST /api/books` означает «создай здесь что-нибудь новое», а `PUT /api/books/42` — «пусть по этому адресу лежит вот это». Именно поэтому PUT идемпотентен, а POST нет.',
    'Вопрос 17': 'GET только читает, поэтому он безопасный, и сколько его ни повторяй — состояние сервера не меняется, поэтому он идемпотентный. DELETE идемпотентен, но не безопасен, а POST и PATCH не обладают ни одним из этих свойств.',
    'Вопрос 18': 'Идемпотентность говорит о состоянии сервера, а не о коде ответа. Первый DELETE вернёт 204, второй — 404, но в обоих случаях итог один: ресурса нет.',
    'Вопрос 19': 'Спецификация не ограничивает содержимое патча. Тело вида «установить статус = выдана» повторять безопасно, а вида «прибавь единицу» — нет, поэтому в общем случае метод относят к неидемпотентным.',
    'Вопрос 20': 'Автоматический повтор безопасен только там, где он ничего не меняет дополнительно. Повтор POST означал бы второй заказ и второе списание с карты — поэтому такие кнопки в интерфейсе ещё и блокируют после первого клика.',
    'Вопрос 21': 'HEAD — это тот же GET, но сервер обрывает ответ после заголовков. Заголовки при этом заполняются как для полноценного GET, поэтому `Content-Length` показывает, сколько байт было бы в теле.',
    'Вопрос 22': 'Тернарные операторы проверяются слева направо: 404 не меньше 200, 300 и 400, но меньше 500 — значит, срабатывает четвёртая ветка. Ровно так класс ответа и определяют: по первой цифре кода.',
    'Вопрос 23': 'Граница между 4xx и 5xx — это ответ на вопрос «кому чинить». 4xx говорит: запрос неисправим в текущем виде, правьте клиент. 5xx говорит: запрос был нормальный, повторите позже. Подмена одного другим ломает и клиентскую логику, и разбор инцидентов.',
    'Вопрос 24': 'Идентификатор новому ресурсу назначает сервер, и клиенту его надо как-то сообщить — для этого и служит `Location`. Код 202 Accepted уместен в другом случае: задача принята в очередь, но ещё не выполнена.',
    'Вопрос 25': '415 означает «я не умею разбирать присланный тип содержимого» — и забытый или неверный `Content-Type` это самая частая его причина. 406 относится к заголовку `Accept`, а 422 — к данным, которые уже успешно разобраны.',
    'Вопрос 26': '401 — про аутентификацию (название Unauthorized историческое и сбивает с толку), 403 — про авторизацию. Если залогиненный пользователь получает 401, предлагать ему войти заново бессмысленно — это ошибка сервера.',
    'Вопрос 27': '404 говорит «такого адреса нет», а здесь адрес есть — не подходит глагол. Спецификация требует, чтобы вместе с 405 сервер прислал заголовок `Allow` со списком поддерживаемых методов.',
    'Вопрос 28': '422 — это «синтаксис верный, но содержимое нарушает правила предметной области». 400 отдают, когда сервер вообще не смог разобрать сообщение; на практике многие API (и Spring с `@Valid` по умолчанию) отвечают 400 и здесь, но точнее именно 422.',
    'Вопрос 29': '502 означает «я посредник, и вышестоящий сервер не ответил или ответил мусором». 504 отдают, когда приложение отвечало, но слишком медленно, а 503 — когда сервис сам сообщает о перегрузке или техобслуживании.',
    'Вопрос 30': 'Инициатива всегда у клиента: кухня не выбегает в зал предлагать котлету. При этом «сервер» — это роль в диалоге, а не отдельный компьютер: ваш ноутбук со Spring Boot одновременно и сервер, и клиент.',
    'Вопрос 31': 'Все три проблемы вытекают из одного: клиент ходит в базу напрямую. Отсюда обновление программы на трёхстах машинах, доступ ко всем таблицам у любого сотрудника с отладчиком и триста открытых соединений к СУБД.',
    'Вопрос 32': 'Звенья называют по назначению. Связка контроллер — сервис — репозиторий описывает внутреннее устройство одного только среднего звена, а не всю трёхзвенную схему.',
    'Вопрос 33': 'Веб-сервер — это газетный киоск: находит готовое на полке и отдаёт. Он ничего не «готовит», поэтому запуск вашего кода и обращение к базе данных — задача сервера приложений.',
    'Вопрос 34': 'Речь об объёме реализуемой спецификации. Для нашего курса хватает контейнера сервлетов: именно он разбирает HTTP, ведёт пул потоков, управляет жизненным циклом сервлетов и сессиями.',
    'Вопрос 35': 'Вся низкоуровневая работа — сокет, чтение текста, разбор, пул потоков, тайм-ауты, keep-alive — спрятана внутри контейнера. Ровно за это и платят серверу приложений: сам по себе такой код вы видели в примере `RawHttpServer`.',
    'Вопрос 36': 'Разделение простое: неизменные файлы с диска дешевле и быстрее отдаст Nginx, а всё, что нужно посчитать, уходит в Java-приложение. Заодно так работает ограничение «слоистая система» из REST.',
    'Вопрос 37': 'Это разница между «привезти мебель в готовую квартиру» и «привезти дом-вагончик вместе с мебелью». Второй вариант проще разворачивать в облаке и в Docker, поэтому Spring Boot сделал его основным.',
    'Вопрос 38': 'Ключевой критерий — где живёт логика. Современные SPA на React или Vue — гибрид: код исполняется в браузере, как у толстого клиента, но доставляется с сервера при каждом открытии страницы и ходит за данными в REST API.',
    'Вопрос 39': 'Сервлет — это арендатор офиса в бизнес-центре: здание, электричество и охрану даёт контейнер, а вы занимаетесь своим делом, соблюдая правила спецификации Jakarta Servlet (пакет `jakarta.servlet`, ранее `javax.servlet`).',
    'Вопрос 40': '`HttpServlet` берёт на себя весь протокольный разбор: смотрит на `request.getMethod()` и вызывает соответствующий метод `doXxx`. `ServletRequest` — это вообще интерфейс запроса, а не базовый класс сервлета.',
    'Вопрос 41': 'Жизненный цикл строгий: создание экземпляра и `init()` происходят однократно, потом на каждый запрос вызывается `service()`, который делегирует в `doGet`/`doPost`, и при остановке однократно вызывается `destroy()`.',
    'Вопрос 42': 'Контейнер создаёт сервлет в единственном экземпляре и вызывает его параллельно из потоков пула, поэтому `counter++` (чтение, инкремент, запись) не атомарен. Изменяемое состояние держат в локальных переменных, в `HttpSession` или в `AtomicInteger` и `ConcurrentHashMap`.',
    'Вопрос 43': 'По умолчанию сервлет создаётся лениво, и первый пользователь оплачивает своим ожиданием всю инициализацию — открытие пулов, чтение конфигурации. `loadOnStartup` переносит эту работу на момент запуска.',
    'Вопрос 44': '`getContextPath()` вернёт `/app`, `getServletPath()` — `/api/books`, а `getPathInfo()` отдаёт «хвост» после шаблона сервлета. Весь путь целиком показал бы `getRequestURI()`.',
    'Вопрос 45': 'Тело запроса — это поток, который исчерпывается при первом чтении, и контейнер разрешает выбрать лишь один способ доступа к нему. Если тело нужно нескольким компонентам, его буферизуют в фильтре (в Spring для этого есть `ContentCachingRequestWrapper`).',
    'Вопрос 46': 'Заголовки физически идут в сообщении раньше тела, поэтому уходят к клиенту первыми. Попытка изменить их после сброса буфера даёт либо `IllegalStateException`, либо молча проигнорированный `setStatus` — один из самых загадочных багов новичка.',
    'Вопрос 47': '`PrintWriter` берёт кодировку в момент создания и уже её не меняет. Один вызов `setContentType` с параметром `charset` задаёт и тип содержимого, и кодировку, — это самый надёжный способ не получить нечитаемый русский текст.',
    'Вопрос 48': 'Порядок приоритетов фиксирован: точное совпадение, затем префикс пути (побеждает более длинный), затем расширение, и только в конце сервлет по умолчанию на `/`. Именно поэтому `DispatcherServlet` на `/` ловит всё, что не перехватил кто-то более конкретный.',
    'Вопрос 49': 'Главная мысль лекции: над сервлетным API нет никакой магии. `@GetMapping` — это лишь способ сказать `DispatcherServlet`, какой метод вызвать, когда `request.getMethod()` вернёт `"GET"`, а путь совпадёт с шаблоном.',
    'Вопрос 50': 'REST — это стиль, а не протокол, не стандарт и не библиотека. Он играет ту же роль, что правила дорожного движения: не говорит, на чём ехать, а говорит, как себя вести, чтобы участники понимали друг друга.',
    'Вопрос 51': '«REST — это когда JSON» — самое распространённое заблуждение. Ограничения касаются адресации ресурсов, самоописываемости сообщений и работы с представлениями, а конкретный формат выбирается согласованием содержимого.',
    'Вопрос 52': 'Клиент-сервер, stateless, кешируемость, единообразие интерфейса и слоистая система обязательны — нарушив любое из них, система перестаёт быть RESTful. Код по требованию (классический пример — JavaScript в браузере) — единственное необязательное.',
    'Вопрос 53': 'Это самое объёмное ограничение, и оно раскладывается ровно на четыре подпункта. Именно его нарушают, когда изобретают глаголы в URL или заставляют клиента опираться на внешние договорённости вместо самоописываемых сообщений.',
    'Вопрос 54': 'Разница как между человеком и его фотографией: по сети передают не сам ресурс, а один из его снимков. Отсюда и расшифровка REST — «передача состояния представления»: GET забирает представление текущего состояния, PUT отправляет представление желаемого.',
    'Вопрос 55': 'В пути только существительные во множественном числе и иерархия вложенности, глагол задаётся методом HTTP. Варианты с `getReviewsOfBook` и `doDeleteReview` прячут действие в адрес, а `/BookReviews` нарушает правило строчных букв с дефисом.',
    'Вопрос 56': 'Критерий простой: если убрать элемент и запрос всё равно адресует осмысленный ресурс — ему место в строке запроса. `/books/42` без `42` книгу уже не адресует, поэтому идентификатор идёт в путь, а фильтры, сортировка и постраничная выдача — в query string.',
    'Вопрос 57': 'На уровне 2 находится подавляющее большинство реальных API, включая те, что вы писали на Spring Boot. Формально настоящим REST по Филдингу считается только уровень 3, но говорить «мы делаем REST API» про уровень 2 — общепринятая условность.',
    'Вопрос 58': 'CRUD одинаково ложится на все слои: `INSERT` — POST — 201, `SELECT` — GET — 200, `UPDATE` — PUT/PATCH — 200 или 204, `DELETE` — DELETE — 204. Вариант «всё через POST с действием в теле» — это уровень 0 по Ричардсону.',
    'Вопрос 59': 'REST — как SMS: коротко, быстро, без церемоний. SOAP — как заказное письмо с описью вложения: медленно и многословно, зато со строгим контрактом, поэтому он до сих пор жив в банках, страховании и госсистемах.',
    'Вопрос 60': 'Единица адресации у RPC — процедура, у REST — ресурс. Отсюда и минусы RPC: сколько процедур, столько имён, HTTP-кеширование не работает, а промежуточные узлы не понимают семантику запроса. Зато gRPC выигрывает в скорости внутри микросервисов.'
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
