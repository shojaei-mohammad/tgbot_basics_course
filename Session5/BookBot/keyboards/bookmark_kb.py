from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from Session5.BookBot.services.prepare_book import book


def create_bookmark_kb(*args) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()

    for page in sorted(args):
        kb_builder.row(
            InlineKeyboardButton(
                text=f"{page} - {book[page][:30]}", callback_data=str(page)
            )
        )

    kb_builder.row(
        InlineKeyboardButton(text="Edit", callback_data="edit_bookmark"),
        InlineKeyboardButton(text="Cancel", callback_data="cancel_bookmark"),
        width=2,
    )

    return kb_builder.as_markup()


def edit_bookmark_kb(*args) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()

    for page in sorted(args):
        kb_builder.row(
            InlineKeyboardButton(
                text=f"❌ {page} - {book[page][:30]}", callback_data=f"{page}del"
            )
        )

    kb_builder.row(
        InlineKeyboardButton(text="Cancel", callback_data="cancel_bookmark"),
    )

    return kb_builder.as_markup()
