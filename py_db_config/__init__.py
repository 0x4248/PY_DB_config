# PY DB Config
# Use database files as a configuration file
# Github: https://www.github.com/lewisevans2007/PY_DB_config
# Licence: GNU General Public License v3.0
# By: Lewis Evans

import sqlite3

class PY_DB_Config:
    def __init__(self, file):
        self.file = file
        self.conn = sqlite3.connect(self.file)
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS config (key TEXT, value TEXT)")
        self.conn.commit()

    def get(self, key):
        self.c.execute("SELECT value FROM config WHERE key = ?", (key,))
        result = self.c.fetchone()
        if result is None:
            return None
        else:
            return result[0]

    def set(self, key, value):
        self.c.execute("SELECT value FROM config WHERE key = ?", (key,))
        result = self.c.fetchone()
        if result is None:
            self.c.execute("INSERT INTO config (key, value) VALUES (?, ?)", (key, value))
        else:
            self.c.execute("UPDATE config SET value = ? WHERE key = ?", (value, key))
        self.conn.commit()

    def delete(self, key):
        self.c.execute("DELETE FROM config WHERE key = ?", (key,))
        self.conn.commit()

    def close(self):
        self.conn.close()

    def exists(self, key):
        self.c.execute("SELECT value FROM config WHERE key = ?", (key,))
        result = self.c.fetchone()
        if result is None:
            return False
        else:
            return True