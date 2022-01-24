#27. Определить количество цифр в числе

def CountNumbers(A):
    count = 0
    while A > 0:
        A = A // 10
        count +=1
    return count
N = int(input('Введите число>>> '))
print(f'Количество цифр: {CountNumbers(N)}')