from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Приветствуем Вас, {message.from_user.full_name}!",
                         reply_markup=kb.main)

@router.callback_query(F.data == "book")
async def book(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('Выберите действие')