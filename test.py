import keyboard

menu = ['природа', 'космос', 'парки', 'музеи']
cursor = '>'
cursor_state = 0

while not (keyboard.is_pressed('shift + enter')):
    if keyboard.is_pressed('shift + up'):
        cursor_state -= 1
        cursor_state %= len(menu)

        menu[cursor_state] = cursor + menu[cursor_state]

        for i in range(len(menu)):
            print(menu[i])
    elif keyboard.is_pressed('shift + down'):
        cursor_state += 1
        cursor_state %= len(menu)

        menu[cursor_state] = cursor + ''.join(menu[cursor_state])

        for i in range(len(menu)):
            print(menu[i])

print(menu[cursor_state])