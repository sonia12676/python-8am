#  WAP to enter any number and check whether the number is even or odd.
# num=int(input("Enter any number to check odd or even "))
# res=num%2
# if res==0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")

# WAP to enter five subject marks and calculate total percentage and grade
#  40-60 > b
#  60-80 >a
#  80-100 >a+
#  fail <40
# sub1=int(input("Enter marks for English "))
# sub2=int(input("Enter marks for Science "))
# sub3=int(input("Enter marks for Math "))
# sub4=int(input("Enter marks for Social "))
# sub5=int(input("Enter marks for Computer "))
# total=sub1+sub2+sub3+sub4+sub5
# per=total*100/500
# print(f"Total marks obtained is {total} and percentage is {per}")
# if per>=80:
#     print("Grade=A+")
# elif per>=60 and per<80:
#     print("Grade=A")
# elif per>=40 and per<60:
#     print("Grade=B")
# else:
#     print("Grade=F")

# enter the username and passowrd
# check the username and password
# username='admin'
# password='admin002'

# username='admin'
# password='admin002'
# username1=input("Enter username:")
# password1=input("Enter password:")
# if username==username1 and password==password1:
#     print("Welcome")
# elif username==username1 or password==password1:
#     print("Username or Password is incorrect")
# else:
#     print("Username and Password is incorrect")

# if-else

# print("Welcome to Nepal Yatayat")
# fare=15
# des=""
# des_option=int(input("Please select your destination: 1.New buspark 2.Chabahil 3. Tinkune 4.Sadobato 5.Balkhu 6.Kalanki:"))
# if des_option==1:
#     des="New buspark"
#     total_fare=fare
# elif des_option==2:
#     des="Chabahil"
#     total_fare=fare*2
# elif des_option==3:
#     des="Tinkune"
#     total_fare=fare*3
# elif des_option==4:
#     des="Sadobato"
#     total_fare=fare*4
# elif des_option==5:
#     des="Balkhu"
#     total_fare=fare*5
# elif des_option==6:
#     des="Kalanki"
#     total_fare=fare*6
# else:
#     print("Invalid option")

# print("=====Invoice=====")
# print("Your destination:",des)
# print("Total fare:Rs.",total_fare)

# *
# 100min
# ntc to ntc= 2.5
# ntc to ncell=3.5
# ncell to ntc=4
# ncell to ncell=5
# 1-10

# call_cost=0
# call_duration=int(input("Provide duration for your call in minutes: "))
# if call_duration>0 and call_duration<=100:
#     print("Please choose the required service providers for the call:")
#     option=int(input("1.NTC to NTC 2.NTC to Ncell 3.Ncell to NTC 4.Ncell to Ncell: "))
#     if option==1:
#         if call_duration<=10:
#             call_cost=2.5
#         elif call_duration>10 and call_duration<=20:
#             call_cost=2.5*2
#         elif call_duration>20 and call_duration<=30:
#             call_cost=2.5*3
#         elif call_duration>30 and call_duration<=40:
#             call_cost=2.5*4
#         elif call_duration>40 and call_duration<=50:
#             call_cost=2.5*5
#         elif call_duration>50 and call_duration<=60:
#             call_cost=2.5*6
#         elif call_duration>60 and call_duration<=70:
#             call_cost=2.5*7
#         elif call_duration>70 and call_duration<=80:
#             call_cost=2.5*8
#         elif call_duration>80 and call_duration<=90:
#             call_cost=2.5*9
#         else:
#             call_cost=2.5*10
#         print(f" Your total for NTC to NTC call for {call_duration} minutes is Rs.{call_cost}")
    
#     elif option==2:
#         if call_duration<=10:
#             call_cost=3.5
#         elif call_duration>10 and call_duration<=20:
#             call_cost=3.5*2
#         elif call_duration>20 and call_duration<=30:
#             call_cost=3.5*3
#         elif call_duration>30 and call_duration<=40:
#             call_cost=3.5*4
#         elif call_duration>40 and call_duration<=50:
#             call_cost=3.5*5
#         elif call_duration>50 and call_duration<=60:
#             call_cost=3.5*6
#         elif call_duration>60 and call_duration<=70:
#             call_cost=3.5*7
#         elif call_duration>70 and call_duration<=80:
#             call_cost=3.5*8
#         elif call_duration>80 and call_duration<=90:
#             call_cost=3.5*9
#         else:
#             call_cost=3.5*10
#         print(f" Your total for NTC to Ncell call for {call_duration} minutes is Rs.{call_cost}")

#     elif option==3:
#         if call_duration<=10:
#             call_cost=4
#         elif call_duration>10 and call_duration<=20:
#             call_cost=4*2
#         elif call_duration>20 and call_duration<=30:
#             call_cost=4*3
#         elif call_duration>30 and call_duration<=40:
#             call_cost=4*4
#         elif call_duration>40 and call_duration<=50:
#             call_cost=4*5
#         elif call_duration>50 and call_duration<=60:
#             call_cost=4*6
#         elif call_duration>60 and call_duration<=70:
#             call_cost=4*7
#         elif call_duration>70 and call_duration<=80:
#             call_cost=4*8
#         elif call_duration>80 and call_duration<=90:
#             call_cost=4*9
#         else:
#             call_cost=4*10
#         print(f" Your total for Ncell to NTC call for {call_duration} minutes is Rs.{call_cost}")

#     else:
#         if call_duration<=10:
#             call_cost=5
#         elif call_duration>10 and call_duration<=20:
#             call_cost=5*2
#         elif call_duration>20 and call_duration<=30:
#             call_cost=5*3
#         elif call_duration>30 and call_duration<=40:
#             call_cost=5*4
#         elif call_duration>40 and call_duration<=50:
#             call_cost=5*5
#         elif call_duration>50 and call_duration<=60:
#             call_cost=5*6
#         elif call_duration>60 and call_duration<=70:
#             call_cost=5*7
#         elif call_duration>70 and call_duration<=80:
#             call_cost=5*8
#         elif call_duration>80 and call_duration<=90:
#             call_cost=5*9
#         else:
#             call_cost=5*10
#         print(f" Your total for Ncell to Ncell call for {call_duration} minutes is Rs.{call_cost}")
        
# else:
#     print("Calls less than 0 minutes and longer than 100 minutes is not supported. Thank you.")

# *
# total users, total active users, total inactive users, total active male, total active female ,total inactive male, total inactive female
# search name
# students=[
#     {'name':'ram','gender':'male','status':True},
#     {'name':'hari','gender':'male','status':False},
#     {'name':'sita','gender':'female','status':True},
#     {'name':'rita','gender':'female','status':True},
#     {'name':'laxmi','gender':'female','status':False}
# ]
# total_users=0
# total_active_users=0
# total_inactive_users=0
# total_active_male=0
# total_active_female=0
# total_inactive_male=0
# total_inactive_female=0

# for user in students:
#     total_users+=1
#     if user['status'] is True:
#         total_active_users+=1
#         if user['gender']=='male':
#            total_active_male+=1
#         else:
#             total_active_female+=1 
#     else:
#         total_inactive_users+=1
#         if user['gender']=='male':
#            total_inactive_male+=1
#         else:
#             total_inactive_female+=1 
# print(f"Total users:{total_users}, Total active users:{total_active_users}, Total active male users:{total_active_male}, Total active female users:{total_active_female}")
# print(f"Total inactive users:{total_inactive_users}, Total inactive male users:{total_inactive_male}, Total inactive female users:{total_inactive_female}, ")  

# *question same as above
# is_found=False
# name_=input("Enter the name of the student you want to search: ")
# for user in students:
#     if name_ in user['name']:
#         print(f"{name_} found in directory")
#         is_found=True
# if not is_found:
#     print("Given student's name not found.")