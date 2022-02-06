# 46. Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов

def Fib(N):
    listpos = [0, 1]
    listneg = [0, 1]
    for i in range (2, N+1):
        fib = int(listpos[i-2] + listpos[i-1])
        listpos.append(fib)
    for j in range (2, N+1):
        neg = float(listneg[j-2] - listneg[j-1])
        listneg.append(neg)
    result = []
    N = len(listneg) - 1
    while N >=0:
        temp = listneg[N]
        result.append(temp)
        N -= 1
    return result + listpos
    

lst = Fib(10)
print(lst)