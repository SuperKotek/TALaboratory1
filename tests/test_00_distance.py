"""Тесты для задания 00_distance.py — расстояния между городами."""
from __future__ import annotations

import ast
import math


# Исходные данные задания (дублируем здесь, чтобы тест был самодостаточным
# и независимо проверял корректность вычислений модуля).
SITES = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}


def expected_distances() -> dict:
    """Независимо строим ожидаемый словарь расстояний по той же формуле."""
    distances = {}
    for k1, v1 in SITES.items():
        for k2, v2 in SITES.items():
            if k1 != k2:
                distances[f'{k1}-{k2}'] = round(math.dist(v1, v2), 3)
    return distances


def test_module_runs_without_errors(run):
    """Модуль запускается, завершается с кодом 0 и не пишет в stderr."""
    res = run("00_distance")
    assert res.returncode == 0
    assert res.stderr == ""


def test_distances_dict_is_correct(run):
    """Выводимый словарь расстояний совпадает с независимо вычисленным."""
    res = run("00_distance")
    parsed = ast.literal_eval(res.stdout.strip())
    assert parsed == expected_distances()


def test_distances_keys_count(run):
    """Для трёх городов получается ровно 3*2 = 6 упорядоченных пар."""
    res = run("00_distance")
    parsed = ast.literal_eval(res.stdout.strip())
    assert len(parsed) == 6
    # Каждая пара городов представлена в обе стороны.
    assert 'Moscow-London' in parsed
    assert 'London-Moscow' in parsed
    assert parsed['Moscow-London'] == parsed['London-Moscow']


def test_symmetric_distance_value(run):
    """Расстояние Moscow-Paris совпадает с Paris-Moscow и равно ~130.384."""
    res = run("00_distance")
    parsed = ast.literal_eval(res.stdout.strip())
    assert parsed['Moscow-Paris'] == parsed['Paris-Moscow']
    assert parsed['Moscow-Paris'] == round(math.dist(SITES['Moscow'], SITES['Paris']), 3)
