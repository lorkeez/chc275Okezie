#Bank system that can deposit, transfer, withdraw, add or remove accounts and view balances
accounts = ["James","Jack","John","Paul"]#List of accounts
balances = [102,90,70,150]#List of balances
check = False
while check == False:#Make sure the program runs til true
     x = input("would you like to open the menu")#Will ask this until something other than else
     if x == ("yes"):
          print("1. deposit")
          print("2. withdraw")
          print("3. view accounts and balances")
          print("4. transfer money")
          print("5. add account")
          print("6. remove account")
          #print all the functions fr the system
          x = input("What number action woudl you like to do")
          if x == ("3"):
               #takes accoint name and links to balance then prints balance
               accountname4 = input("What is you account name")
               index = accounts.index(accountname4)
               print(balances[index])
          elif x == ("5"):
               #creates a new account and a blance for the account
               accountname = input("What is your account name")
               accounts.append(accountname)
               balances.append(0)
               index = accounts.index(accountname)
               print("your account has been added")
          elif x == ("6"):
               #removes account from balance and list
               accountname2 = input("What is your account name")
               index = accounts.index(accountname2)
               accounts.pop(index)
               balances.pop(index)
               print("your account and balance has been removed")
          elif x == ("1"):
               #adds money to account by linking balances
               accountname3 = input("What is your account name")
               index = accounts.index(accountname3)
               x = input("how much would you like to add")
               x = int(x)
               balances[index] = balances[index] + x
               print(f"your new balance is {balances[index]}")
          elif x == ("2"):
               #subracts money from the account balance
               accountname5 = input("What is your account name")
               index = accounts.index(accountname5)
               x = input("how much would you like to withdraw")
               x = int(x)
               balances[index] = balances[index] -x
               print(f"your new balance is {balances[index]}")
          elif x == ("4"):
               #takes in both accounts, subtracts value of money from the transferring account
               accountname6 = input("What is your account name")
               index = accounts.index(accountname6)
               accountname7 = input("What is the transfer account name")
               i = accounts.index(accountname7)
               transfer = input("how much would you like to transfer")
               transfer = int(transfer)
               balances [i] = balances [i] + transfer
               balances[index] = balances[index] - transfer
               print(f"{accountname7}'s balance is {balances[i]}")
               print(f"your account balance is {balances[index]}")
     else:
          check = True#stops program from looping
          print("Thanks for using FFCU")