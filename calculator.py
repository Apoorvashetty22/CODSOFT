import tkinter as tk
import math

history = []
dark_mode = False
last_answer = 0

# ---------------- BASIC FUNCTIONS ----------------
def click(value):
    entry.insert(tk.END, value)

def backspace():
    entry.delete(len(entry.get())-1, tk.END)

def clear():
    entry.delete(0, tk.END)

def ans():
    entry.insert(tk.END, str(last_answer))

def calculate():
    global last_answer
    try:
        expression = entry.get()
        result = eval(expression)

        last_answer = result

        history.append(expression + " = " + str(result))
        if len(history) > 10:
            history.pop(0)

        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# ---------------- SCIENTIFIC FUNCTIONS ----------------
def percent():
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, value / 100)
    except:
        entry.insert(0,"Error")

def sqrt():
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, math.sqrt(value))
    except:
        entry.insert(0,"Error")

def power():
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, value**2)
    except:
        entry.insert(0,"Error")

def sin():
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, math.sin(math.radians(value)))
    except:
        entry.insert(0,"Error")

def cos():
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, math.cos(math.radians(value)))
    except:
        entry.insert(0,"Error")

def tan():
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, math.tan(math.radians(value)))
    except:
        entry.insert(0,"Error")

# ---------------- SCIENTIFIC WINDOW ----------------
def open_scientific():
    sci = tk.Toplevel(root)
    sci.title("Scientific Functions")
    sci.geometry("260x250")
    sci.configure(bg="#F3F0FF")

    buttons = [
        ("sin", sin),
        ("cos", cos),
        ("tan", tan),
        ("√", sqrt),
        ("x²", power),
        ("%", percent)
    ]

    for i,(name,cmd) in enumerate(buttons):
        b = tk.Button(
            sci,
            text=name,
            font=("Segoe UI",12,"bold"),
            bg="#FFADAD",
            fg="black",
            width=8,
            height=2,
            relief="ridge",
            bd=2,
            command=cmd
        )
        b.grid(row=i//2,column=i%2,padx=10,pady=10, sticky="nsew")

# ---------------- HISTORY ----------------
def show_history():
    win = tk.Toplevel(root)
    win.title("History")
    win.geometry("300x320")
    win.transient(root)

    if dark_mode:
        bg_color = "#1C1C1C"
        fg_color = "white"
        list_bg = "#2C2C2C"
    else:
        bg_color = "#F3F0FF"
        fg_color = "black"
        list_bg = "#E9ECEF"

    win.configure(bg=bg_color)
    listbox = tk.Listbox(win, font=("Segoe UI",12), bg=list_bg, fg=fg_color)
    listbox.pack(fill="both", expand=True, padx=10, pady=10)

    for item in history:
        listbox.insert(tk.END,item)

# ---------------- THEME ----------------
def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        root.configure(bg="#1C1C1C")
        entry.configure(bg="#2C2C2C",fg="white")
    else:
        root.configure(bg="#F3F0FF")
        entry.configure(bg="#E9ECEF",fg="black")

# ---------------- HOVER ----------------
def on_enter(e):
    e.widget['bg'] = "#CDB4DB"

def on_leave(e, color):
    e.widget['bg'] = color

# ---------------- KEYBOARD ----------------
def key_input(event):
    if event.keysym == "Return":
        calculate()
    elif event.keysym == "BackSpace":
        backspace()

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Apoorva Smart Calculator")
root.geometry("380x580")
root.configure(bg="#F3F0FF")
root.resizable(True, True)  # <-- now maximizable
root.bind("<Key>", key_input)

# ---------------- DISPLAY WITH BACKSPACE ----------------
display_frame = tk.Frame(root, bg="#F3F0FF")
display_frame.pack(fill="both", padx=12, pady=15)

entry = tk.Entry(
    display_frame,
    font=("Segoe UI",26,"bold"),
    bg="#E9ECEF",
    fg="black",
    bd=0,
    justify="right"
)
entry.pack(side="left", fill="both", expand=True, ipady=12)

back_btn = tk.Button(
    display_frame,
    text="⌫",
    font=("Segoe UI",14,"bold"),
    bg="#FFADAD",
    fg="black",
    width=3,
    relief="ridge",
    bd=2,
    command=backspace
)
back_btn.pack(side="right", padx=5)

# ---------------- BUTTON FRAME ----------------
frame = tk.Frame(root, bg="#F3F0FF")
frame.pack(fill="both", expand=True)

btn_style = {"font":("Segoe UI",14,"bold"), "width":5, "height":2, "bd":0, "relief":"flat"}
number_color = "#B8C0FF"
operator_color = "#FFADAD"
equal_color = "#80ED99"

buttons = [
("7","8","9","/"),
("4","5","6","*"),
("1","2","3","-"),
("ANS","0",".","+")
]

for r,row in enumerate(buttons):
    for c,char in enumerate(row):
        if char == "ANS":
            color = operator_color
            cmd = ans
        elif char in "+-*/":
            color = operator_color
            cmd = lambda ch=char: click(ch)
        else:
            color = number_color
            cmd = lambda ch=char: click(ch)

        b = tk.Button(frame, text=char, bg=color, fg="black", command=cmd, **btn_style)
        b.grid(row=r,column=c,padx=8,pady=8, ipadx=10, ipady=8, sticky="nsew")
        b.bind("<Enter>", on_enter)
        b.bind("<Leave>", lambda e, col=color: on_leave(e,col))

# Make grid expandable
for i in range(4):
    frame.columnconfigure(i, weight=1)
for i in range(4):
    frame.rowconfigure(i, weight=1)

# ---------------- EQUAL BUTTON ----------------
equal_btn = tk.Button(
    root,
    text="=",
    font=("Segoe UI",16,"bold"),
    bg=equal_color,
    fg="black",
    width=20,
    height=2,
    relief="ridge",
    bd=3,
    command=calculate
)
equal_btn.pack(pady=8, fill="x", padx=12)

# ---------------- BOTTOM BUTTONS ----------------
bottom = tk.Frame(root, bg="#F3F0FF")
bottom.pack(pady=15, fill="x")

sci_btn = tk.Button(bottom, text="SCI", bg="#FFADAD", fg="black",
                    font=("Segoe UI",12,"bold"), command=open_scientific,
                    width=10, relief="ridge", bd=2)
sci_btn.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

clear_btn = tk.Button(bottom, text="CLEAR", bg="#FF6B6B", fg="white",
                      font=("Segoe UI",12,"bold"), command=clear,
                      width=10, relief="ridge", bd=2)
clear_btn.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

history_btn = tk.Button(bottom, text="HISTORY", bg="#90DBF4", fg="black",
                        font=("Segoe UI",12,"bold"), command=show_history,
                        width=10, relief="ridge", bd=2)
history_btn.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

theme_btn = tk.Button(bottom, text="THEME", bg="#CDB4DB", fg="black",
                      font=("Segoe UI",12,"bold"), command=toggle_theme,
                      width=10, relief="ridge", bd=2)
theme_btn.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

# Make bottom buttons expand with window
bottom.columnconfigure(0, weight=1)
bottom.columnconfigure(1, weight=1)

root.mainloop()