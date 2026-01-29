def getMin(userlist):
    min_value = userlist[0]
    index = 1
    while index < len(userlist):
        if userlist[index] < min_value:
            min_value = userlist[index]
        index = index + 1
first = [1,2,3,4]
print(first)
print(f"minimum of first list{getMin(first)}")
second = [4,2,1,3]
print(second)
print(f"minimum of second list{getMin(second)}")