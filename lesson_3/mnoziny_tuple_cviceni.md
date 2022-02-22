# Množiny a jejich metody

Během tohoto úkolu jsou zadány pouze funkční pořadavky, způsob jakým docílíte výsledku je na vás. Doporučuji si prohlédnout metody dostupné pro množiny a rozmyslet si, která je ideální pro daný úkol.

Máme dané množiny:

```py
a = {'dog', 'cat', 'bird'}
b = {'dog', 'mouse', 'tiger', 'bird'}
```

1. Vypište prvky, které mají obě množiny společné
2. Vypište prvky, které jsou vždy pouze v jedné z množin
3. Vypište všechny prvky které jsou v obou množinách dohromady (bez duplicit)
4. Upravte množiny tak, aby jejich průnik (tedy prvky, které mají společné) byl prázdný

# Tuple

1. Vyzkoušejte si, že umíte předělat list na tuple (funkce `tuple()`) a naopak (funkce `list()`).

2. Vyzkoušejte si co se stane, když budete chtít rozbalit sekvenci do málo/moc proměnných. Prohlédněte si typ chybové hlášky.

```py
my_list = ['a', 'b', 'c']
a, b = my_list
a, b, c ,d = my_list
```

3. Vyzkoušejte si co se stane když budete chtít v tuple přepsat hodnotu.

```py
my_tuple = ('a', 'b', 'C')
my_tuple[2] = 'c'
```