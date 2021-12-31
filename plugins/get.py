from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pydrive.drive import GoogleDrive
from pyrogram import Client, filters
from pydrive.auth import GoogleAuth
from datetime import datetime
from userbot import app
import tempfile as tf
import subprocess
import traceback
import humanize
import shutil
import pytz
import time
import os

def mega_get_link_file(client: Client, message: Message):
    coming_user_id = message.from_user.id
    reply_message_id = message.message_id
    
    global coming_user_ids
    coming_user_ids = message.from_user.id
    global reply_message_ids
    reply_message_ids = message.message_id

    working_msg = app.send_message(coming_user_id, reply_to_message_id=reply_message_id, text="Working on it.",parse_mode="html")

    try:
        req = message.text

        if 'https' in req:
            mega_get = message.text
            global IST
            IST = pytz.timezone('Asia/Kolkata')

            #downloading
            download_starttime = datetime.now(IST)
            global downloading_msg
            downloading_msg = app.send_message(coming_user_id, reply_to_message_id=reply_message_id, text="Downloading please wait.",parse_mode="html")
            global download_file
            download_file = subprocess.check_output('mega-get --ignore-quota-warn ' + mega_get,shell=True)
            mega_getttt = download_file.decode()
            mega_gettt = mega_getttt.replace("Download finished: /app/./","")
            global mega_gett
            mega_gett = mega_gettt.replace("\n","")
            print(mega_gett)
            global time_taken_for_download
            time_taken_for_download = (datetime.now(IST) - download_starttime).seconds
            print('Downloaded in',time_taken_for_download,'seconds')

            file_size = os.path.getsize(mega_gett)
            less_file_size = humanize.naturalsize(file_size, binary=True)
            print(less_file_size)
            if file_size > 2147483648:
                downloading_msg.delete()
                over_msg = app.send_message(coming_user_id,f"The **{mega_gett}** has **{less_file_size}** size which is greather than **2GiB**. As per **restriction** of TG i **can't** send you file. Do you want to upload it on **gdrive**? or want to cancel this task?",reply_to_message_id=message.message_id,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Yes",callback_data="yesg"),InlineKeyboardButton("No",callback_data="noo")]]))

            if file_size < 2147483648:
                downloading_msg.delete()
                over_msg = app.send_message(coming_user_id,f"The **{mega_gett}** has **{less_file_size}** size which is less than **2GiB**. As per **restriction** of TG i **can** send you file. Do you want to upload it on **gdrive** or **tg**? or want to cancel this task?",reply_to_message_id=message.message_id,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Yes gdrive",callback_data="yesg"),InlineKeyboardButton("No tg",callback_data="noom"),InlineKeyboardButton("No",callback_data="noo")]]))

        else:
            mega_gettt = message.text
            mega_gett = mega_gettt.replace("#get ","")
            mega_get = '"{}"'.format(mega_gett)
            print(mega_get)
            IST = pytz.timezone('Asia/Kolkata')

            #downloading
            download_starttime = datetime.now(IST)
            downloading_msg = app.send_message(coming_user_id, reply_to_message_id=reply_message_id, text="Downloading please wait.",parse_mode="html")
            download_file = subprocess.check_output('mega-get --ignore-quota-warn ' + mega_get,shell=True)
            time_taken_for_download = (datetime.now(IST) - download_starttime).seconds
            print('Downloaded in',time_taken_for_download,'seconds')

            file_size = os.path.getsize(mega_gett)
            less_file_size = humanize.naturalsize(file_size, binary=True)
            print(less_file_size)
            if file_size > 2147483648:
                downloading_msg.delete()
                over_msg = app.send_message(coming_user_id,f"The **{mega_gett}** has **{less_file_size}** size which is greather than **2GiB**. As per **restriction** of TG i **can't** send you file. Do you want to upload it on **gdrive**? or want to cancel this task?",reply_to_message_id=message.message_id,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Yes",callback_data="yesg"),InlineKeyboardButton("No",callback_data="noo")]]))
                
            if file_size < 2147483648:
                downloading_msg.delete()
                over_msg = app.send_message(coming_user_id,f"The **{mega_gett}** has **{less_file_size}** size which is less than **2GiB**. As per **restriction** of TG i **can** send you file. Do you want to upload it on **gdrive** or **tg**? or want to cancel this task?",reply_to_message_id=message.message_id,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Yes gdrive",callback_data="yesg"),InlineKeyboardButton("No tg",callback_data="noom"),InlineKeyboardButton("No",callback_data="noo")]]))
                
        working_msg.delete()     
    except:
        error_var = traceback.format_exc()
        working_msg.delete()
        app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_message_id, text="Got error.",parse_mode="html")
        app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_message_id, text=error_var,parse_mode="html")

@app.on_callback_query(filters.regex(r'noom'))
def noom(client: Client, callback_query: CallbackQuery):
    coming_user_id = coming_user_ids
    reply_message_id = reply_message_ids

    noom_msg = app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_message_id, text="Working on it.",parse_mode="html")
    try:
        aa = callback_query.message.message_id
        callback_query.message.delete()
        if '.jpg' in str(download_file):
            #uploading
            orig = mega_gett
            caption = mega_gett
            photo = (open(orig,'rb'))
            upload_starttime = datetime.now(IST)
            uploading_msg = app.send_message(coming_user_id, reply_to_message_id=reply_message_id, text="Uploading please wait.",parse_mode="html")
            client.send_photo(chat_id=coming_user_id,reply_to_message_id=reply_message_id,caption=caption,photo=photo)
            time_taken_for_upload = (datetime.now(IST) - upload_starttime).seconds
            print('Uploaded in',time_taken_for_upload,'seconds')
            downloading_msg.delete()
            uploading_msg.delete()
            noom_msg.delete()
            app.send_message(coming_user_id, reply_to_message_id=reply_message_id, text="Downloaded in " + str(time_taken_for_download) + " seconds. \nUploaded in " + str(time_taken_for_upload) + " seconds.")

        elif '.jpeg' in str(download_file):
            #uploading
            orig = mega_gett
            caption = mega_gett
            photo = (open(orig,'rb'))
            upload_starttime = datetime.now(IST)
            uploading_msg = app.send_message(coming_user_id, reply_to_message_id=reply_message_id, text="Uploading please wait.",parse_mode="html")
            client.send_photo(chat_id=coming_user_id,reply_to_message_id=reply_message_id,caption=caption,photo=photo)
            time_taken_for_upload = (datetime.now(IST) - upload_starttime).seconds
            print('Uploaded in',time_taken_for_upload,'seconds')
            downloading_msg.delete()
            uploading_msg.delete()
            noom_msg.delete()
            app.send_message(coming_user_id, reply_to_message_id=reply_message_id, text="Downloaded in " + str(time_taken_for_download) + " seconds. \nUploaded in " + str(time_taken_for_upload) + " seconds.")

        elif '.png' in str(download_file):
            #uploading
            orig = mega_gett
            caption = mega_gett
            photo = (open(orig,'rb'))
            upload_starttime = datetime.now(IST)
            uploading_msg = app.send_message(coming_user_id, reply_to_message_id=reply_message_id, text="Uploading please wait.",parse_mode="html")
            client.send_photo(chat_id=coming_user_id,reply_to_message_id=reply_message_id,caption=caption,photo=photo)
            time_taken_for_upload = (datetime.now(IST) - upload_starttime).seconds
            print('Uploaded in',time_taken_for_upload,'seconds')
            downloading_msg.delete()
            uploading_msg.delete()
            noom_msg.delete()
            app.send_message(coming_user_id, reply_to_message_id=reply_message_id, text="Downloaded in " + str(time_taken_for_download) + " seconds. \nUploaded in " + str(time_taken_for_upload) + " seconds.")

        elif '.gif' in str(download_file):
            #uploading
            orig = mega_gett
            caption = mega_gett
            animation = (open(orig,'rb'))
            upload_starttime = datetime.now(IST)
            uploading_msg = app.send_message(coming_user_id, reply_to_message_id=reply_message_id, text="Uploading please wait.",parse_mode="html")
            client.send_animation(chat_id=coming_user_id,reply_to_message_id=reply_message_id,caption=caption,animation=animation)
            time_taken_for_upload = (datetime.now(IST) - upload_starttime).seconds
            print('Uploaded in',time_taken_for_upload,'seconds')
            downloading_msg.delete()
            uploading_msg.delete()
            noom_msg.delete()
            app.send_message(coming_user_id, reply_to_message_id=reply_message_id, text="Downloaded in " + str(time_taken_for_download) + " seconds. \nUploaded in " + str(time_taken_for_upload) + " seconds.")

        elif '.mp4' in str(download_file):
            #uploading
            orig = mega_gett
            caption = mega_gett
            video = (open(orig,'rb'))
            upload_starttime = datetime.now(IST)
            uploading_msg = app.send_message(coming_user_id, reply_to_message_id=reply_message_id, text="Uploading please wait.",parse_mode="html")
            client.send_video(chat_id=coming_user_id,reply_to_message_id=reply_message_id,caption=caption,video=video)
            time_taken_for_upload = (datetime.now(IST) - upload_starttime).seconds
            print('Uploaded in',time_taken_for_upload,'seconds')
            downloading_msg.delete()
            uploading_msg.delete()
            noom_msg.delete()
            app.send_message(coming_user_id, reply_to_message_id=reply_message_id, text="Downloaded in " + str(time_taken_for_download) + " seconds. \nUploaded in " + str(time_taken_for_upload) + " seconds.")

        elif '.mkv' in str(download_file):
            #uploading
            orig = mega_gett
            caption = mega_gett
            video = (open(orig,'rb'))
            upload_starttime = datetime.now(IST)
            uploading_msg = app.send_message(coming_user_id, reply_to_message_id=reply_message_id, text="Uploading please wait.",parse_mode="html")
            client.send_video(chat_id=coming_user_id,reply_to_message_id=reply_message_id,caption=caption,video=video)
            time_taken_for_upload = (datetime.now(IST) - upload_starttime).seconds
            print('Uploaded in',time_taken_for_upload,'seconds')
            downloading_msg.delete()
            uploading_msg.delete()
            noom_msg.delete()
            app.send_message(coming_user_id, reply_to_message_id=reply_message_id, text="Downloaded in " + str(time_taken_for_download) + " seconds. \nUploaded in " + str(time_taken_for_upload) + " seconds.")
  
        elif '.webm' in str(download_file):
            #uploading
            orig = mega_gett
            caption = mega_gett
            video = (open(orig,'rb'))
            upload_starttime = datetime.now(IST)
            uploading_msg = app.send_message(coming_user_id, reply_to_message_id=reply_message_id, text="Uploading please wait.",parse_mode="html")
            client.send_video(chat_id=coming_user_id,reply_to_message_id=reply_message_id,caption=caption,video=video)
            time_taken_for_upload = (datetime.now(IST) - upload_starttime).seconds
            print('Uploaded in',time_taken_for_upload,'seconds')
            downloading_msg.delete()
            uploading_msg.delete()
            noom_msg.delete()
            app.send_message(coming_user_id, reply_to_message_id=reply_message_id, text="Downloaded in " + str(time_taken_for_download) + " seconds. \nUploaded in " + str(time_taken_for_upload) + " seconds.")

        elif '.mp3' in str(download_file):
            #uploading
            orig = mega_gett
            caption = mega_gett
            audio = (open(orig,'rb'))
            upload_starttime = datetime.now(IST)
            uploading_msg = app.send_message(coming_user_id, reply_to_message_id=reply_message_id, text="Uploading please wait.",parse_mode="html")
            client.send_audio(chat_id=coming_user_id,reply_to_message_id=reply_message_id,caption=caption,audio=audio)
            time_taken_for_upload = (datetime.now(IST) - upload_starttime).seconds
            print('Uploaded in',time_taken_for_upload,'seconds')
            downloading_msg.delete()
            uploading_msg.delete()
            noom_msg.delete()
            app.send_message(coming_user_id, reply_to_message_id=reply_message_id, text="Downloaded in " + str(time_taken_for_download) + " seconds. \nUploaded in " + str(time_taken_for_upload) + " seconds.")

        else:
            #uploading
            orig = mega_gett
            caption = mega_gett
            check_dir_t = os.path.isdir(orig)
            if check_dir_t == True:
                folder_to_zip = subprocess.check_output("zip -r " + orig + ".zip " + orig,shell=True) #zip -r aa.zip aaaaaaaaa
                origg = orig + ".zip"
                document = (open(origg,'rb'))
                upload_starttime = datetime.now(IST)
                uploading_msg = app.send_message(coming_user_id, reply_to_message_id=reply_message_id, text="Uploading please wait.",parse_mode="html")
                client.send_document(chat_id=coming_user_id,reply_to_message_id=reply_message_id,caption=caption,document=document)
                time_taken_for_upload = (datetime.now(IST) - upload_starttime).seconds
                print('Uploaded in',time_taken_for_upload,'seconds')
                downloading_msg.delete()
                uploading_msg.delete()
                noom_msg.delete()
                app.send_message(coming_user_id, reply_to_message_id=reply_message_id, text="Downloaded in " + str(time_taken_for_download) + " seconds. \nUploaded in " + str(time_taken_for_upload) + " seconds.")
            else:
                document = (open(orig,'rb'))
                upload_starttime = datetime.now(IST)
                uploading_msg = app.send_message(coming_user_id, reply_to_message_id=reply_message_id, text="Uploading please wait.",parse_mode="html")
                client.send_document(chat_id=coming_user_id,reply_to_message_id=reply_message_id,caption=caption,document=document)
                time_taken_for_upload = (datetime.now(IST) - upload_starttime).seconds
                print('Uploaded in',time_taken_for_upload,'seconds')
                downloading_msg.delete()
                uploading_msg.delete()
                noom_msg.delete()
                app.send_message(coming_user_id, reply_to_message_id=reply_message_id, text="Downloaded in " + str(time_taken_for_download) + " seconds. \nUploaded in " + str(time_taken_for_upload) + " seconds.")

        noom_msg.delete()

    except:
        error_var = traceback.format_exc()
        noom_msg.delete()
        app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_message_id, text="Got error.",parse_mode="html")
        app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_message_id, text=error_var,parse_mode="html")

@app.on_callback_query(filters.regex(r'yesg'))
def yesg_gdrive(client: Client, callback_query: CallbackQuery):
    coming_user_id = coming_user_ids
    reply_message_id = reply_message_ids

    yesg_msg = app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_message_id, text="Working on it.",parse_mode="html")
    try:
        aa = callback_query.message.message_id
        callback_query.message.delete()
        if mega_gett is None:
            #login        
            gauth = GoogleAuth()
            gauth.LoadCredentialsFile("mycreds.txt")
            drive = GoogleDrive(gauth)

            #uploading
            IST = pytz.timezone('Asia/Kolkata')
            uploading_msg = app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_message_id, text="Uploading {mega_gett} to Gdrive please wait.",parse_mode="html")
            orig = download_file
            upload_starttime = datetime.now(IST)
            file1 = drive.CreateFile()
            file1.SetContentFile(orig)
            file1.Upload()
            link=file1['alternateLink']
            time_taken_for_upload = (datetime.now(IST) - upload_starttime).seconds
            print('Uploaded in',time_taken_for_upload,'seconds')
        
            #sending url
            uploading_msg.delete()
            app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_message_id, text=link)
            app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_message_id, text="Downloaded in " + str(time_taken_for_download) + " seconds. \nUploaded in " + str(time_taken_for_upload) + " seconds.")
            print(link)

        elif mega_gett is not None:
            #login        
            gauth = GoogleAuth()
            gauth.LoadCredentialsFile("mycreds.txt")
            drive = GoogleDrive(gauth)

            #uploading
            IST = pytz.timezone('Asia/Kolkata')
            uploading_msg = app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_message_id, text="Uploading " + '<b>' + mega_gett + '</b>' + " to Gdrive please wait.",parse_mode="html")
            orig = mega_gett
            check_dir = os.path.isdir(orig)
            if check_dir == True:
                upload_starttime = datetime.now(IST)
                folder_to_zip = subprocess.check_output("zip -r " + orig + ".zip " + orig,shell=True)
                file1 = drive.CreateFile()
                origg = orig + ".zip"
                file1.SetContentFile(origg)
                file1.Upload()
                link=file1['alternateLink']
                time_taken_for_upload = (datetime.now(IST) - upload_starttime).seconds
                print('Uploaded in',time_taken_for_upload,'seconds')
            else:
                upload_starttime = datetime.now(IST)
                file1 = drive.CreateFile()
                file1.SetContentFile(orig)
                file1.Upload()
                link=file1['alternateLink']
                time_taken_for_upload = (datetime.now(IST) - upload_starttime).seconds
                print('Uploaded in',time_taken_for_upload,'seconds')
        
            #sending url
            uploading_msg.delete()
            app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_message_id, text=link)
            app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_message_id, text="Downloaded in " + str(time_taken_for_download) + " seconds. \nUploaded in " + str(time_taken_for_upload) + " seconds.")
            print(link)
    
        yesg_msg.delete()
        
    except:
        error_var = traceback.format_exc()
        yesg_msg.delete()
        app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_message_id, text="Got error.",parse_mode="html")
        app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_message_id, text=error_var,parse_mode="html")

@app.on_callback_query(filters.regex(r'noo'))
def no_noo(client: Client, callback_query: CallbackQuery):
    coming_user_id = coming_user_ids
    #reply_message_id = reply_message_ids

    try:
        cancelledd_msg = app.send_message(chat_id=coming_user_ids, text="Upload cancelled.",parse_mode="html")
        callback_query.message.delete()
    except:
        error_var = traceback.format_exc()
        cancelledd_msg.delete()
        app.send_message(chat_id=coming_user_ids, text="Got error.",parse_mode="html")
        app.send_message(chat_id=coming_user_ids, text=error_var,parse_mode="html")
