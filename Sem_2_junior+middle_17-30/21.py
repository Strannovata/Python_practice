#21. Программа проверяет пятизначное число на палиндром.

def IsPalindrome (number):
    if number[0] == number[4] and number[1] == number[3]:
        print(f'{number} is palindrome')
    else:
        print(f'{number} is not palindrome')

IsPalindrome(input('Введите 5-изначное число>>>' ))
