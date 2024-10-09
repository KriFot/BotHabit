import os
import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher
from dotenv import load_dotenv
from Handlers import router
from datetime import datetime

#
load_dotenv(dotenv_path="C:\\Users\\nikit\\PycharmProjects\\habit_tracker_bot\\.evn")
#присвоение значения токена
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("токен бота не найден. Проверьте файл .env")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


#
async def set_bot_description():
    description_text = ("Я бот для отслеживания привычек. Нажав /start, вы соглашаетесь с обработкой персональных данных. \n \n Для начала нажмите /start.")
    await bot.set_my_description(description_text)


async def send_message_at_time(chat_id: int, time_str: str):
    while True:
        current_time = datetime.now().strftime('%H:%M')
        if current_time == time_str:
            print("2")
            await asyncio.sleep(60)
        await asyncio.sleep(1)


#basic func
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await set_bot_description()
    dp.include_router(router)  #маршрутизатор
    await dp.start_polling(bot)  # запрос к тг