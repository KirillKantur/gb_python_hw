# Задача 6: 
# Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета

num = int(input("введите шестизначный номер билета: "))
first_half = num//1000
second_half = num%1000
sum_num_first_half = 0
sum_num_second_half = 0
while first_half != 0:
    d = first_half % 10
    sum_num_first_half+=d
    first_half = first_half // 10
while second_half != 0:
    d = second_half % 10
    sum_num_second_half+=d
    second_half = second_half // 10    
if sum_num_first_half == sum_num_second_half:
    print("Билетик счастливый")
else:
    print("Билетик не счастливый")     
    