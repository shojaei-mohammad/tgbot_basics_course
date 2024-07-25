from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    KeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButtonPollType,
    WebAppInfo,
    KeyboardButtonRequestUsers,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

TOKEN = "YOUR_TOKEN"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# btn1 = KeyboardButton(text="dog")
# btn2 = KeyboardButton(text="cat")
# markup = ReplyKeyboardMarkup(keyboard=[[btn1, btn2]], resize_keyboard=True)
#
#
# @dp.message(CommandStart())
# async def process_start(message: Message):
#     await message.answer("Hello, I'm Echo Bot!", reply_markup=markup)
#
#
# @dp.message(F.text == "cat")
# async def process_cat(message: Message):
#     await message.answer_photo(photo=FSInputFile("cat.png"))
#
#
# @dp.message(F.text == "dog")
# async def process_cat(message: Message):
#     await message.answer_photo(photo=FSInputFile("dog.jpg"))

# btn1 = KeyboardButton(text="button 1")
# btn2 = KeyboardButton(text="button 2")
# btn3 = KeyboardButton(text="button 3")
# btn4 = KeyboardButton(text="button 4")
# btn5 = KeyboardButton(text="button 5")
# btn6 = KeyboardButton(text="button 6")
# btn7 = KeyboardButton(text="button 7")
# btn8 = KeyboardButton(text="button 8")
# btn9 = KeyboardButton(text="button 9")
# markup = ReplyKeyboardMarkup(
#     keyboard=[
#         [btn1, btn2, btn3],
#         [
#             btn4,
#             btn5,
#             btn6,
#         ],
#         [btn7, btn8, btn9],
#     ],
#     resize_keyboard=True,
# )
# keyboard: list[list[KeyboardButton]] = [
#     [KeyboardButton(text=f"button{j + 3 + i}") for i in range(1, 4)] for j in range(3)
# ]
#
# markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

# buttons: list[KeyboardButton] = [
#     KeyboardButton(text=f"button{i}") for i in range(1, 10)
# ]
# keyboard: list[list[KeyboardButton]] = [
#     [buttons[0]],
#     buttons[1:3],
#     buttons[3:6],
#     buttons[6:8],
#     [buttons[8]],
# ]


# buttons_1: list[KeyboardButton] = [KeyboardButton(text=f"{i+1}") for i in range(5)]
# buttons_2: list[KeyboardButton] = [KeyboardButton(text=f"{i+6}") for i in range(10)]
# builder = ReplyKeyboardBuilder()
# builder.row(*buttons_1, width=5)
# builder.add(*buttons_2)
# builder.adjust(2, 1, 3, repeat=True)


contact = KeyboardButton(text=f"contact", request_contact=True)
location = KeyboardButton(text=f"location", request_location=True)
poll = KeyboardButton(text=f"poll", request_poll=KeyboardButtonPollType())
web_app = KeyboardButton(text=f"web_app", web_app=WebAppInfo(url="https://github.com"))
user = KeyboardButton(
    text=f"user", request_users=KeyboardButtonRequestUsers(request_id=1)
)
markup = ReplyKeyboardMarkup(keyboard=[[contact, location, poll, web_app, user]])


@dp.message(CommandStart())
async def process_start(message: Message):
    await message.answer("Hello, I'm Echo Bot!", reply_markup=markup)


if __name__ == "__main__":
    print("Bot is running...")
    dp.run_polling(bot)
