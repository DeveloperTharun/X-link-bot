# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "15917107"))
API_HASH = os.environ.get("API_HASH", "8197e7638d58c92ae2504adba7c62117")
BOT_TOKEN = os.environ.get("BOT_TOKEN", " 6022334675:AAF2BTphZXxvk05zIz4JHkCAfuhSB141w_8")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("1503578112")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "x_linkz")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://appuanju1328:<appuvava13>@cluster0.zkbgspx.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("owner Id", "1503578112")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001956624005")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "*xlinkz) # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
