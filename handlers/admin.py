from create_bot import bot
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data_base.sqlite_db import sql_read2

async def command_admin(message: types.Message):
    read = await sql_read2()
    for ret in read:
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\n',\
                             reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Написать', callback_data=f'')))




















def register_handlers_admin(dp: Dispatcher):
    pass