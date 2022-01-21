# 9.Показать последнюю цифру трёхзначного числа

number = int(input('Введите трехзначное число>>> '))
if number < 0:
    number = number*-1
result = number % 10
print(result)
