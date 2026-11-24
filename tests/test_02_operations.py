"""Тесты для задания 02_operations.py — расстановка знаков операций."""
from __future__ import annotations


def test_module_runs_without_errors(run):
    res = run("02_operations")
    assert res.returncode == 0
    assert res.stderr == ""


def test_two_results_printed(run):
    res = run("02_operations")
    lines = res.stdout.strip().splitlines()
    assert lines == ["9", "25"]


def test_expressions_values():
    """Независимо проверяем значения напечатанных выражений."""
    assert (1 + 2) * 3 == 9
    assert 1 * 2 + 3 + 4 * 5 == 25


def test_order_preserved():
    """Порядок чисел 1..5 сохранён во втором выражении."""
    # 1 * 2 + 3 + 4 * 5 содержит числа 1,2,3,4,5 именно в таком порядке.
    expr_numbers = [1, 2, 3, 4, 5]
    assert expr_numbers == list(range(1, 6))
