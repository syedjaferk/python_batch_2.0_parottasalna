import tkinter as tk
from tkinter import messagebox

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def pow_func(a, b):
    return a ** b

def rem(a, b):
    return a % b

def calculate():
    try:
        a = float(entry_num1.get())
        b = float(entry_num2.get())
        op = operation_var.get()
        
        if op == "Addition":
            result = add(a, b)
        elif op == "Subtraction":
            result = sub(a, b)
        elif op == "Multiplication":
            result = mul(a, b)
        elif op == "Division":
            result = div(a, b)
        elif op == "Modulus":
            result = rem(a, b)
        elif op == "Power":
            result = pow_func(a, b)
        else:
            result = "Select a valid operation"

        label_result.config(text=f"Result: {result}")
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", "Invalid input")

# GUI setup
root = tk.Tk()
root.title("Simple Calculator")

# Number inputs
tk.Label(root, text="Enter first number:").grid(row=0, column=0, pady=5)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, pady=5)

tk.Label(root, text="Enter second number:").grid(row=1, column=0, pady=5)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, pady=5)

# Operation selection
tk.Label(root, text="Select operation:").grid(row=2, column=0, pady=5)
operation_var = tk.StringVar(root)
operation_var.set("Addition")  # default value
operations = ["Addition", "Subtraction", "Multiplication", "Division", "Modulus", "Power"]
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.grid(row=2, column=1, pady=5)

# Calculate button
calculate_btn = tk.Button(root, text="Calculate", command=calculate)
calculate_btn.grid(row=3, column=0, columnspan=2, pady=10)

# Result label
label_result = tk.Label(root, text="Result: ")
label_result.grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()
