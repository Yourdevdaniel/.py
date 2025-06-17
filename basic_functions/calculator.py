
def calculator():
    while True:
        print("Welcome to an basic calculator")

        nu1 = input("Enter the first number: ")
        nu2 = input("Enter the second number: ")
        print("we have the following operators  +, -, *, /, %")
        operator = input("Enter the operator: ")

        #Numbers verify

        valid_number = None
        N1 = 0
        N2 = 0

        try:
            N1 = float(nu1)
            N2 = float(nu2)
            valid_number = True
        except ValueError:
            valid_number = None

        if valid_number is None:
            print("Please enter an valid number")
            continue

        if operator == "+":
            result = N1 + N2
        elif operator == "-":
            result = N1 - N2
        elif operator == "*":
            result = N1 * N2
        elif operator == "/":
            if N2 == 0:
                print("can't divide by zero(0)")
                continue
            else:
                result = N1 / N2
        elif operator == "%":
            if N2 == 0:
                print("can't divide by zero(0)")
                continue
            else:
                result = N1 % N2
        else:
            print("Please enter an valid operator")
        
        print("let's see the result")
        print(f"{N1} {operator} {N2} the result is {result}")
            
        leave = input("You want to leave the software? [y]es: ").lower().startswith('y')
    
        if leave:
            break

calculator()