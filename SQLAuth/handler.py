import sqlite3

class SQL():
    def __init__(self, database_name: str) -> None:
        self.database_path = database_name + ".db"
        self.conn = sqlite3.connect(self.database_path)
        "Local SQL connection"
        self.cur = self.conn.cursor()
        "Local SQL connection Cursor"
        self.create_if_not_exists()
    
    def create_if_not_exists(self):
        self.cur.execute("""
    CREATE TABLE IF NOT EXISTS licenses
    (key text, duration int, used_by text, created_by text, created_at int)
""")
        self.cur.execute("""
    CREATE TABLE IF NOT EXISTS users
    (key text, username text, first_use int, banned int, uuid text, ip text)
""")