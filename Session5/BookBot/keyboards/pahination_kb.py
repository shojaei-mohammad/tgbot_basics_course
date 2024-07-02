from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def pagination_bookmarks_kb(*buttons: str) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_mapper: dict = {
        "backward": "<<",
        "forward": ">>",
    }
    keyboard = []
    for button in buttons:

        keyboard.append(
            InlineKeyboardButton(
                text=kb_mapper[button] if button in kb_mapper else button,
                callback_data=button,
            ),
        )
    kb_builder.row(*keyboard, width=3)
    return kb_builder.as_markup()
