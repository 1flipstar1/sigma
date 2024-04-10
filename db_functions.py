import sqlite3


DB_NAME = 'project.sqlite'


def get_transport_types_from_db():
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    cursor.execute(f'''SELECT DISTINCT type FROM routes''')
    res = cursor.fetchall()
    res = [x[0] for x in res]
    return res


def get_matter_from_db():
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    cursor.execute(f'''SELECT DISTINCT matter FROM routes''')
    res = cursor.fetchall()
    res = [x[0] for x in res]
    return res


def get_routes_info_from_db(transport, matter):
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    cursor.execute(f'''SELECT id, name, duration  FROM routes WHERE type = "{transport}" and matter = "{matter}"''')
    res = cursor.fetchall()
    return res


def get_points_by_id_from_db(id):
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    cursor.execute(f'''SELECT rout FROM routes WHERE id = {id}''')
    res = cursor.fetchone()
    return res[0]


if __name__ == '__main__':
    types = get_transport_types_from_db()
    matters = get_matter_from_db()
    res = get_routes_info_from_db(types[0], matters[0])
    print(res)



