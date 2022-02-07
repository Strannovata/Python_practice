# 59. Помните игру с конфетами из модуля "Математика и Информатика"? 

# Создайте такую игру для игры человек против человека

# def playSweets(colsweets, ingive):
#     player = 1
#     plgive = 0
#     while colsweets > ingive:
#         if player == 1:
#             plgive = int(input(f'Игрок {player} возьмите от 1 до {ingive} конфет>>> '))
#             player = 2
#         elif player == 2:
#             plgive = int(input(f'Игрок {player} возьмите от 1 до {ingive} конфет>>> '))
#             player = 1
#         if plgive <= ingive:
#             colsweets = colsweets - plgive
#             print(f'Осталось конфет {colsweets}') 
#         else:
#             print('Вы взяли слишком много конфет! Это не честно, игра закончена')
#             return  
#     print(f'Игрок {player}, забирай последние {colsweets} конфет!')

# playSweets(15, 5)


# Добавьте игру против бота

# from random import randint

# def playSweetsWithComputer(colsweets, ingive):
#     player = 1
#     plgive = 0
#     while colsweets > ingive:
#         if player == 1:
#             plgive = int(input(f'Игрок {player} возьмите от 1 до {ingive} конфет>>> '))
#             player = 2
#         elif player == 2:
#             plgive = randint(1, ingive)
#             print(f'Бот берет {plgive} конфет')
#             player = 1
#         if plgive <= ingive:
#             colsweets = colsweets - plgive
#             print(f'Осталось конфет {colsweets}') 
#         else:
#             print('Вы взяли слишком много конфет! Это не честно, игра закончена')
#             return  
#     print(f'Игрок {player}, забирай последние {colsweets} конфет!')

# playSweetsWithComputer(15, 5)


# Подумайте как наделить бота "интеллектом" 

# from random import randint

# def playSweetsWithComputer(colsweets, ingive):
#     player = 1
#     plgive = 0
#     while colsweets > ingive:
#         if player == 1:
#             plgive = int(input(f'Игрок {player} возьмите от 1 до {ingive} конфет>>> '))
#             player = 2
#         elif player == 2:
#             plgive = colsweets % (ingive + 1)
#             if plgive == 0:
#                 plgive = randint(1, ingive)
#             print(f'Бот берет {plgive} конфет')
#             player = 1
#         if plgive <= ingive:
#             colsweets = colsweets - plgive
#             print(f'Осталось конфет {colsweets}') 
#         else:
#             print('Вы взяли слишком много конфет! Это не честно, игра закончена')
#             return  
#     print(f'Игрок {player}, забирай последние {colsweets} конфет!')

# playSweetsWithComputer(15, 5)