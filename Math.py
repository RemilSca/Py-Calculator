
# Questions about variables 
Fn = int(input("First Number "))
Sn = int(input("Second Number "))
action = input("What action do you want to do? (+, -, *, /) ")

# Addition definition
def Addition():
    print(f"The answer is {Fn + Sn}")

# Difference definition
def Difference():
    print(f"The answer is {Fn - Sn}")

# Product definition
def Product():
    print(f"The answer is {Fn * Sn}")

# Quotient definition 
def Quotient():
    print(f"The answer is {Fn / Sn}")

# Answers
if action == "+":
    Addition() 
else:
    if action == "-":
            Difference()
    else:
        if action == "*":
            Product()
        else:
            if action == "/":
                Quotient()

input("Press 'Enter' to exit ")
