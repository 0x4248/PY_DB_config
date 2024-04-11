# PY DB Config
# Use database files as a configuration file
# Github: https://www.github.com/0x4248/PY_DB_config
# Licence: GNU General Public License v3.0
# By: 0x4248

import sqlite3

class PY_DB_Config:
    def __init__(self, file):
        self.file = file
        self.conn = sqlite3.connect(self.file)
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS config (key TEXT, value TEXT)")
        self.conn.commit()

    def get(self, key):
        """Get a value from the database

        Args:
            key (str): The key to get the value of

        Returns:
            str: The value of the key. Will return None if the key does not exist
        """
        self.c.execute("SELECT value FROM config WHERE key = ?", (key,))
        result = self.c.fetchone()
        if result is None:
            return None
        else:
            return result[0]

    def set(self, key, value):
        """Set a value in the database

        Args:
            key (str): The key to set the value of
            value (str): The value to set the key to
        """   
        self.c.execute("SELECT value FROM config WHERE key = ?", (key,))
        result = self.c.fetchone()
        if result is None:
            self.c.execute("INSERT INTO config (key, value) VALUES (?, ?)", (key, value))
        else:
            self.c.execute("UPDATE config SET value = ? WHERE key = ?", (value, key))
        self.conn.commit()

    def delete(self, key):
        """Delete a key from the database

        Args:
            key (str): The key to delete
        """
        self.c.execute("DELETE FROM config WHERE key = ?", (key,))
        self.conn.commit()

    def close(self):
        """Close the database connection
        """
        self.conn.close()

    def exists(self, key):
        """Check if a key exists in the database

        Args:
            key (str): The key to check

        Returns:
            bool: True if the key exists, False if it does not
        """
        self.c.execute("SELECT value FROM config WHERE key = ?", (key,))
        result = self.c.fetchone()
        if result is None:
            return False
        else:
            return True