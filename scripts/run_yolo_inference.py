import os
import cv2
import psycopg2
from ultralytics import YOLO

# Load model
model = YOLO("yolov8n.pt")  # or yolov8s.pt for better accuracy

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="medinsights",
    user="postgres",
    password="securepassword",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

def process_image(image_path, message_id):
    results = model(image_path)[0]
    for box in results.boxes:
        class_id = int(box.cls[0])
        class_name = model.names[class_id]
        confidence = float(box.conf[0])

        cur.execute("""
            INSERT INTO raw.image_detections (
                message_id, detected_class, confidence
            ) VALUES (%s, %s, %s)
        """, (message_id, class_name, confidence))

    conn.commit()

# Scan folders for images
base_path = "data/raw/telegram_images"
for channel in os.listdir(base_path):
    channel_dir = os.path.join(base_path, channel)
    for img_file in os.listdir(channel_dir):
        if img_file.endswith(".jpg"):
            message_id = int(img_file.replace(".jpg", ""))
            image_path = os.path.join(channel_dir, img_file)
            print(f"Processing {image_path}")
            process_image(image_path, message_id)

cur.close()
conn.close()
