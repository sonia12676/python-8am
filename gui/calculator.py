import tkinter as tk
from tkinter import ttk

num1=num2=operator=None

def get_digit(digit):
    result=enterlbl['text']
    new=result+str(digit)
    enterlbl.config(text=new)

def clear():
    enterlbl.config(text='')

def get_operator(op):
    global num1,operator
    num1=int(enterlbl['text'])
    operator=op
    clear()

def process():
    global num1, num2, operator
    num2=int(enterlbl['text'])
    if operator=='+':
        enterlbl.config(text=str(num1+num2))
    elif operator=='-':
        enterlbl.config(text=str(num1-num2))
    elif operator=='x':
        enterlbl.config(text=str(num1*num2))
    else:
        if num2==0:
            enterlbl.config(text="Error")
        else:
            enterlbl.config(text=str(num1/num2))

app=tk.Tk()
app.title("Calculator")
app.geometry("370x430")
app.resizable(0,0)




# def make_row(container):
    # frame=ttk.Frame(container)
enterlbl=ttk.Label(app,text='')
enterlbl.grid(column=0,row=0,sticky=tk.E,padx=(5,5),pady=5,ipadx=5,ipady=50,columnspan=5)
enterlbl.config(font=('Arial',20,'bold'))
    # return frame
# def numbers(container):
    # def take_input():
    #     print("click")
    # frame=ttk.Frame(container)

    # row0
ttk.Button(app,text='C',command=lambda:clear()).grid(row=1,column=0,ipady=15,ipadx=10)
ttk.Button(app,text='').grid(row=1,column=1,ipady=15,ipadx=10)
ttk.Button(app,text='').grid(row=1,column=2,ipady=15,ipadx=10)
ttk.Button(app,text='/',command=lambda:get_operator('/')).grid(row=1,column=3,ipady=15)



    # row1
ttk.Button(app,text='7',command=lambda:get_digit(7)).grid(row=2,column=0,ipady=15,ipadx=10)
ttk.Button(app,text='8',command=lambda:get_digit(8)).grid(row=2,column=1,ipady=15,ipadx=10)
ttk.Button(app,text='9',command=lambda:get_digit(9)).grid(row=2,column=2,ipady=15,ipadx=10)
ttk.Button(app,text='X',command=lambda:get_operator('x')).grid(row=2,column=3,ipady=15)

    # row2
ttk.Button(app,text='4',command=lambda:get_digit(4)).grid(row=3,column=0,ipady=15,ipadx=10)
ttk.Button(app,text='5',command=lambda:get_digit(5)).grid(row=3,column=1,ipady=15,ipadx=10)
ttk.Button(app,text='6',command=lambda:get_digit(6)).grid(row=3,column=2,ipady=15,ipadx=10)
ttk.Button(app,text='+',command=lambda:get_operator('+')).grid(row=3,column=3,ipady=15)
    
    # row3
ttk.Button(app,text='1',command=lambda:get_digit(1)).grid(row=4,column=0,ipady=15,ipadx=10)
ttk.Button(app,text='2',command=lambda:get_digit(2)).grid(row=4,column=1,ipady=15,ipadx=10)
ttk.Button(app,text='3',command=lambda:get_digit(3)).grid(row=4,column=2,ipady=15,ipadx=10)
ttk.Button(app,text='__',command=lambda:get_operator('-')).grid(row=4,column=3,ipady=15)

    # row4
ttk.Button(app,text='').grid(row=5,column=0,ipady=15,ipadx=10)
ttk.Button(app,text='0',command=lambda:get_digit(0)).grid(row=5,column=1,ipady=15,ipadx=10)
ttk.Button(app,text='.').grid(row=5,column=2,ipady=15,ipadx=10)
ttk.Button(app,text='=',command=process).grid(row=5,column=3,ipady=15)
    
    
    # return frame

# def create_main_window():
#     app=tk.Tk()
#     app.title("Calculator")
#     app.geometry("370x400")
#     app.resizable(0,0)
    
#     input_frame=make_row(app)
#     input_frame.grid(row=0)

#     number_frame=numbers(app)
#     number_frame.grid(row=1,column=0,sticky=tk.W)


app.mainloop()

# create_main_window()

