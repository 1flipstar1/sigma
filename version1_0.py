import requests
import pygame
import sys
import os
import sqlite3

DB_NAME = 'project.sqlite'
MAP_FILE_NAME = 'map.png'
pygame.init()

def get_points_by_id_from_db(id):
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    cursor.execute(f'''SELECT rout FROM routes WHERE id = {id}''')
    res = cursor.fetchone()
    return res[0]

def get_matters_from_db():
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    cursor.execute(f'''SELECT DISTINCT matter FROM routes''')
    res = cursor.fetchall()
    res = [x[0] for x in res]
    return res

def get_routes_info_by_type_from_db(type):
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    cursor.execute(f'''SELECT id, name  FROM routes WHERE type = "{type}"''')
    res = cursor.fetchall()
    return res

def get_info_by_type_from_db(type):
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    cursor.execute(f'''SELECT id, name  FROM routes WHERE type = "{type}"''')
    res = cursor.fetchall()
    return res

def get_transport_types_from_db(matter):
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    cursor.execute(f'''SELECT DISTINCT type FROM routes WHERE matter = "{matter}"''')
    res = cursor.fetchall()
    res = [x[0] for x in res]
    return res

def transform_from_db_to_api(line):
    line = line.replace(', ', ',')[:-1]
    line = line.split('; ')
    line = map(lambda x: x[x.index(':') + 1:], line)
    line = map(lambda x: [x.split(',')[1], x.split(',')[0], 'flag'], line)
    line = map(lambda x: ','.join(x), line)
    line = '~'.join(line)
    return line

def get_map(points):
    api_server = 'http://static-maps.yandex.ru/1.x/'
    params = {
        "l": "map",
        'size': '640,450',
        'z': '14',
        'pt': points
    }
    response = requests.get(api_server, params=params)
    if not response:
        print('Ошибка выполнения запроса:')
        print('Http статус:', response.status_code, '(', response.reason, ')')
        print(points)
        return False
    return response.content

print('Здравствуйте, вас привествует первый путеводитель по Калуге!')

while True:
    print('Выберите тематику:')
    print(*get_matters_from_db())
    matter = input()
    types = get_transport_types_from_db(matter)
    if types:
        break
    else:
        print('Ой-ой, кажется вы ввели то-то неправильное!', 'Попытайтесь снова! :)', end='\n')

while True:
    print('Выберите тип передвижения:')
    print(*types)
    type = input()
    res = get_routes_info_by_type_from_db(type)
    if res:
        break
    else:
        print('Ой-ой, кажется вы ввели то-то неправильное!', 'Попытайтесь снова! :)', end='\n')
while True:
    try:
        print('Вот варианты маршрутов. Выберите номер:')
        for i in res:
            print(*i)
        n = input()
        points = get_points_by_id_from_db(n)
        break
    except:
        print('Ой-ой, кажется вы ввели то-то неправильное!', 'Попытайтесь снова! :)', end='\n')
screen = pygame.display.set_mode((640, 450))
points = transform_from_db_to_api(points)
map_content = get_map(points)
if not map_content:
    sys.exit(-1)

with open(MAP_FILE_NAME, 'wb') as file:
    file.write(map_content)

screen.blit(pygame.image.load(MAP_FILE_NAME), (0, 0))
pygame.display.update()

while pygame.event.wait().type != pygame.QUIT:
    pass

os.remove(MAP_FILE_NAME)