import sys

parametry = sys.argv[1:]

parametry_int = []
sum_cisel = 0
for cislo in parametry:
    cislo_int = int(cislo)
    if cislo_int % 2 == 0:
        parametry_int.append(cislo_int)
        sum_cisel += cislo_int
        # sum_cisel = sum_cisel + cislo_int


# print(parametry)
# print(parametry_int)
# print(sum_cisel)
# print(sum(parametry_int))



parametry = sys.argv[1:]

parametry_int = []
for cislo in parametry:
    cislo_int = int(cislo)
    if cislo_int % 2 == 0:
        parametry_int.append(cislo_int)

# print(parametry_int)

# parametry_int_2 = [f'{cislo}.' for cislo in parametry if int(cislo) % 2 == 0]
# print(parametry_int_2)


pisemky = [
  [1, 3, 2, 1],
  [3, 1, 1, 2],
  [4, 2, 2, 2],
  [1, 1, 1, 1],
  [1, 2, 2, 1],
  [1, 4, 1, 3]
]

# prvni_prvky = []
# for pisemka in pisemky:
#     for znamka in pisemka:
#         print(znamka)

# znamky = [round(znamka) for pisemka in pisemky for znamka in pisemka]
# print(znamky)


vehicle = {
    "ID": 1815,
    "IDB": 0,
    "IDC": 0,
    "VType": 0,
    "LType": 0,
    "Lat": 49.187908,
    "Lng": 16.594223,
    "Bearing": 315,
    "LineID": 5,
    "LineName": "5",
    "RouteID": 5210,
    "Course": "00511",
    "LF": True,
    "Delay": 0,
    "LastStopID": 1512,
    "FinalStopID": 1646,
    "IsInactive": False
}

# Vypsani hodnoty ktera patri k danemu klici
# print(vehicle['Delay'])

# Pridani hodnoty
vehicle['Color'] = 'Red'
vehicle['Color'] += '-Blue'
# vehicle['Color'] = vehicle['Color'] + '-Blue'

print(vehicle['Color'])

# value = vehicle.pop('Color')
# print(value)

# if 'Color' in vehicle:
#     print('Klic tam je')
# else:
#     print('Klic tam neni')

# print(list(vehicle.keys()))
# print(list(vehicle.values()))
# print(len(vehicle))




