# Задача 2: 
# Найдите сумму цифр трехзначного числа.

num = int(input("введите число: "));num1 = num
sum = 0
while num != 0:
    d = num % 10
    sum+=d
    num = num // 10
print("сумма цифр",num1,"равна", sum)  
  
    