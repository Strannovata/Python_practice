# 11.Дано число из отрезка [10, 99]. Показать наибольшую цифру числа

number = int(input('Введите число из отрезка [10, 99]>>> '))
num1 = number//10
num2 = number%10
if num1>num2:
    result = num1
else:
    result = num2
print(f'Наибольшая цифра числа = {result}')