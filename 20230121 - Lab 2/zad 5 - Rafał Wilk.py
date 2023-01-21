
# napisz skrypt wyznaczajacy ocene jaka orzyma student
# ze wzgledu na liczbe otrzymanych punktow z kolokwium

Liczba_Punktow = int(input("Wpisz liczbe punktow: "))

if Liczba_Punktow <= 50:
    print("Liczba punktów <= 50 ocena: 2.0")
elif Liczba_Punktow > 50 and Liczba_Punktow <= 60:
    print("Liczba punktów > 50 ale <= 60 ocena: 3.0")
elif Liczba_Punktow > 60 and Liczba_Punktow <= 70:
    print("Liczba punktów > 60 ale <= 70 ocena: 3.5")
elif Liczba_Punktow > 70 and Liczba_Punktow <= 84:
    print("Liczba punktów > 70 ale <= 84 ocena: 4.0")
elif Liczba_Punktow > 84 and Liczba_Punktow < 95:
    print("Liczba punktów > 84 ale < 95 ocena: 4.5")
else:
    print("Liczba punktów >= 95 ocena: 5.0")