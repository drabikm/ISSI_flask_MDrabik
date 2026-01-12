import sqlite3

def list_movies():
    db = sqlite3.connect('movies.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM movies')
    for row in cursor:
        print('{0}, {1}, {2}'.format(row[1], row[2], row[3]))

def add_movie(title, year, actors):
    db = sqlite3.connect('movies.db')
    cursor = db.cursor()
    cursor.execute(f'INSERT INTO movies (title, year, actors) VALUES ("{title}",{year},"{actors}")')
    db.commit()

def find_movie(key):
    db = sqlite3.connect('movies.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM movies WHERE title LIKE ? OR actors LIKE ?', ("%"+key+"%", "%"+key+"%"))
    # cursor.execute(f'SELECT * FROM movies WHERE title LIKE "%{key}%" OR actors LIKE "%{key}%"') - niebezpieczne, bo SQLInjection
    for row in cursor:
        print('{0}, {1}, {2}'.format(row[1], row[2], row[3]))

def delete_movies(movies_to_be_deleted):
    db = sqlite3.connect('movies.db')
    cursor = db.cursor()
    for id_to_remove in movies_to_be_deleted:
        cursor.execute(f'DELETE from movies where id = {id_to_remove}')
    db.commit()