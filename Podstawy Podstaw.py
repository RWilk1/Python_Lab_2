"""
first_name = "Rafal"
# age = input("Ile masz lat?")
age = 32

# print(f'Hello {first_name}')
print(f'Mam \n {age} lata')
print(f'Czesc \n \t Rafał masz {age} lat')
# print("Float: ", float(3))
print("/:", 9 / 2)
print("//:", 9 // 2)    # Zostaje tylko liczba całkowita
print("%:", 9 % 2)      # Zostaje "reszta z dzielenia"
print("**:", 3 ** 2)    # podniesienie do potęgi 2
"""

# >
# >=
# <
# <=
# ==
# !=
# in
# not 2 == 3
# not in

# Pierwiastek kwadratowy
print(9 ** 0.5)

# Liczby ujemne
print(2 + (-2))


# Zmiana znaków liczb
print(abs(-4))
print(-abs(4))


"""
'\t' - tab
'\n' - new line
print("/:", '\t', 9 / 2)
print(f'Czesc \n \t Rafał masz {age} lat')
"""

"""
# instrukcje sterujace kodem
# if
if first_name == "Rafal":
    print('Hello ', first_name)
else:
    print('Nie wiadomo kim jesteś')
# For range
seqRange = range(1, 5)
print(type(seqRange))
print(list(reversed(seqRange)))

x = 1
print(type(x))

string = 'Hello'
print(string.upper())
"""

# Łańcuchowanie metod
napis = "test1 test2"
print(napis.upper().replace("2", "!"))


# Listy
# Indeksowanie list rozpoczyna się od 0
thislist = ["apple", "banana", "cherry"]
print(thislist)
print(thislist[1])
thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist2[2:5])
print(thislist2[:2])
print(thislist2[-1])

# Sprawdzanie, czy element istnieje na liscie
if "apple" in thislist2:
    print("Yes")
else:
    print("No")

if "apple" not in thislist2:
    print("Yes")
else:
    print("No")

###############################################
# Tworzenie funkcji
def my_function6(x):
  return 5 * x

print(my_function6(3))

###############################################
# Zmiana wartosci na listach
thislist3 = ["apple", "banana", "cherry"]
print(thislist3[-2:])
print(thislist3[:-2])
print(thislist3[1])
print(thislist3[1:3])
thislist3[1] = "blackcurrant"
print(thislist3)

# Zmiana > 1 wartości na raz
thislist4 = ["apple", "banana", "cherry"]
thislist4[0:2] = ["blackcurrant", "watermelon"]
print(thislist4)
# Wstawianie nowych elementów po 2 elemencie
thislist4.insert(2, "plam")
print(thislist4)
# Dodawanie nowego elementu na samym końcu
thislist4.append("Bluebarry")
print(thislist4)
# Łączenie list ze sobą
tropical = ["mango", "pineapple"]
thislist4.extend(tropical)
print(thislist4)
# Lub
thislist4 = thislist4 + tropical
print(thislist4)
# Usuwanie elementów z listy
thislist4.remove('pineapple')
print(thislist4)
# Usuwanie elementów z listy za pomocą indeksu
thislist4.pop(0)
print(thislist4)
# Sortowanie list
thislist4.sort(reverse  = True)
thislist4.reverse()
print("Sort:", thislist4)
# Kopiowanie zmiennych zamiast tworzenia referencji
# W przypadku referencji zmiana wartości w zmiennej zrodlowej spowoduje zmiane w zmiennej docelowej
thislist5 = thislist4.copy()
print(thislist5)

##############################################
# Listy złożone
Blank4 = [
    [1, "a"],
    [2, "b"],
    [3, "c"]
]
print(type(Blank4))
print(Blank4)
print(Blank4[1])
print(Blank4[1][1])
# Zmiana elementu listy złożonej
Blank4[1][1] = "z"
print(Blank4)
##############################################
# Listy słownikowe
cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
print(cars)


###############################################
# Pętla przez sekwencje
first_ten = range(1, 10, 2)

for i in first_ten:
    print(i)

###############################################
# tuples
Male_Friends = ("Joey", "Ross", "Chandler")
print(type(Male_Friends))
print(Male_Friends)
print(Male_Friends[0])

###############################################
# Listy
Female_Friends = ["Monica", "Phoebe", "Rachel"]
print(type(Female_Friends))
print(Female_Friends)
print(Male_Friends[0])
Female_Friends[0] = "Monica2"
print(Female_Friends)
# Generalnie listy są zmienne a Tuple są niezmienne tak więc dużo lepiej używać list

# Sortowanie list
cats_1 = ["Annie", "Neo", "Salem", "Sabrina", "Mary", "Agatha"]
print(sorted(cats_1, reverse=False))

# Dodawanie elementów do list-y
Blank = []
Blank.insert(0, "a")
Blank.insert(1, "b")
Blank.append("c")   # append to jest to samo co insert tylko że bez podawania indeksu
print(Blank)
Blank2 = ["d", "e"]
# Łączenie list, najprostrzy sposób
print(Blank + Blank2)
# Wyodrębnianie określonego elementu z listy
print(Blank.pop(-1))

# Kopiowanie List, inaczej byłoby to tylko odzwierciedlenie zmiennej: Blank
Blank3 = Blank.copy()
Blank.append("z")
print(Blank)
print(Blank3)

# for i in cats_2:
#     print(i)

###############################################
# Ranges()
Even_Numbers = range(2, 12, 2)
print(type(Even_Numbers))
print(Even_Numbers[0])

for i in Even_Numbers:
    print(i)

# Strings(), ciągi znaków, które są niezmienne
Wise_Owl = "Wise Owl"
print(type(Wise_Owl))
print(Wise_Owl[1])

for i in Wise_Owl:
    print(i)

# Tworzenie listy ze stringa
Wise_Owl2 = Wise_Owl.split(sep=" ")
print(type(Wise_Owl2))
print(Wise_Owl2)


###########################################################
import sys
paths = sys.path

for p in paths:
    print("\n")
    print(p)
    last_bit = p.rpartition("\\")
    print(last_bit)
    print(last_bit[-1])

cats = "Annie,Neo,Salem,Sabrina,Marv,Agatha"
cat_list = cats.split(",")
print(cat_list)

for cat_number, cat_name in enumerate(cat_list):
    print("Cat number {0} is {1}".format(cat_number+1, cat_name))



# Funkcja Enumarate
l1 = ["eat", "sleep", "repeat"]

# printing the tuples in object directly
for ele in enumerate(l1):
    print(ele)


###########################################################
# Obsługa wyjątków / błędów

print(1/0)

try:
    print(1/0)
except:
    print("Error")
print("dalej")

# Obsługa tylko jednego rodzaju błędu: ZeroDivisionError
try:
    print(1/0)
except ZeroDivisionError:
    print("Error: ZeroDivisionError")
except:
    print("Different Error")

# Obsługa więcej > 1 błędu
try:
    print(1/0)
except(ZeroDivisionError, IOError):
    print("albo to, albo to")

# Gdy żaden wyjątek nie wystąpił
try:
    print(1/0)
except ZeroDivisionError:
    print("Error: ZeroDivisionError")
else:
    print("No Errors")

# Celowe wywołąnie błędu w celach testowych
# Zwracanie info o błędzie
try:
    raise TypeError(ZeroDivisionError)
except Exception as e:
    print(e)

"""
https://docs.python.org/3.10/library/functions.html
https://python.plainenglish.io/python-a-quick-revision-ebbccb28612a
https://www.youtube.com/watch?v=38Nh9CWpNYw&list=PLNIs-AWhQzckGrdnwITFlXGqiXTCAhWWi&index=10&ab_channel=WiseOwlTutorials
"""





