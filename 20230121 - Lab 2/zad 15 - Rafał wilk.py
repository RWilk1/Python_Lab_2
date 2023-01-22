"""
Napisz skrypt który znajduje najczęściej występującą cyfrę w zbiorzę
"""

# Określanie najczęściej występującej wartości w podanym zbiorze danych
# Lista z częstościa występowania poszczególnych elementów
digits = [1, 2, 4, 6, 6, 2, 6, 6, 9]
Frequency = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print(digits)

for digit in digits:
    Frequency[digit] += 1

most_common = -1
for i in range(len(Frequency)):
    if Frequency[i] > most_common:
        most_common = i
    else:
        pass

print("Najczęściej występującą cyfrą jest: ", str(most_common), ",", "występuje", Frequency[most_common])



