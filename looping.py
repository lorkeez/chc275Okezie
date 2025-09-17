x = 1
while x <= 10: 
    print (x)
    x = x + 1
nums = [1,2,3,4,5,6,7,8,9,10]
x = 0
sum = 0
while x < len(nums):
        sum+= nums [x]
        x +=1
print(f"The sum is {sum}")
check = False
while check == False:
    print("Option 1")
    print("Option 2")
    print("Option 3")
    option = input("Select your option or type quit to exit")
    if option == "1":
        print(1)
    elif option == "2":
        print(2)
    elif option == "3":
        print(3)
    elif option == "quit":
        check = True