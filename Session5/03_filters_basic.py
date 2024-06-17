# from aiogram import Bot, Dispatcher
# from aiogram.filters import Command, ChatMemberUpdatedFilter, IS_MEMBER, IS_NOT_MEMBER
#
# from aiogram.types import Message, ChatMemberUpdated
#
# BOT_TOKEN = "7172049198:AAHrWtw8XR_dUSn8LgXmX5fBQC-M8rJa_5E"
#
# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher()
#
#
# # def my_start_filter(message: Message):
# #     return message.text == "/start"
#
#
# @dp.my_chat_member(ChatMemberUpdatedFilter(KICKED))
# async def process_kicked(event: ChatMemberUpdated) -> None:
#     print(f"user {event.from_user.id} blocked the bot")
#
#
# @dp.my_chat_member(ChatMemberUpdatedFilter(IS_NOT_MEMBER >> IS_MEMBER))
# async def process_kicked(event: ChatMemberUpdated) -> None:
#     print(f"new user detected, chat ID: {event.from_user.id}")
#
#
# @dp.message(Command(commands="start"))
# async def process_start(message: Message) -> None:
#     await message.answer(text="به ربات ما خوش آمدید.")
#
#
# if __name__ == "__main__":
#     print("Starting")
#     dp.run_polling(bot)


# class MyClass:
#     def __init__(self):
#         pass
#
#     def __call__(self):
#         print("Class instance called")
#
#
# my_class_1 = MyClass()
#
# print(my_class_1())


from aiogram import Bot, Dispatcher
from aiogram.filters import Command, BaseFilter


from aiogram.types import Message

BOT_TOKEN = "7172049198:"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# list of admins chat ids
admin_ids: list[int] = [123456, 59778123305]


class IsAdmin(BaseFilter):
    """
    A custom filter for checking if a user is an admin.

    This class inherits from the BaseFilter class provided by the aiogram library.
    It is used to filter messages based on whether the sender is an admin or not.

    Attributes:
    admini_ids (list[int]): A list of user IDs that are considered admins.

    Methods:
    __init__(self, admini_ids: list[int]): The constructor method that initializes the admini_ids attribute.

    __call__(self, message: Message) -> bool:
        The method that is called when the filter is applied to a message.
        It checks if the sender's ID is in the admini_ids list and returns True if it is, otherwise False.
    """

    def __init__(self, admini_ids: list[int]):
        """
        Initialize the admini_ids attribute.

        Parameters:
        admini_ids (list[int]): A list of user IDs that are considered admins.
        """
        self.admini_ids = admini_ids

    async def __call__(self, message: Message) -> bool:
        """
        Check if the sender's ID is in the admini_ids list.

        Parameters:
        message (Message): The message to be checked.

        Returns:
        bool: True if the sender's ID is in the admini_ids list, otherwise False.
        """
        return message.from_user.id in self.admini_ids


@dp.message(IsAdmin(admin_ids))
async def process_admin(message: Message) -> None:
    await message.answer(text="شما ادمین هستید.")


@dp.message(Command(commands="start"))
async def process_start(message: Message) -> None:
    await message.answer(text="به ربات ما خوش آمدید.")


if __name__ == "__main__":
    print("Starting")
    dp.run_polling(bot)
