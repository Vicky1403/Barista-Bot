input("Welcome to the Barista-Bot,\nPlease hit ENTER to continue:\n")
name = input("Let's start with your name:\n")

while name == "":
    name= input("Please type your name:\n")

choice = input("What would you like to have "+ name.capitalize() + " Tea or Coffee?\n")   #Choice is the variable
while choice == "":
    choice= input("Please enter a valid input, Tea or Coffee:\n")
qty = int(input("How many cup of "+ choice.capitalize() + " Would you like to have " + name.capitalize()+ ":\n"))


if choice == "tea" or choice=="TEA" or choice=="Tea":                #total of tea
    total = 5*qty
elif choice == "coffee" or choice == "Coffee" or choice == "COFFEE":      #total of coffee
    total = 10*qty

if choice == "tea" or choice=="TEA" or choice=="Tea":
    print("Your order for Tea would cost you $" + str(total) + ",")
elif choice == "coffee" or choice == "Coffee" or choice == "COFFEE":
    print("Your order for Coffee would cost you $" + str(total)+ ",")

#bank info

bankinfo = int(input("For now we only accept payment through banks,\nEnter your 5-digit account no: [Ex: 12345]\n"))
while len(str(bankinfo))!=5:
    bankinfo = int(input("Enter a valid 5 digit account no: [Ex: 12345]\n"))
import time
while len(str(bankinfo))==5:
    pin = int(input("Enter your 4-digit pin: [Ex: 12345]\n"))
    break
while len(str(pin))!=4:
    pin= int(input("Enter a valid 4 digit pin: [Ex: 12345]\n"))
while len(str(pin))==4:
    for pcs in "Processin":
        print(pcs, end="")
    for seconds in "g...":
        print(seconds, end="")
        time.sleep(1)
    for success in "\nPayment Succesfull":
        print(success, end="")
    break

input("\nHere is you, "+ choice + ". Have a Nice Day!")



#Add payment thing and timer for payment to process using for function