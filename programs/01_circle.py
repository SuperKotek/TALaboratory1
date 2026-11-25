#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

# Есть значение радиуса круга
radius = 42
a_side = 50

# Выведите на консоль значение площади этого круга с точностью до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()
pi = 3.1415926
S = round(pi*radius*radius, 4)
print(S)


# Далее, пусть есть координаты точки
point_1 = (23, 34)
# где 23 - координата х, 34 - координата у

# Если точка point лежит внутри того самого круга [центр в начале координат (0, 0), radius = 42],
# то выведите на консоль True, Или False, если точка лежит вовне круга.
# подсказки:
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула так же есть в интернете
#       квадратный корень - это возведение в степень 0.5
#       операции сравнения дают булевы константы True и False
def IsPointInCircle(point, radius):

    Pifog = math.pow(point[0]**2 + point[1]**2, 0.5)
    print(Pifog <= radius)

def IsPointInTriangle(point, side):

    h = side * (3 ** 0.5) / 2
    print((point[1] >= -h / 3) and (point[1] <= 2 * h / 3 - abs(point[0]) / (3 ** 0.5)))

IsPointInCircle(point_1, radius)

# Аналогично для другой точки
point_2 = (30, 30)
point_3 = (40, 20)
point_4 = (1, 1)
# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
IsPointInCircle(point_2, radius)

IsPointInTriangle(point_2, a_side)
IsPointInTriangle(point_3, a_side)
IsPointInTriangle(point_4, a_side)
# Пример вывода на консоль:
#
# 77777.7777
# False
# False
