from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Updater


def log(update: Update, context: CallbackContext):
    file = open('python_9/db.csv', 'a')
    file.write(f'{update.effective_user.first_name},{update.effective_user.id}, {update.message.text}\n')
    file.close()


def log(update: Update, context: CallbackContext):
    with open('logs.txt', 'a', encoding='utf-8') as file:
        file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')