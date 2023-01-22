"""
1. Wyświetl liczby od 1 do 100 z pominięciem liczb podzielnych przez 3
Liczba jest podzielna przez 3, jeśli suma jej cyfr jest liczbą podzielną przez 3
"""

suma_cyfr = 0

for i in range(1, 101):
    # print(i)
    suma_cyfr = 0
    for j in str(i):
        # print(j)
        suma_cyfr += int(j)
        # print(suma_cyfr)
    if (suma_cyfr % 3) != 0:
        print(i)
    else:
        pass    # Liczba jest podzielna przez 3 więc nic nie rób

