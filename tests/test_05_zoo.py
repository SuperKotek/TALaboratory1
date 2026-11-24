"""Тесты для задания 05_zoo.py — операции над списком (зоопарк)."""
from __future__ import annotations

import ast


def test_module_runs_without_errors(run):
    res = run("05_zoo")
    assert res.returncode == 0
    assert res.stderr == ""


def test_zoo_transformations(run):
    """Три выведенных списка соответствуют insert/extend/remove операциям."""
    res = run("05_zoo")
    lines = [line for line in res.stdout.splitlines() if line.strip()]
    # Первые три строки — списки, четвёртая — строка с индексами.
    assert len(lines) == 4

    # Независимо воспроизводим все трансформации списка.
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
    zoo.insert(1, 'bear')
    assert ast.literal_eval(lines[0]) == zoo

    zoo.extend(['rooster', 'ostrich', 'lark'])
    assert ast.literal_eval(lines[1]) == zoo

    zoo.remove('elephant')
    assert ast.literal_eval(lines[2]) == zoo


def test_indices_line(run):
    """Лев в клетке №1, жаворонок в клетке №7 (1-индексированные номера)."""
    res = run("05_zoo")
    lines = [line for line in res.stdout.splitlines() if line.strip()]
    indices_line = lines[3]
    assert "Лев - 1" in indices_line
    assert "Жаворонок - 7" in indices_line


def test_indices_arithmetic():
    """Независимо проверяем номера клеток после всех трансформаций."""
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
    zoo.insert(1, 'bear')
    zoo.extend(['rooster', 'ostrich', 'lark'])
    zoo.remove('elephant')
    assert zoo.index('lion') + 1 == 1
    assert zoo.index('lark') + 1 == 7
