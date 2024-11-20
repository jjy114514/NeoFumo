import sqlite3

class Database:
    def __init__(self, db_name='chat.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS conversations
                          (id INTEGER PRIMARY KEY, speaker TEXT, text TEXT)''')
        self.conn.commit()

    def insert_conversation(self, speaker, text):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO conversations (speaker, text) VALUES (?, ?)', (speaker, text))
        self.conn.commit()