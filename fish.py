option = input("Enter fish type")
if option == "Carnivorous":
    option = input("Do you already have this fish")
    if option == "yes":
        print("too bad")
    elif option == "no":
        print("enjoy")
elif option == "Salt Water":
    print("Your a fancy fish parent")
elif option == "Community":
    print("You should get more than one")
else:
    print("I dont think thats a fish")