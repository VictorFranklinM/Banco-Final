from daos import tipo_movimento_estoque_dao

def list_all():
    return tipo_movimento_estoque_dao.list_tipos()

def get(tipo_id: int):
    return tipo_movimento_estoque_dao.get_tipo(tipo_id)

def create(data: dict):
    return tipo_movimento_estoque_dao.create_tipo(data)

def update(tipo_id: int, data: dict):
    return tipo_movimento_estoque_dao.update_tipo(tipo_id, data)

def delete(tipo_id: int):
    return tipo_movimento_estoque_dao.delete_tipo(tipo_id)