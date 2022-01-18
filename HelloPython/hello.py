#print('hello, world')

#Типы данных и переменные
#int, float, boolean, str, list, None

#value = None
#print(type(value))
#a = 123
#b = 1.23
#print(a)
#print(type(a))
#print(b)
#print(type(b))
#value = 123456
#print(value)
#print(type(value))

#s = 'hello, world'
#print(s)  #вывод строки

#print(a, '-', b, '-', s)
#print('{} - {} - {}'.format(a, b, s))
#print(f'{a} - {b} - {s}')

#f = False
#print(f)

#list = [1, 2, 3]    #списки (массивы)
#col = ['1', '2', 4.5, 'hello']  #динамическая типизация позволяет миксовать данные разных типов, но так лучше не делать
#print(list) 
#print(col)


#Ввод и вывод данных
#print, input

#print('Введите a')
#a = input()
#print('Введите b')
#b = input()
#print(a, '+', b, '=', a+b)

#print('Введите a')
#a = float(input())    #или int
#print('Введите b')
#b = float(input())
#print(a, '+', b, '=', a+b)


#Арифметические операции
# +, -, *, /, %, //, **
# Приоритет операций: **, ун +, ун -, *, /, //, %, +, -
# (), Сокращенные операции

#a = 1.3
#b = 3
#c = round((a * b), 5)
#print(c)

#a = 3
#a += 5
#print(a)


#Логические операции
# >, >=, <, <=, ==, !=
# not, and, or не путать с &, |, ^
# is, is not, in, not in
# gen

#a = 1 < 4 and 5 > 2
#print(a)

#a = 'qwert'
#b = 'qwert'
#print(a == b)

#f = 1 < 4 or 3 > 5
#print(f)

#f = [1,2,3,4]
#print(f)
#print(2 in f)
#print(not 2 in f)

#is_odd = f[0] % 2 == 0
#print(is_odd)


#Управляющие конструкции
# if, if-else

#a = int(input('a = '))
#b = int(input('b = '))
#if a > b:
#    print(a)
#else:
#    print(b)


# elif

#username = input('Введите имя пользователя: ')
#if username == 'Nick':
#    print('Ура! Это же Nick!')
#elif username == 'Nasty':
#    print('Nasty, я - твой комп!')
#elif username == 'Polly':
#    print('Polly, ничего тут не трогай')
#else:
#    print('Hello, ', username)


# while

#original = 12345
#inverted = 0
#while original != 0:
#    inverted = inverted * 10 + (original % 10)
#    original //= 10
#print(inverted)

#original = 12345
#inverted = 0
#while original != 0:
#    inverted = inverted * 10 + (original % 10)
#    original //= 10
#    print(original)
#else:
#    print ('Пожалуй, хватит')
#print(inverted)


# for

#for i in 1,2,3,4,5:
#    print(i**2)

#list = [1,2,3,10,5]
#for i in list:
#    print(i)

#r = range(10)
#for i in r:
#    print(i)

#for i in range(4, 10, 2):  # в диапазоне от_ до_ с шагом_
#    print(i)

#for i in 'qwe - rty':
#    print(i)


#Немного о строках

#text = 'Котик и Лисичка кодят на Python'
#print(text[0])
#print(text[8])
#print(text[len(text)-1])
#print(text[8:15])


# Функции

#def f(x):
#    if x == 1:
#        return 'Целое'
#    elif x == 2.3:
#        return 23
#    else:
#        return

#arg = 7
#print(f(arg))
#print(type(f(arg)))