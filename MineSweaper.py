import tkinter as tk
import random

class Minesweeper:
    def __init__(self, master, rows=10, columns=10, mines=10):
        self.master = master
        self.rows = rows
        self.columns = columns
        self.mines = mines
        self.board = [[0] * columns for _ in range(rows)]
        self.buttons = [[None] * columns for _ in range(rows)]
        self.create_board()
        self.create_buttons()

    def create_board(self):
        mine_positions = set()
        while len(mine_positions) < self.mines:
            mine_positions.add((random.randint(0, self.rows - 1), random.randint(0, self.columns - 1)))

        for row, col in mine_positions:
            self.board[row][col] = -1

            for r in range(row - 1, row + 2):
                for c in range(col - 1, col + 2):
                    if 0 <= r < self.rows and 0 <= c < self.columns and self.board[r][c] != -1:
                        self.board[r][c] += 1

    def create_buttons(self):
        for row in range(self.rows):
            for col in range(self.columns):
                button = tk.Button(self.master, text="", width=3, height=2, command=lambda r=row, c=col: self.button_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def button_click(self, row, col):
        if self.board[row][col] == -1:
            self.game_over()
        elif self.board[row][col] > 0:
            self.buttons[row][col].config(text=self.board[row][col], state=tk.DISABLED, relief=tk.SUNKEN)
        else:
            self.reveal_empty(row, col)

        self.check_win()

    def reveal_empty(self, row, col):
        if self.buttons[row][col]["state"] == tk.DISABLED:
            return

        self.buttons[row][col].config(text=self.board[row][col], state=tk.DISABLED, relief=tk.SUNKEN)

        if self.board[row][col] == 0:
            for r in range(row - 1, row + 2):
                for c in range(col - 1, col + 2):
                    if 0 <= r < self.rows and 0 <= c < self.columns:
                        self.reveal_empty(r, c)

    def check_win(self):
        safe_cells = self.rows * self.columns - self.mines
        revealed_cells = 0
        for row in range(self.rows):
            for col in range(self.columns):
                if self.buttons[row][col]["state"] == tk.DISABLED:
                    revealed_cells += 1

        if revealed_cells == safe_cells:
            self.master.title("You Win!")
            for row in range(self.rows):
                for col in range(self.columns):
                    self.buttons[row][col].config(state=tk.DISABLED)

    def game_over(self):
        for row in range(self.rows):
            for col in range(self.columns):
                if self.board[row][col] == -1:
                    self.buttons[row][col].config(text="*", state=tk.DISABLED)

        self.master.title("Game Over!")

    def restart(self):
        for row in range(self.rows):
            for col in range(self.columns):
                self.buttons[row][col].destroy()

        self.board = [[0] * self.columns for _ in range(self.rows)]
        self.buttons = [[None] * self.columns for _ in range(self.rows)]
        self.create_board()
        self.create_buttons()
        self.master.title("Minesweeper")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Minesweeper")
    game = Minesweeper(root)

    restart_button = tk.Button(root, text="Restart", command=game.restart)
    restart_button.grid(row=game.rows, column=0, columnspan=game.columns, sticky=tk.W+tk.E)

    root.mainloop()