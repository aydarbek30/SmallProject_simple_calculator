#Simple calculator

import math

a = float(input("Enter the 1st number: "))
b = float(input("Enter the 2nd number: "))
c = input("Enter an operator (+ - * / ^ sqrt): ")

if c == "+":
    print(round(a+b, 3))
elif c == "-":
    print(round(a-b, 3))
elif c == "*":
    print(round(a*b, 3))
elif c == "/":
    print(round(a/b, 3))
elif c == "^":
    print(pow(a, 2))
elif c == "sqrt":
    print(math.sqrt(a))
else:
    print(f"{c} is not a valid operator")

