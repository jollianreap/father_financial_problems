from aiogram import Router
from aiogram.types import Message
from tgbot.filters.non_admin import NonAdminFilter
from aiogram.filters import CommandStart
from tgbot.keyboards.reply import builder_markup
from aiogram.filters import Text


user_router = Router()
user_router.message.filter(NonAdminFilter())


@user_router.message(CommandStart())
async def start_user(message: Message):
    await message.reply("Добрый день!"
                        "Вы хотите стать вершителем судьбы Шарика?", reply_markup=builder_markup().as_markup(resize_keyboard=True))
    print(message.from_user.id)


@user_router.message(Text(text="Да"))
async def adding(message: Message):
    # config.tg_bot.admin_ids.append(message.from_user.id)
    await message.reply("Ага")