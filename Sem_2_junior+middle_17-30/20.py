#20.Задать номер четверти, показать диапазоны для возможных координат

quarter = int(input('Введите номер четверти>>> '))
if quarter == 1:
    print(f'x > 0, y > 0')
elif quarter == 2:
    print(f'x < 0, y > 0')
elif quarter == 3:
    print(f'x < 0, y < 0')
elif quarter == 4:
    print(f'x > 0, y < 0')
else:
    print('Неверно указан номер четверти')