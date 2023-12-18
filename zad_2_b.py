# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 10:34:00 2023

@author: Admin
"""


lista = [1, 2, 3, 4, 20]

wynik = []
for liczba in lista:
        wynik.append(liczba * 2)

print(wynik)



lista = [1, 2, 3, 4, 5]
wynik = [liczba * 2 for liczba in lista]

print(wynik)