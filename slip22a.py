class StringRepeater:
    def __init__(self, s):
        self.s = s
    
    
    def __mul__(self, n):
        if isinstance(n, int):  
            return self.s * n
        else:
            raise ValueError("The multiplier must be an integer.")


input_string = input("Enter a string: ")
n = int(input("Enter the number of repetitions: "))

# Creating an instance of StringRepeater
string_repeater = StringRepeater(input_string)

# Using the overloaded * operator
result = string_repeater * n
print("Repeated string is:", result)
