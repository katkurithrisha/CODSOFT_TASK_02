import tkinter as tk

def add():
    try:
        result = float(entry1.get()) + float(entry2.get())
        label_result.config(text="Result: " + str(result))
    except ValueError:
        label_result.config(text="Invalid input! Please enter numeric values.")

def subtract():
    try:
        result = float(entry1.get()) - float(entry2.get())
        label_result.config(text="Result: " + str(result))
    except ValueError:
        label_result.config(text="Invalid input! Please enter numeric values.")

def multiply():
    try:
        result = float(entry1.get()) * float(entry2.get())
        label_result.config(text="Result: " + str(result))
    except ValueError:
        label_result.config(text="Invalid input! Please enter numeric values.")

def divide():
    try:
        denominator = float(entry2.get())
        if denominator == 0:
            label_result.config(text="Error! Division by zero.")
        else:
            result = float(entry1.get()) / denominator
            label_result.config(text="Result: " + str(result))
    except ValueError:
        label_result.config(text="Invalid input! Please enter numeric values.")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("1000x1000")

# Create and place widgets
label1 = tk.Label(root, text="Enter first number:")
label1.grid(row=0, column=0, sticky=tk.W)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

label2 = tk.Label(root, text="Enter second number:")
label2.grid(row=1, column=0, sticky=tk.W)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

button_add = tk.Button(root, text="Add", command=add)
button_add.grid(row=2, column=0)

button_subtract = tk.Button(root, text="Subtract", command=subtract)
button_subtract.grid(row=2, column=1)

button_multiply = tk.Button(root, text="Multiply", command=multiply)
button_multiply.grid(row=3, column=0)

button_divide = tk.Button(root, text="Divide", command=divide)
button_divide.grid(row=3, column=1)

label_result = tk.Label(root, text="Result: ")
label_result.grid(row=4, columnspan=2)

# Run the application
root.mainloop()
