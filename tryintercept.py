check = False
print("Welcome to the calculator")
while check == False:
    try:
        option = input("What operation do you want to do? (Type quit to exit): ").strip().lower()
        
        if option == "addition":
            x = input("What is x?").strip()
            x = int(x)
            y = input("What is y?").strip()
            y = int(y)
            sum = x + y
            print(f"the sum of {x} and {y} is {sum}")
        elif option == "subtraction":
            x = input("What is x?").strip()
            x = int(x)
            y = input("What is y?").strip()
            y = int(y)
            difference = x - y
            print(f"the difference of {x} and {y} is {difference}")
        elif option == "multiplication":
            x = input("What is x?").strip()
            x = int(x)
            y = input("What is y?").strip()
            y = int(y)
            product = x * y
            print(f"the product of {x} and {y} is {product}")
        elif option == "division":
            x = input("What is x?").strip()
            x = int(x)
            y = input("What is y?").strip()
            y = int(y)
            try:
                quotiant = x / y
                print(f"the quotiant of {x} and {y} is {quotiant}")
            except ZeroDivisionError:
                print("Error: cannot divide by zero")
    except ValueError:
            print("that is not a numerical value")
    if option == quit:
                check = True
                print("Thanks for using the calc")