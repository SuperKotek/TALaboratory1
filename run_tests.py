#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""run_tests.py — единая точка запуска всех тестов лабораторной работы."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

# Корень проекта: каталог, где лежит этот файл, menu.py и модули-задания.
PROJECT_DIR = Path(__file__).resolve().parent
TESTS_DIR = PROJECT_DIR / "tests"

def list_test_files() -> list[Path]:
    """Возвращает отсортированный список всех файлов тестов test_*.py."""
    return sorted(TESTS_DIR.glob("test_*.py"))


def print_banner(test_files: list[Path]) -> None:
    """Печатает заголовок и список запускаемых файлов тестов."""
    print()
    print("=" * 72)
    print(" Лабораторная работа 1 — запуск всех тестов pytest")
    print("=" * 72)
    print(f"Каталог тестов: {TESTS_DIR}")
    print(f"Найдено файлов тестов: {len(test_files)}")
    for path in test_files:
        print(f"  • {path.relative_to(PROJECT_DIR)}")
    print("=" * 72)
    print()


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv

    test_files = list_test_files()
    if not test_files:
        print("Ошибка: файлы тестов не найдены в каталоге tests/.", file=sys.stderr)
        return 2

    print_banner(test_files)

    # Если аргументы не переданы — запускаем весь каталог tests/ целиком.
    # Если переданы (файл, -v, -k и т. п.) — отдаём их pytest как есть,
    # чтобы можно было запускать конкретный файл или фильтровать тесты.
    pytest_args = args if args else [str(TESTS_DIR)]
    cmd = [sys.executable, "-m", "pytest", *pytest_args]

    # Сбрасываем буфер stdout ДО запуска дочернего процесса: иначе в
    # неинтерактивном режиме (когда stdout — пайп) наш баннер печатается в
    # буфер и всплывает в выводе уже после отчёта pytest, потому что дочерний
    # процесс пишет напрямую в файловый дескриптор.
    sys.stdout.flush()

    # subprocess.call сам напечатает вывод pytest в терминал и вернёт его
    # код завершения (0 — все тесты прошли, ненулевое значение — есть падения).
    return subprocess.call(cmd, cwd=str(PROJECT_DIR))


if __name__ == "__main__":
    sys.exit(main())
