
import random

counter = 1
number = random.randint(1, 10)
print(number)
guess = int(input("zgadnij jaką liczbę mam na mysli (1-10); "))

while number != guess:
    guess = int(input("Nie, to nie tak. Spróbuj jeszcze raz: "))
    counter += 1

print("Brawo! Udało Ci się za ", str(counter), " razem.")

