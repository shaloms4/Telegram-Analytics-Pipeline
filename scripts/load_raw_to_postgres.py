import os
import json
import psycopg2
from datetime import datetime

conn = psycopg2.connect(
    dbname="medinsights",
    user="postgres",
    password="securepassword",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

def load_messages_from_file(filepath, channel):
    with open(filepath, encoding="utf-8") as f:
        messages = json.load(f)

    for msg in messages:
        cur.execute("""
            INSERT INTO raw.telegram_messages (
                id, channel, date, message, has_media, message_length
            ) VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING
        """, (
            msg.get('id'),
            channel,
            msg.get('date'),
            msg.get('message'),
            bool(msg.get('media')),
            len(msg.get('message') or '')
        ))

    conn.commit()

base_dir = "data/raw/telegram_messages"
for date_dir in os.listdir(base_dir):
    date_path = os.path.join(base_dir, date_dir)
    for file in os.listdir(date_path):
        channel = file.replace(".json", "")
        print(f"Loading {channel}")
        load_messages_from_file(os.path.join(date_path, file), channel)

cur.close()
conn.close()
