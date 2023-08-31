from create_bot import dp
from aiogram.utils import executor
from aiogram import types
from handlers import admin, client, other
from data_base import sqlite_db

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)



async def on_startup(_):
    sqlite_db.sql_start()
    print('Бот вышел на охоту')




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)