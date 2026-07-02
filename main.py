import sqlite3

# 1. СВЯЗЬ С ФАЙЛОМ
connection = sqlite3.connect("database.db")

# 2. ПОЛУЧЕНИЕ ИНСТРУМЕНТА
cursor = connection.cursor()

# 3. ПОДГОТОВКА ДАННЫХ
sql_insert = "INSERT INTO games (hero, kills) VALUES (?, ?)"
new_game = ("Lina", 16)

# 4. ОТПРАВКА КОМАНДЫ
cursor.execute(sql_insert, new_game)

# 5. СОХРАНЕНИЕ НА ДИСК
connection.commit()

# 6. ЧТЕНИЕ ИЗ БАЗЫ
cursor.execute("SELECT * FROM games")
all_games = cursor.fetchall()

# 7. ВЫВОД НА ЭКРАН
print("\n--- Твоя история матчей ---")
for game in all_games:
    print(f"ID матча: {game[0]} | Герой: {game[1]} | Убийств: {game[2]}")

# 8. ЗАКРЫТИЕ ФАЙЛА
connection.close()