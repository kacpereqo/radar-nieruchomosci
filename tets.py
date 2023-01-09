from a import cities_id

temp = {}
for city in cities_id:
    temp[city["id"]] = {}
    temp[city["id"]]['name'] = city["name"]
    temp[city["id"]]['cities'] = {}
    for y in city['subregions']:
        temp[city["id"]]['cities'][y['name']] = {
            "id": y['id'],
            "name": y['name'],
            "long_name": y['name_long']
        }

with open("c.py", "w", encoding="utf-8") as f:
    f.write(f"CITIES = {temp}")
