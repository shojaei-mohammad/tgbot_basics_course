from aiogram import Router
from aiogram.types import Message


other_router = Router()


@other_router.message()
async def echo(message: Message):
    await message.answer(text="Unprocessable command or message")
