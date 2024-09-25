class Student:
    def GetStudent(self):
        self.RollNo=int(input("enter student roll number"))
        self.name=input("enter student name")
        self.age=int(input("enter student age"))
        self.gender=input("enter gender of student")
    def PutStudent(self):
        print("student roll no:", self.RollNo)  
        print("student name:",self.name)  
        print("student age:",self.age)
        print("student gender:",self.gender)
class Test(Student):
    def GetMarks(self):
        self.MarkMar=int(input("enter marks of marathi subject"))
        self.MarkHin=int(input("enter marks of hindi subject"))
        self.MarkEng=int(input("enter marks  of english"))
    def PutMarks(self):
        print("marathi marks:", self.MarkMar)    
        print("hindi marks:", self.MarkHin)
        print("english marks:", self.MarkEng)
n=int(input("enter how many students"))
lst=[]
for i in range(0,n):
        obj=input("enter object name")
        lst.append(obj)
print(lst)  

for i in range(0,n):
    lst[j]=Test()
    lst[j].GetStudent()
    lst[j].GetMarks()
    print("display details of student:",j+1)
    lst[j].PutStudent()
    lst[j].PutMarks()