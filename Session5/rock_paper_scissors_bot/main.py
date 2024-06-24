import asyncio

from aiogram import Bot, Dispatcher

from Session5.rock_paper_scissors_bot.config import load_config
from Session5.rock_paper_scissors_bot.handers.other_handlers import other_router
from Session5.rock_paper_scissors_bot.handers.users import users_router
from Session5.rock_paper_scissors_bot.services.bot_commands import set_commands


async def main() -> None:
    config = load_config()
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    dp.include_router(users_router)
    dp.include_router(other_router)
    await set_commands(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Bot is running...")
    asyncio.run(main())
