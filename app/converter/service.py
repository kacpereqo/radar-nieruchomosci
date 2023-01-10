import ujson

import io
import gzip
import csv

from app.mongodb.service import MongoDatabase

# |------------------------------------------------------------|#


class Converter():
    def __init__(self) -> None:
        self.client = MongoDatabase()

# |------------------------------------------------------------|#

    def convert_to_csv(self):
        header = ["is_owner_is_business", "city_id", "region_id", "is_rent",
                  "date", "price", "area", "rooms", "floor", "is_furnished", "built_type"]

        schema = {
            "_id": 0,
            "url": 0,
            "currency": 0,
        }

        data = self.client.db.offers.flat_offers.find({}, schema)

        with gzip.GzipFile("test.gz", mode='wb', compresslevel=6) as gz:
            buff = io.StringIO()

            writer = csv.DictWriter(buff, fieldnames=header)
            writer.writeheader()

            writer.writerows(data)
            gz.write(buff.getvalue().encode('utf-8'))

# |------------------------------------------------------------|#

    def convert_to_json(self):
        json = {}
        json['data'] = []

        for offer in self.data:
            offer['_id'] = str(offer['_id'])
            json['data'].append(offer)

        with open("test.json", "w", encoding='utf-8') as f:
            ujson.dump(json, f)

# |------------------------------------------------------------|#


converter = Converter()
converter.convert_to_csv()
# converter.convert_to_json()
