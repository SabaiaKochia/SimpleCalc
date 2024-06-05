#   Saba Kochadze
#   Dec 28, 2023
#   Update 1.0 June 5, 2024
#   Simple Calculator



from ctypes.wintypes import RGB
from tkinter import *
from tkinter.tix import INTEGER
from turtle import color



def add_data():
    global result 
    
    num1_val = int(num1.get())
    num2_val = int(num2.get())
    
    result = num1_val + num2_val
    
def sub_data():
    global result
    num1_val = int(num1.get())
    num2_val = int(num2.get())
    
    result = num1_val - num2_val


def mul_data():
    global result
    num1_val = int(num1.get())
    num2_val = int(num2.get())
    
    result = num1_val * num2_val
    
def div_data():
    global result
    num1_val = int(num1.get())
    num2_val = int(num2.get())
    
    result = num1_val / num2_val
    
def power_data():
    global result
    num1_val = int(num1.get())
    num2_val = int(num2.get())
    
    result = 1
    
    i = 0
    while num2_val > i:
        
        result = result * num1_val
        
        i = i + 1
    
def clear():

    num1.delete(0, END)
    num1.insert(0, "")
    num2.delete(0, END)
    num2.insert(0, "")
    

def calculate():
    
    lab1 = Label(window, text = 'Result' + str(result)).grid(row = i, column = 1)
    
    
#   declare a window
window = Tk()

#   Title + Shape
window.title("Simple Calculator")
window.geometry()
  
lab1 = Label(window, text="NUM 1").grid(row=0)
lab2 = Label(window, text="NUM 2").grid(row=1)

num1 = Entry(window)
num2 = Entry(window)

num1.grid(row=0, column=1)
num2.grid(row = 1, column = 1)

Button( window, text='EXIT', command=window.quit).grid( row=5, column=3, pady=4)
Button( window, text='ENTER', command= calculate).grid( row=5, column=1, pady=1)
Button( window, text='CLEAR', command= clear).grid( row=3, column=3, pady=4)
Button( window, text='+', command= add_data).grid(row=3,column=0,pady=1)
Button( window, text='-', command= sub_data).grid(row=3,column=1,pady=1)
Button( window, text='x', command= mul_data).grid(row=4,column=0,pady=1)
Button( window, text='/', command= div_data).grid(row=4,column=1,pady=1)
Button( window, text='^', command= power_data).grid(row=5,column=0,pady=1)

#Allows the grid to adjust as it is reshaped

for row in range(7):
    window.grid_rowconfigure(row, weight=1)
for col in range(7):
    window.grid_columnconfigure(col, weight=1)
#   Displays the window
window.mainloop()
