import os
from telethon.sync import TelegramClient
from telethon.tl.types import MessageMediaPhoto
from dotenv import load_dotenv
from scraper.log_utils import get_logger

load_dotenv()
logger = get_logger("fetch_images")

api_id = os.getenv("TELEGRAM_API_ID")
api_hash = os.getenv("TELEGRAM_API_HASH")
client = TelegramClient('images', api_id, api_hash)

async def download_images(channel, save_dir, limit=200):
    os.makedirs(save_dir, exist_ok=True)
    await client.start()
    async for message in client.iter_messages(channel, limit=limit):
        if message.media and isinstance(message.media, MessageMediaPhoto):
            try:
                await client.download_media(message.media, file=os.path.join(save_dir, f"{message.id}.jpg"))
                logger.info(f"Downloaded image {message.id} from {channel}")
            except Exception as e:
                logger.error(f"Failed to download image from {channel}: {e}")
