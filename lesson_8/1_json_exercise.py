import requests

# 4 Seznam lidí
# Jak už jsme si ověřili v lekci, datové API na adrese http://api.kodim.cz/python-data/people obsahuje seznam lidí.
# Napište program, který tento seznam z API stáhne a převede z formátu JSON na Python slovníky.
# Proveďte následující úkoly.

# Zjistěte kolik lidí celkem seznam obsahuje.
# Zjistěte jaké všechny informace máme o jednotlivých osobách.
# Zjistěte, kolik je v souboru mužů a žen.

url = 'http://api.kodim.cz/python-data/people'
# response = requests.get(url)
# dict_response = response.json()

# print(dict_response)
# print(dict_response[0].keys())

# female, male = 0, 0
# for person in dict_response:
#     if person['gender'] == 'Female':
#         female += 1
#     if person['gender'] == 'Male':
#         male += 1
# print(f'Zeny {female}, Muzi {male}')

# pripadne list comprehension
# print(f'Zeny: {len([p for p in dict_response if p["gender"] == "Female"])}')
# print(f'Muzi: {len([p for p in dict_response if p["gender"] == "Male"])}')


# 5 Svátky
# Na adrese http://svatky.adresa.info/json najdete API, které vám odpoví, kdo má dneska svátek.

# Využijte toto API k tomu, abyste napsali program, který po spuštění vypíše na obrazovku kdo má dneska svátek.
# Pokud použijete adresu http://svatky.adresa.info/json?date=DDMM, kde místo DDMM doplníte datum, dostanete jméno, které má svátek v zadaný den.
# Formát DDMM znamená že 6. ledna bude zapsáno jako 0601, 12. září jako 1209 apod.
# Napište program, který dostane na příkazové řádce číslo dne a číslo měsíce a vypíše na výstup kdo má v daný den svátek.
# Použijte váš program abyste zjistili, kdo má svátek 29. února.

def get_name():
    url = 'http://svatky.adresa.info/json'
    response = requests.get(url)
    return response.json()[0]['name']

print(f'Dnes ma svatek {get_name()}')

day = input('Zadej den ve formatu DD: ')
month = input('Zadej mesic ve formatu MM: ')

def better_get_name(day, month):
    url = f'http://svatky.adresa.info/json?date={day}{month}'
    response = requests.get(url)
    #  pripadne jde i vyuzit params parameter funkce get, ten bere slovnik specifikujici parametry
    # response = requests.get(url, params={'date': day + month})
    return response.json()[0]['name']

print(better_get_name(day, month))
