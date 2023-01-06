from pymongo import MongoClient


class MongoDatabase():
    def __init__(self) -> None:
        DB = "mongodb+srv://dblogin:TI0LJ1nUgFowNt7R@cluster0.9rytgvr.mongodb.net/?retryWrites=true&w=majority"
        self.db = MongoClient(DB)

    def add(self, database: str, collection: str, data: dict) -> None:
        self.db[database][collection].insert_many(data)

    def list_all(self):
        return self.db.list_database_names()
