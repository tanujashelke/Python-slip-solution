class Employee:
    def acceptEmp(self):
        self.id=int(input("enter employee id"))
        self.name=input("enter employee name")
        self.department=input("enter employee department")
        self.salary=int(input("enter salary"))
    def displayEmp(self):
        print("employee id:",self.id)
        print("employee name",self.name)
        print("employee department",self.department)
        print("employee salary:",self.salary)   
class Manager(Employee):
    def acceptManager(self):
        self.bonus=int(input("enter  manager bonus"))
    def displayManager(self):
        print("bonus is:",self.salary+self.bonus);

m=Manager()
m.acceptEmp()
m.displayEmp()
m.acceptManager()
m.displayManager()
