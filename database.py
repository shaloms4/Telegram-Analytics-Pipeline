import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    return psycopg2.connect(
        dbname="medinsights",
        user="postgres",
        password="securepassword",
        host="localhost",
        port="5432"
    )
