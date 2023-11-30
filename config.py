from aiogram.fsm.state import StatesGroup, State
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


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
                     3: 'ответ 3'}


config = Settings()
