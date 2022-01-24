# 30.Показать кубы чисел, заканчивающихся на четную цифру

def OddToCube(list):
    for i in list:
        if i % 2 == 0:
            print(i**3)

value = [6, 23, 4, 8]
OddToCube(value)