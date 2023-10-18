import requests
import pygame
import sys
import os

api_key = '40d1649f-0493-4b70-98ba-98533de7710b'
map_request = 'https://static-maps.yandex.ru/v1?lang=ru_RU&pl=38.423625,27.143245,38.423912,27.143015,38.424102,27.142795,38.424128,27.142795,38.424128,27.142387,38.423918,27.141909,38.423918,27.138275,38.42422&apikey=api_key'

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

screen = pygame.display.set_mode((301, 163))
screen.blit(pygame.image.load(map_pic), (0, 0))
pygame.display.update()

while pygame.event.wait().type != pygame.QUIT:
    pass

os.remove(map_pic)