from daos import local_estoque_dao

def list_all():
    return local_estoque_dao.list_locais()

def get(local_id: int):
    return local_estoque_dao.get_local(local_id)

def create(data: dict):
    return local_estoque_dao.create_local(data)

def update(local_id: int, data: dict):
    return local_estoque_dao.update_local(local_id, data)

def delete(local_id: int):
    return local_estoque_dao.delete_local(local_id)