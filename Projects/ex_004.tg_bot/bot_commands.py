from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy import *

def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}')

def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Привет, я Strannovata_bot, и вот что я могу:\n/hi - эту команду пиши, чтобы поздороваться\n/time - так можно узнать точное время\n/sum - можно сложить два числа, для этого нужно написать: /sum число число (через пробел)\n/help')

def time_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'{datetime.datetime.now().time()}')

def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    #print(msg)
    items = msg.split() # /sum 123 6799
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x + y}')
