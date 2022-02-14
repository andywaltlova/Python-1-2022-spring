# První skript

**Deadline: 23.2. 23:59**

[Odkaz na navod k odevzdani](https://docs.google.com/presentation/d/1iVXiZC8hUy9Irxxqebdaaz7-uTkuJT16/edit?usp=sharing&ouid=104337294426056946104&rtpof=true&sd=true)


## 1. možnost (více volnosti pro vlastní fantazii a to co vás zajímá)
Tato varianta úkolu pouze specifikuje co skript má dělat, způsob jakým toho dosáhnete je na vás.

- Načíst hodnotu (nebo více hodnot) od uživatele (funkce `input()` nebo parametry příkazové řádky)
- Naimportovat si modul (Pouze [standartní knihovna](https://docs.python.org/3/library/))
  - doporučuji [matematické moduly](https://docs.python.org/3/library/numeric.html), nebo například modul [`calendar`](https://docs.python.org/3/library/calendar.html)
  - úkolem je alespoň trochu se zorientovat v dokumentaci, nevadí tedy pokud si kus kódu najdete a do úkolu zkopírujete
- Použít alespoň jednu funkci z naimportovaného modulu
- Vypsat výsledek funkce na výstup (po spuštění skripu tedy uvidím nějakou zprávu v terminálu)
  - Můžete například udělat vypočet nebo transformaci textu.

## 2. možnost (chci už vymyšlené zadání)

Vyvoříme si mini program, kterému na vstup zadáme rok, měsíc a den. Výstupem programu bude řetězec oznamující, který den v týdnu reprezentuje zadané datum.Ke zjištění dne v týdne použijeme funkci a proměnnou z modulu [`calendar`](https://docs.python.org/3/library/calendar.html), konkrétně funkci [`calendar.weekday(year, month, day)`](https://docs.python.org/3/library/calendar.html#calendar.weekday) a proměnnou [`calendar.day_name`](https://docs.python.org/3/library/calendar.html#calendar.day_name).

Tedy například pokud skriptu dám den 14, měsíc 2 a rok 2022 výsledkem bude `14-2-2022 was Monday`.

Problém doporučuji rozdělit na menší podproblémy a ty řešit postupně.

1. Import potřebného modulu
2. Načtení vstupu (použijte jeden ze způsobů, které jsme si ukazovali - `input()`, parametry příkazové řádky)
3. Správně zavolat funkci `calendar.weekday()` a výsledek si uložit do proměnné
4. Správně využít výsledek z předchozího volání funkce `calendar.weekday()` k získání názvu dne z proměnné `calendar.day_name`
5. Jednotlivé části spojit do řetězce
6. Řetězec vypsat na výstup pomocí funkce `print()`
