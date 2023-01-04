import requests
from bs4 import BeautifulSoup
from schemas import Flat
from typing import List, Dict, Type

# |------------------------------------------------------------|#


class ScrapperService:
    def __init__(self, url):
        self.url = url

    def get_html(self) -> str:
        r = requests.get(self.url)
        return r.text

    def get_flats_urls(self) -> Dict[str, List[str]]:
        html = self.get_html()
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

    # def get_olx_flat_details(self, url: str) -> Type[Flat]:
    #     html = self.get_html()
    #     soup = BeautifulSoup(html, 'html.parser')

    #     title = soup.find('h1', class_='css-1jy2b5v').text
    #     price = soup.find('strong', class_='css-1w6kz


scrapper = ScrapperService(
    'https://www.olx.pl/d/nieruchomosci/mieszkania/')

scrapper.get_flats_urls()
