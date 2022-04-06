# Outline

1. [JSON](https://kodim.cz/czechitas/python-data/zaklady-programovani/slovniky-json/#format-json)
2. [CSV](#csv)

# CSV

1. [Jak soubory číst](#jak-soubory-číst)
2. [Jak soubory zapisovat](#jak-soubory-zapisovat)
3. [Exercises](#exercises)

Formát CSV (Comma Separated Values) je jedním z nejjednodušších a nejběžnějších způsobů ukládání tabulkových dat. Chcete-li představovat soubor CSV, musí být uložen s příponou .csv . Jako oddělovač můžeme mít libovolný znak, nejenom čárku.

I když bychom mohli použít  `open()` funkci pro práci se soubory, kterou jsme si ukazovlali minulou lekco, pro CSV v Pythonu existuje speciální `csv` modul, díky kterému je práce se soubory CSV mnohem jednodušší.

Než budeme moci použít metody k csv modulu, musíme nejprve importovat modul pomocí `import csv`

V této sekci budeme pracovat se soubory ze složky [star wars](star_wars/). Data jsou z [datasetu na portálu kaggle](https://www.kaggle.com/datasets/jsphyg/star-wars?resource=download).

## Jak soubory číst

Podobně jako v minulé lekci budeme používat blik s `with` a funkci `open()`. Tentokrát si díky modulu csv, můžeme vytvořit tzv. reader, kterému můžeme specifikovat parametry našeho csv souboru (například použitý oddělovač), dále ho budeme číst stejně jako textové soubory minulou lekci. Níže je nejjednoduší ukázka čtení jednoho ze souborů ze star wars složky.

Csv soubory standartně používají funkci `open()` se specifikovaným parametrem `newline=''`, to proto aby se správně interpretovali znaky pro nový řádek v případném textu v csv souboru ([oficiální poznámka v dokumentaci](https://docs.python.org/3/library/csv.html#id3)).

Pro čtení můžeme využít for cyklus a procházet tzv iterátor, který nám vytvořil objekt reader. Momentálně nepotřebujeme o iterátorech vědět více, kdo je zvědavý určitě vygooglí (například [zde](https://wiki.python.org/moin/Iterator)).

Sekce o čtení csv [v oficiální dokumentaci](https://docs.python.org/3/library/csv.html#reader-objects).

```python
import csv
with open('planets.csv', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        print(row)

    # Případně všechny řádký najednou
    # rows = list(reader)
```

Výsledkem kódu výše je pak výpis seznamu seznamů, které představují jednotlivé řádky.

Pokud chceme mít výsledná data uložené ve slovníku, můžeme ke čtení využít speciální `DictReader`, který modul csv také podporuje. Tento objekt pro čtení nám dovoluje pomocí parametru `fieldnames` nastavit názvy sloupců, které zapisujeme. Pokud parametr vynecháme, vezme se automaticky z prvního řádku který přečteme.

```python
import csv
with open('vehicles.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)

    # Případně všechny řádký najednou
    # rows = list(reader)
```

## Jak soubory zapisovat

Zapisování je opět velice podobné jako zapisování textových souborů, tentokrát si vytvoříme objekt pro zápis, csv writer, který bude mít nastavené parametry pro výstupní csv soubor.

Pro zápis můžeme použít metody `writer.writerow()` nebo `writer.writerows()`, minule jsme používali `write()` a `writelines()`.

Sekce o zápisu [v oficiální dokumentaci](https://docs.python.org/3/library/csv.html#writer-objects).

```python
import csv
with open('some.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(someiterable)
```

Pokud máme data v našem skriptu uložená ve slovníku, můžeme k zápisu využít speciální `DictWriter`, který modul csv také podporuje. Tento objekt pro zápis nám dovoluje pomocí parametru `fieldnames` nastavit názvy sloupců, funguje to analogicky jako pro čtení pomocí `DictReader`.

```python
import csv

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
```

## Exercises

### 1. Čtení

Stáhnětě si soubor [starships.csv](star_wars/starships.csv)

1. Načtěte data pomocí modulu csv - nechám na vás jestli do slovníku nebo do seznamů.
2. Vypiště si data na výstup
3. Vypiště pouze jména a výrobce lodí, které mají kapacitu pro pasažéry alespoň 2.
   Pokud hodnota není číslo, použijte k ošetření buď podmínky nebo vyjímky.
   - Kolik takových lodí je?
4. Najděte loď, která má celkovou nejvyší kapacitu, tedy vejde se do ní nejvíc posádky a pasažérů (crew a passengers).
   Pokud některá z hodnot není číslo, použijte k ošetření buď podmínky nebo vyjímky.

### 2. Zápis

Stáhnětě si soubor [vehicles.csv](star_wars/vehicles.csv)

1. Načtěte data pomocí modulu csv - nechám na vás jestli do slovníku nebo do seznamů.
2. Vypiště si data na výstup
3. Zapište do jednoho csv souboru pouze lodě, které mají `vehicle_class` starfighter nebo gunship.
   - nezapomeňtě na header, tedy první řádek s názvy sloupců. Mohli by se vám hodit metody values a keys u slovníků.
4. Zapište do druhého csv souboru pouze subset parametrů, tedy vyberte si pouze sloupce které vás zajímají a ty zapiště do souboru.
   - opět nezapomeňte na header

### 3. (Bonus) Čtení pomocí csv, zápis pomocí json

Stáhnětě si soubor [characters.csv](star_wars/characters.csv)

1. Načtěte si data pomocí `DictReader` z modulu `csv`.
2. Zapiště data pomocí některé z funkcí z modulu `json` do json souboru.
   - Zapište do zvlášť json souboru pouze všechny ženy
   - Zapište do zvlášť json souboru pouze všechny muže

# Knowledge check

- vím jak vypadá json formát
- vím, že existují ruzné API (Application Programming Interface)
- Umím otevřít a přečíst řádky z json souboru
- Umím otevřít a zapsat řádky do json souboru

# Meme for this week

![JSON API drug](https://memegenerator.net/img/instances/68258022.jpg)
