from aiogram import Bot, Dispatcher

from config import laod_config

config = laod_config()
bot = Bot(config.tg_bot.token)
dp = Dispatcher()

# my_var_1 = 1
# my_var_2 = "something"
# #forst method
# dp.workflow_data.update({"my_var_1": may_var_1, "my_var_2": my_var_2})
# # second method
# dp["my_var_1"] = my_var_1
# dp["my_var_2"] = my_var_2
#
# #third method
# dp.start_polling(bot, my_var_1=my_var_1, my_var_2=my_var_2)
#
# @dp.message()
# async def echo(message, my_var_1, my_var_2):
#     print(my_var_1)
#     print(my_var_2)
#     await message.answer(message.text)


if __name__ == "__main__":
    dp.run_polling()
    print("Bot is running...")
