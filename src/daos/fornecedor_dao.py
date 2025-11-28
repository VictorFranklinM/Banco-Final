from typing import List, Optional
from database import fetchall, fetchone, execute
import psycopg2

def list_fornecedores() -> List[dict]:
    sql = "SELECT id, nome, cnpj FROM fornecedor ORDER BY id"
    return fetchall(sql)

def get_fornecedor(fid: int) -> Optional[dict]:
    sql = "SELECT id, nome, cnpj FROM fornecedor WHERE id = %s"
    return fetchone(sql, (fid,))

def create_fornecedor(data: dict) -> dict:
    sql = "INSERT INTO fornecedor (nome, cnpj) VALUES (%s, %s) RETURNING id, nome, cnpj"
    return fetchone(sql, (data.get("nome"), data.get("cnpj")))

def update_fornecedor(fid: int, data: dict) -> Optional[dict]:
    cols = []
    vals = []
    for k, v in data.items():
        cols.append(f"{k} = %s")
        vals.append(v)
    if not cols:
        return get_fornecedor(fid)
    sql = f"UPDATE fornecedor SET {', '.join(cols)} WHERE id = %s RETURNING id, nome, cnpj"
    vals.append(fid)
    return fetchone(sql, tuple(vals))

def delete_fornecedor(fid: int) -> bool:
    sql = "DELETE FROM fornecedor WHERE id = %s"
    try:
        execute(sql, (fid,))
        return True
    except psycopg2.errors.ForeignKeyViolation:
        return False