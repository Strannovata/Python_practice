from random import randint

def playSweetsWithComputer(colsweets, ingive):
    player = 1
    plgive = 0
    while colsweets > ingive:
        if player == 1:
            plgive = int(input(f'Игрок {player} возьмите от 1 до {ingive} конфет>>> '))
            player = 2
        elif player == 2:
            plgive = randint(1, ingive)
            print(f'Бот берет {plgive} конфет')
            player = 1
        if plgive <= ingive:
            colsweets = colsweets - plgive
            print(f'Осталось конфет {colsweets}') 
        else:
            print('Вы взяли слишком много конфет! Это не честно, игра закончена')
            return  
    print(f'Игрок {player}, забирай последние {colsweets} конфет!')

print('Давайте сыграем в игру с конфетами! Игроки по очереди берут не больше оговоренного количества конфет. Победит тот, кому достанутся последние конфеты! Для начала установим правила:')
A = int(input('Сколько у вас всего конфет? >>> '))
B = int(input('Какое максимальное количество конфет будете брать за раз? >>> '))
playSweetsWithComputer(A, B)