# Outline

1. Standartně dostupné funkce (`len()`, `round()`)
2. Dokumentace
3. Import modulu ze standartní knihovny
4. Použití funkcí z modulů
5. Metoda vs funkce
6. Vytvoření prvního skriptu
7. Funkce `print()` a `input()`
8. Spojení hodnot různých datových typů
9. [Sekvenční hodnoty - řetězec, list]
10. [Metoda `append()`]
11. [Parametry příkazové řádky]

# Materials

## Links

- [Funkce a moduly](https://kodim.cz/czechitas/uvod-do-progr/prvni-krucky/funkce-moduly)
- [Vstup a vystup](https://kodim.cz/czechitas/uvod-do-progr/prvni-krucky/vstup-vystup)
- [Sekvenční hodnoty](https://kodim.cz/czechitas/uvod-do-progr/prvni-krucky/sekvence)
  - Pozor vynechali jsme kapitolu s podmínkami (schválně)
- [Parametry příkazové řádky](#parametry-příkazové-řádky) (níže)

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
K těmto parametrům můžete přistupovat pomocí indexu proměnné `sys.argv`, tedy pro první parameter `sys.argv[1]` (na prvním indexu je název skriptu). Podobně jako u funkce `input()`, argumenty jsou vždy řetězce.

### Něco navíc

S tímto principem se můžete setkat i u CLI (Command line interface), tedy aplikací, které jsou ovládané z příkazové řádky. Nejjednoduším příkladem CLI jsou terminály operačních systémů. Ať už se jedná o `PowerShell` ve Windows, nebo například `bash` v Linuxu, či `zsh` v MacOS (což je vpodstatě rozšířený `bash`).

Moc pěkně je CLI vysvětlené v [tomto](https://youtu.be/mUXVBMhr7Xg) videu (anglicky), přímo s ukázkami na Windows.

Pokud by vás CLI zaujali více, doporučuji podívat se na více komplexní python modul `argparse`, kerý je uzpůsobený k vytvoření vašeho vlastního CLI.

# Knowledge check

- Umím naimportovat modul ze standartní knihovny: `import module`
  - Umím naimportovat konkrétní funkci z modulu `from module import function`
- Vím kde najdu standartní knihovnu a oficiální dokumentaci jazyka Python
- Umím vytvořit a spustit soubor s koncovkou `.py`
- Umím spojit hodnoty různých datových typů do jednoho řetězce
  - Použití funcí k přetypování: `str()`, `int()`, `float()`
  - Použití f-stringu: `f"text {variable} text"`
- Znám funkce `print()` a `input()` a umím z terminálu načíst vstup od uživatele a opět ho vypsat
- [Umím přitupovat k jednotlivým písmenům-částem řetězce]
- [Umím definovat seznam hodnot a přitupovat k jednotlivým prvkům]
- [Umím do seznamu přidat prvek]
- [Umím skript zavolat s parametry a opět si je vypsat na výstup]


# Meme for this week

![It's gettin serious](https://memegenerator.net/img/instances/71420730.jpg)
