# 52. Дана последовательность чисел. 
# Получить список неповторяющихся элементов исходной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

def uniqueElements(list):
    listUn = [list[0],]
    for i in range(0, len(list)):
        if list[i] not in listUn:
            listUn.append(list[i])
    return listUn


listdef = [1, 2, 3, 5, 1, 5, 3, 10, 2, 3, 5, 11]
uniq = uniqueElements(listdef)
print(uniq)
