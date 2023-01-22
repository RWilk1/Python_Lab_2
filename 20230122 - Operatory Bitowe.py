a = 5
b = 3

######################################################
# Konunkcja bitowa: "&"
print(a, "&", b, "=", a & b)

# Wynik 1 bo:
print(bin(a))
print(bin(b))

# Pokazywanie powyższego na 8 bitach
print("{:08b}".format(a))
print("{:08b}".format(b))
print("{:08b}".format(a & b))
# bo: 1*1 = 1; 0*1=0; 1*0=0

######################################################
# Alternatywa bitowa: "|"
print("\n", "ALTERNATYWA BITOWA", end="", sep="")
print(a, "|", b, "=", a | b)

# Wynik 7 bo:
print(bin(a))
print(bin(b))

# Pokazywanie powyższego na 8 bitach
print("{:08b}".format(a))
print("{:08b}".format(b))
print("{:08b}".format(a & b))
# bo: 1+1 = 1; 0+1=1; 1+0=1

######################################################
# xor
print("{:08b}".format(a ^ b))

######################################################
# przesunięcie bitowe w prawo: ">>"
print("\n", "PRZESUNIĘCIE BITOWE W PRAWO", end="", sep="")
print(a, ">>", b, "=", a >> 2)

# Wynik 0 bo:
print(bin(a))
print(bin(b))

# Pokazywanie powyższego na 8 bitach
print("{:08b}".format(a))
print("{:08b}".format(b))
print("{:08b}".format(a >> b))
# bo: 1+1 = 1; 0+1=1; 1+0=1


######################################################
# przesunięcie bitowe w lewo: "<<"
print("\n", "PRZESUNIĘCIE BITOWE W LEWO", end="", sep="")
# przesuniecie o 2 miejsca
print(a, ">>", b, "=", a << 2)

# Wynik 20 bo:
print(bin(a))
print(bin(b))

# Pokazywanie powyższego na 8 bitach
print("{:08b}".format(a))
print("{:08b}".format(b))
print("{:08b}".format(a << b))


######################################################
# Negacja bitowa: "~"
print("\n", "NEGACJA BITOWA", end="", sep="")
# przesuniecie o 2 miejsca
print(a, "=", ~a)

# Wynik -1 bo:
print(bin(a))

# Pokazywanie powyższego na 8 bitach
print("{:08b}".format(a))
print("{:08b}".format(~a))

# Przykład
for i in range(5, -5, -1):
    print("{0:08b} => {1:d}".format(i & 255, i))

######################################################
