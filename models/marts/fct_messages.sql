SELECT
    m.message_id,
    c.channel_id,
    d.date,
    m.message,
    m.message_length,
    m.has_media
FROM {{ ref('stg_telegram_messages') }} m
JOIN {{ ref('dim_channels') }} c ON m.channel = c.channel_id
JOIN {{ ref('dim_dates') }} d ON m.message_date = d.date
