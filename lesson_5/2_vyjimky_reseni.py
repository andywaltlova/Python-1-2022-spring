# 1 Ošetření dělení nulou
# Předchozí ukázku uprav následujícím způsobem:

# Program bude na příkazové řádce očekávat dva parametry
# Parametry mohou být celá nebo desetinná čísla
# Vypiš podíl těchto čísel
# Ošetři, aby program nezhavaroval při pokusu o dělení nulou

# Všechny chyby řeš ošetřováním výjimek.


def division(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print('[Warning] Zero division')

# Nejake dalsi varianty reseni
# def division(a, b):
#     result = 0
#     try:
#         result = a/b
#     except ZeroDivisionError:
#         print('[Warning] Zero division')
#     return result

# Pouziti druheho pristupu kdy nejdriv kontrolujeme hodnoty
# def division(a, b):
#     if b == 0:
#         print('[Warning] Zero division')
#         return #stejne jako kdybychom meli primo return None
#     return a/b


print(division(2, 1))

# Vsimnete si ze se po spusteni vypise i None, protoze funkce dela vypis i vraci None (defaultne kdyz neni receno jinak)
# Mohli bysme i vracet string, ja jsem to neudelala, protoze mi prijde lepsi,
# kdyz funkce konstantne vraci stejny datovy typ (nebo nic), maloktera funkce vraci nekdy int a nekdy str.
print(division(2, 0))
