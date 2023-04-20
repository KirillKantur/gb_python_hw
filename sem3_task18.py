# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X .
# Если таких значений больше одного, вывести первый найденный.

import random
rand_list = []
n = int(input('введите количество элементов в масиве: '))
for i in range(n):
	rand_list.append(random.randint(0, 9))
print(rand_list)

num = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
min = abs(num - rand_list[0])
index = 0
for i in range(1, n):
        count = abs(num - rand_list[i])
        if count < min:
            min = count
            index = i
print(f'Число {rand_list[index]} в списке rand_list наиболее близко по величине к числу {num}')