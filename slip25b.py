class MathOp:
    def add(self):
        self.a=int(input("enter first number:"))
        self.b=int(input("enter second number:"))
        self.c=self.a+self.b
        print("addition is:",self.c)
    def sub(self):
        self.a=int(input("enter first number" ))
        self.b=int(input("enter second number"))
        self.c=self.a-self.b
        print("substraction is:",self.c)
    def mul(self):
        self.a=int(input("enter first number:"))
        self.b=int(input("enter second number:"))
        self.c=self.a*self.b
        print("multiplication is:",self.c)
    def div(self):
        self.a=int(input("enter first number:"))
        self.b=int(input("enter second number:"))
        self.c=self.a/self.b
        print("division is:",self.c)                   
m=MathOp()
while True:
    print("\n 1:addition")
    print("2:substraction")
    print("3:multiplication")
    print("4:division")
    print("5.exit")
    ch=int(input("enter your choice to perform operations:"))
    if ch==1:
        m.add()
    elif ch==2:
        m.sub()
    elif ch==3:
        m.mul()
    elif ch==4:
        m.div()
    elif ch==5:
        print("stop")
        break      
    else:
        print("wrong choice")                  