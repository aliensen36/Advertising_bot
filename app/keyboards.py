from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Записаться')],
    [KeyboardButton(text='Перенести')],
    [KeyboardButton(text='Отменить')],
], resize_keyboard=True, input_field_placeholder='Выберите действие')

aux = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Записаться', callback_data='book')],
    [InlineKeyboardButton(text='Перенести', callback_data='change')],
    [InlineKeyboardButton(text='Отменить', callback_data='cancel')],
])