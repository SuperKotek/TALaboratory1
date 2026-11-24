"""Тесты для задания 04_my_family.py — списки и рост семьи."""
from __future__ import annotations


def test_module_runs_without_errors(run):
    res = run("04_my_family")
    assert res.returncode == 0
    assert res.stderr == ""


def test_father_height_line(run):
    """Строка про рост отца выводится в нужном формате."""
    res = run("04_my_family")
    assert "Рост отца - 170 см" in res.stdout


def test_total_family_height_line(run):
    """Общий рост семьи выводится в нужном формате и равен сумме ростов."""
    res = run("04_my_family")
    assert "Общий рост моей семьи - 664 см" in res.stdout


def test_total_height_arithmetic():
    """Независимо проверяем сумму ростов всех членов семьи."""
    heights = [170, 166, 172, 156]  # Отец, Мать, Дедушка, Бабушка
    assert sum(heights) == 664
