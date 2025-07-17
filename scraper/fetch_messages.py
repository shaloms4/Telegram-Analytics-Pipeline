from telethon.sync import TelegramClient
from telethon.errors import FloodWaitError
import os
from dotenv import load_dotenv
from scraper.log_utils import get_logger

load_dotenv()
logger = get_logger("fetch_messages")

api_id = os.getenv("TELEGRAM_API_ID")
api_hash = os.getenv("TELEGRAM_API_HASH")

client = TelegramClient('anon', api_id, api_hash)

async def fetch_channel_messages(channel_username, limit=200):
    try:
        await client.start()
        messages = []
        async for msg in client.iter_messages(channel_username, limit=limit):
            messages.append(msg.to_dict())
        return messages
    except FloodWaitError as e:
        logger.error(f"Rate limited while fetching {channel_username}: wait {e.seconds} seconds.")
        return []
    except Exception as e:
        logger.error(f"Error fetching {channel_username}: {e}")
        return []
