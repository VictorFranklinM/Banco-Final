from daos import tamanho_dao

def list_all():
    return tamanho_dao.list_tamanhos()

def get(tamanho_id: int):
    return tamanho_dao.get_tamanho(tamanho_id)

def create(data: dict):
    return tamanho_dao.create_tamanho(data)

def update(tamanho_id: int, data: dict):
    return tamanho_dao.update_tamanho(tamanho_id, data)

def delete(tamanho_id: int):
    return tamanho_dao.delete_tamanho(tamanho_id)