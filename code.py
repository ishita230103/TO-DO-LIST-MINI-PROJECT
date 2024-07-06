import tkinter as tk
from tkinter import messagebox
from tkinter import*

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def show_task():
    selected_task = listbox.curselection()
    if selected_task:
        task = listbox.get(selected_task)
        messagebox.showinfo("Task Details", f"Selected Task: {task}")
    else:
        messagebox.showwarning("Warning", "Please select a task to show.")

def update_task():
    selected_task = listbox.curselection()
    if selected_task:
        new_task = entry.get()
        if new_task:
            listbox.delete(selected_task)
            listbox.insert(selected_task, new_task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a new task.")
    else:
        messagebox.showwarning("Warning", "Please select a task to update.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")
root.config(background="light blue")

lbltitle=Label(root,text="ENTER TODAY'S TO-DO LIST",bd=5,relief=RIDGE
                      ,bg="white",fg="LIGHT BLUE",font=("times new roman",40,"bold"),padx=0,pady=2)
lbltitle.pack(side=TOP,fill=X)



# Create widgets
entry = tk.Entry(root, width=40)
add_button = tk.Button(root, text="Add Task", command=add_task)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
show_button = tk.Button(root, text="Show Task", command=show_task)
update_button = tk.Button(root, text="Update Task", command=update_task)
listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40)

# Place widgets in the window
entry.pack(pady=50)
add_button.pack(pady=5)
delete_button.pack(pady=5)
show_button.pack(pady=5)
update_button.pack(pady=5)
listbox.pack(pady=50)



# Start the main loop
root.mainloop()
