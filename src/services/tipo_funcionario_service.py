from daos import (tipo_funcionario_dao)

def list_tipos_funcionarios():
    return tipo_funcionario_dao.list_tipos_funcionarios()

def get_tipo_funcionario(tipo_id: int):
    return tipo_funcionario_dao.get_tipo_funcionario(tipo_id)

def create_tipo_funcionario(data: dict):
    return tipo_funcionario_dao.create_tipo_funcionario(data)

def update_tipo_funcionario(tipo_id: int, data: dict):
    return tipo_funcionario_dao.update_tipo_funcionario(tipo_id, data)

def delete_tipo_funcionario(tipo_id: int):
    return tipo_funcionario_dao.delete_tipo_funcionario(tipo_id)