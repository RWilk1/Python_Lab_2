# Wyświetl tylko liczby podzielne przez 3, 5 lub 7
# ze zbioru określonego przez użytkownika
_Min = int(input("Wskaż dolną granice zbioru: "))
_Max = int(input("Wskaż górną granicę zbioru: "))
_Zbior = list(range(_Min, _Max))

for i in _Zbior:
    if (i % 3) == 0 or (i % 5) == 0 or (i % 7) == 0:
        print(i)
    else:
        pass    # nic nie rób

