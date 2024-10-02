import sqlite3 as sql


def get_leaderboard():
    conn = sql.connect("leaderboard.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM leaderboard ORDER BY score DESC")
    leaderboard = cur.fetchall()
    conn.close()
    return leaderboard

def add_to_leaderboard(name:str, score:int):
    conn = sql.connect("leaderboard.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS leaderboard (name TEXT, score INTEGER)")
    cur.execute("INSERT INTO leaderboard (name, score) VALUES (?, ?)", (name, score))
    conn.commit()
    conn.close()

