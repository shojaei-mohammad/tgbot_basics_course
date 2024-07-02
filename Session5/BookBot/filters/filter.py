from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery


class IsDigitCallback(BaseFilter):
    async def __call__(self, call: CallbackQuery) -> bool:
        return call.data.isdigit()


class IsDelBookmarkCallback(BaseFilter):
    async def __call__(self, call: CallbackQuery) -> bool:
        return call.data.endswith("del") and call.data[:-3].isdigit()
