from daos import produto_variacao_dao

def list_all():
    return produto_variacao_dao.list_variacoes()

def get(var_id: int):
    return produto_variacao_dao.get_variacao(var_id)

def create(data: dict):
    return produto_variacao_dao.create_variacao(data)

def update(var_id: int, data: dict):
    return produto_variacao_dao.update_variacao(var_id, data)

def delete(var_id: int):
    return produto_variacao_dao.delete_variacao(var_id)