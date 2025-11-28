from daos import area_campus_dao

def list_all():
    return area_campus_dao.list_areas()

def get(area_id: int):
    return area_campus_dao.get_area(area_id)

def create(data: dict):
    return area_campus_dao.create_area(data)

def update(area_id: int, data: dict):
    return area_campus_dao.update_area(area_id, data)

def delete(area_id: int):
    return area_campus_dao.delete_area(area_id)