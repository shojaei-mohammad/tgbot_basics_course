"""
useful links:

    HTML Style:
        https://core.telegram.org/bots/api#html-style

    Markdown Style:
        https://core.telegram.org/bots/api#markdownv2-style
"""

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message


TOKEN = "YOUR_TOKEN"


bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="HTML"))

dp = Dispatcher()


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text="Hello!\n\nI'm a bot demonstrating "
        "how markup works. Send the command "
        "from the list below:\n\n"
        "/html - example markup using HTML\n"
        "/markdownv2 - example of marking using MarkdownV2\n"
        "/noformat - example with markup, but without indication "
        "parameter parse_mode"
    )


@dp.message(Command(commands="help"))
async def process_help_command(message: Message):
    await message.answer(
        text="I'm a bot demonstrating"
        "how markup works. Send the command "
        "from the list below:\n\n"
        "/html is an example of markup using HTML\n"
        "/markdownv2 - example of markup using MarkdownV2\n"
        "/noformat - example with markup, but without specifying "
        "parameter parse_mode"
    )


@dp.message(Command(commands="html"))
async def process_html_command(message: Message):
    await message.answer(
        text="This is a text demonstrating "
        "how HTML markup works:\n\n"
        "<b>This is bold text</b>\n"
        "<i>This is italic text</i>\n"
        "<u>This is underlined text</u>\n"
        '<span class="tg-spoiler">And this is a spoiler</span>\n\n'
        "To view the list of available commands again - "
        "send the command /help",
        parse_mode=ParseMode.HTML,
    )


@dp.message(Command(commands="markdownv2"))
async def process_markdownv2_command(message: Message):
    await message.answer(
        text="This is a text demonstrating "
        "how MarkdownV2\-markup works:\n\n"
        "*This is bold text*\n"
        "_This is italic text_\n"
        "__This is underlined text__\n"
        "||And this is a spoiler||\n\n"
        "To view the list of available commands again \- "
        "send the command /help",
        parse_mode="MarkdownV2",
    )


@dp.message(Command(commands="noformat"))
async def process_noformat_command(message: Message):
    await message.answer(
        text="This is a text demonstrating "
        "how text is displayed if you don't specify "
        "parameter parse_mode:\n\n"
        "<b>This could be bold text</b>\n"
        "_This could be italic text_\n"
        "<u>This could be underlined text</u>\n"
        "||And this could be a spoiler||\n\n"
        "To view the list of available commands again - "
        "send command /help"
    )


@dp.message()
async def send_echo(message: Message):
    await message.answer(
        text="I can't even imagine,"
        "what do you mean\n\n"
        "To view the list of available commands - "
        "send command /help"
    )


if __name__ == "__main__":
    dp.run_polling(bot)
