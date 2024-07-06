from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from Session5.RockPaperScissorsBot.keyboards.keyboards import yes_no_markup, game_kb
from Session5.RockPaperScissorsBot.services.utils import bot_choice, get_winner

users_router = Router()


@users_router.message(CommandStart())
async def process_start(message: Message):
    text = (
        "hello!\n\n"
        "This is a Rock, Paper, Scissors bot. you know the rules"
        "If not just send me the /help command, I'll guid you through the game"
    )
    await message.answer(text=text, reply_markup=yes_no_markup)


@users_router.message(Command("help"))
async def process_help(message: Message):
    text = (
        "This is a very simple game. We both choose one of three items at the same time: Rock, Paper, or Scissors.\n\n"
        "If we choose the same item, it's a draw. Otherwise, Rock beats Scissors, Scissors beat Paper, and Paper beats Rock.\n\n"
        "Shall we play?"
    )
    await message.answer(text=text, reply_markup=yes_no_markup)


@users_router.message(F.text == "Let's Play!")
async def process_play(message: Message):
    await message.answer(text="Okay, let's play!", reply_markup=game_kb)


@users_router.message(F.text == "Not Now!")
async def process_not_now(message: Message):
    await message.answer(text="Okay, see you later!")


@users_router.message(F.text.in_(["Rock", "Paper", "Scissors"]))
async def process_choice(message: Message):
    bot_choise = bot_choice()
    await message.answer(text=f"Bot choice: {bot_choise}\n\n")
    winner = get_winner(user_choice=message.text, bot_choice=bot_choise)
    await message.answer(text=f"Winner: {winner}\n\n")
