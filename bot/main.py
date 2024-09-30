import os
import asyncio
import logging

from aiogram import Bot, types
from aiogram import Router
from aiogram.filters import Command 
from aiogram import Dispatcher
from aiogram.loggers import dispatcher
from dotenv import load_dotenv

from Handlers import router


# Загружаем переменные окружения
load_dotenv(dotenv_path="C:\\Users\\nikit\\PycharmProjects\\habit_tracker_bot\\.evn")

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("токен бота не найден. Проверьте файл .env")



bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def main():
    await bot.delete_webhook(drop_pending_updates=True)

    dp.include_router(router)  #маршрутизатор
    await dp.start_polling(bot)  # запрос к тг



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)#замедляет бота. отключить при выпуске
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Off')
