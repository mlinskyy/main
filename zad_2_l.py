# -*- coding: utf-8 -*-

class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library in {self.city}, {self.street}, {self.zip_code} | Open hours: {self.open_hours} | Phone: {self.phone}"


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name} | Hire date: {self.hire_date} | Birth date: {self.birth_date} | Location: {self.city}, {self.street}, {self.zip_code} | Phone: {self.phone}"


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book: {self.author_name} {self.author_surname} | Published: {self.publication_date} | Pages: {self.number_of_pages} | Location: {self.library}"


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_list = "\n\t".join(str(book) for book in self.books)
        return f"Order by {self.employee.first_name} {self.employee.last_name} for {self.student.first_name} {self.student.last_name} | Order date: {self.order_date}\nBooks:\n\t{book_list}"


# Tworzenie bibliotek, książek, pracowników, studentów, i zamówień
library1 = Library("City1", "Street1", "ZIP1", "9:00 AM - 5:00 PM", "123-456-789")
library2 = Library("City2", "Street2", "ZIP2", "10:00 AM - 6:00 PM", "987-654-321")

employee1 = Employee("John", "Doe", "2022-01-01", "1990-01-01", "City1", "Street1", "ZIP1", "555-111-222")
employee2 = Employee("Jane", "Smith", "2022-02-01", "1992-02-01", "City2", "Street2", "ZIP2", "555-333-444")
employee3 = Employee("Bob", "Johnson", "2022-03-01", "1995-03-01", "City1", "Street1", "ZIP1", "555-555-666")

book1 = Book(library1, "2022-01-01", "Author1", "Surname1", 200)
book2 = Book(library1, "2022-02-01", "Author2", "Surname2", 250)
book3 = Book(library2, "2022-03-01", "Author3", "Surname3", 300)
book4 = Book(library2, "2022-04-01", "Author4", "Surname4", 350)
book5 = Book(library2, "2022-05-01", "Author5", "Surname5", 400)

student1 = Employee("Alice", "Johnson", "2021-01-01", "2000-01-01", "City1", "Street1", "ZIP1", "777-888-999")
student2 = Employee("Bob", "Williams", "2021-02-01", "2002-02-01", "City2", "Street2", "ZIP2", "777-111-222")
student3 = Employee("Charlie", "Davis", "2021-03-01", "2005-03-01", "City1", "Street1", "ZIP1", "777-333-444")

order1 = Order(employee1, student1, [book1, book2], "2022-06-01")
order2 = Order(employee2, student2, [book3, book4, book5], "2022-06-02")

# Wyświetlanie zamówień
print(order1)
print("\n" + "="*50 + "\n")
print(order2)