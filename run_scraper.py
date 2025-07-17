import asyncio
from scraper.config import CHANNELS, IMAGE_CHANNELS
from scraper.fetch_messages import fetch_channel_messages
from scraper.fetch_images import download_images
from scraper.save_to_datalake import save_raw_data
from scraper.log_utils import get_logger

logger = get_logger("main")

async def run_scraping():
    for channel in CHANNELS:
        logger.info(f"Scraping text from: {channel}")
        messages = await fetch_channel_messages(channel)
        if messages:
            save_raw_data(channel, messages)
            logger.info(f"Saved {len(messages)} messages for {channel}")

    for channel in IMAGE_CHANNELS:
        logger.info(f"Scraping images from: {channel}")
        await download_images(channel, f"data/raw/telegram_images/{channel}")

if __name__ == "__main__":
    asyncio.run(run_scraping())
