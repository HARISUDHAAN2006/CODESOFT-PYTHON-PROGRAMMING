import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    current = entry.get()
    try:
        result = eval(current)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")
''

entry = tk.Entry(root, width=20, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0
for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=20, pady=20, command=button_equal).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, padx=20, pady=20, command=lambda b=button: button_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

clear_button = tk.Button(root, text="C", padx=20, pady=20, command=button_clear)
clear_button.grid(row=row_val, column=col_val)

root.mainloop()
 