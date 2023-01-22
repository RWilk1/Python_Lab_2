# Program do szyfrowania operacje na bitach
# Napisac program ktory rozszyfruje ponizsza wiadomosc:
# Xq|`gf(bm{|(nibfq)
# Sposob zakodowania, dla kazdego znaku zmieniono 4 bit na przeciwny
# 4 bit, a bity liczymy od najmniej znaczacego, 4 bit -> indeks 3

# Xq|`gf(bm{|(nibfq)
# wartość liczbowa znaku: c
print(ord("c")) # znak: c ma wartosc 99
# ta liczba zapisana jest zapisana bitowo
print(bin(ord("c")))
# operacja odwrotna, wywołanie znaku za pomocą jego wartosc
print(chr(99))
# zapis bitowy
print("{:08b}".format(ord("c")))    # 01100011

# Wykonywanie operacji tylko na poszczególnych bitach
# 01100011 - nasza liczba
# 00001000 - maska
# 01101011 - używamy XOR (alternatywa rozłączna), operator XOR pozwala zamiane bit-ów wskazanych za pomocą maski

# Generowanie maski dla każdego znaku, przesumięcie bitowe
# przesuniecie bitowe
print("{:08b}".format(ord("c") ^ (1 << 3)))

msg = "Xq|`gf(bm{|(nibfq)"
for c in msg:
    # print(c)
    print(chr(ord(c) ^ (1 << 3)), end="")

