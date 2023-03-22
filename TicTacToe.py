import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.root = tk.Tk()
        self.root.title("3目並べ")
        self.create_board()
        self.status = tk.Label(self.root, text=f"現在の手番: {self.player}", font=("Helvetica", 14))
        self.status.grid(row=3, columnspan=3)
        self.game_over = False
    
    def create_board(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text=" ", font=("Helvetica", 20), 
                                   width=4, height=2, command=lambda row=row, col=col: self.click_button(row, col))
                button.grid(row=row, column=col)
    
    def click_button(self, row, col):
        if self.game_over:
            return
        button = self.root.grid_slaves(row=row, column=col)[0]
        if button["text"] == " ":
            button["text"] = self.player
            self.board[row][col] = self.player
            if self.check_win():
                self.status["text"] = f"{self.player}が勝ちました！"
                self.game_over = True
            elif self.check_tie():
                self.status["text"] = "引き分けです。"
                self.game_over = True
            else:
                self.player = "O" if self.player == "X" else "X"
                self.status["text"] = f"現在の手番: {self.player}"
    
    def check_win(self):
        # 横のラインをチェック
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != " ":
                return True
        # 縦のラインをチェック
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                return True
        # 斜めのラインをチェック
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        return False
    
    def check_tie(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == " ":
                    return False
        return True
    
    def reset_board(self):
        for row in range(3):
            for col in range(3):
                button = self.root.grid_slaves(row=row, column=col)[0]
                button["text"] = " "
                self.board[row][col] = " "
        self.player = "X"
        self.status["text"] = f"現在の手番: {self.player}"
        self.game_over = False
    
    def play(self):
        self.root.mainloop()

game = TicTacToe()
game.play()