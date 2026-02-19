import sqlite3

conn=sqlite3.connect("database/student.sqlite3")

myCur=conn.cursor()

# def create_table():

#     myCur.execute("""
#         CREATE TABLE IF NOT EXISTS course(
#                       id INTEGER PRIMARY KEY AUTOINCREMENT,
#                       name TEXT NOT NULL,
#                       teacher TEXT NOT NULL,
#                       phone INTEGER NOT NULL
                    
#                   )

                  
                  
#     """)

#     conn.commit()
#     print("Table created")

# create_table()

# def insert_data(name,email,phone,department):
#     myCur.execute(f"""
#             INSERT INTO teacher(name,email,phone,department)
#             VALUES ('{name}','{email}','{phone}','{department}')""")
#     conn.commit()
#     print("Data entered successfully")

# name=input("Enter name: ")
# email=input("Enter email: ")
# phone=input("Enter phone number: ")
# department=input("Enter department: ")
# insert_data(name,email,phone,department)

# def show():
#     data=myCur.execute("SELECT * FROM course WHERE name='am'")
#     data=data.fetchall()
#     print(data)
# show()