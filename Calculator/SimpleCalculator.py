from tkinter import *

root = Tk()

root.title("Calculator")
root.geometry("300x332")
root.resizable(0,0) #Prevents the Window Resize

expression = ""
input_num = StringVar()

def btn_clicked(number):
    global expression
    expression = expression + str(number)
    input_num.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_num.set("")

def btn_equal():
    global expression
    result = str(eval(expression))
    input_num.set(result)
    expression=""

input_frame = Frame(root, width = 290, height=5, bd=5, highlightbackground = "black", highlightcolor="black")
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable=input_num, width=50, bg = "#ee9", bd=0)

input_field.grid(row=0, column=0)
input_field.pack(ipady=5)

btn_frame = Frame(root, width= 290, bg="grey")
btn_frame.pack(ipady=2,ipadx=2)

#First Row:
btn_cancel = Button(btn_frame, text="C", fg="black",width=32,height=3,bd=2, bg="#ffe", cursor="hand2", command=btn_clear)
btn_cancel.grid(row=0,column=0,columnspan=3)
btn_divide = Button(btn_frame, text="/", fg="black",width=10,height=3,bd=2, bg="#ffc", cursor="hand2", command=lambda:btn_clicked("/"))
btn_divide.grid(row=0,column=3)

#Second Row:
btn_seven = Button(btn_frame, text="7", fg="black",width=10,height=3,bd=2, bg="#fff", cursor="hand2", command=lambda:btn_clicked(7))
btn_seven.grid(row=1,column=0)
btn_eight = Button(btn_frame, text="8", fg="black",width=10,height=3,bd=2, bg="#fff", cursor="hand2", command=lambda:btn_clicked(8))
btn_eight.grid(row=1,column=1)
btn_nine = Button(btn_frame, text="9", fg="black",width=10,height=3,bd=2, bg="#fff", cursor="hand2", command=lambda:btn_clicked(9))
btn_nine.grid(row=1,column=2)
btn_multiply = Button(btn_frame, text="X", fg="black",width=10,height=3,bd=2, bg="#ffc", cursor="hand2", command=lambda:btn_clicked("*"))
btn_multiply.grid(row=1,column=3)

#Third Row:
btn_four = Button(btn_frame, text="4", fg="black",width=10,height=3,bd=2, bg="#fff", cursor="hand2", command=lambda:btn_clicked(4))
btn_four.grid(row=2,column=0)
btn_five = Button(btn_frame, text="5", fg="black",width=10,height=3,bd=2, bg="#fff", cursor="hand2", command=lambda:btn_clicked(5))
btn_five.grid(row=2,column=1)
btn_six = Button(btn_frame, text="6", fg="black",width=10,height=3,bd=2, bg="#fff", cursor="hand2", command=lambda:btn_clicked(6))
btn_six.grid(row=2,column=2)
btn_subtract = Button(btn_frame, text="-", fg="black",width=10,height=3,bd=2, bg="#ffc", cursor="hand2", command=lambda:btn_clicked("-"))
btn_subtract.grid(row=2,column=3)

#Fourth Row:
btn_one = Button(btn_frame, text="1", fg="black",width=10,height=3,bd=2, bg="#fff", cursor="hand2", command=lambda:btn_clicked(1))
btn_one.grid(row=3,column=0)
btn_two = Button(btn_frame, text="2", fg="black",width=10,height=3,bd=2, bg="#fff", cursor="hand2", command=lambda:btn_clicked(2))
btn_two.grid(row=3,column=1)
btn_three = Button(btn_frame, text="3", fg="black",width=10,height=3,bd=2, bg="#fff", cursor="hand2", command=lambda:btn_clicked(3))
btn_three.grid(row=3,column=2)
btn_add = Button(btn_frame, text="+", fg="black",width=10,height=3,bd=2, bg="#ffc", cursor="hand2", command=lambda:btn_clicked("+"))
btn_add.grid(row=3,column=3)

#Fifth Row:
btn_zero = Button(btn_frame, text="0", fg="black",width=21,height=3,bd=2, bg="#fff", cursor="hand2", command=lambda:btn_clicked(0))
btn_zero.grid(row=4,column=0, columnspan=2)
btn_dot = Button(btn_frame, text=".", fg="black",width=10,height=3,bd=2, bg="#ffe", cursor="hand2", command=lambda:btn_clicked("."))
btn_dot.grid(row=4,column=2)
btn_eq = Button(btn_frame, text="=", fg="black",width=10,height=3,bd=2, bg="#ffc", cursor="hand2", command=btn_equal)
btn_eq.grid(row=4,column=3)

root.mainloop()


