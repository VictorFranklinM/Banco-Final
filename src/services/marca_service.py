from daos import marca_dao

def list_all():
    return marca_dao.list_marcas()

def get(marca_id: int):
    return marca_dao.get_marca(marca_id)

def create(data: dict):
    return marca_dao.create_marca(data)

def update(marca_id: int, data: dict):
    return marca_dao.update_marca(marca_id, data)

def delete(marca_id: int):
    return marca_dao.delete_marca(marca_id)
