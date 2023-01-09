import json
import requests
import pprint
from bs4 import BeautifulSoup


class ScrapperCity():
    def __init__(self) -> None:
        self.url = "https://www.olx.pl/d/nieruchomosci/mieszkania"

    def get_page(self, region=""):
        return requests.get(f"{self.url}/{region}")

    def replace_polsish_letters(self, word: str) -> str:
        word = word.lower().replace("ś", "s").replace("ł", "l").replace("ż", "z").replace("ź", "z").replace(
            "ó", "o").replace("ą", "a").replace("ę", "e").replace("ć", "c").replace("ń", "n")
        return word

    def get_cities(self):
        cities_dict = {}
        result = []

        page = self.get_page()
        soup = BeautifulSoup(page.content, 'html.parser')

        regions = soup.find_all('ul', class_='css-1dz1uxb')[2]
        for region in regions:

            region = self.replace_polsish_letters(region.text.split(' ')[0])
            cities_dict[region] = []

            page = self.get_page(region)

            soup = BeautifulSoup(page.content, 'html.parser')
            cities = soup.find_all('ul', class_='css-1dz1uxb')[2]

            for city in cities:
                result.append(city.text.split(' ')[0])

        return result


scrapper = ScrapperCity()
pprint.pprint(scrapper.get_cities())
