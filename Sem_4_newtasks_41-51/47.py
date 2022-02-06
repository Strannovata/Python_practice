# 47. Строка содержит набор чисел. Показать большее и меньшее число

def findMaxMin(string):
    max = 0
    min = 9
    for i in string:
        num = int(i)
        if num > max:
            max = num
        if num <= min:
            min = num
    return max, min
      

str = '1654335'
print(findMaxMin(str))
