"""
2. Napisz skrypt wyświetlający na ekranie macierz.
Rozmiar oraz znka z jakiej będzie zbudowana powinien określić użytkwonik
"""

Znak = str(input("Podaj znak: "))
Rozmiar_Macierzy = int(input("Podaj rozmiar macierzy: "))
i = 1

while i <= Rozmiar_Macierzy:
    print(Znak * Rozmiar_Macierzy)
    i = i + 1