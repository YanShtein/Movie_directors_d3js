import sqlite3
import csv

conn = sqlite3.connect('Movies.sqlite')
cur = conn.cursor()

conn.executescript('''
DROP TABLE IF EXISTS Movies;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Director;

CREATE TABLE Genre (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Director (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Movies (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT,
    released INTEGER,
    director_id INTEGER,
    run_time TEXT,
    genre1_id INTEGER,
    genre2_id INTEGER,
    genre3_id INTEGER,
    IMDB_rating FLOAT,
    votes INTEGER,
    gross INTEGER,
    overview TEXT
);
''')

file = open('imdb.csv')
data = csv.reader(file)
next(data)


def get_genre(lst, i):
    try:
        return lst[i]
    except:
        return None


for row in data:
    gen = row[4].split(', ')
    gen.sort()
    # print(gen)
    dirc = row[2]
    genre_list = list()
    for item in gen:
        cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (item, ))
        cur.execute('SELECT id FROM Genre WHERE name = ?', (item, ))
        genre_id = cur.fetchone()[0]
        genre_list.append(genre_id)
    # print(genre_list)
    cur.execute('INSERT OR IGNORE INTO Director (name) VALUES (?)', (dirc, ))
    cur.execute('SELECT id FROM Director WHERE name = ?', (dirc, ))
    director_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Movies
        (title, released, director_id, run_time, genre1_id, genre2_id, genre3_id, IMDB_rating, votes, overview, gross)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
        (row[0], row[1], director_id, row[3],
         get_genre(genre_list, 0), get_genre(genre_list, 1), get_genre(genre_list, 2), row[5], row[6], row[7], row[8]))

conn.commit()


