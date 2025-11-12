file = open("days.txt","r")
buffer = file.readlines()
file.close()
print(buffer)
msft = buffer[0].split(",")
msft.pop(0
amzn = buffer[1]
nvda = buffer[2]
print(msft)
