# 13.Выяснить, кратно ли число заданному, если нет, вывести остаток.

a = int(input('Задайте число (делитель)>>> '))
b = int(input('Введите число, которое будем проверять на кратность заданному>>> '))
ost = b % a
if ost == 0:
    print(f'Число {b} кратно {a}')
else:
    print(f'Число {b} не кратно {a}. Остаток = {ost}')