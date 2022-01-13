import config
import telebot
import requests
import time
from bs4 import BeautifulSoup as bs

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




#
#     bot.send_message(message.chat.id, 'Надеюсь работает. \n Когда нфт появятся я пришлю тебе ссылку )')
#
#     while not main.check_box(1):
#         time.sleep(1)
#
#     else:
#         answer = 'YESSSSSSSSSSSSSS' + '\n' + \
#                  'https://kanaria.rmrk.app/catalogue?symbol=YLTD21&page=1&priceMax=1&sortBy=price'
#         bot.send_message(message.chat.id, answer)
#
bot.polling()



