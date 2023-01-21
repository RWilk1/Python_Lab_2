
i = 2
while i < 10:
    print(i, end=" ")
    i += 1

for i in range(0, 10):
    print(i, end=" ")

for i in range(2, 10, 3):
    print(i, end=" ")

# Zmniejszanie o -1
for i in range(9, -10, -2):
    print(i)

# Obliczanie silni
# 3! = 1 * 2 * 3 = 6
number = 5  # 1 * 2 * 3 * 4 * 5
factorial = 1

for i in range(1, number + 1):
    factorial *= i
    print(factorial)

i = 1
while number == True:
    factorial *= number
    number -= 1

for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print("Koniec pętli...")





