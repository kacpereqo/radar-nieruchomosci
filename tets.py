import requests

url = "https://www.olx.pl/d/nieruchomosci/mieszkania/wynajem/"

html = requests.get(url).text
with open('olx.html', 'w', encoding="utf-8") as f:
    f.write(html)
