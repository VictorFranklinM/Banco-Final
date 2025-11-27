from typing import Optional, Tuple, Any
from psycopg2.pool import SimpleConnectionPool
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager
from config import settings

_pool: Optional[SimpleConnectionPool] = None

def init_db_pool(minconn: int = 1, maxconn: int = 10) -> None:
    global _pool
    if _pool is None:
        _pool = SimpleConnectionPool(
            minconn, maxconn,
            host=settings.POSTGRES_HOST,
            port=settings.POSTGRES_PORT,
            dbname=settings.POSTGRES_DB,
            user=settings.POSTGRES_USER,
            password=settings.POSTGRES_PASSWORD
        )

def close_db_pool() -> None:
    """Fecha todas as conexões do pool (chame no shutdown do app)."""
    global _pool
    if _pool:
        _pool.closeall()
        _pool = None

@contextmanager
def get_conn():
    """
    Context manager que fornece uma conexão retirada do pool.
    Usage:
        with get_conn() as conn:
            ...
    Ao sair, a conexão é devolvida ao pool automaticamente.
    """
    global _pool
    if _pool is None:
        raise RuntimeError("Connection pool is not initialized. Call init_db_pool() on startup.")
    conn = _pool.getconn()
    try:
        yield conn
    finally:
        # devolve a conexão ao pool (não fechar)
        _pool.putconn(conn)

# ----- helpers -----
def fetchall(query: str, params: Optional[Tuple[Any, ...]] = None):
    params = params or ()
    with get_conn() as conn:
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query, params)
                rows = cur.fetchall()
            conn.commit()
            return rows
        except Exception:
            conn.rollback()
            raise

def fetchone(query: str, params: Optional[Tuple[Any, ...]] = None):
    params = params or ()
    with get_conn() as conn:
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query, params)
                row = cur.fetchone()
            conn.commit()
            return row
        except Exception:
            conn.rollback()
            raise

def execute(query: str, params: Optional[Tuple[Any, ...]] = None):
    params = params or ()
    with get_conn() as conn:
        try:
            with conn.cursor() as cur:
                cur.execute(query, params)
            conn.commit()
        except Exception:
            conn.rollback()
            raise