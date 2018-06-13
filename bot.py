import logging
from telegram.ext import Updater, CommandHandler

updater = Updater(token='559899786:AAF0icPrHjiA0WZ3-GR4SmnAD-htwYqkHZo')

dispatcher = updater.dispatcher

def start(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)

updater.start_polling()
