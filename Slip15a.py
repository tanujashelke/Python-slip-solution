class Student:
    def accept(self):
        self.name=(input("enter name of student"))
        self.marks=int(input("enter marks of student"))
    def display(self):
        print("Name of student:",self.name)
        print("Marks of student:",self.marks)
s=Student()
s.accept()
s.display()            