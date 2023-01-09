from .parsers import OlxParser
from typing import List, Dict
import requests
from app.mongodb.service import MongoDatabase


# |------------------------------------------------------------|#


class ScrapperService:
    def __init__(self, url):
        self.url = url
        self.db = MongoDatabase()

    # |------------------------------------------------------------|#

    def scrap(self, save: bool = False, city_id: int = 0, region_id: int = 0, category_id: int = 0) -> List[Dict]:

        _params = {
            "limit": "40",
            "category_id": "15",
            "region_id": "15",
            "filtSer_refiners": "spell_checker",
            "sl": "1857d191fc5x1238b41b",
            "sort_by": "filter_float_price:asc",
            "offset": "0",
            "filter_float_price:from": 0,
            "city_id": "4499",
            "offset": 0,
        }

        data = []
        urls = []

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
                        data.append(OlxParser().parse(offer, url=urls[-1]))
                        return data

                _params['offset'] = _params['offset'] + 40

                if _params['offset'] > 1000:
                    _params['filter_float_price:from'] = data[-1]['price']
                    _params['offset'] = 0

    # |--------------------------------------~----------------------|#


scrapper = ScrapperService("https://www.olx.pl/api/v1/offers/")

flats = scrapper.scrap(save=True)
print(flats)
