import asyncio
import random
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from config import config
from funcs import greet, question1_1, question1_2, \
    question2_1, question2_2, question3, end, \
    attempting_start_again, accepted, not_accepted, \
    alreadly_won

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()
states = config.States()
answers = config.answers


@dp.message(Command('start'))
async def start_handler(message: types.Message, state: FSMContext):
    if not await state.get_state():
        await message.answer(greet())

        choice = random.randint(1, 2)
        print(choice)

        if choice == 1:
            await bot.send_message(message.from_user.id, question1_1(), reply_markup=config.question1_1_markup)
            await state.set_state(states.answering1_1)

        elif choice == 2:
            await bot.send_message(message.from_user.id, question1_2(), reply_markup=config.question1_2_markup)
            await state.set_state(states.answering1_2)

    else:
        await message.answer(attempting_start_again())


@dp.message(StateFilter(states.answering1_1, states.answering1_2))
async def question1_handler(message: types.Message, state: FSMContext):
    curr_question = int(str(await state.get_state())[-3:])

    if message.text == answers[curr_question]:
        await message.answer(accepted())
        choice = random.randint(1, 2)

        if choice == 1:
            await bot.send_message(message.from_user.id, question2_1(), reply_markup=config.question2_1_markup)
            await state.set_state(states.answering2_1)

        elif choice == 2:
            await bot.send_message(message.from_user.id, question2_2(), reply_markup=config.question2_2_markup)
            await state.set_state(states.answering2_2)

    else:
        await message.answer(not_accepted())
        await bot.send_message(message.from_user.id, question1_1() if
                               curr_question == 1_1 else question1_2(),
                               reply_markup=config.question1_1_markup if curr_question == 1_1
                               else config.question1_2_markup)


@dp.message(StateFilter(states.answering2_1, states.answering2_2))
async def question2_handler(message: types.Message, state: FSMContext):
    curr_question = int(str(await state.get_state())[-3:])

    if message.text == answers[curr_question]:
        await message.answer(accepted())
        await bot.send_message(message.from_user.id, question3(), reply_markup=types.ReplyKeyboardRemove())
        await state.set_state(states.answering3)

    else:
        await message.answer(not_accepted())
        await bot.send_message(message.from_user.id, question2_1() if
                               curr_question == 2_1 else question2_2(),
                               reply_markup=config.question2_1_markup if curr_question == 2_1
                               else config.question2_2_markup)


@dp.message(StateFilter(states.answering3))
async def question3_handler(message: types.Message, state: FSMContext):
    curr_question = int(str(await state.get_state())[-1])

    if message.text == answers[curr_question]:
        await message.answer(end())
        await state.set_state(states.won)

    else:
        await message.answer(not_accepted())
        await bot.send_message(message.from_user.id, question3(), reply_markup=types.ReplyKeyboardRemove())


@dp.message(StateFilter(states.won))
async def question3_handler(message: types.Message, state: FSMContext):
    await message.answer(alreadly_won())


async def main():
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)

    finally:
        pass


if __name__ == "__main__":
    try:
        asyncio.run(main())

    except:
        pass

    finally:
        print('[ Turning off ]')
