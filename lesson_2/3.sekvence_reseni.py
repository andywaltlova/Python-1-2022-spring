# 1 Řetězce jako sekvence
# Uložte si v Python konzoli do proměnné jmeno svoje celé jméno a nechte vypsat jeho třetí, pátý a sedmý znak.
# Vyzkoušejte, co se stane, když budete chtít znak na pozici, která překračuje délku řetězce.
uzivatel = input("Zadej uživatelské jméno: ")

print(uzivatel[2]) # treti znak
print(uzivatel[4]) # paty znak
print(uzivatel[6]) # sedmy znak


# 2 Seznamy
# Celé toto cvičení dělejte v příkazové řádce Pythonu.

# Vytvořte nějaký seznam celých čísel, například počty diváků na několika po sobě jdoucích představeních. Použije metodu append a přidejte do seznamu počet diváků na jednom dalším představení.
pocty_divaku = [120, 100, 95, 78, 100]
pocty_divaku.append(113)
# Vytvořte nějaký seznam desetinných čísel, například zaplněnost divadla v několika po sobě jdoucích představeních.
zaplnenost = [0.9, 0.8, 0.7, 0.65, 0.8, 0.85]
# Vytvořte nějaký seznam řetězců, například seznam názvů několika divadelních představení, která divadlo hraje. Uložte tento seznam do proměnné hry. Uložte do nějaké proměnné druhou položku tohoto seznamu.
hry = ["Hra A", "Hra B", "Hra C", "Hra D", "Hra E", "Hra F"]
druha_hra = hry[1]
# Do proměnné hodnoceni uložte seznam hodnocení, které obdržela divadelní hra “Plyšáci na útěku” v různých recenzních časopisech. Hodnocení je vždy dvouprvkový seznam obsahující název recenzního časopisu jako řetězec a samotné hodnocení jako číslo mezi 1 až 10. Přidejte na konec tohoto seznamu nové hodnocení z časopisu Divadelní oběžník.
hodnoceni = [["Casopis A", 5], ["Casopis B", 8], ["Casopis C", 7]]
hodnoceni.append["Divadelni obeznik", 7]