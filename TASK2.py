# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random
n = int(input("Введите число элементов в массиве: "))
list_1 = []
for i in range(n):
    from random import randint
    list_1.append(random.randint(0, n))
print(list_1)
x = int(input("Введите искомое число: "))
index_element = 0
min_element = abs(x - list_1[0])
for i in range(1, n):
    buffer_element = abs(x - list_1[i])
    if buffer_element < min_element:
        min_element = buffer_element
        index_element = i

print(
    f"Самый близкий по величине элемент к заданному числу {list_1[index_element]}")
