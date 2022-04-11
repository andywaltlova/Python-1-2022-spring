# 3. Fíha banka a.s. nabízí na svých stránkách spořící účet s úrokem 2.4 %.
# Když si na takový účet uložíte 1 000 000 kč, kolik peněz nastřádáte za 10 let?

money = 1_000_000
interest = 2.4
for i in range(10):
    money *= interest
# print(f'Za 10 let nastradame: {money} Kc.')

# 4. Délka filmu
# V programu kin se často uvádí délka filmu v minutách.
# Například rozšířená verze filmu Pán prstenů: Dvě věže trvá 223 minut.
# My bychom ovšem délku filmu raději věděli v hodinách a minutách.
# Použijte operátory celočíselného dělení a dělení se zbytkem, abyste spočetli,
# kolik hodin a minut trvá film Pán prstenů: Dvě věže.

total_length = 223
hours = total_length // 60
minutes = total_length % 60
# print(f'Pán prstenů: Dvě věže: {hours}h a {minutes} minut.')

# 5. Průměrní teploty
# Následující tabulka obsahuje průměrné roční teploty v České republice za roky 2001 až 2010 (zdroj: Český hydrometeorologický ústav).

# rok	teplota °C
# 2001	7.8
# 2002	8.7
# 2003	8.2
# 2004	7.8
# 2005	7.7
# 2006	8.2
# 2007	9.1
# 2008	8.9
# 2009	8.4
# 2010	7.2
# Vytvořte reprezentaci této tabulky pomocí seznamu seznamů. Zde existují dvě možnosti.
# Nejprve vytvořte seznam, který obsahuje řádky tabulky jako dvouprvkové seznamy a uložte jej do proměnné radky.
# Poté vytvořte seznam, který obsahuje sloupce tabulky, tedy dva seznamy po deseti prvcích. Uložte jej do proměnné sloupce.

radky = [
    [2001, 7.8],
    [2002, 8.7],
    [2003, 8.2],
    [2004, 7.8],
    [2005, 7.7],
    [2006, 8.2],
    [2007, 9.1],
    [2008, 8.9],
    [2009, 8.4],
    [2010, 7.2],
]

sloupce = [
    [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010], # nebo list(range(2001, 2011))
    [7.8, 8.7, 8.2, 7.8, 7.7, 8.2, 9.1, 8.9, 8.4, 7.2]
]

# Pro obě tyto reprezentace vyřešte následující úkoly

# Získejte teplotu na třetím řádku tabulky.
print(radky[2][1])
print(sloupce[1][2])

# Získejte rok na pátém řádku tabulky.
print(radky[4][0])
print(sloupce[0][4])

# Získejte poslední řádek tabulky jako seznam.
print(radky[-1])
print([sloupce[0][-1], sloupce[1][-1]])

# Vytvořte tabulku bez prvních dvou řádků.
print(radky[2:])
print([sloupce[0][2:], sloupce[1][2:]])

# Vytvořte tabulku pouze z prvních dvou řádků.
print(radky[:2])
print([sloupce[0][:2], sloupce[1][:2]])

# Vytvořte tabulku obsahující jen řádky 5, 6, 7, 8.
print(radky[5:9])
print([sloupce[0][5:9], sloupce[1][5:9]])

# Použitím proměnné sloupce vypište seznam teplot seřazený vzestupně podle velikosti.
# Šlo by to i pomocí proměnné radky, ale to ještě neumíme.
print(sorted(sloupce[1]))

# pomoci radky - list comprehension
print(sorted([teplota for rok, teplota in radky]))

# 6 Průměr
# Mějme proměnnou s, ve které předpokládáme uložený nějaký seznam.
# Sestavte v Python konzoli výraz (vzoreček), který spočítá průměrnou hodnotu
# v takovém seznamu. Otestujte jej na seznamech různých délek.

s = [1, 2, 3, 4, 5, 6]
print(sum(s)/len(s))


# 7 Nový koberec
# Do místnosti tvaru čtverce o rozloze 30 m2 potřebujeme koupit nový koberec.
# Jakou délku má mít strana koberce? Vejde se nám srolovaný do dodávky s nákladovým
# prostorem dlouhým 5 m?

# tady teoreticky nemusime nic pocitat, protoze jedna strana muze tedy mit maximalne 5m
# aby se koberec vesel do auta, 5*5 je 25 (obsah ctverce), coz logicky znamena ze nam nestaci 5m dlouhy prostor

max_length = 5
needed_area = 30
it_will_fit = max_length*max_length >= needed_area
print(it_will_fit)

# 8 Rozpětí
# Postupujte obdobně jako v úložce Průměr, ale tentokrát sestavte výraz pro výpočet rozpětí,
# tedy rozdílu mezi minimální a maximální hodnotou.

s = list(range(33, 45))
print(max(s) - min(s))

# 9. Vlastní minimum a maximum
# Prohlédněte si funkce pro práci se seznamy uvedené dříve v obsahu lekce.
# Představte si, že bychom neměli k dispozici funkce min() a max().
# Dokázali byste vytvořit výraz, který zjistí minimální resp. maximální hodnotu
# v seznamu uloženém v proměnné s? Můžete v tomto vzorečku použít cokoliv,
# co jsme probrali na lekci kromě samotných funkcí min() a max().

# muzeme pouzit napriklad funkci sorted

s = list(range(30,45))

minimum = sorted(s)[0]
maximum = sorted(s)[-1]
print(minimum, maximum)

# 10. Střed seznamu
# Sestavte výraz, který vrátí číslo nacházející se přesně uprostřed v zadaném seznamu s.
# U seznamů liché délky je střed jasně definovaný, ovšem u seznamů sudé délky nám padne mezi
# dvě čísla. V takovém případě vyberte jako střed číslo blíže ke konci seznamu.
import math
s = [1, 2, 3, 4, 5, 6]
middle = math.ceil(len(s) / 2)
print(s[middle])

# toto reseni nefunguje spravne na seznam o delce 1

# 11. Střed seznamu podruhé
# Sestavte vzoreček, který vrátí číslo nacházející se přesně uprostřed v zadaném seznamu s.
# Tentokrát však u seznamů sudé délky vyberte jako střed číslo blíž k začátku seznamu.
import math
s = [1, 2, 3, 4, 5, 6]
middle = math.ceil(len(s) / 2) - 1
print(s[middle])

# Oba priklady jsou resit pomoci podminek a rozliseni sude/liche delky pomoci operatoru %