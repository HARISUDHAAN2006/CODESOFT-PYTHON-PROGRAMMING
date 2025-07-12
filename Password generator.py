import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        password_length = int(length_entry.get())
        if password_length <= 0:
            messagebox.showerror("Error", "Password length must be greater than 0")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("350x200")
root.config(bg="#f0f0f0")

length_label = tk.Label(root, text="Password Length:", font=("Arial", 12), bg="#f0f0f0")
length_label.pack(pady=5)

length_entry = tk.Entry(root, font=("Arial", 12))
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", font=("Arial", 12), bg="#4CAF50", fg="white", command=generate_password)
generate_button.pack(pady=10)

password_label = tk.Label(root, text="Generated Password:", font=("Arial", 12), bg="#f0f0f0")
password_label.pack(pady=5)

password_entry = tk.Entry(root, font=("Arial", 12))
password_entry.pack(pady=5)

root.mainloop()
