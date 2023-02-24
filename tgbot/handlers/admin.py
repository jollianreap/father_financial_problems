from datetime import date

from tgbot.models.tables import Sharik_trouble
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.state import State
from aiogram.types import Message
from tgbot.models.database import Database
from tgbot.filters.admin import AdminFilter
from loader import db # i took out db from this handler, because maybe i wll user this one in onther handler
                      # and for avoiding circular imports I created new file: loader.py
from tgbot.keyboards.reply import builder_markup
from aiogram.filters import Text


admin_router = Router()
admin_router.message.filter(AdminFilter()) # it checks user status

last_id = db.get_id_or_debt()  # here i get last id for pruning down adding a new debt
last_debt = db.get_id_or_debt(last_id)[0]  # and here i get last debt with last id


@admin_router.message(CommandStart())
async def admin_start(message: Message):
    reply_markup = builder_markup() # it creates a new keyboard
    await message.reply("Добро пожаловать в долговую яму Шарика\n"
                        "Шарик не меняется? Все так же десяточка накидывается??",
                        reply_markup=reply_markup.as_markup(resize_keyboard=True)) # resize_keyboard needs to show correct size of buttons


@admin_router.message(Text(text="Да")) # Text() is a filter which filter by text, i guess, it`s clear
async def debt_without_changes(message: Message):

    data = {
            "id": last_id +1, # here i plus id to avoid error with same ids
            "debt": last_debt + 10000, # usually nothing changes so i just increase on 10 thousand
            "date": date.today() # this moment i should remake because it`s not conviment to write date every time
            }

    db.add_unique_record(data, Sharik_trouble, "id") # check this method in database.py
    await message.reply("Ок, щас занесем в книжечку")


@admin_router.message(Text(text="Нет")) # here i offer user to change amount of debt
async def debt_with_changes(message: Message):

    await message.reply("Введите новое число долга: ")


@admin_router.message()
async def change_debt_amount(message: Message):
    await message.reply(f"{message.text}, щас добавлю")
    data = {
        "id": last_id + 1,
        "debt": last_debt + int(message.text),
        "date": date.today()
    }
    # here i texture new dict of data which i will add to db
    db.add_unique_record(data, Sharik_trouble, "id")


