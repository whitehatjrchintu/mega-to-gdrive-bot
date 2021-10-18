# Mega.nz to GDrive uploader

With this telegram bot you can **download files from [mega.nz](https://mega.nz) and upload those files or telegram uploaded files to [GDrive](https://drive.google.com)**. **You can even upload telegram uploaded files to [mega.nz](https://mega.nz)**. This TG bot is **heroku** based. Now before you continue i recommend you to read [**Prerequisites**](https://github.com/whitehatjrchintu/mega-to-gdrive-bot#Prerequisites-) section.

## Prerequisites:-
<details>
<summary>
  :information_source: Important information.
</summary>

  1. Create account on [GitHub](https://www.github.com) (if you haven't).
  2. Create account on [mega.nz](https://mega.nz) (if you haven't).
  3. Create account on [Heroku](https://dashboard.heroku.com) (if you haven't).
  4. Create account on [Telegram](https://web.telegram.org) (if you haven't).
  5. Create account on [Gmail](https://mail.google.com) (if you haven't for only this script).
  6. Go to [my.telegram.org/auth](https://my.telegram.org/auth), login and create app. Check [how to create app on telegram](https://core.telegram.org/api/obtaining_api_id). Now save api_id and api_hash which you got from [my.telegram.org/auth](https://my.telegram.org/auth).
  7. Create a telegram bot by using [Bot Father](https://t.me/botfather). Check [how to create bot in telegram](https://core.telegram.org/bots#3-how-do-i-create-a-bot). [Bot Father](https://t.me/botfather) will give you bot token save that token.
  8. Create **Google Drive API key** from your above created gmail account. Read [this article's](https://medium.com/analytics-vidhya/how-to-connect-google-drive-to-python-using-pydrive-9681b2a14f20) **Getting Your API Key** and **Saving Your Credentials** section for getting two file named **client_secrets.json** and **mycreds.txt**.
  9. Search **@chatid_echo_bot** in telegram (This bot is not mine. You can google how to get chat id in telegram.) and click start this will give you your **telegram user_id**.
  10. So now you have saved **five** things:-
		- api_id
		- api_hash
		- bot_token
		- client_secrets.json
		- mycreds.txt
		- telegram user_id

</details>

## How to use?
<details>
  <summary>
    Steps to use.
  </summary>
	
#### Step 1:
- Just git clone this repository.

   `git clone https://github.com/whitehatjrchintu/mega-to-gdrive-bot.git`
   
   `cd mega-to-gdrive-bot`

- Or download this [repository](https://github.com/whitehatjrchintu/mega-to-gdrive-bot/archive/main.zip) as zip.
#### Step 2:
- After cd or unzip upload **client_secrets.json** and **mycreds.txt** files, which we download in **step 8** of **Prerequisites**, in that folder.
#### Step 3:
- Now create repository (i will recommend to create private repository.) in your github account and upload all files and folders.
#### Step 4:
- Copy your github repository's link and paste after **?template=** in this link `https://www.heroku.com/deploy/?template=`. Like this:-

   `https://www.heroku.com/deploy/?template=https://github.com/whitehatjrchintu/mega-to-gdrive-bot`
#### Step 5:
- Now enter App name in **app_name** and **api_id**, **api_hash**, **bot_token**, **mega.nz email**, **mega.nz password** and your **telegram user_id** which you saved in above steps, in **respective** asked field. Then click **Deploy app**.
#### Step 6:
- Finally go to your bot, click start button, send **#login** command and this will login into [mega.nz](https://mega.nz).
</details>

## What this bot can do?

- You can operate your [mega.nz](https://mega.nz) account with this bot.
- You can download other [mega.nz](https://mega.nz) files to telegram. Just send https://mega.nz/the_other_file_url it will send that file to your telegram.
- You can upload [mega.nz](https://mega.nz) uploaded files to GDrive. Just send https://mega.nz/the_other_file_url it will ask you.

	![link](https://user-images.githubusercontent.com/74552895/137736579-1713d5e9-c5aa-4aaf-bf25-221515cac16d.PNG)

- You can upload telegram uploaded files to [mega.nz](https://mega.nz). Just **forward** the telegram upload file to the bot.
- You can upload telegram uploaded files to GDrive. Just **forward** the telegram upload file to the bot.

	![forward](https://user-images.githubusercontent.com/74552895/137737105-a09261c4-89e0-4b1d-807c-46180cfd8fb8.PNG)

- You can import other [mega.nz](https://mega.nz) files to your account. Use **#import https://mega.nz/the_other_file_url** command.
- You can list files that are uploaded on your [mega.nz](https://mega.nz) account. Just use **#ls** command.
- You can remove any file from your [mega.nz](https://mega.nz) account. Just use **#remove file_name** command.
- You can download your own [mega.nz](https://mega.nz) files. Just use **#get file_name** command.
- You can use **#other** command for executing other [mega.nz commands](https://github.com/meganz/MEGAcmd/blob/master/UserGuide.md).

### If you found any mistake or have any suggestion let me know i will correct/apply that.	
## Meant for educational purpose only. I am not responsible if mega or telegram block your account.
