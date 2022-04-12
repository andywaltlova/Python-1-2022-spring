# 9 Ověřování věku
# Následující seznam obsahuje věky uživatelů naší malé sociální sítě.

veky = [35, 12, 44, 11, 18, 21, 28, 18]
# Vytvořte pomocí chroustání seznamů seznam celých čísel, které udávají, kolik jednotlivým uživatelům zbývá do 18ti let.
# Záporná čísla budou znamenat, že uživatel už věk překročil.
print([18 - vek for vek in veky])
# Vytvořte pomocí chroustání seznamů seznam pravdivostních hodnot, které udávají, který uživatel je starší 18ti let.
print([vek > 18 for vek in veky])
# Vytvořte pomocí chroustání seznamů seznam pravdivostních hodnot, které udávají, který uživatel má přesně 18 let.
print([vek == 18 for vek in veky])


# 10 Promítání
# V letním kině Šmajchl mají program na každý den uložený jako dva seznamy.
# První seznam obsahuje názvy filmů a druhý jejich délky v minutách, např. takto:
# nazvy = [
#   'Někdo to rád horké, extended edition',
#   'Adéla ještě nevečeřela',
#   'Kulový blesk'
# ]

delky = [136, 105, 82]

# Použijte chroustání seznamů a vyrobte seznam trvání, který bude obsahovat délky filmů nikoliv jako čísla v minutách,
# ale jako řetězce v hodinách a v minutách. Výsledek tedy bude vypadat takto

trvani = ['2:16', '1:45', '1:22']
trvani = [f'{delka//60}:{delka%60}' for delka in delky]
print(trvani)

# 11 Počty obyvatel
# Mějme počty obyvatel v jednotlivých krajích ČR podle následující tabulky.

# Tuto tabulku máme reprezentovanou jako seznam:

kraje = [
  ['Hlavní město Praha', '1 280 508'],
  ['Jihočeský kraj', '638 782'],
  ['Jihomoravský kraj', '1 178 812'],
  ['Karlovarský kraj', '296 749'],
  ['Kraj Vysočina', '508 952'],
  ['Královéhradecký kraj', '550 804'],
  ['Liberecký kraj', '440 636'],
  ['Moravskoslezský kraj', '1 209 879'],
  ['Olomoucký kraj', '633 925'],
  ['Pardubický kraj', '517 087'],
  ['Plzeňský kraj', '578 629'],
  ['Středočeský kraj', '1 338 982'],
  ['Ústecký kraj', '821 377'],
  ['Zlínský kraj', '583 698']
]
# Vytvořte seznam, který obsahuje pouze názvy všech krajů, tedy první sloupeček této tabulky.
prvni_sloupec = [kraj[0] for kraj in kraje]
print(prvni_sloupec)
# Vytvořte seznam, který obsahuje počty obyvatel jako čísla. Pro zbavení se mezer v číslech se vám jistě bude hodit metoda řetězců jménem replace().
druhy_sloupec = [int(kraj[1].replace(' ','')) for kraj in kraje]
print(druhy_sloupec)
# Do vhodně pojmenované proměnné uložte seznam, který reprezentuje výše uvedenou tabulku jako dva seznamy: seznam jmen a seznam počtů obyvatel jako čísla.
sloupce = [prvni_sloupec, druhy_sloupec]
print(sloupce)

# 12 Volby
# Máme pět kandidátů na post prezidenta ČR. Následující tabulka obsahuje hlasy, které jednotliví kandidáti získali v prvním kole prezidentských voleb.
# Data máme k dispozici v následujícím formátu

hlasy = [
  [78774, 43179, 225111, 144799, 242854],
  [91062, 22451, 17475, 53391, 46450],
  [179186, 216499, 4493, 156305, 61222],
  [9619, 53476, 926, 64737, 34566],
  [66904, 85730, 27271, 12964, 38041],
  [118755, 1929, 30426, 25178, 31952],
  [64467, 40993, 81181, 39392, 4335],
  [11221, 97970, 26179, 98539, 112578],
  [171064, 7638, 8752, 96666, 39738],
  [74235, 101680, 18920, 45904, 1922],
  [39309, 1505, 10531, 30458, 40228],
  [131584, 1812, 241122, 22267, 99326],
  [194133, 39985, 200997, 28229, 20780],
  [66188, 51607, 15977, 177272, 17664]
]

# Zodpovězte následující otázky
# Kolik získal každý kandidát hlasů v celé ČR?

pocet_kandidatu = len(hlasy[0])

index_kandidata = 1 # muzeme zameni za 0 .. 4 , muzeme folat i ve for comprehension
kandidat_hlasy = sum([kraj[index_kandidata] for kraj in hlasy])

kandidati_hlasy = [sum([kraj[i] for kraj in hlasy]) for i in range(pocet_kandidatu)]

# Který kandidát vyhrál první kolo voleb?
print(kandidati_hlasy) # bud se podivame a vidime a nebo si musime udelat jeste seznam kandidatu

max_hodnota = max(kandidati_hlasy)
index_max = kandidati_hlasy.index(max_hodnota)
kandidati = ['Igor Rezek', 'Augustýn Doležal', 'Vladan Bednář', 'Ondřej Brotz', 'Radim Kašpar']
print(kandidati[index_max])

# Ve kterých krajích byla nejvyšší a nejnižší volební účast
# Tady moc nevim jak je to mysleno, protoze nemame udaje kolik je volicu v jednotlivych krajich, ale predpokladam ze se ma udelat jen suma radku

ucast = [sum(kraj) for kraj in hlasy]
print(ucast)
max_hodnota = max(ucast)
index_max = ucast.index(max_hodnota) # ope bychom idealne cheli seznam kraju abychom si o rovnou vypsali
print(index_max)

# Vytvořte tabulku, která ukazuje který kandidát vyhrál v kterém kraji.
# No tady je vic pristupu, hodne zalezi jak chceme aby vypadal vysledek

# Muzeme si treba vypsat indexy pro kandidaty
print([kraj.index(max(kraj)) for kraj in hlasy])
#  Nebo pouzit nas seznam kandidatu
print([kandidati[kraj.index(max(kraj))] for kraj in hlasy])


# Vytvořte tabulku podobnou té z tohoto cvičení, která místo čísel bude obsahovat jaké procento celkového počtu hlasů získal každý kandidát v daném kraji.
procenta_hlasy = [f'{round(kandidat/(sum(hlasy[0]) / 100), 2)} %' for kandidat in hlasy[0]]
procenta_hlasy = [f'{round(kandidat/(sum(hlasy[1]) / 100), 2)} %' for kandidat in hlasy[1]]
procenta_hlasy = [f'{round(kandidat/(sum(hlasy[2]) / 100), 2)} %' for kandidat in hlasy[2]]
procenta_hlasy = [f'{round(kandidat/(sum(hlasy[3]) / 100), 2)} %' for kandidat in hlasy[3]]
#  atd.
print(procenta_hlasy)

# Nápověda: postupuje tak, že použijete na každý řádek tabulky zvlášť chroustání seznamů. Tabulku můžete sestavit tak, že tento postup ručně zopakujete 13 krát, jednou pro každý kraj. Pokud toužíte po elegantnějším řešení, vyčkejte na nepovinné úložky.

# Vytvořte seznam pravdivostních hodnot, který bude říkat, ve kterých krajích překročila volební účast 50 %. Pro jednoduchost uvažujte, že data o počtech obyvatel z předchozího cvičení jsou počty oprávněných voličů.
# ja mam v promenne sloupce ulozenou tabulku jako sloupec kraju a sloupec obyvatel
# print(sloupce)

obyvatele = sloupce[1]
ucast_nad_50 = [sum(hlasy[i])/(obyvatele[i]/100) > 50 for i in range(len(hlasy))]
print(ucast_nad_50)

# 13 Elegantní volby
# Pokud vás trápí, že řešení varianty 5 v úloze o volbách není příliš elegantní,
# zkuste sestavit Python výraz na jeden řádek, který celý bod 5 vyřeší najednou.
# Bude potřeba do sebe zanořit dvě chroustání seznamů, jedno přes hodnoty v řádcích
# a druhé přes jednotlivé kraje.

procenta_hlasy = [[f'{round(kandidat/(sum(kraj) / 100),2)} %' for kandidat in kraj] for kraj in hlasy]