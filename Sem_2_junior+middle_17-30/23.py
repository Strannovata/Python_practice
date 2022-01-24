#23. Показать таблицу квадратов чисел от 1 до N

N = int(input('Введите N>>> '))

for i in range(1, N+1):
    result = i**2
    print(f'{i}^2 = {result}')
    i +=1
