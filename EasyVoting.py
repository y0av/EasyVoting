from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram.ext import MessageHandler, Filters
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

custom_keyboard = [['set new poll', 'top-right'], ['bottom-left', 'bottom-right']]
reply_markup = ReplyKeyboardMarkup(custom_keyboard)
def start(bot, update):
	bot.send_message(chat_id=update.message.chat_id,
					 text="Howdy there!",
					 reply_markup=reply_markup)
start_handler = CommandHandler('start', start)


def ask(bot, update):
	keyboard = [[InlineKeyboardButton("Option 1", callback_data='1'),
				 InlineKeyboardButton("Option 2", callback_data='2')],
				[InlineKeyboardButton("Option 3", callback_data='3')]]
	reply_markup = InlineKeyboardMarkup(keyboard)
	update.message.reply_text('Please choose:', reply_markup=reply_markup)

def button(bot, update):
    query = update.callback_query
    bot.edit_message_text(text="Selected option: {}".format(query.data),
                          chat_id=query.message.chat_id,
	message_id=query.message.message_id)



def unknown(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")
unknown_handler = MessageHandler(Filters.command, unknown)



def main():
    """Run bot."""
    updater = Updater("662413436:AAE2zkyXQPvVisLnaP17lH0UbXnbe62bFFs")


    dispatcher = updater.dispatcher



    #dispatcher.add_handler(start_handler)
    #dispatcher.add_handler(unknown_handler)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('ask', ask))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()