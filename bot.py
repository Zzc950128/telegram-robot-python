import logging
from telegram.ext import Updater, CommandHandler

updater = Updater(token='617336269:AAGAAmLZFsJ1fgSS9FvgKtXDbXvb8sYiLWs')

dispatcher = updater.dispatcher

def start(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)

updater.start_polling()
