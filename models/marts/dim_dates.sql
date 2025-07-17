SELECT DISTINCT
    message_date AS date,
    EXTRACT(DAY FROM message_date) AS day,
    EXTRACT(MONTH FROM message_date) AS month,
    EXTRACT(YEAR FROM message_date) AS year,
    TO_CHAR(message_date, 'Day') AS weekday
FROM {{ ref('stg_telegram_messages') }}
