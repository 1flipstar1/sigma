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

def transform_from_dp_to_api(line):
    print(line)
    line = line.replace(', ', ',')[:-1]
    line = line.split('; ')
    line = map(lambda x: x[2:], line)
    line = map(lambda x: [x.split(',')[1], x.split(',')[0], 'flag'], line)
    line = map(lambda x: ','.join(x), line)
    line = '~'.join(line)
    return line

def get_map(points):
    api_server = 'http://static-maps.yandex.ru/1.x/'
    params = {
        "l": "map",
        'size': '640,450',
        'z': '12',
        'pt': points
    }
    response = requests.get(api_server, params=params)
    if not response:
        print('Ошибка выполнения запроса:')
        print('Http статус:', response.status_code, '(', response.reason, ')')
        return False
    return response.content




print('input number')
n = int(input())
screen = pygame.display.set_mode((640, 450))
points = transform_from_dp_to_api(get_points_by_id_from_db(n))
print(points)
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