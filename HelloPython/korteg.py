# Кортеж - неизменяемый список

# a = (3, 11, 4)  # a = (3,) - кортеж из 1 элемента
# print(a)
# print(a[-1])
# a[1] = 12  # элементы нельзя добавлять

t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{} g:{} b:{}'.format(red, green, blue))