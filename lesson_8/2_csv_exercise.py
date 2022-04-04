import csv
import json


### 1. Čtení

# Stáhnětě si soubor [starships.csv](star_wars/starships.csv)

# 1. Načtěte data pomocí modulu csv - nechám na vás jestli do slovníku nebo do seznamů.
# 2. Vypiště si data na výstup
# 3. Vypiště pouze jména a výrobce lodí, které mají kapacitu pro pasažéry alespoň 2.
#    Pokud hodnota není číslo, použijte k ošetření buď podmínky nebo vyjímky.
#    - Kolik takových lodí je?
# 4. Najděte loď, která má celkovou nejvyší kapacitu, tedy vejde se do ní nejvíc posádky a pasažérů (crew a passengers).
#    Pokud některá z hodnot není číslo, použijte k ošetření buď podmínky nebo vyjímky.

with open('star_wars/starships.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    # for row in reader:
    #     print(row)
    rows = list(reader)

no_ships = 0
for ship in rows:
    # Vyuzila jsem toho ze python vyhodnocuje podminky zleva a jelikoz chci aby platily vsechny,
    # tak pokud prvni neplati, python uz se dal nediva
    if ship['passengers'].isdigit() and int(ship['passengers']) >= 2:
        print(ship['name'], ship['manufacturer'])
        no_ships += 1

# Případně lze udělat nový list pomocí list comprehension a pomocí funkce len() dostat cislo
print(no_ships)


max_capacity = 0
best_ship = {}
for ship in rows:
    try:
        passengers, crew = int(ship['passengers']), int(ship['crew'])
        if passengers + crew > max_capacity:
            max_capacity = passengers + crew
            best_ship = ship
    except ValueError:
        # Pokud hodnota neni cislo, chci pokracovat dale v prochazeni dalsich lodi
        continue
print(best_ship)


### 2. Zápis

# Stáhnětě si soubor [vehicles.csv](star_wars/vehicles.csv)

# 1. Načtěte data pomocí modulu csv - nechám na vás jestli do slovníku nebo do seznamů.
# 2. Vypiště si data na výstup
# 3. Zapište do jednoho csv souboru pouze lodě, které mají `vehicle_class` starfighter nebo gunship.
#    - nezapomeňtě na header, tedy první řádek s názvy sloupců. Mohli by se vám hodit metody values a keys u slovníků.
# 4. Zapište do druhého csv souboru pouze subset parametrů, tedy vyberte si pouze sloupce které vás zajímají a ty zapiště do souboru.
#    - opět nezapomeňte na header

with open('star_wars/vehicles.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    # for row in reader:
    #     print(row)
    rows = list(reader)


with open('starships_filtered.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(rows[0].keys())
    for row in rows:
        if row['vehicle_class'] == 'starfighter' or row['vehicle_class'] == 'gunship':
            writer.writerow(row.values())

with open('starships_subset.csv', 'w', newline='') as csvfile:
    filednames = ['name', 'model', 'manufacturer']
    writer = csv.DictWriter(csvfile, fieldnames=filednames)
    writer.writeheader()
    for row in rows:
        new_row = {}
        for field in filednames:
            new_row[field] = row[field]
        writer.writerow(new_row)


### 3. (Bonus) Čtení pomocí csv, zápis pomocí json

# Stáhnětě si soubor [characters.csv](star_wars/characters.csv)

# 1. Načtěte si data pomocí `DictReader` z modulu `csv`.
# 2. Zapiště data pomocí některé z funkcí z modulu `json` do json souboru.
#    - Zapište do zvlášť json souboru pouze všechny ženy
#    - Zapište do zvlášť json souboru pouze všechny muže

with open('star_wars/characters.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    # for row in reader:
    #     print(row)
    rows = list(reader)

with open('all.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(rows, jsonfile, indent=4)

females = [char for char in rows if char['gender'] == 'female']
males = [char for char in rows if char['gender'] == 'male']

with open('females.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(females, jsonfile, indent=4)

with open('males.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(males, jsonfile, indent=4)
