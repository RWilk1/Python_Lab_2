# Udowodnij, że w zborze liczb z zakresu 1-100 jest 11 liczb, które są parzyste
# i jednocześnie większe od 90, a gdy są nieparzyste, to przynajmniej dzielą się przez 9

Suma_Liczb = 0

for i in range(1, 101):
    if i > 90 and (i % 2) == 0:
        print(i)
        Suma_Liczb = Suma_Liczb + 1
    elif (i % 2) != 0 and (i % 9) == 0:
        print(i)
        Suma_Liczb = Suma_Liczb + 1
    else:
        pass    # W przeciwnym przypadku nic

print("Liczba liczb spełniających warunki to: ", Suma_Liczb)
