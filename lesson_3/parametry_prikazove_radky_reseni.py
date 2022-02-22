import sys
import math
import statistics

# Čas v minutách
# Napište program minuty.py, která dělá obrácenou věc než program cas.py z textu výše. Když mu na příkazové řádce předáme
# dva parametry ‒ počet hodin a počet minut ‒ například takto
# $ python3 minuty.py 2 54
# program nám vrátí délku tohoto času minutách. V tomto případě tedy číslo 174.
# Nejprve program napište tak, že si hodnoty 2 a 54 uložíte přímo natvrdo v programu do nějakých proměnných a z nich spočítáte a vytisknete výsledek.
# Až když váš program bude fungovat, zkuste tyto proměnné načíst z parametrů příkazové řádky.
# Nezapomeňte, že parametry jsou vždy řetězce a že první parametr je vždy název vašeho programu.

hours = int(sys.argv[1])
minutes = int(sys.argv[2])
print(hours * 60 + minutes)


# Zaokrouhlování
# Napište program, který dostane na vstupu desetinné číslo a na výstup napíše toto číslo zaokrouhlené nejdříve nahoru,
# potom dolů a potom běžným Pythonovským zaokrouhlováním.

float_num = float(sys.argv[1])
print('Nahoru: ',math.floor(float_num))
print('Dolu: ',math.ceil(float_num))
print('Klasicky: ',round(float_num))


# Doména na URL
# Napište program url.py, který jako parametr dostane název domény, například kodim.cz a na výstup vypíše URL,
# kterou je třeba zadat do prohlížeče pro přístup k webové stránce na této doméně, tedy http://kodim.cz.

domain = float_num = sys.argv[1]
print(f'https://{domain}')
print('https://' + domain)


# Průměr versus medián - VYNECHALI JSME
# Často se hovoří o tom, že průměr není pro některé veličiny (například platy) vypovídající hodnota a lepší je dívat se na medián.
# Napište program, který s použitím funkcí statistics.mean() a statistics.median() vypíše na výstup průměr a medián zadaných hodnot.
# Hodnoty program obdrží na příkazovém řádku.

# Příklad použití:
# $ python3 prumer-median.py 2 1 8 3 4 11 7 1512
# Průměr: 193.5
# Medián: 5.5

# numbers = sys.argv[1:]
# int_values = [int(num) for num in numbers] # jeste jsme nedelali list comprehension, budeme delat priste spolu s cykly
# print('Prumer: ', statistics.mean(int_values))
# print('Median: ', statistics.median(int_values))


# BONUS - Klasické zaokrouhlování
# Jazyk Python překvapivě neposkytuje žádnou funkci, která by dělala klasické zaokrouhlování, tedy takové, na které jsme všichni zvyklí ze školy.
# S něčím takovým se nemůžeme spokojit.

# Napište program, který dostane na vstupu nezáporné číslo a zaokrouhlí jej klasickým zaokrouhlováním.
# Zkuste vymyslet jak to udělat co nejúsporněji s použitím zaokrouhlovacích funkcí, které už znáte.

cislo = 2.5  # cislo opet muzeme vzit i jako parametr
zaokrouhlene = math.floor(cislo + 0.5)
print(zaokrouhlene)