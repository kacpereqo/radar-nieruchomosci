from abc import ABC, abstractmethod
from typing import List, Dict
from datetime import datetime
from .utils import extract_numbers_from_string


class Parser(ABC):

    @abstractmethod
    def parse(self, html: str) -> List[Dict[str, str]]:
        pass


class OtoDomParser(Parser):

    def parse(self, html: str) -> List[Dict[str, str]]:
        pass


class OlxParser(Parser):

    def parse(self, flat_details: str, price: str, url: str, is_rent: bool, localization: List) -> List[Dict[str, str]]:
        data = {}

        data['url'] = url
        data['is_rent'] = is_rent
        data['owner'] = flat_details[0]
        data['price'] = self.get_price(price)
        data['state'] = localization[0]
        data['city'] = localization[1]
        data['date'] = datetime.now()

        for i in flat_details[1:]:
            category, value = i.split(': ')

            if category == 'Powierzchnia':
                data['area'] = self.get_area(value)

            elif category == 'Liczba pokoi':
                data['rooms'] = self.get_rooms(value)

            elif category == 'Poziom':
                data['floor'] = self.get_floor(value)

            elif category == 'Rodzaj zabudowy':
                data['type_of_building'] = value

        data['price_per_sqmeter'] = round(data['price'] / data['area'], 2)

        return data

    def get_area(self, data: str) -> float:
        area = float(extract_numbers_from_string(data))
        return area

    def get_rooms(self, data: str) -> int:
        if data == 'Kawalerka':
            rooms = 1
        else:
            rooms = int(extract_numbers_from_string(data))
        return rooms

    def get_floor(self, data: str) -> int:
        if data == 'Parter':
            floor = 0
        else:
            floor = int(extract_numbers_from_string(data))
        return floor

    def get_price(self, data: str) -> int:
        price = float(extract_numbers_from_string(data))
        return price
