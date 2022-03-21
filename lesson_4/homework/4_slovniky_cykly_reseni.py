# 1. Vysvědčení
# Uvažujme vysvědčení, které máme zapsané jako slovník.
# Napiš program, který spočte průměrnou známku ze všech předmětů.
# Uprav program, aby vypsal všechny předměty, ve kterých získal student známku 1.

school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}

sum_of_marks = 0
for mark in school_report.values():
    sum_of_marks += mark
print(f"Průměrná známka je {sum_of_marks/len(school_report)}.")

# Alternativní výpočet - využití funkce sum místo cyklu
print(f"Průměrná známka je {sum(school_report.values())/len(school_report)}.")

for subject, mark in school_report.items():
    if mark == 1:
        print(subject)


# 2. Čtenářský deník
# Gustav je vášnivým čtenářem detektivek z našeho nakladatelství a navíc si zapisuje knihy, které přečetl. Níže ve slovníku vidíme, jaké informace si eviduje - název knihy, počet stran a hodnocení od 0 do 10.

# Napiš program, který spočte celkový počet stran, které Gustav přečetl.
# Připiš do programu výpočet počtu knih, kterým dal Gustav hodnocení alespoň 8.
books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]

total_pages = 0
for book in books:
    total_pages += book["pages"]
print(f"Gustav celkem přečetl {total_pages} stran.")

print("Knihy, které mají hodnocení 8 a více:")
for book in books:
    if book["rating"] >= 8:
        print(book["title"])

# Pocet knih s hodnocenim 8 a vice

# 1 zpusob - list comprehension
print(len([book for book in books if book["rating"] >= 8]))
# 2. zpusob - klasicky for cyklus
count = 0
for book in books:
    if book["rating"] >= 8:
        count += 1
print(count)


# 3. Poznávací značky
# V následujícím slovníků je evidence automobilů. Klíčem jsou státní poznávací značky (SPZ)
# a hodnotou je jméno majitele vozu. Napiš program, který vypíše všechny majitele,
# jejichž vozidlo je registrováno v Plzeňském kraji, tj. na druhém místě (index 1!)
# řetězce v klíči je písmeno P.

plates = {"4A2 3000": "František Novák",
          "6P5 4747": "Jana Pilná",
          "3B7 3652": "Jaroslav Sečkár",
          "1P5 5269": "Marta Nováková",
          "37E 1252": "Martina Matušková",
          "2A5 2241": "Jan Král"}

for key, value in plates.items():
    if key[1] == "P":
        print(value)

# 4 Spolubydlící
# Zkus dotáhnout náš program na finanční vypořádání spolubydlících.
# Z lekce si můžeš zkopírovat kódy, které vytvoří slovník s útratami jednotlivých
# spolubydlících a výpočet průměrné útraty na osobu. Dopiš cyklus, který projde
# slovník sumPerPerson a pro každého ze spolubydlících vypíše, kolik by měl doplatit
# (pokud utratil(a) méně než průměr), případně kolik by měl obdržet (pokud utratil(a) více než průměr).

purchaseList = [
    {"person": "Petr", "item": "Prací prášek", "value": 399},
    {"person": "Ondra", "item": "Savo", "value": 80},
    {"person": "Petr", "item": "Toaletní papír", "value": 65},
    {"person": "Libor", "item": "Pivo", "value": 124},
    {"person": "Petr", "item": "Pytel na odpadky", "value": 75},
    {"person": "Míša", "item": "Utěrky na nádobí", "value": 130},
    {"person": "Ondra", "item": "Toaletní papír", "value": 120},
    {"person": "Míša", "item": "Pečící papír", "value": 30},
    {"person": "Zuzka", "item": "Savo", "value": 80},
    {"person": "Pavla", "item": "Máslo", "value": 50},
    {"person": "Ondra", "item": "Káva", "value": 300}
]

sum_per_person = {}
for item in purchaseList:
    person = item["person"]
    value = item["value"]
    if person in sum_per_person:
        sum_per_person[person] += value
    else:
        sum_per_person[person] = value

total_value = 0
for person, value in sum_per_person.items():
    total_value += value
    print(f"{person} utratil(a) za společné nákupy {value} Kč.")

average_value = total_value / len(sum_per_person)
print(f"Průměrná hodnota na osobu je {round(average_value)} Kč.")

# ^ Nahore je kod ktery lze zkopirovat z materialu ^

for person, num in sum_per_person.items():
    if num > average_value:
        print(f"{person} má obdržet {round(num - average_value)} Kč.")
    else:
        print(f"{person} má doplatit {round(average_value - num)} Kč.")
