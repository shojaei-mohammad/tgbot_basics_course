import random

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

BOT_TOKEN = "7172049198:AAHrWtw8XR_dUSn8LgXmX5fBQC-M8rJa_5E"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
user_info: dict = {
    "in_game": False,
    "secret_numer": None,
    "attempts": None,
    "total_games": 0,
    "win_games": 0,
}

ATTEMPTS = 5


def get_random_numer():
    return random.randint(1, 100)


@dp.message(CommandStart())
async def process_start(message: Message) -> None:
    await message.answer(
        'سلام!\nبیایید بازی "حدس زدن عدد" را شروع کنیم؟\n\n'
        "برای دریافت قوانین بازی و لیست دستورات موجود، "
        "دستور /help را ارسال کنید.\n"
        "برای شروع بازی با ارسال یکی از پیام‌های زیر بازی شروع خواهد شد.\n\n"
        "بازی ، بازی کنیم، بزن بریم"
    )


@dp.message(Command(commands=["help"]))
async def process_help(message: Message) -> None:
    await message.answer(
        f"قوانین بازی:\n\nمن عددی بین 1 تا 100 در نظر می‌گیرم، "
        f"و شما باید آن را حدس بزنید\nشما {ATTEMPTS} بار فرصت دارید\n\n"
        f"دستورات موجود:\n/help - قوانین بازی و لیست دستورات\n"
        f"/cancel - خروج از بازی\n/stat - مشاهده آمار\n\n"
        f"بیایید بازی کنیم؟"
        "برای شروع کافی کلمه 'بازی' رو برام ارسال کنی"
    )


@dp.message(Command(commands=["stat"]))
async def process_game(message: Message) -> None:
    await message.answer(
        f"تعداد کل بازی‌های: {user_info['total_games']}\n"
        f"تعداد بازی‌های برنده: {user_info['win_games']}\n"
    )


@dp.message(Command(commands=["cancle"]))
async def process_cancle(message: Message) -> None:
    if user_info["in_game"]:
        user_info["in_game"] = False
        await message.answer("بازی متوقف شد")
    else:
        await message.answer("در حال حاضر بازی  نمیکنید")


@dp.message(F.text.in_(["بازی", "بازی میکنم", "بزن بریم"]))
async def process_possitive_answer(message: Message) -> None:
    if not user_info["in_game"]:
        user_info["in_game"] = True
        user_info["secret_numer"] = get_random_numer()
        user_info["attempts"] = ATTEMPTS

        await message.answer("من یک عدد بین صفر تا صدد در نظر گرفتم سعی کد حدس بزنیش")

    else:
        await message.answer(
            "شما در حال بازی هستید و فقط میتوانید عدد ارسال کنید \n\n"
            "با استفاده از دستور /cancle میتوانید بازی را لغو کنید."
        )


@dp.message(F.text.in_(["باشه بعدا", "بازی نمیکنم", "نه"]))
async def process_negative_answer(message: Message) -> None:
    if not user_info["in_game"]:
        await message.answer(
            "هروقت دوست داشتی بازی کنی فقط کافیه کلمه  بازی رو برای من ارسال کنی"
        )
    else:
        await message.answer(
            "شما در حال بازی هستید تلاش کنید که عدد مخفی رو پیدا کنید."
        )


@dp.message(lambda x: x.text and x.text.isdigit() and 1 < int(x.text) < 100)
async def process_answer(message: Message) -> None:
    gussed_number = int(message.text)
    if user_info["in_game"]:
        if gussed_number == user_info["secret_numer"]:
            user_info["total_games"] += 1
            user_info["win_games"] += 1
            await message.answer(
                f"عدد مخفی: {user_info['secret_numer']}\n"
                f"عدد شما: {gussed_number}\n\n"
                f"عدد شما درست بود\n"
                f"بازی متوقف شد"
            )
            user_info["in_game"] = False
        elif gussed_number > user_info["secret_numer"]:
            await message.answer("عدد مخفی کوچکتر است")
            user_info["attempts"] -= 1
        elif gussed_number < user_info["secret_numer"]:
            await message.answer("عدد مخفی بزرگتر است")
            user_info["attempts"] -= 1

        if user_info["attempts"] == 0:
            user_info["total_games"] += 1
            user_info["in_game"] = False
            await message.answer(
                f"شما باختید \n\n عدد مخفی: {user_info['secret_numer']}"
            )

    else:
        await message.answer("شما در حال بازی نیستید")


@dp.message()
async def process_other_entry(message: Message) -> None:
    if user_info["in_game"]:
        await message.answer(
            "شما در حال بازی هستید و فقط میتوانید عدد ارسال کنید \n\n"
            "با استفاده از دستور /cancle میتوانید بازی را لغو کنید."
        )
    else:
        await message.answer(
            "هروقت دوست داشتی بازی کنی فقط کافیه کلمه  بازی رو برای من ارسال کنی"
        )


if __name__ == "__main__":
    print("Bot is running...")
    dp.run_polling(bot)
