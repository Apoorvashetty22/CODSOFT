import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date

tasks = []

# ---------------- Refresh Table ----------------
def refresh_table(show_list=None):

    for row in tree.get_children():
        tree.delete(row)

    data = show_list if show_list else tasks

    for i, task in enumerate(data, start=1):

        tag = ""
        if task["priority"] == "High":
            tag = "high"
        elif task["priority"] == "Medium":
            tag = "medium"
        else:
            tag = "low"

        tree.insert("", "end",
                    values=(i,
                            task["name"],
                            task["added"],
                            task["due"],
                            task["priority"],
                            task["status"]),
                    tags=(tag,))


# ---------------- Add Task ----------------
def open_add():

    win = tk.Toplevel(root)
    win.title("Add Task")
    win.geometry("320x300")
    win.configure(bg="#F3E5F5")

    tk.Label(win,text="Add Task",
             font=("Segoe UI",12,"bold"),
             bg="#F3E5F5",
             fg="#6A1B9A").pack(pady=10)

    tk.Label(win,text="Task Name",bg="#F3E5F5").pack()
    name = tk.Entry(win,width=25)
    name.pack(pady=5)

    tk.Label(win,text="Due Date",bg="#F3E5F5").pack()
    due = tk.Entry(win,width=25)
    due.pack(pady=5)

    tk.Label(win,text="Priority",bg="#F3E5F5").pack()

    priority = tk.StringVar()
    priority.set("Medium")

    tk.OptionMenu(win,priority,"High","Medium","Low").pack()

    def save():

        if name.get()=="":
            messagebox.showwarning("Warning","Enter task name")
            return

        task = {
            "name":name.get().title(),
            "added":str(date.today()),
            "due":due.get(),
            "priority":priority.get(),
            "status":"⏳ Pending"
        }

        tasks.append(task)
        refresh_table()
        win.destroy()

    tk.Button(win,text="Save",
              bg="#8E24AA",
              fg="white",
              width=12,
              command=save).pack(pady=15)


# ---------------- Update Task ----------------
def open_update():

    selected = tree.focus()

    if not selected:
        messagebox.showwarning("Warning","Select task")
        return

    index = tree.index(selected)
    task = tasks[index]

    win = tk.Toplevel(root)
    win.title("Update Task")
    win.geometry("320x300")
    win.configure(bg="#F3E5F5")

    tk.Label(win,text="Update Task",
             font=("Segoe UI",12,"bold"),
             bg="#F3E5F5",
             fg="#6A1B9A").pack(pady=10)

    tk.Label(win,text="Task Name",bg="#F3E5F5").pack()
    name = tk.Entry(win,width=25)
    name.insert(0,task["name"])
    name.pack(pady=5)

    tk.Label(win,text="Due Date",bg="#F3E5F5").pack()
    due = tk.Entry(win,width=25)
    due.insert(0,task["due"])
    due.pack(pady=5)

    tk.Label(win,text="Priority",bg="#F3E5F5").pack()

    priority = tk.StringVar()
    priority.set(task["priority"])

    tk.OptionMenu(win,priority,"High","Medium","Low").pack()

    def save():

        tasks[index] = {
            "name":name.get().title(),
            "added":task["added"],
            "due":due.get(),
            "priority":priority.get(),
            "status":task["status"]
        }

        refresh_table()
        win.destroy()

    tk.Button(win,text="Update",
              bg="#7B1FA2",
              fg="white",
              width=12,
              command=save).pack(pady=15)


# ---------------- Delete Task ----------------
def delete_task():

    selected = tree.focus()

    if not selected:
        messagebox.showwarning("Warning","Select task")
        return

    index = tree.index(selected)

    confirm = messagebox.askyesno("Confirm","Delete task?")

    if confirm:
        tasks.pop(index)
        refresh_table()


# ---------------- Mark Completed ----------------
def complete_task():

    selected = tree.focus()

    if not selected:
        messagebox.showwarning("Warning","Select task")
        return

    index = tree.index(selected)

    tasks[index]["status"] = "✔ Completed"

    refresh_table()


# ---------------- Search Task ----------------
def search_task():

    value = search_entry.get().lower()

    if value == "":
        refresh_table()
        return

    filtered = []

    for task in tasks:
        if value in task["name"].lower():
            filtered.append(task)

    if not filtered:
        messagebox.showinfo("Result","Task not found")

    refresh_table(filtered)


# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Task Manager")
root.geometry("750x420")
root.configure(bg="#EDE7F6")

tk.Label(root,
         text="💜 Task Manager",
         font=("Segoe UI",16,"bold"),
         bg="#EDE7F6",
         fg="#4A148C").pack(pady=10)

# ---------------- Search Bar ----------------
search_frame = tk.Frame(root,bg="#EDE7F6")
search_frame.pack()

search_entry = tk.Entry(search_frame,width=30)
search_entry.grid(row=0,column=0,padx=5)

tk.Button(search_frame,
          text="Search",
          bg="#AB47BC",
          fg="white",
          command=search_task).grid(row=0,column=1,padx=5)

# ---------------- Table ----------------
columns = ("No","Task","Added Date","Due Date","Priority","Status")

tree = ttk.Treeview(root,
                    columns=columns,
                    show="headings",
                    height=12)

for col in columns:
    tree.heading(col,text=col)
    tree.column(col,width=110,anchor="center")

tree.pack(pady=10)

tree.tag_configure("high",background="#F8BBD0")
tree.tag_configure("medium",background="#E1BEE7")
tree.tag_configure("low",background="#F3E5F5")

# ---------------- Buttons ----------------
frame = tk.Frame(root,bg="#EDE7F6")
frame.pack()

tk.Button(frame,text="Add",
          width=12,
          bg="#8E24AA",
          fg="white",
          command=open_add).grid(row=0,column=0,padx=5)

tk.Button(frame,text="Update",
          width=12,
          bg="#7B1FA2",
          fg="white",
          command=open_update).grid(row=0,column=1,padx=5)

tk.Button(frame,text="Complete",
          width=12,
          bg="#BA68C8",
          fg="white",
          command=complete_task).grid(row=0,column=2,padx=5)

tk.Button(frame,text="Delete",
          width=12,
          bg="#EC407A",
          fg="white",
          command=delete_task).grid(row=0,column=3,padx=5)

root.mainloop()