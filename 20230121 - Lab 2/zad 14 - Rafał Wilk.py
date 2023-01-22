"""
Napisz program, który zasymuluje 16 rzutów kostką a następie wyświetli informacje
- zestaw wylosowanych wyników
- wyrzucaną wartość za 8-smym razem
- liczbe wyrzuconych 6-stek
- maksymalną liczbę wyrzuconych tych samych wartości pod rząd
"""
import random as rn

Wyniki_Rzutow = []
# i = 1
Liczba_Szostek = 0
Wartosc_8raz = 0
Najczestszy_Wynik = []

for i in range(1, 17):
    # print("Iteracja nr.: ", i)
    Rzut = rn.randint(1, 6)
    print("Aktualny wynik: ", Rzut)
    Wyniki_Rzutow.append(Rzut)
    print("Poprzednik wynik: ", Wyniki_Rzutow[i-1], "\n")
    if Rzut == 6:
        Liczba_Szostek += 1
    else:
        pass
    if i == 8:
        Wartosc_8raz = Rzut
    else:
        pass

# Maksymalna liczba tych samych wartosci wyrzucona pod rzad
in_row_Value_tmp = Wyniki_Rzutow
in_row_total_tmp = 0
in_row_value = 0

for roll in Wyniki_Rzutow:
    if roll == in_row_Value_tmp:
        in_row_total_tmp += 1
    else:
        in_row_value_tmp = roll
        in_row_total_tmp = 1
    if in_row_total_tmp > in_row_value:
        in_row_total = in_row_total_tmp
        in_row_value = in_row_value_tmp
    else:
        pass

# Wyniki
print("Zbiór 16 rzutów to: ", Wyniki_Rzutow)
print("Liczba wyrzuceń 6: ", Liczba_Szostek)
print("Za 8 rzutem wypadło: ", Wartosc_8raz)
print("Pod rząd wyrzucono: ", in_row_total, "razy wartość: ", str(in_row_total_tmp))


