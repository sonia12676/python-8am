# print("========WELCOME TO LAPTOP BAZAR========")
# print("1. Dell (Rs.20000) 2. Hp(Rs.30000) 3.Apple (Rs.50000)")
# dell_price=0
# hp_price=0
# apple_price=0
# product_name=""
# quantity=0

# option=(int(input("Enter the option number you want to buy: ")))
# if option==1:
#     quantity=(int(input("Enter the quantity you want to buy: ")))
#     dell_price=quantity*20000
#     product_name="Dell"
# elif option==2:
#     quantity=(int(input("Enter the quantity you want to buy: ")))
#     hp_price=quantity*30000
#     product_name="HP"
# elif option==3:
#     quantity=(int(input("Enter the quantity you want to buy: ")))
#     apple_price=quantity*50000
#     product_name="apple"
# else:
#     print("Invalid option")

# total=dell_price+hp_price+apple_price
# print("Choose option for delivery 1.Home (Rs.1000) 2. Home pickup(Rs.0)")
# del_price=0
# del_option=int(input("Enter the delivery option number: "))
# if del_option==1:
#     del_price=1000
# elif del_option==2:
#     del_price=0
# else:
#     print("Invalid option")

# packing_price=0
# print("Packing:  1.Plastic (Rs 100) 2.Gift wrap (Rs 500) 3.None")
# pack_option=int(input("Enter the option for packaging:"))
# if option==1:
#     packing_price=100
# elif option==2:
#     packing_price=500
# elif option==3:
#     packing_price=0
# else:
#     print("Invalid option")

# tax_amount=0
# print("Location  1.KTM (13%) 2.LTP (0)")
# loc_option=int(input("Enter your locaion option number: "))
# if loc_option==1:
#     tax_amount=total*0.13

# grand_total=tax_amount+packing_price+total
# print("=======INVOICE=======")
# print("Product name:",product_name)
# print("Quantity",quantity)
# print("Total price:Rs.",total)
# print("Delivery price:Rs.",del_price)
# print("Packing price:Rs.",packing_price)
# print("Tax amount:Rs.",tax_amount)
# print("Grand total:Rs.",grand_total)



print("=====WELCOME TO BOOKSHOP=====")
print("Please log in to purchase any book")
quantity=0
op_price=0
java_price=0
python_price=0
c_price=0
book_name=""
admin=input("Enter your username: ")
password=input("Enter your password: ")
if admin=="admin" and password=="pwd123":
    print("Welcome to the book shop ",admin)
    print("1. Operating System (Rs.500)2.Java (Rs.100) 3.Python (Rs.200) 4.C++ (Rs.300)")
    book_option=int(input("Choose the option to puchase the book:"))
    if book_option==1:
        quantity=int(input("Enter the quantity you want to purchase: "))
        op_price=quantity*500
        book_name="Operating System"
    elif book_option==2:
        quantity=int(input("Enter the quantity you want to purchase: "))
        java_price=quantity*100
        book_name="Java"
    elif book_option==3:
        quantity=int(input("Enter the quantity you want to purchase: "))
        pyhton_price=quantity*200
        book_name="Python"
    elif book_option==4:
        quantity=int(input("Enter the quantity you want to purchase: "))
        c_price=quantity*300
        book_name="C++"
    else:
        print("invalid option")

    total=op_price+java_price+python_price+c_price

    print("Choose option for delivery 1.Home (Rs.1000) 2. Home pickup(Rs.0)")
    del_price=0
    del_option=int(input("Enter the delivery option number: "))
    if del_option==1:
        del_price=1000
    elif del_option==2:
        del_price=0
    else:
        print("Invalid option")

    packing_price=0
    print("Packing:  1.Plastic (Rs 100) 2.Gift wrap (Rs 500) 3.None")
    pack_option=int(input("Enter the option for packaging:"))
    if pack_option==1:
        packing_price=100
    elif pack_option==2:
        packing_price=500
    elif pack_option==3:
        packing_price=0
    else:
        print("Invalid option")
    grand_total=packing_price+total+del_price
    print("=======INVOICE=======")
    print("Book name:",book_name)
    print("Quantity",quantity)
    print("Total price:Rs.",total)
    print("Delivery price:Rs.",del_price)
    print("Packing price:Rs.",packing_price)
    print("Grand total:Rs.",grand_total)
    
else:
    print("Your username or passsword is incorrect")
