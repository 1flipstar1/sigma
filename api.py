import requests
import pygame
import sys
import os
from main import get_points_by_id_from_db

MAP_FILE_NAME = 'map.png'
pygame.init()
def transform_from_dp_to_api(line):
    line = line.replace(', ', ',')[:-1]
    line = line.split('; ')
    line = map(lambda x: x[2:], line)
    line = map(lambda x: [x.split(',')[1], x.split(',')[0], 'flag'], line)
    line = map(lambda x: ','.join(x), line)
    line = '~'.join(line)
    return line


def get_map(points):
    # map_request = 'http://static-maps.yandex.ru/1.x/?pt=36.242889,54.511964,pm2ywm50~36.242638,54.510594,pm2wtm50&spn=0.002,0.002&l=map'
    api_server = 'http://static-maps.yandex.ru/1.x/'
    params = {
        #"ll": "36.242889,54.511964",
        #"spn": "0.002,0.002",
        "l": "map",
        'size': '640,450',
        'z': '15',
        'pt': points
    }
    response = requests.get(api_server, params=params)


    if not response:
        print('Ошибка выполнения запроса:')
        print('Http статус:', response.status_code, '(', response.reason, ')')
        return False
    return response.content





screen = pygame.display.set_mode((640, 450))
points = transform_from_dp_to_api(get_points_by_id_from_db(3))
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
