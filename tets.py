import requests
from a import cities

url = "https://www.olx.pl/api/partner/cities"


headers = {"Authorization": "Bearer 9640ef08b5b76432be1100f97fde42b30d8b539d",
           "Version": "{{version}}"}
params = {"offset": 0}

print(len(cities))
cities_ids = {}
i = 0
while True:
    r = requests.get(url, headers=headers, params=params)
    data = r.json()

    for city in data["data"]:
        if city["name"] in cities:
            # print(city["name"], city['id'], city['region_id'])
            cities_ids[city["name"]] = [city['id'], city['region_id']]

    print(cities_ids.get('Warszawa', params["offset"]))

    if len(cities_ids) == len(cities):
        break

    params['offset'] += 1000


print("done")
