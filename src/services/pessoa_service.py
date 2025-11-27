from daos import (pessoa_dao)

def list_pessoas():
    return pessoa_dao.list_pessoas()

def get_pessoa(pessoa_id: int):
    return pessoa_dao.get_pessoa(pessoa_id)

def create_pessoa(data: dict):
    return pessoa_dao.create_pessoa(data)

def update_pessoa(pessoa_id: int, data: dict):
    return pessoa_dao.update_pessoa(pessoa_id, data)


def delete_pessoa(pessoa_id: int):
    ok = pessoa_dao.delete_pessoa(pessoa_id)
    return ok