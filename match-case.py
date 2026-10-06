print("----------------- MENU -------------------")
print("1.Biryani\n2.Chicken 65\n3.Veg Pulao\n4.Butter Chicken\n5.Panner Tikka")
choice=int(input("Enter Your Choice : "))
match choice:
    case 1:
        print("Item    :  Biryani ")
        print("Price    :  ₹250 ")
    case 2:
        print("Item    :  Chicken 65 ")
        print("Price    :  ₹200 ")
    case 3:
        print("Item    :  Veg Pulao ")
        print("Price    :  ₹150 ")
    case 4:
        print("Item    :  Butter Chicken ")
        print("Price    :  ₹220 ")
    case 5:
        print("Item    :  Panner Tikka ")
        print("Price    :  ₹200 ")



# print("---------- ATM MENU -----------")
# print("1.Check Balance\n2.Deposit\n3.Withdrawl\n4.Exit")
# initial_balance=10000
# choose=int(input("Enter Your Choice : "))
# match choose:
#     case 1:
#         print("Current Balance : ",initial_balance)
#     case 2:
#         deposit = int(input("Enter deposit Amount : ")) 
#         print("Amount Deposited and Added to Account Successfully")
#         print("Total Balance : ",initial_balance+deposit)
#     case 3:
#         withdraw=int(input("Enter withdrawl Amount : "))
#         print("Withdrawl Successful")
#         print("Avalible Balance : ",initial_balance-withdraw)
#     case 4:
#         print("Exit")        