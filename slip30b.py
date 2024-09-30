class Country:
    def acceptCountry(self):
        self.name=input("enter name  of country:")
    def displayCountry(self):
        print("country:",self.name)
class State(Country):
    def acceptState(self):
        self.sname=input("enter name of state:") 
    def displayState(self):
        print("state name is:",self.sname)              
s=State()
s.acceptState()
s.displayState()
s=Country()
s.acceptCountry()
s.displayCountry()        