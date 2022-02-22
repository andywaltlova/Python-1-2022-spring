# Množiny a jejich metody (https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)

# Během tohoto úkolu jsou zadány pouze funkční pořadavky, způsob jakým docílíte výsledku je na vás.
# Doporučuji si prohlédnout metody dostupné pro množiny a rozmyslet si, která je ideální pro daný úkol.

# Máme dané množiny:
a = {'dog', 'cat', 'bird'}
b = {'dog', 'mouse', 'tiger', 'bird'}

# 1. Vypište prvky, které mají obě množiny společné
print(a.intersection(b))
# 2. Vypište prvky, které jsou vždy pouze v jedné z množin
print(a.symmetric_difference(b))
# 3. Vypište všechny prvky které jsou v obou množinách dohromady (bez duplicit)
print(a.union(b))
# 4. Upravte množiny tak, aby jejich průnik (tedy prvky, které mají společné) byl prázdný

a.remove('dog')
a.remove('bird')
print(a.intersection(b))

# Tuple

# 1. Vyzkoušejte si, že umíte předělat list na tuple (`funkce tuple()`) a naopak (funkce `list()`).

my_tuple = ('a', 'b', 'c')
my_list = list(my_tuple)
my_tuple_again = tuple(my_list)

print(my_tuple)
print(my_list)
print(my_tuple_again)


# 2. Vyzkoušejte si co se stane, když budete chtít rozbalit sekvenci do málo/moc proměnných. Prohlédněte si typ chybové hlášky.
my_list = ['a', 'b', 'c']
a, b = my_list
a, b, c ,d = my_list

# 3. Vyzkoušejte si co se stane když budete chtít v tuple přepsat hodnotu.
my_tuple = ('a', 'b', 'C')
my_tuple[2] = 'c'
