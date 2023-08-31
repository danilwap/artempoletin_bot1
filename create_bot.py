from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()

bot = Bot(token='6088392533:AAHDauOyWs_C55EQhUtxFT7M-qrbIDzfsiU')
dp = Dispatcher(bot, storage=storage)