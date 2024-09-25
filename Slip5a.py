class myClass:
    def getString(self):
        self.str=input("enter string")
    def printString(self):
        s=self.str
        print("string in uppercase:",s.upper())
c=myClass()
c.getString()
c.printString()            