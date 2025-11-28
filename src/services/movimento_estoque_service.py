from daos import movimento_estoque_dao

def list_all():
    return movimento_estoque_dao.list_movimentos()

def get(mov_id: int):
    return movimento_estoque_dao.get_movimento(mov_id)

def create(data: dict):
    return movimento_estoque_dao.create_movimento(data)

def update(mov_id: int, data: dict):
    return movimento_estoque_dao.update_movimento(mov_id, data)

def delete(mov_id: int):
    return movimento_estoque_dao.delete_movimento(mov_id)