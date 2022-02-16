# 51. Составить список простых множителей натурального числа N

def listOfPrimeNum(N):
    prime = []
    list = []
    for num in range (2, N):
        while N % num == 0:
            list.append(num)
            N = N / num
        num += 1
    return list



print(listOfPrimeNum(355))
