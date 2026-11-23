#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

for k1, v1 in sites.items():
    for k2, v2 in sites.items():
        if k1 != k2:
            distances[f'{k1}-{k2}'] = round(((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2) ** 0.5, 3)


print(distances)
