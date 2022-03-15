"""
Napište funkci mult, která bude mít dva číselné parametry. Funkce oba parametry vynásobí a vrátí výsledek.
"""

def mult(a, b):
  return a * b

"""
Napiš funkci totalPrice, která vypočte cenu noci v hotelu.
Funkce bude mít dva parametry - persons (typ int) a breakfast (typ bool).
Cena za noc za osobu je 850 Kč a cena za snídani za osobu je 125 Kč.
Funkce vrátí výslednou cenu. Parametr breakfast je nepovinný a výchozí hodnota je False.
Funkci vyzkoušej se zadáním dvou i jedné hodnoty, např. totalPrice(3), totalPrice(2, True).
"""

def totalPrice(persons, breakfast=False):
  pricePerPerson = 850
  if breakfast:
    pricePerPerson += 125
  return pricePerPerson * persons

print(totalPrice(3))
print(totalPrice(3, True))

"""
Napiš funkce monthOfBirth, která bude mít jeden parametr - rodné číslo.
Funkce ze zadaného rodného čísla určí měsíc narození, které vrátí jako výstup.
Nezapomeň, že pro ženy je k měsíci připočtena hodnota 50.
Příklad: Pro hodnotu 9207054439 vrátí 7. Pro hodnotu 9555125899 vrátí 5.
"""

def monthOfBirth(birthNumber):
  month = birthNumber[2] + birthNumber[3]
  month = int(month)
  month = month % 50
  return month

print(monthOfBirth("9555125899"))

"""
Napiš funkci, která bude jednoduchou simulací rulety. Budeme uvažovat pouze možnost sázení na řady. Uživatel si může vybrat jednu ze tří řad:
- první řada (hodnoty 1, 4, 7 atd.),
- druhá řada (hodnoty 2, 5, 8 atd.),
- třetí řada (hodnoty 3, 6, 9 atd.).
- Zeptej se uživatele, na kterou ze tří řad sází a na výši sázky.
- Vytvoř funkci `roulette`, která bude mít parametry číslo řady a výši sázky. Pomocí funkce `randint` z modulu `random` vygeneruj náhodné číslo v rozsahu od 0 (včetně) do 36.  Vyhodnoť, do které řady číslo náleží. Nezapomeň, že 0 nepatří do žádné z řad a pokud padne, uživatel vždy prohrává.
- Funkce `roulette` vrací hodnotu výhry. Pokud uživatel vsadil na správnou řadu, vyhrává dvojnásobek sázky, v opačném případě nevyhrává nic jeho sázka propadá.
"""

import random

def roulette(row, bet):
  number = random.randint(0, 36)
  # kontrolní výpis
  print(f"Padlo číslo {number}.")
  if number == 0:
    return - bet
  if number % 3 == 1 and row == 1:
    return bet * 2
  if number % 3 == 2 and row == 2:
    return bet * 2
  if number % 3 == 0 and row == 3:
    return bet * 2
  return - bet

# alternativní řešení
# def roulette(row, bet):
#   number = random.randint(0, 36)
#   print(f"Padlo číslo {number}.")
#   if number == 0:
#     return - bet
#   rowModified = row % 3
#   if number % 3 == rowModified:
#     return bet * 2
#   return - bet

row = input("Zadej řadu: ")
bet = input("Zadej sázku: ")
win = roulette(int(row), float(bet))
print(win)