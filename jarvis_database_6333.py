import sqlite3
import time

# Reusing the modular concept to keep it clean
class JarvisDatabase:
    def __init__(self):
        self.db_name = "jarvis_memory.db"
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS phases 
                            (id INTEGER PRIMARY KEY, phase_num INT, title TEXT, timestamp TEXT)''')
        self.conn.commit()

    def save_phase(self, num, title):
        ts = time.strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute("INSERT INTO phases (phase_num, title, timestamp) VALUES (?, ?, ?)", (num, title, ts))
        self.conn.commit()
        print(f"\033[1;32m[DATABASE] Phase {num} logged successfully at {ts}.\033[0m")

    def show_history(self):
        print("\n\033[1;37m--- JARVIS MEMORY HISTORY ---\033[0m")
        self.cursor.execute("SELECT * FROM phases ORDER BY id DESC LIMIT 5")
        for row in self.cursor.fetchall():
            print(f"ID: {row[0]} | Phase: {row[1]} | Task: {row[2]}")

if __name__ == "__main__":
    db = JarvisDatabase()
    # Logging the current progress
    db.save_phase(6333, "Neural-Database-Core-Sync")
    db.show_history()
