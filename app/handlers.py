# handlers.py

from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import F, Router
import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет.\nТвой ID: {message.from_user.id}\nТвое имя: {message.from_user.full_name}',
                        reply_markup=kb.settings)

@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Это команда /help')

@router.message(F.text == 'Как дела?')
async def how_are_you(message: Message):
    await message.answer('В полном порядке!')

@router.message(Command('get_photo'))
async def get_photo(message: Message):
    await message.answer_photo(photo='https://static-cse.canva.com/blob/847132/paulskorupskas7KLaxLbSXAunsplash2.jpg',
                               caption='Это фото')

@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')
