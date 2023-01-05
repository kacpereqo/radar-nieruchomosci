import requests
from bs4 import BeautifulSoup
from schemas import Flat
from typing import List, Dict, Type

# |------------------------------------------------------------|#


class ScrapperService:
    def __init__(self, url):
        self.url = url

    def get_page_html(self) -> str:
        r = requests.get(self.url)
        return r.text

    def get_flats_urls(self) -> Dict[str, List[str]]:
        html = self.get_page_html()
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

        self.flat_urls = flat_urls

    def get_olx_flat_details(self, url: str) -> List[str]:
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')

        flat_data = soup.find_all('li', class_='css-ox1ptj')
        flat_data = [data.text for data in flat_data]
        flat_data.append(
            soup.find('h3', class_='css-19cr6mc-TextStyled er34gjf0').text)
        flat_data.append(url)

        return Flat(**self.filter_data_from_olx(flat_data))

    def filter_data_from_olx(self, flat_data: str) -> Dict[str, str]:
        data = {}

        data['owner'] = flat_data[0]
        data['price'] = int(flat_data[-2].replace('zł', '').replace(' ', ''))
        data['url'] = self.url + flat_data[-1]

        for i in flat_data[1:-2]:
            print(i)
            category, value = i.split(': ')

            if category == 'Cena':
                data['price'] = int(value)

            elif category == 'Powierzchnia':
                value = value.replace(' m²', '')
                data['area'] = int(value)

            elif category == 'Liczba pokoi':
                if value == 'Kawalerka':
                    value = 1
                else:
                    value = value.split(' ')[0]
                data['rooms'] = int(value)

            elif category == 'Poziom':
                if value == 'Parter':
                    value = 0
                data['floor'] = int(value)

            elif category == 'Rodzaj zabudowy':
                data['type_of_building'] = value

            elif category == 'Czynsz':
                data['rent'] = int(value)

        data['price_per_sqmeter'] = round(data['price'] / data['area'], 2)
        data['is_rent'] = True if self.url.split(
            '/')[-2] == 'wynajem' else False

        print(data)
        return data

    def get_Flats(self) -> List[Type[Flat]]:
        for url in self.flat_urls['olx']:
            self.get_olx_flat_details(url)


scrapper = ScrapperService(
    'https://www.olx.pl/d/nieruchomosci/mieszkania/wynajem/')

scrapper.get_flats_urls()
scrapper.get_Flats()
