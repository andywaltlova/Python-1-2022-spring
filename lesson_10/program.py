import pandas as pd

# Documentation: https://pandas.pydata.org/docs/

# read_csv, read_json, index
mesta = pd.read_csv('data/mesta.csv', index_col='mesto')

# json_data = pd.read_json('data/star_wars.json')
# print(json_data)

# info(), describe(), columns, shape
# print(mesta.columns)

# loc, iloc
# Muze byt jeden sloupec/radek, seznam, nebo rozsah pomoci :
# Priklady jsou stejne pro loc i iloc, jen pozor na to ktere rozsahy jsou vcetne (loc) a ktere vyjma (iloc)
mesta.iloc[1]
mesta.iloc[[1, 3, 5]]
mesta.iloc[1:3]

mesta.loc['brno']
mesta.loc[['olomouc', 'plzen']]
mesta.loc['olomouc':'plzen']

# Muzete klidne pouzit promenne
sloupce = [1,2]
radky = [0,2]
mesta.iloc[sloupce, radky]


# to_csv, to_json

selekce = mesta.loc[['olomouc', 'plzen'], ['obyvatel','linky']]
# print(selekce)
selekce.to_csv('selekce.csv')
# selekce.to_excel('selekce.xlsx')

#####
mesta_2 = pd.read_csv('data/mesta.csv')
# print(mesta_2)

# head, tail
# print(mesta_2.tail(-2))
# print(mesta_2.head(-2))

# max, min
# print(mesta_2.min())

# selekce jako v sql, sloupce, radky

# filtered_dataframe = mesta[['kraj','obyvatel']]
# print(filtered_dataframe)

condition = mesta_2['vymera'] < 200
# print(mesta_2[condition])

# logicke operatory
# and ... &
# or ... |
vymera_pod_200 = mesta_2['vymera'] < 200
b = mesta_2['obyvatel'] < 500_000
condition = vymera_pod_200 | b
print(mesta_2[condition]['kraj'])


# TODO next lesson
# isin()
# prevod dataframu na list, reset_index