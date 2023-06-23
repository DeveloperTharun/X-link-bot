# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "8754146"))
API_HASH = os.environ.get("API_HASH", "8b56a6989f6d04f6f4fe78133ade02fd")
BOT_TOKEN = os.environ.get("BOT_TOKEN", " 6282735009:AAEdT0iNTtCHqusbr15a-dnFHbS7uHBE_dw")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("5669934860")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "x_linkz")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://SkMedia:Tharunraj1828@cluster0.vbdxs.mongodb.net/myFirstDatabase?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("owner Id", "5669934860")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001691155744) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "*Rapid_Bots) # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
