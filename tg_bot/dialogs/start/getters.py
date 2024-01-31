from aiogram.types import User


async def get_user_name(event_from_user: User, **kwargs):
    return {'name': event_from_user.first_name}

