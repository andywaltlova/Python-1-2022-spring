import json
import csv
import requests

# 0. Otevirani souboru z minula

# with open('test.txt', mode='w', encoding='utf-8') as file:
#     nums = [1, 2, 3]
#     lines = [str(n) + '\n' for n in nums]
#     file.writelines(lines)


# 1. JSON
# https://kodim.cz/czechitas/python-data/zaklady-programovani/slovniky-json/#format-json
# https://docs.python.org/3/library/json.html#basic-usage
# loads : json str -> dictionary
# load : json file -> dictionary
# dump: dictionary -> file
# dumps : dictionary -> str

with open('absolventi.json', mode='r', encoding='utf-8') as file:
    data = json.load(file)


# absolventi = json.loads(text)
# for absolvent in absolventi:
#     print(absolvent)

# with open('absolventi2.json', mode='w', encoding='utf-8') as file:
#     json.dump(data, file, ensure_ascii=False, indent=4)

# json_string = json.dumps(data)
# json_obj = json.loads(json_string)

# print(type(json_string))
# print(type(json_obj))


# Requests - https://docs.python-requests.org/en/latest/user/quickstart/
url = 'https://swapi.dev/api/people'

# response = requests.get(url)
# print(response.json())
# json_data = response.json()
# print(json_data['results'])


# regiojet_url = 'https://brn-ybus-pubapi.sa.cz/restapi/routes/search/simple'
# params = {
#     'tariffs': 'REGULAR',
#     'toLocationType': 'STATION',
#     'toLocationId': '2704917000',
#     'fromLocationType': 'CITY',
#     'fromLocationId': '10202002',
#     'departureDate': '2022-04-05'
# }

# response = requests.get(regiojet_url, params=params)
# routes = response.json()['routes']

# with open('routes.json', mode='w') as f:
#     json.dump(routes, f, indent=4)




# CSV

import csv

with open('star_wars/planets.csv', mode='r', newline='') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    for row in rows:
        print(row)


