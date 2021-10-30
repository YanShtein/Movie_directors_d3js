# Movie_directors_d3js
Final project of Python for Everybody course.

<img src="https://github.com/YanShtein/Movie_directors_d3js/blob/main/preview.PNG" alt="Output preview" style="max-width: 80%;">

We were asked to identify a data source, perform some analysis on that data to later vizualize it in browser. (based on chapter 16 of the book: 'Python for Everybody' by Dr. Charles R. Severance)
After some research, I decided to use <a href='https://www.kaggle.com/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows?select=imdb_top_1000.csv'>imdb_top_1000</a> Dataset.

These were my steps in short:
1. Using the csv file, I created my sqlite3 database , after deciding which tables and columns I want in my data.
2. Based on the csv structure, I performed the cur.execute function and added the rows each in its place, in the data.
3. I created movies_js.py file which performs SELECT and JOIN operation on specific columns and tables from the created database, creating the movies.js file with the results.
4. The movies.js file using text and size, to vizualize the highest and lowest results in the browser.

The implementation makes use of <a href='https://github.com/jasondavies/d3-cloud'>d3.layout.cloud </a> by Jason Davies.
