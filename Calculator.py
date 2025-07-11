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
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Classic Calculator")
root.config(bg="#f0f0f0")
root.geometry("320x400")
root.resizable(False, False)

entry = tk.Entry(root, width=18, borderwidth=5, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

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
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 14), bg="#4CAF50", fg="white", command=button_equal).grid(row=row_val, column=col_val, padx=5, pady=5)
    else:
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 14), bg="white", fg="black", command=lambda b=button: button_click(b)).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(root, text="C", padx=20, pady=20, font=("Arial", 14), bg="#f44336", fg="white", command=button_clear).grid(row=row_val, column=col_val, padx=5, pady=5)

root.mainloop()
