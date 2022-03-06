from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pydrive.drive import GoogleDrive
from pyrogram import Client, filters
from pydrive.auth import GoogleAuth
from datetime import datetime
from userbot import app
import subprocess
import traceback
import shutil
import pytz

def gdrive_mega1(client: Client, message: Message):
    global coming_user_id
    coming_user_id = message.from_user.id
    
    global reply_to_message_ids
    reply_to_message_ids = message.message_id

    #getting file name
    global file_name
    file_name = None
    if message.media:
        if message.audio:
            file_name = message.audio.file_name
        elif message.document:
            file_name = message.document.file_name
        elif message.video:
            file_name = message.video.file_name

    what_msg = app.send_message(coming_user_id,f"Where you want to upload {file_name}?",reply_to_message_id=message.message_id,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("gdrive",callback_data="gdrive"),InlineKeyboardButton("mega",callback_data="mega")]]))
    
@app.on_callback_query(filters.regex(r'gdrive'))
def gdrive_answer(client: Client, callback_query: CallbackQuery):
    #getting file id
    file_id = None
    if callback_query.message.reply_to_message.media:
        if callback_query.message.reply_to_message.audio:
            file_id = callback_query.message.reply_to_message.audio.file_id
        elif callback_query.message.reply_to_message.document:
            file_id = callback_query.message.reply_to_message.document.file_id
        elif callback_query.message.reply_to_message.photo:
            file_id = callback_query.message.reply_to_message.photo.file_id
        elif callback_query.message.reply_to_message.video:
            file_id = callback_query.message.reply_to_message.video.file_id
    msg = app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_to_message_ids, text="Working on it.",parse_mode="html")
    try:
        call_data = file_id
        print(call_data)
        aa = callback_query.message.message_id
        callback_query.message.delete()
        if file_name is None:
            #login        
            gauth = GoogleAuth()
            gauth.LoadCredentialsFile("mycreds.txt")
            drive = GoogleDrive(gauth)

            #downloading
            IST = pytz.timezone('Asia/Kolkata')
            download_starttime = datetime.now(IST)
            downloading_msg = app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_to_message_ids, text="Downloading image please wait.",parse_mode="html")
            download_file = app.download_media(call_data)
            print(download_file)
            time_taken_for_download = (datetime.now(IST) - download_starttime).seconds
            print('Downloaded in',time_taken_for_download,'seconds')

            #uploading
            uploading_msg = app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_to_message_ids, text="Uploading image to Gdrive please wait.",parse_mode="html")
            orig = download_file
            upload_starttime = datetime.now(IST)
            file1 = drive.CreateFile()
            file1.SetContentFile(orig)
            file1.Upload()
            link=file1['alternateLink']
            time_taken_for_upload = (datetime.now(IST) - upload_starttime).seconds
            print('Uploaded in',time_taken_for_upload,'seconds')
        
            #sending url
            downloading_msg.delete()
            uploading_msg.delete()
            app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_to_message_ids, text=link)
            app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_to_message_ids, text="Downloaded in " + str(time_taken_for_download) + " seconds. \nUploaded in " + str(time_taken_for_upload) + " seconds.")
            print(link)

        elif file_name is not None:
            #login        
            gauth = GoogleAuth()
            gauth.LoadCredentialsFile("mycreds.txt")
            drive = GoogleDrive(gauth)

            #downloading
            IST = pytz.timezone('Asia/Kolkata')
            download_starttime = datetime.now(IST)
            downloading_msg = app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_to_message_ids, text="Downloading " + '<b>' + file_name + '</b>' + " please wait.",parse_mode="html")
            download_file = app.download_media(call_data)
            print(download_file)
            time_taken_for_download = (datetime.now(IST) - download_starttime).seconds
            print('Downloaded in',time_taken_for_download,'seconds')

            #uploading
            uploading_msg = app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_to_message_ids, text="Uploading " + '<b>' + file_name + '</b>' + " to Gdrive please wait.",parse_mode="html")
            orig = shutil.copy(download_file, file_name)
            upload_starttime = datetime.now(IST)
            file1 = drive.CreateFile()
            file1.SetContentFile(orig)
            file1.Upload()
            link=file1['alternateLink']
            time_taken_for_upload = (datetime.now(IST) - upload_starttime).seconds
            print('Uploaded in',time_taken_for_upload,'seconds')
        
            #sending url
            downloading_msg.delete()
            uploading_msg.delete()
            app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_to_message_ids, text=link)
            app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_to_message_ids, text="Downloaded in " + str(time_taken_for_download) + " seconds. \nUploaded in " + str(time_taken_for_upload) + " seconds.")
            print(link)
            
        msg.delete()
    except:
        error_var = traceback.format_exc()
        msg.delete()
        app.send_message(chat_id=coming_user_id, text="Got error.",parse_mode="html")
        app.send_message(chat_id=coming_user_id, text=error_var,parse_mode="html")

@app.on_callback_query(filters.regex(r'mega')) 
def mega_answer(client: Client, callback_query: CallbackQuery):
    #getting file id
    file_id = None
    if callback_query.message.reply_to_message.media:
        if callback_query.message.reply_to_message.audio:
            file_id = callback_query.message.reply_to_message.audio.file_id
        elif callback_query.message.reply_to_message.document:
            file_id = callback_query.message.reply_to_message.document.file_id
        elif callback_query.message.reply_to_message.photo:
            file_id = callback_query.message.reply_to_message.photo.file_id
        elif callback_query.message.reply_to_message.video:
            file_id = callback_query.message.reply_to_message.video.file_id
    msg = app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_to_message_ids, text="Working on it.",parse_mode="html")
    try:
        call_data = file_id
        print(call_data)
        aa = callback_query.message.message_id
        callback_query.message.delete()   
        if file_name is None:
            #downloading
            IST = pytz.timezone('Asia/Kolkata')
            download_starttime = datetime.now(IST)
            downloading_msg = app.send_message(coming_user_id, reply_to_message_id=reply_to_message_ids, text="Downloading image please wait.",parse_mode="html")
            download_file = app.download_media(call_data)
            print(download_file)
            time_taken_for_download = (datetime.now(IST) - download_starttime).seconds
            print('Downloaded in',time_taken_for_download,'seconds')

            #uploading
            uploading_msg = app.send_message(coming_user_id, reply_to_message_id=reply_to_message_ids, text="Uploading image to mega please wait.",parse_mode="html")
            orig = download_file
            upload_starttime = datetime.now(IST)
            upload_file = subprocess.check_output('mega-put --ignore-quota-warn ' + orig,shell=True)
            import_msg_decode = upload_file.decode()
            time_taken_for_upload = (datetime.now(IST) - upload_starttime).seconds
            print('Uploaded in',time_taken_for_upload,'seconds')
    
            #sending message
            downloading_msg.delete()
            uploading_msg.delete()
            app.send_message(coming_user_id, reply_to_message_id=reply_to_message_ids, text=str(import_msg_decode) + "\n" + "Downloaded in " + str(time_taken_for_download) + " seconds. \nUploaded in " + str(time_taken_for_upload) + " seconds.")

        elif file_name is not None:
            #downloading
            IST = pytz.timezone('Asia/Kolkata')
            download_starttime = datetime.now(IST)
            downloading_msg = app.send_message(coming_user_id, reply_to_message_id=reply_to_message_ids, text="Downloading " + '<b>' + file_name + '</b>' + " please wait.",parse_mode="html")
            download_file = app.download_media(call_data)
            print(download_file)
            time_taken_for_download = (datetime.now(IST) - download_starttime).seconds
            print('Downloaded in',time_taken_for_download,'seconds')

            #uploading
            uploading_msg = app.send_message(coming_user_id, reply_to_message_id=reply_to_message_ids, text="Uploading " + '<b>' + file_name + '</b>' + " to mega please wait.",parse_mode="html")
            orig = shutil.copy(download_file, file_name)
            upload_starttime = datetime.now(IST)
            upload_file = subprocess.check_output('mega-put --ignore-quota-warn ' + orig,shell=True)
            import_msg_decode = upload_file.decode()
            time_taken_for_upload = (datetime.now(IST) - upload_starttime).seconds
            print('Uploaded in',time_taken_for_upload,'seconds')
    
            #sending message
            downloading_msg.delete()
            uploading_msg.delete()
            app.send_message(coming_user_id, reply_to_message_id=reply_to_message_ids, text=str(import_msg_decode) + "\n" + "Downloaded in " + str(time_taken_for_download) + " seconds. \nUploaded in " + str(time_taken_for_upload) + " seconds.")
 
        msg.delete()
    except:
        error_var = traceback.format_exc()
        msg.delete()
        app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_to_message_ids, text="Got error.",parse_mode="html")
        app.send_message(chat_id=coming_user_id, reply_to_message_id=reply_to_message_ids, text=error_var,parse_mode="html")
