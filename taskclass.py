import json
from datetime import datetime

class Task:
    def __init__(self, name, description, due_date):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.status = "Pending"

    def mark_completed(self):
        self.status = "Completed"

    def __repr__(self):
        return f"{self.name} - {self.status} (Due: {self.due_date})"
def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as f:
            tasks = json.load(f)
            return [Task(**task) for task in tasks]
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as f:
        json.dump([task.__dict__ for task in tasks], f)

def add_task(tasks, name, description, due_date):
    task = Task(name, description, due_date)
    tasks.append(task)
    save_tasks(tasks)

def delete_task(tasks, name):
    tasks = [task for task in tasks if task.name != name]
    save_tasks(tasks)

def mark_completed(tasks, name):
    for task in tasks:
        if task.name == name:
            task.mark_completed()
            break
    save_tasks(tasks)

def list_tasks(tasks):
    for task in tasks:
        print(task)


def cli():
    tasks = load_tasks()

    while True:
        print("\nTask Manager CLI")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(tasks, name, description, due_date)

        elif choice == "2":
            name = input("Enter task name to delete: ")
            delete_task(tasks, name)

        elif choice == "3":
            name = input("Enter task name to mark as completed: ")
            mark_completed(tasks, name)

        elif choice == "4":
            list_tasks(tasks)

        elif choice == "5":
            break

        else:
            print("Invalid choice! Please try again.")
import tkinter as tk
from tkinter import messagebox

class TaskManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.tasks = load_tasks()

        # Setup UI elements
        self.name_label = tk.Label(root, text="Task Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.description_label = tk.Label(root, text="Task Description:")
        self.description_label.pack()
        self.description_entry = tk.Entry(root)
        self.description_entry.pack()

        self.due_date_label = tk.Label(root, text="Due Date (YYYY-MM-DD):")
        self.due_date_label.pack()
        self.due_date_entry = tk.Entry(root)
        self.due_date_entry.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root)
        self.task_listbox.pack()
        self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def add_task(self):
        name = self.name_entry.get()
        description = self.description_entry.get()
        due_date = self.due_date_entry.get()

        if name and description and due_date:
            add_task(self.tasks, name, description, due_date)
            self.update_task_list()
        else:
            messagebox.showwarning("Input Error", "All fields must be filled in!")

    def delete_task(self):
        selected_task = self.task_listbox.get(tk.ACTIVE)
        if selected_task:
            name = selected_task.split(" - ")[0]
            delete_task(self.tasks, name)
            self.update_task_list()

    def mark_completed(self):
        selected_task = self.task_listbox.get(tk.ACTIVE)
        if selected_task:
            name = selected_task.split(" - ")[0]
            mark_completed(self.tasks, name)
            self.update_task_list()

# Run the GUI
root = tk.Tk()
app = TaskManagerGUI(root)
root.mainloop()
