# 43. Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

def multipleOfPair(list):
    result = []
    N = len(list)-1
    K = len(list)
    if K % 2 != 0:
        K = K // 2 + 1
    else:
        K = K // 2
    for i in range (0, K):
        elem = list[i] * list[N]
        N -= 1
        i +=1
        result.append(elem)
    return result


lstdefolt = [1, 2, 3]
lstmult = multipleOfPair(lstdefolt)
print(lstmult)
