from daos import categoria_material_dao

def list_all():
    return categoria_material_dao.list_categorias()

def get(cat_id: int):
    return categoria_material_dao.get_categoria(cat_id)

def create(data: dict):
    return categoria_material_dao.create_categoria(data)

def update(cat_id: int, data: dict):
    return categoria_material_dao.update_categoria(cat_id, data)

def delete(cat_id: int):
    return categoria_material_dao.delete_categoria(cat_id)