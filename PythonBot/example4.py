# -*- coding: utf-8 -*-
# Установка библиотеки командой pip install pytelegrambotapi
# Отправка файлов

import telebot
import config

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def send(message): # Название функции не играет никакой роли
    FILEID = "AgACAgIAAxkDAAMgYh8ZTedgcaG73X2-opUxT7PN_egAAq25MRt45PhIuVUbbL3Z6LwBAAMCAANzAAMjBA"
    chat_id = message.chat.id
    photo = open('bot.png', 'rb')
    msg = bot.send_photo(chat_id, photo)
    print(msg.photo[0].file_id)


if __name__ == '__main__':
    bot.infinity_polling()
