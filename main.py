import sqlite3
# СЮДА БЫ ПРИКРУТИТЬ СЕРИАЛИЗАТОР В ОБЪЕКТ ИЛИ СЛОВАРЕМ ВОЗВРЩАТЬ. ЭХ ДЖЕЙСОНЫ МОИ ДЖЕЙСОНЫ

DB_NAME = 'project.sqlite'

# db = sqlite3.connect('project.sqlite')
# cursor = db.cursor()


# def userChoose(col1, filt1=None, filt_col1=None, filt2=None, filt_col2=None):
#     cursor.execute(f'''SELECT DISTINCT {col1} FROM routes WHERE "{filt_col1}" = "{(None, filt1)[filt1 is not None]}"
#                     AND "{filt_col2}" = "{(None, filt2)[filt2 is not None]}"''')
#
#     col_lst = cursor.fetchall()
#
#     for i in range(len(col_lst)):
#         print(str(i + 1) + '.', col_lst[i][0])
#
#     user_ans = int(input(f'choose {col1} (write): '))
#     res = col_lst[user_ans - 1][0]
#
#     return res

def get_all_from_db():
    cursor.execute('''SELECT * FROM routes''')
    res = cursor.fetchall()
    return res

def get_columns_from_db(columns, filters):
    request = f'''SELECT {', '.join(columns)} FROM routes'''
    if filters:
        temp = list()
        for filter in filters:
            x = f'{filter} = {filters[filter]}'
            temp.append(x)
        where_part = ' WHERE ' + ' AND '.join(temp)
        request = request + where_part
    cursor.execute(request)
    res = cursor.fetchall()
    return res

def get_points_by_id_from_db(id):
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    cursor.execute(f'''SELECT rout FROM routes WHERE id = {id}''')
    res = cursor.fetchone()
    return res[0]

# matter = userChoose('matter')
# tp = userChoose('type', matter, 'matter')
# route = userChoose('name', matter, 'matter', tp, 'type')
#
# cursor.execute(f'SELECT duration FROM routes WHERE name = "{route}"')
# duration = ''.join(cursor.fetchone())
#
# print(f'\nназвание: {route}\nпродолжительность: {duration}\nсредство передвижения: {tp}\nтематика: {matter}')
#
# db.close()


if __name__ == '__main__':

    result = get_points_by_id_from_db(2)
    print(result)
