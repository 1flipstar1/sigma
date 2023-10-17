import sqlite3

db = sqlite3.connect('project.sqlite')
cursor = db.cursor()

print(cursor.execute('SELECT id FROM ROUTES').fetchall())

db.close()