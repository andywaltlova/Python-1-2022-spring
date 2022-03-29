"""
Výplata přesněji
Zatím jsme výplatu počítali za předpokladu, že každý měsíc odpracujeme stejný počet hodin,
což není příliš realistické. Vytvořte proto textový soubor vykaz.txt, který bude obsahovat 12
řádků a na každém řádku počet odpracovaných hodin za každý měsíc za poslední rok.

Otevřete tento soubor ve svém programu a načtěte hodnoty na řádcích do seznamu vykaz.
Vytiskněte tento seznam na konzoli funkcí print() abyste si ověřili, že jste soubor načetli správně.
Nechte uživatele zadat na příkazovém řádku hodinovou mzdu.
Spočítejte a na výstup vytiskněte celkovou výplatu za celý rok a průměrnou výplatu na jeden měsíc.
"""

with open('vykaz.txt') as f:
    # Takto bych to napsala elegantne a zkracene, samozrejme je mozne si rozepsat kod do vice radku
    hours_per_month = [int(line) for line in f.readlines()]

hour_pay = int(input('Zadej hodinovou mzdu: '))

# Mohli bychom toto predelani na cislo klidne dat do try, except bloku
# try:
#     hodinova_mzda = int(input('Zadej hodinovou mzdu: '))
# except ValueError:
#     print('Zadej ciselnou hodnotu!')
#     exit(1)

year_salary = sum(hours_per_month) * hour_pay
average_per_month = round(year_salary / len(hours_per_month))

print(f'Celkovy rocni plat: {year_salary} Kc')
print(f'Prumerny mesicni plat: {average_per_month} Kc')

# Pokud byste chteli vyuzit funkce, muzete si klidne obalit kazde cviceni do funkce a tu potom pouze volat
def vyplata():
    with open('vykaz.txt') as f:
        hours_per_month = [int(line) for line in f.readlines()]

    hour_pay = int(input('Zadej hodinovou mzdu: '))
    year_salary = sum(hours_per_month) * hour_pay
    average_per_month = round(year_salary / len(hours_per_month))

    print(f'Celkovy rocni plat: {year_salary} Kc')
    print(f'Prumerny mesicni plat: {average_per_month} Kc')

# vyplata()


"""
Počet slov
Stáhněte si odevzdanou slohovou práci.
Zadání bylo sepsat text o nejméně 150ti slovech pojednávající o našem hlavním městě.
Napište program, který spočítá počet slov v tomto textu, abychom věděli, zda bylo zadání formálně splněno.
Nechte se vést následujícím návodem.

Nechte váš program otevřít soubor a načíst jednotlivé řádky do seznamu.
Každý řádek převeďte na seznam slov. Slovem se rozumí vše, co je odděleno mezerou nebo novým řádkem.
Vypište na výstup seznam hodnot udávající počty slov na každém řádku.
Vypište na výstup celkový počet všech slov v souboru.
"""
def pocet_slov():
    with open('praha.txt') as f:
        lines = f.readlines()

    seznam_radku_slov = [line.split() for line in lines]
    print(seznam_radku_slov)
    pocet_slov_na_radkach = [len(line) for line in seznam_radku_slov]
    print(pocet_slov_na_radkach)
    celkovy_pocet_slov = sum(pocet_slov_na_radkach)
    print(celkovy_pocet_slov)

# pocet_slov()


"""
Půjčovna
Půjčovna aut má v každém kraji ČR jedno auto s danou SPZ.
Ke konci roku chce zjistit, kolik všechna auta najezdila dohromady kilometrů.
V souboru auta.txt je pro každou SPZ zaznamenáno kolik dané auto ujelo kilometrů za daný rok.
Hodnoty jsou v tisících kilometrů. Bohužel se v jednotlivých krajích blbě zkoordinovali a někdo používal desetinnou čárku, někdo zase tečku.

Napište program, který na výstup vypíše součet všech ujetých kilometrů. Jistě se vám bude hodit metoda řetězců jménem replace().
Upravte váš program tak, aby jméno souboru k otevření dostal na příkazové řádce, abychom mohli takto zpracovávat výkazy z různých souborů, aniž bychom museli upravovat samotný kód programu.
"""

def pujcovna():
    filename = input('Zadej jmeno souboru s daty: ')
    with open(filename) as f:
        lines = f.readlines()

    # neprehledny one-liner pro fajnsmekry
    kilometry = sum([float(line.split()[1].replace(',', '.')) for line in lines])
    print(kilometry)

    # Po jednotlivych krocich (kazdy list comprehension jde samozrejme nahradit za klasicky for cyklus)
    spz_km = [line.split() for line in lines]
    pouze_km = [sk[1] for sk in spz_km]
    nahrazene_carky = [km.replace(',', '.') for km in pouze_km]
    float_hodnoty = [float(km) for km in nahrazene_carky]
    celkem_km = sum(float_hodnoty)
    print(celkem_km)

pujcovna()