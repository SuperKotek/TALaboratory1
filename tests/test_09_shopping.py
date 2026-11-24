"""Тесты для задания 09_shopping.py — магазины с минимальными ценами."""
from __future__ import annotations

import ast


# Исходные данные задания: для каждого магазина — список товаров с ценами.
SHOPS = {
    'ашан': [
        {'name': 'печенье', 'price': 10.99},
        {'name': 'конфеты', 'price': 34.99},
        {'name': 'карамель', 'price': 45.99},
        {'name': 'пирожное', 'price': 67.99},
    ],
    'пятерочка': [
        {'name': 'печенье', 'price': 9.99},
        {'name': 'конфеты', 'price': 32.99},
        {'name': 'карамель', 'price': 46.99},
        {'name': 'пирожное', 'price': 59.99},
    ],
    'магнит': [
        {'name': 'печенье', 'price': 11.99},
        {'name': 'конфеты', 'price': 30.99},
        {'name': 'карамель', 'price': 41.99},
        {'name': 'пирожное', 'price': 62.99},
    ],
}


def expected_cheapest() -> dict:
    """
    Независимо строим ожидаемый результат: для каждого товара — два магазина
    с минимальными ценами, отсортированные по возрастанию цены.
    """
    per_product = {}
    for shop, items in SHOPS.items():
        for item in items:
            per_product.setdefault(item['name'], []).append(
                {'shop': shop, 'price': item['price']}
            )
    result = {}
    for name, entries in per_product.items():
        result[name] = sorted(entries, key=lambda e: e['price'])[:2]
    return result


def test_module_runs_without_errors(run):
    res = run("09_shopping")
    assert res.returncode == 0
    assert res.stderr == ""


def test_sweets_dict_matches_two_cheapest(run):
    """Выводимый словарь содержит ровно два самых дешёвых магазина на товар."""
    res = run("09_shopping")
    parsed = ast.literal_eval(res.stdout.strip())
    assert parsed == expected_cheapest()


def test_four_products_present(run):
    res = run("09_shopping")
    parsed = ast.literal_eval(res.stdout.strip())
    assert set(parsed.keys()) == {'печенье', 'конфеты', 'карамель', 'пирожное'}


def test_two_shops_per_product(run):
    """На каждый товар указано ровно по два магазина."""
    res = run("09_shopping")
    parsed = ast.literal_eval(res.stdout.strip())
    for product, shops in parsed.items():
        assert len(shops) == 2


def test_prices_ascending(run):
    """В каждой паре магазинов первая цена не больше второй."""
    res = run("09_shopping")
    parsed = ast.literal_eval(res.stdout.strip())
    for product, shops in parsed.items():
        assert shops[0]['price'] <= shops[1]['price']


def test_cheapest_prices_correct():
    """Независимо проверяем минимальные цены на каждый товар."""
    expected = expected_cheapest()
    assert expected['печенье'][0]['price'] == 9.99      # пятерочка
    assert expected['конфеты'][0]['price'] == 30.99     # магнит
    assert expected['карамель'][0]['price'] == 41.99    # магнит
    assert expected['пирожное'][0]['price'] == 59.99    # пятерочка
