print("Welcome to NBA2K My Career")
print("You will be able to choose your own career path and make your own chocies")
name = input("What is your name")
option = input(f"Hey {name} where would you like to start your career? College or NBA?")
if option == "College":
    option = input("You can pick between Duke, Alabama, or Maryland")
    if option == "Duke":
        position = input("What position are you going to play? Options: PG, SG, SF, PF, C.")
        print(f"Welcome {position} {name} to the University of Duke")