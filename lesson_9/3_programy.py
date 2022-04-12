import sys

# 9 Minuty
# Vytvořte program casy.py, který bude zpracovávat seznam naměřených časů v minutách.
# Nejprve přímo do programu zadrátujte konkrétní hodnoty například takto:

casy = [12, 25, 64, 27, 15, 66, 128, 44]
# Vyfiltrujte z tohoto seznamu pouze ty časy, které se vejdou do jedné hodiny.
under_hour = [cas for cas in casy if cas < 60]
# Vyfiltrujte z tohoto seznamu pouze ty časy, které překračují jednu hodinu a to tak, že výsledkem bude seznam minut, udávajících o kolik jsme jednu hodinu překročili.
over_hour = [cas - 60 for cas in casy if cas > 60]

# Upravte program tak, aby seznam naměřených hodnot obdržel na příkazové řádce.
# jediny rozdil je ze casy musime predela na cisla

# casy = [int(num) for num in sys.argv[1:]]
# under_hour = [cas for cas in casy if cas < 60]
# over_hour = [cas - 60 for cas in casy if cas > 60]
# print(casy, under_hour, over_hour)


# 10 Fahrnheit vs. Celsius
# Pokud pečete podle anglických receptů, často se po váš požaduje rozehřát troubu na uvedenou teplotu.
# Pokud si ovšem neuvědomíte, že Američané používají pro měření teploty stupně Fahrenheita namísto Celsia,
# bude vás na konci pečení čekat nemilé překvapení.

# Nastudujte si na České Wikipedii jak se převádějí stupně Fahrenheita na stupně Celsia a napište program,
# který takový převod provede. Váš program dostane na příkazové řádce teplotu ve stupních Fahrenheita
# a vypíše její ekvivalent ve stupních Celsia.

# fahrenheit = int(sys.argv[1])
#  sem teda vygooglila
# celsius = (fahrenheit - 32) * 5.0/9.0


# 11 Úprava řetězce
# Napište program, který dostane jako jeden parametr řetězec s mezerami
# (aby to fungovalo, musí být ten řetězec obalen v uvozovkách).
# Vypište tento řetězec tak, že mezery nahradíte za podtržítka.

# $ python uprava_retezce.py "retezec s mezerami"
# retezec_s_mezerami

# retezec_s_mezerami = sys.argv[1]
# print(retezec_s_mezerami.replace(' ', '_'))


# 12 Házení kostkou
import random
# Napište program, který při každém spuštění hodí šestistěnnou kostkou ‒ tedy vypíše náhodné číslo mezi 1 až 6.
# print(random.randint(1, 6))
# Upravte program tak, aby jako parametr dostal počet stěn kostky. Bude tedy umět házet třeba sedmistěnnou nebo devítistěnnou kostkou podle toho, jaké číslo dostane na vstupu.
# steny = int(sys.argv[1])
# print(random.randint(1, steny))

# Předejte programu další parametr, který bude udávat kolik hodů má program provést. Program pak na výstup vytiskne seznam tolika hodů, kolik jste zadali na vstupu.
# Cílem je tedy vymyslet, jak vyrobit seznam náhodných čísel. Jistě se nám k tomu bude hodit chroustání seznamů.
# pocet_hodu = int(sys.argv[2])
# print([random.randint(1, steny) for i in range(pocet_hodu)])



# 13 Karty 1
# Napište program, který vylosuje náhodnou hrací kartu z klasické whistové sady obsahující 52 karet,
# rozdělených do čtyř barev (kříže, srdce, piky, káry), s hodnotami 2, 3, 4, 5, 6, 7, 8, 9, 10,
# J (kluk), Q (dáma), K (král), A (eso).

# Výstup programu může vypadat například takto:
# Karta: kluk kříže

barvy = ['kříže', 'srdce', 'piky', 'káry']
hodnoty = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'kluk', 'dáma', 'král', 'eso']

barva = barvy[random.randint(0, len(barvy)-1)]
hodnota = hodnoty[random.randint(0, len(hodnoty)-1)]

print(f'Karta: {hodnota} {barva}')

# 14 Jak proměnit hada na velblouda
# Napište program, který dostane na příkazovém řádku název proměnné v hadí notaci a vrátí tentýž název zapsaný ve velbloudí notaci.

# Příklad:
# $ python3 had-velbloud.py had_honi_velblouda
# hadHoniVelblouda

# vstup = sys.argv[1]

# slova = vstup.split('_')
# vystup = [slovo.capitalize() for slovo in slova]
# vystup = "".join(vystup)
# vystup = vystup[0].lower() + vystup[1:]
# print(vystup)


# 15 Jak proměnit velblouda na hada
# Napište program, který dostane na příkazovém řádku název proměnné ve velbloudí notaci a vrátí tentýž název zapsaný v hadí notaci.

# Příklad:
# $ python3 velbloud-had.py velbloudHoniHada
# velbloud_honi_hada

# Ano, tohle už není procházka růžovým sadem a jde o úložku spíše pro fajnšmekry,
# Python gurmány a lidi s neutišitelnou touhou nenechat žádný příklad nevyřešený.
# Vězte, že skutečně existuje řešení, které používá výhradně probrané techniky.
# Vyplatí se mrknout na to, jaké všechny metody nabízí Python řetězce, jinak ale není potřeba žádné googlení,
# jen se nesmíte bát věci, které už tak dobře znáte, opravdu použít, a nemít je ve své programátorské
# dílně jen vystavené za sklem.

# Některé pasáže programu si lze mírně ulehčit použitím funkce enumerate(),
# která vám při chroustání seznamů vrací nejen prvek seznamu, ale i jeho index.
# Vyzkoušejte například následující příkaz

# [[i, jmeno] for i, jmeno in enumerate(['petr', 'jana', 'vlasta', 'onyx'])]
# Úlohu lze však vyřešit i bez enumerate()!

vstup = sys.argv[1]

#  Tohle je prvni reseni co napadlo me, nejsem si jista jestli se ukazuji inline podminky v teto kapitole
snake_case = ''.join(['_' + c.lower() if c.isupper() else c for c in vstup]).lstrip('_')
print(snake_case)

# Reseni s enumerate a indexy mi prijde zbytecne slozite, ja jsem vymyslela nize napsane, taky ale neni uplne elegantni

indexes = [i for i in range(len(vstup)) if vstup[i].isupper()]

# pridam prvni a posledni index + 1
indexes = [0] + indexes + [len(vstup)]
with_underscores = [vstup[indexes[i-1]:indexes[i]].lower() + '_' for i in range(len(indexes))]
print(with_underscores)
snake_case = ''.join(with_underscores).strip('_')
print(snake_case)