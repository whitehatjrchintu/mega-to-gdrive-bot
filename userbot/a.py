from pyrogram import Client
from os import environ

api_id = int(environ["API_ID"])
api_hash = environ["API_HASH"]
bot_token = environ["BOT_TOKEN"]
app = Client(":memory:", api_id, api_hash, bot_token=bot_token)
