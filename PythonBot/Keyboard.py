# -*- coding: utf-8 -*-
from telebot import types


def generate_markup(buttons):
    """
    Создаем кастомную клавиатуру из списка
    """
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for button in buttons:
        markup.add(button)
    return markup


def generate_markup_row(buttons):
    """
    Создаем кастомную клавиатуру для трех кнопок, расположенных в разных строках
    """
    markup = types.ReplyKeyboardMarkup()
    markup.row(buttons[0], buttons[1])
    markup.row(buttons[2])
