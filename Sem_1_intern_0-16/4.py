# 4.Найти максимальное из трех чисел

a = int(input('Введите первое число>> '))
b = int(input('Введите второе число>> '))
d = int(input('Введите третье число>> '))
if b<a>d:
    max = a
elif a<b>d:
    max = b
else:
    max = d
print(f'Максимальное число = {max}')