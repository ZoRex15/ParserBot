from aiogram.types import User
from service.service import Database


async def get_settings(event_from_user: User, **kwargs):
    return Database.get_all_filters(user_id=event_from_user.id, mode='name')