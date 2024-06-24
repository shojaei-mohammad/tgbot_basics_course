from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.exceptions import TelegramBadRequest


TOKEN = "7172049198:AAHrWtw8XR_dUSn8LgXmX5fBQC-M8rJa_5E"

bot = Bot(token=TOKEN)
dp = Dispatcher()

btn_1 = InlineKeyboardButton(text="btn_1", callback_data="btn_1")
btn_2 = InlineKeyboardButton(text="btn_2", callback_data="btn_2")
markup = InlineKeyboardMarkup(inline_keyboard=[[btn_1, btn_2]])


def create_markup(width: int, *args: str, **kwargs: str):
    buttons: list[InlineKeyboardButton] = []
    kb_builder = InlineKeyboardBuilder()

    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(text=button, callback_data=button))

    if kwargs:
        for text, button in kwargs.items():
            buttons.append(InlineKeyboardButton(text=text, callback_data=button))

    return kb_builder.row(*buttons, width=width).as_markup()


new_markup = create_markup(
    4, "button1", "button2", "button3", "button4", menu="button4"
)


@dp.message(CommandStart())
async def process_start(message: Message):
    await message.answer("Hello, I'm Echo Bot!", reply_markup=new_markup)


@dp.callback_query(F.data == "btn_1")
async def process_btn_1(callback_query: CallbackQuery):

    try:

        await callback_query.message.edit_text(
            text="menu changed to menu1",
            reply_markup=callback_query.message.reply_markup,
        )
        await callback_query.answer(text="btn_1 pressed")
    except TelegramBadRequest as e:
        await callback_query.answer(text=f"an error occured: {e}", show_alert=True)


@dp.callback_query(F.data == "btn_2")
async def process_btn_1(callback_query: CallbackQuery):
    try:

        await callback_query.message.edit_text(
            text="menu changed to menu1",
            reply_markup=callback_query.message.reply_markup,
        )
        await callback_query.answer(text="btn_2 pressed")
    except TelegramBadRequest as e:
        await callback_query.answer(text=f"an error occured: {e}", show_alert=True)


if __name__ == "__main__":
    print("Bot is running...")
    dp.run_polling(bot)
