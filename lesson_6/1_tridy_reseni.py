"""
Uvažuj, že navrhuješ software pro zásilkovou společnost.

Vytvoř třídu Balik, která bude mít tři atributy - adresa, hmotnost a doruceno.
První dva atributy nastav pomocí parametrů funkce __init__. Parametr doruceno nastav na začátku jako False.

Připoj ke třídě funkci deliver, která změní hodnotu parametru doruceno na True.
Přidej metodu __str__, která vypíše adresu, hmotnost a informaci o tom, zda byl balík již doručen.
Zkus si vytvořit nějaké objekty ze třídy Balik a ověř, že vše funguje.
"""


class Balik:
    def __init__(self, adresa, hmotnost):
        self.adresa = adresa
        self.hmotnost = hmotnost
        self.doruceno = False

    def deliver(self):
        self.doruceno = True

    def __str__(self):
        if self.doruceno:
            deliveredText = "Balík byl doručen"
        else:
            deliveredText = "Balík zatím nebyl doručen."
        return f"Balík je na adresu {self.adresa} a váží {self.hmotnost}. {deliveredText}"

balik = Balik('Brno', 50)
print(balik)

"""
Zkus pro našeho nakladatele vytvořit software s využitím tříd a objektů.
Vytvoř tedy třídu Kniha, která reprezentuje knihu.
Každá kniha bude mít atributy nazev, pocet_stran a cena. Hodnoty nastav ve funkci __init__.

Přidej knize funkci __str__, která vypíše informace o knize v nějakém pěkném formátu.

Občas se stane, že se kniha moc neprodává a knihkupec se snaží nalákat kupující slevou.
Přidej metodu sleva(), která bude mít jeden parametr - velikost slevy v procentech.
Funkce sníží cenu knihy o dané procento.
"""


class Kniha:
    def __init__(self, nazev, pocet_stran, cena):
        self.nazev = nazev
        self.pocet_stran = pocet_stran
        self.cena = cena

    def __str__(self):
        return f"Název knihy: {self.nazev}. Počet stran: {self.pocet_stran}. Cena: {self.cena}"

    def sleva(self, sleva_v_procentech):
        self.cena *= (1 - sleva_v_procentech / 100)


kniha = Kniha("Noc, která mě zabila", 590, 499)
print(kniha)
kniha.sleva(10)
print(kniha)


"""
U zaměstnanců budeme nově evidovat, jestli jsou ve zkušební době.

Rozšiř metodu __init__ třídy Zamestnanec o parametr zkusebni_doba, který bude typu bool.
Tuto hodnotu ulož jako atribut třídy Zamestnanec.
Uprav metodu __str__. Pokud je zaměstnanec ve zkušební době, přidej k jeho/jejímu výpisu text Je ve zkušební době.
"""


class Zamestnanec:
    def __init__(self, jmeno, pozice, dny_dovolene, zkusebni_doba):
        self.jmeno = jmeno
        self.pozice = pozice
        self.dny_dovolene = dny_dovolene
        self.zkusebni_doba = zkusebni_doba

    # zamenila jsem nasi funkci vypis informace za __str__ protoze to dava vetsi smysl v kontextu zadani (ale muzete si nechat i obe)
    def __str__(self):
        info = f'Zamestnanec se jmenuje {self.jmeno}, pracuje na pozici {self.pozice} a ma {self.dny_dovolene} dni dovolene.'
        if self.zkusebni_doba:
            info += ' A zamestnanec je ve zkusebni dobe.'
        return info

    def cerpani_dovolene(self, dny):
        if dny > self.dny_dovolene:
            print(f'Nemuzes si vzit {dny} dni dovolene, protoze mas pouze {self.dny_dovolene} dni.')
        else:
            self.dny_dovolene -= dny
            # self.dny_dovolene = self.dny_dovolene - dny
            print(f'Vzal sis {dny} dni dovolene, zbyva ti {self.dny_dovolene} dni.')
