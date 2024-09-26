class MyClass:
    def getString(self):
        self.str=input("enter string")
    def printString(self):
        s=self.str 
        print(s)
        cnt=len(s)
        i=cnt-1
        RevStr=""
        while(i>=0):
            RevStr=RevStr+s[i]
            i=i-1
        print("reverse string:",RevStr) 
m=MyClass()
m.getString()
m.printString()           