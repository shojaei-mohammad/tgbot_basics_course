from aiogram import Bot
from aiogram.types import BotCommand


async def set_commands(bot: Bot):
    main_menu_commads = [
        BotCommand(command="/start", description="show main menu"),
        BotCommand(command="/help", description="show help menu"),
        BotCommand(command="/about", description="show about menu"),
    ]

    await bot.set_my_commands(commands=main_menu_commads)
