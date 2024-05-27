import tkinter as tk
from tkinter import *
clc=tk.Tk()
clc.title("Python Caluclator")

def equal_to():
    try:
        output=str(eval(display.get()))
        clearing_io()
        display.insert(0,output)
    except:
        clearing_io()
        display.insert(0,"Error")
        
def clearing_io():
    display.delete(0,END)

def send_input(num):
    
    take_input = display.get()
    clearing_io()
    show=take_input+num
    display.insert(0,show)

#for giving input and displaying output

display=Entry(clc,borderwidth=10,width=25,font=("Arial,28"),justify=RIGHT)
display.grid(row=0,column=0,columnspan=3,padx=30,pady=10)

#for creating buttons from 0 to 9

number_0=Button(clc,text="0",font=("arial,10"),padx=45,pady=7,command=lambda : send_input("0"))
number_0.grid(row=4,column=0)

number_1=Button(clc,text="1",font=("arial,10"),padx=45,pady=7,command=lambda:send_input("1"))
number_1.grid(row=3,column=0)

number_2=Button(clc,text="2",font=("arial,10"),padx=45,pady=7,command=lambda:send_input("2"))
number_2.grid(row=3,column=1)

number_3=Button(clc,text="3",font=("arial,10"),padx=45,pady=7,command=lambda:send_input("3"))
number_3.grid(row=3,column=2)

number_4=Button(clc,text="4",font=("arial,10"),padx=45,pady=7,command=lambda:send_input("4"))
number_4.grid(row=2,column=0)

number_5=Button(clc,text="5",font=("arial,10"),padx=45,pady=7,command=lambda:send_input("5"))
number_5.grid(row=2,column=1)

number_6=Button(clc,text="6",font=("arial,10"),padx=45,pady=7,command=lambda:send_input("6"))
number_6.grid(row=2,column=2)

number_7=Button(clc,text="7",font=("arial,10"), padx=45,pady=7,command=lambda:send_input("7"))
number_7.grid(row=1,column=0,padx=0,pady=0)

number_8=Button(clc,text="8",font=("arial,10") ,padx=45,pady=7,command=lambda:send_input("8"))
number_8.grid(row=1,column=1,padx=0,pady=0)

number_9=Button(clc,text="9",font=("arial,10") ,padx=45,pady=7,command=lambda:send_input("9"))
number_9.grid(row=1,column=2,padx=0,pady=0)

#creating clear button

button_clear=Button(clc,text="Clear",font=("arial,10"),padx=86,pady=7,command=clearing_io)
button_clear.grid(row=4,column=1,columnspan=2)

#creating mathematical operators

addition_button=Button(clc,text="+",font=("arial,10"),padx=44,pady=7,command=lambda:send_input("+"))
addition_button.grid(row=5,column=0)

subtraction_button=Button(clc,text="-",font=("arial,10"),padx=46,pady=7,command=lambda:send_input("-"))
subtraction_button.grid(row=5,column=1)

multiplication_button=Button(clc,text="*",font=("arial,10"),padx=46,pady=7,command=lambda:send_input("*"))
multiplication_button.grid(row=6,column=0)

division_button=Button(clc,text="/",font=("arial,10"),padx=46,pady=7,command=lambda:send_input("/"))
division_button.grid(row=6,column=1)

equalto_button=Button(clc,text="=",font=("arial,10"),padx="44",pady=32,command=equal_to)
equalto_button.grid(row=5,column=2,rowspan=2)


 




clc.mainloop()