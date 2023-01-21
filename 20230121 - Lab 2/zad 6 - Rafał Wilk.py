
# napisz gre z zgadywanie liczby z przedzialu od 1 do 10
# gracz powinien miec 3 szanse
# po po nieudanej probie gracz powinien otrzymac podpowiedz o parzystosci zgadywanej liczby
import random as rn

Liczba = rn.randint(1, 10)
Liczba_Modulo = (Liczba % 2)
Ilosc_Prob = 1
print(Liczba)

while Ilosc_Prob <= 3:
    Podaj_Liczbe = int(input("Podaj liczbe z zakresu od 1 do 10: "))
    if (Podaj_Liczbe != Liczba) and (Ilosc_Prob < 3):
        print("Pudlo prubuj dalej")
        if (Podaj_Liczbe != Liczba) and (Ilosc_Prob > 1):
            if Liczba_Modulo == 0:
                print("Podpowiedz: Wylosowana liczba jest parzysta")
            else:
                print("Podpowiedz: Wylosowana liczba NIE jest parzysta")
        if (Podaj_Liczbe != Liczba) and (Ilosc_Prob == 2):
            print("UWAGA: czeka cię 3 i ostatnia próba")
        else:
            pass    # Czyli nic nie rób
        Ilosc_Prob = Ilosc_Prob + 1
    elif (Podaj_Liczbe == Liczba) and (Ilosc_Prob <= 3):
        print("Gratulacje zgadłeś")
        break
    else:
        print("niezgadłeś i zmarnowałeś wszystkie próby - przegrałeś życie")
        break

