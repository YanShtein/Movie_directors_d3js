import sqlite3

conn = sqlite3.connect('Movies.sqlite')
cur = conn.cursor()
# We select the following tables, grouping by director name, combining the stats for each director.
# than for the size output on the js file, we sum the votes, averaging the rating and do math operation later.
# Writing to js, one director and its popularity, to vizualise in browser.
cur.execute('''SELECT Director.name, avg(Movies.IMDB_rating), sum(Movies.votes)
            FROM Movies JOIN Director ON Movies.director_id = Director.id
            GROUP BY Director.name''')

fhand = open('movies.js','w')
fhand.write("movies = [")
first = True
for name, rating, votes in cur:
    if not first: fhand.write(",\n")
    first = False
    t = str(name)
    t = t.replace("'", "")
    s = int((rating * votes) / 280000)
    fhand.write("{text: '"+t+"', size: "+str(s)+"}")
fhand.write( "\n];\n")
fhand.close()
