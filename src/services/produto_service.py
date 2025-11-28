from daos import produto_dao

def list_all():
    return produto_dao.list_produtos()

def get(produto_id: int):
    return produto_dao.get_produto(produto_id)

def create(data: dict):
    return produto_dao.create_produto(data)

def update(produto_id: int, data: dict):
    return produto_dao.update_produto(produto_id, data)

def delete(produto_id: int):
    return produto_dao.delete_produto(produto_id)