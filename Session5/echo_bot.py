from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN = "7172049198:AAHrWtw8XR_dUSn8LgXmX5fBQC-M8rJa_5E"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=["start"]))
async def process_start(message: Message) -> None:
    await message.answer(text="به ربات ما خوش آمدید.\nیک متن برای من ارسال کن")


@dp.message(F.photo)
async def handle_photo(message: Message) -> None:
    await message.answer(message.photo[-1].file_id)
    await message.reply_photo(message.photo[-1].file_id)


@dp.message()
async def echo(message: Message) -> None:
    await message.answer(text=message.text)


if __name__ == "__main__":
    dp.run_polling(bot)
