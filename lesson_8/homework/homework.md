# Čtení a zápis souborů - csv, json

**Deadline: 17.4. 23:59**

[Odkaz na návod k odevzdání](https://docs.google.com/presentation/d/1iVXiZC8hUy9Irxxqebdaaz7-uTkuJT16/edit?usp=sharing&ouid=104337294426056946104&rtpof=true&sd=true)

## Materiály z lekce
* [Json, requests, api](https://kodim.cz/czechitas/python-data/zaklady-programovani/slovniky-json/#format-json)
* [CSV](../README.md) sekce v materiálech, případně [oficiální dokumentace k csv modulu](https://docs.python.org/3/library/csv.html)

# Obecné požadavky na úkol (vyžaduje více času a vlastní iniciativy)

Velice podobné jako minulý týden, otevřít json nebo csv soubor, upravit soubor a zase ho zapsat. Můžete klidně zkusit nějaké csv předělat na json (nebo naopak).

Pokud chcete využít i modul `requests`, můžete se mrknout na veřejně dostupné [Star Wars API](https://swapi.dev/documentation) a nějaká data vzít odtud (nebo z jiného API, kterí najdete) :)

Pro testování doporučuju uložit data do souboru a tam testovat jejich zpracování, přece jen čtení ze souboru je rychlejší než čekat na odpověď od API, navíc u něktých by se vám mohlo stát že překročíte rate limit, u star wars API je limit 10 000/den, což je poměrně dost.

# Vymyšlené zadání

Pro každý bod níže si ideálně napište separátní funkci.

1. Načtěte si json data z http://hp-api.herokuapp.com/api/characters
2. Uložte je do `hp_characters.json` souboru naformátovaná, tedy ne na jeden řádek.
    * TIP: Možná se vám bude hodit obecnější funkce abyste ji mohli využít i v 5. bodě zadání
3. Načtěte json data ze souboru, funkce může být obecná, v úkolu však budete načítat jen soubor který jste si v předchozím bodu vytvořily.
4. Zjistětě:
   * Kolik různých patronů (klíč `"patronus"`) v datech existuje
   * Kolik postav už nežije
   * Která postava je nejstarší - použijte pouze klíč `yearOfBirth`, na zpracování celého datumu bychom mohli použít modul [`datetime`](https://docs.python.org/3/library/datetime.html) (těžší varianta), ukázka použití například [zde](https://www.geeksforgeeks.org/python-datetime-strptime-function/), datetime objekty se pak dají porovnávat klasicky pomocí `>` a `<`.
5. Zapište to souboru `gryffindor.json` pouze postavy, které mají v klíči `house` hodnotu `"Gryffindor"`
