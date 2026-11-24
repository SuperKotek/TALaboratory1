"""Тесты для задания 10_store.py — стоимость товаров на складе."""
from __future__ import annotations


GOODS = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

STORE = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}


def expected_lines() -> list:
    """Независимо считаем ожидаемые строки вывода для каждого товара."""
    code_to_name = {code: name for name, code in GOODS.items()}
    lines = []
    for code, batches in STORE.items():
        total_qty = sum(b['quantity'] for b in batches)
        total_sum = sum(b['quantity'] * b['price'] for b in batches)
        lines.append(f"{code_to_name[code]} - {total_qty} шт, стоимость {total_sum} руб")
    return lines


def test_module_runs_without_errors(run):
    res = run("10_store")
    assert res.returncode == 0
    assert res.stderr == ""


def test_four_products_printed(run):
    res = run("10_store")
    lines = [line for line in res.stdout.splitlines() if line.strip()]
    assert len(lines) == 4


def test_totals_correct(run):
    """Каждая строка содержит правильные количество и сумму по товару."""
    res = run("10_store")
    lines = [line for line in res.stdout.splitlines() if line.strip()]
    assert lines == expected_lines()


def test_specific_values(run):
    """Проверяем конкретные ожидаемые значения для каждого товара."""
    res = run("10_store")
    output = res.stdout
    assert "Лампа - 27 шт, стоимость 1134 руб" in output
    assert "Стол - 54 шт, стоимость 27860 руб" in output
    assert "Диван - 3 шт, стоимость 3550 руб" in output
    assert "Стул - 105 шт, стоимость 10311 руб" in output


def test_totals_arithmetic():
    """Независимо проверяем арифметику сумм по каждому товару."""
    # Лампа: 27 * 42
    assert 27 * 42 == 1134
    # Стол: 22*510 + 32*520
    assert 22 * 510 + 32 * 520 == 27860
    # Диван: 2*1200 + 1*1150
    assert 2 * 1200 + 1 * 1150 == 3550
    # Стул: 50*100 + 12*95 + 43*97
    assert 50 * 100 + 12 * 95 + 43 * 97 == 10311
