#25. Найти сумму чисел от 1 до А

A = int(input('Введите A>>> '))
result = 0
for i in range(1, A + 1):
    result += i
    print(f'+ {i}', end = " ")
    i += 1
print(f'= {result}')
