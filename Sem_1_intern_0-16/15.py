#15. Дано число. Проверить кратно ли оно 7 и 23

number = int(input('Введите число>>> '))
if number % 7 == 0:
    print(f'Число {number} кратно 7')
else:
    print(f'Число {number} не кратно 7')
if number % 23 == 0:
    print(f'Число {number} кратно 23')
else:
    print(f'Число {number} не кратно 23')