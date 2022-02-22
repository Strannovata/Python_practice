# 55. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

def FindMissing(list):
    for i in range(0, len(list)):
        if list[i+1] != list[i] + 1:
            return list[i] + 1

path = 'Missingnumber.txt'
data = open(path, 'r')
for line in data:
    string = line
    listsym = string.split()
data.close()


listnum = []
for i in listsym:
    res = int(i)
    listnum.append(res)


print(listnum)
print(FindMissing(listnum))