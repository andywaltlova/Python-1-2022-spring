# opakovani nacteni, loc, iloc, selekce, export do souboru
# isin, prevod na seznam seznamu


import wget
import pandas as pd

# wget.download('https://kodim.cz/czechitas/python-data/datova-analyza/pandas-agregace/assets/u202.csv')
# wget.download('https://kodim.cz/czechitas/python-data/datova-analyza/pandas-agregace/assets/u203.csv')
# wget.download('https://kodim.cz/czechitas/python-data/datova-analyza/pandas-agregace/assets/u302.csv')

# Práce s chybějícími hodnotami

u202 = pd.read_csv('data/u202.csv')
# print(u202)
empty_mark = u202['známka'].isnull()

u202_clean = u202.fillna(u202['známka'].mean())
# print(u202_clean)


# Spojovani - concat, merge

u202 = pd.read_csv('data/u202.csv', encoding='utf-8').dropna()
u203 = pd.read_csv('data/u203.csv', encoding='utf-8').dropna()
u302 = pd.read_csv('data/u302.csv', encoding='utf-8').dropna()
u202['místnost'] = 'u202'
u203['místnost'] = 'u203'
u302['místnost'] = 'u302'



maturita = pd.concat([u202, u203, u302], ignore_index=True)


# merge
preds = pd.read_csv('data/predsedajici.csv', encoding='utf-8')

test = pd.merge(u202, preds, on=['den'])
test = test.rename(columns={'jméno_x': 'jméno', 'jméno_y': 'předs'})
# print(test)
# Group by

maturita2 = pd.merge(maturita, preds, on=['den'])
maturita2 = maturita2.rename(columns={'jméno_x': 'jméno', 'jméno_y': 'předs'})

print(type(maturita2.groupby('místnost')['známka'].mean()))

print(maturita2[maturita2['známka'] == maturita['známka'].min()]['jméno'])
