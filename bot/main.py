import telebot
import config
bot = telebot.TeleBot(config.BOT_TOKEN, parse_mode="HTML")
# bot = telebot.TeleBot('5606512719:AAExW4UkCRF32XgXMh3xxW-CxxkTFXlG0qc')  
if __name__ == "__main__":

    from menu import send_to_admin
    send_to_admin()
