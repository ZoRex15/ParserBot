import aio_pika
import asyncio
from aiogram import Bot
from tg_bot.config.config import Config, load_config


config: Config = load_config('tg_bot/.env')
print(config.tg_bot.token)
        
async def main():
    bot = Bot(config.tg_bot.token)
    connect = await aio_pika.connect_robust(host='localhost')
    queue_name = 'requests'
    async with connect:
        channel = await connect.channel()
        await channel.set_qos(prefetch_count=10)
        queue = await channel.declare_queue(queue_name, durable=True)
        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                   
                    chat_id, message_id, text = map(str, message.body.decode().split(':'))
                    await bot.edit_message_text(
                        chat_id=chat_id,
                        message_id=int(message_id),
                        text=text
                    )
                    

if __name__ == '__main__':
    asyncio.run(main())
