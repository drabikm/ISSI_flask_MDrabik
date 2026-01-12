import sqlite3

from flask import Flask, render_template, request, redirect, url_for
import database

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        movies_to_remove_ids = request.form.getlist('movieToRemove')
        database.delete_movies(movies_to_remove_ids)
        return redirect(url_for('home'))
    db = sqlite3.connect('movies.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM movies')
    return render_template("home.html", movies = cursor)

@app.route('/addMovie', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        title = request.form.get('title')
        year = request.form.get('year')
        actors = request.form.get('actors')
        database.add_movie(title, year, actors)
        return redirect(url_for('home'))
    return render_template("add.html")

if __name__ == '__main__':
    app.run()
