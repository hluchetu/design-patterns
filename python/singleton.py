import sqlite3


class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating Database object")
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):
        if hasattr(self, "_initialized"):
            return

        print("Opening database connection")
        self.connection = sqlite3.connect("katiba.db")
        self._initialized = True

    def create_tables(self) -> None:
        self.connection.execute(
            """
            CREATE TABLE IF NOT EXISTS articles (
                number INTEGER PRIMARY KEY,
                title TEXT NOT NULL
            )
            """
        )
        self.connection.commit()

    def add_article(self, number: int, title: str) -> None:
        self.connection.execute(
            """
            INSERT INTO articles (number, title)
            VALUES (?, ?)
            """,
            (number, title),
        )
        self.connection.commit()

    def find_article(self, number: int) -> tuple | None:
        cursor = self.connection.execute(
            """
            SELECT number, title
            FROM articles
            WHERE number = ?
            """,
            (number,),
        )
        return cursor.fetchone()

    def close(self) -> None:
        self.connection.close()
