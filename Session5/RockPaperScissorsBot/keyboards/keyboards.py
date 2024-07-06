from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

button_yes = KeyboardButton(text="Let's Play!")
button_no = KeyboardButton(text="Not Now!")

yes_no_builder = ReplyKeyboardBuilder()
yes_no_builder.row(button_yes, button_no, width=2)

yes_no_markup = yes_no_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


btn_1 = KeyboardButton(text="Rock")
btn_2 = KeyboardButton(text="Paper")
btn_3 = KeyboardButton(text="Scissors")

game_kb = ReplyKeyboardMarkup(
    keyboard=[[btn_1], [btn_2], [btn_3]], resize_keyboard=True
)
