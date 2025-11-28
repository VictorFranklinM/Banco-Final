from daos import funcionario_dao

def list_all():
    return funcionario_dao.list_funcionarios()

def get(func_id: int):
    return funcionario_dao.get_funcionario(func_id)

def create(data: dict):
    return funcionario_dao.create_funcionario(data)

def update(func_id: int, data: dict):
    return funcionario_dao.update_funcionario(func_id, data)

def delete(func_id: int):
    return funcionario_dao.delete_funcionario(func_id)