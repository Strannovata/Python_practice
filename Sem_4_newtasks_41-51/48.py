# 48. Найти корни квадратного уравнения Ax² + Bx + C = 0
# Математикой

# def quadEquation(a, b, c):
#     if a != 0 and b!= 0 and c!= 0:
#         D = b**2 - 4 * a * c
#         print(D)
#         if D < 0: print('Уравнение не имеет корней')
#         elif D == 0:
#             x = -b/(2*a)
#             print(f'x = {x}')
#         else:
#             x1 = (-b + D**0.5)/(2*a)
#             x2 = (-b - D**0.5)/(2*a)
#             print(f'x1 = {x1}, x2 = {x2}')
#     elif a != 0 and b == 0 and c == 0:
#         print('x = 0')
#     elif a != 0 and b == 0 and c != 0:
#         temp = - c / a
#         if temp < 0:
#             print('Уравнение не имеет корней')
#         elif temp > 0:
#             x1 = (-c / a)**0.5
#             x2 = -(-c / a)**0.5
#             print(f'x1 = {x1}, x2 = {x2}')   
#     elif a == 0 and b != 0:
#         x = -c / b
#         print(f'x = {x}')
    

       
# num1 = 0
# num2 = 2
# num3 = -3

# quadEquation(num1, num2, num3)

# Используя дополнительные библиотеки*

import math

def quadEquation(a, b, c):
    if a != 0 and b!= 0 and c!= 0:
        D = b**2 - 4 * a * c
        print(f'D = {D} sqr = {math.sqrt(D)}')
        if D < 0: print('Уравнение не имеет корней')
        elif D == 0:
            x = -b/(2*a)
            print(f'x = {x}')
        else:
            x1 = -b + math.sqrt(D)/(2*a)
            x2 = -b - math.sqrt(D)/(2*a)
            print(f'x1 = {x1}, x2 = {x2}')
    else:
        print('Уравнение не квадратное')

print('Введите коэффициенты уравнения Ax² + Bx + C = 0')
A = float(input('A = '))
B = float(input('B = '))
C = float(input('C = '))

quadEquation(A, B, C)
