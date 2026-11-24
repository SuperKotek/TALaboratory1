#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
menu.py — верхнеуровневый модуль-меню для лабораторной работы TALaboratory1.

Запускает любое из заданий лабораторной (модули 00_…10_ из каталога programs/)
через единый консольный интерфейс. Сами модули не изменяются: каждое задание
выполняется в отдельном процессе (subprocess), поэтому их вывод и поведение
полностью совпадают с самостоятельным запуском `python programs/<модуль>.py`.

Использование:
    python menu.py            # интерактивное меню
    python menu.py 3          # сразу запустить задание №3
    python menu.py all        # запустить все задания по очереди
    python menu.py list       # только вывести список заданий
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

# Каталог, в котором лежит этот файл — он же корень проекта.
PROJECT_DIR = Path(__file__).resolve().parent

# Каталог с модулями-заданиями 00_…10_: они вынесены в подпапку programs/,
# чтобы корень проекта содержал только точки входа (menu.py, run_tests.py),
# конфигурацию и тесты, а сами программы лежали отдельно.
PROGRAMS_DIR = PROJECT_DIR / "programs"

# Описатель задания: номер, имя файла и краткое человеческое описание.
TASKS: list[tuple[int, str, str]] = [
    (0, "00_distance.py",         "Расстояния между городами (словарь словарей)"),
    (1, "01_circle.py",           "Площадь круга и проверка точки внутри круга"),
    (2, "02_operations.py",       "Расстановка знаков операций между числами"),
    (3, "03_favorite_movies.py",  "Срезы строк: любимые фильмы"),
    (4, "04_my_family.py",        "Списки: рост членов семьи"),
    (5, "05_zoo.py",              "Список: зоопарк (insert/append/remove)"),
    (6, "06_songs_list.py",       "Списки и словари: время звучания песен"),
    (7, "07_secret.py",           "Расшифровка сообщения срезами строк"),
    (8, "08_garden.py",           "Множества: цветы из сада и луга"),
    (9, "09_shopping.py",         "Словарь: магазины с минимальными ценами"),
    (10, "10_store.py",           "Словарь: стоимость товаров на складе"),
]

# Быстрый доступ к описателю по номеру задания и по имени файла.
TASK_BY_NUMBER = {n: (n, fname, desc) for n, fname, desc in TASKS}


# --------------------------------------------------------------------------- #
# Вывод интерфейса
# --------------------------------------------------------------------------- #
def print_banner() -> None:
    """Печатает заголовок меню."""
    print()
    print("=" * 72)
    print(" Теория алгоритмов | Лабораторная работа 1 — меню запуска заданий")
    print("=" * 72)


def print_tasks() -> None:
    """Печатает пронумерованный список доступных заданий."""
    print()
    print("Доступные задания:")
    for number, fname, desc in TASKS:
        print(f"  [{number:>2}] {fname:<26} — {desc}")
    print()
    print("  [ a] Запустить все задания по очереди")
    print("  [ l] Только показать список заданий (list)")
    print("  [ q] Выход (quit)")
    print()


# --------------------------------------------------------------------------- #
# Запуск заданий
# --------------------------------------------------------------------------- #
def run_task(number: int) -> int:
    """
    Запускает модуль-задание с указанным номером в отдельном процессе и
    печатает его вывод. Возвращает код завершения процесса (0 — успех).
    """
    if number not in TASK_BY_NUMBER:
        print(f"Ошибка: задания с номером {number} не существует.", file=sys.stderr)
        return 2

    _, fname, desc = TASK_BY_NUMBER[number]
    script = PROGRAMS_DIR / fname
    if not script.is_file():
        print(f"Ошибка: файл задания не найден: {script}", file=sys.stderr)
        return 2

    # Подсветим границы вывода, чтобы было видно, где начинается и кончается
    # вывод конкретного задания.
    print("-" * 72)
    print(f"Запуск задания [{number}]: {fname} — {desc}")
    print("-" * 72)
    # Обязательно сбрасываем буфер stdout ДО запуска дочернего процесса:
    # иначе в неинтерактивном режиме (когда stdout — пайп, а не терминал)
    # заголовок печатается в буфер и всплывает в выводе уже после вывода
    # самого задания, потому что дочерний процесс пишет напрямую в fd.
    sys.stdout.flush()
    try:
        # cwd = каталог programs/, чтобы модуль находил свои файлы-данные,
        # если они появятся рядом с ним. Вывод наследуется от терминала (не
        # перехватываем), поэтому пользователь видит результат сразу и в
        # привычном виде.
        completed = subprocess.run(
            [sys.executable, str(script)],
            cwd=str(PROGRAMS_DIR),
        )
    except KeyboardInterrupt:
        print("\n(прервано пользователем)")
        return 130
    except OSError as exc:
        print(f"Ошибка запуска Python: {exc}", file=sys.stderr)
        return 1
    print()
    return completed.returncode


def run_all() -> int:
    """Последовательно запускает все задания. Возвращает 0, если все успешны."""
    worst = 0
    for number, _, _ in TASKS:
        rc = run_task(number)
        if rc != 0:
            worst = rc
    print("=" * 72)
    print(" Все задания выполнены." if worst == 0 else f" Завершено с ошибками (код {worst}).")
    print("=" * 72)
    return worst


# --------------------------------------------------------------------------- #
# Разбор ввода пользователя
# --------------------------------------------------------------------------- #
def parse_choice(raw: str) -> str | int:
    """
    Превращает строку ввода в команду.
    Возвращает:
      - int n  — номер задания для запуска;
      - 'all'  — запустить всё;
      - 'list' — показать список;
      - 'quit' — выход;
      - 'unknown' — неизвестная команда.
    """
    token = raw.strip().lower()
    if token in ("", "q", "quit", "exit"):
        return "quit"
    if token in ("a", "all"):
        return "all"
    if token in ("l", "list"):
        return "list"
    # Допускаем как "3", так и "03" — ведущие нули не имеют значения.
    if token.isdigit():
        return int(token)
    return "unknown"


# --------------------------------------------------------------------------- #
# Главный цикл
# --------------------------------------------------------------------------- #
def interactive_loop() -> int:
    """Основной интерактивный цикл меню. Возвращает код завершения программы."""
    print_banner()
    print_tasks()
    while True:
        try:
            raw = input("Выберите задание (0-10), a/l/q > ")
        except (EOFError, KeyboardInterrupt):
            # Ctrl-D / Ctrl-C — корректный выход из меню.
            print()
            return 0

        choice = parse_choice(raw)
        if choice == "quit":
            print("До свидания!")
            return 0
        if choice == "list":
            print_tasks()
            continue
        if choice == "all":
            return run_all()
        if choice == "unknown":
            print(f"Не понял команду «{raw.strip()}». "
                  f"Введите число от 0 до 10, a, l или q.")
            continue
        # choice — это номер задания (int).
        run_task(choice)


def main(argv: list[str] | None = None) -> int:
    """
    Точка входа. Поддерживает аргументы командной строки для неинтерактивного
    запуска (удобно для скриптов и тестов):
        python menu.py 3        # запустить задание 3
        python menu.py all      # запустить все
        python menu.py list     # показать список
    Без аргументов — интерактивное меню.
    """
    args = sys.argv[1:] if argv is None else argv

    # Без аргументов — интерактивный режим.
    if not args:
        return interactive_loop()

    # Флаг помощи.
    if args[0] in ("-h", "--help"):
        print(__doc__)
        return 0

    choice = parse_choice(args[0])
    if choice == "quit":
        return 0
    if choice == "list":
        print_banner()
        print_tasks()
        return 0
    if choice == "all":
        return run_all()
    if choice == "unknown":
        print(f"Неизвестная команда: {args[0]!r}", file=sys.stderr)
        print(__doc__, file=sys.stderr)
        return 2
    return run_task(choice)


if __name__ == "__main__":
    sys.exit(main())
