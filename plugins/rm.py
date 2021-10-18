from pyrogram.types import Message
from pyrogram import Client
from datetime import datetime
from userbot import app
import subprocess
import traceback
import pytz
import os

def mega_rm_file(client, message):
    coming_user_id = message.from_user.id
    reply_message_id = message.message_id

    msg = app.send_message(coming_user_id, reply_to_message_id=reply_message_id, text="Working on it.",parse_mode="html")

    try:
        mega_rmmm = message.text
        mega_rmm = mega_rmmm.replace("#rm ","")
        mega_rm = '"{}"'.format(mega_rmm)
        rm_file = subprocess.check_output('mega-rm -f ' + mega_rm,shell=True)
        rm_msg = app.send_message(coming_user_id, reply_to_message_id=reply_message_id, text="file removed.",parse_mode="html")
        msg.delete()

    except:
        error_var = traceback.format_exc()
        msg.delete()
        app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_message_id, text="Got error.",parse_mode="html")
        app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_message_id, text=error_var,parse_mode="html")
