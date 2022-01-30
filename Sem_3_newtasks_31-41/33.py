# 33. Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

def numberOfOccurrences(string1, string2):
    text = str(string2)
    count = 0
    i = 0
    while i < len(string1):
        if text in string1:
            count += 1
        i +=1
    return count

s1 = input("Введите строку>>> ")
s2 = input("Введите искомую часть>>> ")
print(numberOfOccurrences(s1, s2))