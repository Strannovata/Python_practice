# 34. Подсчитать сумму цифр в вещественном числе

def SumNumbers(number):
    num = str(number)
    result = 0
    for i in num:
        if i != '-' and i !='.':
            result += int(i)
    return result
N = input('Введите число>>> ')
print(f'Сумма цифр: {SumNumbers(N)}')