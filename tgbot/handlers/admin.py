from tgbot.models.tables import Sharik_trouble
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.state import State
from aiogram.types import Message
from tgbot.models.database import Database
from tgbot.filters.admin import AdminFilter

db = Database("sqlite:///tgbot/models/debts.sqlite") # I wrote this here because it`d be better than write database and create files every time
admin_router = Router()
admin_router.message.filter(AdminFilter())


@admin_router.message(CommandStart())
async def admin_start(message: Message):
    await message.reply("Добро пожаловать в долговую яму Шарика\n"
                        "Шарик не меняется? Все так же десяточка накидывается??")


@admin_router.message()
async def debt_update(message: Message):
    await message.reply("Ок, щас занесем в книжечку")
    last_id = db.get_id_or_debt() # here i get last id for pruning down adding a new debt
    last_debt = db.get_id_or_debt(last_id)[0] # and here i get last debt with last id
    data = {
            "id": last_id +1, # here i plus id to avoid error with same ids
            "debt": last_debt + 10000, # usually nothing changes so i just increase on 10 thousand
            "date": "25-05-23" # this moment i should remake because it`s not conviment to write date every time
            }

    db.add_unique_record(data, Sharik_trouble, "id")
    await message.reply(f"Ойойоойоййоой а должок то растет уже {db.get_id_or_debt(last_id)[0]}")