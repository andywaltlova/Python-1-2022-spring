import pandas as pd

"""
2 Česká jména podruhé
Budeme pokračovat s daty o českých jménech z předchozího cvičení.
Minule jsme používali sloupeček se jmény jako index.
Tentokrát načtěte soubor se jmény tak, aby Pandas vyrobil index číselný.

Proveďte následující dotazy

Vypište všechny řádky se jmény, jejichž nositelé mají průměrný věk vyšší než 60.
Vypište pouze jména z těch řádků, kde četnost je mezi 80 000 a 100 000.
Vypište jména a četnost pro jména se slovanským nebo hebrejským původem.
    Kolik takových jmen je?
Vypište všechna jména, která mají svátek prvních 7 dní v únoru.
"""

# Nacteni - ciselny index
jmena = pd.read_csv('jmena100.csv')

# Nechtela se mi psat diakritika, tak jsem to prejmenovala
jmena = jmena.rename(columns={
    'jméno':'jmeno',
    'četnost':'cetnost',
    'věk':'vek',
    'pohlaví':'pohlavi',
    'svátek':'svatek',
    'původ':'puvod',
})

# Vypište všechny řádky se jmény, jejichž nositelé mají průměrný věk vyšší než 60.
greater_than_60 = jmena['vek'] > 60
print(jmena[greater_than_60])

# Vypište pouze jména z těch řádků, kde četnost je mezi 80 000 a 100 000.
condition = (jmena['cetnost'] > 80_000) & (jmena['cetnost'] < 100_000)
print(jmena[condition])

# Vypište jména a četnost pro jména se slovanským nebo hebrejským původem.
#     Kolik takových jmen je? - count(), nebo shape na vyslednem df

# condition = jmena['puvod'].isin(['hebrejský','slovanský'])
condition = (jmena['puvod']=='hebrejský') | (jmena['puvod']=='slovanský')
print(jmena[condition][['jmeno','cetnost']])


# Vypište všechna jména, která mají svátek prvních 7 dní v únoru.
condition = jmena['svatek'].isin(['1.2','2.2','3.2', '4.2', '5.2', '6.2', '7.2'])
print(jmena[condition])
