from typing import List, Optional
from database import fetchall, fetchone, execute
import psycopg2

def list_tamanhos() -> List[dict]:
    sql = "SELECT id, descricao FROM tamanho ORDER BY id"
    return fetchall(sql)

def get_tamanho(tamanho_id: int) -> Optional[dict]:
    sql = "SELECT id, descricao FROM tamanho WHERE id = %s"
    return fetchone(sql, (tamanho_id,))

def create_tamanho(data: dict) -> dict:
    sql = "INSERT INTO tamanho (descricao) VALUES (%s) RETURNING id, descricao"
    return fetchone(sql, (data.get("descricao"),))

def update_tamanho(tamanho_id: int, data: dict) -> Optional[dict]:
    sql = "UPDATE tamanho SET descricao = %s WHERE id = %s RETURNING id, descricao"
    return fetchone(sql, (data.get("descricao"), tamanho_id))

def delete_tamanho(tamanho_id: int) -> bool:
    sql = "DELETE FROM tamanho WHERE id = %s"
    try:
        execute(sql, (tamanho_id,))
        return True
    except psycopg2.errors.ForeignKeyViolation:
        return False