SELECT
    id AS detection_id,
    message_id,
    detected_class,
    ROUND(confidence::numeric, 3) AS confidence_score
FROM raw.image_detections
