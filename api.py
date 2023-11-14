import requests
import pygame
import sys
import os

map_request = 'http://static-maps.yandex.ru/1.x/?pt=36.242889,54.511964,pm2ywm50~36.242638,54.510594,pm2wtm50&spn=0.002,0.002&l=map'

response = requests.get(map_request)

if not response:
    print('Ошибка выполнения запроса:')
    print(map_request)
    print('Http статус:', response.status_code, '(', response.reason, ')')

    sys.exit(1)

map_pic = 'map.png'
with open(map_pic, 'wb') as file:
    file.write(response.content)

pygame.init()

screen = pygame.display.set_mode((500, 350))
screen.blit(pygame.image.load(map_pic), (0, 0))
pygame.display.update()

while pygame.event.wait().type != pygame.QUIT:
    pass

os.remove(map_pic)
