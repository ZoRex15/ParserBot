from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from tg_bot.service.service import Database

import sqlite3


class DatabaseMiddleware(BaseMiddleware):
    def __init__(self, db: str) -> None:
        self.db = db
        

    async def __call__(self, 
                       handler: Callable[[TelegramObject, Dict[str, Any]], 
                       Awaitable[Any]], 
                       event: TelegramObject, 
                       data: Dict[str, Any]
    ) -> Any:
        with sqlite3.connect(self.db) as session:
            db = Database(session=session)
            data['db'] = db
            result = await handler(event, data)
            return result