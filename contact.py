import tkinter as tk
from tkinter import messagebox

contacts = []

# ---------------- Refresh List ----------------
def refresh_list():
    listbox.delete(0, tk.END)

    # ✅ Alphabetical sorting
    sorted_contacts = sorted(contacts, key=lambda x: x[0].lower())

    for i, contact in enumerate(sorted_contacts, start=1):
        listbox.insert(tk.END, f"{i}. {contact[0]} | {contact[1]}")

# ---------------- Add Window ----------------
def open_add_window():
    window = tk.Toplevel(root)
    window.title("Add Contact")
    window.geometry("320x330")
    window.configure(bg="#F3E5F5")

    tk.Label(window, text="Add Contact",
             font=("Segoe UI", 13, "bold"),
             bg="#F3E5F5", fg="#6A1B9A").pack(pady=8)

    tk.Label(window, text="Name", bg="#F3E5F5").pack()
    name = tk.Entry(window, width=28)
    name.pack()

    tk.Label(window, text="Phone", bg="#F3E5F5").pack()
    phone = tk.Entry(window, width=28)
    phone.pack()

    tk.Label(window, text="Email", bg="#F3E5F5").pack()
    email = tk.Entry(window, width=28)
    email.pack()

    tk.Label(window, text="Address", bg="#F3E5F5").pack()
    address = tk.Entry(window, width=28)
    address.pack()

    def save():
        if name.get().strip() == "" or phone.get().strip() == "":
            messagebox.showwarning("Warning", "Name and Phone required")
            return

        # ✅ Auto Capital
        contacts.append([
            name.get().title(),
            phone.get(),
            email.get(),
            address.get()
        ])

        refresh_list()
        window.destroy()

    tk.Button(window, text="Save",
              bg="#8E24AA", fg="white",
              width=14, command=save).pack(pady=12)

# ---------------- Update Window ----------------
def open_update_window():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Select a contact first")
        return

    index = selected[0]

    # Use sorted list to match display order
    sorted_contacts = sorted(contacts, key=lambda x: x[0].lower())
    selected_contact = sorted_contacts[index]
    real_index = contacts.index(selected_contact)

    window = tk.Toplevel(root)
    window.title("Update Contact")
    window.geometry("320x330")
    window.configure(bg="#F3E5F5")

    tk.Label(window, text="Update Contact",
             font=("Segoe UI", 13, "bold"),
             bg="#F3E5F5", fg="#6A1B9A").pack(pady=8)

    tk.Label(window, text="Name", bg="#F3E5F5").pack()
    name = tk.Entry(window, width=28)
    name.pack()
    name.insert(0, contacts[real_index][0])

    tk.Label(window, text="Phone", bg="#F3E5F5").pack()
    phone = tk.Entry(window, width=28)
    phone.pack()
    phone.insert(0, contacts[real_index][1])

    tk.Label(window, text="Email", bg="#F3E5F5").pack()
    email = tk.Entry(window, width=28)
    email.pack()
    email.insert(0, contacts[real_index][2])

    tk.Label(window, text="Address", bg="#F3E5F5").pack()
    address = tk.Entry(window, width=28)
    address.pack()
    address.insert(0, contacts[real_index][3])

    def update():
        contacts[real_index] = [
            name.get().title(),   # ✅ Auto Capital
            phone.get(),
            email.get(),
            address.get()
        ]
        refresh_list()
        window.destroy()

    tk.Button(window, text="Update",
              bg="#7B1FA2", fg="white",
              width=14, command=update).pack(pady=12)

# ---------------- Search Window ----------------
def open_search_window():
    window = tk.Toplevel(root)
    window.title("Search Contact")
    window.geometry("280x180")
    window.configure(bg="#F3E5F5")

    tk.Label(window, text="Search Contact",
             font=("Segoe UI", 13, "bold"),
             bg="#F3E5F5", fg="#6A1B9A").pack(pady=8)

    tk.Label(window, text="Enter Name or Phone", bg="#F3E5F5").pack()
    search = tk.Entry(window, width=22)
    search.pack()

    def do_search():
        value = search.get().strip().lower()

        if value == "":
            messagebox.showwarning("Warning", "Enter something to search")
            return

        listbox.delete(0, tk.END)
        found = False

        sorted_contacts = sorted(contacts, key=lambda x: x[0].lower())

        for i, contact in enumerate(sorted_contacts, start=1):
            # ✅ Proper partial search
            if value in contact[0].lower() or value in contact[1]:
                listbox.insert(tk.END, f"{i}. {contact[0]} | {contact[1]}")
                found = True

        if not found:
            messagebox.showinfo("Not Found", "Contact not found")
            refresh_list()

        window.destroy()

    tk.Button(window, text="Search",
              bg="#AB47BC", fg="white",
              width=12, command=do_search).pack(pady=12)

# ---------------- Delete ----------------
def delete_contact():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Select a contact first")
        return

    sorted_contacts = sorted(contacts, key=lambda x: x[0].lower())
    selected_contact = sorted_contacts[selected[0]]
    real_index = contacts.index(selected_contact)

    confirm = messagebox.askyesno("Confirm", "Delete selected contact?")
    if confirm:
        contacts.pop(real_index)
        refresh_list()

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("My Contact Book")
root.geometry("600x400")
root.configure(bg="#EDE7F6")

tk.Label(root,
         text="💜 My Contact Book",
         font=("Segoe UI", 16, "bold"),
         bg="#EDE7F6",
         fg="#4A148C").pack(pady=10)

left_decor = tk.Label(root,
                      text="📞\n\n💜\n\n📒\n\n✨",
                      font=("Segoe UI", 16),
                      bg="#EDE7F6",
                      fg="#BA68C8",
                      justify="center")
left_decor.place(x=5, y=120)

right_decor = tk.Label(root,
                       text="✨\n\n📱\n\n💬\n\n💜",
                       font=("Segoe UI", 16),
                       bg="#EDE7F6",
                       fg="#BA68C8",
                       justify="center")
right_decor.place(x=565, y=120)

main_frame = tk.Frame(root, bg="#EDE7F6")
main_frame.pack(pady=5)

left_frame = tk.Frame(main_frame, bg="#EDE7F6")
left_frame.grid(row=0, column=0, padx=20)

tk.Label(left_frame,
         text="Saved Contacts",
         font=("Segoe UI", 12, "bold"),
         bg="#EDE7F6",
         fg="#6A1B9A").pack(anchor="w")

listbox = tk.Listbox(left_frame,
                     width=30,
                     height=15,
                     font=("Segoe UI", 10),
                     bg="white",
                     fg="#4A148C",
                     selectbackground="#CE93D8")
listbox.pack(pady=5)

right_frame = tk.Frame(main_frame, bg="#EDE7F6")
right_frame.grid(row=0, column=1, padx=20)

tk.Button(right_frame, text="Add",
          width=12, bg="#8E24AA", fg="white",
          command=open_add_window).pack(pady=5)

tk.Button(right_frame, text="Update",
          width=12, bg="#7B1FA2", fg="white",
          command=open_update_window).pack(pady=5)

tk.Button(right_frame, text="Search",
          width=12, bg="#AB47BC", fg="white",
          command=open_search_window).pack(pady=5)

tk.Button(right_frame, text="Delete",
          width=12, bg="#BA68C8", fg="white",
          command=delete_contact).pack(pady=5)

root.mainloop()