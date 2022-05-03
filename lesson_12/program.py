import pandas as pd
# Opacko z minule + cviceni z minule 30min - https://kodim.cz/czechitas/python-data/datova-analyza/pandas-agregace/#cviceni



# 12. lekce Pandas transformace - https://kodim.cz/czechitas/python-data/datova-analyza/pandas-transformace/

# def nazev_funkce(povinny_argument, nepovinny_argument=2):
#     def vnorena_funkce():
#         pass # TODO
#     # Funkcionalita
#     # jakykoli dalsi kod
#     return povinny_argument



vaha = pd.read_csv('data/vaha.txt', encoding='utf-8', sep='\t')
# print(vaha)

# .str a uprava dat
cisloDne = vaha['den'].str[3:].str.replace('.', '')
# print(cisloDne)

cislo_den_num = pd.to_numeric(cisloDne)
# print(cislo_den_num)

vaha['cislo den'] = cislo_den_num
vaha['den'] = vaha['den'].str[:3]
# print(vaha)


# apply a vyuziti vlastnich funkci na seriich

def kilogramy(vstup):
  casti = vstup.split(' ')
  if len(casti) < 2:
    casti = vstup.split('k')

  return float(casti[0].replace(',', '.'))

vaha['váha'] = vaha['váha'].apply(kilogramy)
print(vaha)

# agg a vlastni agregacni funkce

# Vlastni funkce + cviceni 20min - https://kodim.cz/czechitas/python-data/datova-analyza/pandas-transformace/#cviceni

# Uvidime jak budeme stihat - https://kodim.cz/czechitas/python-data/bonusove-kapitoly/vizualizace
