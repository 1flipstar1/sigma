import sqlite3

db = sqlite3.connect('project.sqlite')
cursor = db.cursor()

cursor.execute('SELECT matter FROM routes')
matters = cursor.fetchall()

for i in range(len(matters)):
    print(str(i + 1) + '.', matters[i][0])

user_mtr = int(input('выбери тематику маршрута (написать его номер): '))
mtr = matters[user_mtr - 1][0]
print(mtr)

cursor.execute(f'SELECT type FROM routes WHERE matter = "{mtr}"')
types = cursor.fetchall()

for i in range(len(types)):
    print(str(i + 1) + '.', types[i][0])

user_tp = int(input('выбери способ передвижения (написать его номер): '))
tp = types[user_tp - 1][0]
print(tp)

db.close()


def userChoose(col, filt=None, filt_col=None):
    if filt is not None and filt_col is not None:
        cursor.execute(f'SELECT "{col}" FROM routes WHERE "{filt_col}" = "{mtr}"')
    else:
        cursor.execute(f'SELECT "{col}" FROM routes')

    col_lst = cursor.fetchall()

    for i in range(len(col_lst)):
        print(str(i + 1) + '.', col_lst[i][0])

    user_ans = int(input(f'выбери {col} (написать его номер): '))
    res = col_lst[user_ans - 1][0]

    return res