from daos import estoque_dao

def list_estoque():
    return estoque_dao.list_estoque()

def get_estoque(produto_variacao_id: int, local_estoque_id: int):
    return estoque_dao.get_estoque(produto_variacao_id, local_estoque_id)

def create_estoque(data: dict):
    return estoque_dao.create_estoque(data)

def update_estoque(produto_variacao_id: int, local_estoque_id: int, data: dict):
    return estoque_dao.update_estoque(produto_variacao_id, local_estoque_id, data)

def delete_estoque(produto_variacao_id: int, local_estoque_id: int):
    return estoque_dao.delete_estoque(produto_variacao_id, local_estoque_id)