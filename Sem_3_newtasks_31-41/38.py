# 38. Реализовать алгоритм перемешивания списка.

from random import randint

def ShakeList(list):
    index1 = len(list) -1
    while index1 >= 0:
        index2 = randint(0, len(list)-1)
        temp = list[index2]
        list.pop(index2)
        list.append(temp)
        index1 -=1
    return list

lst = [1, 2, 3, 4, 5, 6]
print(ShakeList(lst))