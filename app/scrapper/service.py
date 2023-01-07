import tqdm
from .utils import extract_numbers_from_string
from .parsers import OlxParser
from typing import List, Dict
from bs4 import BeautifulSoup
import requests
from app.mongodb.service import MongoDatabase


# |------------------------------------------------------------|#


class ScrapperService:
    def __init__(self, url):
        self.url = url
        self.is_rent = True if 'wynajem' in url else False

    # |------------------------------------------------------------|#

    def get_page_html(self, page: int) -> str:
        if page == 1:
            r = requests.get(self.url)

        else:
            r = requests.get(f"{self.url}?page={page}")

        return r.text

    # |------------------------------------------------------------|#

    def get_number_of_pages(self) -> int:
        html = self.get_page_html(1)
        soup = BeautifulSoup(html, 'html.parser')
        results = extract_numbers_from_string(
            soup.find('div', {'data-testid': "total-count"}).text)
        return (int(results) // 40) + 1

    # |------------------------------------------------------------|#

    def get_flats_urls(self, page: int) -> Dict[str, List[str]]:
        html = self.get_page_html(page)

        soup = BeautifulSoup(html, 'html.parser')
        flats = soup.find_all('a', class_='css-rc5s2u')

        # sample olx href /d/oferta/kawalerka-do-wynajecia-CID3-IDNlGgA.html => [0] == "/"
        # sample otodom href https://www.otodom.pl/pl/oferta/mieszkanie-ul-glowackiego-o-pow-36-94m2-parter-ID4jFX9.html => [0] == "h"

        flat_urls = {"otodom": [], "olx": []}

        for flat in flats:
            href = flat.get('href')

            if href[0] == '/':
                flat_urls['olx'].append(f"https://www.olx.pl/{href}")

            elif href[0] == 'h':
                flat_urls['otodom'].append(href)

        return flat_urls

    # |------------------------------------------------------------|#

    def get_olx_flat_details(self, url: str) -> List[str]:
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')

        try:
            price = soup.find(
                'h3', class_='css-19cr6mc-TextStyled er34gjf0').text
            flat_details = soup.find_all('li', class_='css-ox1ptj')
            flat_details = [data.text for data in flat_details]

            localization = soup.find_all('a', class_='css-tyi2d1')
            localization = [x.text.split()[-1] for x in localization[-2:]]

            return OlxParser().parse(flat_details, price, url, self.is_rent, localization)

        except Exception as e:
            return None

    # |------------------------------------------------------------|#

    def scrap(self, save: bool = False):

        db = MongoDatabase() if save else None

        flats = []
        pages = self.get_number_of_pages()

        for page in tqdm.trange(1, 3, desc="[Scrapping]", position=0):
            flat_urls = self.get_flats_urls(page)

            for k, flat_url in flat_urls.items():
                if k == "olx":
                    for url in flat_url:
                        flats.append(self.get_olx_flat_details(url))

            if save:
                try:
                    db.add('offers', 'flat_offers', flats)
                except Exception as e:
                    print(e)
                flats = []

        return flats

    # |------------------------------------------------------------|#


scrapper = ScrapperService(
    'https://www.olx.pl/d/nieruchomosci/mieszkania/wynajem/')

flats = scrapper.scrap(save=True)
