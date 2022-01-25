# Множества

# colors = {'red', 'green', 'blue'}
# print(type(colors))  
# print(colors)
# colors.add('red')       # добавление элементов. не добавит если есть
# print(colors)
# colors.add('gray')      # добавление
# print(colors)
# colors.remove('red')    # удаление (если элемента нет - ошибка)
# print(colors)
# colors.discard('red')   # позволяет удалять несуществующие элементы
# print(colors)
# colors.clear            # очистка множества
# print(colors)

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()            # копирование
print(c)
u = a.union(b)          # объединение
print(u)    
i = a.intersection(b)   # пересечение
print(i)     
dl = a.difference(b)    # отрицание b
print(dl)
dr = b.difference(a)    # отрицание a
print(dr) 

s = frozenset(a)        # неизменяемое множество