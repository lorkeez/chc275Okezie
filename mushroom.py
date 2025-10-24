sizes = []
large = []
medium = []
small = []
check = False
while check == False:
    print("1. add sizes")
    print("2. catogorize mushrooms by sizes")
    option = input("What option would you like")
    if option == "1":
        size = input("What sizes are mushrooms?")
        if size.isnumeric():
            size = int(size)
            sizes.append(size)
        else:
            print("that is not a numeric size")
    elif option == 2:
        for i in range(len(sizes)):
            if sizes[i] < 100:
                small.append(sizes[i])
            if sizes[i] >= 200:
                medium.append(sizes[i])
            if sizes[i] >= 200:
                large.append(size[i])
        check = True
print(small)
print(medium)
print(large)