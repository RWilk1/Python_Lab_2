# Napisz program wyznaczający wartosc n-tego bitu dla dowolnej liczby calkowitej
# Bity liczymy od 0, od najmniej znaczacego bitu
# Najmniej znaczący bit to ten od prawej strony

Liczba = int(input("Podaj liczbę: "))
Pozycja_Bitu = int(input("Podaj pozycje bitu: "))

print(Pozycja_Bitu)
print(bin(Liczba))
print("{:08b}".format(Liczba))

# Wynik
print("{:08b}".format(Liczba)[-Pozycja_Bitu])



