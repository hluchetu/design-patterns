from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self)->None:
        pass

    @abstractmethod
    def execute(self,query:str)->None:
        pass


class SQLiteDatabase(Database):
    def connect(self) -> None:
        print("Connected to SQLite")

    def execute(self, query: str) -> None:
        print(f"SQLite executing: {query}")


class PostgreSQLDatabase(Database):
    def connect(self) -> None:
        print("Connected to PostgreSQL")

    def execute(self, query: str) -> None:
        print(f"PostgreSQL executing: {query}")


def create_database(database_type:str)->Database:
    if database_type == "sqlite":
        return SQLiteDatabase()

    if database_type == "postgres":
        return PostgreSQLDatabase()

    raise ValueError(f"Unsupported database type:{database_type}")
