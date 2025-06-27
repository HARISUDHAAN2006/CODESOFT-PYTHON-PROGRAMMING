

import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    
    if password_length <= 0:
        messagebox.showerror("Error", "Password length must be greater than 0")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(password_length))
    
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

root = tk.Tk()
root.title("Password Generator")
''

length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_label = tk.Label(root, text="Generated Password:")
password_label.pack()

password_entry = tk.Entry(root)
password_entry.pack()
root.mainloop()