# 45. Написать программу преобразования десятичного числа в двоичное

def transformToBinary(number):
    temp = 0
    listremaind = []
    while number > 0:
        temp = number % 2
        listremaind.append(temp)
        number = number // 2
    binary = []
    N = len(listremaind) - 1
    while N >=0:
        B = listremaind[N]
        binary.append(B)
        N -= 1
    return binary


lst = transformToBinary(18)
print(lst)
