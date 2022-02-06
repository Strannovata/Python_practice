# 42. Найти сумму чисел списка стоящих на нечетной позиции

def sumOddPositionOfList(list):
    res = 0
    for i in range (0, len(list)):
        if i % 2 == 0:
            res += int(list[i])
            i += 1
    return res

lst = [1, 2, 3, 4, 5, 6, 7]
print(sumOddPositionOfList(lst))