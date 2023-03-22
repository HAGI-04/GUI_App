import tkinter as tk

def on_key(event):
    display_text.set(f"キーが押されました: {event.keysym}")

def on_click(event):
    display_text.set(f"マウスがクリックされました: 座標({event.x}, {event.y})")

def on_move(event):
    display_text.set(f"マウスが移動されました: 座標({event.x}, {event.y})")

root = tk.Tk()
root.title("入力検出アプリ")

display_text = tk.StringVar()
display_label = tk.Label(root, textvariable=display_text, font=("Arial", 16))
display_label.pack(padx=10, pady=10)

frame = tk.Frame(root, width=300, height=200, bg="lightblue")
frame.pack(padx=10, pady=10)

frame.bind("<Key>", on_key)
frame.bind("<Button-1>", on_click)
frame.bind("<Motion>", on_move)

frame.focus_set()

root.mainloop()