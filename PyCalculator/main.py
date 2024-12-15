import tkinter as tk
from tkinter import messagebox


# FUNCTIONS

condition = True


def add_digit(digit):
    value = calc.get()
    global condition
    if condition == False:
        value = "0"
    if value[0] == "0" and len(value) == 1:
        value = value[1:]
    calc["state"] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, value+digit)
    condition = True
    calc["state"] = tk.DISABLED


def add_operation(operation):
    global condition
    value = calc.get()
    if value[-1] in "+-*/":
        value = value[:-1]
    elif "+" in value or "-" in value or "*" in value or "/" in value:
        value = eval(value)
    calc["state"] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, str(value)+operation)
    condition = True
    calc["state"] = tk.DISABLED


def calculate():
    global condition    
    value = calc.get()
    if value[-1] in "+-*/":
        value = value + value[:-1]
    try:
        result = eval(value)
        calc["state"] = tk.NORMAL
        calc.delete(0, tk.END)
        calc.insert(0, result)
        calc["state"] = tk.DISABLED
    except Exception:
        messagebox.showinfo("Attention", "Please enter valid data")
        calc["state"] = tk.NORMAL
        calc.delete(0, tk.END)
        calc.insert(0, "0")
        calc["state"] = tk.DISABLED
    condition = False


def clear():
    calc["state"] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, "0")
    calc["state"] = tk.DISABLED


def make_digit_button(num):
    return tk.Button(text=num, bd=5, font=("Arial", 15),bg="white", command= lambda : add_digit(num))


def make_oper_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 15), bg="orange", command= lambda : add_operation(operation))


def make_calc_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 15), bg="orange", command=calculate)


def make_clear_button(operation):
    return tk.Button(text=operation, bd=5, font=("Arial", 15),fg="white", bg="grey", command=clear)


def press_key(event):
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in "+-*/":
        add_operation(event.char)
    elif event.char == "\r":
        calculate()
    elif event.char == "=":
        calculate()


#Tkinter part

win = tk.Tk()
win.geometry(f"260x290+100+200")
win['bg'] = 'grey'
win.title("Calculator")

win.bind("<Key>", press_key)


calc = tk.Entry(win, justify=tk.RIGHT, font=("Arial", 17), width=15, bd=10, fg="black")
calc.insert(0, "0")
calc["state"] = tk.DISABLED
calc.grid(row=0, column=0, columnspan=4, stick="we")


make_digit_button("1").grid(row=1, column=0, stick="wens", padx=5, pady=5)
make_digit_button("2").grid(row=1, column=1, stick="wens", padx=5, pady=5)
make_digit_button("3").grid(row=1, column=2, stick="wens", padx=5, pady=5)
make_digit_button("4").grid(row=2, column=0, stick="wens", padx=5, pady=5)
make_digit_button("5").grid(row=2, column=1, stick="wens", padx=5, pady=5)
make_digit_button("6").grid(row=2, column=2, stick="wens", padx=5, pady=5)
make_digit_button("7").grid(row=3, column=0, stick="wens", padx=5, pady=5)
make_digit_button("8").grid(row=3, column=1, stick="wens", padx=5, pady=5)
make_digit_button("9").grid(row=3, column=2, stick="wens", padx=5, pady=5)
make_digit_button("0").grid(row=4, column=0, stick="wens", padx=5, pady=5)

make_oper_button("+").grid(row=1, column=3, stick="wens", padx=5, pady=5)
make_oper_button("-").grid(row=2, column=3, stick="wens", padx=5, pady=5)
make_oper_button("*").grid(row=3, column=3, stick="wens", padx=5, pady=5)
make_oper_button("/").grid(row=4, column=3, stick="wens", padx=5, pady=5)

make_calc_button("=").grid(row=4, column=2, stick="wens", padx=5, pady=5)

make_clear_button("C").grid(row=4, column=1, stick="wens", padx=5, pady=5)


win.grid_columnconfigure(0, minsize=65)
win.grid_columnconfigure(1, minsize=65)
win.grid_columnconfigure(2, minsize=65)
win.grid_columnconfigure(3, minsize=65)


win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()