def string_test(s):
    d={"upper":0,"lower":0}
    for c in s:
            if c.isupper():
                d["upper"]+=1
            elif c.islower():
                d["lower"]+=1
            else:
                pass
    print("original string",s)
    print("no of uppercase characters:",d["upper"])  
    print("no of lowercase characters:",d["lower"])  
string_test("the Quick Brown Box")            