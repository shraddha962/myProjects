# app.py
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_categories():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()
    connection.close()
    return categories

def get_polls_by_category(category_id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM polls WHERE category_id=?", (category_id,))
    polls = cursor.fetchall()
    connection.close()
    return polls

def get_options_by_poll(poll_id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM options WHERE poll_id=?", (poll_id,))
    options = cursor.fetchall()
    connection.close()
    return options

@app.route('/')
def index():
    categories = get_categories()
    return render_template('index.html', categories=categories)

@app.route('/section/<int:category_id>')
def section(category_id):
    polls = get_polls_by_category(category_id)
    return render_template('section.html', polls=polls, category_id=category_id)

@app.route('/poll/<int:poll_id>')
def poll(poll_id):
    options = get_options_by_poll(poll_id)
    return render_template('poll.html', options=options, poll_id=poll_id)

if __name__ == "__main__":
    app.run(debug=True)
