import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())

        if strength_var.get() == "":
            messagebox.showwarning("⚠️ Warning", "Select strength!")
            return

        if strength_var.get() == "Weak":
            chars = string.ascii_lowercase
        elif strength_var.get() == "Medium":
            chars = string.ascii_letters + string.digits
        else:
            chars = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(random.choice(chars) for _ in range(length))
        result_var.set(password)

    except:
        messagebox.showerror("❌ Error", "Enter valid length!")

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(result_var.get())
    messagebox.showinfo("✅ Copied", "Password copied!")

def show_password():
    result_entry.config(show="")

def hide_password():
    result_entry.config(show="*")

# GUI
root = tk.Tk()
root.title("🛡 My Guard")
root.geometry("420x400")
root.config(bg="#ffe4e6")

# Title
tk.Label(root, text="🛡 My Guard 💖", font=("Arial", 18, "bold"),
         bg="#ffe4e6", fg="#be123c").pack(pady=10)

# Length
tk.Label(root, text="🔢 Enter Length:", bg="#ffe4e6", fg="#9f1239",
         font=("Arial", 11)).pack()
length_entry = tk.Entry(root, bg="#fff1f2", fg="#111",
                        relief="flat", justify="center", font=("Arial", 11))
length_entry.pack(pady=5)

# Strength
strength_var = tk.StringVar()
tk.Label(root, text="🔒 Select Strength:", bg="#ffe4e6", fg="#9f1239",
         font=("Arial", 11)).pack(pady=5)

tk.Radiobutton(root, text="😌 Weak", variable=strength_var, value="Weak",
               bg="#ffe4e6", fg="#9f1239", selectcolor="#ffe4e6",
               font=("Arial", 10)).pack()

tk.Radiobutton(root, text="🙂 Medium", variable=strength_var, value="Medium",
               bg="#ffe4e6", fg="#9f1239", selectcolor="#ffe4e6",
               font=("Arial", 10)).pack()

tk.Radiobutton(root, text="😎 Strong", variable=strength_var, value="Strong",
               bg="#ffe4e6", fg="#9f1239", selectcolor="#ffe4e6",
               font=("Arial", 10)).pack()

# Buttons
tk.Button(root, text="✨ Generate Password", command=generate_password,
          bg="#fb7185", fg="white",
          font=("Arial", 11, "bold"),
          padx=10, pady=5,
          activebackground="#f43f5e").pack(pady=10)

tk.Button(root, text="📋 Copy Password", command=copy_password,
          bg="#fda4af", fg="#7f1d1d",
          font=("Arial", 11, "bold"),
          padx=10, pady=5,
          activebackground="#fb7185").pack(pady=5)

# Result
result_var = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result_var,
                        font=("Arial", 12),
                        width=30, show="*",
                        bg="#fff1f2", fg="#111",
                        relief="flat", justify="center")
result_entry.pack(pady=10)

# Show / Hide buttons
btn_frame = tk.Frame(root, bg="#ffe4e6")
btn_frame.pack()

tk.Button(btn_frame, text="👁 Show", command=show_password,
          bg="#fecdd3", fg="#7f1d1d",
          font=("Arial", 11, "bold"),
          padx=8, pady=4).pack(side="left", padx=5)

tk.Button(btn_frame, text="🙈 Hide", command=hide_password,
          bg="#fecdd3", fg="#7f1d1d",
          font=("Arial", 11, "bold"),
          padx=8, pady=4).pack(side="left", padx=5)

# Run
root.mainloop()