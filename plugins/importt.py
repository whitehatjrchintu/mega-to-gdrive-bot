from pyrogram.types import Message
from pyrogram import Client
from datetime import datetime
from userbot import app
import subprocess
import traceback
import pytz
import os

def mega_import_file(client: Client, message: Message):
    coming_user_id = message.from_user.id
    reply_message_id = message.message_id

    msg = app.send_message(coming_user_id, reply_to_message_id=reply_message_id, text="Working on it.",parse_mode="html")

    try:
        mega_importtt = message.text
        mega_importt = mega_importtt.replace("#import ","")
        mega_import = '"{}"'.format(mega_importt)
        download_file = subprocess.check_output('mega-import ' + mega_import,shell=True)
        import_msg_decode = download_file.decode()
        import_msg = app.send_message(coming_user_id, reply_to_message_id=reply_message_id, text=import_msg_decode,parse_mode="html")
        msg.delete()

    except:
        error_var = traceback.format_exc()
        msg.delete()
        app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_message_id, text="Got error.",parse_mode="html")
        app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_message_id, text=error_var,parse_mode="html")
