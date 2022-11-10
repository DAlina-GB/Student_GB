import os
import sys

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

from bot_commands import *
import strings as st


BOT_TOKEN_FILENAME = 'token.txt'

def getToken():
    token = '5415981853:AAE4UXhwdqxW8_8vHn5DFIkjiMgxv78uiNw'
    if os.path.isfile(st.BOT_TOKEN_FILENAME):
        f = open(st.BOT_TOKEN_FILENAME, "r")
        token = f.read()
        f.close()
    else:
        print("Пожалуйста, создайте в папке проекта файл 'token.txt' и поместите туда токен для работы телеграм бота  и запустите скрипт заново")
        sys.exit()  # завершить работу скрипта
    return token

def help_command(update, _):
    update.message.reply_text(st.ANSW_HELP)


if __name__ == '__main__':
    updater = Updater(getToken())  # получения токена из файла 'token.txt' и инициализация updater

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
updater.dispatcher.add_handler(CommandHandler('w_d', w_d_command))
updater.dispatcher.add_handler(CommandHandler('ran', ran_command))
updater.dispatcher.add_handler(CommandHandler('calc', calc_command))
updater.dispatcher.add_handler(CommandHandler('tictac', newGame))
updater.dispatcher.add_handler(CommandHandler('new_game', newGame))
updater.dispatcher.add_handler(MessageHandler(Filters.text, help_command))  # обработчик на любое текстовое сообщение
updater.dispatcher.add_handler(CallbackQueryHandler(button))  # добавление обработчика на CallBack кнопки


print('server start')
updater.start_polling()
updater.idle()
