from abc import ABC, abstractmethod
from typing import List, Dict
from datetime import datetime


class Parser(ABC):

    @abstractmethod
    def parse(self, html: str) -> List[Dict[str, str]]:
        pass


class OtoDomParser(Parser):

    def parse(self, html: str) -> List[Dict[str, str]]:
        pass


class OlxParser(Parser):

    def parse(self, offer: Dict, url: str, city_id: int, region_id: int, is_rent: bool) -> List[Dict[str, str]]:
        data = {}

        word_to_number_en = {
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
        }

        data['url'] = url.split("/")[-1]
        data['is_owner_is_business'] = offer['business']
        data['city_id'] = city_id
        data['region_id'] = region_id
        data['is_rent'] = is_rent
        data['date'] = datetime.now().strftime("%Y/%m/%d")

        for param in offer['params']:
            if param['key'] == 'floor_select':
                data['floor'] = param['value']['label']

            if param['key'] == 'furniture':
                data['is_furnished'] = True if param['value']['key'] == 'yes' else False

            elif param['key'] == 'price':
                data['price'] = param['value']['value']
                data['currency'] = param['value']['currency']

            elif param['key'] == 'm':  # area
                data['area'] = param['value']['key']

            elif param['key'] == 'builttype':
                data['built_type'] = param['value']['key']

            elif param['key'] == 'rooms':
                data['rooms'] = word_to_number_en[param['value']['key']]

        return data
