# -*- coding: utf-8 -*-

class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property - Area: {self.area} sqm | Rooms: {self.rooms} | Price: {self.price} | Address: {self.address}"


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House - {super().__str__()} | Plot Size: {self.plot} sqm"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat - {super().__str__()} | Floor: {self.floor}"


# Tworzenie obiektów klasy House i Flat
house1 = House(150, 5, 300000, "123 Main St", 500)
flat1 = Flat(80, 3, 150000, "456 Oak St", 2)

# Wyświetlanie obiektów
print(house1)
print("\n" + "="*50 + "\n")
print(flat1)
