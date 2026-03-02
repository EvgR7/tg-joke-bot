import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from database import add_user, increment_joke, increment_word_joke, udate_last_seen, get_stats
from aiogram.types import Message
from aiogram.filters import Command
from dotenv import load_dotenv
from joke import Joke
from keyboard import control_keyboard
import os

load_dotenv()
TOKEN = os.getenv('TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID')

bot = Bot(token=TOKEN)
dp = Dispatcher()

class  Form(StatesGroup):
    waiting_for_word = State()

jokes = {}
joke = Joke()
@dp.message(Command("start"))
async def start(message:Message):
    add_user(message.from_user.id)
    udate_last_seen(message.from_user.id)

    jokes[message.chat.id] = [joke, message.from_user.id]
    #jokes['user_id'] = message.from_user.id
    await message.answer("Hi! Select the option", reply_markup=control_keyboard())


@dp.message(Command("stats"))
async def stats(message:Message):

    if message.from_user.id != int(ADMIN_ID):
        return
    total_users, total_jokes, total_word_jokes = get_stats()
    text = (
        f"Статистика бота:\n\n"
        f"Пользователей: {total_users}\n"
        f"Рандомных шуток: {total_jokes}\n"
        f"Шуток по слову: {total_word_jokes}\n"
    )
    await message.answer(text)


@dp.callback_query(F.data.in_({'JOKE','JOKEONWORD'}))
async def request(callback, state:FSMContext):

    if callback.data == 'JOKE':
        joke = jokes[callback.message.chat.id][0]

        increment_joke(jokes[callback.message.chat.id][1])
        text = joke.get_joke_rand()

        await callback.message.answer(text, reply_markup=control_keyboard())
    elif callback.data == 'JOKEONWORD':
        increment_word_joke(jokes[callback.message.chat.id][1])

        await callback.message.answer('Please enter the word')
        await state.set_state(Form.waiting_for_word)
    await callback.answer()

@dp.message(Form.waiting_for_word)
async def process_word(message:Message, state:FSMContext):
    word = message.text
    joke = jokes[message.chat.id][0]
    await message.answer(joke.return_rand_joke(word), reply_markup=control_keyboard())
    await state.clear()

async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())
