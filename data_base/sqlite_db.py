import sqlite3
from aiogram import types

def sql_start():
    global base, cur
    base = sqlite3.connect('list_client.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute('CREATE TABLE IF NOT EXISTS list_primary(userid TEXT PRIMARY KEY, username TEXT, firstname TEXT, fullname TEXT)')
    base.commit()

async def sql_add_client(message: types.Message):
    cur.execute('INSERT INTO list_primary VALUES (?, ?, ?, ?)', (message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.full_name))
    base.commit()

async def sql_check(userid):
    pass

async def sql_read(message: types.Message):
    cur.execute('SELECT userid FROM menu')

async def sql_read2(message: types.Message):
    cur.execute('SELECT * FROM menu').fetchall()