# 49. Найти НОК двух чисел

def nok(a,b):
    for x in range(1, (a*b)+1):
        if x % a == 0 and x % b == 0:
            return x
        

print(nok(12, 49))

# a = 12
# b = 49

# nok = list((a, b, x) for x in range(1, lambda a, b: (a*b) + 1) if (x % a == 0) and (x % b == 0))
# print(nok)