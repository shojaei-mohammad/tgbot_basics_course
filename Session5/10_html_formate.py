from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

BOT_TOKEN = "YOUR_TOKEN"

bot = Bot(BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text="Hello!\n\nI am a bot demonstrating how HTML "
        "formatting works. Send a command from the list below:\n\n"
        "/bold - bold text\n"
        "/italic - italic text\n"
        "/underline - underlined text\n"
        "/strike - strikethrough text\n"
        "/spoiler - spoiler\n"
        "/link - external link\n"
        "/tglink - internal link\n"
        "/code - monospace text\n"
        "/pre - preformatted text\n"
        "/precode - preformatted code block\n"
        "/precodediff - difference between &lt;code&gt; and &lt;pre&gt;\n"
        "/boldi - bold italic text\n"
        "/iu - italic underlined text\n"
        "/biu - bold italic underlined text"
    )


@dp.message(Command(commands="help"))
async def process_help_command(message: Message):
    await message.answer(
        text="I am a bot demonstrating how HTML "
        "formatting works. Send a command from the list below:\n\n"
        "/bold - bold text\n"
        "/italic - italic text\n"
        "/underline - underlined text\n"
        "/strike - strikethrough text\n"
        "/spoiler - spoiler\n"
        "/link - external link\n"
        "/tglink - internal link\n"
        "/code - monospace text\n"
        "/pre - preformatted text\n"
        "/precode - preformatted code block\n"
        "/precodediff - difference between &lt;code&gt; and &lt;pre&gt;\n"
        "/boldi - bold italic text\n"
        "/iu - italic underlined text\n"
        "/biu - bold italic underlined text"
    )


@dp.message(Command(commands="bold"))
async def process_bold_command(message: Message):
    await message.answer(
        text="&lt;b&gt;This is bold text&lt;/b&gt;:\n"
        "<b>This is bold text</b>\n\n"
        "&lt;strong&gt;And this is also bold text&lt;/strong&gt;:\n"
        "<strong>And this is also bold text</strong>"
    )


@dp.message(Command(commands="italic"))
async def process_italic_command(message: Message):
    await message.answer(
        text="&lt;i&gt;This is italic text&lt;/i&gt;:\n"
        "<i>This is italic text</i>\n\n"
        "&lt;em&gt;And this is also italic text&lt;/em&gt;:\n"
        "<em>And this is also italic text</em>"
    )


@dp.message(Command(commands="underline"))
async def process_underline_command(message: Message):
    await message.answer(
        text="&lt;u&gt;This is underlined text&lt;/u&gt;:\n"
        "<u>This is underlined text</u>\n\n"
        "&lt;ins&gt;And this is also underlined text&lt;/ins&gt;:\n"
        "<ins>And this is also underlined text</ins>"
    )


@dp.message(Command(commands="strike"))
async def process_strike_command(message: Message):
    await message.answer(
        text="&lt;s&gt;This is strikethrough text&lt;/s&gt;:\n"
        "<s>This is strikethrough text</s>\n\n"
        "&lt;strike&gt;And this is also strikethrough text&lt;/strike&gt;:\n"
        "<strike>And this is also strikethrough text</strike>\n\n"
        "&lt;del&gt;And this is also strikethrough text&lt;/del&gt;:\n"
        "<del>And this is also strikethrough text</del>"
    )


@dp.message(Command(commands="spoiler"))
async def process_spoiler_command(message: Message):
    await message.answer(
        text='&lt;span class="tg-spoiler"&gt;This is spoiler text&lt;/span&gt;:\n'
        '<span class="tg-spoiler">This is spoiler text</span>\n\n'
        "&lt;tg-spoiler&gt;And this is spoiler text&lt;/tg-spoiler&gt;:\n"
        "<tg-spoiler>And this is spoiler text</tg-spoiler>"
    )


@dp.message(Command(commands="link"))
async def process_link_command(message: Message):
    await message.answer(
        text='&lt;a href="https://google.com"&gt;External '
        "link&lt;/a&gt;:\n"
        '<a href="https://google.com">External link</a>'
    )


@dp.message(Command(commands="tglink"))
async def process_tglink_command(message: Message):
    await message.answer(
        text='&lt;a href="tg://user?id=173901673"&gt;Internal '
        "link&lt;/a&gt;:\n"
        '<a href="tg://user?id=173901673">Internal link</a>'
    )


@dp.message(Command(commands="code"))
async def process_code_command(message: Message):
    await message.answer(
        text="&lt;code&gt;This is monospace text&lt;/code&gt;:\n"
        "<code>This is monospace text</code>"
    )


@dp.message(Command(commands="pre"))
async def process_pre_command(message: Message):
    await message.answer(
        text="&lt;pre&gt;Preformatted text&lt;/pre&gt;:\n"
        "<pre>Preformatted text</pre>"
    )


@dp.message(Command(commands="precode"))
async def process_precode_command(message: Message):
    await message.answer(
        text='&lt;pre&gt;&lt;code class="language-python"&gt;'
        "Preformatted code block in Python&lt;/code&gt;&lt;/pre&gt;:\n"
        '<pre><code class="language-python">'
        "Preformatted code block in Python</code></pre>"
    )


@dp.message(Command(commands="precodediff"))
async def process_precodediff_command(message: Message):
    await message.answer(
        text="This text helps to understand the difference between "
        "the tags &lt;code&gt; and &lt;pre&gt; - text inside "
        "the &lt;code&gt; tag <code>does not stand out as a "
        "separate block</code>, but becomes part of the line in which it is placed, "
        "while the &lt;pre&gt; tag separates the text <pre>into a separate block,</pre> breaking "
        "the line in which it is placed"
    )


@dp.message(Command(commands="boldi"))
async def process_boldi_command(message: Message):
    await message.answer(
        text="&lt;b&gt;&lt;i&gt;This is bold italic text&lt;/i&gt;&lt;/b&gt;:\n\n"
        "<b><i>This is bold italic text</i></b>"
    )


@dp.message(Command(commands="iu"))
async def process_iu_command(message: Message):
    await message.answer(
        text="&lt;i&gt;&lt;u&gt;This is italic underlined text&lt;/u&gt;&lt;/i&gt;:\n\n"
        "<i><u>This is italic underlined text</u></i>"
    )


@dp.message(Command(commands="biu"))
async def process_biu_command(message: Message):
    await message.answer(
        text="&lt;b&gt;&lt;i&gt;&lt;u&gt;This is bold italic underlined "
        "text&lt;/u&gt;&lt;/i&gt;&lt;/b&gt;:\n\n"
        "<b><i><u>This is bold italic underlined text</u></i></b>"
    )


async def send_echo(message: Message):
    await message.answer(
        text="I can't even imagine what you mean\n\n"
        "To see a list of available commands, send the /help command"
    )


if __name__ == "__main__":
    dp.run_polling(bot)
