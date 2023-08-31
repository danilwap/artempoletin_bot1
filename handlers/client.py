from create_bot import bot
from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from data_base.sqlite_db import sql_add_client, sql_read, sql_check

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    age = State()
    maritul_status = State()
    request = State()
    divides = State()
    about_us = State()


kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

async def command_start(message: types.Message):
    if sql_check(message.from_user.id):
        await sql_add_client(message)
    await message.answer('Описание группы', reply_markup=kb_client.add(KeyboardButton('Заполнить анкету на вступление')))

async def start_anket(message: types.Message):
    await FSMAdmin.photo.set()
    await message.answer('Загрузи фото')

async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Ок')

async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.answer('Теперь введите Имя')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer('Теперь введите Ваш возраст')


async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
    await FSMAdmin.next()
    await message.answer('Теперь выберите Ваше семейное положение')


async def load_maritul_status(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['maritul_status'] = message.text
    await FSMAdmin.next()
    await message.answer('Какой у Вас запрос?')


async def load_request(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['request'] = message.text
    await FSMAdmin.next()
    await message.answer('Чем Вы можете поделиться?')


async def load_divides(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['divides'] = message.text
    await FSMAdmin.next()
    await message.answer('Теперь расскажите о себе в свободной форме')

async def load_about_us(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['about_us'] = message.text
        await message.answer(data)
    await FSMAdmin.finish()
    await message.answer('Анкета заполнена')


async def load_divides(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['divides'] = message.text
        await message.answer_photo(data['photo'], caption=f'Имя: {data["name"]}')
    await state.finish()
    await message.answer('Анкета заполнена')

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(start_anket, Text(equals='Заполнить анкету на вступление', ignore_case=True))
    dp.register_message_handler(cancel_handler, state='*', commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state='*')
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_maritul_status, state=FSMAdmin.maritul_status)
    dp.register_message_handler(load_request, state=FSMAdmin.request)
    dp.register_message_handler(load_divides, state=FSMAdmin.divides)
    dp.register_message_handler(load_about_us, state=FSMAdmin.about_us)









