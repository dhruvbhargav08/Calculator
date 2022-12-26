from tkinter import *
root=Tk()
root.title("Calculator")
entry=Entry(root,width=35)
entry.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def input(number):
    current=entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current)+str(number))
def clear():
    entry.delete(0,END)
def addition():
    first_number=entry.get()
    global f_num
    global operation
    operation=1
    f_num=float(first_number)
    entry.delete(0,END)
def substraction():
    first_number=entry.get()
    global f_num
    global operation
    operation=2
    f_num=float(first_number)
    entry.delete(0,END)
def multiplication():
    first_number=entry.get()
    global f_num
    global operation
    operation=3
    f_num=float(first_number)
    entry.delete(0,END)
def division():
    first_number=entry.get()
    global f_num
    global operation
    operation=4
    f_num=float(first_number)
    entry.delete(0,END)
def equal():
    second_number=entry.get()
    entry.delete(0,END)
    s_num=float(second_number)
    if operation==1:
        answer=f_num+s_num
    if operation==2:
        answer=f_num-s_num
    if operation==3:
        answer=f_num*s_num
    if operation==4:
        answer=f_num/s_num
    entry.insert(0,answer)
button_7=Button(root,text="7",padx=40,pady=20,command=lambda: input(7)).grid(row=1,column=0)
button_8=Button(root,text="8",padx=40,pady=20,command=lambda: input(8)).grid(row=1,column=1)
button_9=Button(root,text="9",padx=40,pady=20,command=lambda: input(9)).grid(row=1,column=2)
button_4=Button(root,text="4",padx=40,pady=20,command=lambda: input(4)).grid(row=2,column=0)
button_5=Button(root,text="5",padx=40,pady=20,command=lambda: input(5)).grid(row=2,column=1)
button_6=Button(root,text="6",padx=40,pady=20,command=lambda: input(6)).grid(row=2,column=2)
button_1=Button(root,text="1",padx=40,pady=20,command=lambda: input(1)).grid(row=3,column=0)
button_2=Button(root,text="2",padx=40,pady=20,command=lambda: input(2)).grid(row=3,column=1)
button_3=Button(root,text="3",padx=40,pady=20,command=lambda: input(3)).grid(row=3,column=2)
button_zero=Button(root,text="0",padx=40,pady=20,command=lambda: input(0)).grid(row=4,column=0)
button_addition=Button(root,text="+",padx=40,pady=20,command=addition).grid(row=4,column=1)
button_substraction=Button(root,text="-",padx=40,pady=20,command=substraction).grid(row=4,column=2)
button_multiply=Button(root,text="X",padx=40,pady=20,command=multiplication).grid(row=5,column=0)
button_divide=Button(root,text="/",padx=40,pady=20,command=division).grid(row=5,column=1)
button_equal=Button(root,text="=",padx=40,pady=20,command=equal).grid(row=5,column=2)
button_clear=Button(root,text="Clear",padx=40,pady=20,command=clear).grid(row=6,column=0,columnspan=3)
root.mainloop()