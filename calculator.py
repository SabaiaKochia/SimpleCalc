#   Saba Kochadze
#   Dec 28, 2023
#   Update 1.0 June 5, 2024
#   Update 1.1 June 14, 2024
#   Simple Calculator



from tkinter import *
from tkinter.tix import INTEGER
import math

def test_dummy():
    pass



def on_validate(P):
    # Validate function to allow only integers and an optional minus sign
    if P.isdigit() or (P == "-" and len(num1.get()) == 0):
        return True
    else:
        return False

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
        
def square_root():


    Label(Tk(), text='Sorry but the square root function is out on a smoke break right now').grid(row=0, column=0)
    
    
    Label
    

    

    
def clear():

    num1.delete(0, END)
    num1.insert(0, "")
    num2.delete(0, END)
    num2.insert(0, "")

    

def calculate():
    
    lab1 = Label(window, text = 'Result' + str(result)).grid(row = 7, column = 1)
    
    
#   declare a window
window = Tk()

#   Title + Shape
window.title("Saba Kochadze Simple Calculator")
window.geometry()
  
lab1 = Label(window, text="NUM 1").grid(row=0)
lab2 = Label(window, text="NUM 2").grid(row=1)

vcmd = window.register(on_validate)
num1 = Entry(window, validate="key", validatecommand=(vcmd, '%P'))
num2 = Entry(window, validate="key", validatecommand=(vcmd, '%P'))

num1.grid(row=0, column=1)
num2.grid(row = 1, column = 1)

Button( window, text='EXIT',fg='black' ,bg='light blue', command=window.quit).grid( row=6, column=2)
Button( window, text='=',fg='black' ,bg='light blue',width= 5, command= calculate).grid( row=6, column=1)
Button( window, text='CLEAR',fg='black' ,bg='light blue', command= clear).grid( row=5, column=1)
Button( window, text='+',fg='black' ,bg='orange', width= 5, command= add_data).grid(row=3,column=0)
Button( window, text='-',fg='black' ,bg='orange',width= 5, command= sub_data).grid(row=3,column=1)
Button( window, text='x',fg='black' ,bg='orange',width= 5, command= mul_data).grid(row=4,column=0)
Button( window, text='/',fg='black' ,bg='orange',width= 5, command= div_data).grid(row=4,column=1)
Button( window, text='^',fg='black' ,bg='orange',width= 5, command= power_data).grid(row=5,column=0)
Button( window, text='Sqrt()',fg='black' ,bg='orange',width= 5, command= square_root).grid(row=6,column=0)


#Allows the grid to adjust as it is reshaped

for row in range(7):
    window.grid_rowconfigure(row, weight=1)
for col in range(7):
    window.grid_columnconfigure(col, weight=1)
#   Displays the window
window.mainloop()
