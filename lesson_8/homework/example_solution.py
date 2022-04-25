import json
import requests
import datetime
 
 
# 1 Načtěte si json data z http://hp-api.herokuapp.com/api/characters
def get_json_data_from_api(url):
    response = requests.get(url)
    return response.json()
 
# 2 Uložte je do `hp_characters.json` souboru naformátovaná, tedy ne na jeden řádek.
def save_data_to_json_file(data, filename):
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=True)
 
# 3 Načtěte json data ze souboru, funkce může být obecná, v úkolu však budete načítat jen soubor který jste si v předchozím bodu vytvořily.
def get_json_data_from_file(filename):
    with open(filename, mode='r', encoding="utf-8") as file:
        data = json.load(file)
    return data
 
# 4 Zjistětě:
#    Kolik různých patronů (klíč `"patronus"`) v datech existuje
#    Kolik postav už nežije
#    Která postava je nejstarší
#      - použijte pouze klíč `yearOfBirth`
#      - na zpracování celého datumu bychom mohli použít modul datetime, datetime objekty se pak dají porovnávat klasicky pomocí `>` a `<`.
def print_information(data):
    patrons = [ch['patronus'] for ch in data]
    unique_values = set(patrons)
    unique_values.remove("")
    print(f'V datasetu je {len(unique_values)} unikátních patronů.')
 
    not_alive = [ch for ch in data if not ch['alive']]
    print(f'V datasetu je {len(not_alive)} postav, které už nežijí.')
 
    # Bez datetime
    oldest_char = get_oldest_character_by_year(data)
    print(f'Nejstarsi postava je: {oldest_char["name"]}')
 
    # S datetime
    oldest_char = get_oldest_character_by_date(data)
    print(f'Nejstarsi postava je: {oldest_char["name"]}')
 
def get_oldest_character_by_year(data):
    oldest_char = data[0]
    for char in data:
        # Porovnavam jen pokud jsou data k dispozici
        if char['yearOfBirth'] != "":
            year = int(char['yearOfBirth'])
            if year < int(oldest_char['yearOfBirth']):
                oldest_char = char
    return oldest_char
 
def get_oldest_character_by_date(data):
    oldest_char = data[0]
    for char in data:
        # Porovnavam jen pokud jsou data k dispozici
        if char['dateOfBirth'] != "":
            datetime_format = '%d-%m-%Y'
            date = datetime.datetime.strptime(char['dateOfBirth'], datetime_format)
            oldest_date_so_far = datetime.datetime.strptime(oldest_char['dateOfBirth'], datetime_format)
            if date < oldest_date_so_far:
                oldest_char = char
    return oldest_char
 
# 5 Zapište to souboru `gryffindor.json` pouze postavy, které mají v klíči `house` hodnotu `"Gryffindor"`
def save_gryffindor_to_json_file(data, filename):
    filtered_data = [ch for ch in data if ch['house'] == 'Gryffindor']
 
    # Nemusím duplikovat kód, funkci jsem si udělala dostatečně obecnou takže ji mohu použít znovu
    save_data_to_json_file(filtered_data, filename)
 
 
 
url = 'http://hp-api.herokuapp.com/api/characters'
data = get_json_data_from_api(url)
 
file = 'hp_characters.json'
save_data_to_json_file(data, file)
data = get_json_data_from_file(file)
print_information(data)
save_gryffindor_to_json_file(data, 'gryffindor.json')