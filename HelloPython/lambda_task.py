# В файле хранятся числа, нужно выбрать четные и составить список пар (число, квадрат числа)
# Пример: 1 2 3 5 8 15 23 38 -->  [(2,4), (8, 64), (38, 1444)]

path = 'listOfnumber.txt'
f = open(path, 'r')
data = f.read() + ' '
f.close()

numbers = data.split()

res = map(int, numbers)
res = filter(lambda x: not x % 2, res)
res = list(map(lambda x:(x, x**2), res))
print(res)
