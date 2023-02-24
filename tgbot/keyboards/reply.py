from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.filters import Text
from aiogram import types


def builder_markup():
    builder = ReplyKeyboardBuilder()

    builder.row(
        types.KeyboardButton(text="Да"),
        types.KeyboardButton(text="Нет")
        )

    return builder

