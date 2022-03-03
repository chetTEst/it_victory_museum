# -*- coding: utf-8 -*-
# Установка библиотеки командой pip install pytelegrambotapi
# Клавиатура для бота

import telebot
import config

bot = telebot.TeleBot(config.token)
from Keyboard import generate_markup


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # Название функции не играет никакой роли
    markup = generate_markup(["Кнопка 1", "Кнопка 2", "Кнопка 3", "Кнопка 4"])
    bot.send_message(message.chat.id, message.text, reply_markup=markup)


if __name__ == '__main__':
    bot.infinity_polling()
