#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список животных в зоопарке
zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

# Посадите медведя (bear) между львом и кенгуру
# и выведите список на консоль
zoo.insert(1, 'bear')
print(zoo)


# Добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark']
# и выведите список на консоль
[zoo.append(bird) for bird in birds]
print(zoo)


# Уберите слона (elephant) из зоопарка
# и выведите список на консоль
zoo.remove('elephant')
print(zoo)

# Дополнительное задание - Добавление зверя в середину и вывод информации об этом (Тушканчик - jerboa)
zoo.insert(len(zoo)//2, 'jerboa')
print(zoo)
print(f"Тушканчик был добавлен в качестве элемента {zoo.index('jerboa')}")

# Выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть 1-индексированными (первая клетка - номер 1).
print(f"Лев - {zoo.index('lion')+1}, Жаворонок - {zoo.index('lark')+1},")
