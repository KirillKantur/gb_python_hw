# Задача 8:
# Требуется определить, можно ли от шоколадки размером n ×mk
# долек отломить
# долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).

height = int(input("введите количество долек по высоте"))
width = int(input("введите количество долек по ширине"))
slice = int(input("введите количество долек"))
if (height % slice == 0) or (width % slice == 0):
    print("Можно")
else:
    print("Нельзя")
