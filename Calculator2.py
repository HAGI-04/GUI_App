import tkinter as tk
from math import *

def click(key):
    if key == "=":
        try:
            expression = display.get()
            result = eval(expression)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "エラー")
    elif key == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, key)

def create_button(text, row, col):
    button = tk.Button(app, text=text, width=5, height=2, command=lambda: click(text))
    button.grid(row=row, column=col, padx=2, pady=2)

app = tk.Tk()
app.title("関数電卓")

display = tk.Entry(app, width=40)
display.grid(row=0, column=0, columnspan=5)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3), ("*", 1, 4),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("+", 2, 3), ("-", 2, 4),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("0", 4, 0),
    ("sin(", 4, 1), ("cos(", 4, 2), ("log(", 4, 3),
    (")", 3, 3), ("=", 3, 4), ("C", 4, 4)
]

for button in buttons:
    create_button(button[0], button[1], button[2])

app.mainloop()