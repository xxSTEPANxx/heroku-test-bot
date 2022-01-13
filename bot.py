import config
import telebot

import test

from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["start"])
def handle_start(message):
    # print(message)
    markup = ReplyKeyboardMarkup()
    markup.add(KeyboardButton("get_lowest_price"))
    markup.add(KeyboardButton("start_notify"))
    bot.send_message(message.chat.id, 'hi', reply_markup= markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == 'get_lowest_price':
        answer = test.get_lowerst()
        bot.send_message(message.chat.id, answer[0])
        bot.send_message(message.chat.id, answer[1])
    if message.text == 'start_notify':
        answer = test.start_notify()
        bot.send_message(message.chat.id, answer[0])
        bot.send_message(message.chat.id, answer[1])

bot.polling()



