import pandas as pd

"""
3 Původ jmen
Napište program, který:

Načte naše data o českých jménech.

Vytvoří z něj DataFrame, který obsahuje jména a četnosti jmen, která nejsou
ani hebrejského, ani aramejského ani slovanského původu.

Převede tento DataFrame na obyčejné Python seznamy.
Pomocí chroustání seznamů spočítá součet všech četností těchto jmen.

Na výstup vypíše, jaké procentuální zastoupení mají tato jména v celé ČR.
Podle odhadů OSN má k osmému květnu 2019 Česká Republika 10 629 798 obyvatel.
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

# Vytvoří z něj DataFrame, který obsahuje jména a četnosti jmen, která nejsou
# ani hebrejského, ani aramejského ani slovanského původu.
condition = (jmena['puvod']!='hebrejský') & (jmena['puvod']!='slovanský') & (jmena['puvod']!='aramejský')
jmena = jmena[condition]

# Převede tento DataFrame na obyčejné Python seznamy.
jmena_seznamy = jmena.values.tolist()
# print(jmena_seznamy)

# Pripadne na dictionary (slovnik)
jmena_dict = jmena.to_dict('records')
# print(jmena_dict)

# Pomocí chroustání seznamů spočítá součet všech četností těchto jmen.

sum_cetnost = sum([line[1] for line in jmena_seznamy])
sum_cetnost = sum([line['cetnost'] for line in jmena_dict])
# print(cetnost)

# Na výstup vypíše, jaké procentuální zastoupení mají tato jména v celé ČR.
# Podle odhadů OSN má k osmému květnu 2019 Česká Republika 10 629 798 obyvatel.

obyvatele = 10_629_798  # 100%
sum_cetnost             #   x%

jedno_procento = obyvatele / 100
zastoupeni = round(sum_cetnost/jedno_procento, 2)
print(f'Jmena maji zastoupeni {zastoupeni} %')




