# 33. Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

def numberOfOccurrences(string1, string2):
    text = ' '
    count = 0
    u = 0
    while u < len(string2):
        for i in string1:
            for j in string2:
                if i == j:
                    count += 1
                    # text += i
        u +=1
    return (count // u) // u
   
s1 = input("Введите строку>>> ")
s2 = input("Введите искомую часть>>> ")
print(numberOfOccurrences(s1, s2))