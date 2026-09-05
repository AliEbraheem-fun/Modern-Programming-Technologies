# Тест 10: Документирование и тестирование (Лекция 10)

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

<!-- ===== РАЗДЕЛ 1: Комментарии и Javadoc (Вопросы 1–8) ===== -->

<div class="quiz-question" data-correct="1">
<h4>Вопрос 1. Сколько синтаксических форм комментария есть в Java и какая из них обрабатывается отдельной утилитой из состава JDK?</h4>

<div class="quiz-option" data-index="0">Две формы — однострочная и блочная; обе обрабатывает компилятор</div>
<div class="quiz-option" data-index="1">Три формы; отдельной утилитой javadoc обрабатывается только документирующий комментарий</div>
<div class="quiz-option" data-index="2">Три формы; утилита javadoc обрабатывает и блочный, и документирующий комментарий</div>
<div class="quiz-option" data-index="3">Четыре формы, включая маркер TODO, который читает компилятор</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 2. Попадают ли комментарии в скомпилированный файл .class?</h4>

<div class="quiz-option" data-index="0">Нет: компилятор отбрасывает комментарии всех трёх видов</div>
<div class="quiz-option" data-index="1">Да, документирующие комментарии сохраняются и доступны через рефлексию</div>
<div class="quiz-option" data-index="2">Да, сохраняются все комментарии — иначе javadoc не смог бы их прочитать</div>
<div class="quiz-option" data-index="3">Сохраняются только комментарии, содержащие дескриптор @author</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 3. Где должен стоять документирующий комментарий, чтобы утилита javadoc его увидела?</h4>

<div class="quiz-option" data-index="0">В любом месте файла — javadoc собирает все комментарии вида /** */</div>
<div class="quiz-option" data-index="1">Непосредственно перед объявлением класса, интерфейса, метода, конструктора или поля</div>
<div class="quiz-option" data-index="2">Внутри тела метода, перед первым оператором</div>
<div class="quiz-option" data-index="3">В самом начале файла, до объявления пакета</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 4. Что считается кратким описанием (summary) в документирующем комментарии?</h4>

<div class="quiz-option" data-index="0">Первые 80 символов комментария</div>
<div class="quiz-option" data-index="1">Только текст, помеченный дескриптором @summary; без него краткого описания нет</div>
<div class="quiz-option" data-index="2">Всё, что идёт до первого блочного дескриптора</div>
<div class="quiz-option" data-index="3">Текст до первой точки, за которой следует пробел</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 5. Класс описан фразой «Вычисляет штрафы. Ставка — 5 руб. в день.» Какой текст попадёт в сводную таблицу как краткое описание?</h4>

<div class="quiz-option" data-index="0">«Вычисляет штрафы.»</div>
<div class="quiz-option" data-index="1">Вся фраза целиком</div>
<div class="quiz-option" data-index="2">«Вычисляет штрафы. Ставка — 5 руб.»</div>
<div class="quiz-option" data-index="3">Ничего: для классов краткое описание не формируется</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 6. В каком порядке идут части документирующего комментария?</h4>

<div class="quiz-option" data-index="0">Блок дескрипторов, краткое описание, подробное описание</div>
<div class="quiz-option" data-index="1">Краткое описание, блок дескрипторов, подробное описание</div>
<div class="quiz-option" data-index="2">Порядок произвольный: javadoc сам разложит части по разделам страницы</div>
<div class="quiz-option" data-index="3">Краткое описание, подробное описание, блок дескрипторов</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 7. Почему комментарий «увеличиваем i на единицу» над строкой i = i + 1 считается вредным?</h4>

<div class="quiz-option" data-index="0">Он замедляет компиляцию: компилятор разбирает его текст</div>
<div class="quiz-option" data-index="1">Однострочные комментарии в Java не рекомендуются</div>
<div class="quiz-option" data-index="2">Он мешает утилите javadoc собрать документацию метода</div>
<div class="quiz-option" data-index="3">Он дублирует код, со временем расходится с ним, а человек верит комментарию</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 8. Каким файлом документируют целый пакет?</h4>

<div class="quiz-option" data-index="0">Файлом package.html в корне проекта</div>
<div class="quiz-option" data-index="1">Файлом README.md рядом с исходниками пакета</div>
<div class="quiz-option" data-index="2">Файлом package-info.java с документирующим комментарием перед объявлением пакета</div>
<div class="quiz-option" data-index="3">Файлом overview-tree.html, который создаёт сам javadoc</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 2: Дескрипторы Javadoc и генерация документации (Вопросы 9–16) ===== -->

<div class="quiz-question" data-correct="3">
<h4>Вопрос 9. Что такое дескриптор (тег) Javadoc?</h4>

<div class="quiz-option" data-index="0">Аннотация Java, которую обрабатывает компилятор</div>
<div class="quiz-option" data-index="1">Заголовок HTML-страницы, которую создаёт javadoc</div>
<div class="quiz-option" data-index="2">Директива компилятора, включающая строгую проверку документации</div>
<div class="quiz-option" data-index="3">Специальная метка с символа @, помечающая фрагмент документации как имеющий определённый смысл</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 10. Чем блочный дескриптор отличается от строчного (инлайнового)?</h4>

<div class="quiz-option" data-index="0">Блочный применяется к классам, строчный — только к методам</div>
<div class="quiz-option" data-index="1">Блочный обрабатывается утилитой javadoc, строчный — только средой разработки</div>
<div class="quiz-option" data-index="2">Блочный начинает отдельную строку в блоке тегов, строчный записывается в фигурных скобках прямо внутри текста</div>
<div class="quiz-option" data-index="3">Блочный можно повторять, а строчный допустим только один на комментарий</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 11. Сколько дескрипторов @return допустимо у метода?</h4>

<div class="quiz-option" data-index="0">Ровно один, и для void-методов он не пишется</div>
<div class="quiz-option" data-index="1">По одному на каждый оператор return в теле метода</div>
<div class="quiz-option" data-index="2">Обязательно один у любого метода, включая void</div>
<div class="quiz-option" data-index="3">Ни одного: результат описывают дескриптором @param</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 12. Как соотносятся дескрипторы @throws и @exception?</h4>

<div class="quiz-option" data-index="0">@throws описывает проверяемые исключения, @exception — непроверяемые</div>
<div class="quiz-option" data-index="1">@throws пишут у методов, @exception — у конструкторов</div>
<div class="quiz-option" data-index="2">@exception описывает только исключения, перечисленные в сигнатуре метода</div>
<div class="quiz-option" data-index="3">Это полные синонимы; @exception — историческая форма, сегодня пишут @throws</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 13. Как в Javadoc описывают параметры типа обобщённого класса Pair&lt;K, V&gt; и компоненты записи (record)?</h4>

<div class="quiz-option" data-index="0">Отдельным дескриптором @generic для каждого параметра типа</div>
<div class="quiz-option" data-index="1">Тем же дескриптором @param, записывая имя параметра типа в угловых скобках: @param &lt;K&gt; тип ключа</div>
<div class="quiz-option" data-index="2">Никак: параметры типа и компоненты записи документировать нельзя</div>
<div class="quiz-option" data-index="3">Дескриптором @see со ссылкой на класс Object</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 14. Чем инлайн-дескриптор {@code текст} отличается от {@literal текст}?</h4>

<div class="quiz-option" data-index="0">{@code} подставляет значение константы, {@literal} — её имя</div>
<div class="quiz-option" data-index="1">{@code} создаёт ссылку на класс, {@literal} выводит просто текст</div>
<div class="quiz-option" data-index="2">Оба защищают текст от разбора как HTML, но {@code} выводит его моноширинным шрифтом</div>
<div class="quiz-option" data-index="3">{@code} работает только в блоке тегов, {@literal} — только в описании</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 15. Что делает инлайн-дескриптор {@inheritDoc} и когда он нужен?</h4>

<div class="quiz-option" data-index="0">Копирует документацию во все подклассы на этапе компиляции</div>
<div class="quiz-option" data-index="1">Запрещает наследование документации от родителя</div>
<div class="quiz-option" data-index="2">Наследует документацию только от интерфейсов, но не от классов</div>
<div class="quiz-option" data-index="3">Вставляет документацию переопределяемого метода; нужен, когда к описанию родителя надо добавить своё</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 16. Студент написал @author в комментарии к классу, сгенерировал документацию и не нашёл автора на HTML-странице. В чём причина?</h4>

<div class="quiz-option" data-index="0">По умолчанию javadoc не выводит @author и @version — нужны опции -author и -version</div>
<div class="quiz-option" data-index="1">Дескриптор @author поддерживается только в файле package-info.java</div>
<div class="quiz-option" data-index="2">Дескриптор устарел и современными версиями javadoc не обрабатывается</div>
<div class="quiz-option" data-index="3">Дескриптор должен стоять первым в комментарии, иначе игнорируется</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 3: Виды тестов и структура JUnit 5 (Вопросы 17–25) ===== -->

<div class="quiz-question" data-correct="1">
<h4>Вопрос 17. Чем метод чёрного ящика отличается от метода белого ящика?</h4>

<div class="quiz-option" data-index="0">Чёрный ящик применяют к интерфейсу, белый — только к базам данных</div>
<div class="quiz-option" data-index="1">При чёрном ящике известен только внешний контракт, при белом — внутренняя структура кода</div>
<div class="quiz-option" data-index="2">При чёрном ящике тесты пишет автор кода, при белом — заказчик</div>
<div class="quiz-option" data-index="3">Чёрный ящик — это ручное тестирование, белый — автоматизированное</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 18. Какие тесты находятся в основании пирамиды тестирования и почему?</h4>

<div class="quiz-option" data-index="0">Сквозные (E2E): они проверяют систему так, как её видит пользователь</div>
<div class="quiz-option" data-index="1">Интеграционные: они дают баланс скорости и охвата</div>
<div class="quiz-option" data-index="2">Модульные: они самые быстрые и точнее всех указывают место поломки</div>
<div class="quiz-option" data-index="3">Ручные: с них начинают проверку любой системы</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 19. Как называется антипаттерн, при котором почти всё проверяется вручную и сквозными тестами, а модульных почти нет?</h4>

<div class="quiz-option" data-index="0">«Мороженое» (ice cream cone) — перевёрнутая пирамида</div>
<div class="quiz-option" data-index="1">«Золотой молоток»</div>
<div class="quiz-option" data-index="2">«Большой ком грязи»</div>
<div class="quiz-option" data-index="3">«Ленивая загрузка»</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 20. Какие три свойства обязательны для хорошего модульного теста?</h4>

<div class="quiz-option" data-index="0">Короткий, красивый, снабжённый комментариями</div>
<div class="quiz-option" data-index="1">Быстрый, независимый, повторяемый</div>
<div class="quiz-option" data-index="2">Интеграционный, автоматический, задокументированный</div>
<div class="quiz-option" data-index="3">Длинный, всеобъемлющий, покрывающий 100 % кода</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 21. Что означает схема AAA, по которой строят тест?</h4>

<div class="quiz-option" data-index="0">Assert — Act — Arrange, именно в таком порядке</div>
<div class="quiz-option" data-index="1">Analyze — Automate — Assert</div>
<div class="quiz-option" data-index="2">Arrange (подготовка) — Act (действие) — Assert (проверка)</div>
<div class="quiz-option" data-index="3">Assume — Assert — Announce</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 22. Из каких трёх подпроектов состоит JUnit 5?</h4>

<div class="quiz-option" data-index="0">JUnit Core, JUnit Runner, JUnit Assert</div>
<div class="quiz-option" data-index="1">JUnit API, JUnit Engine, JUnit Mock</div>
<div class="quiz-option" data-index="2">JUnit Platform, JUnit Params, JUnit Legacy</div>
<div class="quiz-option" data-index="3">JUnit Platform, JUnit Jupiter, JUnit Vintage</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 23. За что отвечает JUnit Platform?</h4>

<div class="quiz-option" data-index="0">За выполнение тестов, помеченных аннотацией @Test</div>
<div class="quiz-option" data-index="1">За параметризованные тесты и источники данных</div>
<div class="quiz-option" data-index="2">За создание заглушек и проверку вызовов</div>
<div class="quiz-option" data-index="3">За запуск тестов и связь с IDE и системами сборки через интерфейс TestEngine</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 24. В каком артефакте лежат аннотации и класс Assertions — то, что видит автор теста?</h4>

<div class="quiz-option" data-index="0">junit-platform-launcher</div>
<div class="quiz-option" data-index="1">junit-jupiter-api</div>
<div class="quiz-option" data-index="2">junit-jupiter-engine</div>
<div class="quiz-option" data-index="3">junit-vintage-engine</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 25. Где Maven ожидает найти тестовый класс FineCalculatorTest и как он должен называться?</h4>

<div class="quiz-option" data-index="0">В src/test/java, в том же пакете, что и тестируемый класс; имя оканчивается на Test или Tests</div>
<div class="quiz-option" data-index="1">В src/main/java рядом с тестируемым классом; имя оканчивается на Spec</div>
<div class="quiz-option" data-index="2">В src/test/resources, потому что тесты считаются ресурсами; имя начинается с Check</div>
<div class="quiz-option" data-index="3">В отдельном модуле с собственным pom.xml; имя оканчивается на IT</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 4: Тестовые классы, методы и аннотации JUnit (Вопросы 26–34) ===== -->

<div class="quiz-question" data-correct="2">
<h4>Вопрос 26. Обязан ли тестовый класс в JUnit 5 быть public?</h4>

<div class="quiz-option" data-index="0">Да, иначе движок его не обнаружит</div>
<div class="quiz-option" data-index="1">Да, и все тестовые методы тоже обязаны быть public</div>
<div class="quiz-option" data-index="2">Нет, достаточно package-private видимости — так теперь и принято писать</div>
<div class="quiz-option" data-index="3">Нет, но тестовые методы обязаны быть public</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 27. Каким должен быть метод, помеченный аннотацией @Test?</h4>

<div class="quiz-option" data-index="0">static — чтобы не создавать экземпляр тестового класса</div>
<div class="quiz-option" data-index="1">private — чтобы не засорять открытый API класса</div>
<div class="quiz-option" data-index="2">возвращающим boolean, где true означает успешную проверку</div>
<div class="quiz-option" data-index="3">не static, не private и возвращающим void</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 28. Что даёт аннотация @DisplayName?</h4>

<div class="quiz-option" data-index="0">Задаёт имя файла с отчётом о прогоне тестов</div>
<div class="quiz-option" data-index="1">Переименовывает тестовый метод при компиляции</div>
<div class="quiz-option" data-index="2">Задаёт имя категории для выборочного запуска тестов</div>
<div class="quiz-option" data-index="3">Задаёт человекочитаемое имя класса или теста в отчёте, допуская пробелы, кириллицу и знаки препинания</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 29. Сколько раз выполнится метод, помеченный @BeforeEach, в классе с тремя тестами?</h4>

<div class="quiz-option" data-index="0">Один раз — перед первым тестом</div>
<div class="quiz-option" data-index="1">Три раза — перед каждым тестовым методом</div>
<div class="quiz-option" data-index="2">Три раза — после каждого тестового метода</div>
<div class="quiz-option" data-index="3">Ни разу, если ни один тест не упал</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 30. Выполнится ли метод с аннотацией @AfterEach, если тест упал с исключением?</h4>

<div class="quiz-option" data-index="0">Да, он выполняется после каждого теста независимо от результата</div>
<div class="quiz-option" data-index="1">Нет, при падении теста метод пропускается</div>
<div class="quiz-option" data-index="2">Да, но только если исключение перехвачено внутри самого теста</div>
<div class="quiz-option" data-index="3">Выполнится дважды: после падения и после отката состояния</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 31. Сколько экземпляров тестового класса создаст JUnit 5 по умолчанию для класса с четырьмя тестовыми методами?</h4>

<div class="quiz-option" data-index="0">Один — все тесты работают с общим состоянием</div>
<div class="quiz-option" data-index="1">Два: отдельный для @BeforeAll и общий для тестов</div>
<div class="quiz-option" data-index="2">Четыре — по новому экземпляру на каждый тестовый метод</div>
<div class="quiz-option" data-index="3">Ни одного: тестовые методы вызываются статически</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 32. Почему методы @BeforeAll и @AfterAll по умолчанию обязаны быть статическими?</h4>

<div class="quiz-option" data-index="0">Так быстрее работает загрузчик классов</div>
<div class="quiz-option" data-index="1">Они вызываются в момент, когда экземпляра тестового класса ещё или уже не существует</div>
<div class="quiz-option" data-index="2">Статические методы нельзя переопределить, и это защищает от ошибок наследования</div>
<div class="quiz-option" data-index="3">Требование пришло из JUnit 3 и сохранено исключительно ради совместимости</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 33. Каким должен быть класс, помеченный аннотацией @Nested?</h4>

<div class="quiz-option" data-index="0">Статическим вложенным классом</div>
<div class="quiz-option" data-index="1">Отдельным классом верхнего уровня в том же файле</div>
<div class="quiz-option" data-index="2">Нестатическим внутренним классом — тогда он видит поля внешнего тестового класса</div>
<div class="quiz-option" data-index="3">Анонимным классом, объявленным внутри тестового метода</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 34. Чем @Disabled отличается от простого удаления аннотации @Test?</h4>

<div class="quiz-option" data-index="0">Тест остаётся видимым и попадает в отчёт как пропущенный, а в аннотации указывают причину отключения</div>
<div class="quiz-option" data-index="1">Ничем: это два равнозначных способа выключить тест</div>
<div class="quiz-option" data-index="2">@Disabled убирает тест из отчёта полностью</div>
<div class="quiz-option" data-index="3">@Disabled помечает тест как провалившийся</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 5: Утверждения JUnit (Вопросы 35–41) ===== -->

<div class="quiz-question" data-correct="1">
<h4>Вопрос 35. Как называется класс утверждений в JUnit 5 и в каком он пакете?</h4>

<div class="quiz-option" data-index="0">Assert в пакете org.junit</div>
<div class="quiz-option" data-index="1">Assertions в пакете org.junit.jupiter.api</div>
<div class="quiz-option" data-index="2">Assert в пакете org.junit.jupiter</div>
<div class="quiz-option" data-index="3">Assertions в пакете org.junit.api</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 36. Каким по счёту аргументом передаётся сообщение об ошибке в assertEquals у JUnit 5?</h4>

<div class="quiz-option" data-index="0">Первым, как это было в JUnit 4</div>
<div class="quiz-option" data-index="1">Сообщение задаётся только аннотацией @DisplayName</div>
<div class="quiz-option" data-index="2">Последним</div>
<div class="quiz-option" data-index="3">Сообщение доступно лишь в отдельном методе assertEqualsWithMessage</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 37. В каком порядке передаются значения в assertEquals и чем грозит их перестановка?</h4>

<div class="quiz-option" data-index="0">Сначала фактическое, затем ожидаемое; иначе код не скомпилируется</div>
<div class="quiz-option" data-index="1">Порядок не важен: сравнение симметрично и на сообщение не влияет</div>
<div class="quiz-option" data-index="2">Сначала фактическое, затем ожидаемое; при перестановке тест всегда падает</div>
<div class="quiz-option" data-index="3">Сначала ожидаемое, затем фактическое; при перестановке тест работает, но сообщение об ошибке вводит в заблуждение</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 38. Чем assertSame отличается от assertEquals?</h4>

<div class="quiz-option" data-index="0">assertSame сравнивает ссылки оператором ==, а assertEquals вызывает метод equals()</div>
<div class="quiz-option" data-index="1">assertSame работает только с примитивными типами</div>
<div class="quiz-option" data-index="2">assertSame сравнивает поля объектов через рефлексию</div>
<div class="quiz-option" data-index="3">Это синонимы, второй оставлен ради совместимости с JUnit 4</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 39. Что произойдёт при выполнении теста: double sum = 0.1 + 0.2; assertEquals(0.3, sum);</h4>

<div class="quiz-option" data-index="0">Тест пройдёт: JUnit округляет значения типа double до 15 знаков</div>
<div class="quiz-option" data-index="1">Код не скомпилируется: для double обязателен третий аргумент</div>
<div class="quiz-option" data-index="2">Тест упадёт, потому что 0.1 + 0.2 даёт 0.30000000000000004</div>
<div class="quiz-option" data-index="3">Тест будет пропущен как недостоверный</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 40. Зачем нужен метод assertAll?</h4>

<div class="quiz-option" data-index="0">Чтобы запустить все тесты класса из одного метода</div>
<div class="quiz-option" data-index="1">Чтобы выполнить все переданные проверки и показать сразу все ошибки, а не только первую</div>
<div class="quiz-option" data-index="2">Чтобы проверить равенство всех элементов коллекции</div>
<div class="quiz-option" data-index="3">Чтобы повторить проверку во всех потоках приложения</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 41. Чем предположение assumeTrue отличается от утверждения assertTrue?</h4>

<div class="quiz-option" data-index="0">Невыполненное предположение пропускает тест, а провалившееся утверждение проваливает его</div>
<div class="quiz-option" data-index="1">Предположение проверяется до запуска теста компилятором</div>
<div class="quiz-option" data-index="2">assumeTrue — устаревшая форма assertTrue, оставшаяся от JUnit 4</div>
<div class="quiz-option" data-index="3">Предположение проваливает тест, а утверждение выводит только предупреждение</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 6: Тестирование исключений (Вопросы 42–45) ===== -->

<div class="quiz-question" data-correct="2">
<h4>Вопрос 42. Как в JUnit 5 проверяют, что метод бросает исключение?</h4>

<div class="quiz-option" data-index="0">Атрибутом аннотации: @Test(expected = IllegalArgumentException.class)</div>
<div class="quiz-option" data-index="1">Только блоком try/catch с вызовом fail() в конце блока try</div>
<div class="quiz-option" data-index="2">Методом assertThrows, которому передают класс исключения и лямбду с проверяемым кодом</div>
<div class="quiz-option" data-index="3">Аннотацией @Throws над тестовым методом</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 43. Что возвращает метод assertThrows и зачем это нужно?</h4>

<div class="quiz-option" data-index="0">boolean — было ли брошено исключение; значение используют в последующих if</div>
<div class="quiz-option" data-index="1">Строку с сообщением исключения</div>
<div class="quiz-option" data-index="2">void; проверить сообщение исключения средствами JUnit нельзя</div>
<div class="quiz-option" data-index="3">Само пойманное исключение — его можно исследовать дальше: сообщение, код, причину getCause()</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 44. Метод бросил NumberFormatException. Пройдёт ли тест с assertThrows(IllegalArgumentException.class, ...)?</h4>

<div class="quiz-option" data-index="0">Да: assertThrows принимает и наследников указанного класса, а NumberFormatException наследует IllegalArgumentException</div>
<div class="quiz-option" data-index="1">Нет: assertThrows требует точного совпадения классов</div>
<div class="quiz-option" data-index="2">Нет: NumberFormatException не является наследником IllegalArgumentException</div>
<div class="quiz-option" data-index="3">Тест будет помечен как неопределённый и не учтён в результате</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 45. Зачем нужен assertDoesNotThrow, если непойманное исключение и так провалит тест?</h4>

<div class="quiz-option" data-index="0">Он перехватывает и подавляет исключение, чтобы тест продолжился</div>
<div class="quiz-option" data-index="1">Ради читаемости: он явно объявляет, что предметом проверки является именно отсутствие исключения</div>
<div class="quiz-option" data-index="2">Это единственный способ проверить методы, возвращающие void</div>
<div class="quiz-option" data-index="3">Он превращает исключение в предупреждение в отчёте</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 7: Параметризованные, повторяющиеся и динамические тесты (Вопросы 46–50) ===== -->

<div class="quiz-question" data-correct="1">
<h4>Вопрос 46. Тест помечен @ParameterizedTest и @ValueSource(ints = {0, 1, 5, 100, 1000}). Сколько раз он выполнится?</h4>

<div class="quiz-option" data-index="0">Один раз, получив массив из пяти элементов</div>
<div class="quiz-option" data-index="1">Пять раз — по одному прогону на каждое значение</div>
<div class="quiz-option" data-index="2">Столько раз, сколько задано в атрибуте value аннотации @RepeatedTest</div>
<div class="quiz-option" data-index="3">Пять раз, но результат засчитывается как один тест</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 47. Почему для проверки поведения на null нельзя обойтись одним @ValueSource и существуют @NullSource и @NullAndEmptySource?</h4>

<div class="quiz-option" data-index="0">@ValueSource работает только со строками</div>
<div class="quiz-option" data-index="1">null запрещено передавать в тестовые методы правилами JUnit</div>
<div class="quiz-option" data-index="2">Аннотации Java не принимают null в массивах значений, поэтому подать его через @ValueSource невозможно</div>
<div class="quiz-option" data-index="3">@ValueSource преобразует null в пустую строку, что искажает проверку</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 48. Когда вместо @CsvSource нужен @MethodSource?</h4>

<div class="quiz-option" data-index="0">Когда наборы данных — не литералы, а объекты, которые нужно собрать кодом в статическом методе</div>
<div class="quiz-option" data-index="1">Когда наборов данных больше десяти</div>
<div class="quiz-option" data-index="2">Когда тест должен выполняться в отдельном потоке</div>
<div class="quiz-option" data-index="3">Когда у тестового метода ровно один параметр</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 49. Для чего применяют @RepeatedTest и какое у него принципиальное ограничение?</h4>

<div class="quiz-option" data-index="0">Для ускорения прогона; ограничение — работает только с параметризованными тестами</div>
<div class="quiz-option" data-index="1">Для проверки одного и того же кода на разных данных; ограничение — данные задаются только числами</div>
<div class="quiz-option" data-index="2">Для замера производительности; ограничение — не учитывает прогрев JVM</div>
<div class="quiz-option" data-index="3">Для кода со случайностью, конкурентностью или кэшем; ограничение — он не делает недетерминированный код детерминированным</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 50. Чем динамические тесты из @TestFactory отличаются от параметризованных?</h4>

<div class="quiz-option" data-index="0">Они выполняются параллельно, а параметризованные — последовательно</div>
<div class="quiz-option" data-index="1">Они не требуют утверждений: результат определяется возвращаемым значением</div>
<div class="quiz-option" data-index="2">Их набор формируется во время выполнения, метод возвращает поток или коллекцию DynamicTest, а @BeforeEach отрабатывает один раз на всю фабрику</div>
<div class="quiz-option" data-index="3">Они пишутся в отдельном классе, помеченном аннотацией @Nested</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 8: Mockito (Вопросы 51–56) ===== -->

<div class="quiz-question" data-correct="3">
<h4>Вопрос 51. Зачем при тестировании сервиса LoanService подменять репозиторий и отправителя писем макетами?</h4>

<div class="quiz-option" data-index="0">Чтобы увеличить процент покрытия кода в отчёте JaCoCo</div>
<div class="quiz-option" data-index="1">Чтобы обойти ограничение JUnit на количество зависимостей в тестируемом классе</div>
<div class="quiz-option" data-index="2">Чтобы не писать конструктор с параметрами</div>
<div class="quiz-option" data-index="3">Чтобы тест остался модульным: без реальной базы и почтового сервера он быстрый, повторяемый и никому не шлёт писем</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 52. В чём практическая разница между стабом (stub) и моком (mock)?</h4>

<div class="quiz-option" data-index="0">Стаб создаётся вручную, а мок — только библиотекой Mockito</div>
<div class="quiz-option" data-index="1">Стаб применяется к интерфейсам, а мок — к классам</div>
<div class="quiz-option" data-index="2">Стаб отвечает на вопросы заранее заданными значениями, а мок ещё и позволяет проверить сами вызовы</div>
<div class="quiz-option" data-index="3">Стаб оборачивает настоящий объект, а мок создаётся с нуля</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 53. Как ведёт себя только что созданный мок, если его метод не настроен через when()?</h4>

<div class="quiz-option" data-index="0">Возвращает «пустое» значение: null для объектов, 0 для чисел, false для boolean, пустой Optional</div>
<div class="quiz-option" data-index="1">Бросает UnsupportedOperationException</div>
<div class="quiz-option" data-index="2">Вызывает реальную реализацию метода</div>
<div class="quiz-option" data-index="3">Проваливает тест с сообщением о ненастроенном вызове</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 54. Что делает связка @ExtendWith(MockitoExtension.class), @Mock и @InjectMocks?</h4>

<div class="quiz-option" data-index="0">Поднимает контекст Spring и подменяет в нём бины моками</div>
<div class="quiz-option" data-index="1">Создаёт моки один раз на весь класс и переиспользует их во всех тестах</div>
<div class="quiz-option" data-index="2">Требует, чтобы у тестируемого класса был конструктор без параметров</div>
<div class="quiz-option" data-index="3">Перед каждым тестом создаёт свежие моки для полей @Mock и передаёт их в конструктор объекта из @InjectMocks</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 55. Строка verify(sender).send("ivan@example.com", anyString()) приводит к InvalidUseOfMatchersException. Почему и как исправить?</h4>

<div class="quiz-option" data-index="0">Метод send нельзя проверять через verify: у него тип void — нужен doVerify</div>
<div class="quiz-option" data-index="1">Если хотя бы один аргумент задан матчером, остальные тоже должны быть матчерами: пишем eq("ivan@example.com")</div>
<div class="quiz-option" data-index="2">Матчер anyString() не принимает null, поэтому нужен nullable(String.class)</div>
<div class="quiz-option" data-index="3">Порядок аргументов в verify обратный: сначала матчеры, потом точные значения</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 56. Чем ArgumentCaptor дополняет verify?</h4>

<div class="quiz-option" data-index="0">Он заменяет verify: проверять количество вызовов через verify больше не нужно</div>
<div class="quiz-option" data-index="1">Он позволяет отменить сделанный вызов и повторить его с другими аргументами</div>
<div class="quiz-option" data-index="2">Он перехватывает фактические аргументы вызова, чтобы проверить их содержимое, в том числе у объектов, созданных внутри тестируемого метода</div>
<div class="quiz-option" data-index="3">Он записывает вызовы в файл для последующего анализа</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 9: Тестирование Spring-приложений и покрытие кода (Вопросы 57–60) ===== -->

<div class="quiz-question" data-correct="1">
<h4>Вопрос 57. Что поднимает аннотация @WebMvcTest и чем в таком тесте заменяют сервис?</h4>

<div class="quiz-option" data-index="0">Весь контекст приложения; сервис используется настоящий</div>
<div class="quiz-option" data-index="1">Только веб-слой: контроллеры, преобразователи JSON, обработчики ошибок; сервис подменяют моком через @MockitoBean</div>
<div class="quiz-option" data-index="2">Только слой данных; сервис подменяют классом-заглушкой из src/test/java</div>
<div class="quiz-option" data-index="3">Веб-слой вместе с базой в памяти; сервис внедряется через @Autowired</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 58. Какие особенности у среза @DataJpaTest?</h4>

<div class="quiz-option" data-index="0">По умолчанию подставляется встроенная база в памяти, каждый тест идёт в транзакции с откатом, доступен помощник TestEntityManager</div>
<div class="quiz-option" data-index="1">Поднимается полный контекст приложения вместе с контроллерами</div>
<div class="quiz-option" data-index="2">Данные сохраняются между тестами, чтобы следующий тест мог их использовать</div>
<div class="quiz-option" data-index="3">Репозитории подменяются моками Mockito, реальные запросы не выполняются</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 59. Что означает значение webEnvironment = MOCK, стоящее по умолчанию у @SpringBootTest?</h4>

<div class="quiz-option" data-index="0">Все бины приложения заменяются моками Mockito</div>
<div class="quiz-option" data-index="1">Поднимается настоящий сервер на случайном свободном порту</div>
<div class="quiz-option" data-index="2">Веб-окружение не поднимается вообще</div>
<div class="quiz-option" data-index="3">Веб-окружение имитируется, реальный порт не занимается, запросы идут через MockMvc</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 60. Тест вызывает calculate(10) и не содержит ни одного утверждения. JaCoCo показывает 100 % покрытия метода. О чём это говорит?</h4>

<div class="quiz-option" data-index="0">О том, что метод протестирован полностью и дополнительных тестов не нужно</div>
<div class="quiz-option" data-index="1">О том, что покрытие фиксирует лишь факт выполнения строк, но ничего не говорит о проверке результата</div>
<div class="quiz-option" data-index="2">О том, что JaCoCo настроен неверно: без утверждений покрытие должно быть нулевым</div>
<div class="quiz-option" data-index="3">О том, что достигнуто покрытие ветвлений, а покрытие строк осталось нулевым</div>
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
    'Вопрос 1': 'Форм ровно три: однострочная, блочная и документирующая. Компилятор игнорирует все три, но документирующую дополнительно читает утилита javadoc, а маркер TODO — это соглашение для IDE, а не отдельная синтаксическая форма.',
    'Вопрос 2': 'В байт-код не попадает ни один вид комментария. Противоречия здесь нет: javadoc работает не с файлами .class, а с исходными файлами .java.',
    'Вопрос 3': 'Javadoc привязывает комментарий к следующему за ним объявлению. Комментарий внутри тела метода документацией не станет — его просто не к чему привязать.',
    'Вопрос 4': 'Именно этот фрагмент javadoc помещает в сводные таблицы вроде «Method Summary». Поэтому точка в середине первой фразы обрывает краткое описание, и границу приходится задавать инлайн-тегом {@summary}.',
    'Вопрос 5': 'Описание обрывается на первой же точке, за которой стоит пробел, — это точка после слова «штрафы». Всё остальное уйдёт в подробное описание.',
    'Вопрос 6': 'Блок дескрипторов всегда идёт последним: как только началась строка с символа @, обычный текст описания закончился и всё дальнейшее относится к тегам.',
    'Вопрос 7': 'Такой комментарий не добавляет информации, зато живёт своей жизнью: код правят, комментарий забывают, и через полгода они противоречат друг другу. Полезный комментарий объясняет «почему именно так», а не «что написано».',
    'Вопрос 8': 'Этот файл не содержит ничего, кроме комментария и строки package, а его текст попадает на страницу package-summary.html. Файлы overview-tree.html и index-all.html javadoc генерирует самостоятельно.',
    'Вопрос 9': 'Дескриптор работает как графа в почтовой накладной: он сообщает генератору, что данный текст описывает параметр, результат или исключение, и тот раскладывает текст по нужным разделам HTML-страницы.',
    'Вопрос 10': 'Вид определяется формой записи: @param и @return стоят отдельными строками в конце комментария, а {@link} и {@code} встраиваются прямо в предложение.',
    'Вопрос 11': '@return описывает не конкретный оператор return, а возвращаемое значение метода в целом, поэтому он один. У void-метода возвращать нечего, и тег не нужен.',
    'Вопрос 12': 'Сначала появился @exception, затем его переименовали в @throws, а старое имя оставили ради совместимости. Обрабатываются они одинаково.',
    'Вопрос 13': 'Специального тега для обобщений не существует: и параметры метода, и параметры типа, и компоненты записи описываются одним дескриптором @param — отличается только форма имени.',
    'Вопрос 14': 'Без любого из них угловые скобки обобщённого типа браузер примет за HTML-тег и вырежет вместе с содержимым: от записи List со String в скобках останется одно слово List. Разница между самими тегами только в начертании шрифта.',
    'Вопрос 15': 'Если у переопределяющего метода Javadoc отсутствует вообще, документация наследуется автоматически. Тег применяют именно тогда, когда нужно взять текст родителя и дописать к нему подробности реализации.',
    'Вопрос 16': 'Оба этих тега по умолчанию выключены в выводе, и включаются они отдельными опциями командной строки или соответствующими настройками maven-javadoc-plugin.',
    'Вопрос 17': 'Разница в том, что известно тестировщику. Модульные тесты обычно ближе к белому ящику: зная про ограничение сверху внутри метода, вы специально подбираете значения вокруг этой границы.',
    'Вопрос 18': 'Чем ниже уровень, тем дешевле тест и тем конкретнее сообщение о поломке. Упавший модульный тест называет метод и значение, а упавший сквозной сообщает лишь, что страница не открылась.',
    'Вопрос 19': 'Пирамида в такой системе стоит на вершине: дорогих и хрупких проверок много, дешёвых почти нет. Прогон занимает часы, а падения плохо локализуются.',
    'Вопрос 20': 'Это первые три буквы аббревиатуры FIRST. Тест, который лезет в реальную базу, зависит от порядка запуска или от сегодняшней даты, нарушает их и рано или поздно начнёт врать.',
    'Вопрос 21': 'Сначала готовят данные, затем вызывают ровно один тестируемый метод и только потом сверяют результат. Из BDD пришло второе название той же схемы — Given — When — Then.',
    'Вопрос 22': 'Platform запускает тесты и связывает фреймворк с IDE и системами сборки, Jupiter даёт новую модель программирования и расширений, Vintage выполняет старые тесты JUnit 3 и JUnit 4.',
    'Вопрос 23': 'Сама платформа тесты не выполняет — она задаёт SPI TestEngine, через который к ней подключаются движки. Благодаря этому на ней работают и сторонние фреймворки, например Spock или Cucumber.',
    'Вопрос 24': 'API нужен для написания тестов, а движок junit-jupiter-engine — для их выполнения во время прогона. Зонтичный артефакт junit-jupiter приносит оба сразу вместе с junit-jupiter-params.',
    'Вопрос 25': 'Отдельный каталог не даёт тестам попасть в собранный JAR, а совпадение пакетов открывает тесту доступ к package-private членам. По имени тестовые классы отбирает плагин Surefire; суффикс IT закреплён за интеграционными тестами и плагином Failsafe.',
    'Вопрос 26': 'Это одно из отличий от JUnit 4, где public требовался. В JUnit 5 ни класс, ни метод в модификаторе public не нуждаются.',
    'Вопрос 27': 'Результат теста определяется не возвращаемым значением, а тем, сработало ли утверждение, поэтому метод возвращает void. Параметры допустимы только те, что внедряет сам JUnit, например TestInfo.',
    'Вопрос 28': 'Имя метода ограничено синтаксисом Java, а отчёт читают в том числе не-программисты. С @DisplayName список тестов превращается в живое описание поведения системы.',
    'Вопрос 29': 'Аннотация так и называется — «перед каждым»: подготовка повторяется столько раз, сколько в классе тестов. Один раз на весь класс выполняется только @BeforeAll.',
    'Вопрос 30': 'Именно поэтому в него выносят освобождение ресурсов: закрыть соединение или удалить временный файл нужно и после успешного теста, и после провалившегося.',
    'Вопрос 31': 'Режим по умолчанию — @TestInstance(Lifecycle.PER_METHOD). Новый экземпляр перед каждым тестом и есть механизм, которым фреймворк обеспечивает независимость тестов друг от друга.',
    'Вопрос 32': 'В режиме PER_METHOD экземпляр создаётся перед каждым тестом, а эти методы работают до первого и после последнего. Требование снимается режимом @TestInstance(Lifecycle.PER_CLASS).',
    'Вопрос 33': 'Доступ к полям внешнего экземпляра есть только у нестатического внутреннего класса. Благодаря этому вложенная группа переиспользует подготовку из @BeforeEach внешнего класса.',
    'Вопрос 34': 'Отключённый тест не должен потеряться: отчёт показывает его как пропущенный, а текст причины напоминает, чего ждём. Метод без @Test для фреймворка просто не существует.',
    'Вопрос 35': 'Assert из пакета org.junit — это JUnit 4. Проверять стоит именно импорты: у JUnit 5 они всегда начинаются с org.junit.jupiter.api.',
    'Вопрос 36': 'Это одно из отличий Jupiter от JUnit 4, где сообщение шло первым аргументом. Если сообщение дорого собирать, вместо строки передают Supplier — он вычислится только при провале проверки.',
    'Вопрос 37': 'Сравнение действительно симметрично, поэтому ошибку компилятор не заметит. Пострадает диагностика: строка «expected: 4 but was: 5» поменяет смысл на противоположный, и вы будете искать ошибку не там.',
    'Вопрос 38': 'Два разных объекта с одинаковым содержимым пройдут assertEquals, но провалят assertSame — это разные вопросы: «равны ли по значению» и «это ли один и тот же объект».',
    'Вопрос 39': 'Тип double хранит значения приближённо, поэтому прямое сравнение ненадёжно. Правильная форма — assertEquals(0.3, sum, 0.000001), где третий аргумент задаёт дельту, то есть допустимое расхождение.',
    'Вопрос 40': 'Обычное утверждение прерывает тест на первой же неудаче, и остальные расхождения остаются невидимыми. assertAll принимает набор лямбд Executable и выполняет каждую — применяют его для независимых проверок одного объекта.',
    'Вопрос 41': 'Разница в смысле: провалившееся утверждение означает ошибку в коде, а невыполненное предположение — что в этих условиях проверять нечего, например тест написан только для Linux.',
    'Вопрос 42': 'Атрибут expected — это JUnit 4, и у него два изъяна: непонятно, какая строка бросила исключение, и нельзя проверить сообщение. assertThrows очерчивает ровно тот фрагмент кода, который должен упасть.',
    'Вопрос 43': 'Возврат объекта исключения и есть главное преимущество перед JUnit 4: после проверки типа обычно проверяют, что в сообщении есть внятное объяснение и значение, вызвавшее ошибку.',
    'Вопрос 44': 'Проверка идёт по совместимости типов, а не по точному равенству классов. Если требуется ровно указанный класс и никакой другой, применяют assertThrowsExactly.',
    'Вопрос 45': 'Технически он ничего не добавляет, зато сообщает читателю намерение автора. Особенно уместен на граничных значениях, где легко ошибиться со знаком сравнения: например, ноль дней просрочки — валидное значение.',
    'Вопрос 46': 'Параметризованный тест выполняется столько раз, сколько наборов данных подал источник, и каждый прогон попадает в отчёт отдельной строкой. Имя строки задаётся шаблоном в атрибуте name, где {0} — первый аргумент.',
    'Вопрос 47': 'Ограничение идёт от самого языка: значения в аннотациях — константы времени компиляции, и null среди них быть не может. Поэтому для null и пустого значения сделаны отдельные источники, которые можно комбинировать с @ValueSource.',
    'Вопрос 48': '@CsvSource ограничен строками, которые JUnit сам приводит к типам параметров. @MethodSource ссылается на статический метод, возвращающий Stream или коллекцию Arguments, и потому подаёт данные любой сложности.',
    'Вопрос 49': 'Повтор помогает поймать плавающую ошибку, но ничего не гарантирует: если сбой случается раз на тысячу прогонов, десять повторов его, скорее всего, не заметят. Это инструмент диагностики, а не доказательство корректности.',
    'Вопрос 50': 'Обычный тест определён на этапе компиляции, а динамический создаётся в рантайме — например, по данным из файла или базы. Платой за гибкость становится урезанный жизненный цикл, поэтому при известном заранее наборе данных проще @ParameterizedTest.',
    'Вопрос 51': 'Тест, лезущий в базу и в сеть, перестаёт быть модульным: он медленный, зависит от внешних систем и вызывает побочные эффекты. Проверяется же логика самого сервиса, а не работа базы и почты.',
    'Вопрос 52': 'Настроили when(...).thenReturn(...) и смотрите на результат — используете объект как стаб; написали verify(...) и проверяете факт вызова — как мок. Настоящий объект оборачивает шпион (spy), а не стаб.',
    'Вопрос 53': 'Мок по умолчанию максимально безобиден: ничего не делает и ничего не бросает. Именно поэтому забытая настройка обычно проявляется как неожиданный null, а не как явная ошибка.',
    'Вопрос 54': 'Расширение подключает Mockito к жизненному циклу JUnit 5 — в JUnit 4 ту же роль играл @RunWith(MockitoJUnitRunner.class). Свежесть моков принципиальна: настройки и записанные вызовы не должны переходить из теста в тест.',
    'Вопрос 55': 'Mockito не умеет смешивать точные значения и матчеры в одном вызове — сопоставление аргументов работает либо целиком по матчерам, либо целиком по значениям. Обёртка eq() превращает точное значение в матчер.',
    'Вопрос 56': 'verify отвечает на вопрос «вызвали ли», а захватчик — «с чем именно вызвали». Если вызовов было несколько, все перехваченные значения доступны через getAllValues().',
    'Вопрос 57': 'Срез проверяет маршрутизацию, коды ответа и формат JSON, а работу сервиса не проверяет вовсе — тот заменён моком. Запросы выполняет MockMvc, обращаясь к DispatcherServlet напрямую, без сети и без запуска сервера.',
    'Вопрос 58': 'Смысл среза — проверить, что производные методы репозитория превращаются в правильный SQL, поэтому запросы выполняются по-настоящему. Откат транзакции после каждого теста не даёт им влиять друг на друга.',
    'Вопрос 59': 'Контекст при этом поднимается полностью — имитируется только веб-часть. Настоящий сервер даёт RANDOM_PORT или DEFINED_PORT, и тогда запросы отправляют через TestRestTemplate.',
    'Вопрос 60': 'Строка выполнилась — значит, засчитана, даже если результат никто не сверял, и ошибка в формуле проедет мимо. Низкое покрытие — надёжный признак беды, а высокое лишь необходимое, но не достаточное условие качества.'
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
