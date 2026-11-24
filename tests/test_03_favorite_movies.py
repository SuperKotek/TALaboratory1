"""Тесты для задания 03_favorite_movies.py — срезы строк."""
from __future__ import annotations

MOVIES = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Ожидаемые четыре фильма в порядке вывода задания:
#   первый, последний, второй, второй с конца.
EXPECTED_FILMS = ["Терминатор", "Назад в будущее", "Пятый элемент", "Чужие"]


def test_module_runs_without_errors(run):
    res = run("03_favorite_movies")
    assert res.returncode == 0
    assert res.stderr == ""


def test_four_films_printed(run):
    res = run("03_favorite_movies")
    lines = res.stdout.strip().splitlines()
    assert lines == EXPECTED_FILMS


def test_no_trailing_comma(run):
    """Ни в одной выведенной строке не должно быть запятой."""
    res = run("03_favorite_movies")
    for line in res.stdout.strip().splitlines():
        assert "," not in line
        assert " ," not in line


def test_each_film_is_substring_of_source():
    """Каждый выведенный фильм действительно присутствует в исходной строке."""
    for film in EXPECTED_FILMS:
        assert film in MOVIES
