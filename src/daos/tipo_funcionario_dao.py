from typing import List, Optional
from database import fetchall, fetchone, execute
import psycopg2

def list_tipos_funcionarios() -> List[dict]:
    sql = "SELECT id, descricao FROM tipo_funcionario ORDER BY id"
    return fetchall(sql)

def get_tipo_funcionario(tipo_id: int) -> Optional[dict]:
    sql = "SELECT id, descricao FROM tipo_funcionario WHERE id = %s"
    return fetchone(sql, (tipo_id,))

def create_tipo_funcionario(data: dict) -> dict:
    sql = "INSERT INTO tipo_funcionario (descricao) VALUES (%s) RETURNING id, descricao"
    return fetchone(sql, (data.get("descricao"),))

def update_tipo_funcionario(tipo_id: int, data: dict) -> Optional[dict]:
    cols = []
    vals = []
    for k, v in data.items():
        cols.append(f"{k} = %s")
        vals.append(v)
    if not cols:
        return get_tipo_funcionario(tipo_id)
    sql = f"""
            UPDATE tipo_funcionario
            SET {', '.join(cols)}
            WHERE id = %s
            RETURNING id, descricao
        """
    vals.append(tipo_id)
    return fetchone(sql, tuple(vals))

def delete_tipo_funcionario(tipo_id: int) -> bool:
    sql = "DELETE FROM tipo_funcionario WHERE id = %s"
    try:
        execute(sql, (tipo_id,))
        return True
    except psycopg2.errors.ForeignKeyViolation:
        return False