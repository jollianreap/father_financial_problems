from aiogram.filters import BaseFilter
from aiogram.types import Message

from tgbot.config import Config


class NonAdminFilter(BaseFilter):
    is_admin: bool = False # I added this filter for new users who aren`t admins,
                           # so I just head them to user handler where I get id and update list of admins

    async def __call__(self, obj: Message, config: Config) -> bool:
        return (obj.from_user.id in config.tg_bot.admin_ids) == self.is_admin