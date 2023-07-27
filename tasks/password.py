import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_show_password():
    user_name = username_entry.get()
    password_length = int(length_entry.get())

    if not user_name:
        messagebox.showerror("Error","Please enter a username.")
        return

    if password_length <= 0:
        messagebox.showerror("Error","Please enter a valid password length.")
        return

    generated_password = generate_password(password_length)
    generated_password_label.config(text=f"Generated password for '{user_name}': {generated_password}")
    accept_button.config(state=tk.NORMAL)

def accept_password():
    accepted_password = generated_password_label.cget("text").split(": ")[-1]
    messagebox.showinfo("Accepted", f"Password '{accepted_password}' has been accepted. Thank you!")

def reset_fields():
    username_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    generated_password_label.config(text="")
    accept_button.config(state=tk.DISABLED)

app = tk.Tk()
app.title("Password Generator")

username_label = tk.Label(app, text="Username:")
username_label.pack()
username_entry = tk.Entry(app)
username_entry.pack()

length_label = tk.Label(app, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(app)
length_entry.pack()

generate_button = tk.Button(app, text="Generate Password", command=generate_and_show_password)
generate_button.pack()

generated_password_label = tk.Label(app, text="")
generated_password_label.pack()

accept_button = tk.Button(app, text="Accept", command=accept_password, state=tk.DISABLED)
accept_button.pack()

reset_button = tk.Button(app, text="Reset", command=reset_fields)
reset_button.pack()

app.mainloop()
