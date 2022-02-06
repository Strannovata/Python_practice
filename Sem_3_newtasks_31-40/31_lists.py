# 31. Для натурального N создать список: 1, -3, 9, -27, 81 и т.д.

def GetList(N):
    list = [1]
    temp = 1
    for i in range(1,N):
        temp *= -3
        list.append(temp)
    return list

print(GetList(10))