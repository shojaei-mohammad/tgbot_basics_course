import logging

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from Session5.MiddlewareMiniBot.filters.filters import MyTrueFilter, MyFalseFilter

logger = logging.getLogger(__name__)

user_router = Router()


@user_router.message(CommandStart(), MyTrueFilter())
async def process_start_command(message: Message):
    logger.debug("Entered the handler for the /start command")
    button = InlineKeyboardButton(text="Button", callback_data="button_pressed")
    markup = InlineKeyboardMarkup(inline_keyboard=[[button]])
    await message.answer(text="You pressed the button!", reply_markup=markup)
    logger.debug("Exiting the handler for the /start command")


# This handler triggers on pressing the inline button
@user_router.callback_query(F.data, MyTrueFilter())
async def process_button_click(callback: CallbackQuery):
    logger.debug("Entered the handler for inline button press")
    await callback.answer(text="You pressed the button!")
    logger.debug("Exiting the handler for inline button press")


@user_router.message(F.text, MyFalseFilter())
async def process_text(message: Message):
    logger.debug("Entered the handler for text processing")
    logger.debug("Exiting the handler for text processing")
