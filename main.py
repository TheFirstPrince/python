import sqlite3

connection = sqlite3.connect("database.db")

cursor = connection.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hero TEXT,
    kills INTEGER
)
"""
)

connection.commit()

connection.close()

print("База данных успешно готова к работе")