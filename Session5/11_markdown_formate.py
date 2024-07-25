from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

BOT_TOKEN = "YOUR_TOKEN"

bot = Bot(BOT_TOKEN, default=DefaultBotProperties(parse_mode="MarkdownV2"))
dp = Dispatcher()


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text="Hello\!\n\nI am a bot demonstrating how MarkdownV2 formatting works\. "
        "Send a command from the list below:\n\n"
        "/bold \- bold text\n"
        "/italic \- italic text\n"
        "/underline \- underlined text\n"
        "/strike \- strikethrough text\n"
        "/spoiler \- spoiler\n"
        "/link \- external link\n"
        "/tglink \- internal link\n"
        "/code \- monospace text\n"
        "/pre \- preformatted text\n"
        "/precode \- preformatted code block\n"
        "/boldi \- bold italic text\n"
        "/iu \- italic underlined text\n"
        "/biu \- bold italic underlined text"
    )


@dp.message(Command(commands="help"))
async def process_help_command(message: Message):
    await message.answer(
        text="I am a bot demonstrating how MarkdownV2 formatting works\. "
        "Send a command from the list below:\n\n"
        "/bold \- bold text\n"
        "/italic \- italic text\n"
        "/underline \- underlined text\n"
        "/strike \- strikethrough text\n"
        "/spoiler \- spoiler\n"
        "/link \- external link\n"
        "/tglink \- internal link\n"
        "/code \- monospace text\n"
        "/pre \- preformatted text\n"
        "/precode \- preformatted code block\n"
        "/boldi \- bold italic text\n"
        "/iu \- italic underlined text\n"
        "/biu \- bold italic underlined text"
    )


@dp.message(Command(commands="bold"))
async def process_bold_command(message: Message):
    await message.answer(text="\*This is bold text\*:\n" "*This is bold text*")


@dp.message(Command(commands="italic"))
async def process_italic_command(message: Message):
    await message.answer(text="\_This is italic text\_:\n" "_This is italic text_")


@dp.message(Command(commands="underline"))
async def process_underline_command(message: Message):
    await message.answer(
        text="\_\_This is underlined text\_\_:\n" "__This is underlined text__"
    )


@dp.message(Command(commands="strike"))
async def process_strike_command(message: Message):
    await message.answer(
        text="\~This is strikethrough text\~:\n" "~This is strikethrough text~"
    )


@dp.message(Command(commands="spoiler"))
async def process_spoiler_command(message: Message):
    await message.answer(
        text="\|\|This is spoiler text\|\|:\n" "||This is spoiler text||"
    )


@dp.message(Command(commands="link"))
async def process_link_command(message: Message):
    await message.answer(
        text="\[External link\]\(https://google\.com\):\n"
        "[External link](https://google.com)"
    )


@dp.message(Command(commands="tglink"))
async def process_tglink_command(message: Message):
    await message.answer(
        text="\[Internal link\]\(tg://user?id\=173901673\):\n"
        "[Internal link](tg://user?id=173901673)"
    )


@dp.message(Command(commands="code"))
async def process_code_command(message: Message):
    await message.answer(text="\`Monospace text\`:\n" "`Monospace text`")


@dp.message(Command(commands="pre"))
async def process_pre_command(message: Message):
    await message.answer(
        text="\`\`\` Preformatted text\`\`\`:\n" "``` Preformatted text```"
    )


@dp.message(Command(commands="precode"))
async def process_precode_command(message: Message):
    await message.answer(
        text="\`\`\`python Preformatted code block in Python\`\`\`:\n"
        "```python Preformatted code block in Python```"
    )


@dp.message(Command(commands="boldi"))
async def process_boldi_command(message: Message):
    await message.answer(
        text="\*\_This is bold italic text\_\*:\n" "*_This is bold italic text_*"
    )


@dp.message(Command(commands="iu"))
async def process_iu_command(message: Message):
    await message.answer(
        text="\_\_\_This is italic underlined text\_\_\_:\n"
        "___This is italic underlined text___"
    )


@dp.message(Command(commands="biu"))
async def process_biu_command(message: Message):
    await message.answer(
        text="\*\_\_\_This is bold italic underlined text\_\_\_\*:\n"
        "*___This is bold italic underlined text___*"
    )


@dp.message()
async def send_echo(message: Message):
    await message.answer(
        text="I can't even imagine what you mean\n\n"
        "To see a list of available commands, send the /help command"
    )


if __name__ == "__main__":
    dp.run_polling(bot)
