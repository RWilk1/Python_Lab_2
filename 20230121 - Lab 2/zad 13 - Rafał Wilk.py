"""
Napisz skrypt, pobierający od użytkownika zbiór imion
- Liczba elementów
- pobierać kolejne elementy i dodawać je do listy
- wyświetlić w podsumownaiu jakie imiona pobrał od użytkownika
"""

Liczba_Elementow = int(input("Podaj liczbe imion: "))
imiona = []
i = 1

while i <= Liczba_Elementow:
    Imie = input("Podaj imie: ")
    imiona.append(Imie)
    i += 1

print("Podałeś następujące imiona: ", imiona)

