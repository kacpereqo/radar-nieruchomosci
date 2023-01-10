from abc import ABC, abstractmethod
from typing import List, Dict
from datetime import datetime


class Parser(ABC):

    @abstractmethod
    def parse(self, html: str) -> List[Dict[str, str]]:
        pass

# |------------------------------------------------------------|#


class OtoDomParser(Parser):

    def parse(self, html: str) -> List[Dict[str, str]]:
        pass

# |------------------------------------------------------------|#


class OlxParser(Parser):

    def parse(self, offer: Dict, url: str, city_id: int, region_id: int, is_rent: bool) -> List[Dict[str, str]]:
        data = {}

        _word_to_number_en = {
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
        }

        data['url'] = url.split("/")[-1]
        data['is_owner_is_business'] = offer['business']
        data['city_id'] = int(city_id)
        data['region_id'] = int(region_id)
        data['is_rent'] = is_rent
        data['date'] = datetime.now().strftime("%Y/%m/%d")

        for param in offer['params']:

            """
            -1  - suterena
             0  - parter
             11 - powyżej 10
             12 - poddasze
            """

            if param['key'] == 'floor_select':
                if param['value']['label'] == 'Parter':
                    data['floor'] = 0

                elif param['value']['label'] == 'Powyżej 10':
                    data['floor'] = 11

                elif param['value']['label'] == 'Suterena':
                    data['floor'] = -1

                elif param['value']['label'] == 'Poddasze':
                    data['floor'] = 12

                else:
                    data['floor'] = int(param['value']['label'])

            if param['key'] == 'furniture':
                data['is_furnished'] = True if param['value']['key'] == 'yes' else False

            elif param['key'] == 'price':
                data['price'] = int(param['value']['value'])
                data['currency'] = param['value']['currency']

            elif param['key'] == 'm':  # area
                data['area'] = int(param['value']['key'].split(".")[0])

            elif param['key'] == 'builttype':
                data['built_type'] = param['value']['key']

            elif param['key'] == 'rooms':
                data['rooms'] = _word_to_number_en[param['value']['key']]

        return data

# |------------------------------------------------------------|#
