class Date:
    def accept(self):
        self.day=int(input("enter day"))
        self.month=int(input("enter month"))
        self.year=int(input("enter year"))
    def display(self):
        try:
            if self.day>31:    
                raise ValueError("day value is greater than 31")
            if self.month>12:
                raise ValueError("month value is greater than 12")
            print("date is",self.day,self.month,self.year )
        except ValueError as e:
            print(e)
d=Date()
d.accept()
d.display()                