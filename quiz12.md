# Тест 12: Системы контроля версий и процессы разработки (Лекция 12)

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

<!-- ===== РАЗДЕЛ 1: Основы Git и модель данных (Вопросы 1–7) ===== -->

<div class="quiz-question" data-correct="2">
<h4>Вопрос 1. Чем распределённая система контроля версий (Git) принципиально отличается от централизованной (SVN)?</h4>

<div class="quiz-option" data-index="0">Git умеет хранить только текстовые файлы, а SVN — файлы любых типов</div>
<div class="quiz-option" data-index="1">Git не требует явных коммитов: изменения сохраняются автоматически при записи файла</div>
<div class="quiz-option" data-index="2">У каждого участника есть полная копия репозитория со всей историей, а не только рабочая копия последней версии</div>
<div class="quiz-option" data-index="3">Git хранит историю целиком на сервере, а SVN раздаёт её копии клиентам</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 2. Как Git хранит историю проекта?</h4>

<div class="quiz-option" data-index="0">Как последовательность снимков (snapshot) всего проекта на момент каждого коммита</div>
<div class="quiz-option" data-index="1">Как цепочку разниц (дельт), которые нужно применять по очереди</div>
<div class="quiz-option" data-index="2">Как журнал выполненных команд, воспроизводимый при откате</div>
<div class="quiz-option" data-index="3">Как ежедневный архив рабочего каталога</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 3. В каком объекте Git хранится имя файла?</h4>

<div class="quiz-option" data-index="0">В blob, рядом с содержимым файла</div>
<div class="quiz-option" data-index="1">В объекте commit, вместе с сообщением</div>
<div class="quiz-option" data-index="2">В объекте tag</div>
<div class="quiz-option" data-index="3">В объекте tree</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 4. Что хранит объект commit?</h4>

<div class="quiz-option" data-index="0">Полный текст изменённых файлов в виде дельт относительно предыдущей версии</div>
<div class="quiz-option" data-index="1">Ссылку на корневой tree, ссылки на родительские коммиты, автора, дату и сообщение</div>
<div class="quiz-option" data-index="2">Список веток и тегов, которые на него указывают</div>
<div class="quiz-option" data-index="3">Только сообщение коммита и время его создания</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 5. Почему нельзя незаметно подменить старый коммит в истории?</h4>

<div class="quiz-option" data-index="0">Каталог .git становится доступным только для чтения после первого коммита</div>
<div class="quiz-option" data-index="1">Каждый коммит подписывается сервером в момент отправки</div>
<div class="quiz-option" data-index="2">Хеш коммита считается в том числе от хеша родителя, поэтому изменение старого коммита меняет хеши всех последующих</div>
<div class="quiz-option" data-index="3">Git хранит контрольную сумму всей истории в отдельном файле и сверяет её при каждой команде</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 6. Что означает состояние «отсоединённый HEAD» (detached HEAD)?</h4>

<div class="quiz-option" data-index="0">Репозиторий потерял связь с удалённым сервером</div>
<div class="quiz-option" data-index="1">HEAD указывает напрямую на коммит, минуя ветку</div>
<div class="quiz-option" data-index="2">В рабочем каталоге есть незакоммиченные изменения</div>
<div class="quiz-option" data-index="3">Текущая ветка удалена на сервере, но осталась локально</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 7. Команду <code>echo "hello" | git hash-object --stdin</code> выполнили на двух разных компьютерах. Что получится?</h4>

<div class="quiz-option" data-index="0">Один и тот же хеш: имя объекта — это хеш его содержимого</div>
<div class="quiz-option" data-index="1">Разные хеши: в вычисление входит время выполнения команды</div>
<div class="quiz-option" data-index="2">Разные хеши: в вычисление входит имя пользователя из git config</div>
<div class="quiz-option" data-index="3">Ошибка: команда работает только внутри репозитория, где уже есть хотя бы один коммит</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 2: Базовые команды и индекс (Вопросы 8–16) ===== -->

<div class="quiz-question" data-correct="3">
<h4>Вопрос 8. Какую роль играет индекс (staging area)?</h4>

<div class="quiz-option" data-index="0">Ускоряет поиск по содержимому файлов, как индекс в базе данных</div>
<div class="quiz-option" data-index="1">Хранит список всех веток и тегов репозитория</div>
<div class="quiz-option" data-index="2">Кеширует объекты, скачанные с удалённого репозитория</div>
<div class="quiz-option" data-index="3">Промежуточная область, в которой собирается содержимое следующего коммита</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 9. В каком состоянии находится файл, который вы только что создали в рабочем каталоге и ни разу не добавляли командой git add?</h4>

<div class="quiz-option" data-index="0">Неотслеживаемый (untracked)</div>
<div class="quiz-option" data-index="1">Изменённый (modified)</div>
<div class="quiz-option" data-index="2">Подготовленный (staged)</div>
<div class="quiz-option" data-index="3">Зафиксированный (committed)</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 10. Чем <code>git add -p</code> полезнее, чем <code>git add .</code>?</h4>

<div class="quiz-option" data-index="0">Он работает быстрее на репозиториях с большим числом файлов</div>
<div class="quiz-option" data-index="1">Он сразу создаёт коммит, экономя одну команду</div>
<div class="quiz-option" data-index="2">Он показывает изменения кусками (hunks) и позволяет включить в коммит только часть правок одного файла</div>
<div class="quiz-option" data-index="3">Он добавляет в индекс в том числе файлы, перечисленные в .gitignore</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 11. Чем <code>git diff</code> отличается от <code>git diff --staged</code>?</h4>

<div class="quiz-option" data-index="0">git diff сравнивает две ветки, а git diff --staged — два коммита</div>
<div class="quiz-option" data-index="1">git diff сравнивает рабочий каталог с индексом, а git diff --staged — индекс с последним коммитом</div>
<div class="quiz-option" data-index="2">git diff показывает только имена изменённых файлов, а --staged — ещё и содержимое</div>
<div class="quiz-option" data-index="3">git diff работает до отправки на сервер, а --staged — только после</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 12. Что делает <code>git commit --amend</code>?</h4>

<div class="quiz-option" data-index="0">Добавляет новый коммит поверх последнего, не изменяя его</div>
<div class="quiz-option" data-index="1">Отменяет последний коммит, создавая обратный коммит</div>
<div class="quiz-option" data-index="2">Переносит последний коммит в другую ветку</div>
<div class="quiz-option" data-index="3">Переписывает последний коммит: у него меняется хеш</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 13. Файл application-local.properties был закоммичен неделю назад. Вы добавили его имя в .gitignore. Что произойдёт?</h4>

<div class="quiz-option" data-index="0">Файл будет удалён из репозитория при следующем коммите</div>
<div class="quiz-option" data-index="1">Git откажется коммитить, пока правило не убрано из .gitignore</div>
<div class="quiz-option" data-index="2">Ничего: .gitignore действует только на неотслеживаемые файлы, а этот уже под контролем версий</div>
<div class="quiz-option" data-index="3">Файл останется в репозитории, но Git перестанет замечать его изменения</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 14. В коммит попал рабочий пароль от базы данных, и коммит уже отправлен на сервер. Что нужно сделать в первую очередь?</h4>

<div class="quiz-option" data-index="0">Считать пароль скомпрометированным и сменить его, а чистку истории делать после</div>
<div class="quiz-option" data-index="1">Удалить пароль следующим коммитом — этого достаточно</div>
<div class="quiz-option" data-index="2">Добавить файл в .gitignore, тогда пароль исчезнет из истории</div>
<div class="quiz-option" data-index="3">Выполнить git reset --hard, чтобы стереть коммит у всех участников</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 15. Какая команда сдвинет ветку на один коммит назад, но оставит все изменения подготовленными в индексе?</h4>

<div class="quiz-option" data-index="0">git reset --hard HEAD~1</div>
<div class="quiz-option" data-index="1">git reset --soft HEAD~1</div>
<div class="quiz-option" data-index="2">git reset --mixed HEAD~1</div>
<div class="quiz-option" data-index="3">git restore --staged .</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 16. Ошибочный коммит уже в ветке main на сервере, и коллеги успели его забрать. Как правильно его отменить?</h4>

<div class="quiz-option" data-index="0">git reset --hard HEAD~1, затем git push --force</div>
<div class="quiz-option" data-index="1">git commit --amend с исправленным содержимым</div>
<div class="quiz-option" data-index="2">git restore --source=HEAD~1 для всех изменённых файлов</div>
<div class="quiz-option" data-index="3">git revert с хешем этого коммита — создать новый коммит с обратными изменениями</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 3: Ветвление и слияние (Вопросы 17–23) ===== -->

<div class="quiz-question" data-correct="0">
<h4>Вопрос 17. Почему создание ветки в Git — практически мгновенная операция независимо от размера проекта?</h4>

<div class="quiz-option" data-index="0">Ветка — это файл со ссылкой на один коммит, файлы проекта при её создании не копируются</div>
<div class="quiz-option" data-index="1">Git копирует только изменённые файлы, а остальные оставляет на месте</div>
<div class="quiz-option" data-index="2">Ветка создаётся на сервере, а локально ничего не происходит</div>
<div class="quiz-option" data-index="3">Перед созданием ветки Git сжимает рабочий каталог</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 18. Вы создали ветку feature от main, сделали два коммита, а main за это время не менялась. Что произойдёт при <code>git merge feature</code>?</h4>

<div class="quiz-option" data-index="0">Git создаст коммит слияния с двумя родителями</div>
<div class="quiz-option" data-index="1">Git откажется сливать и предложит сначала выполнить rebase</div>
<div class="quiz-option" data-index="2">Быстрая перемотка: указатель main просто переместится на вершину feature</div>
<div class="quiz-option" data-index="3">Возникнет конфликт, так как база слияния не определена</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 19. Зачем сливать ветку командой <code>git merge --no-ff</code>?</h4>

<div class="quiz-option" data-index="0">Чтобы ускорить слияние на больших репозиториях</div>
<div class="quiz-option" data-index="1">Чтобы Git автоматически разрешил все конфликты</div>
<div class="quiz-option" data-index="2">Чтобы перенести из ветки только часть коммитов</div>
<div class="quiz-option" data-index="3">Чтобы сохранить в истории факт существования отдельной ветки, создав коммит слияния</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 20. Какие три снимка сравнивает Git при трёхстороннем слиянии?</h4>

<div class="quiz-option" data-index="0">Первый коммит репозитория и вершины обеих веток</div>
<div class="quiz-option" data-index="1">Вершину текущей ветки, вершину сливаемой ветки и их общего предка</div>
<div class="quiz-option" data-index="2">Три последних коммита каждой из веток</div>
<div class="quiz-option" data-index="3">Индекс, рабочий каталог и последний коммит</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 21. Сколько родителей у коммита слияния?</h4>

<div class="quiz-option" data-index="0">Ни одного: он начинает новую линию истории</div>
<div class="quiz-option" data-index="1">Два или больше — по одному на каждую слитую линию</div>
<div class="quiz-option" data-index="2">Один, как у обычного коммита</div>
<div class="quiz-option" data-index="3">Столько, сколько файлов было изменено при слиянии</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 22. Что означает такой вывод команды <code>git log --oneline --graph</code>?<br><code>*&nbsp;&nbsp; 9c4e1a2 (HEAD -> main) Слияние ветки feature/search<br>|\<br>| * 71ba9f3 (feature/search) Добавить поиск по автору<br>| * 5e0c2d8 Добавить индекс по полю author<br>* | 3d7f4b1 Поправить README<br>|/<br>* 8f2c1a4 Начальная версия проекта</code></h4>

<div class="quiz-option" data-index="0">После общего предка 8f2c1a4 ветки развивались параллельно и были объединены коммитом слияния 9c4e1a2</div>
<div class="quiz-option" data-index="1">Ветка feature/search была влита быстрой перемоткой, коммита слияния нет</div>
<div class="quiz-option" data-index="2">Ветка feature/search ещё не влита в main</div>
<div class="quiz-option" data-index="3">В репозитории всего одна ветка, а отступы — просто оформление вывода</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 23. Какая модель ветвления лучше всего подходит для учебного или небольшого командного проекта с одной актуальной версией?</h4>

<div class="quiz-option" data-index="0">Git Flow с постоянной веткой develop и ветками release/* и hotfix/*</div>
<div class="quiz-option" data-index="1">Trunk-based development с флагами функций и выкладками несколько раз в день</div>
<div class="quiz-option" data-index="2">GitHub Flow: ветка на задачу, pull request, зелёный конвейер CI, слияние в main</div>
<div class="quiz-option" data-index="3">Работа без веток: все коммитят прямо в main без pull request</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 4: Конфликты слияния (Вопросы 24–28) ===== -->

<div class="quiz-question" data-correct="3">
<h4>Вопрос 24. Когда при слиянии возникает конфликт?</h4>

<div class="quiz-option" data-index="0">Всегда, когда обе ветки изменили один и тот же файл</div>
<div class="quiz-option" data-index="1">Когда в ветках разное количество коммитов</div>
<div class="quiz-option" data-index="2">Когда у сливаемых веток нет общего предка</div>
<div class="quiz-option" data-index="3">Когда обе ветки изменили одни и те же строки одного файла</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 25. После неудачного слияния в файле появились маркеры &lt;&lt;&lt;&lt;&lt;&lt;&lt; HEAD, ======= и &gt;&gt;&gt;&gt;&gt;&gt;&gt; feature/search. Что находится между первым и вторым маркером?</h4>

<div class="quiz-option" data-index="0">Версия из ветки feature/search, которую вы сливаете</div>
<div class="quiz-option" data-index="1">Версия из текущей ветки, в которую выполняется слияние</div>
<div class="quiz-option" data-index="2">Версия из общего предка обеих веток</div>
<div class="quiz-option" data-index="3">Вариант объединения, автоматически предложенный Git</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 26. Как полностью отменить начатое слияние и вернуться в состояние до него?</h4>

<div class="quiz-option" data-index="0">git reset --soft HEAD~1</div>
<div class="quiz-option" data-index="1">git revert HEAD</div>
<div class="quiz-option" data-index="2">git merge --abort</div>
<div class="quiz-option" data-index="3">git restore --staged .</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 27. Вы вручную объединили конфликтующие участки кода. Что обязательно сделать перед git add и git commit?</h4>

<div class="quiz-option" data-index="0">Убедиться, что не осталось ни одного маркера конфликта, и прогнать сборку с тестами</div>
<div class="quiz-option" data-index="1">Выполнить git fetch, чтобы обновить сведения о сервере</div>
<div class="quiz-option" data-index="2">Создать тег на будущем коммите слияния</div>
<div class="quiz-option" data-index="3">Переименовать ветку, чтобы конфликт не повторился</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 28. Что делает <code>git checkout --theirs BookService.java</code> во время разрешения конфликта?</h4>

<div class="quiz-option" data-index="0">Берёт версию файла из текущей ветки целиком</div>
<div class="quiz-option" data-index="1">Берёт версию файла из общего предка</div>
<div class="quiz-option" data-index="2">Оставляет оба варианта, разделив их маркерами</div>
<div class="quiz-option" data-index="3">Берёт версию файла из сливаемой ветки целиком</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 5: Удалённые репозитории и код-ревью (Вопросы 29–35) ===== -->

<div class="quiz-question" data-correct="3">
<h4>Вопрос 29. Что такое origin?</h4>

<div class="quiz-option" data-index="0">Основная ветка репозитория, создаваемая по умолчанию</div>
<div class="quiz-option" data-index="1">Первый коммит в истории проекта</div>
<div class="quiz-option" data-index="2">Служебный каталог внутри .git, где хранятся объекты</div>
<div class="quiz-option" data-index="3">Имя по умолчанию для удалённого репозитория</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 30. Чем <code>git fetch origin</code> отличается от <code>git pull origin main</code>?</h4>

<div class="quiz-option" data-index="0">fetch отправляет коммиты на сервер, а pull забирает их оттуда</div>
<div class="quiz-option" data-index="1">fetch только скачивает изменения и обновляет ветки вида origin/main, а pull дополнительно сливает их в текущую ветку</div>
<div class="quiz-option" data-index="2">fetch скачивает только сообщения коммитов, а pull — их содержимое</div>
<div class="quiz-option" data-index="3">fetch работает с одной веткой, а pull — сразу со всеми</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 31. Что даёт флаг -u в команде <code>git push -u origin feature/search</code>?</h4>

<div class="quiz-option" data-index="0">Отправляет ветку принудительно, затирая серверную версию</div>
<div class="quiz-option" data-index="1">Отправляет вместе с веткой все локальные теги</div>
<div class="quiz-option" data-index="2">Связывает локальную ветку с серверной, после чего push и pull работают без аргументов</div>
<div class="quiz-option" data-index="3">Создаёт ветку на сервере, но не отправляет в неё коммиты</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 32. git push отклонён с сообщением «rejected — non-fast-forward». Что произошло?</h4>

<div class="quiz-option" data-index="0">На сервере есть коммиты, которых нет у вас: нужно забрать их и отправить снова</div>
<div class="quiz-option" data-index="1">У вас нет прав на запись в этот репозиторий</div>
<div class="quiz-option" data-index="2">Ветка не связана с серверной, нужно выполнить git remote add</div>
<div class="quiz-option" data-index="3">В коммите слишком большие файлы, требуется Git LFS</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 33. Чем <code>git push --force-with-lease</code> безопаснее, чем <code>git push --force</code>?</h4>

<div class="quiz-option" data-index="0">Он сначала прогоняет тесты и отправляет изменения только при их успехе</div>
<div class="quiz-option" data-index="1">Он сохраняет резервную копию серверной ветки перед отправкой</div>
<div class="quiz-option" data-index="2">Он откажется затирать серверную ветку, если на ней появились коммиты, которых вы не видели</div>
<div class="quiz-option" data-index="3">Он требует подтверждения от второго участника команды</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 34. Что такое pull request на GitHub (merge request на GitLab)?</h4>

<div class="quiz-option" data-index="0">Команда Git, скачивающая изменения с сервера</div>
<div class="quiz-option" data-index="1">Автоматическое слияние ветки сразу после её отправки на сервер</div>
<div class="quiz-option" data-index="2">Запрос прав на запись в чужой репозиторий</div>
<div class="quiz-option" data-index="3">Механизм платформы: изменения выносятся на обсуждение, ревью и проверку CI до попадания в основную ветку</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 35. Какое утверждение о код-ревью соответствует практике, описанной в лекции?</h4>

<div class="quiz-option" data-index="0">Ревьюер должен вручную проверять форматирование и соблюдение стиля кода</div>
<div class="quiz-option" data-index="1">Механические проверки выполняет CI, а ревьюер смотрит на логику, читаемость, тесты и обработку ошибок</div>
<div class="quiz-option" data-index="2">Чем крупнее pull request, тем качественнее получается ревью</div>
<div class="quiz-option" data-index="3">Автор не должен отвечать на комментарии: он просто молча вносит правки</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 6: rebase и продвинутые инструменты (Вопросы 36–45) ===== -->

<div class="quiz-question" data-correct="0">
<h4>Вопрос 36. Что делает <code>git rebase main</code>, выполненный в ветке feature?</h4>

<div class="quiz-option" data-index="0">Переносит коммиты feature поверх вершины main, создавая новые коммиты с новыми хешами</div>
<div class="quiz-option" data-index="1">Сливает main в feature, создавая коммит слияния с двумя родителями</div>
<div class="quiz-option" data-index="2">Переносит указатель main на вершину feature</div>
<div class="quiz-option" data-index="3">Удаляет из feature все коммиты, кроме последнего</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 37. Какое утверждение верно различает merge и rebase?</h4>

<div class="quiz-option" data-index="0">merge сохраняет хеши коммитов и добавляет коммит слияния, а rebase создаёт новые коммиты и оставляет историю линейной</div>
<div class="quiz-option" data-index="1">merge создаёт линейную историю, а rebase — ветвистую</div>
<div class="quiz-option" data-index="2">merge меняет хеши коммитов, а rebase их сохраняет</div>
<div class="quiz-option" data-index="3">rebase безопасен для опубликованных веток, а merge — нет</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 38. Почему нельзя перебазировать ветку, которую уже забрали другие участники?</h4>

<div class="quiz-option" data-index="0">Git физически запретит выполнить такую операцию</div>
<div class="quiz-option" data-index="1">Rebase заменяет старые коммиты новыми, и после принудительной отправки история коллеги разойдётся с вашей</div>
<div class="quiz-option" data-index="2">Rebase удаляет ветку на сервере вместе с историей</div>
<div class="quiz-option" data-index="3">Rebase работает только с локальными ветками и выдаст ошибку при наличии upstream</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 39. В редакторе <code>git rebase -i HEAD~4</code> строки выглядят так:<br><code>pick&nbsp;&nbsp; 8f2c1a4 добавил поиск по автору<br>squash 3d7f4b1 ещё раз фикс<br>squash 5e0c2d8 фикс<br>reword 71ba9f3 доделал</code><br>Что получится в результате?</h4>

<div class="quiz-option" data-index="0">Четыре коммита останутся, изменятся только их сообщения</div>
<div class="quiz-option" data-index="1">Останется один коммит, включающий все четыре</div>
<div class="quiz-option" data-index="2">Rebase прервётся ошибкой: squash нельзя ставить сразу после pick</div>
<div class="quiz-option" data-index="3">Останется два коммита: объединённый из первых трёх и последний с переписанным сообщением</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 40. Зачем нужен Git LFS (Large File Storage)?</h4>

<div class="quiz-option" data-index="0">Чтобы ускорить клонирование за счёт сжатия истории коммитов</div>
<div class="quiz-option" data-index="1">Чтобы хранить в репозитории собранные JAR-файлы и скомпилированные классы</div>
<div class="quiz-option" data-index="2">Чтобы заменить большие бинарные файлы текстовыми указателями, а содержимое держать на отдельном сервере</div>
<div class="quiz-option" data-index="3">Чтобы автоматически разбивать большие коммиты на несколько мелких</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 41. Что делает <code>git cherry-pick a3f1c9e</code>?</h4>

<div class="quiz-option" data-index="0">Отменяет коммит a3f1c9e, создавая обратный коммит</div>
<div class="quiz-option" data-index="1">Переносит указатель текущей ветки на коммит a3f1c9e</div>
<div class="quiz-option" data-index="2">Сливает всю ветку, содержащую коммит a3f1c9e, в текущую</div>
<div class="quiz-option" data-index="3">Применяет изменения коммита a3f1c9e к текущей ветке, создавая новый коммит с новым хешем</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 42. Вы выполнили <code>git reset --hard HEAD~2</code> и поняли, что потеряли два нужных коммита. Что поможет?</h4>

<div class="quiz-option" data-index="0">git reflog: найти прежнюю позицию HEAD и вернуть ветку командой git reset --hard HEAD@{1}</div>
<div class="quiz-option" data-index="1">git revert последнего коммита вернёт прежнее состояние</div>
<div class="quiz-option" data-index="2">Ничего: reset --hard удаляет коммиты безвозвратно</div>
<div class="quiz-option" data-index="3">git pull origin main восстановит коммиты с сервера в любом случае</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 43. Ошибка появилась где-то за последние 300 коммитов. Что делает <code>git bisect</code>?</h4>

<div class="quiz-option" data-index="0">Перебирает коммиты подряд от старых к новым, пока не найдёт первый плохой</div>
<div class="quiz-option" data-index="1">Ищет строку с ошибкой во всех версиях файла и показывает её автора</div>
<div class="quiz-option" data-index="2">Ищет первый «плохой» коммит двоичным поиском: около 8–9 проверок вместо 300</div>
<div class="quiz-option" data-index="3">Автоматически отменяет коммиты по одному, пока тесты не начнут проходить</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 44. Зачем нужен <code>git stash</code>?</h4>

<div class="quiz-option" data-index="0">Чтобы отправить незавершённую работу на сервер в отдельную ветку</div>
<div class="quiz-option" data-index="1">Чтобы временно убрать незакоммиченные правки, получить чистый рабочий каталог и позже вернуть их обратно</div>
<div class="quiz-option" data-index="2">Чтобы отменить последний коммит, сохранив его изменения в индексе</div>
<div class="quiz-option" data-index="3">Чтобы заархивировать репозиторий вместе со всей историей</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 45. Какое утверждение о тегах в Git верно?</h4>

<div class="quiz-option" data-index="0">Тег уходит на сервер автоматически вместе с обычным git push</div>
<div class="quiz-option" data-index="1">Для релизов используют аннотированный тег (git tag -a), а на сервер теги отправляют отдельной командой</div>
<div class="quiz-option" data-index="2">Тег сдвигается вперёд при каждом новом коммите, как ветка</div>
<div class="quiz-option" data-index="3">Легковесный тег хранит автора, дату и сообщение</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 7: CI/CD (Вопросы 46–52) ===== -->

<div class="quiz-question" data-correct="3">
<h4>Вопрос 46. Чем непрерывная доставка (Continuous Delivery) отличается от непрерывного развёртывания (Continuous Deployment)?</h4>

<div class="quiz-option" data-index="0">Доставка собирает проект, а развёртывание только прогоняет тесты</div>
<div class="quiz-option" data-index="1">Доставка работает с тестовым стендом, а развёртывание — с машиной разработчика</div>
<div class="quiz-option" data-index="2">Доставка выполняется по расписанию, а развёртывание — после каждого коммита</div>
<div class="quiz-option" data-index="3">При доставке решение о выкладке на продуктив принимает человек, при развёртывании прошедшее проверки изменение выкладывается автоматически</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 47. Что такое непрерывная интеграция (CI)?</h4>

<div class="quiz-option" data-index="0">Автоматическая сборка и прогон тестов в чистом окружении после каждого изменения в репозитории</div>
<div class="quiz-option" data-index="1">Ежедневное ручное объединение веток разработчиков ответственным инженером</div>
<div class="quiz-option" data-index="2">Развёртывание приложения на продуктив несколько раз в день</div>
<div class="quiz-option" data-index="3">Практика написания тестов до реализации функциональности</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 48. Как соотносятся stage и job в конвейере GitLab CI?</h4>

<div class="quiz-option" data-index="0">Job состоит из нескольких stage, выполняемых по очереди</div>
<div class="quiz-option" data-index="1">Stage и job — синонимы, разница только в версии GitLab</div>
<div class="quiz-option" data-index="2">Stage — это группа заданий: стадии идут последовательно, а задания внутри одной стадии выполняются параллельно</div>
<div class="quiz-option" data-index="3">Stage выполняется на сервере, а job — на машине разработчика</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 49. Чем artifacts отличаются от cache в GitLab CI?</h4>

<div class="quiz-option" data-index="0">Artifacts — результаты задания (JAR, отчёты о тестах), сохраняемые для скачивания и следующих стадий, а cache — переиспользуемые между запусками данные, например локальный репозиторий Maven</div>
<div class="quiz-option" data-index="1">Artifacts хранятся вечно, а cache удаляется сразу после завершения задания</div>
<div class="quiz-option" data-index="2">Artifacts доступны только внутри одного задания, а cache — всем проектам сервера</div>
<div class="quiz-option" data-index="3">Разницы нет: это два названия одного механизма</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 50. В .gitlab-ci.yml задание deploy-production описано так:<br><code>rules:<br>&nbsp;&nbsp;- if: $CI_COMMIT_TAG =~ /^v\d+\.\d+\.\d+$/<br>&nbsp;&nbsp;&nbsp;&nbsp;when: manual</code><br>Когда оно выполнится?</h4>

<div class="quiz-option" data-index="0">При каждом push в любую ветку, автоматически</div>
<div class="quiz-option" data-index="1">При каждом слиянии merge request в main, автоматически</div>
<div class="quiz-option" data-index="2">Никогда: правило записано некорректно</div>
<div class="quiz-option" data-index="3">Только если коммит помечен тегом вида v1.0.0, и только после нажатия кнопки человеком</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 51. Где в проекте с GitLab CI должны храниться пароли и токены, нужные для развёртывания?</h4>

<div class="quiz-option" data-index="0">В файле .gitlab-ci.yml рядом с командами, которые их используют</div>
<div class="quiz-option" data-index="1">В защищённых переменных CI/CD в настройках проекта, откуда они попадают в задание как переменные окружения</div>
<div class="quiz-option" data-index="2">В отдельном файле secrets.properties, закоммиченном в репозиторий</div>
<div class="quiz-option" data-index="3">В описании merge request, чтобы ревьюер мог их проверить</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 52. Чем GitHub Actions отличается от GitLab CI по способу описания конвейера?</h4>

<div class="quiz-option" data-index="0">GitHub Actions настраивается только через веб-интерфейс, без файлов в репозитории</div>
<div class="quiz-option" data-index="1">GitHub Actions не умеет запускать тесты, он только собирает артефакты</div>
<div class="quiz-option" data-index="2">GitHub Actions описывается файлами в каталоге .github/workflows, где задания состоят из шагов и переиспользуют готовые действия через uses</div>
<div class="quiz-option" data-index="3">GitHub Actions требует отдельного сервера сборки, который команда разворачивает сама</div>
<div class="quiz-feedback"></div>
</div>

<!-- ===== РАЗДЕЛ 8: Agile, Scrum и Kanban (Вопросы 53–60) ===== -->

<div class="quiz-question" data-correct="2">
<h4>Вопрос 53. Какая из четырёх ценностей Agile-манифеста сформулирована верно?</h4>

<div class="quiz-option" data-index="0">Исчерпывающая документация важнее работающего продукта</div>
<div class="quiz-option" data-index="1">Следование первоначальному плану важнее готовности к изменениям</div>
<div class="quiz-option" data-index="2">Люди и взаимодействие важнее процессов и инструментов</div>
<div class="quiz-option" data-index="3">Согласование условий контракта важнее сотрудничества с заказчиком</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 54. Какое утверждение об Agile ошибочно?</h4>

<div class="quiz-option" data-index="0">Планирование в Agile есть, но короткими горизонтами и с регулярным пересмотром</div>
<div class="quiz-option" data-index="1">Agile означает отказ от документации и от дисциплины</div>
<div class="quiz-option" data-index="2">Scrum — лишь один из фреймворков, реализующих ценности Agile</div>
<div class="quiz-option" data-index="3">Короткие циклы требуют более строгой инженерной дисциплины, а не меньшей</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 55. Кто в Scrum определяет содержание и порядок бэклога продукта?</h4>

<div class="quiz-option" data-index="0">Скрам-мастер</div>
<div class="quiz-option" data-index="1">Команда разработчиков</div>
<div class="quiz-option" data-index="2">Руководитель отдела разработки</div>
<div class="quiz-option" data-index="3">Владелец продукта (Product Owner)</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 56. Что такое бэклог спринта (Sprint Backlog)?</h4>

<div class="quiz-option" data-index="0">Задачи, выбранные командой на текущий спринт, вместе с целью спринта и планом её достижения</div>
<div class="quiz-option" data-index="1">Полный упорядоченный список всего, что может понадобиться продукту</div>
<div class="quiz-option" data-index="2">Список дефектов, найденных на обзоре спринта</div>
<div class="quiz-option" data-index="3">Работоспособный результат спринта, соответствующий определению готовности</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="3">
<h4>Вопрос 57. Чем обзор спринта (Sprint Review) отличается от ретроспективы (Sprint Retrospective)?</h4>

<div class="quiz-option" data-index="0">Обзор проводит скрам-мастер, а ретроспективу — владелец продукта</div>
<div class="quiz-option" data-index="1">Обзор проходит в начале спринта, а ретроспектива — в его середине</div>
<div class="quiz-option" data-index="2">Обзор обязателен, а ретроспектива проводится по желанию команды</div>
<div class="quiz-option" data-index="3">Обзор — про продукт: что получилось и что делать дальше; ретроспектива — про процесс: как работали и что изменить</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="2">
<h4>Вопрос 58. Зачем команде определение готовности (Definition of Done)?</h4>

<div class="quiz-option" data-index="0">Чтобы зафиксировать срок, к которому задача должна быть выполнена</div>
<div class="quiz-option" data-index="1">Чтобы определить, какие задачи вообще можно брать в спринт</div>
<div class="quiz-option" data-index="2">Чтобы слово «готово» означало для всех одно и то же: код, тесты, ревью, зелёный конвейер, слияние в main</div>
<div class="quiz-option" data-index="3">Чтобы владелец продукта мог оценить задачу в стори-поинтах</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="0">
<h4>Вопрос 59. Что такое стори-поинты и скорость (velocity)?</h4>

<div class="quiz-option" data-index="0">Относительная оценка объёма работы и среднее число закрываемых за спринт поинтов, используемое для планирования следующего спринта</div>
<div class="quiz-option" data-index="1">Точная оценка задачи в часах и число часов, отработанных командой за спринт</div>
<div class="quiz-option" data-index="2">Оценка сложности кода статическим анализатором и её изменение от спринта к спринту</div>
<div class="quiz-option" data-index="3">Показатели, по которым сравнивают производительность разных команд</div>
<div class="quiz-feedback"></div>
</div>

<div class="quiz-question" data-correct="1">
<h4>Вопрос 60. В чём главное отличие Kanban от Scrum?</h4>

<div class="quiz-option" data-index="0">В Kanban задачи оцениваются в часах, а в Scrum — в стори-поинтах</div>
<div class="quiz-option" data-index="1">В Kanban нет спринтов и обязательных ролей: есть непрерывный поток задач и WIP-лимиты на столбцах доски</div>
<div class="quiz-option" data-index="2">В Kanban нет доски задач, работа ведётся по списку в трекере</div>
<div class="quiz-option" data-index="3">Kanban применяется только в производстве и не подходит для разработки программного обеспечения</div>
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
    'Вопрос 1': 'Полная локальная копия истории даёт мгновенные операции без сети и позволяет восстановить репозиторий с любого рабочего ноутбука, если сервер откажет.',
    'Вопрос 2': 'Неизменившиеся файлы не копируются заново, а переиспользуются по ссылке на прежний blob, поэтому восстановление любой версии — это «взять готовый снимок», а не применить сотни правок подряд.',
    'Вопрос 3': 'blob хранит только содержимое, а имена и структуру каталогов описывает tree — поэтому два одинаковых по содержимому файла с разными именами дают один blob и две записи в дереве.',
    'Вопрос 4': 'Коммит связывает снимок проекта (корневой tree) с местом в истории (родители) и метаданными; ветки, наоборот, сами ссылаются на коммит, а не перечислены внутри него.',
    'Вопрос 5': 'Цепочка хешей делает историю самопроверяемой: подмена одного байта в прошлом меняет идентификаторы всех коммитов после него, и расхождение сразу заметно.',
    'Вопрос 6': 'Обычно HEAD ссылается на ветку (ref: refs/heads/main); после git checkout по хешу он указывает прямо на коммит, и новые коммиты не принадлежат ни одной ветке — найти их потом можно только через reflog.',
    'Вопрос 7': 'Идентификатор объекта определяется исключительно его содержимым, поэтому один и тот же коммит на вашей машине и на сервере называется одинаково и централизованная нумерация версий не нужна.',
    'Вопрос 8': 'Индекс позволяет положить в коммит только часть сделанных правок — например, три файла из десяти — и собирать логически цельные коммиты вместо свалки изменений.',
    'Вопрос 9': 'Git о таком файле ничего не знает; состояние modified возможно только у файла, который уже находится под контролем версий.',
    'Вопрос 10': 'Именно так в коммит не попадает отладочный System.out.println, забытый в соседнем методе того же файла.',
    'Вопрос 11': 'Первая команда отвечает на вопрос «что я ещё не подготовил», вторая — «что именно уйдёт в следующий коммит».',
    'Вопрос 12': 'Пока коммит не отправлен на сервер, это удобный способ поправить сообщение или добавить забытый файл; после отправки amend превращается в переписывание опубликованной истории.',
    'Вопрос 13': 'Чтобы вывести уже отслеживаемый файл из-под контроля версий, нужен git rm --cached application-local.properties — он убирает файл из индекса, оставляя его на диске.',
    'Вопрос 14': 'Секрет остался в истории и в клонах у всех, кто успел забрать изменения, поэтому единственная надёжная мера — ротация самого пароля или ключа.',
    'Вопрос 15': 'Режим --soft двигает только указатель ветки, не трогая ни индекс, ни рабочий каталог, поэтому изменения сразу готовы к новому, переделанному коммиту.',
    'Вопрос 16': 'revert ничего не удаляет из опубликованной истории, а добавляет обратный коммит; reset с принудительной отправкой переписал бы историю, которую другие уже забрали, и сломал бы её у всей команды.',
    'Вопрос 17': 'Технически main — это файл .git/refs/heads/main с сорока символами хеша внутри; именно дешевизна ветвления и позволила заводить отдельную ветку под каждую задачу.',
    'Вопрос 18': 'Есть прямой путь вперёд по истории, поэтому новый коммит не нужен — Git двигает указатель, и история остаётся линейной.',
    'Вопрос 19': 'При запрете быстрой перемотки каждая задача видна в истории отдельным «пузырём», и её всегда можно рассмотреть или отменить целиком.',
    'Вопрос 20': 'Сравнение с общим предком (базой слияния) показывает, что именно изменила каждая сторона: правка только в одной ветке принимается автоматически, правка одних и тех же строк в обеих даёт конфликт.',
    'Вопрос 21': 'Именно наличие двух родителей фиксирует, что в этой точке сошлись две линии разработки, и рисует развилку в выводе git log --graph.',
    'Вопрос 22': 'Развилка после 8f2c1a4 и схождение линий в 9c4e1a2 — признак трёхстороннего слияния; при быстрой перемотке история выглядела бы одной прямой линией без коммита слияния.',
    'Вопрос 23': 'GitHub Flow даёт минимум правил, сохраняя ревью и автоматические проверки; Git Flow избыточен без нескольких поддерживаемых версий, а trunk-based требует зрелой культуры тестирования.',
    'Вопрос 24': 'Правки в разных местах одного файла Git объединяет сам; человек нужен только там, где обе стороны переписали одни и те же строки и машинного критерия правоты не существует.',
    'Вопрос 25': 'Верхний блок — это состояние HEAD, то есть ветки-приёмника, а нижний блок — состояние сливаемой ветки; версию предка Git покажет только при настройке merge.conflictstyle diff3.',
    'Вопрос 26': 'Команда --abort откатывает и индекс, и рабочий каталог к моменту перед слиянием; revert применим только к уже созданному коммиту, а reset и restore оставили бы репозиторий в промежуточном состоянии.',
    'Вопрос 27': 'Забытый маркер — гарантированная ошибка компиляции, а механически «склеенный» код часто собирается, но делает не то, поэтому одной вычитки глазами мало.',
    'Вопрос 28': 'Ключ --ours означает ветку, в которую сливают, а --theirs — ветку, которую сливают; обе команды заменяют файл целиком, поэтому правки второй стороны в нём теряются.',
    'Вопрос 29': 'Это просто короткое имя, которое Git присваивает удалённой копии при клонировании; удалённых репозиториев может быть несколько — например, при работе с форком добавляют ещё и upstream.',
    'Вопрос 30': 'После fetch рабочий каталог не меняется: вы смотрите git log HEAD..origin/main и сливаете осознанно, тогда как pull выполняет слияние сразу и может свалить конфликт в неподходящий момент.',
    'Вопрос 31': 'Именно эта связь (upstream) позволяет git status сообщать «ваша ветка опережает origin/main на 2 коммита».',
    'Вопрос 32': 'Серверная ветка ушла вперёд, и отправка стёрла бы чужие коммиты; правильное решение — забрать изменения и отправить снова, а не git push --force.',
    'Вопрос 33': 'Проверка «серверная ветка там же, где я видел её в последний раз» отсекает главный сценарий беды — потерю чужих коммитов, отправленных, пока вы перебазировали свою ветку.',
    'Вопрос 34': 'Это возможность хостинга, а не команда Git: она добавляет к обычному слиянию комментарии к конкретным строкам, обязательное одобрение ревьюеров и запрет слияния при красном конвейере.',
    'Вопрос 35': 'Ревьюер — слишком дорогой линтер, поэтому машине отдают всё, что она умеет проверять; к тому же изменение на 200 строк получит осмысленное ревью, а на 3000 — комментарий «выглядит нормально».',
    'Вопрос 36': 'Содержимое изменений сохраняется, но родитель у коммитов другой, а хеш считается в том числе от родителя — поэтому C3 и C4 превращаются в новые C3'+"'"+' и C4'+"'"+', а старые остаются в базе объектов без ссылок.',
    'Вопрос 37': 'В этом и состоит плата за красивую линейную историю: rebase удобнее для чтения и для git bisect, но переписывает коммиты, тогда как merge честно фиксирует реальный ход событий.',
    'Вопрос 38': 'Коллега продолжит работать поверх коммитов, которых на сервере больше нет, и получит конфликты в коде, которого не писал; поэтому общие ветки — main, develop, релизные — обновляют только через merge.',
    'Вопрос 39': 'Обе строки squash вливаются в стоящий выше pick, давая один коммит, а reword оставляет последний коммит отдельным и лишь предлагает изменить его сообщение.',
    'Вопрос 40': 'Git хранит каждую версию бинарного файла целиком и не умеет их сливать, поэтому история видео и макетов раздувает репозиторий; LFS оставляет в нём указатель размером в сотню байт, а данные скачиваются по требованию.',
    'Вопрос 41': 'Это удобно, когда исправление сделали в ветке разработки, а оно срочно нужно в релизной; но дублирующиеся изменения потом путают при полном слиянии, поэтому основным способом переноса кода cherry-pick быть не должен.',
    'Вопрос 42': 'Reflog — журнал всех перемещений HEAD и веток в локальном репозитории: сами коммиты остаются в базе объектов и достижимы по записям вида HEAD@{1}, пока не истёк срок хранения журнала.',
    'Вопрос 43': 'Каждая проверка отбрасывает половину диапазона, а в режиме git bisect run критерием служит код возврата команды, и весь поиск выполняется без участия человека.',
    'Вопрос 44': 'Это верхний ящик стола: правки прячутся локально командой git stash push и возвращаются через git stash pop, так что в истории не появляется коммит со сломанным кодом.',
    'Вопрос 45': 'Аннотированный тег — полноценный объект с автором, датой и сообщением, поэтому по нему видно, кто и когда выпустил версию; отправлять его нужно явно, например git push origin --tags.',
    'Вопрос 46': 'Обе практики требуют, чтобы после конвейера артефакт был готов к выпуску; разница ровно в одном — есть ли кнопка, которую нажимает человек.',
    'Вопрос 47': 'Смысл CI — короткая обратная связь и одинаковое окружение сборки: ошибку находят через пять минут после коммита, а фраза «но у меня на машине работает» перестаёт быть аргументом.',
    'Вопрос 48': 'Если задание падает, следующие стадии не запускаются — именно поэтому build ставят раньше test, а deploy делают последним.',
    'Вопрос 49': 'Артефакты — то, что произвела сборка и что нужно людям или следующим заданиям; кеш лишь ускоряет повторный запуск и может быть потерян без последствий для результата.',
    'Вопрос 50': 'Условие отбирает запуски по тегу семантической версии, а when: manual превращает задание в кнопку — это типичная реализация непрерывной доставки, где выкладку подтверждает человек.',
    'Вопрос 51': 'Всё, что попало в репозиторий, остаётся в истории и доступно каждому, у кого есть клон; защищённые переменные задаются вне кода и не показываются в логах заданий.',
    'Вопрос 52': 'Идея у обеих систем одна — задания, запускаемые событием в репозитории; отличаются ключевые слова и способ переиспользования, поэтому переход с одной системы на другую занимает день.',
    'Вопрос 53': 'Манифест расставляет приоритеты, не отрицая важности того, что справа: документация, планы и договоры нужны, но при выборе предпочтение отдаётся левой части.',
    'Вопрос 54': 'Документация сохраняется ровно в том объёме, который приносит пользу, а девятый принцип манифеста прямо требует постоянного внимания к техническому совершенству.',
    'Вопрос 55': 'Владелец продукта отвечает за ценность и решает «что» делать, команда решает «как» и «сколько успеет», а скрам-мастер отвечает за процесс и не является начальником команды.',
    'Вопрос 56': 'Бэклог продукта — это список всего и вся, за него отвечает владелец продукта; бэклог спринта принадлежит команде разработчиков, а инкремент — уже результат, а не план.',
    'Вопрос 57': 'Ретроспектива, не заканчивающаяся одним-двумя конкретными действиями с ответственным, — потерянное время, а обзор без работающего инкремента превращается в показ слайдов.',
    'Вопрос 58': 'Без общего списка условий технический долг копится незаметно, а «почти готовые» задачи держат линию диаграммы сгорания горизонтальной; условия входа в спринт описывает отдельное определение Definition of Ready.',
    'Вопрос 59': 'Люди систематически ошибаются в абсолютных оценках времени, но неплохо сравнивают задачи между собой; сравнивать velocity разных команд бессмысленно — шкалы у них разные, а требование роста ведёт к завышению оценок.',
    'Вопрос 60': 'Ограничение незавершённой работы заставляет команду сначала закрывать начатое: как на кухне с четырьмя конфорками, восемь одновременно готовящихся блюд не ускорят выдачу заказов.'
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
