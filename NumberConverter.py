import tkinter as tk

class NumberConverterApp:
    def __init__(self, master):
        self.master = master
        master.title("Number Converter")

        # 2進数、10進数、16進数の入力欄とテキストを作成
        self.binary_input = tk.Entry(master)
        self.binary_input.grid(row=0, column=1)
        self.binary_input_label = tk.Label(master, text="2進数")
        self.binary_input_label.grid(row=0, column=0)
        self.decimal_input = tk.Entry(master)
        self.decimal_input.grid(row=1, column=1)
        self.decimal_input_label = tk.Label(master, text="10進数")
        self.decimal_input_label.grid(row=1, column=0)
        self.hex_input = tk.Entry(master)
        self.hex_input.grid(row=2, column=1)
        self.hex_input_label = tk.Label(master, text="16進数")
        self.hex_input_label.grid(row=2, column=0)

        # 変換ボタンを作成
        self.binary_to_decimal_button = tk.Button(master, text="2進数→10進数/16進数", command=self.binary_to_decimal_hex)
        self.binary_to_decimal_button.grid(row=0, column=2)
        self.decimal_to_binary_button = tk.Button(master, text="10進数→2進数/16進数", command=self.decimal_to_binary_hex)
        self.decimal_to_binary_button.grid(row=1, column=2)
        self.hex_to_decimal_button = tk.Button(master, text="16進数→2進数/10進数", command=self.hex_to_binary_decimal)
        self.hex_to_decimal_button.grid(row=2, column=2)

        # 削除ボタンを作成
        self.clear_button = tk.Button(master, text="削除", command=self.clear_all)
        self.clear_button.grid(row=3, column=1)

    def binary_to_decimal_hex(self):
        binary = self.binary_input.get()
        decimal = int(binary, 2)
        hex = format(decimal, "X")
        self.decimal_input.delete(0, tk.END)
        self.decimal_input.insert(0, str(decimal))
        self.hex_input.delete(0, tk.END)
        self.hex_input.insert(0, hex)
        self.binary_input.delete(0, tk.END)
        self.binary_input.insert(0, binary)

    def decimal_to_binary_hex(self):
        decimal = self.decimal_input.get()
        binary = bin(int(decimal))[2:]
        hex = format(int(decimal), "X")
        self.binary_input.delete(0, tk.END)
        self.binary_input.insert(0, binary)
        self.hex_input.delete(0, tk.END)
        self.hex_input.insert(0, hex)
        self.decimal_input.delete(0, tk.END)
        self.decimal_input.insert(0, decimal)

    def hex_to_binary_decimal(self):
        hex = self.hex_input.get()
        decimal = int(hex, 16)
        binary = bin(decimal)[2:]
        self.binary_input.delete(0, tk.END)
        self.binary_input.insert(0, binary)
        self.decimal_input.delete(0, tk.END)
        self.decimal_input.insert(0, str(decimal))
        self.hex_input.delete(0, tk.END)
        self.hex_input.insert(0, hex)

    def clear_all(self):
        # 入力欄と出力欄の内容をクリア
        self.binary_input.delete(0, tk.END)
        self.decimal_input.delete(0, tk.END)
        self.hex_input.delete(0, tk.END)

root = tk.Tk()
app = NumberConverterApp(root)
root.mainloop()