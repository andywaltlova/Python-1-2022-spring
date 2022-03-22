"""
Částečný úvazek

Naše firma se rozhodla zaměstnávat i pracovníky na částečné úvazky, pro které bude vytvořena zvláštní třída.
Vytvoř novou třídu Brigadnik, která bude dědit od třídy Zamestnanec a bude mít navíc atribut uvazek,
který reprezentuje velikost úvazku oproti plnému.
Přidej informaci o úvazku k výpisu informací do funkce __str__.
"""

class Zamestnanec:
    def __init__(self, jmeno, pozice, dny_dovolene, zkusebni_doba):
        self.jmeno = jmeno
        self.pozice = pozice
        self.dny_dovolene = dny_dovolene
        self.zkusebni_doba = zkusebni_doba

    # zamenila jsem nasi funkci vypis informace za __str__ protoze to dava vetsi smysl v kontextu zadani cviceni (ale muzete si nechat i obe)
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

class Brigadnik(Zamestnanec):
    def __init__(self, jmeno, pozice, dny_dovolene, zkusebni_doba, uvazek):
        super().__init__(jmeno, pozice, dny_dovolene, zkusebni_doba)
        self.uvazek = uvazek

    def __str__(self):
        return super().__str__() + f" Zamestnanec je brigadnik a pracuje pouze na {self.uvazek} uvazek."

michal_brigadnik = Brigadnik('Michal', 'Kvetinar junior', 0, True, 0.3)
print(michal_brigadnik)


"""
Balík
Pokračuj ve své práci pro zásilkovou společnost. Společnost nově doručuje i cenné balíky, které mají zadanou určitou hodnotu.

Vytvoř třídu CennyBalik, která dědí od třídy Balik. CennyBalik má navíc atribut hodnota, ostatní atributy dědí od třídy Balik.
Atribut hodnota nastav pomocí funkce __init__. Ostatní parametry předej funkci __init__ třídy Balik.
Vytvoř si alespoň jeden objekt a zkus volání jeho funkcí.
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

class CennyBalik(Balik):
    def __init__(self, adresa, hmotnost, hodnota):
        super().__init__(adresa, hmotnost)
        self.hodnota = hodnota
    def __str__(self):
        return super().__str__() + f' Jedna se o cenny balik ktery ma hodnotu {self.hodnota} Kc.'

cenny_balik_do_prahy = CennyBalik('Praha', 20, 2000)
print(cenny_balik_do_prahy)