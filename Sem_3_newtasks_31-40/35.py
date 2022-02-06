#35. Написать программу получающую набор произведений чисел от 1 до N.
#Пример: пусть N = 4, тогда
#[ 1, 2, 6, 24 ]

def SetOfMultiple(N):
    list = [1]
    temp = 1
    k = 2
    for i in range (1, N):
        temp *= k
        list.append(temp)
        k += 1
    return list

print(SetOfMultiple(6))
