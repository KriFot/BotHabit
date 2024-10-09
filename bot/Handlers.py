import asyncio
import bot.KBoards as kb

from aiogram import Router, F, Bot
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from bot.DataBase import Registri



router = Router()



@router.message(CommandStart())
async def send_welcome(message: Message):
    user_id = int(message.from_user.id)
    await Registri(user_id)
    await message.answer("привет! \n \n Мои команды:", reply_markup=kb.greet)


@router.message(Command("help"))
async def send_welcome(message: Message):
    await message.answer("прости, я пока ничего не умею(")


@router.message(Command("SartTimer")) #функция хуета ебучая, вообще не останавливается
async  def StartTimer (message: Message):
    await message.answer('таймер запущен')
    while True:
        await asyncio.sleep(10)  # Ждем 10 секунд
        await message.answer("Это сообщение отправляется каждые 10 секунд.")


@router.message(Command('StartTimeMes'))
async def start_schedule(message: Message):
    from basic import send_message_at_time
    chat_id = message.chat.id
    await message.answer('1')
    asyncio.create_task(send_message_at_time(chat_id,"22:09"))


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