from pymongo import MongoClient

from datetime import datetime


class MongoDatabase():
    def __init__(self) -> None:
        DB = "mongodb+srv://dblogin:TI0LJ1nUgFowNt7R@cluster0.9rytgvr.mongodb.net/?retryWrites=true&w=majority"
        self.db = MongoClient(DB)

        self.create_collection()

    def add(self, database: str, collection: str, data) -> None:
        self.db[database][collection].insert_many(data)

    def create_collection(self) -> None:
        try:
            self.db.offers.flat_offers.create_index(
                [('url', 1), ('date', 1)], unique=True)
        except Exception as e:
            print(e)
            pass
