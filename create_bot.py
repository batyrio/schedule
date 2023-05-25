from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token='6111410203:AAGJue-9SajYFOtRHD6GX10s_PhYb18mSwU')

dp = Dispatcher(bot, storage=storage)