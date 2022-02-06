# 40. Определить, присутствует ли в заданном списке строк, некоторое число 

lst = ['a18', '7ud', '567', '8hf', '865']
num = '7'

def foundNumber(list, found):
    count = 0
    for i in list:
        str = i
        for j in str:
            if j == found:
                count +=1
    if count > 0:
        print(f'Число {found} присутствует {count} раз(а)')
    else:
        print(f'Число не присутствует')

foundNumber(lst, num)