import tkinter as t
from tkinter import*
equation=""
def clear():
    global equation
    equation=""
    lb.config(text=equation)


def show(value):
    global equation
    equation+=value
    lb.config(text=equation)

def calculate():
    global equation
    result=""
    if(equation!=""):
        result=eval(equation)
        lb.config(text=result)



win=t.Tk()
win.geometry("570x600")
win.title("CALCULATOR")
win.resizable(False,False)
win.config(bg="blue")



lb=t.Label(win,text="",width=25,height=2,bg="springgreen",font=("arial",30))
lb.pack()

bt=t.Button(win,text="AC",
          width=5,height=1,
          bg="blue",fg="white",
          font=("arial",30,"bold"),
          bd=1,command=lambda:clear())
bt.place(x=10,y=100)
          
bt1=t.Button(win,text="/",
          width=5,height=1,
          bg="gray",fg="white",
          font=("arial",30,"bold"),
          bd=1,command=lambda:show("/"))
             
bt1.place(x=150,y=100)
   

bt2=t.Button(win,text="%",
          width=5,height=1,
          bg="gray",fg="white",
          font=("arial",30,"bold"),
          bd=2,command=lambda:show("%"))
bt2.place(x=290,y=100)

bt3=t.Button(win,text="*",
          width=5,height=1,
          bg="gray",fg="white",
          font=("arial",30,"bold"),
          bd=2,command=lambda:show("*"))
bt3.place(x=430,y=100)

bt4=t.Button(win,text="7",
          width=5,height=1,
          bg="brown",fg="white",
          font=("arial",30,"bold"),
          bd=2,command=lambda:show("7"))
bt4.place(x=10,y=200)

bt5=t.Button(win,text="8",
          width=5,height=1,
          bg="brown",fg="white",
          font=("arial",30,"bold"),
         bd=2,command=lambda:show("8"))
bt5.place(x=150,y=200)

bt6=t.Button(win,text="9",
          width=5,height=1,
          bg="brown",fg="white",
          font=("arial",30,"bold"),
          bd=2,command=lambda:show("9"))
bt6.place(x=290,y=200)

bt7=t.Button(win,text="-",
          width=5,height=1,
          bg="gray",fg="white",
          font=("arial",30,"bold"),
          bd=2,command=lambda:show("-"))
bt7.place(x=430,y=200)

bt8=t.Button(win,text="4",
          width=5,height=1,
          bg="brown",fg="white",
          font=("arial",30,"bold"),
          bd=2,command=lambda:show("4"))
bt8.place(x=10,y=300)

bt9=t.Button(win,text="5",
          width=5,height=1,
          bg="brown",fg="white",
          font=("arial",30,"bold"),
          bd=2,command=lambda:show("5"))
bt9.place(x=150,y=300)

bt10=t.Button(win,text="6",
          width=5,height=1,
          bg="brown",fg="white",
          font=("arial",30,"bold"),
          bd=2,command=lambda:show("6"))
bt10.place(x=290,y=300)

bt11=t.Button(win,text="+",
          width=5,height=1,
          bg="gray",fg="white",
          font=("arial",30,"bold"),
          bd=2,command=lambda:show("+"))
bt11.place(x=430,y=300)

bt12=t.Button(win,text="1",
          width=5,height=1,
          bg="brown",fg="white",
          font=("arial",30,"bold"),
          bd=2,command=lambda:show("1"))
bt12.place(x=10,y=400)

bt13=t.Button(win,text="2",
          width=5,height=1,
          bg="brown",fg="white",
          font=("arial",30,"bold"),
          bd=2,command=lambda:show("2"))
bt13.place(x=150,y=400)

bt14=t.Button(win,text="3",
          width=5,height=1,
          bg="brown",fg="white",
          font=("arial",30,"bold"),
          bd=2,command=lambda:show("3"))
bt14.place(x=290,y=400)

bt15=t.Button(win,text="=",
          width=5,height=3,
          bg="orange",fg="white",
          font=("arial",30,"bold"),
          bd=2,command=lambda:calculate())
bt15.place(x=430,y=400)

bt16=t.Button(win,text="0",
          width=5,height=1,
          bg="brown",fg="white",
          font=("arial",30,"bold"),
          bd=2,command=lambda:show("0"))
bt16.place(x=10,y=500)

bt16=t.Button(win,text="00",
          width=5,height=1,
          bg="brown",fg="white",
          font=("arial",30,"bold"),
          bd=2,command=lambda:show("00"))
bt16.place(x=150,y=500)




bt17=t.Button(win,text=".",
          width=5,height=1,
          bg="brown",fg="white",
          font=("arial",30,"bold"),
          bd=2,command=lambda:show("."))
bt17.place(x=290,y=500)















   
