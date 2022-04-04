# 1. JSON - https://kodim.cz/czechitas/python-data/zaklady-programovani/slovniky-json/#format-json


# 2. CSV - lesson_8 materialy

import csv
with open('star_wars/planets.csv') as f:
    reader = csv.reader(f, delimiter=',')
    # print(list(reader))

with open('star_wars/planets.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    print(list(reader))