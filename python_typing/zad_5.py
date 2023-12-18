# -*- coding: utf-8 -*-


sprawdzarka = (lambda lst, value: any(x == value for x in lst))


lista = input("Podaj listę liczb oddzielonych spacją: ")


try:
    listav2 = [int(x) for x in lista.split()]
    print("Wprowadzona lista liczb:", listav2)
except ValueError:
    print("Błąd: Wprowadź poprawne liczby oddzielone spacją.")
    exit()

liczba = int(input("Podaj wartość do sprawdzenia w liście: "))


wynik = sprawdzarka(listav2, liczba)
print(wynik)
