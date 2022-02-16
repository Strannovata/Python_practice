# 50. Вычислить число ПИ c заданной точностью d
# Пример: при d = 0.001, π = 3.141. 10**-1≤ d ≤10**-10

from itertools import count
import math

def Pi(d):
    temp = d.split('.')
    print(temp)
    colelem = temp[1]
    count = 0
    for i in colelem:
        count +=1
    result = round(math.pi, count)
    return result

d = '0.000001'
print(Pi(d))