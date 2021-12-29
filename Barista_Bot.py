input("Welcome to the Barista-Bot,\nPlease hit ENTER to continue:\n")
name = input("Let's start with your name:\n")

while name == "":
    name= input("Please type your name:\n")

choice = input("What would you like to have "+ name.capitalize() + " Tea or Coffee?\n")   #Choice is the variable
qty = int(input("How many cup of "+ choice.capitalize() + " Would you like to have " + name.capitalize()+ ":\n"))
if choice == "tea" or choice=="TEA" or choice=="Tea":                #total of tea
    total = 5*qty
elif choice == "coffee" or choice == "Coffee" or choice == "COFFEE":      #total of coffee
    total = 10*qty

if choice == "tea" or choice=="TEA" or choice=="Tea":
    print("Your order for Tea would cost you $" + str(total))
elif choice == "coffee" or choice == "Coffee" or choice == "COFFEE":
    print("Your order for Coffee would cost you $" + str(total))

#Add payment thing and timer for payment to process using for function