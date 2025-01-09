# create_db.py
import sqlite3

def create_database():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    # Create a table for categories
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    ''')

    # Create a table for polls
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS polls (
            id INTEGER PRIMARY KEY,
            category_id INTEGER,
            question TEXT NOT NULL,
            FOREIGN KEY (category_id) REFERENCES categories (id)
        )
    ''')

    # Create a table for options
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS options (
            id INTEGER PRIMARY KEY,
            poll_id INTEGER,
            option_text TEXT NOT NULL,
            FOREIGN KEY (poll_id) REFERENCES polls (id)
        )
    ''')

    # Create a table for votes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS votes (
            id INTEGER PRIMARY KEY,
            option_id INTEGER,
            user_id TEXT NOT NULL,  -- For simplicity, user_id can be a string (e.g., username)
            FOREIGN KEY (option_id) REFERENCES options (id)
        )
    ''')

    # Example categories
    cursor.execute("INSERT INTO categories (name) VALUES ('Sports')")
    cursor.execute("INSERT INTO categories (name) VALUES ('Politics')")
    cursor.execute("INSERT INTO categories (name) VALUES ('Technology')")
    cursor.execute("INSERT INTO categories (name) VALUES ('Entertainment')")

    # Example polls
    cursor.execute("INSERT INTO polls (category_id, question) VALUES (1, 'Who will win the championship?')")
    cursor.execute("INSERT INTO polls (category_id, question) VALUES (2, 'Who is the best candidate?')")
    cursor.execute("INSERT INTO polls (category_id, question) VALUES (3, 'What is the future of AI?')")
    cursor.execute("INSERT INTO polls (category_id, question) VALUES (4, 'What is the best movie of the year?')")

    # Example options for each poll
    cursor.execute("INSERT INTO options (poll_id, option_text) VALUES (1, 'Team A')")
    cursor.execute("INSERT INTO options (poll_id, option_text) VALUES (1, 'Team B')")
    cursor.execute("INSERT INTO options (poll_id, option_text) VALUES (1, 'Team C')")

    cursor.execute("INSERT INTO options (poll_id, option_text) VALUES (2, 'Candidate X')")
    cursor.execute("INSERT INTO options (poll_id, option_text) VALUES (2, 'Candidate Y')")

    cursor.execute("INSERT INTO options (poll_id, option_text) VALUES (3, 'AI in healthcare')")
    cursor.execute("INSERT INTO options (poll_id, option_text) VALUES (3, 'AI in finance')")
    cursor.execute("INSERT INTO options (poll_id, option_text) VALUES (3, 'AI in transportation')")

    cursor.execute("INSERT INTO options (poll_id, option_text) VALUES (4, 'Movie A')")
    cursor.execute("INSERT INTO options (poll_id, option_text) VALUES (4, 'Movie B')")
    cursor.execute("INSERT INTO options (poll_id, option_text) VALUES (4, 'Movie C')")

    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_database()
