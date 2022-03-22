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


class Manazer(Zamestnanec):
    def __init__(self, jmeno, pozice, dny_dovolene, zkusebni_doba, pocet_podrizenych):
        super().__init__(jmeno, pozice, dny_dovolene, zkusebni_doba)
        # self.jmeno = jmeno
        # self.pozice = pozice
        # self.dny_dovolene = dny_dovolene
        # self.zkusebni_doba = zkusebni_doba
        self.pocet_podrizenych = pocet_podrizenych

    def __str__(self):
        return super().__str__() + f' Jako manazer ma {self.pocet_podrizenych} podrizenych.'

michal = Zamestnanec('Michal1', 'Kvetinar', 10, False)
print(michal)
michal_boss = Manazer('Michal2', 'Vedouci Kvetinarstvi', 20, True, 2)
print(michal_boss)
# michal_boss.cerpani_dovolene(10)
# print(michal_boss)

