from pyrogram.types import Message
from pyrogram import Client
from datetime import datetime
from userbot import app
from os import environ
import subprocess
import traceback
import pytz
import os

def mega_login(client: Client, message: Message):
    coming_user_id = message.from_user.id
    reply_message_id = message.message_id

    try:
        login_msg = app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_message_id, text="Trying to login.",parse_mode="html")
        login_msg_id = login_msg.message_id
        meganz_email = environ["MEGA.NZ_EMAIL"]
        meganz_password = environ["MEGA.NZ_PASSWORD"]
        login_msg_edit = app.edit_message_text(chat_id=coming_user_id, message_id=login_msg_id, text="Logged.",parse_mode="html")
        mega_login = subprocess.check_output('mega-login' + " " + meganz_email + " " +meganz_password,shell=True)
    except:
        error_var = traceback.format_exc()
        login_msg_edit.delete()
        if not 'exit status 54' in error_var:
            app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_message_id, text="Got error.",parse_mode="html")
            app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_message_id, text=error_var,parse_mode="html")
        else:
            app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_message_id, text="Already logged in.",parse_mode="html")
