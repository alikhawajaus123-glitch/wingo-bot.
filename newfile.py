import telebot
import os

# Yahan apna API Token dalein
API_TOKEN = '1000527315:AAH...' 
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Bot chal raha hai!")

if __name__ == '__main__':
    bot.infinity_polling()
