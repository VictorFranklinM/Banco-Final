from daos import fornecedor_dao

def list_all():
    return fornecedor_dao.list_fornecedores()

def get(fid: int):
    return fornecedor_dao.get_fornecedor(fid)

def create(data: dict):
    return fornecedor_dao.create_fornecedor(data)

def update(fid: int, data: dict):
    return fornecedor_dao.update_fornecedor(fid, data)

def delete(fid: int):
    return fornecedor_dao.delete_fornecedor(fid)