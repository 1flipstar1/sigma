import requests
import sys
import os

def transform_from_dp_to_api(line):
    line = line.replace(', ', ',')[:-1]
    line = line.split('; ')
    line = map(lambda x: x[x.find(':')+1:], line)
    line = map(lambda x: [x.split(',')[1], x.split(',')[0], 'flag'], line)
    line = map(lambda x: ','.join(x), line)
    line = '~'.join(line)
    return line

def get_map(points, z=15):
    # map_request = 'http://static-maps.yandex.ru/1.x/?pt=36.242889,54.511964,pm2ywm50~36.242638,54.510594,pm2wtm50&spn=0.002,0.002&l=map'
    api_server = 'http://static-maps.yandex.ru/1.x/'
    params = {
        #"ll": "36.242889,54.511964",
        #"spn": "0.002,0.002",
        "l": "map",
        'size': '640,450',
        'z': z,
        'pt': points
    }
    response = requests.get(api_server, params=params)

    if not response:
        print('Ошибка выполнения запроса:')
        print('Http статус:', response.status_code, '(', response.reason, ')')
        return False
    return response.content
