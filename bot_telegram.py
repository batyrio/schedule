from create_bot import bot, dp
from aiogram.utils import executor


async def on_startup():
    print('Bot Online!')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
