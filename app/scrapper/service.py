from pymongo.errors import BulkWriteError
import requests

from typing import List, Dict

from app.mongodb.service import MongoDatabase
from .parsers import OlxParser
from .constants import CITIES

# |------------------------------------------------------------|#


class ScrapperService:
    def __init__(self, url):
        self.url = url
        self.db = MongoDatabase()

    # |------------------------------------------------------------|#

    def scrap(self, city_id: int = 0, region_id: int = 0, category_id: int = 0) -> List[Dict]:

        _params = {
            "limit": "40",
            "category_id": "15",
            "region_id": region_id,
            "filtSer_refiners": "spell_checker",
            "sl": "1857d191fc5x1238b41b",
            "sort_by": "filter_float_price:asc",
            "offset": "0",
            "filter_float_price:from": 0,
            "city_id": city_id,
            "offset": 0,
        }

        data = []
        urls = []
        is_rent = True if category_id == 15 else False

        s = requests.Session()

        while True:

            r = s.get(self.url, params=_params)
            json = r.json()

            if json['data'] == []:
                return data

            else:

                for offer in json['data']:

                    if offer['url'] not in urls:
                        urls.append(offer['url'])
                        data.append(OlxParser().parse(
                            offer, url=urls[-1], city_id=city_id, region_id=region_id, is_rent=is_rent))

                _params['offset'] = _params['offset'] + 40

                if _params['offset'] > 1000:
                    _params['filter_float_price:from'] = data[-1]['price']
                    _params['offset'] = 0

    # |--------------------------------------~----------------------|#

    def scrap_all(self) -> List[Dict]:
        for region in CITIES:
            for city in CITIES[region]['cities'].values():
                print("Scraping: ", CITIES[region]['name'], city['name'])

                flats = self.scrap(city_id=city['id'], region_id=region)

                print("Found: ", len(flats), "flats in", city['name'])

                try:

                    if flats != []:
                        self.db.add('offers', 'flat_offers', flats)
                        print("Added: ", len(flats), "flats in", city['name'])

                except BulkWriteError:
                    pass

                except Exception as e:
                    print(e)

                print("----------------------------------")


scrapper = ScrapperService("https://www.olx.pl/api/v1/offers/")

flats = scrapper.scrap_all()
