import math
def getList():
    userList = []
    print("Enter numbers for your list.")
    print("Type 'done' when finished.")

    while True:
        val = input("Enter a number (or done): ")
        if val.lower() == "done":
            break
        try:
            userList.append(float(val))
        except ValueError:
            print("Invalid input. Try again.")

    return userList
def printMenu():
    print("\nStatistics Calculator Menu")
    print("1. Get Minimum")
    print("2. Get Maximum")
    print("3. Get Mean")
    print("4. Get Median")
    print("5. Get Standard Deviation")
    print("6. Enter New List")
    print("0. Quit")

def getMean(userList):
    if len(userList) == 0:
        return 0
    return sum(userList) / len(userList)

def getMedian(userList):
    n = len(userList)
    if n == 0:
        return 0

    s = sorted(userList)

    if n % 2 == 1:
        return s[n // 2]
    else:
        return (s[n//2 - 1] + s[n//2]) / 2

def getMin(userList):
    if not userList:
        return 0
    
    m = userList[0]
    for x in userList:
        if x < m:
            m = x
    return m

def getMax(userList):
    if not userList:
        return 0
    
    m = userList[0]
    for x in userList:
        if x > m:
            m = x
    return m

def getStdDev(userList):
    n = len(userList)
    if n == 0:
        return 0

    mean = getMean(userList)

    SSE = 0
    for x in userList:
        SSE += (x - mean) ** 2

    SSE = SSE / n
    return math.sqrt(SSE)


def main():
    userList = getList()

    while True:
        printMenu()
        choice = input("Choose an option: ")

        if choice == "1":
            print("Min:", getMin(userList))

        elif choice == "2":
            print("Max:", getMax(userList))

        elif choice == "3":
            print("Mean:", getMean(userList))

        elif choice == "4":
            print("Median:", getMedian(userList))

        elif choice == "5":
            print("Std Dev:", getStdDev(userList))

        elif choice == "6":
            userList = getList()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
