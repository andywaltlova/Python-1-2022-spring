import sys

params = sys.argv[1:]


# Moje menicko
coffe = 12
milkshake = 10
tea = 34

pancakes = 55
muffin = 80
cake = 45

# Promenna pro vyslednou cenu
price = 0


if len(params) == 1:
    print('Vitejte v cukrárně u Andy')
    print('Na dnešním menu můžete najít:')
    print(f'Kávu: {coffe} Kč')
    print(f'Čaj: {tea} Kč')
    print(f'Milkshake: {milkshake} Kč')
    print('---')
    print(f'Palačinky: {pancakes} Kč')
    print(f'Muffin: {muffin} Kč')
    print(f'Dort: {cake} Kč')
    print()
    print('Snídani si můžete objednat ve formátu:')
    print('`python3 order_breakfast.py DRINK FOOD NO_PEOPLE TOGO TIP`')
    print('DRINK - nápoj z menu fe formátu: drink-size, kde size je big nebo small')
    print('FOOD - jídlo z menu')
    print('NO_PEOPLE - číslo indikující kolik snídaní objednávám (předpokládáme, že všechny osoby si dávají stejné jídlo)')
    print('TOGO - pokud chceme snídani s sebou hodnota 1, jinak 0')
    print('TIP - pokud chceme dát spropitné hodnota 1, jinak 0')
    exit()

# Predpokladam ze bude 1 nebo 5 (s jinym poctem selze)
drink, food, no_people, togo, tip = params

# DRINK
drink_price = 0
drink, size = drink.split('-')

if drink == 'coffe':
    drink_price = coffe
elif drink == 'tea':
    drink_price = tea
else:
    drink_price = milkshake

if size == 'big':
    drink_price += drink_price/2

# FOOD
food_price = 0
if food == 'pancakes':
    food_price = pancakes
elif food == 'muffin':
    food_price = muffin
else:
    food_price = cake

# NO_PEOPLE
no_people = int(no_people)

# TOGO
materials_price = 0
if togo == '1':
    materials_price += no_people * 10

# Celková cena (bez spropitného)

price = (drink_price + food_price + materials_price) * no_people

# TIP
tip_amount = 0
if tip == '1':
    tip_amount = (price / 100) * 10


price += tip_amount

print('Shrnutí objednávky:')
print()
print(f'Number of breakfasts: {no_people}')
print(f'{drink}-{size}: {drink_price} Kč')
print(f'{food}: {food_price} Kč')
if materials_price > 0:
    print(f'Materials to-go: {materials_price} Kč')
if tip_amount != 0:
    print(f'Tip amount: {tip_amount} Kč')
print(10 * '-')
print(f'Price: {price} Kč')
