from lib2to3.pgen2.pgen import ParserGenerator
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from botcommands import *
import user_message

updater = Updater('5197070955:AAHTciErIui5xG8k_55-FSR7kH4Y82IZ3BY')

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('game', game_command))
updater.dispatcher.add_handler(MessageHandler(Filters.all, game_command))

print('server start')
updater.start_polling()
updater.idle()