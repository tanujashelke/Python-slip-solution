dict={"mon":3,"tue":5,"wed":6,"thu":9}
print("the given dictionary is:",dict)
check_key=input("enter key to check")
check_value=input("enter value to check")
if check_key in dict:
    print(check_key,"isPresent")
    dict.pop(check_key)
    dict[check_key]=check_value
else:
    print(check_key,"is not present")
dict[check_key]=check_value
print("updated dictionary:",dict)