# Списки

# list1 = [1, 2, 3, 4, 5]
# list2 = list1

# for e in list1:
#     print(e, end = ' ')

# print()

# for e in list2:
#     print(e, end = ' ')

# print()

# list1[0] = 123
# list2[1] = 222

# for e in list1:
#     print(e, end = ' ')

# print()

# for e in list2:
#     print(e, end = ' ')

list = [1, 4, 8, 34, 2]

print(list.pop())           # Удаляет последний элемент
print(list)

print(list.pop(2))          # Удаляет эл с индексом 2
print(list)


print(list.insert(2, 11))   # Вставляет на позицию _ элемент _
print(list)


print(list.append(11))      # Добавляет элемент в конец
print(list)