def makeList():
    nums = []
    x = input("1")
    while x != "stop":
        nums.append(int(x))
        x = input("stop)")
    return nums
list = makeList
print(list)