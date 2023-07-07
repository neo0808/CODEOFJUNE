import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task_name = task_entry.get()
    if task_name:
        tasks.append(task_name)
        task_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Task added successfully!")
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Please enter a task name.")

def update_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        index = selected_task[0]
        new_task_name = task_entry.get()
        if new_task_name:
            tasks[index] = new_task_name
            task_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Task updated successfully!")
            update_task_list()
        else:
            messagebox.showwarning("Warning", "Please enter a task name.")
    else:
        messagebox.showwarning("Warning", "Please select a task to update.")

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        index = selected_task[0]
        del tasks[index]
        messagebox.showinfo("Success", "Task deleted successfully!")
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

def clear_task_list():
    confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to clear the task list?")
    if confirmed:
        tasks.clear()
        update_task_list()

root = tk.Tk()
root.title("To-Do List")

task_frame = tk.Frame(root)
task_label = tk.Label(task_frame, text="Task:")
task_label.pack(side=tk.LEFT)
task_entry = tk.Entry(task_frame)
task_entry.pack(side=tk.LEFT)
task_entry.focus()
task_frame.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

update_button = tk.Button(root, text="Update Task", command=update_task)
update_button.pack()

task_listbox = tk.Listbox(root, width=50)
task_listbox.pack(pady=10)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

clear_button = tk.Button(root, text="Clear Task List", command=clear_task_list)
clear_button.pack()

root.mainloop()
