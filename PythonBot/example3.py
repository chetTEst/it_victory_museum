# -*- coding: utf-8 -*-
# Установка библиотеки командой pip install pytelegrambotapi
# Команды для бота

import telebot
import config

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start', 'starts'])
def start(message):
    bot.send_message(message.chat.id, 'Команда старт активирована')


if __name__ == '__main__':
    bot.infinity_polling()
