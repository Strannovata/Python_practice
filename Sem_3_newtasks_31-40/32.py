# 32. Для натурального N создать словарь индекс-значение, состоящий из элементов последовательности 3k + 1.

def GetDictionary(N):
    dict = {}
    for k in range(1,N+1):
        dict[k] = 3 * k + 1
    print(dict)

N = int(input('Введите число N>>> '))
GetDictionary(N)