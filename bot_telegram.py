from create_bot import bot, dp
from aiogram.utils import executor
from data_base import sqlite_db
from handlers import admin_side


async def on_startup(_):
    sqlite_db.sql_start()
    print('Bot Online!')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
