# 44. В заданном списке вещественных чисел найдите разницу между 
# максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math    

def getListFract(list):
    fract = []
    for i in list:
        c = math.floor(i)
        f = round((i - c), 3)
        fract.append(f)
    return fract

lstDefolt = [1.3, 1.6, 3.1, 5, 10.01]
lstFract = getListFract(lstDefolt)

def diffMaxMin(list):
    min = list[0]
    max = list[0]
    for i in list:
        if (i != 0 and i < min):
            min = i
        if (i != 0 and i > max):
            max = i
    return (max - min)

print(diffMaxMin(lstFract))




                        


