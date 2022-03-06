# Mega.nz to GDrive uploader

With this telegram bot you can **download files/folders from [mega.nz](https://mega.nz) and upload those files/folders to [GDrive](https://drive.google.com)**. **You can even upload telegram uploaded files to [mega.nz](https://mega.nz) or [GDrive](https://drive.google.com)**. This TG bot is **heroku** based. Now before you continue i recommend you to read [**Prerequisites**](https://github.com/whitehatjrchintu/mega-to-gdrive-bot#Prerequisites-) section and [**What this bot can do?**](https://github.com/whitehatjrchintu/mega-to-gdrive-bot#What-this-bot-can-do) section.

## Can it download files over 5GiB?

- Yes it can download. But for downloading files over 5GiB you have to wait for 5-6 hours or 10-12 hours after transfer quota exceeds. After completing 5-6 hours it will automatically download that file and after completing download it will ask you for uploading that file on GDrive. See proofs here:-

screenshot 1 | screenshot 2
--- | ---
![photo_2021-10-20_15-46-43](https://user-images.githubusercontent.com/74552895/138076069-32ead8cf-9a9e-41c9-9c92-0b5cb9211d60.jpg) | ![photo_2021-10-20_15-46-51](https://user-images.githubusercontent.com/74552895/138076094-4c87987c-46e6-4a49-8b7d-494d5c56f10f.jpg)

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
  10. So now you have saved **six** things:-
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
<details>
	<summary>
		Full Details
	</summary>

- You can operate your [mega.nz](https://mega.nz) account with this bot.
- You can list files that are uploaded on your [mega.nz](https://mega.nz) account. Just use **#ls** command.
- You can remove any file from your [mega.nz](https://mega.nz) account. Just use **#rm file_name** command.
- You can download your own [mega.nz](https://mega.nz) files. Just use **#get file_name** command.
- You can use **#other** command for executing other [mega.nz commands](https://github.com/meganz/MEGAcmd/blob/master/UserGuide.md). Such as:- **#other mv old_name.mp4 new_name.mp4**, **#other cp orignal.mp4 copied.mp4** etc.
- You can download other [mega.nz](https://mega.nz) files to telegram. Just send https://mega.nz/the_other_file_url it will send that file to your telegram.
- You can download other [mega.nz](https://mega.nz) folders to telegram. Just send https://mega.nz/the_other_file_url it will send that folder's zip file to your telegram.
- You can upload [mega.nz](https://mega.nz) uploaded files to GDrive. Just send https://mega.nz/the_other_file_url it will ask you.
- You can upload [mega.nz](https://mega.nz) uploaded folders to GDrive. Just send https://mega.nz/the_other_file_url it will ask you.
	
where to upload mega.nz file? | mega.nz folder uploaded to telegram as zip file
--- | ---
![photo_2021-10-20_15-46-43](https://user-images.githubusercontent.com/74552895/137736579-1713d5e9-c5aa-4aaf-bf25-221515cac16d.PNG) | ![photo_2021-10-20_15-46-51](https://user-images.githubusercontent.com/74552895/147825235-274d0879-490e-4e31-8626-191c4fbb7593.PNG)

- You can upload telegram uploaded files to [mega.nz](https://mega.nz). Just **forward** the telegram upload file to the bot.
- You can upload telegram uploaded files to GDrive. Just **forward** the telegram upload file to the bot.
	
	|    where to upload telegram uploaded file?    |
	|---|
	| <img width="100%" src="https://user-images.githubusercontent.com/71216298/156917678-4de7823b-77a8-468f-bb31-930312d4fb4e.PNG"> |

- You can import other [mega.nz](https://mega.nz) files and folders to your account. Use **#import https://mega.nz/the_other_file_url** command.


### Please note spaces are sensitive here so use double quotes if your file have spaces in its name. Example:- 

|correct &check;|wrong &cross;|
|---|---|
|#rm "my video.mp4"|#rm my video.mp4|
|#other mv "my video with spaces.mp4" my_video_without_spaces.mp4|#other mv my video with spaces.mp4 my_video_without_spaces.mp4|

</details>

<details>
	<summary>
		List of commands
	</summary>
	

|commands|mean|
|---|---|
|#login|for login into mega.nz|
|#ls|list files that are in your mega.nz account.|
|#import mega.nz url|directly import another mega.nz file to your account. no download no upload for mega to mega.|
|#get file_name|download your own mega.nz file and will ask you where to upload that file.|
|#rm file_name|remove file from your mega.nz account.|
|#other mega commands|execute other [mega.nz commands](https://github.com/meganz/MEGAcmd/blob/master/UserGuide.md) with the help of this command. mean operate your mega.nz account on telegram|
|url of mega.co.nz or mega.nz|this will download file from mega.nz automatically and will ask you where to upload that file. this will also download folder from mega.nz,then zip that folder and will ask you where to upload that zip file.|
	
</details>

### If you found any mistake or have any suggestion let me know i will correct/apply that.	
## Meant for educational purpose only. I am not responsible if mega or telegram block your account.
