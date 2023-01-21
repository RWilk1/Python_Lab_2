
# 1. napisz skrypt sprawdzający, czy pierwiastek kwadratowy z liczby całkowitej
# pobranej od użytkownika jest także liczbą całkowitą

# Podaj Liczbę całkowitą
Liczba_Calk = int(input("Podaj liczbe calkowitą: "))
Liczba_Calk_Pierw = Liczba_Calk ** 0.5

if  (Liczba_Calk_Pierw % 1) == 0:
    print(f"Pierwiastek kwadratowy {Liczba_Calk_Pierw} z liczby {Liczba_Calk} \n jest liczba całkowitą")
else:
    print(f"Pierwiastek kwadratowy {Liczba_Calk_Pierw} z liczby {Liczba_Calk} \n NIE jest liczba całkowitą")
