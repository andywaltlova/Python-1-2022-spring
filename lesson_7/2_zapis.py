"""
Rozepsaná výplata
Modifikujte program pro počítání výplaty z předchozí sekce tak,
aby nevypisoval průměrnou výplatu za rok, nýbrž aby vypsal konkrétní vyplacenou částku pro každý měsíc zvlášť.

Nejprve tyto informace vypište na výstup pomocí funkce print().
Poté program upravte tak, aby vypsal tyto výsledky do souboru.
"""
# Zase muzeme klidne rovnou pouzit pro kazde cviceni samostatnou funkci
# Ja to pouzivam protoze pak nemusim vice kodu komentovat

def rozepsana_vyplata():
    #  Z predchoziho cviceni
    with open('vykaz.txt') as f:
        hours_per_month = [int(line) for line in f.readlines()]
    hour_pay = int(input('Zadej hodinovou mzdu: '))

    # novy kod - print
    for month_hours in hours_per_month:
        month_salary = month_hours * hour_pay
        print(f'{month_salary} Kc')

    # novy kod - do souboru (varianta s list comprehension)
    with open('vyplata_vystup.txt', mode='w', encoding='utf-8') as file:
        lines = [f'{month_hours * hour_pay} Kc\n' for month_hours in hours_per_month]
        file.writelines(lines)

# rozepsana_vyplata()

"""
Hody kostkou
Napište program, který vytvoří seznam deseti náhodných hodů dvanáctistěnnou kostkou.

Nejdříve tento seznam vytiskněte na konzoli pomocí funkce print().
Upravte váš program tak, aby náhodné hody kostkou vypsal do souboru s názvem hody.txt na jeden řádek oddělené čárkou a mezerou.
Upravte váš program tak, aby počet hodů dostal jako parametr na příkazové řádce. Zkuste použitím vašeho programu vyrobit 100, 1000 a 10 000 hodů.
"""
import random
import sys

def hody_kostkou(args):
    # funkce z modulu random
    pocet_hodu = int(args[1])
    hody = [random.randint(1,6) for i in range(pocet_hodu)]
    # pouze print
    print(hody)

    # do souboru pomoci oddeleni carkami

    # pomoci for cyklu
    with open('hody.txt', mode='w', encoding='utf-8') as f:
        for hod in hody:
            f.write(f'{hod}, ')
        # Tady vam zustane carka a mezera na konci, nize jsou dlasi varianty

    # pomoci metody join si vytvorit string
    with open('hody.txt', mode='w', encoding='utf-8') as f:
        hody_s_carkami = ", ".join([str(hod) for hod in hody])
        f.writelines(hody_s_carkami)

    # A nebo pomoci for cyklu vytvorit string k zapisu
    with open('hody.txt', mode='w', encoding='utf-8') as f:
        content = ''
        for hod in hody:
            content += f'{hod}, '
        # Pokud nechcete mit za poslednim cislem carku a mezeru muzete pouzit metodu rstrip()
        # content = content.rstrip(', ')
        f.writelines(content)

# hody_kostkou(sys.argv)

"""
Dny v měsíci
Napište program, který bude mít přímo v kódu zapsaný počet dní v jednotlivých měsících takto:

pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
Nechte váš program vypsat tento seznam do souboru s názvem kalendar.txt, každé číslo na jeden řádek.
Upravte váš program tak, aby zároveň s počtem dnů vypisoval i název měsíce. Oddělte v souboru název měsíce a počet dnů pomocí tabulátoru.
Upravte váš program tak, aby jako první řádek výsledného souboru obsahoval nadpisy pro jednotlivé sloupce, tedy měsíc a počet dní.
"""

def dny_v_mesici():
    pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    with open('kalendar.txt', mode='w', encoding='utf-8') as f:
        for den in pocty_dni:
            f.write(f'{den}\n')

    # S nazvy mesicu
    with open('kalendar.txt', mode='w', encoding='utf-8') as f:
        for den in pocty_dni:
            f.write(f'{den}\n')
    # Muzete si na nazvy mesice vytvorit take list, pripadne upravit predchozi list, nebo treba pouzit nazvy mesicu z modulu calendar

    # Vlastni mesice
    months = ['Leden', 'Unor', 'Brezen', 'Duben', 'Kveten', 'Cerven', 'Cervenec', 'Srpen', 'Zari', 'Rijen', 'Listopad', 'Prosinec']

    # Mesice z modulu calendar
    # je treba posunou index, protoze promenna z modulu ma na 0 nic, a az na 1 leden atd.
    # import calendar
    # months = list(calendar.month_name)[1:]

    with open('kalendar.txt', mode='w', encoding='utf-8') as f:
        f.write(f'Mesic\tPocet dnu\n') # Pro zahlavi

        # zip dela ze dvou listu list dvojic https://docs.python.org/3/library/functions.html#zip
        for month, days in zip(months, pocty_dni):
            f.write(f'{month}\t{days}\n')
            # Mozna lepsi nez tabulator je zarovnat mesice na deset znaku zleva pomoci formatovan iv f stringu (jen pro zajimavost)
            # f.write(f'{month:<10}{days}\n')

    # slo by resit i s range(12) a indexovat oba listy stejnym indexem
    with open('kalendar.txt', mode='w', encoding='utf-8') as f:
        for i in range(12):
            f.write(f'{months[i]}\t{pocty_dni[i]}\n')


dny_v_mesici()