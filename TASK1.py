#Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random
n = int(input("Введите число элементов в массиве: "))
list_1=[]
for i in range (n):
    from random import randint
    list_1.append(random.randint(0, n))
print(list_1)
x = int(input("Введите искомое число: "))

count = 0
for i in range (len(list_1)):
    if list_1[i] == x:
        count = count+1
    i = i+1
print(count)