import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Colorful Todo List")
        self.tasks = []
        self.task_listbox = tk.Listbox(self.root, height=10, width=50)
        self.task_listbox.pack(pady=10)
        self.task_entry = tk.Entry(self.root, width=50)
        self.task_entry.pack()
        add_task_btn = tk.Button(self.root, text="Add Task", command=self.add_task)
        add_task_btn.pack(pady=10)
        remove_task_btn = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        remove_task_btn.pack()
        self.colors = ['cyan', 'magenta']

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def remove_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove!")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks, start=1):
            color = self.colors[index % len(self.colors)]
            self.task_listbox.insert(tk.END, f"{index}. {task}")
            self.task_listbox.itemconfig(index-1, bg=color)

if __name__ == "__main__":
    root = (link unavailable)()
    app = TodoApp(root)
    root.mainloop()
