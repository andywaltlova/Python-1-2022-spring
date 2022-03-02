"""
V proměnné níže naleznete data, která budete zpracovávat/upravovat/filtrovat v následujících úkolech.

Jako první si tedy prohlédněte jak data vypadají, jaká je struktura dat.
Připomínám že hranaté závorky značí listy, složené značí slovníky.
Prohlédněte si také datové typy jednotlivých hodnot.

1. Upravte data, tak aby hodnoty měli odpvídající datový typ.

To znamená například hodnoty u klíče "height" by velice pravděpodobně měli být čísla. Stačí upravit číselné hodnoty (pro počítání v dalších úkolech).
S hodnotami 'birth_year' nebo 'gravity' příliš dělat nejde a dál se s nimi v úkolu nijak nepočítá.
Než budete upravů zkoušet pro všechny data, klidně si nejdřív vemte jen první slovník (data[0]) a zkoušejte si to na něm.
Pozor ale, že některá číselná data nejsou dostupná u všech slovníků, například "population" je u některých planet "unknown".
Zde se vám bude hodit kontrolovat, zda string opravdu obsahuje čísla. Můžete k tomu využít metodu isdigit() - https://docs.python.org/3/library/stdtypes.html#str.isdigit.
Pokud hodnota neexistuje, nebo nejde smysluplně převést, nahradtě ji například  -1, 0.

2. Spočítejte průměrnou výšku všech postav.

3. Vytvořte seznam seznamů s jmeny postav seskupené podle pohlaví. Tedy jeden seznam se seznamy kde jou ženy, jeden kde jsou muži, případně další pohlaví.
Doporučuji nejdřív zjistit jakých hodnot (pozor unikátních hodnot, hint: list se dá předělat na množinu) klíč "gender" nabývá, pak už pro každou hodnotu můžete data filtrovat v cyklu.

Bonus: Zkuste misto seznamu seznamů, vytvořit slovník, kde klíč je daný gender a hodnotou je list se jmény postav.

4. Vypiště jména postav, které mají bílou kůži nebo vlasy. Tedy v "hair_color" nebo v "skin_color" se nachází "white".

5. Vytvořte seznam obsahující pouze planety. Tedy seznam který v sobě bude mít slovníky obsahující planety.
Zamyslete se, jakým způsobem byste řešili duplicity planet, v našem případě hned dvě postavy žijí na planetě Tatooine.
"""

data = [
    {
        "name": "Luke Skywalker",
        "height": "172",
        "mass": "77",
        "hair_color": "blond",
        "skin_color": "fair",
        "eye_color": "blue",
        "birth_year": "19BBY",
        "gender": "male",
        "homeworld": {
            "name": "Tatooine",
            "rotation_period": "23",
            "orbital_period": "304",
            "diameter": "10465",
            "climate": "arid",
            "gravity": "1 standard",
            "terrain": "desert",
            "surface_water": "1",
            "population": "200000"},
    },
    {
        "name": "Obi-Wan Kenobi",
        "height": "182",
        "mass": "77",
        "hair_color": "auburn, white",
        "skin_color": "fair",
        "eye_color": "blue-gray",
        "birth_year": "57BBY",
        "gender": "male",
        "homeworld": {
            "name": "Stewjon",
            "rotation_period": "unknown",
            "orbital_period": "unknown",
            "diameter": "0",
            "climate": "temperate",
            "gravity": "1 standard",
            "terrain": "grass",
            "surface_water": "unknown",
            "population": "unknown"}
    },
    {
        "name": "R2-D2",
        "height": "96",
        "mass": "32",
        "hair_color": "n/a",
        "skin_color": "white, blue",
        "eye_color": "red",
        "birth_year": "33BBY",
        "gender": "n/a",
        "homeworld": {
            "name": "Naboo",
            "rotation_period": "26",
            "orbital_period": "312",
            "diameter": "12120",
            "climate": "temperate",
            "gravity": "1 standard",
            "terrain": "grassy hills, swamps, forests, mountains",
            "surface_water": "12",
            "population": "4500000000"}
    },
    {
        "name": "Darth Vader",
        "height": "202",
        "mass": "136",
        "hair_color": "none",
        "skin_color": "white",
        "eye_color": "yellow",
        "birth_year": "41.9BBY",
        "gender": "male",
        "homeworld": {
            "name": "Tatooine",
            "rotation_period": "23",
            "orbital_period": "304",
            "diameter": "10465",
            "climate": "arid",
            "gravity": "1 standard",
            "terrain": "desert",
            "surface_water": "1",
            "population": "200000"}
    },
    {
        "name": "Chewbacca",
        "height": "228",
        "mass": "112",
        "hair_color": "brown",
        "skin_color": "unknown",
        "eye_color": "blue",
        "birth_year": "200BBY",
        "gender": "male",
        "homeworld": {
            "name": "Kashyyyk",
            "rotation_period": "26",
            "orbital_period": "381",
            "diameter": "12765",
            "climate": "tropical",
            "gravity": "1 standard",
            "terrain": "jungle, forests, lakes, rivers",
            "surface_water": "60",
            "population": "45000000"}
    },
    {
        "name": "Yoda",
        "height": "66",
        "mass": "17",
        "hair_color": "white",
        "skin_color": "green",
        "eye_color": "brown",
        "birth_year": "896BBY",
        "gender": "male",
        "homeworld": {
            "name": "unknown",
            "rotation_period": "0",
            "orbital_period": "0",
            "diameter": "0",
            "climate": "unknown",
            "gravity": "unknown",
            "terrain": "unknown",
            "surface_water": "unknown",
            "population": "unknown", }
    },
    {
        "name": "Leia Organa",
        "height": "150",
        "mass": "49",
        "hair_color": "brown",
        "skin_color": "light",
        "eye_color": "brown",
        "birth_year": "19BBY",
        "gender": "female",
        "homeworld": {
                "name": "Alderaan",
                "rotation_period": "24",
                "orbital_period": "364",
                "diameter": "12500",
                "climate": "temperate",
                "gravity": "1 standard",
                "terrain": "grasslands, mountains",
                "surface_water": "40",
                "population": "2000000000"}
    },
]

# 1
# Ideálně by mass, height, rotation_period, orbital_period, diameter, surface_water a population meli byt cisla

for person in data:
    person['height'] = int(person['height'])
    person['mass'] = int(person['height'])

    planet = person['homeworld']
    keys_to_convert = ['rotation_period', 'orbital_period', 'diameter', 'surface_water', 'population']
    for key in keys_to_convert:
        value = planet[key]
        if value.isdigit():
            planet[key] = int(value)
        else:
            planet[key] = -1

# Pro kontrolu
# for d in data:
#     print(d)

# 2

heights = [person['height'] for person in data]
avg = round(sum(heights) / len(heights), 2)
print(f'Prumerna vyska postav je {avg} cm.')


# 3

# ziskání hodnot, které klic gender nabývá
genders = set([person['gender'] for person in data])

# Vice variant reseni

# Oba klasicke for cykly
list_of_lists = []
for gender in genders:
    names = []
    for person in data:
        if person['gender'] == gender:
            names.append(person['name'])
    list_of_lists.append(names)

# Kombinace klasickeho cyklu a list comprehension
list_of_lists = []
for gender in genders:
    names = [person['name'] for person in data if person['gender'] == gender]
    list_of_lists.append(names)

# Pouze List comprehension
list_of_lists = [[person['name'] for person in data if person['gender'] == gender] for gender in genders]

print(list_of_lists)


# Bonus

# Cykly
gender_dict = {}
for gender in genders:
    names = []
    for person in data:
        if person['gender'] == gender:
            names.append(person['name'])
    gender_dict[gender] = names

# Dict comprehension
gender_dict = {gender:[person['name'] for person in data if person['gender'] == gender] for gender in genders}

print(gender_dict)

# 4

for person in data:
    has_white_hair = 'white' in person['hair_color']
    has_white_skin = 'white' in person['skin_color']

    if has_white_hair or has_white_skin:
        print(person['name'])

# 5

# Cele objekty
planets = [person['homeworld'] for person in data]

# Kdybychom chteli pouze objekty ktere nejsou 'unknown'
planets = [person['homeworld'] for person in data if person['homeworld']['name'] != 'unknown']

# Jen jmena
planets = [person['homeworld']['name'] for person in data]

print(planets)

# Duplicit se muzeme zbavit napriklad predelanim na mnozinu.

# V pripade jmen staci
planets = set(planets)
print(planets)

# V pripade slovniku nesaci pouzit pouze set(), protoze python neumi poznat zda jsou dva slovniky totozne.
# V tomto pripade by bylo k zamysleni, jaky udaj nam unikatne identifikuje planetu. Mohli bychom napriklad vytvorit slovnik,
# kde klice jsou jmena planet (coz by zajistilo unikatnost) a hodnoty by byly zbyla data o planetach.
