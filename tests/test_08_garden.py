"""Тесты для задания 08_garden.py — операции над множествами цветов.

Вывод модуля — это шесть строк с литералами множеств set(...). Порядок
элементов в множестве не детерминирован (hash randomization), поэтому тест
парсит каждую строку в настоящее множество и сравнивает как множество,
а не как строку.
"""
from __future__ import annotations

import ast


GARDEN = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')
MEADOW = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')


def parse_output_sets(output: str) -> list:
    """Парсит непустые строки вывода в объекты set."""
    return [ast.literal_eval(line) for line in output.splitlines() if line.strip()]


def test_module_runs_without_errors(run):
    res = run("08_garden")
    assert res.returncode == 0
    assert res.stderr == ""


def test_six_lines_printed(run):
    """Модуль печатает ровно шесть множеств: сад, луг, объединение,
    пересечение, только сад, только луг."""
    res = run("08_garden")
    sets = parse_output_sets(res.stdout)
    assert len(sets) == 6


def test_garden_and_meadow_sets(run):
    res = run("08_garden")
    sets = parse_output_sets(res.stdout)
    assert sets[0] == set(GARDEN)
    assert sets[1] == set(MEADOW)


def test_union(run):
    res = run("08_garden")
    sets = parse_output_sets(res.stdout)
    assert sets[2] == set(GARDEN) | set(MEADOW)


def test_intersection(run):
    res = run("08_garden")
    sets = parse_output_sets(res.stdout)
    assert sets[3] == set(GARDEN) & set(MEADOW)


def test_garden_only(run):
    """Цветы, которые растут в саду, но не на лугу."""
    res = run("08_garden")
    sets = parse_output_sets(res.stdout)
    assert sets[4] == set(GARDEN) - set(MEADOW)


def test_meadow_only(run):
    """Цветы, которые растут на лугу, но не в саду."""
    res = run("08_garden")
    sets = parse_output_sets(res.stdout)
    assert sets[5] == set(MEADOW) - set(GARDEN)


def test_intersection_subset_of_each():
    """Пересечение должно быть подмножеством и сада, и луга."""
    g, m = set(GARDEN), set(MEADOW)
    assert (g & m).issubset(g)
    assert (g & m).issubset(m)
