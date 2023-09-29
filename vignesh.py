import tkinter as tk
import math
import tkinter.messagebox
from math import factorial

calculation =" "
is_degrees = True 

# usend to enter the numbers 
def add_to_calcultion(symbol): 
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0 ,calculation)

# It is used for calculation 
def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0 , result)
    except:
        clear_field()
        text_result.insert(1.0 , "Error")

# Defing clear the all numbers in text box
def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0 ,"end")

# Defing removel of last character
def remove_last_character():
    global calculation
    calculation = calculation[:-1]
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

# Define a function to calculate the decimal_point
def add_decimal_point():
    global calculation
    if "." not in calculation:
        calculation += "."
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)

# Define a function to calculate the calculate_square
def calculate_square():
    global calculation
    try:
        result = str(eval(calculation) ** 2)
        calculation = result
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

# Define a function to calculate the calculate_square_root
def calculate_square_root():
    global calculation
    try:
        result = str(math.sqrt(eval(calculation)))
        calculation = result
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

# Define a function to calculate the calculate_cos
def calculate_cos():
    global calculation
    try:
        if is_degrees:
            result = str(math.cos(math.radians(eval(calculation))))
        else:
            result = str(math.cos(eval(calculation)))
        calculation = result
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

# Define a function to calculate the calculate_sin
def calculate_sin():
    global calculation
    try:
        if is_degrees:
            result = str(math.sin(math.radians(eval(calculation))))
        else:
            result = str(math.sin(eval(calculation)))
        calculation = result
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

# Define a function to calculate the calculate_tan
def calculate_tan():
    global calculation
    try:
        if is_degrees:
            result = str(math.tan(math.radians(eval(calculation))))
        else:
            result = str(math.tan(eval(calculation)))
        calculation = result
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

# Define a function to calculate the calculate_log
def calculate_log():
    global calculation
    try:
        result = str(math.log(eval(calculation)))
        calculation = result
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

# Define a function to calculate the calculate_exponential
def calculate_exponential():
    global calculation
    try:
        result = str(math.exp(eval(calculation)))
        calculation = result
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

# Define a function to calculate the factorial
def calculate_factorial():
    global calculation
    try:
        num = int(eval(calculation))
        result = str(factorial(num))
        calculation = result
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

root = tk.Tk()
root.geometry("303x260")
root.resizable(0 , 0)
root.configure(bg= "#3d7c47")

#To Show the result
text_result = tk.Text(root , height=2 ,width=21 , font=("Arial", 24))
text_result.grid(columnspan=5 )

# To add the buttons 
btn_1 = tk.Button(root, text="1", command=lambda:  add_to_calcultion(1) , width=5 ,font=("Arial", 14) )
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text="2",  command=lambda: add_to_calcultion(2) , width=5 ,font=("Arial", 14) )
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text="3",  command=lambda: add_to_calcultion(3) , width=5 ,font=("Arial", 14) )
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calcultion(4) , width=5 ,font=("Arial", 14) )
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calcultion(5), width=5 ,font=("Arial", 14) )
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calcultion(6) , width=5 ,font=("Arial", 14) )
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calcultion(7) , width=5 ,font=("Arial", 14) )
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calcultion(8) , width=5 ,font=("Arial", 14) )
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calcultion(9) , width=5 ,font=("Arial", 14) )
btn_9.grid(row=4, column=3)
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calcultion(0) , width=5 ,font=("Arial", 14) )
btn_0.grid(row=5, column=2)
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calcultion("+") , width=5 ,font=("Arial", 14) )
btn_plus.grid(row=2, column=4)
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calcultion("-") , width=5 ,font=("Arial", 14) )
btn_minus.grid(row=3, column=4)
btn_mul = tk.Button(root, text="*", command=lambda: add_to_calcultion("*") , width=5 ,font=("Arial", 14) )
btn_mul.grid(row=4, column=4)
btn_div = tk.Button(root, text="/", command=lambda: add_to_calcultion("/") , width=5 ,font=("Arial", 14) )
btn_div.grid(row=5, column=4)
btn_open = tk.Button(root, text="(", command=lambda: add_to_calcultion("(") , width=5 ,font=("Arial", 14) )
btn_open.grid(row=5, column=1)
btn_close = tk.Button(root, text=")", command=lambda: add_to_calcultion(")") , width=5 ,font=("Arial", 14) )
btn_close.grid(row=5, column=3)
btn_equals = tk.Button(root, text="=", command=evaluate_calculation  , width=5 ,font=("Arial", 14) )
btn_equals.grid(row=6, column=4)
btn_clear = tk.Button(root, text="c", command=clear_field , width=5 ,font=("Arial", 14) )
btn_clear.grid(row=6, column=1)
btn_backspace = tk.Button(root, text="←", command=remove_last_character, width=5, font=("Arial", 14))
btn_backspace.grid(row=6, column=2)
btn_decimal = tk.Button(root, text=".", command=add_decimal_point, width=5, font=("Arial", 14))
btn_decimal.grid(row=6, column=3)
btn_square = tk.Button(root, text="x^2", command=calculate_square, width=5, font=("Arial", 14))
btn_square.grid(row=7, column=1)
btn_square_root = tk.Button(root, text="√", command=calculate_square_root, width=5, font=("Arial", 14))
btn_square_root.grid(row=7, column=2)
btn_cos = tk.Button(root, text="cos", command=calculate_cos, width=5, font=("Arial", 14))
btn_cos.grid(row=8, column=2)
btn_sin = tk.Button(root, text="sin", command=calculate_sin, width=5, font=("Arial", 14))
btn_sin.grid(row=8, column=1)
btn_tan = tk.Button(root, text="tan", command=calculate_tan, width=5, font=("Arial", 14))
btn_tan.grid(row=8, column=3)
btn_log = tk.Button(root, text="log", command=calculate_log, width=5, font=("Arial", 14))
btn_log.grid(row=7, column=3)
btn_exp = tk.Button(root, text="exp", command=calculate_exponential, width=5, font=("Arial", 14))
btn_exp.grid(row=7, column=4)
btn_factorial = tk.Button(root, text="!", command=calculate_factorial, width=5, font=("Arial", 14))
btn_factorial.grid(row=8, column=4)

root.mainloop()