import asyncio

from aiogram import Bot, Dispatcher

from Session5.BookBot.handlers.other_handler import other_handler_rouer
from Session5.BookBot.handlers.user import user_router
from Session5.BookBot.services.bot_commands import set_commands
from Session5.SampleStructure.config import laod_config


async def main():
    config = laod_config()
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()
    await set_commands(bot)
    dp.include_router(user_router)
    dp.include_router(other_handler_rouer)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Bot is running...")
    asyncio.run(main())
