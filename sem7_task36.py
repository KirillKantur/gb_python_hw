# Задача 36: 
# На вход программы поступает строка в формате:
# ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
# Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
# tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))
# Выводить на экран ничего не нужно, только преобразовать строку в кортеж с именем tp.
# Sample Input:
# 'house=дом car=машина men=человек tree=дерево'
# Sample Output:
# (('house', 'дом'), ('car','машина'), ('men', 'человек'), ('tree', 'дерево'))


str_1 ='house=дом car=машина men=человек tree=дерево'
str = str_1.split()
d = {}
d.update( list( map( lambda x: tuple( x.split('=') ), str ) ) )
print( *sorted( d.items() ) )
