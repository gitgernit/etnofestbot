from aiogram.fsm.state import StatesGroup, State
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr
from funcs import question1_1_answer_1, question1_1_answer_2, \
    question1_2_answer_1, question1_2_answer_2, question2_2_answer_1, \
    question2_2_answer_2, question3_answer_1, question3_answer_2, \
    input_field, question2_1_answer_1, question2_1_answer_2


class Settings(BaseSettings):
    bot_token: SecretStr
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    class States(StatesGroup):
        answering1_1 = State()
        answering1_2 = State()
        answering2_1 = State()
        answering2_2 = State()
        answering3 = State()
        won = State()

    answers: dict = {1_1: 'ответ 1_1', 1_2: 'ответ 1_2',
                     2_1: 'ответ 2_1', 2_2: 'ответ 2_2',
                     3: 'kotik'}

    question1_1_kb: list = [
        [
            KeyboardButton(text=question1_1_answer_1()),
            KeyboardButton(text=question1_1_answer_2())
        ]
    ]
    question1_1_markup: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=question1_1_kb,
        resize_keyboard=True,
        input_field_placeholder=input_field()
    )

    question1_2_kb: list = [
        [
            KeyboardButton(text=question1_2_answer_1()),
            KeyboardButton(text=question1_2_answer_2())
        ]
    ]
    question1_2_markup: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=question1_2_kb,
        resize_keyboard=True,
        input_field_placeholder=input_field()
    )

    question2_1_kb: list = [
        [
            KeyboardButton(text=question2_1_answer_1()),
            KeyboardButton(text=question2_1_answer_2())
        ]
    ]
    question2_1_markup: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=question2_1_kb,
        resize_keyboard=True,
        input_field_placeholder=input_field()
    )

    question2_2_kb: list = [
        [
            KeyboardButton(text=question2_2_answer_1()),
            KeyboardButton(text=question2_2_answer_2())
        ]
    ]
    question2_2_markup: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=question2_2_kb,
        resize_keyboard=True,
        input_field_placeholder=input_field()
    )


config = Settings()
