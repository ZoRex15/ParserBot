from aiogram.types import User

from tg_bot.service import Database

from aiogram_dialog import DialogManager


async def get_settings(event_from_user: User, dialog_manager: DialogManager, **kwargs):
    db: Database = dialog_manager.middleware_data.get('db')
    return db.get_all_filters(user_id=event_from_user.id, mode='name')