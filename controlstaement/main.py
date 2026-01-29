# print("=======WELCOME TO ATM=======")
# pin=int(input("Enter 4 digit pin:"))
# if pin==1234:
#     print("1. Balance inquiry 2. Cash Withdrawal")
#     balance=10000
#     option=int(input("Choose an option (1 or 2)"))
#     if option==1:
#         print(f"Your current balance is {balance}")
#     elif option==2:
#         amount=int(input("Amount to withdraw:"))
#         balance-=amount
#         print("Please collect your cash")
#         print(f"Your current balance is {balance}")
#         print("Thank you ")
#     else:
#         print ("Invalid option")

# print("1. Dell (Rs.200,000) 2. HP (Rs.150,000) 3. MackBook (Rs250,000)")
# option=int(input("Choose option (1-3) for laptop "))
# if option==1 or option==2 or option==3:
#     quantity=int(input("Enter quantity for selected laptop to purchase:"))
#     dellstock=10
#     hpstock=8
#     macstock=4
#     if dellstock>=quantity or hpstock>=quantity or macstock>=quantity:
#       print("Please provide following information for order confirmation")
#       name=input("Name:")
#       address=input("Address:")
#       mobile=int(input("Mobile number:"))
#       if option==1:
#         total=200000*quantity
#       elif option==2:
#        total=150000*quantity
#       else:
#        total=quantity*250000
#       print(f"Your total is Rs.{total}")
#     else:
#        print("Insufficient stock")

# else:
#   print("Invalid option")


# x=50
# y=6
# z=7
# if x>y:
#     if x>z:
#      print("x")
#     else:
#      print("z")
# else:
#   if y>z:
#     print("y")
#   else:
#     print("z")


# x=91
# y=24
# z=3
# if x>y:
#     if x>z:
#         if y>z:
#             print(x,y,z)
#         else:
#             print(x,z,y)
#     else:
#         print(z,x,y)
# elif y>z:
#     if x>z:
#      print(y,x,z)
#     else:
#         print(y,z,x)
# else:
#     print(z,y,x)

# x=50
# y=6
# z=70

# if x>y:
#     if x>z:
#         if y>z:
#             print(x,y,z)
#         else:
#             print(x,z,y)
#     else:
#         print(z,x,y)
# else:
#     if y>z:
#         if x>z:
#             print(y,x,z)
#         else:
#             print(y,z,x)
#     else:
#         print(z,y,x)





# x=91
# y=24
# z=3

# if x<y:
#     if x<z:
#         if y<z:
#             print(x,y,z)
#         else:
#             print(x,z,y)
#     else:
#         print(z,x,y)
# elif y<z:
#     if x<z:
#      print(y,x,z)
#     else:
#         print(y,z,x)
# else:
#     print(z,y,x)

# print("1. Dell (Rs.200,000) 2. HP (Rs.150,000) 3. MackBook (Rs250,000)")
# option=int(input("Choose option (1-3) for laptop "))
# if option==1 or option==2 or option==3:
#     quantity=int(input("Enter quantity for selected laptop to purchase:"))
#     print("Please provide following information for order confirmation")
#     name=input("Name:")
#     address=input("Address:")
#     mobile=int(input("Mobile number:"))
#     if option==1:
#         total=200000*quantity
#     elif option==2:
#        total=150000*quantity
#     else:
#        total=quantity*250000
#     print(f"Your total is Rs.{total}")

# else:
#   print("Invalid option")

# data=['admin','admin002']
# username=input("Enter username: ")
# password=input("Enter password: ")
# if username==data[0] and password==data[1]:
#     print("Welcome ",username)
# else:
#     print("Username and password not match")

# data=[
#     {'username':'admin','password':'admin002'},
#     {'username':'sita','password':'sita002'},
#     {'username':'ram','password':'ram002'}
# ]
# username=input("Enter username: ")
# password=input("Enter password: ")

# if username==data[0]['username'] and password==data[0]['password']:
#     print("welcome",data[0]['username'])
# elif username==data[1]['username'] and password==data[1]['password']:
#     print("welcome",data[1]['username'])
# elif username==data[2]['username'] and password==data[2]['password']:
#     print("welcome",data[2]['username'])
# else:
#     print("Username and password not match")

# print("=====Welcome to bookstorre=====")
# username=input("Enter your username: ")
# password=input("Enter your password: ")
# if username=="admin" and password=="admin123":
#     books=['python','java','c++','javascript']
#     print("1. View Books 2.Add book 3.Delete: ")
#     option=int(input("Enter option from (1-3)"))
#     if option==1:
#         print(books)
#     elif option==2:
#         name=input("Enter the book to be added")
#         books.append(name)
#         print(books)
# else:
#     print("Invalid credentials. Access denied. ")


# print("=====Welcome to the party=====")
# age=int(input("Please enter your age: "))
# if age>=18 and age<=40:
#     print('Welcome to the party ')
#     drinks=['cola','wine','beer']
#     option=int(input("Would you like to view menu for the drinks: 1.Yes 2.No "))
#     if option==1:
#         print(drinks)
#         drink_option=int(input("Choose the option for your drink: "))
#         if drinks[2]:
#             if age >=30 and age<=40:
#                 print("here's your drink. Enjoy")
#             else:
#                 print("This drink is only available for age beyond 30.")
#         elif drinks[1]:
#             if age >=25 and age<=40:
#                 print("here's your drink. Enjoy")
#             else:
#                 print("This drink is only available for age beyond 25.")
#         else:
#             if age >=18:
#                 print("here's your drink. Enjoy")
#     else:
#         print("Please enjoy the party")
    
# elif age<18:
#     print("Underage. Accesss denied")
# else:
#     print("Too old. Access denied.")