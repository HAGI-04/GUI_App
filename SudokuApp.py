import tkinter as tk
import random
from sudoku import Sudoku

class SudokuApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sudoku")
        self.geometry("450x450")
        self.create_widgets()
        self.new_board()

    def create_widgets(self):
        self.cells = []

        for i in range(9):
            row = []
            for j in range(9):
                cell = tk.Entry(self, width=3, font=("Helvetica", 20), justify="center")
                cell.grid(row=i, column=j, padx=3, pady=3)
                row.append(cell)
            self.cells.append(row)

        check_button = tk.Button(self, text="Check", command=self.check_solution)
        check_button.grid(row=9, column=0, columnspan=3, sticky="w", padx=3, pady=3)

        clear_button = tk.Button(self, text="Clear", command=self.clear_board)
        clear_button.grid(row=9, column=3, columnspan=3, padx=3, pady=3)

        new_game_button = tk.Button(self, text="New Game", command=self.new_board)
        new_game_button.grid(row=9, column=6, columnspan=3, sticky="e", padx=3, pady=3)

    def new_board(self):
        puzzle = Sudoku(level='easy').new().board
        for i in range(9):
            for j in range(9):
                value = puzzle[i][j]
                self.cells[i][j].delete(0, "end")
                if value != 0:
                    self.cells[i][j].insert(0, str(value))
                    self.cells[i][j].config(state="readonly", disabledbackground="white")
                else:
                    self.cells[i][j].config(state="normal")

    def check_solution(self):
        board = []

        for i in range(9):
            row = []
            for j in range(9):
                try:
                    value = int(self.cells[i][j].get())
                except ValueError:
                    value = 0
                row.append(value)
            board.append(row)

        solution = Sudoku(board).solve()
        if solution:
            self.show_message("Success", "Correct solution!")
        else:
            self.show_message("Error", "Incorrect solution. Please try again.")

    def clear_board(self):
        for i in range(9):
            for j in range(9):
                if self.cells[i][j]["state"] != "readonly":
                    self.cells[i][j].delete(0, "end")

    def show_message(self, title, message):
        messagebox = tk.messagebox.showinfo(title, message)

if __name__ == "__main__":
    app = SudokuApp()
    app.mainloop()