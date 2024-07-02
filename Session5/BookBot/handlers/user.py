from copy import deepcopy

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart

from Session5.BookBot.database.db import users_db, user_dict_template
from Session5.BookBot.filters.filter import IsDelBookmarkCallback, IsDigitCallback
from Session5.BookBot.keyboards.bookmark_kb import create_bookmark_kb, edit_bookmark_kb
from Session5.BookBot.keyboards.pahination_kb import pagination_bookmarks_kb
from Session5.BookBot.services.prepare_book import book

user_router = Router()


@user_router.message(CommandStart())
async def process_start_command(message: Message):
    text = (
        "Hello, reader!\n\nThis is a bot in which "
        "you can read book's.\n\nTo view the list of available "
        "commands - type /help"
    )
    await message.answer(text)
    if message.chat.id not in users_db:
        users_db[message.chat.id] = deepcopy(user_dict_template)


@user_router.message(Command(commands="help"))
async def process_help(message: Message):
    text = (
        "This is a reader bot\n\nAvailable commands:\n\n/beginning - "
        "go to the beginning of the book\n/continue - continue"
        "reading\n/bookmarks - view the list of bookmarks\n/help - "
        "help for the bot\n\nTo save a bookmark - "
        "click on the button with the page number\n\nHave fun reading!"
    )
    await message.answer(text)


@user_router.message(Command(commands="beginning"))
async def process_beginning_command(message: Message):
    users_db[message.chat.id]["page"] = 1
    text = book[users_db[message.chat.id]["page"]]

    await message.answer(
        text,
        reply_markup=pagination_bookmarks_kb(
            "backward", f"{users_db[message.chat.id]['page']} / {len(book)}", "forward"
        ),
    )


@user_router.message(Command(commands="continue"))
async def process_continue_command(message: Message):
    text = book[users_db[message.chat.id]["page"]]

    await message.answer(
        text,
        reply_markup=pagination_bookmarks_kb(
            "backward", f"{users_db[message.chat.id]['page']} / {len(book)}", "forward"
        ),
    )


@user_router.message(Command(commands="bookmarks"))
async def process_bookmarks_command(message: Message):
    if users_db[message.chat.id]["bookmarks"]:
        await message.answer(
            text="This is your bookmark list",
            reply_markup=create_bookmark_kb(*users_db[message.chat.id]["bookmarks"]),
        )
    else:
        await message.answer(text="You don't have any bookmarks")


@user_router.callback_query(F.data == "forward")
async def process_forward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]["page"] < len(book):
        users_db[callback.from_user.id]["page"] += 1
        text = book[users_db[callback.from_user.id]["page"]]

        await callback.message.edit_text(
            text,
            reply_markup=pagination_bookmarks_kb(
                "backward",
                f"{users_db[callback.from_user.id]['page']} / {len(book)}",
                "forward",
            ),
        )
    await callback.answer()


@user_router.callback_query(F.data == "backward")
async def process_backward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]["page"] > 1:
        users_db[callback.from_user.id]["page"] -= 1
        text = book[users_db[callback.from_user.id]["page"]]

        await callback.message.edit_text(
            text,
            reply_markup=pagination_bookmarks_kb(
                "backward",
                f"{users_db[callback.from_user.id]['page']} / {len(book)}",
                "forward",
            ),
        )


@user_router.callback_query(
    lambda x: " / " in x.data and x.data.replace(" / ", "").isdigit()
)
async def process_page_press(callback: CallbackQuery):
    users_db[callback.from_user.id]["bookmarks"].add(
        users_db[callback.from_user.id]["page"]
    )
    await callback.answer()


@user_router.callback_query(IsDigitCallback())
async def process_bookmark_press(callback: CallbackQuery):
    text = book[int(callback.data)]
    users_db[callback.from_user.id]["page"] = int(callback.data)
    await callback.message.edit_text(
        text,
        reply_markup=pagination_bookmarks_kb(
            "backward",
            f"{users_db[callback.from_user.id]['page']} / {len(book)}",
            "forward",
        ),
    )


@user_router.callback_query(F.data == "edit_bookmark")
async def process_edit_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text="This is your bookmark list for edit",
        reply_markup=edit_bookmark_kb(*users_db[callback.from_user.id]["bookmarks"]),
    )


@user_router.callback_query(F.data == "cancel_bookmark")
async def process_cancel_press(callback: CallbackQuery):
    await callback.message.edit_text(text="'/continue - continue reading'")


@user_router.callback_query(IsDelBookmarkCallback())
async def process_del_bookmark_press(callback: CallbackQuery):
    users_db[callback.from_user.id]["bookmarks"].remove(int(callback.data[:-3]))
    if users_db[callback.from_user.id]["bookmarks"]:
        await callback.message.edit_text(
            text="This is your bookmark list for edit",
            reply_markup=edit_bookmark_kb(
                *users_db[callback.from_user.id]["bookmarks"]
            ),
        )
    else:
        await callback.message.edit_text(text="You don't have any bookmarks")
