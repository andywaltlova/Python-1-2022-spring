# Načtení hodnot z parametrů, podmínky - naše malé CLI (Command-line interface)

**Deadline: 6.3. 23:59**

[Odkaz na návod k odevzdání](https://docs.google.com/presentation/d/1iVXiZC8hUy9Irxxqebdaaz7-uTkuJT16/edit?usp=sharing&ouid=104337294426056946104&rtpof=true&sd=true)


Během tohoto úkolu si vytvoříme naše malé CLI (Command-line interface), které bude brát parametry pomocí modulu `sys`. Během úkolu využijeme hlavně metody a funkce k transformaci textu, seznamy a podmínky.

V obou variantách předpokládejte, že uživatel zadává pouze validní vstupy - nebudeme zatím nijak ošetřovat vyjímky, pro komplexnější řešení bychom stejně neparsovali text z parametrů přímo, ale pravděpodobně bychom použili modul [`argparse`](https://docs.python.org/3/library/argparse.html) nebo [`click`](https://click.palletsprojects.com/en/8.0.x/).

- [Vymyšlené zadání](#zadání)
- [Pokyny pro ty, kteří si chtějí vymyslet vlastní zadání](#chci-si-vymyslet-vlastní-téma-na-cli)

## Zadání

Náš skript se bude jmenovat `order_breakfast.py`. Program bude představovat objednávkový systém, který dostane na vstupu seznam daných parametrů, následně vypočítá cenu jídla. Výstupem programu bude výpis do terminálu, kde bude souhrn objednávky a její výsledná cena (formát výsledné zprávy nechávám na vás).

```py
# Skript půjde zavolat dvěma způsoby

# a) 5 parametrů
python3 order_breakfast.py DRINK FOOD NO_PEOPLE TOGO TIP

# b) 1 parametr
python3 order_breakfast.py 'help'
```

### V případě spuštění skriptu s pěti parametry
#### ☕ DRINK (string)
Druhy a ceny nápojů si definujte podle sebe.

Představuje parametr obsahující nápoj, vždy bude ve formátu `drink_name-[big or small]`, tedy například `cofee-big`, `tea-small`. Pokud bude nápoj velký, jeho cena bude o polovinu větší než u malého. Pro zjištění jaký nápoj si uživatel objednává využijte metodu [`split()`](https://docs.python.org/3/library/stdtypes.html#str.split) a operátor `in`.

#### 🍰 FOOD (string)
Druhy a ceny jídel si definujte podle sebe.

Podobně jako nápoj, ale jídlo nemá danou velikost, parametr tedy bude pouze obsahovat string s názvem jídla, kterou bude mít vámi defnovanou cenu.

#### 🧑‍🤝‍🧑 NO_PEOPLE (integer)
Představuje parametr obsahující číslo indikující kolik snídaní objednávám (předpokládáme, že všechny osoby si dávají stejné jídlo).

Výsledná cena tedy musí reflektovat, pro kolik jídel objednávám.

#### 💰 TIP
Představuje parametr indikující, zda chcete podniku dát spropitné (hodnota bude buď 0 nebo 1, případně vámi zvolené ekvivalenty)

Pokud spropitné chceme dát (hodnota 1), k ceně připočtěte 10%. V opačném případě (hodnota 0) cenu neměňte.

#### 🥡 TOGO
Představuje parametr indikující, zda chcete jídlo s sebou (hodnota bude buď 0 nebo 1, případně vámi zvolené ekvivalenty)

Pokud chceme snídani s sebou (hodnota 1), za každou snídani (zaleží pro kolik osob snídani objednávám) zvyšte cenu o 10 Kč za obalové materiály. V opačném případě (hodnota 0) cenu neměňte.

### V případě spuštění skriptu s jedním parametrem `'help'`

Skript vypíše nápovědu, která bude obsahovat seznam parametrů které je možno použít (meníčko). Po vypsání nápovědy program skončí, můžete využít funkci `exit()`.


### Příklady spuštění skriptu

```
python3 order_breakfast.py coffe-small pancakes 1 0 0
Objednali jste si: .... (může být i celá účtenka, fantazii se meze nekladou)
Výsledná cena je: ....

python3 order_breakfast.py milkshake-big muffin 2 1 1
Objednali jste si: .... (může být i celá účtenka, fantazii se meze nekladou)
Výsledná cena je: ....

python3 order_breakfast.py 'help'
Nápověda obsahující meníčko (možnosti, které mužu v FOOD a DRINK parametru zvolit)
```


## Chci si vymyslet vlastní téma na CLI

Nechcete objednávat snídani ale chcete například nakupovat v obchodě/jít k zubaři/objednávat na eshopu/adoptovat kočičky/ cokoli jiného? Samozřejmě můžete, snažte se pouze v rozumné míře procvičit si parametry příkazové řádky, indexaci, podmínky, použítí základních funkcí (`len()`, `round()`, apod.) a metod řetězců (`string.split()`, další v [dokumentaci](https://docs.python.org/3/library/stdtypes.html#string-methods)).

Váše řešení by vždy mělo jít zavolat s jedním parametrem `'help'` (podobně jako zadání výše), aby opravující věděl, jak může váš program použít.
