# Outline

1. Podmínky
2. Parametry příkazové řádky
3. Sekvenční hodnoty (tuple, range, množina)

# Materials

## Links

- [Podmínky](https://kodim.cz/czechitas/uvod-do-progr/prvni-krucky/podminky)
  - `bool` hodnoty
  - Logické operátory `and` a `or` ([například zde](https://naucse.python.cz/lessons/beginners/and-or/))
- [Parametry příkazové řádky](#parametry-příkazové-řádky) (níže, případně [kapitola z kodim](https://kodim.cz/czechitas/python-data/zaklady-programovani/prvni-programy/#parametry-prikazove-radky))
- [Sekvenční hodnoty (tuple, množina)](#sekvenční-hodnoty-tuple-množina)
  - [Rozbalení hodnot](#unpackingrozbalení-hodnot)
  - [Oficialní dokumenace](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)

## Parametry příkazové řádky

Ukázali jsme si funkci `input()`, která čeká až uživatel nějakou hodnotu zadá. Co kdybychom ale chtěli náš skript rovnou spustit s nějakým daným nastavením? Představme si že vždy chceme aby nám skript zapsal data do nějak pojmenovaného souboru, ale my nechceme čekat než skript data odněkud stáhne a pak se nás teprve zeptá na jméno souboru do kterého data má zapsat, ideálně mu chceme vše říci hned nazačátku aby mohl skript běžet bez našeho dalšího zásahu.

My si můžeme parametry simulovat pomocí modulu [`sys`](https://docs.python.org/3/library/sys.html#sys.argv), konkrétně proměnné z tohoto modulu `sys.argv`.

Proměnná `sys.argv` obsahuje seznam hodnot. Prvním prvkem tohoto listu je jméno samotného skriptu který jsme spustili, každý další parametr je na následujícím indexu. Pokud by tedy muj skript `mine_script.py` obsahoval tento kód:

```py
import sys

print(sys.argv)
```

Následující spuštění skriptu by vypsalo tento výsledek

```
python3 mine_script.py
['mine_script.py']
```

Pokud skriptu při spuštění dám nějaké parametry (oddělené mezerou), objeví se v našem listu také.

```
python3 mine_script.py arg_1 arg_2
['mine_script.py', 'arg_1', 'arg_2']
```

K těmto parametrům můžete přistupovat pomocí indexu proměnné `sys.argv`, tedy pro první parameter `sys.argv[1]` (na prvním místě (nultém indexu) je název skriptu). Podobně jako u funkce `input()`, argumenty jsou vždy řetězce.

### Něco navíc

S tímto principem se můžete setkat i u CLI (Command line interface), tedy aplikací, které jsou ovládané z příkazové řádky. Nejjednoduším příkladem CLI jsou terminály operačních systémů. Ať už se jedná o `PowerShell` ve Windows, nebo například `bash` v Linuxu, či `zsh` v MacOS (což je vpodstatě rozšířený `bash`).

Moc pěkně je CLI vysvětlené v [tomto](https://youtu.be/mUXVBMhr7Xg) videu (anglicky), přímo s ukázkami na Windows.

Pokud by vás CLI zaujali více, doporučuji podívat se na více komplexní python modul `argparse`, kerý je uzpůsobený k vytvoření vašeho vlastního CLI.

## Sekvenční hodnoty (tuple, množina)

Množiny - https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
Tuples - https://docs.python.org/3/library/stdtypes.html#tuple

(a nebo samozřejmě googlete)

### Unpacking/Rozbalení hodnot

K rozbalení hodnot ze sekvence do jednotlivých proměnných můžeme jednoduše použít přiřazení. Občas je lepší použít unpacking než postupně pomocí indexů ukládat hodnoty do proměnných.

```py
numbers = [1, 2, 3]
one, two, three = numbers
```

Podobný princip se dá využít pro předání více argumentů funkci. Hodnoty ze sekvence můžeme rozbalit pomocí operátoru `*`. Pozdějí v kurzu si ukážeme, že se dá použít i operátor `**` pro rozbalení hodnot ve slovníku (páry klíčů a hodnot, proto dvě hvězdičky).

```py
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']

print(*numbers, *letters)
```

# Knowledge check

- Ovládám syntaxi podmínek: `if`, `else`, `elif`
- Umím spojovát více logických výrazů pomocí operátorů `and` a `or`
- Ovládám operátory `in` a `not` (případne kombinaci `not in`)
- Umím načíst parametry z příkazové řádky při spuštění skriptu
- Ovládám základní množinové operace (vím kde a jak hledat více informací)
- Umím sekvenci hodnot rozbalit do samostatných proměnných
- Umím sekvenci hodnot předat funkci jako jednotlivé parametry

# Meme for this week

![Python bites](https://pics.me.me/does-your-python-bite-no-but-it-can-hurt-you-63085382.png)
