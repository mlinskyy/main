# -*- coding: utf-8 -*-

# Stworzenie anonimowej funkcji realizującej zadane operacje
sprawdzarka = (lambda list1, list2: list(map(lambda x: x**3, set(list1 + list2))))

# Wprowadzenie pierwszej listy liczb od użytkownika
lista_a = input("Podaj listę liczb oddzielonych spacją: ")
try:
    lista_1 = [int(x) for x in lista_a.split()]
    print("Wprowadzona lista liczb:", lista_1)
except ValueError:
    print("Błąd: Wprowadź poprawne liczby oddzielone spacją.")
    exit()

# Wprowadzenie drugiej listy liczb od użytkownika
lista_b = input("Podaj listę liczb oddzielonych spacją: ")
try:
    lista_2 = [int(x) for x in lista_b.split()]
    print("Wprowadzona lista liczb:", lista_2)
except ValueError:
    print("Błąd: Wprowadź poprawne liczby oddzielone spacją.")
    exit()

# Wywołanie funkcji i wyświetlenie wyniku
wynik = sprawdzarka(lista_1, lista_2)
print(wynik)
