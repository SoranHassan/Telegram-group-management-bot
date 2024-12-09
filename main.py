import asyncio
from configparser import ConfigParser
from telethon import TelegramClient as client
from telethon import events
from collections import deque
from database.db import *


config = ConfigParser()
config.read("./configs/config.ini")

app = client(
    'iran_ausbildung',
    config['telegram']['API_ID'],
    config['telegram']['API_HASH'],
    proxy=
    (
        config['proxy']['proxy_type'],
        config['proxy']['addr'],
        int(config['proxy']['port']),
        True,
        config['proxy']['username'],
        config['proxy']['password'],
        
           ))