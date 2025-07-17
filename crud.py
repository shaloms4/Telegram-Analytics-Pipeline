from database import get_connection

def get_top_products(limit: int = 10):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT LOWER(product) AS product, COUNT(*) AS mentions
        FROM fct_messages
        WHERE product IS NOT NULL
        GROUP BY product
        ORDER BY mentions DESC
        LIMIT %s;
    """, (limit,))
    rows = cur.fetchall()
    conn.close()
    return [{"product": r[0], "mentions": r[1]} for r in rows]

def get_channel_activity(channel_name: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT date::text, COUNT(*) AS message_count
        FROM fct_messages
        WHERE channel_name = %s
        GROUP BY date
        ORDER BY date;
    """, (channel_name,))
    rows = cur.fetchall()
    conn.close()
    return [{"date": r[0], "message_count": r[1]} for r in rows]

def search_messages(keyword: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT message_id, channel_name, message, date::text
        FROM fct_messages
        WHERE LOWER(message) LIKE %s
        ORDER BY date DESC
        LIMIT 50;
    """, (f"%{keyword.lower()}%",))
    rows = cur.fetchall()
    conn.close()
    return [{
        "message_id": r[0],
        "channel_name": r[1],
        "message": r[2],
        "date": r[3]
    } for r in rows]
