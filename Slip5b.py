def Fibo(terms):
    f1, f2 = 0, 1  
    yield f1        
    yield f2        

    for _ in range(terms - 2):  
        f3 = f1 + f2
        yield f3   
        f1, f2 = f2, f3  


terms = int(input("How many terms: "))
gen = Fibo(terms)

while True:
    try:
        print(next(gen))  
    except StopIteration:
        break  
