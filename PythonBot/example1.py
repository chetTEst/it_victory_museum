# -*- coding: utf-8 -*-
# Установка библиотеки командой pip install pytelegrambotapi
# Бот автоответчик

import telebot
import config

bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    print(message)
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()