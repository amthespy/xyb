from pyrogram import Client
from telethon.sync import TelegramClient
import logging
import sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 24490919
API_HASH = "d1b3b15126c47dd4cb491553ee1db910"
BOT_TOKEN = "6654202400:AAF3Fcn9dvM4BLDWS7uiITa0omKgrql05Ps"
SESSION = "BQBLQgngPBucZBz_zQuPjTQI4O4L6BH4iBIjEoXsSn3bUGt4MUFSyJG3ygDwWqaJ71SZCH0cgfiTTIhl94bz2JGwuM1YOMxxYHEyO0WGNwglrDYxzi6LO5mvuyBA3-CxQedOermmgVs_zdL7Xu8WW8kugE8Nkl16IDtS8_1s9RjqZRpp7DHNLDEVpu8C5PVy5fqXYoDBszis5E49wXiKJMljLEuC3mI0XMUnqWgL22h4UevHshPqYFD5jQZ0qtM9-r7jywn3G74NmjJZT5-DssZ6IM15kVKxqxIKH7kjGCwh5XvgOaAdtnyVGhxHUXW9V4dH8WsIU_BA7RWjzeaBRkj3AAAAAU8LZgIA"
FORCESUB = "batchingupdates"
AUTH = 5621114370

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
userbot = Client("saverestricted", api_hash=API_HASH, api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
