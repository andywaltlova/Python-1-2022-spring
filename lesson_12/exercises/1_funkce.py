# 1 Obsah elipsy
# Tentokrát chceme spočítat plochu pozemku ve tvaru elipsy jako na obrázku.
# Z matematiky víme, že známe-li šířku a výšku elipsy, její obsah je polovina šířky krát polovina výšky krát číslo pí. 
# Napište funkci elipseArea, která spočítá plochu pozemku dle zadané šířky a výšky. Číslo pí najdete v modulu math jako math.pi.
from math import pi

def obsah_elipsy(sirka, vyska):
    return (sirka / 2) * (vyska / 2) * pi

# 2 Větší ze dvou čísel
# Napište funkci jménem max2, který vrátí větší ze dvou zadaných čísel.
def max2(a, b):
    return a if a > b else b # nebo samozrejme rozepsana podminka na vice radku


# 3 Geometrický průměr
# Napište funkci jménem gmean, která spočítá takzvaný geometrický průměr ze zadaného seznamu čísel.
# Geometrický průměr n čísel se spočítá tak, že se všechny hodnoty navzájem vynásobí a z výsledného součinu se spočítá n-tá odmocnina.
def gmean(list_hodnot):
    product = 1 # nemuze byt nula, protoze  o * x je vzdy nula
    for hodnota in list_hodnot:
        product *= hodnota

    # 2 odmocnina je matematicky x na (1/2), 3 je x na (1/3), n-ta je tedy x na (1/n)
    # mocneni je v pythone operator **
    return product ** (1/len(list_hodnot))

# 4 Větší ze tří čísel
# Napište funkci jménem max3, který vrátí největší ze tří zadaných čísel.
def max3(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    return c