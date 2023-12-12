import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=10)

        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=2, column=0, padx=5, pady=10)

        self.clear_button = tk.Button(root, text="Clear All", command=self.clear_tasks)
        self.clear_button.grid(row=2, column=1, padx=5, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.tasks.pop(index)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def clear_tasks(self):
        self.tasks = []
        self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

def main():
    root = tk.Tk()
    todo_app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
