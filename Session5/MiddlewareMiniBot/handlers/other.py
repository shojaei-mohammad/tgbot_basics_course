import logging

from aiogram import Router
from aiogram.types import Message


from Session5.MiddlewareMiniBot.filters.filters import MyTrueFilter, MyFalseFilter

logger = logging.getLogger(__name__)

other_router = Router()


@other_router.message(MyTrueFilter())
async def send_echo(message: Message):
    logger.debug("Entered Echo Handler")
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        text = "This type of update is not supported " "using the send_copy method"
        await message.reply(text=text)
    logger.debug("Exiting Echo Handler")
