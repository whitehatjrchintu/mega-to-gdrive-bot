from pyrogram.types import Message
from pyrogram import Client
from datetime import datetime
from userbot import app
import subprocess
import traceback
import pytz
import os

def mega_ls(client: Client, message: Message):
    coming_user_id = message.from_user.id
    reply_message_id = message.message_id
    
    try:
        msg = app.send_message(coming_user_id,reply_to_message_id=reply_message_id, text="Doing.")
        ls = subprocess.check_output('mega-ls',shell=True)
        ls_decode = ls.decode('utf-8')
        ls_msg = app.send_message(coming_user_id,reply_to_message_id=reply_message_id, text=ls_decode)
        msg.delete()
    except:
        error_var = traceback.format_exc()
        msg.delete()
        app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_message_id, text="Got error.",parse_mode="html")
        app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_message_id, text=error_var,parse_mode="html")
