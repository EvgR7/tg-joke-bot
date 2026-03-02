import sqlite3
from datetime import datetime
conn = sqlite3.connect('stats.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, jokes_count INTEGER DEFAULT 0, 
word_jokes_count INTEGER DEFAULT 0, first_seen TEXT, last_seen TEXT)""")
conn.commit()


def add_user(user_id):
    now = datetime.now().isoformat()
    cursor.execute("""INSERT OR IGNORE INTO users (user_id, first_seen, last_seen) 
    VALUES (?, ?, ?)""",(user_id, now, now))
    conn.commit()

def get_stats():
    cursor.execute("""SELECT COUNT(*) FROM users""")
    total_users = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(jokes_count) FROM users")
    total_jokes = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(word_jokes_count) FROM users")
    total_word_jokes = cursor.fetchone()[0] or 0

    return total_users, total_jokes, total_word_jokes


def udate_last_seen(user_id):
    now = datetime.now().isoformat()
    cursor.execute("""UPDATE users SET last_seen = ? WHERE user_id = ?""", (now, user_id))
    conn.commit()


def increment_joke(user_id):
    cursor.execute("""UPDATE users SET jokes_count = jokes_count + 1 WHERE user_id = ?""", (user_id,))
    conn.commit()


def increment_word_joke(user_id):
    cursor.execute("""UPDATE users SET word_jokes_count = word_jokes_count + 1 WHERE user_id = ?""", (user_id,))
    conn.commit()
