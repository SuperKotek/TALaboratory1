"""Общие фикстуры и помощники для тестов лабораторной работы TALaboratory1.

Все модули-задания (00_…10_) — это скрипты, которые печатают результат в
stdout на верхнем уровне (без функций-обёрток и без `if __name__ == '__main__'`).
Поэтому самый честный способ их протестировать — запустить файл как отдельный
процесс и проверить вывод. Это гарантирует, что тесты проверяют ровно то
поведение, которое получит студент при самостоятельном запуске `python …`.

Модули-задания лежат в каталоге `programs/` рядом с тестами (не внутри `tests/`),
поэтому путь к программе вычисляется как «выйти из tests/ в корень проекта,
затем зайти в programs/»:  tests/  ->  ..  ->  programs/<модуль>.py.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

# Корень проекта: на один уровень выше каталога tests/ (где лежит этот файл).
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Каталог с модулями-заданиями 00_…10_: подпапка programs/ в корне проекта.
# Тесты ищут программы не у себя в tests/, а в ../programs/.
PROGRAMS_DIR = PROJECT_ROOT / "programs"

# Добавляем корень проекта в sys.path, чтобы тесты могли импортировать menu.py
# (он лежит в корне, а не в каталоге tests/).
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def run_module(module_name: str) -> subprocess.CompletedProcess:
    """
    Запускает модуль проекта (например, "00_distance") как отдельный процесс
    и возвращает CompletedProcess с перехваченными stdout/stderr.

    Параметр module_name — имя файла без расширения «.py». Программа ищется
    в каталоге programs/ корня проекта (../programs/ относительно tests/).
    """
    script = PROGRAMS_DIR / f"{module_name}.py"
    assert script.is_file(), f"Файл задания не найден: {script}"
    return subprocess.run(
        [sys.executable, str(script)],
        cwd=str(PROGRAMS_DIR),
        capture_output=True,
        text=True,
        timeout=30,
    )


@pytest.fixture
def run():
    """Фикстура, возвращающая функцию run_module для удобного вызова в тестах."""
    return run_module


@pytest.fixture(scope="session")
def project_root() -> Path:
    """Путь к корню проекта (каталогу с menu.py, programs/ и tests/)."""
    return PROJECT_ROOT


@pytest.fixture(scope="session")
def programs_dir() -> Path:
    """Путь к каталогу programs/, где лежат модули-задания."""
    return PROGRAMS_DIR
