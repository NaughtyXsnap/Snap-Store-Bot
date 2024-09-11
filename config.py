import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", "24440741"))
API_HASH = os.environ.get("API_HASH", "eda231ff278ef43dc36164de83ee8fd6")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002440776976"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6307223516"))
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://haryanvivibe0077:Cr0VrfWiVuivnStU@cluster0.ivjjz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#Shortner (token system) 

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "https://modijiurl.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "c0085d50d85c0ead2158e143bd69b4c5015b57f9")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID", "https://t.me/Tutorial_modijiurl/3") 

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "1"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}, I'm Providing Best Snaps for @NaughtyX11 ⚡️.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6307223516").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}\n\n<b>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @NaughtyX11</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "sᴏʀʀʏ ! ɪ ᴄᴀɴ'ᴛ ʀᴇᴘʟʏ ʏᴏᴜʀ,ᴍᴇssᴀɢᴇ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴛᴀʟᴋ ᴘʟᴇᴀsᴇ ᴄᴏɴᴛᴇᴄᴛ NᴀᴜɢʜᴛʏX ᴀssɪsᴛᴀɴᴛ ʙᴏᴛ. Tʜᴀɴᴋs❣️!!"

ADMINS.append(OWNER_ID)
ADMINS.append(6307223516)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
