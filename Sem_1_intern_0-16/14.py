# 14.Найти третью цифру числа или сообщить, что её нет (я ищу третью с начала)

num = int(input('Введите число>>> '))
if num < 0:
    num = num * -1
if num < 100:
    print('Третьей цифры нет')
else:
    numbers = str(num)
    print(numbers[2])
