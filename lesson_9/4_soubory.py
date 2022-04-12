# 7 Pasažéři
# Autobus mezi Zdebudevsí a Kozoprdy jezdí čtyřikrát denně každý všední den v týdnu.
# Za poslední týden jsme naměřili počty pasažérů pro každou jízdu tam i zpět.
# Data jsou uložená v souboru pasazeri.txt.
# Jízda vždy obsahuje dvě čísla oddělená čárkou, která udávají počet pasažérů směrem tam a směrem zpět.

# Napište program, který pro první den vypíše, kolik pasažérů jelo celkem směrem tam a kolik směrem zpět.
# Nechť váš program vypisuje součty pasažérů ze celý týden, tedy kolik lidí za celý týden jelo směrem tam a kolik směrem zpět.

with open('data/pasazeri.txt', mode='r') as f:
    days = [line.split() for line in f.readlines()]

# print(days)

#  prvni den
first_day = [jizda.split(',') for jizda in days[0]]
tam = sum([int(jizda[0]) for jizda in first_day])
zpet = sum([int(jizda[1]) for jizda in first_day])
print(f'Tam: {tam}, Zpet: {zpet}')

# celkem za tyden
tam = sum([sum([int(jizda.split(',')[0]) for jizda in day]) for day in days])
zpet = sum([sum([int(jizda.split(',')[1]) for jizda in day]) for day in days])
print(f'Tam: {tam}, Zpet: {zpet}')

# 8 Preznamkovani
#  Bylo za DU, jeste nezverejneno

# 9 Karty 2
# Napište program, který vylosuje seznam 4 náhodných hracích karet podobně jako v úložce Karty 1 z minulé lekce.
# Můžeme si představovat, že rozdáváme karty například v pokeru.
# Zatím pro jednoduchost nebudeme řešit, že se nám může nějaká karta v seznamu opakovat.

# Vymyslete, jak budete vylosovanou kartu v seznamu reprezentovat. Vypište pak tento seznam na výstup.
# Dále k tomuto seznamu vypište součet hodnot všech vylosovaných karet.
# Položme hodnotu karet J, Q a K rovnu deseti a eso rovnu jedné.
import random
barvy = ['kříže', 'srdce', 'piky', 'káry']
hodnoty = [[2,2], [3,3], [4,4], [5,5], [6,6], [7,7], [8,8], [9,9], [10,10], [10,'J'], [10,'Q'], [10,'K'], [1,'A']]

# strasne neprehledne pomoci list comprehension, pouzila bych klasicky for cyklus
karty = [
    [hodnoty[random.randint(0, len(hodnoty)-1)], barvy[random.randint(0, len(barvy)-1)]]
    for i in range(4)]

print(karty)
hodnoty_karet = sum([karta[0][0] for karta in karty])
print(hodnoty_karet)

# hezci by bylo udelat si slovnik na prekladani hodnot karet a pak ho pouzit pro karty ktere nejsou cisla

# 10 Karty
# Zkusme vyřešit problém losování karet tak, aby se nám nemohlo stát, že nám nějaká karta padne vícekrát,
# když by správně v balíčku měla být od každé karty pouze jedna.

# Ze souboru karty.txt si načtěte do seznamu kompletní balíček karet.
# Zadání je stejné jako v předchozí úložce, tedy vylosovat 4 karty z balíčku a vypsat je jako seznam spolu se součtem hodnot.

# Existuje vícero možných postupů, které vedou ke stejnému výsledku.
# Zde už můžete trochu zagooglit. Ve většině postupů se vám bude hodit příkaz,
# který umí odstranit prvek seznamu na zadaném indexu:

# >>> x = [1, 2, 3]
# >>> del x[0]
# >>> x
# [2, 3]
# Také se vám může hodit funkce shuffle() z modulu random, která umí náhodně zamíchat seznam.

with open('data/karty.txt', mode='r') as f:
    cards = [card.split() for card in f.readlines()]

#  Nejjednodusi po googleni mi prijde pouzit funkci z modulu rando, ktera vraci vzorek n cisel (neopakuji se)
indexes = random.sample(range(0, len(cards)), 4)
#  no a kdyz se nam neopakuji indexy, tak ani karty nemuzou

cards = [cards[index] for index in indexes]
print(cards)

# dalsi moznost jak pocitat hodnoty
values = 0
values += sum([int(card[0]) for card in cards if card[0].isdigit()])
values += sum([10 for card in cards if card[0] in ['kluk', 'král', 'dáma']])
values += sum([1 for card in cards if card[0] == 'eso'])


print(values)
