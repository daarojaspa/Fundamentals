"""only one object  of this sort in all aplication and that can be shared in all aplications"""

"""class constructur should be private"""
"""create method acts as interface between constructor and outsite wrld , ensures
that only one method is created """
import sqlite3

class DatabaseHandler:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if self._initialized:
            return

        self._db_path = "db.sqlite"
        self.conn = None

        self._initialized = True

    @classmethod
    def get_instance(cls):
        return cls()

    def connect(self):
        if self.conn is None:
            self.conn = sqlite3.connect(self._db_path)

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def write(self, query, params=()):
        self.connect()  # ensure connection
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        self.conn.commit()
        self.close()
        return True
    def read(self,query,params=()):
        self.connect()  # ensure connection
        cursor = self.conn.cursor()
        data=cursor.execute(query, params)
        self.close()
        return data
