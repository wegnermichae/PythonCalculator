import tkinter as tk  
from tkinter import *  

#Setting up of GUI
root = tk.Tk()
root.title("Calculator")

commands = []

entry_box = Entry(root, width=40, borderwidth=5)
entry_box.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#Defining of Functions
def button_click(number):
    current = entry_box.get()
    entry_box.delete(0, END)
    entry_box.insert(0, str(current) + str(number))

def button_clear():
    entry_box.delete(0, END)
    commands.clear()

def button_add():
    commands.clear()
    current = entry_box.get()
    commands.append(current)
    commands.append("add")
    entry_box.delete(0, END)

def button_minus():
    commands.clear()
    current = entry_box.get()
    commands.append(current)
    commands.append("minus")
    entry_box.delete(0, END)

def button_multiply():
    commands.clear()
    current = entry_box.get()
    commands.append(current)
    commands.append("multiply")
    entry_box.delete(0, END)

def button_divide():
    commands.clear()
    current = entry_box.get()
    commands.append(current)
    commands.append("divide")
    entry_box.delete(0, END)

def negative_button():
    commands.clear()
    current = entry_box.get()
    entry_box.delete(0, END)
    entry_box.insert(0, float(current) * -1)
#Decimal Logic incomplete: adds aditional leading 0
def decimal_button():
    commands.clear()
    current = entry_box.get()
    if len(entry_box.get()) == 0:
        current = 0
    entry_box.delete(0, END)
    entry_box.insert(0, float(current))

def percent_button():
    commands.clear()
    current = entry_box.get()
    entry_box.delete(0, END)
    entry_box.insert(0, float(current) / 100)

#Equals button Logic
def equals_button(arr):
    first = arr[0]
    second = entry_box.get()
    operand = arr[1]
    if operand == "add":
        entry_box.delete(0, END)
        entry_box.insert(0, float(first) + float(second))
    elif operand == "minus":
        entry_box.delete(0, END)
        entry_box.insert(0, float(first) - float(second))
    elif operand == "multiply":
        entry_box.delete(0, END)
        entry_box.insert(0, float(first) * float(second))
    elif operand == "divide":
        entry_box.delete(0, END)
        entry_box.insert(0, float(first) / float(second))

    commands.clear()

#Setting up of Buttons and commands
but_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
but_1.grid(row=4 ,column=0)
but_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
but_2.grid(row=4 ,column=1)
but_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
but_3.grid(row=4 ,column=2)
but_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
but_4.grid(row=3 ,column=0)
but_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
but_5.grid(row=3 ,column=1)
but_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
but_6.grid(row=3 ,column=2)
but_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
but_7.grid(row=2 ,column=0)
but_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
but_8.grid(row=2 ,column=1)
but_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
but_9.grid(row=2 ,column=2)
but_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
but_0.grid(row=5 ,column=1)

add_but = Button(root, text="+", padx=40, pady=20, command= lambda: button_add())
add_but.grid(row=4, column=3)

eq_but = Button(root, text="=", padx=40, pady=20, command=lambda: equals_button(commands))
eq_but.grid(row=5, column=3)

sub_but = Button(root, text="-", padx=41, pady=20, command=lambda: button_minus())
sub_but.grid(row=3, column=3)

mul_but = Button(root, text="x", padx=41, pady=20, command=lambda: button_multiply())
mul_but.grid(row=2, column=3)

div_but = Button(root, text="÷", padx=40, pady=20, command=lambda: button_divide())
div_but.grid(row=1, column=3)

clear_but = Button(root, text="C", padx=39, pady=20, command=lambda: button_clear())
clear_but.grid(row=1, column=0)

per_but = Button(root, text="%", padx=39, pady=20, command=lambda: percent_button())
per_but.grid(row=1, column=2)

dec_but = Button(root, text=".", padx=41, pady=20, command=lambda: decimal_button())
dec_but.grid(row=5, column=2)

neg_but = Button(root, text="+/-", padx=34, pady=20, command=lambda: negative_button())
neg_but.grid(row=1, column=1)

root.mainloop()