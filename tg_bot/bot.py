from aiogram import Bot, Dispatcher
import asyncio
from config import Config, load_config
from aiogram.fsm.storage.redis import RedisStorage, Redis, DefaultKeyBuilder
from aiogram.fsm.storage.memory import SimpleEventIsolation
from aiogram_dialog import setup_dialogs
from dialogs import (main_menu,
                    start,
                    start_router,
                    settings_router)


async def main():
    config: Config = load_config()
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    redis: Redis = Redis(host='localhost')
    storage: RedisStorage = RedisStorage(redis, key_builder=DefaultKeyBuilder(with_destiny=True))
    dp = Dispatcher(storage=storage, events_isolation=SimpleEventIsolation())
    dp.include_router(start_router)
    dp.include_router(start)
    dp.include_router(main_menu)
    dp.include_router(settings_router)
    setup_dialogs(dp)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())