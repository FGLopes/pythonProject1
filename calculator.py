var_x = int(input("enter the first number: "))
var_y = int(input("enter the second number: "))
operation = input("Choose math operation (+, -, *, /): ")

if operation == "+":
    print(var_x + var_y)

elif operation == "-":
    print(var_x - var_y)

elif operation == "*":
    print(var_x * var_y)

elif operation == "/":
    print(var_x / var_y)

else:
    print("Please insert a valid math operation.")
