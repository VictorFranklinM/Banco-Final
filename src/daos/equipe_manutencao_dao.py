from typing import List, Optional
from database import fetchall, fetchone, execute
import psycopg2

def list_equipes() -> List[dict]:
    sql = "SELECT id, nome, turno FROM equipe_manutencao ORDER BY id"
    return fetchall(sql)

def get_equipe(equipe_id: int) -> Optional[dict]:
    sql = "SELECT id, nome, turno FROM equipe_manutencao WHERE id = %s"
    return fetchone(sql, (equipe_id,))

def create_equipe(data: dict) -> dict:
    sql = "INSERT INTO equipe_manutencao (nome, turno) VALUES (%s, %s) RETURNING id, nome, turno"
    return fetchone(sql, (data.get("nome"), data.get("turno")))

def update_equipe(equipe_id: int, data: dict) -> Optional[dict]:
    cols = []
    vals = []
    for k, v in data.items():
        cols.append(f"{k} = %s")
        vals.append(v)
    if not cols:
        return get_equipe(equipe_id)
    sql = f"UPDATE equipe_manutencao SET {', '.join(cols)} WHERE id = %s RETURNING id, nome, turno"
    vals.append(equipe_id)
    return fetchone(sql, tuple(vals))

def delete_equipe(equipe_id: int) -> bool:
    sql = "DELETE FROM equipe_manutencao WHERE id = %s"
    try:
        execute(sql, (equipe_id,))
        return True
    except psycopg2.errors.ForeignKeyViolation:
        return False