import asyncio
import bot.KBoards as kb

from aiogram import Router, F, Bot
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from bot.DataBase import Registri
from datetime import datetime


router = Router()



@router.message(CommandStart())
async def send_welcome(message: Message):
    user_id = int(message.from_user.id)
    await Registri(user_id)
    await message.answer("привет! \n \n Мои команды:", reply_markup=kb.greet)


@router.message(Command("help"))
async def send_welcome(message: Message):
    await message.answer("прости, я пока ничего не умею(")


@router.callback_query(F.data == "Catalog")
async def Catal(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Catalog', reply_markup=await kb.catteft())


@router.callback_query(F.data == "new")
async def new(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('new')


@router.callback_query(F.data == "redact")
async def redact(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('redact')


@router.message(Command("SartTimer")) #функция хуета ебучая, вообще не останавливается
async  def StartTimer (message: Message):
    await message.answer('таймер запущен')
    ff=True
    while ff:
        x=0
        if x == 1:
            return 0
        else:
            await asyncio.sleep(10)
            await message.answer('##@##')
            x+=1


async def send_message_at_time(chat_id: int, time_str: str):
    while True:
        current_time = datetime.now().strftime('%H:%M')
        if current_time == time_str:
            print("лох")
            await asyncio.sleep(60)
        await asyncio.sleep(1)

@router.message(Command('StartTimeMes'))
async def start_schedule(message: Message):
    chat_id = message.chat.id
    await message.answer('кек')
    asyncio.create_task(send_message_at_time(chat_id,"23:59"))