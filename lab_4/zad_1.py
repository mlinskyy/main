

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def zdane(self):
        average_marks = sum(self.marks) / len(self.marks) if len(self.marks) > 0 else 0
        return average_marks > 50


student1 = Student("Damian Mliński", [60, 70, 80])
student2 = Student("Piotr Skowyrski", [40, 30, 20])


wynik1 = student1.zdane()
wynik2 = student2.zdane()


print(f"Czy {student1.name} zdał? {wynik1}")
print(f"Czy {student2.name} zdał? {wynik2}")