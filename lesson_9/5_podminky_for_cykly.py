import sys

# 7 Heslo
# Napište program login.py, který na příkazovém řádku obdrží uživatelské jméno a heslo.
# Program bude mít v sobě uloženo správné heslo a pokud jej uživatel zadá,
# program vypíše něco ve smyslu “přístup povolen”. Zadá-li uživatel špatné heslo,
# program odpoví “přístup odepřen”.

# spravne_heslo = '1234'

# username, heslo = sys.argv[1:3]

# if heslo == spravne_heslo:
#     print('přístup povolen')
# else:
#     print('přístup odepřen')

# 8 Převod na USD
# Napište program usd.py, který bude umět převádět měnu na americké dolary. Když program zavoláte takto

# $ python3 usd.py czk 550
# převede 550 českých korun na americké dolary. Pokud jej zavoláte takto

# $ python3 usd.py eur 21
# převede 21 euro na americké dolary.

# Jako přídavek můžete do svého programu přidat tolik měn, kolik se vám líbí.

# mena, hodnota = sys.argv[1:3]
# hodnota = int(hodnota)

# # sem vygooglila kurz, pokud bychom chteli, tak muzeme doinstalovat nejaky modul na konverzi
# # napr. https://pypi.org/project/CurrencyConverter/
# czk_usd = 0.044
# eur_usd = 1.08

# if mena == 'czk':
#     hodnota *= czk_usd
# if mena == 'eur':
#     hodnota *= eur_usd

# print(f'USD: {round(hodnota, 2)}')


# 9 Banka
# Napište program, který z textového souboru přečte seznam zůstatků na spořících účtech
# a vypíše tyto zůstatky navýšené o 2.5% úrok.

# Vypište každý navýšený zůstatek na samostatný řádek.
# Vypište jen ty zůstatky, které nejsou záporné.
# Zkuste jednotlivé řádky očíslovat. Každý řádek tedy bude obsahovat číslo řádku a výsledný zůstatek.

# with open('zustatky.txt') as file:
#     zustatky = [int(num) for num in file.readlines()]

# for num in zustatky:
#     navyseny = num + num/100 * 2.5
#     print(navyseny)

# for num in zustatky:
#     navyseny = num + num/100 * 2.5
#     if navyseny > 0:
#         print(navyseny)

# radek = 0
# for num in zustatky:
#     navyseny = num + num/100 * 2.5
#     if navyseny > 0:
#         print(f'{radek:>2}. -- {navyseny:>10} Kc')
#     radek += 1

# 10 Hadanky - jen na koukani

# 11 Vzestupný seznam
# Napište program, který o zadaném seznamu celých čísel rozhodne,
# zda jsou čísla v tomto seznamu vzestupně seřazena.

# seznam = [1, 2, 3, 4]
# seznam_2 = [1, 5, 4]

# vzestupny = True
# previous = seznam[0]
# for num in seznam[1:]:
#     if num <= previous:
#         vzestupny = False
#         break # ukonci for cyklus predcasne
#     previous = num

# print('Vzestupny' if vzestupny else 'Neni vzestupny')

# 12 Písemky
# Napište program, který obdrží seznam známek z písemek a na výstup vypíše souhrn toho,
# kolik bylo dohromady jedniček, kolik dvojek, kolik trojek a tak dále.
# pisemky_znamky = [1,1,1,4,5]

# for znamka in [1, 2, 3, 4, 5]:
#     print(f'{znamka} se objevila {pisemky_znamky.count(znamka)}')

# 13 Maximum
# Zkuste napsat program, který na vstupu obdrží seznam čísel a najde mezi nimi nejvyšší číslo.
# Pozor, bez použití funkce max().
# nums = [34, 56, 78, 23, -1, 32]
# maximum = nums[0]
# for num in nums[1:]:
#     if num > maximum:
#         maximum = num
# print(maximum)

# 14 Druhé maximum
# Zkuste napsat program, který na vstupu obdrží seznam čísel a najde mezi nimi druhé nejvyšší číslo.
# Opět bez použití funkce max().

# Tady mi reseni prijde stejne jako priklad nize na k-te maximum

# 15 K-té maximum
# Napište program, který dostane na příkazové řádce posloupnost čísel.
# První číslo udává, kolikáté největší číslo chceme ve zbytku zadaných čísel najít.
# Můžeme tak chtít třeba páté největší číslo z 6, 1, 3, 8, 4, 7, 2

# $ python3 kmax.py 5 6 1 3 8 4 7 2
# 3
# Pokud je nějaké číslo v seznamu dvakrát, bere se jako dvě různá maxima.
# Nepoužívejte žádné Python funkce typu sorted nebo max. Napište všechno pěkně od píky.

# Možností, jak tento úkol vyřešit, je více. Nebojte se zagooglit, nebojte se být kreativní.

nums = [int(num) for num in sys.argv[1:]]
k = nums[0]
nums = nums[1:]

result = [nums[0]]

# Vnejsi cyklus pro k-te maximum
for _ in range(k):
    maximum = nums[0]
    # vnitrni cyklus vzdy najde maximum v danem seznamu
    for num in nums:
        if num > maximum:
            maximum = num
    result.append(maximum)
    # po tom co najdeme maximum ho ze seznamu vyhodime
    # tim zarucime ze dalsi iterace najde dalsi maximum
    nums.remove(maximum)

print(result[-1])

# sorted a index je nejjednodusi, zadani ale pozaduje vse napsat bez pouziti techto funkci
# print(sorted(nums)[-k])


# 16 Ruleta
# Na obrázku vidíte rozložení čísel na klasické Francouzské ruletě.
# Ruleta obsahuje čísla 0 - 36. Každé číslo s výjimkou nuly je buď sudé nebo liché a zároveň červené nebo černé.
# Pro čísla 1 až 10 a 19 až 28 platí, že lichá čísla jsou červená a sudá jsou černá.
# Pro zbytek platí obrácené pravidlo, tedy lichá jsou černá a sudá červená.
# Nula není ani lichá ani sudá, ani černá ani červená.

# Napište program, kterému uživatel zadá číslo a program odpoví jestli jde o číslo sudé nebo liché, černé nebo červené,
# nebo je to nula.

"""
Klíčová slova and a or jsou popsaná zde:
http://nove.kodim.cz/czechitas/progr2-python/zaklady-programovani-2/podminky-2
"""

# cislo = input("Zadej čislo: ")
# cislo = int(cislo)

# if cislo == 0:
#     print("Číslo je 0.")
# else:
#     if cislo % 2 == 0:
#         print("Číslo je sudé.")
#     else:
#         print("Číslo je liché.")
#     if cislo <= 10 or (cislo >= 19 and cislo <= 28):
#         if cislo % 2 == 0:
#             print("Číslo je černé.")
#         else:
#             print("Číslo je červené.")
#     else:
#         if cislo % 2 == 1:
#             print("Číslo je černé.")
#         else:
#             print("Číslo je červené.")

# 17 Přestupný rok
# Napište program, který po zadání kalendářního roku vypíše, zda jde o rok přestupný, či nikoliv.
# Letopočet je přestupný, pokud je dělitelný čtyřmi.
# Roky, které jsou dělitelné 100 jsou ovšem přestupné pouze tehdy, jsou-li zároveň dělitelné 400.

# rok = input("Zadej rok: ")
# rok = int(rok)
# if rok % 4 == 0:
#     if rok % 100 == 0:
#         if rok % 400 == 0:
#             print("Rok je přestupný.")
#         else:
#             print("Rok není přestupný")
#     else:
#         print("Rok je přestupný.")
# else:
#     print("Rok není přestupný.")

# """
# Alternativní řešení pomocí klíčových slov and a or.
# Klíčová slova and a or jsou popsaná zde:
# http://nove.kodim.cz/czechitas/progr2-python/zaklady-programovani-2/podminky-2
# """

# if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0):
#     print("Rok je přestupný.")
# else:
#     print("Rok není přestupný")