def prime(num):
    flag=0
    for i in range(2,num):
        if num%i==0:
            flag =1
            break
        if flag==0:
            print("number is prime")
        else:
            print("number is not prime")
def fact(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
        
        print("factorial of given number is:",fact)
num=int(input("enter number :"))
prime(num)
fact(num)        
