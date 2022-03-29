# Opakovani syntaxe tridy
# class Country:
#     def __init__(self, name, population):
#         self.name = name
#         self.population = population

#     def __str__(self):
#         return self.name

# class CzechRepublic(Country):
#     def __init__(self):
#         super().__init__('Czech Republic', 10)


# cz = CzechRepublic()
# print(cz)



# Cteni souboru

# file = open('mereni.txt', encoding='utf-8')

# # for line in file.readlines():
# #     print(line)

# file.close()

with open('mereni.txt', encoding='utf-8', mode='r') as txt_file:
    lines = txt_file.readlines()
# print(lines)

# Rozdeleni podle tabulatoru

# result = []
# for line in lines:
#     result.append(line.split('\t'))
# print(result)

lines = [line.split('\t') for line in lines]

# Predelani cisla na cislo
lines_int = [[day[0], float(day[1])] for day in lines]

# result = []
# for name, num in lines:
#     result.append([name, float(num)])
# print(result)

# print(lines_int)


## Zapis do souboru

jmena = ['Roman', 'Jana', 'Radek', 'Petra', 'Vlasta']
with open('uzivatele.txt', mode='w', encoding='utf-8') as f:
    # f.writelines(jmena)
    # for jmeno in jmena:
    #     f.write(f'{jmeno}\n')

    jmena_s_newline = [f'{jmeno}\n' for jmeno in jmena]
    # jmena_s_newline[-1] = jmena_s_newline[-1].rstrip('\t')

    f.writelines(jmena_s_newline)




