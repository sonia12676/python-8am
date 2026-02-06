
# def total(numbers):
#     total_sum=0
#     for a in numbers:
#         total_sum+=a
#     print(total_sum)

# total([1,3,5,6])

# *
# def add(a,b):
#     return a+b
# def total(x,y,callback):
#     print(callback(x,y))

# total(6,7,add)

# *
# total=lambda x,y:x+y
# print(total(8,8))

# def marks():
#     sub1=int(input("Enter marks for subject1: "))
#     sub2=int(input("Enter marks for subject2: "))
#     sub3=int(input("Enter marks for subject3: "))
#     sub4=int(input("Enter marks for subject4: "))
#     sub5=int(input("Enter marks for subject5: "))
#     return [sub1,sub2,sub3,sub4,sub5]
# def total():
#     sub1,sub2,sub3,sub4,sub5=marks()
#     return sub1+sub2+sub3+sub4+sub5
# def percentage():
#     a=total()
#     p=a/5
#     return [a,p]
# def division():
#     per=percentage()
#     y=per[1]
#     grade=""
    
#     if y<40:
#         grade="F"
#     elif y>40 and y<50:
#         grade="C"
#     elif y>50 and y<65:
#         grade="B"
#     elif y>65 and y<80:
#         grade="A"
#     else:
#         grade="A+"
#     a=per[0]
#     return [a,y,grade]

# def result():
#     res=division()
#     print("total marks:",res[0])
#     print("Percentage:",res[1])
#     print("Grade:",res[2])
#     # tot=total()
#     # print(tot)

# result()

#*
# def fact(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n*fact(n-1)

# print(fact(5))
# *
# def add(x,y):
#     print(x+y)
# add(9,0)
# *
# def add(x,y):
#     return x+y
# def total():
#     return add(6,7)
# print(total())
# *
# def add(a,b):
#     return a+b
# def total(callback):
#     return callback(6,7)
# print(total(add))
# *
# tot=lambda x,y: x+y
# print(tot(4,5))
# *
# def login():
#     username=input("Enter your username: ")
#     password=input("Enter your password: ")
#     if username=="admin" and password=="admin123":
#         print("welcome",username)
#     else:
#         option=input("Do you want to try again? yes/p: ")
#         if option=='yes':
#             login()
#         else:
#             pass


# print(login())
# *
# def login():
#     return "admin"

# name=input("Enter your name: ")

# if name==login():
#     print("welcome admin")
# else:
#     print("Access denied")
# *
people=["ram","shyam","hari","ram"]
def search_name(name_):
    for name in people:
        if name==name_:
            print(name)


search_name("ram")
