from telegram import Chat, Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from random import randint
import user_message


    
def hi_command(update: Update, context: CallbackContext):
    #log(update, context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}')

def help_command(update: Update, context: CallbackContext):
    #log(update, context)
    update.message.reply_text(f'Привет, я Strannovata_bot, и вот что я могу:\n/hi - эту команду пиши, чтобы поздороваться\n/game - сыграем в игру?')

def game_command(update: Update, context: CallbackContext):
    chat = update.effective_chat
    context.bot.send_message(chat_id = chat.id, text = 'Давайте сыграем в игру с конфетами! Игроки по очереди берут не больше оговоренного количества конфет. Победит тот, кому достанутся последние конфеты! Для начала установим правила:')
    context.bot.send_message(chat_id = chat.id, text ='Сколько у вас всего конфет?')
    msg = update.message.text
    colsweet = int(msg)
    context.bot.send_message(chat_id = chat.id, text ='Какое максимальное количество конфет будете брать за раз?')
    msg = update.message.text
    ingive = int(msg)
    context.bot.send_message(chat_id = chat.id, text =(f'Ок, всего {colsweet} конфет, и берем не более {ingive}'))
    player = 1
    plgive = 0
    while colsweets > ingive:
        if player == 1:
            plgive = int(input(f'Игрок {player} возьмите от 1 до {ingive} конфет>>> '))
            player = 2
        elif player == 2:
            plgive = colsweets % (ingive + 1)
            if plgive == 0:
                plgive = randint(1, ingive)
            update.message.reply_text(f'Бот берет {plgive} конфет')
            player = 1
        if plgive <= ingive:
            colsweets = colsweets - plgive
            update.message.reply_text(f'Осталось конфет {colsweets}') 
        else:
            update.message.reply_text(f'Вы взяли слишком много конфет! Это не честно, игра закончена')
    
    update.message.reply_text(f'Игрок {player}, забирай последние {colsweets} конфет!')


