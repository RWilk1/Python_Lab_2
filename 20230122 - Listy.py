
# Lista to uporządkowana kolekcja elementów
# Listy []
# Do elementów listy odwołujemy się zawsze za pomocą indeksów: 0:N
# Listy mogą przechowywać dane o różnych typach, a dane mogą się powtarzać

fruits = ["Banan", "jabłko", "Kiwi"]
print(fruits[1])
print(fruits[-1])
print(type(fruits))
# Liczba elementów listy
print(len(fruits))
# dodawanie elementów do listy

# Metody listy
# Metody to specjalne funkcje, które są przyporządkowane do danego rodzajów obiektów
# Funkcje w przeciwieństwie do metod można używać na różnych klasach obiektów to są funkcje "uniwersalne"
cars = ['Ford', 'BMW', 'Volvo']
print(cars.sort())  # metoda nie działa
print(sorted(cars))
print(sorted(cars, reverse=True))

numbers = [0, 2, 2, 4, 6, 8, 9, 10, "b", True]
print(numbers)
print(numbers[0:4])
print(numbers[-3:-1])
# Usuwanie elementów z listy
del numbers[-1] # Instrukcja del,
print(numbers)
# Dodawanie elementów do listy
numbers.insert(0, -1)
print(numbers)

###########################################################################
# Example: Half Dollars
denver = [1_700_000, 4_600_000, 2_100_000]
philad = []
philad.append(1_800_000)
philad.append(5_000_000)
philad.append(2_500_000)
# suma
total = [0, 0, 0]
total[0] = denver[0] + philad[0]
total[1] = denver[1] + philad[1]
total[2] = denver[2] + philad[2]
# Średnia
Average = (total[0] + total[1] + total[2]) / len(total)
print("Produkcja monent w 2012 wyniosła: ", "{:,d}".format(total[0]).replace(",", " "), 'sztuk')
print("Produkcja monent w 2013 wyniosła: ", "{:,d}".format(total[1]).replace(",", " "), 'sztuk')
print("Produkcja monent w 2014 wyniosła: ", "{:,d}".format(total[2]).replace(",", " "), 'sztuk')


###########################################################################
# Iterowanie po listach
fruits2 = ["Banan", "jabłko", "Kiwi"]
print(type(fruits2))

for i in range(len(fruits2)):
     print(i)
     print(fruits2[i])





