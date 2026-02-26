# Темы презентаций: Ядро Linux и модули ядра

Данный раздел содержит темы групповых презентаций. Каждая тема рассчитана на группу из 2–3 студентов.

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

- Презентация должна содержать **примеры кода** на языке C (код модулей ядра, системные вызовы и т.д.)
- Необходимо включить **схемы и диаграммы** для иллюстрации архитектуры
- Рекомендуется подготовить **демонстрацию** (видео или live-demo в виртуальной машине)
- Все утверждения должны быть подкреплены **ссылками на источники**

---

## Темы презентаций

| № | Тема | Основные вопросы для раскрытия |
|:-:|------|-------------------------------|
| 1 | **Архитектура ядра Linux** (Linux Kernel Architecture) | История и эволюция ядра Linux; монолитное ядро vs микроядро vs гибридное; основные подсистемы ядра (процессы, память, VFS, сеть, драйверы); пространство ядра vs пользовательское пространство (Ring 0 / Ring 3); механизм системных вызовов (`int 0x80` / `syscall`) |
| 2 | **Система сборки ядра Linux** (Kernel Build System) | Kconfig и инструменты конфигурации (`menuconfig`, `nconfig`, `xconfig`); иерархия Makefile и Kbuild; полный цикл сборки (`make menuconfig` → `make` → `make modules` → `make install`); кросс-компиляция (`ARCH`, `CROSS_COMPILE`, ARM/RISC-V); управление конфигурацией (`.config`, `defconfig`, `oldconfig`) |
| 3 | **Загружаемые модули ядра — LKM** (Loadable Kernel Modules) | Структура модуля: `module_init()`, `module_exit()`, `MODULE_LICENSE`; Makefile для out-of-tree модулей; утилиты `insmod`, `rmmod`, `lsmod`, `modinfo`; параметры модулей (`module_param()`, типы, права доступа); интерфейсы `/proc/modules` и `/sys/module/` |
| 4 | **Динамические загружаемые модули — DLKM** (Dynamic Loadable Kernel Modules) | Различие LKM и DLKM; `modprobe` и разрешение зависимостей (`depmod`, `modules.dep`, `modules.alias`); экспорт символов: `EXPORT_SYMBOL()`, `EXPORT_SYMBOL_GPL()`; наложение модулей (module stacking), межмодульная коммуникация; автозагрузка через udev, `/etc/modprobe.d/`, чёрные списки |
| 5 | **Драйверы символьных устройств** (Character Device Drivers) | Классификация устройств: символьные, блочные, сетевые; номера major/minor: `register_chrdev_region()`, `alloc_chrdev_region()`; структура `file_operations` (`open`, `read`, `write`, `release`, `ioctl`); API `cdev`: `cdev_init()`, `cdev_add()`, `cdev_del()`; создание узлов: `mknod`, udev, `device_create()` |
| 6 | **Драйверы блочных устройств** (Block Device Drivers) | Блочные vs символьные устройства; `gendisk` и `block_device_operations`; очереди запросов (request queues) и структуры `bio`; планировщики I/O: `noop`, `deadline`, `CFQ`, `mq-deadline`, `BFQ`, `kyber`; RAM-диск как практический пример (модуль `brd`) |
| 7 | **Управление памятью в ядре** (Kernel Memory Management) | Адресное пространство: `ZONE_DMA`, `ZONE_NORMAL`, `ZONE_HIGHMEM`; страничный аллокатор и buddy system; SLAB/SLUB/SLOB: `kmalloc()`, `kfree()`, `kmem_cache_create()`; `vmalloc()` vs `kmalloc()`; таблицы страниц, TLB и OOM killer |
| 8 | **Планирование процессов** (Process Scheduling) | `task_struct` и состояния процесса; CFS: красно-чёрное дерево, `vruntime`; политики реального времени: `SCHED_FIFO`, `SCHED_RR`, `SCHED_DEADLINE`; значения `nice`, приоритеты, классы планирования; CPU affinity (`taskset`) и контроллер CPU в cgroups |
| 9 | **Виртуальная файловая система — VFS** (Virtual File System) | Архитектура VFS (единообразный интерфейс для всех ФС); ключевые структуры: `superblock`, `inode`, `dentry`, `file`; регистрация ФС: `register_filesystem()`, `mount()`; procfs (`/proc`): создание записей, `seq_file`; sysfs (`/sys`): `kobject`, взаимодействие ядра и user space |
| 10 | **Сетевой стек Linux** (Networking Stack) | Архитектура стека (сокеты, протоколы, устройства); `sk_buff` — контейнер сетевых пакетов; Netfilter: hooks и `iptables`/`nftables`; написание модуля Netfilter для фильтрации пакетов; сетевые драйверы: `net_device`, NAPI |
| 11 | **Модули безопасности ядра — LSM** (Linux Security Modules) | Архитектура LSM и security hooks; SELinux: мандатное управление доступом, политики, контексты; AppArmor: профильное управление доступом; Linux capabilities: `CAP_NET_ADMIN`, `CAP_SYS_ADMIN` и др.; seccomp и seccomp-BPF: фильтрация системных вызовов |
| 12 | **Отладка ядра и модулей** (Kernel Debugging) | `printk()`: уровни, `dmesg`, dynamic debug; ftrace: function tracer, function_graph, trace events; kprobes и kretprobes: динамическая инструментация; KGDB/KDB: настройка ядерного отладчика; kdump и crash: анализ crash-дампов (vmcore) |
| 13 | **Механизмы синхронизации в ядре** (Kernel Synchronization) | Гонки данных в контексте ядра (IRQ, preemption, SMP); спинлоки: `spin_lock()`, `spin_lock_irqsave()`; мьютексы и семафоры в ядре; RCU: `rcu_read_lock()`, `synchronize_rcu()`; атомарные операции (`atomic_t`) и барьеры памяти (`mb()`, `rmb()`, `wmb()`) |
| 14 | **Взаимодействие ядра и user space** (Kernel–Userspace Communication) | Системные вызовы: таблица syscall, `copy_from_user`/`copy_to_user`; `ioctl`: `_IOW`/`_IOR`/`_IOWR`; procfs и sysfs для обмена информацией; Netlink-сокеты для асинхронной коммуникации; `mmap` — разделяемая память ядра и user space |
| 15 | **Процесс загрузки Linux** (Boot Process) | BIOS vs UEFI, POST, MBR vs GPT; загрузчик GRUB2: этапы, `grub.cfg`; распаковка и инициализация ядра (`start_kernel()`); initramfs/initrd: назначение, содержимое, `mkinitramfs`/`dracut`; передача управления init-системе (systemd / SysVinit / OpenRC) |
| 16 | **Контейнеризация: Namespaces и Cgroups** (Namespaces & Control Groups) | 7 типов namespaces (PID, network, mount, UTS, IPC, user, cgroup); `unshare`, `nsenter`, флаги `clone()`; cgroups v1 vs v2: архитектура и контроллеры (cpu, memory, io, pids); как Docker/Podman используют namespaces + cgroups; rootless-контейнеры, Kata Containers |

---

## Распределение тем

| № | Тема | Группа | Участники | Дата выступления |
|:-:|------|--------|-----------|:----------------:|
| 1 | Архитектура ядра Linux | — | — | — |
| 2 | Система сборки ядра Linux | — | — | — |
| 3 | Загружаемые модули ядра (LKM) | — | — | — |
| 4 | Динамические загружаемые модули (DLKM) | — | — | — |
| 5 | Драйверы символьных устройств | — | — | — |
| 6 | Драйверы блочных устройств | — | — | — |
| 7 | Управление памятью в ядре | — | — | — |
| 8 | Планирование процессов | — | — | — |
| 9 | Виртуальная файловая система (VFS) | — | — | — |
| 10 | Сетевой стек Linux | — | — | — |
| 11 | Модули безопасности ядра (LSM) | — | — | — |
| 12 | Отладка ядра и модулей | — | — | — |
| 13 | Механизмы синхронизации в ядре | — | — | — |
| 14 | Ядро и пользовательское пространство | — | — | — |
| 15 | Процесс загрузки Linux | — | — | — |
| 16 | Контейнеризация: Namespaces и Cgroups | — | — | — |

> **Порядок выбора:** Темы выбираются в порядке очереди. Каждая тема может быть выбрана только одной группой. Для регистрации темы обратитесь к преподавателю.

---

## Полезные ресурсы

### Книги

- **Linux Kernel Development** — Robert Love (3rd Edition)
- **Linux Device Drivers** — Jonathan Corbet, Alessandro Rubini, Greg Kroah-Hartman (3rd Edition, доступна бесплатно на lwn.net)
- **Understanding the Linux Kernel** — Daniel P. Bovet, Marco Cesati (3rd Edition)
- **The Linux Programming Interface** — Michael Kerrisk

### Онлайн-ресурсы

- [The Linux Kernel Documentation](https://www.kernel.org/doc/html/latest/) — официальная документация ядра
- [Linux Kernel Module Programming Guide](https://sysprog21.github.io/lkmpg/) — руководство по написанию модулей ядра
- [LWN.net](https://lwn.net/) — новости и статьи о разработке ядра Linux
- [Kernel Newbies](https://kernelnewbies.org/) — ресурс для начинающих разработчиков ядра
- [Bootlin Elixir Cross-Referencer](https://elixir.bootlin.com/linux/latest/source) — навигация по исходному коду ядра
- [Linux Insides](https://0xax.gitbooks.io/linux-insides/content/) — подробное описание внутренностей ядра
