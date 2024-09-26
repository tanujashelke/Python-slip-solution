class myClass:
    def getString(self):
       self.str=input("enter string")
    def printString(self):
        s=self.str
        print("String in uppercase:",s.upper())
        cnt=len(s)
        i=cnt-1
        RevStr=""
        while(i>=0):
            RevStr=RevStr+s[i]
            i=i-1
        print("String in lowercase:",RevStr.lower())    

m=myClass()
m.getString()
m.printString()        
    
