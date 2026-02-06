# obj=open("filehandling/students.txt","a")
# name=input("Enter your name: ")
# nep=int(input("Enter marks for nep: "))
# eng=int(input("Enter marks for eng: "))
# sci=int(input("Enter marks for sci: "))
# math=int(input("Enter marks for math: "))
# com=int(input("Enter marks for com: "))
# total=nep+eng+sci+math+com
# per=total/5
# obj.write(f"Name={name}\nNepali={nep}\tEnglish={eng}\tScience={sci}\tMath={math}\tComputer={com}\nTotal={total}\nPercentage={per}\n")
# obj.close()

# obj=open("filehandling/students.txt","r")
# name=input("Enter your name: ")
# email=input("Enter your email: ")
# address=input("Enter your address: ")
# obj.write(f"{name},{email},{address}")
# print(obj.read())
# print(obj.readline())
# print(obj.readlines())
# obj.close()

# *
def add_student():
    obj=open("filehandling/students.txt","a")
    name=input("Enter your name: ")
    nep=int(input("Enter marks for nep: "))
    eng=int(input("Enter marks for eng: "))
    sci=int(input("Enter marks for sci: "))
    math=int(input("Enter marks for math: "))
    com=int(input("Enter marks for com: "))
    total=nep+eng+sci+math+com
    per=total/5
    obj.write(f"Name={name}\nNepali={nep}\tEnglish={eng}\tScience={sci}\tMath={math}\tComputer={com}\nTotal={total}\nPercentage={per}\n")
    obj.close()
    return "New user added"

def check(file_name,search):
    file= open(file_name,"r")
    for line in file:
        if search in line:
            print("Welcome ",name)
            return True
    else:
        print(f"No existing user found in name {name}")
        new_user=input("Create new user? (yes/no):")
        if new_user == "no":
            return 
        else:
            print(add_student())


    
name=input("Enter your name: ")
check("filehandling/students.txt",name)

# regex
# tkinter module