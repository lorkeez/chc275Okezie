x = input("What is the number?")
x = int(x)
check = False
while check == False:
    print(x)
    if x == 1:
        check = True
    if x % 2 == 1:
        x = 3*x + 1
    if x % 2 == 0:
        x = x/2