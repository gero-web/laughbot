from aiogram import types
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup


def InlineKeyBoardBuilder(data):
    buttons = InlineKeyboardMarkup()
    for text, callback_data in data:
        buttons.add(InlineKeyboardButton( text, callback_data=callback_data))
    return buttons