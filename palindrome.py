reverse = ""
pal = input("What is your word").strip().lower()
for char in pal:
    reverse = char + reverse
if reverse == pal:
    print("it is a palindrome")
else:
    print("It is not a palindrome")