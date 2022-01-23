from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery
from plugins import *
from userbot import app
from os import environ

my_user_id = environ["2051438564"]

@app.on_message(filters.command(["start"]))
def start(client: Client, message: Message):
    msg = app.send_message(message.from_user.id,"Welcome",reply_to_message_id=message.message_id)

@app.on_message(filters.regex(r'#other'))
def megaother(client: Client, message: Message):
    mega_other(client, message)

@app.on_message(filters.regex(r'#login'))
def megalogin(client: Client, message: Message):
    mega_login(client, message)

@app.on_message(filters.regex(r'#rm'))
def mega_rm(client: Client, message: Message):
    mega_rm_file(client, message)

@app.on_message(filters.regex(r'#import'))
def mega_import(client: Client, message: Message):
    mega_import_file(client, message)

@app.on_message(filters.regex(r'#get|mega.co.nz|mega.nz'))
def mega_get(client: Client, message: Message):
    mega_get_link_file(client, message)
        
@app.on_message(filters.regex(r'#ls'))
def megals(client: Client, message: Message):
    mega_ls(client, message)

@app.on_message(filters.audio | filters.document | filters.photo | filters.video)
def gdrive_mega(client: Client, message: Message):
    gdrive_mega1(client, message)
    def gdrive_megaa(client: Client, callback_query: CallbackQuery):
        gdrive_answer(client, callback_query)
        mega_answer(client, callback_query)

app.run()
