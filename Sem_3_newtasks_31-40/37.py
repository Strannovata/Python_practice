# 37. Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

from random import randint

def GetList(N):
    list = []
    temp = 0
    for i in range(0,N):
        temp = randint(-N, N)
        list.append(temp)
    return list

lst = GetList(5)
print(lst)

def MultiplePosition(list):
    res = 1
    path = 'posOfElements.txt'
    data = open(path, 'r')
    for i in range(0, len(list)):
        for line in data:
            i = int(line)  
            temp = list[i]
            print(f'позиция элемента>>> {i} || элемент>>> {temp}') 
            res *= temp
    return res
    data.close()

           
print(f'Произведение элементов >>> {MultiplePosition(lst)}')