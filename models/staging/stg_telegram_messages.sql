WITH raw AS (
    SELECT * FROM raw.telegram_messages
)

SELECT
    id AS message_id,
    channel,
    CAST(date AS DATE) AS message_date,
    message,
    has_media,
    message_length
FROM raw
