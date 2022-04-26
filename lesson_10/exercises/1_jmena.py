import pandas as pd

"""
1 Česká jména
Stáhněte si soubor jmena100.csv, který obsahuje tabulku 100 nejpoužívanějších
českých křestních jmen seřazených od nejpoužívanějšího k nejméně používanému.
Otevřete Python konzoli a pomocí Pandas načtěte tuto tabulku jako DataFrame.
Jako index zvolte sloupec s názvem 'jméno'.

Datový soubor obsahuje následující sloupečky

jméno - křestní jméno
četnost - počet obyvatel ČR mající toto jméno
věk - průměrný věk nositelů jména
pohlaví - zda je jméno mužské či ženské
svátek - datum, kdy má dané jméno svátek
původ - původ jména

Vyřešte následující úkoly.

Vypište na konzoli informace o jménu Martin.
Vypište na konzoli informace pro jména Martin, Zuzana a Josef.
Vypište na konzoli informace o všech nejčastějších jménech až po Martina.
Vypište pouze průměrné věky osob mající jména mezi Martinem a Terezou.
Vypište průměrný věk a původ pro všechna jména od Libora dolů.
Vypište sloupečky mezi věkem a původem pro všechna jména v tabulce.
"""

# Nacteni
jmena = pd.read_csv('jmena100.csv', index_col='jméno')

# Nechtela se mi psat diakritika, tak jsem to prejmenovala
jmena = jmena.rename(columns={
    'jméno':'jmeno',
    'četnost':'cetnost',
    'věk':'vek',
    'pohlaví':'pohlavi',
    'svátek':'svatek',
    'původ':'puvod',
})

# Vypište na konzoli informace o jménu Martin.
print(jmena.loc[['Martin']])

# Vypište na konzoli informace pro jména Martin, Zuzana a Josef.
print(jmena.loc[['Martin','Zuzana','Josef']])

# Vypište na konzoli informace o všech nejčastějších jménech až po Martina.
print(jmena.loc[:'Martin'])

# Tady je dobre se jen zamyslet nad tim, ze nase data uz jsou serazena
# v nekterych pripadech by bylo fajn nejdriv si hodnoty seradit
jmena = jmena.sort_index()
jmena = jmena.sort_values(by='cetnost', ascending=False)

# Vypište pouze průměrné věky osob mající jména mezi Martinem a Terezou.
print(jmena.loc['Martin':'Tereza', 'vek'])

# Vypište průměrný věk a původ pro všechna jména od Libora dolů.
print(jmena.loc['Libor':, ['vek','puvod']])

# Vypište sloupečky mezi věkem a původem pro všechna jména v tabulce.
print(jmena.loc[:,'vek':'puvod'])

# pozor na rozdil mezi loc a iloc
print(jmena.iloc[:, 2:-1])