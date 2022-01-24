#19. Определить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0

def QuarterSearch(x, y):
    if (x > 0) and (y > 0):
        quarter = 1
    elif (x < 0) and (y > 0):
        quarter = 2
    elif (x < 0) and (y < 0):
        quarter = 3
    elif (x > 0) and (y < 0):
        quarter = 4
    return quarter

x = int(input('Введите координату X>>> '))
y = int(input('Введите координату Y>>> '))
print(f'Номер четверти >>> {QuarterSearch(x, y)}')