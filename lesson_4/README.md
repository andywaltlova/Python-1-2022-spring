# Outline

1. For loop, `range()`
2. List comprehension
   - inline podmínky
3. Slovníky
   - Dict comprehension
4. While loop + `break`, `continue`

# Materials

## Links

- [Cykly - for loop](https://kodim.cz/czechitas/uvod-do-progr/prvni-krucky/cykly)
- [List comprehension](https://kodim.cz/czechitas/python-data/zaklady-programovani/text-chroustani/#chroustani-seznamu)
  - [One line if statement](#podmínky-na-jeden-řádek)
- [Slovníky](https://kodim.cz/czechitas/progr2-python/zaklady-programovani-2/slovniky)
  - [Slovníky a cykly](https://kodim.cz/czechitas/progr2-python/zaklady-programovani-2/slovniky-a-cykly)
  - [Dict comprehension](#dict-comprehension)
- [Cykly - přerušení a while loop](https://kodim.cz/czechitas/progr2-python/zaklady-programovani-2/cykly-2)

## Podmínky na jeden řádek

My už umíme psát klasické podmínky:

```py
its_raining = True
if its_raining:
    print("You need an umbrella!")
else:
    print("You don't need an umbrella!")
```

Co kdybychom chtěli tento zápis ještě zkrátit? Je to možné? Ano je! Mohli bychom si všimnout, že řetězce ve funkci print se liší jen jedním slovem a to je `"don't"`. Jak to tedy zapsat jinak? Můžeme využít jednořádkové podmínky a nám již známe f-stringy.

```py
its_raining = True
its_raining_str = "need" if its_raining else "don't need"

print(f"You {its_raining_str} an umbrella!")
```

Ze začátk use může zápis zdát matoucí, ale při přečtení zleva doprava dává smysl, první je hodnota která se do proměnné uloží pokud podmínka platí a za klíčovým slovem else je hodnota, která se do proměnné uloží v opačném případe.

Pokud přemýšlíte, zda se i takové podmínky dají vnořit do sebe, tak ano dají, ale pozor na čitelnost :)

```py
name = 'Mr. Anderson'
greetings = 'Hello ' + 'there' if not name else 'Neo' if name == 'Mr. Anderson' else name
```

## Dict comprehension
Už známe list comprehension z kapitoly na kódím. Python umí stejným způsobem konstruovat i slovníky, případně i množiny. Pokud chceme zkonstruovat slovník pomocí zkráceného zápisu, tedy dict comprehension, nesmíme zapomenout, že slovník vždy očekává pár, tedy klíč a jeho hodnotu. V případě množin je syntaxe stejná jako list comprehension, pouze závorky se liší.

```py
# Conversion of list to dict
list_of_pairs = [[1,'one'], [2,'two']]
pairs_dict = {pair[0]:pair[1] for pair in list_of_pairs}

points = {
    'Iva' : 3,
    'Bara': 30,
    'Klara':15
}
# Creating filtered copy of already existing dict (only record with points higher than 10)
filered_dict = {k:v for k,v in points.items() if v > 10}

# And to be complete, here is set comprehension
nums = {i+1 for i in range(10)}
```

# Knowledge check

- Umím syntaxi pro for loop
  - Umím procházet sekvence - řetězce, listy, slovníky a rozsahy (`range()`)
- Umím napsat list comprehension
  - Vím jak použít inline if statement v list comprehension
- Vím jaký je rozdíl mezi klasickým for cyklem a list comprehension
- Vím jak se vytváří slovník a kde je vhodné ho použít
- Vím, že existuje dict a set comprehension (stejný princip jako list comprehension)
- Vím, že je možnost cyklus přerušit (`break`), případne iteraci přeskočit (`continue`)

# Meme for this week

![Python loop](https://preview.redd.it/vzs32ng8lpi21.gif?format=png8&s=86b4afedbed61221a54b6a077275a164ebcf4723)
