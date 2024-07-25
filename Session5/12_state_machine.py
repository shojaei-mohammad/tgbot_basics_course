from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message

API_TOKEN = "YOUR_TOKEN"

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)


class RegistrationForm(StatesGroup):
    name = State()
    age = State()
    location = State()
    photo = State()


@dp.message(CommandStart())
async def process_start(message: Message, state: FSMContext):
    await state.set_state(RegistrationForm.name)
    await message.reply(text="Lets start registration, please enter your full name:")


@dp.message(RegistrationForm.name)
async def name_handler(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(RegistrationForm.age)
    await message.reply(text="Now enter your age:")


@dp.message(RegistrationForm.age, F.text.isdigit())
async def age_handler(message: Message, state: FSMContext):

    await state.update_data(age=message.text)
    await state.set_state(RegistrationForm.location)
    await message.reply(text="Great, Now enter your location:")


@dp.message(RegistrationForm.age)
async def invalid_age_handler(message: Message):
    await message.reply(text="Please enter your age in digits.")


@dp.message(RegistrationForm.location)
async def location_handler(message: Message, state: FSMContext):
    await state.update_data(location=message.text)
    await state.set_state(RegistrationForm.photo)
    await message.reply(text="Last Step, give me you photo")


@dp.message(RegistrationForm.photo, F.photo)
async def photo_handler(message: Message, state: FSMContext):
    photo = message.photo[-1]
    file_id = photo.file_id
    await state.update_data(file_id=file_id)
    data = await state.get_data()
    name = data.get("name")
    age = data.get("age")
    location = data.get("location")
    file_id = data.get("file_id")
    text = (
        "Here is your data:\n\n"
        f"Name: {name}\n"
        f"Age: {age}\n"
        f"Location: {location}\n"
    )
    await message.answer_photo(photo=file_id, caption=text)

    await state.clear()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
