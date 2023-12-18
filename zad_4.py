# -*- coding: utf-8 -*-

sprawdzarka = lambda a, b, c: (a + b) >= c

liczba1 = int(input("Podaj pierwszą liczbę całkowitą: "))
liczba2 = int(input("Podaj drugą liczbę całkowitą: "))
liczba3 = int(input("Podaj trzecią liczbę całkowitą: "))

wynik = sprawdzarka(liczba1, liczba2, liczba3)

print(wynik)

