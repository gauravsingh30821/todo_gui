import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "tasks.json"

# ---------------------------
# Functions
# ---------------------------

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file)

def refresh_list():
    task_list.delete(0, tk.END)
    for task in tasks:
        task_list.insert(tk.END, task)

def add_task():
    task = task_entry.get()

    if task.strip() == "":
        messagebox.showwarning("Warning", "Task cannot be empty!")
        return

    tasks.append(task)
    save_tasks()
    refresh_list()
    task_entry.delete(0, tk.END)

def delete_task():
    try:
        index = task_list.curselection()[0]
        tasks.pop(index)
        save_tasks()
        refresh_list()
    except:
        messagebox.showwarning("Warning", "Select a task first!")

def complete_task():
    try:
        index = task_list.curselection()[0]

        if not tasks[index].startswith("✓ "):
            tasks[index] = "✓ " + tasks[index]

        save_tasks()
        refresh_list()

    except:
        messagebox.showwarning("Warning", "Select a task first!")

# ---------------------------
# Main Window
# ---------------------------

root = tk.Tk()
root.title("Modern To-Do App")
root.geometry("500x500")

tasks = load_tasks()

title = tk.Label(
    root,
    text="To-Do List",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)

task_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=30
)
task_entry.pack(pady=10)

add_btn = tk.Button(
    root,
    text="Add Task",
    command=add_task,
    width=20
)
add_btn.pack(pady=5)

task_list = tk.Listbox(
    root,
    width=50,
    height=12,
    font=("Arial", 12)
)
task_list.pack(pady=10)

complete_btn = tk.Button(
    root,
    text="Mark Complete",
    command=complete_task,
    width=20
)
complete_btn.pack(pady=5)

delete_btn = tk.Button(
    root,
    text="Delete Task",
    command=delete_task,
    width=20
)
delete_btn.pack(pady=5)

refresh_list()

root.mainloop()
