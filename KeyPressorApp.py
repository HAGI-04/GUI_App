import tkinter as tk
from tkinter import ttk
import keyboard
from pynput.mouse import Button, Controller as MouseController
import time
import threading


class KeyPresserApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Key Presser")

        self.frame = ttk.Frame(self, padding=10)
        self.frame.grid(row=0, column=0, sticky=tk.W+tk.E+tk.N+tk.S)

        self.mouse = MouseController()

        self._create_widgets()

        self.key_press_enabled = False
        self.key = ""
        self.interval = 0

        self._bind_key_toggle()

    def _create_widgets(self):
        self.key_label = ttk.Label(self.frame, text="Key/Button:")
        self.key_label.grid(row=0, column=0, sticky=tk.W)

        self.available_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'enter', 'space', 'shift', 'ctrl', 'alt', 'left_click', 'right_click', 'middle_click']
        self.key_combobox = ttk.Combobox(self.frame, values=self.available_keys)
        self.key_combobox.grid(row=0, column=1)

        self.interval_label = ttk.Label(self.frame, text="Interval (ms):")
        self.interval_label.grid(row=1, column=0, sticky=tk.W)
        self.interval_entry = ttk.Entry(self.frame)
        self.interval_entry.grid(row=1, column=1)

        self.status_label = ttk.Label(self.frame, text="OFF", font=("Helvetica", 24))
        self.status_label.grid(row=0, column=2, rowspan=2, padx=10, sticky=tk.W+tk.E+tk.N+tk.S)

    def _bind_key_toggle(self):
        keyboard.add_hotkey("f12", self.toggle_key_press)

    def toggle_key_press(self):
        self.key_press_enabled = not self.key_press_enabled
        self.status_label["text"] = "ON" if self.key_press_enabled else "OFF"

        if self.key_press_enabled:
            self.key = self.key_combobox.get()
            self.interval = float(self.interval_entry.get()) / 1000
            threading.Thread(target=self.start_key_press, daemon=True).start()

    def start_key_press(self):
        while self.key_press_enabled:
            if self.key == "left_click":
                self.mouse.press(Button.left)
                time.sleep(self.interval)
                self.mouse.release(Button.left)
            elif self.key == "right_click":
                self.mouse.press(Button.right)
                time.sleep(self.interval)
                self.mouse.release(Button.right)
            elif self.key == "middle_click":
                self.mouse.press(Button.middle)
                time.sleep(self.interval)
                self.mouse.release(Button.middle)
            else:
                keyboard.press(self.key)
                time.sleep(self.interval)
                keyboard.release(self.key)


if __name__ == "__main__":
    app = KeyPresserApp()
    app.mainloop()