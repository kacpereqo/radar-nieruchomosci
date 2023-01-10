import ujson

import csv
import xml

from app.mongodb.service import MongoDatabase


class Converter():
    def __init__(self) -> None:
        self.data = MongoDatabase().read()

    def convert_to_csv(self):
        header = ["_id", "url", "is_owner_is_business", "city_id", "region_id", "is_rent",
                  "date", "price", "currency", "area", "rooms", "floor", "is_furnished", "built_type"]

        with open("test.csv", "w") as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            for offer in self.data:
                writer.writerow(offer)

    def convert_to_json(self):
        json = {}
        json['data'] = []

        for offer in self.data:
            offer['_id'] = str(offer['_id'])
            json['data'].append(offer)

        with open("test.json", "w", encoding='utf-8') as f:
            ujson.dump(json, f)


converter = Converter()
# converter.convert_to_csv()
converter.convert_to_json()
