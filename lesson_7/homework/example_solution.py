"""
Univerzita pro celoživotní vzdělávání se rozhodla změnit svůj známkovací systém
z číselných známek 1 až 5 na hodnocení písmeny A až F.
Bohužel změna se odehrála jaksi uprostřed semestru, takže je potřeba změnit
aktuální výkazy o známkách z čísel na písmena. Nechte se vést následujícím postupem.
 
Otevřete si dokument s jedním výkazem známek.
Zkopírujte si tuto tabulku do textového souboru.
Napište program, který tuto tabulku načte ze souboru a změní všechny známky tak, že 1 bude A, 2 bude B, 3 bude C, 4 bude D a 5 bude F.
Vypište váš výsledek do nějakého souboru tak, aby se z něj dal zase zkopírovat do tabulky Google.
Vytvořte novou Google tabulku, která vypadá stejně jako ta výše avšak s převedenými známkami.
"""
 
with open('znamky.txt', mode='r', encoding='utf-8') as f:
    lines = f.readlines()
 
modified_lines = [lines[0]]
for line in lines[1:]:
    new_line = line.replace('1', 'A') \
                   .replace('2', 'B') \
                   .replace('3', 'C') \
                   .replace('4', 'D') \
                   .replace('5', 'F')
    modified_lines.append(new_line)
 
with open('znamky_updated_1.txt', mode='w', encoding='utf-8') as f:
    f.writelines(modified_lines)
 
# Pote jsem ctrl+c zkopirovala tabulku v souboru a shift+ctr+v do google sheetu
# https://docs.google.com/spreadsheets/d/1GLJnoy7Zm_GZZQct9TyLvXuPB7LnXZSzKK5I0Q9lY_4/edit?usp=sharing
 
 
# Pomoci modulu csv, princip porad stejny jen sem zvolila trochu jiny zpusob predelani znamek, ktery se mi spise hodil k tomu jak jsem data nacetla
import csv
 
with open('znamky.txt', mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter='\t')
    # nebo reader nize pokud nacitate primo z csv souboru
    # reader = csv.DictReader(f, delimiter=',')
    lines = list(reader)
 
znamky_map = {
    '1' : 'A',
    '2' : 'B',
    '3' : 'C',
    '4' : 'D',
    '5' : 'F',
}
for key in ['Test 1', 'Test 2', 'Test 3', 'Test 4', 'Test 5', 'Test 6']:
    for line in lines:
        line[key] = znamky_map[line[key]]
 
with open('znamky_updated_2.txt', mode='w', encoding='utf-8') as f:
    f.writelines(modified_lines)