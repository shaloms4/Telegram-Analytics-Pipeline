import os
import json
from datetime import datetime

def save_raw_data(channel_name, messages):
    date_str = datetime.today().strftime('%Y-%m-%d')
    directory = os.path.join("data", "raw", "telegram_messages", date_str)
    os.makedirs(directory, exist_ok=True)

    file_path = os.path.join(directory, f"{channel_name}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=2, ensure_ascii=False, default=str)
