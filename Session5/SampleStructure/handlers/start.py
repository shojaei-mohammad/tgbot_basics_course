from aiogram import Router
from aiogram.filters import CommandStart

router = Router()


@router.message(CommandStart())
async def process_start(message):
    await message.answer("سلام\n\n خوش آمدید!")


@router.message()
async def echo(message):
    await message.answer(message.text)
