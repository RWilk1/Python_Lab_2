
"""
Załóżmy, że na pierwsze pole szachownicy kładiemy 1 ziarno zboża,
a na drugie 2 ziarna, na trzecie 4 ziarna i na każde następne pole dwa razy więcej ziaren niż na pole poprzednie.
Napis program, który zasymulje taką sytujację i zliczy sumę wszystkich ziaren na szachownicy
szachownica ma 64 pola

"""
suma_ziaren = 0

for i in range(64):
    suma_ziaren += 2 ** i

print("Liczba uzyskanych ziaren to: ", suma_ziaren, "czyli: ", round(suma_ziaren / 1000000000, 0), "miliarda")
# 1 ziarno - 0,4 mg
# 1 ziarno - 0,0004 g
# 1kg = 1000g
# 1t = 1000kg
tons = int(suma_ziaren * 0.0004 / 1000 / 1000)
print("Daje to: ", tons, "ton")
# To jest szacunkowa ilosc rocznej produkcji przenicy na swiecie: 782_000_000 ton zapis naukowy 782e6 (782 * 1000 * 1000 * 1000 * 1000 * 1000 * 1000)
year = int(tons / 782_000_000)
print("To jest ekwiwalent: ", year, "rocznych produkcji przenicy na świecie")