from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from decouple import config

TGBOTAPI_TOKEN = config("TGBOTAPI_TOKEN")

bot = Bot(token=TGBOTAPI_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
