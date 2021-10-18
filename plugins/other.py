from pyrogram.types import Message
from pyrogram import Client
from datetime import datetime
from userbot import app
import subprocess
import traceback
import pytz
import os

def mega_other(client, message):
    coming_user_id = message.from_user.id
    reply_message_id = message.message_id

    msg = app.send_message(coming_user_id, reply_to_message_id=reply_message_id, text="Working on it.",parse_mode="html")

    try:
        mega_otherrr = message.text
        mega_otherr = mega_otherrr.replace("#other ","")
        #mega_other = '"{}"'.format(mega_otherr)
        other_file = subprocess.check_output('mega-' + mega_otherr,shell=True)
        print(other_file)
        other_msg_decode = other_file.decode()
        other_msg = app.send_message(coming_user_id, reply_to_message_id=reply_message_id, text=other_msg_decode,parse_mode="html")
        msg.delete()
        
    except:
        error_var = traceback.format_exc()
        msg.delete()
        if not 'MESSAGE_EMPTY' in error_var:
            app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_message_id, text="Got error.",parse_mode="html")
            app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_message_id, text=error_var,parse_mode="html")
        else:
            None
