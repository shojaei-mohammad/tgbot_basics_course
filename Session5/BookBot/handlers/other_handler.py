from aiogram import Router
from aiogram.types import Message

other_handler_rouer = Router()


@other_handler_rouer.message()
async def handle_other_method(message: Message):
    await message.answer(text="Unprocessable command")
