from aiogram import Bot
from aiogram.types import BotCommand


async def set_commands(bot: Bot):
    bot_commands = [
        BotCommand(command="/start", description="show main menu"),
        BotCommand(command="/help", description="show help"),
        BotCommand(command="/beginning", description="start fresh reading"),
        BotCommand(command="/continue", description="continue reading"),
        BotCommand(command="/bookmarks", description="show bookmarks"),
    ]
    await bot.set_my_commands(commands=bot_commands)
