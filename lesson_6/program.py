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


michal = Zamestnanec('Michal', 'Kvetinar', 10, False)
print(michal)
michal.cerpani_dovolene(12)
print(michal)
michal.cerpani_dovolene(5)
print(michal)