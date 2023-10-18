import sqlite3

db = sqlite3.connect('project.sqlite')
cursor = db.cursor()


def userChoose(col1, filt1=None, filt_col1=None, filt2=None, filt_col2=None):
    cursor.execute(f'''SELECT {col1} FROM routes WHERE "{filt_col1}" = "{(None, filt1)[filt1 is not None]}" AND 
                    "{filt_col2}" = "{(None, filt2)[filt2 is not None]}"''')

    col_lst = cursor.fetchall()

    for i in range(len(col_lst)):
        print(str(i + 1) + '.', col_lst[i][0])

    user_ans = int(input(f'выбери {col1} (написать его номер): '))
    res = col_lst[user_ans - 1][0]

    return res


matter = userChoose('matter')
tp = userChoose('type', matter, 'matter')
route = userChoose('name', matter, 'matter', tp, 'type')

cursor.execute(f'SELECT duration FROM routes WHERE name = "{route}"')
duration = ''.join(cursor.fetchone())

print(f'\nназвание: {route}\nпродолжительность: {duration}\nсредство передвижения: {tp}\nтематика: {matter}')

db.close()

