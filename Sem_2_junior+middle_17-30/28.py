#28. Подсчитать сумму цифр в числе

def SumNumbers(number):
    num = str(number)
    result = 0
    for i in num:
        result += int(i)
    return result
N = input('Введите число>>> ')
print(f'Сумма цифр: {SumNumbers(N)}')