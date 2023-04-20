# Задача 16: 
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
import random

rand_list=[]
n= int(input('введите количество элементов в масиве: '))
for i in range(n):
	rand_list.append(random.randint(0,9))
print(rand_list)


num = int(input('введите число для поиска: '))
count = 0
for i in range(len(rand_list)):
        if rand_list[i]==num:
            count +=1
print(f'количество совпадений',count)            

