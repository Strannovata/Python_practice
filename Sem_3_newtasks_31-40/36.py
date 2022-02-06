# 36. Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму

def GetSumList(n):
    list = []
    sum = 0
    for i in range(1, n+1):
        temp = (1 + 1 / i)**i
        list.append(temp)
        sum += temp
        i+=1
    print(list)
    return sum

print(GetSumList(7))