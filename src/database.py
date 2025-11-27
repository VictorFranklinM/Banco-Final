import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    return psycopg2.connect(
        host="localhost",
        port=5433,
        database="sigej",
        user="postgres",
        password="postgres",
        cursor_factory=RealDictCursor
    )
