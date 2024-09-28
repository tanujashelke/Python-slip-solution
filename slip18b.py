class Person:
    def accept(self):
        self.name=input("entre name")
        self.address=input("enter address")
    def display(self):
        print("name  of person:",self.name)
        print("address of person:",self.address)
class Employee(Person):
    def acceptEmp(self):
        self.salary=int(input("enter salary"))
    def  displayEmp(self):
        print("employee salary:",self.salary)
        n=int(input("enter how many employees"))
e=Employee()
e.accept()
e.display()
e.acceptEmp()
e.displayEmp()

                