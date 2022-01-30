# 31. Для натурального N создать множество: 1, -3, 9, -27, 81 и т.д.

def GetSet(N):
    set = {1}
    temp = 1
    for i in range(1,N):
        temp *= -3
        set.add(temp)
    return set

#print(GetSet(10))

list = GetSet(10)
print(list)
