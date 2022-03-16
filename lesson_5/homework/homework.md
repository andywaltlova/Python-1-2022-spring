# Vytvoření uživatelského účtu - generátor hesel

**Deadline: 27.3. 23:59**

[Odkaz na návod k odevzdání](https://docs.google.com/presentation/d/1iVXiZC8hUy9Irxxqebdaaz7-uTkuJT16/edit?usp=sharing&ouid=104337294426056946104&rtpof=true&sd=true)

## Zadání

Napište program který bude simulovat registraci uživatele do systému, tedy vytvoření uživatelského účtu. Program si od uživatele vyžádá potřebné informace k registraci (zvolte si je sami, vzpomeňtě si/najděte si jaké údaje požadují aplikace, které používáte).
Hlavní součástí, kterou je zapotřebí naimplementovat je generátor hesel. Buďte kreativní při generování hesel – silná hesla se skládají z malých písmen, velkých písmen, čísel a symbolů. Hesla by měla být náhodná - při každém spuštění programu se vygeneruje jiné heslo.

Formální požadavky na funkcionalitu (tzn. je mi jedno **jak** konkrétně program napíšete, hlavně že půjde spustit)

- Uživatel zadá svoje osobní údaje
- Uživatel si může zvolit jak dlouhé vygenerované heslo má být.
- Uživatel si může nějakým způsobem zvolit strukturu hesla (konkrétní podmínky jsou na vás). Strukturou je myšleno, že uživatel bude mít možnost nějakým způsobem ovlivnit, jak heslo bude vypada, například že bude mít 3 velká písmena, 1 malé, 2 čísla a bude v něm někde jméno mazlíčka. Konkrétní implementace nebo konkrétní věci které uživatele necháš upravit jsou na tobě - tedy záleží čistě na tobě, jak moc komplikované si to vymyslíš (ideálně začni s jednou možností a postupně přidávej další). Níže jsou nějaké návrhy, které můžeš využít.
  - Minimálně jedno malé písmeno (nebo konkrétní počet)
  - Minimálně jedno velké písmeno (nebo konkrétní počet)
  - Minimálně jedno číslo (nebo konkrétní počet)
  - Minimálně jeden speciální znak (nebo konkrétní počet)
  - Heslo může v nějaké formě obsahovat jméno mazlíčka (pokud ho uživatel zadá)
  - Uživatel může zadat slovo/frázi, která ve výsledném hesle bude obsažena (generátor ji například pouze doplní na potřebný počet znaků a přidá požadovaná specifika výše)
- Výsledné heslo nesmí obsahovat osobní údaje, které uživatel sám zadal (například ruzné kombinace jména, rok narození, místo pobytu apod.)
- Program pomocí try/except bloku (alespoň jednoho) zachytí situace, kdy uživatel na vstup poskytne špatná vstupní data (jiný datový typ, nedostatečný počet argumentů apod.)
  - Materiály k vyjímkám jsou dostupné na [kodím](https://kodim.cz/czechitas/progr2-python/zaklady-programovani-2/vyjimky) případně [v oficiální dokumentaci](https://docs.python.org/3/tutorial/errors.html#handling-exceptions), případně [oficialní seznam výjimek](https://docs.python.org/3/library/exceptions.html).
- Uveďte stručné pokyny pro opravujícího, tedy napiště jakým způsobem by měl váš program použít (pokud budete mit řešení formou command-line interface, můžete použít help příkaz podobně jako v úkolu ze 3.lekce)

Tipy:

- Využijte funkce z modulu `random`. Například [`shuffle`, `choice` nebo `choices`](https://docs.python.org/3/library/random.html#functions-for-sequences).
- Pro specifikování sekvencí ruzných znaků můžete použít proměnné z modulu [`string`](https://docs.python.org/3/library/string.html#string-constants).
- Snažte se problém rozdělit na menší problémy a za použití funkcí zbytečně neduplikovat kód
- Využijte poziční argumenty a funkci input pro získání vstupu od uživatele - můžete to nakombinovat.

## Knowledge check
  - Vím jak v Pythonu ošetřit výjimky
