# # Задача 14:
# # Требуется вывести все целые 
# степени двойки (т.е. числа вида 2^k),
# # не превосходящие числа N.

num = int(input('введите число'))
stepen = 0
while 2**stepen < num:
    print(2**stepen)
    stepen += 1
