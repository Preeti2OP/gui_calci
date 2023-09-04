from tkinter import*
import tkinter as tk
from tkinter import ttk, messagebox


def clear():
    global equation
    equation = ""
    input_field.delete(0, "end")

def show(value):
    global equation
    equation += str(value)
    input_field.delete(0, "end")
    input_field.insert(0, equation)

def calculate():
    global equation
    try:
        result = eval(equation)
        input_field.delete(0, "end")
        input_field.insert(0, str(result))
        equation = str(result)
    except Exception as e:
        input_field.delete(0, "end")
        input_field.insert(0, "Error")
        equation = ""


root=tk.Tk()
root.geometry("700x500")
root.title("CALCULATOR")
root.config(bg='light green')
icon=PhotoImage(file="pngwing.com.png")
root.iconphoto(False,icon)

frame1 = Frame(root, bg='white', width='700', height='150')
frame1.pack()


equation=""


input_field = Entry(root, font='segoe 20 bold')
input_field.place(x=10, y=10, width=680)


button1=Button(root,text='7',bg='#081F4D',fg='white',font='segoe 20 bold',width=8,command=lambda:show("7"))
button1.place(x=10,y=160)

button2=Button(root,text='8',bg='#081F4D',fg='white',font='segoe 20 bold',width=8,command=lambda:show("8"))
button2.place(x=185,y=160)

button3=Button(root,text='9',bg='#081F4D',fg='white',font='segoe 20 bold',width=8,command=lambda:show("9"))
button3.place(x=350,y=160)

button4=Button(root,text='4',bg='#081F4D',fg='white',font='segoe 20 bold',width=8,command=lambda:show("4"))
button4.place(x=10,y=220)

button5=Button(root,text='5',bg='#081F4D',fg='white',font='segoe 20 bold',width=8,command=lambda:show("5"))
button5.place(x=185,y=220)

button6=Button(root,text='6',bg='#081F4D',fg='white',font='segoe 20 bold',width=8,command=lambda:show("6"))
button6.place(x=350,y=220)

button7=Button(root,text='3',bg='#081F4D',fg='white',font='segoe 20 bold',width=8,command=lambda:show("3"))
button7.place(x=10,y=280)

button8=Button(root,text='2',bg='#081F4D',fg='white',font='segoe 20 bold',width=8,command=lambda:show("2"))
button8.place(x=185,y=280)

button9=Button(root,text='1',bg='#081F4D',fg='white',font='segoe 20 bold',width=8,command=lambda:show("1"))
button9.place(x=350,y=280)

button10=Button(root,text='C',bg='orange',fg='white',font='segoe 20 bold',width=8,command=lambda:clear())
button10.place(x=10,y=340)

button11=Button(root,text='0',bg='#081F4D',fg='white',font='segoe 20 bold',width=8,command=lambda:show("0"))
button11.place(x=185,y=340)

button12=Button(root,text='.',bg='#081F4D',fg='white',font='segoe 20 bold',width=8,command=lambda:show("."))
button12.place(x=350,y=340)

button13=Button(root,text='X',bg='red',fg='white',font='segoe 20 bold',width=8,command=lambda:show("X"))
button13.place(x=515,y=160)

button14=Button(root,text='+',bg='red',fg='white',font='segoe 20 bold',width=8,command=lambda:show("+"))
button14.place(x=515,y=220)

button15=Button(root,text='-',bg='red',fg='white',font='segoe 20 bold',width=8,command=lambda:show("-"))
button15.place(x=515,y=280)

button16=Button(root,text='%',bg='red',fg='white',font='segoe 20 bold',width=8,command=lambda:show("%"))
button16.place(x=515,y=340)

button17=Button(root,text='x',bg='orange',fg='white',font='segoe 20 bold',width=8,command=lambda:show("x"))
button17.place(x=350,y=400)

button17=Button(root,text='/',bg='red',fg='white',font='segoe 20 bold',width=8,command=lambda:show("/"))
button17.place(x=185,y=400)

button17=Button(root,text='=',bg='red',fg='white',font='segoe 20 bold',width=8,command=calculate)
button17.place(x=10,y=400)


root.mainloop()