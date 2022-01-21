# 12. Удалить вторую цифру трёхзначного числа

number = int(input('Введите трехзначное число>> '))
num1 = number//100
num2 = number%10
result = num1*10+num2
print(result)

