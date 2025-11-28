from typing import List, Optional
from database import fetchall, fetchone, execute
import psycopg2

def list_tipos() -> List[dict]:
    sql = "SELECT id, descricao FROM tipo_ordem_servico ORDER BY id"
    return fetchall(sql)

def get_tipo(tipo_id: int) -> Optional[dict]:
    sql = "SELECT id, descricao FROM tipo_ordem_servico WHERE id = %s"
    return fetchone(sql, (tipo_id,))

def create_tipo(data: dict) -> dict:
    sql = "INSERT INTO tipo_ordem_servico (descricao) VALUES (%s) RETURNING id, descricao"
    return fetchone(sql, (data.get("descricao"),))

def update_tipo(tipo_id: int, data: dict) -> Optional[dict]:
    sql = "UPDATE tipo_ordem_servico SET descricao = %s WHERE id = %s RETURNING id, descricao"
    return fetchone(sql, (data.get("descricao"), tipo_id))

def delete_tipo(tipo_id: int) -> bool:
    sql = "DELETE FROM tipo_ordem_servico WHERE id = %s"
    try:
        execute(sql, (tipo_id,))
        return True
    except psycopg2.errors.ForeignKeyViolation:
        return False