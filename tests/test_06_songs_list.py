"""Тесты для задания 06_songs_list.py — сумма времён звучания песен."""
from __future__ import annotations


def test_module_runs_without_errors(run):
    res = run("06_songs_list")
    assert res.returncode == 0
    assert res.stderr == ""


def test_two_sums_printed(run):
    res = run("06_songs_list")
    lines = res.stdout.strip().splitlines()
    assert lines == ["14.93", "13.49"]


def test_list_sum_arithmetic():
    """Halo + Enjoy the Silence + Clean из списка, округлено до 3 знаков."""
    violator_songs_list = [
        ['World in My Eyes', 4.86],
        ['Sweetest Perfection', 4.43],
        ['Personal Jesus', 4.56],
        ['Halo', 4.9],
        ['Waiting for the Night', 6.07],
        ['Enjoy the Silence', 4.20],
        ['Policy of Truth', 4.76],
        ['Blue Dress', 4.29],
        ['Clean', 5.83],
    ]
    total = round(violator_songs_list[3][1] + violator_songs_list[5][1] + violator_songs_list[8][1], 3)
    assert total == 14.93


def test_dict_sum_arithmetic():
    """Sweetest Perfection + Policy of Truth + Blue Dress из словаря."""
    violator_songs_dict = {
        'World in My Eyes': 4.76,
        'Sweetest Perfection': 4.43,
        'Personal Jesus': 4.56,
        'Halo': 4.30,
        'Waiting for the Night': 6.07,
        'Enjoy the Silence': 4.6,
        'Policy of Truth': 4.88,
        'Blue Dress': 4.18,
        'Clean': 5.68,
    }
    total = round(
        violator_songs_dict['Sweetest Perfection']
        + violator_songs_dict['Policy of Truth']
        + violator_songs_dict['Blue Dress'],
        3,
    )
    assert total == 13.49
