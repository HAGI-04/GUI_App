import tkinter as tk

class HanoiGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("ハノイの塔ゲーム")
        self.geometry("800x400")

        self.canvas = tk.Canvas(self, width=800, height=300, bg="white")
        self.canvas.pack()

        self.start_button = tk.Button(self, text="ゲーム開始", command=self.start_game)
        self.start_button.pack()

        self.tower_buttons = [
            tk.Button(self, text="タワー1", command=lambda: self.handle_click(0)),
            tk.Button(self, text="タワー2", command=lambda: self.handle_click(1)),
            tk.Button(self, text="タワー3", command=lambda: self.handle_click(2)),
        ]

        for i, button in enumerate(self.tower_buttons):
            button.place(x=250 * i + 215, y=30)

        self.selected_disk_label = tk.Label(self, text="")
        self.selected_disk_label.pack()

        self.disk_colors = ["red", "orange", "yellow", "green", "blue"]

        self.towers = [[] for _ in range(3)]
        self.selected_tower = None

    def start_game(self):
        self.canvas.delete("all")
        self.towers = [[5, 4, 3, 2, 1], [], []]
        self.selected_tower = None
        self.selected_disk_label.config(text="")
        self.draw_towers()

    def draw_towers(self):
        self.canvas.delete("disk")
        self.canvas.create_rectangle(150, 250, 750, 260, fill="black")  # 線の範囲を調整

        for i in range(3):
            x = 250 * i + 250
            self.canvas.create_rectangle(x - 10, 50, x + 10, 250, fill="black")

            for j, disk in enumerate(self.towers[i]):
                self.draw_disk(x, 250 - 20 * j, 20 * disk, self.disk_colors[disk - 1])  # ディスクの幅を小さくする

    def draw_disk(self, x, y, width, color):
        self.canvas.create_rectangle(x - width, y - 10, x + width, y + 10, fill=color, tags="disk")

    def handle_click(self, tower_index):
        if self.selected_tower is None:
            self.selected_tower = tower_index
            if self.towers[tower_index]:
                self.selected_disk_label.config(text=f"選択中のディスク: {self.towers[tower_index][-1]}")
            else:
                self.selected_tower = None
        else:
            self.move_disk(self.selected_tower, tower_index)
            self.selected_tower = None
            self.selected_disk_label.config(text="")
            self.draw_towers()

    def move_disk(self, from_tower, to_tower):
        if not self.towers[from_tower]:
            return

        disk = self.towers[from_tower][-1]
        target_tower = self.towers[to_tower][-1] if self.towers[to_tower] else float("inf")

        if disk < target_tower:
            self.towers[from_tower].pop()
            self.towers[to_tower].append(disk)

if __name__ == "__main__":
    game = HanoiGame()
    game.mainloop()