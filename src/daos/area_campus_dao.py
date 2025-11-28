from typing import List, Optional
from database import fetchall, fetchone, execute
import psycopg2

def list_areas() -> List[dict]:
    sql = "SELECT id, tipo_area_id, descricao, bloco FROM area_campus ORDER BY id"
    return fetchall(sql)

def get_area(area_id: int) -> Optional[dict]:
    sql = "SELECT id, tipo_area_id, descricao, bloco FROM area_campus WHERE id = %s"
    return fetchone(sql, (area_id,))

def create_area(data: dict) -> dict:
    sql = "INSERT INTO area_campus (tipo_area_id, descricao, bloco) VALUES (%s, %s, %s) RETURNING id, tipo_area_id, descricao, bloco"
    return fetchone(sql, (data.get("tipo_area_id"), data.get("descricao"), data.get("bloco")))

def update_area(area_id: int, data: dict) -> Optional[dict]:
    cols = []
    vals = []
    for k, v in data.items():
        cols.append(f"{k} = %s")
        vals.append(v)
    if not cols:
        return get_area(area_id)
    sql = f"UPDATE area_campus SET {', '.join(cols)} WHERE id = %s RETURNING id, tipo_area_id, descricao, bloco"
    vals.append(area_id)
    return fetchone(sql, tuple(vals))

def delete_area(area_id: int) -> bool:
    sql = "DELETE FROM area_campus WHERE id = %s"
    try:
        execute(sql, (area_id,))
        return True
    except psycopg2.errors.ForeignKeyViolation:
        return False