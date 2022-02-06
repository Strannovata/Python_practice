# 39. Реализовать алгоритм задания случайных чисел. 
# Без использования встроенного генератора псевдослучайных чисел

def randomNumber(N):
    list = []
    list2 = []
    for i in range(-N, N+1):
        list.append(i)
    for j in list:
        k = (j**2 - 4*j - 3*j)
        list2.append(j+k)
    return list2
       
print(randomNumber(99))