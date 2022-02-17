from lib2to3.pgen2.pgen import ParserGenerator
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from botcommands import *


# def on_message(update: Update, context: CallbackContext):
#     chat = update.effective_chat
#     #text = update.message.text
#     # try:
#     #     number = float(text)
#     #     update.message.reply_text(number)
#     # except:
#     context.bot.send_message(chat_id = chat.id, text = 'Omg')

