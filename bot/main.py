import os
import asyncio
import logging
from aiogram import Bot, types
from aiogram import Router
from aiogram.filters import Command
from aiogram import Dispatcher
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    raise ValueError("Токен бота не найден. Проверьте файл .env")


bot = Bot(token=BOT_TOKEN)
router = Router()


@router.message(Command('start'))
async def send_welcome(message: types.Message):
    await message.answer("привет!")


async def main():
    await bot.delete_webhook(drop_pending_updates=True)

    # Инициализация диспетчера и добавление маршрутизатора
    dp = Dispatcher()
    dp.include_router(router)

    # запрос к тг
    await dp.start_polling(bot)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)#замедляет бота. отключить при выпуске
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Off')
