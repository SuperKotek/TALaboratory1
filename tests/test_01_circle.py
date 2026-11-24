"""Тесты для задания 01_circle.py — площадь круга и проверка точки внутри."""
from __future__ import annotations

import math

PI = 3.1415926
RADIUS = 42


def test_module_runs_without_errors(run):
    res = run("01_circle")
    assert res.returncode == 0
    assert res.stderr == ""


def test_area_value(run):
    """Площадь круга печатается с 4 знаками после запятой и равна pi*r^2."""
    res = run("01_circle")
    lines = res.stdout.strip().splitlines()
    assert len(lines) == 3
    expected_area = round(PI * RADIUS ** 2, 4)
    assert float(lines[0]) == expected_area
    # Должно быть 4 знака после запятой.
    assert "." in lines[0]
    assert len(lines[0].split(".")[1]) == 4


def test_point_inside_circle_true(run):
    """Точка (23, 34) лежит внутри круга R=42: sqrt(23^2+34^2) ~ 41.05 < 42."""
    res = run("01_circle")
    lines = res.stdout.strip().splitlines()
    assert lines[1].strip() == "True"
    assert math.dist((23, 34), (0, 0)) < RADIUS


def test_point_outside_circle_false(run):
    """Точка (30, 30) лежит вне круга R=42: sqrt(1800) ~ 42.43 > 42."""
    res = run("01_circle")
    lines = res.stdout.strip().splitlines()
    assert lines[2].strip() == "False"
    assert math.dist((30, 30), (0, 0)) > RADIUS


def test_output_order(run):
    """Полный вывод: площадь, затем результат для двух точек."""
    res = run("01_circle")
    expected_area = round(PI * RADIUS ** 2, 4)
    expected = f"{expected_area}\nTrue\nFalse"
    assert res.stdout.strip() == expected
