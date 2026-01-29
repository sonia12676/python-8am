# lang='nep'
# match lang:
#     case 'nep':
#         print("Nepali")
#     case 'eng':
#         print("English")
#     case _:
#         print("Language not found")

# x=int(input("Enter value for x: "))
# y=int(input("Enter value for y: "))
# operator=input("Enter an operator (+,-,*,/): ")
# match operator:
#     case '+':
#         print(x+y)
#     case '-':
#         print(x-y)
#     case '*':
#         print(x*y)
#     case '/':
#         print(x/y)
#     case _:
#         print("not found")

# x=10
# while x>=1:
#     print (x)
#     x-=1

# num=int(input("Enter any number: "))
# x=1
# while x<=10:
#     print(f"{num}X{x}={num*x}")
#     x+=1

# x=1
# y=0
# while x<=10:
#     y+=x 
#     x+=1
# print(y)  

# users=['ram','hari','gita','sita','laxmi']
# only print ram gita laxmi



# users=[
#     {"name":'admin', 'password':'admin002'},
#     {"name":'ram', 'password':'ram002'},
#     {"name":'gita', 'password':'gita002'},
    
# ]
# username=input("Enter username: ")
# password=input("Enter password: ")
# is_login=False

# for user in users:  
    
#     if user['name']==username and user['password']==password:
#         print("Welcome")
#         is_login=True
    
# if not is_login:
#     print("Username and password not matched")


# users=[
#     {"name":'admin', 'password':'admin002'},
#     {"name":'ram', 'password':'ram002'},
#     {"name":'gita', 'password':'gita002'},
    
# ]
# for user in users:  
#     print(user)

# users=[
#     {"name":'admin', 'password':'admin002'},
#     {"name":'ram', 'password':'ram002'},
#     {"name":'gita', 'password':'gita002'},
    
# ]
# username=input("Enter username: ")
# password=input("Enter password: ")
# abc=False
# for user in users:
#     if user['name']==username and user['password']==password:
#         print('Welcome')
#         abc=True
#     if abc==False:        
#         print('Access denied.')


# for (if abc==False) -> if (not abc) is True so, if false: muniko code run hune or 

# Create a sample collection
# users = [{'name':'Hans','status': 'active'},
#           {'name':'Éléonore','status':'inactive'},
#           {'name':'Ram','status': 'active'}
# ]

# # Strategy:  Iterate over a copy
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]

# # Strategy:  Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status

# Create a sample collection
# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
# print(users.items())

# # Strategy:  Iterate over a copy
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]
# print(users)

# # Strategy:  Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status
# print(active_users)

# x=10
# while x>=1:
#     print(x,end=" ")
#     x-=1

# data=['ram','hari','sita']
# for name in data:
#     print(type(name))

# users=['ram','hari','gita','sita','laxmi']
# only print ram gita laxmi
# for user in users:
#     if user=='ram' or user=='gita' or user=='laxmi':
#         print(user,end=" ")


# sentence=we are learning python programming
# only print vowel letters
# sentence="we are learning python programming"
# for vowel_check in sentence:
#     if vowel_check in 'aeiou':
#         print(vowel_check)

# *
# categories=[
#     {'cid':1,'name': 'laptop'},
#     {'cid':2,'name': 'mobile'},
#     {'cid':3,'name': 'tv'},
#     {'cid':4,'name': 'books'},
# ]

# products=[
#     {'id':1,'cid':1,'name': 'dell'},
#     {'id':2,'cid':1,'name': 'mac'},
#     {'id':3,'cid':1,'name': 'hp'},
#     {'id':4,'cid':2,'name': 'samsung'},
#     {'id':5,'cid':2,'name': 'apple'},
#     {'id':6,'cid':3,'name': 'sony'},
#     {'id':7,'cid':3,'name': 'lg'},
# ]

# is_found=False
# for category in categories:
#     print(f"Category: {category['name']}")
#     for p in products:
#         if category['cid'] == p['cid']:
#             print(f"\t \t Product: {p['name']}")
#             is_found=True
# else:
#     print(f"No {category['name']} found")
#     is_found=False

# *
# products=[
#     {'id':1,'name': 'dell','quantity':10,'price':5000},
#     {'id':2,'name': 'mac','quantity':5,'price':2000},
#     {'id':3,'name': 'hp','quantity':8,'price':1000},
#     {'id':4,'name': 'samsung','quantity':15,'price':3000},
#     {'id':5,'name': 'apple','quantity':7,'price':4000},
#     {'id':6,'name': 'sony','quantity':12,'price':500},
#     {'id':7,'name': 'lg','quantity':9,'price':100},
# ]
# total price
# for product in products:
#      print(product)
#      total_price=product['quantity']*product['price']
#      print(f"\t Total price:Rs.{total_price}")
# *
# num=int(input("Enter number of students: "))
# x=1
# student_marks=[]
# while x<=num:
#     print(f"=====Roll no.:{x}=====")
#     nep=int(input('Enter marks for nep: '))
#     eng=int(input('Enter marks for eng: '))
#     sci=int(input('Enter marks for sci: '))
#     mat=int(input('Enter marks for mat: '))
#     com=int(input('Enter marks for com: '))
#     total=nep+eng+sci+mat+com
#     student_marks.append(total)
#     x+=1
# for total in student_marks:
#     per=total/5
#     grade=""
#     if per>35 and per<60:
#         grade="C"
#     elif per>60 and per<80:
#         grade="B"
#     elif per>80 and per<=100:
#         grade="A"
#     else:
#         grade="None"
    
#     print(f"Total: {total} percentage: {per}")
# **
students=[
    {'name':'ram','marks':[34,55,76,88,45]},
    {'name':'sita','marks':[34,65,45,88,45]},
    {'name':'hari','marks':[34,55,55,92,45]},
    {'name':'gita','marks':[34,40,38,88,67]},
]

for student in students:
    total_marks=0
    for mark in student['marks']:
        total_marks=total_marks+mark
    # print(total_marks)
    per=total_marks/5
    if per>35 and per<60:
        grade="C"
    elif per>60 and per<80:
        grade="B"
    elif per>80 and per<=100:
        grade="A"
    else:
        grade="None"

    print(f"\t \t{student['name']}'s Report card")
    print(f"Marks on individual subject: {student['marks']}")
    print(f"Total marks: {total_marks} \t Percentage: {per} \t Grade:{grade}")
    print("*******************************************************")
    
        