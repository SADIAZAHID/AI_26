import tkinter as tk
import random
import json
import os

# --- Configuration & Constants ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE = 25
SAVE_FILE = "snake_data.json"

# Nord Color Palette
COLORS = {
    "bg": "#ECEFF4",
    "canvas": "#FFFFFF",
    "snake": "#5E81AC",
    "food": "#BF616A",
    "text": "#2E3440",
    "border": "#D8DEE9"
}


class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Snake Pro")
        self.root.configure(bg=COLORS["bg"])

        # --- UI Layout ---
        self.main_frame = tk.Frame(root, bg=COLORS["bg"])
        self.main_frame.pack(padx=20, pady=20)

        self.canvas = tk.Canvas(self.main_frame, width=SCREEN_WIDTH, height=SCREEN_HEIGHT,
                                bg=COLORS["canvas"], highlightthickness=1,
                                highlightbackground=COLORS["border"])
        self.canvas.pack(side=tk.LEFT)

        self.sidebar = tk.Frame(self.main_frame, bg=COLORS["bg"], width=150)
        self.sidebar.pack(side=tk.RIGHT, fill=tk.Y, padx=20)

        self.score_label = tk.Label(self.sidebar, text="Score: 0", font=("Helvetica", 18, "bold"), bg=COLORS["bg"],
                                    fg=COLORS["text"])
        self.score_label.pack(pady=10)

        self.high_score_label = tk.Label(self.sidebar, text="Best: 0", font=("Helvetica", 12), bg=COLORS["bg"],
                                         fg=COLORS["text"])
        self.high_score_label.pack()

        # --- Game Logic ---
        self.high_score = self.load_high_score()
        self.high_score_label.config(text=f"Best: {self.high_score}")
        self.reset_game_state()

        self.root.bind("<KeyPress>", self.handle_keypress)
        self.show_menu()

    def load_high_score(self):
        if os.path.exists(SAVE_FILE):
            try:
                with open(SAVE_FILE, 'r') as f:
                    return json.load(f).get("high_score", 0)
            except:
                return 0
        return 0

    def save_high_score(self):
        with open(SAVE_FILE, 'w') as f: json.dump({"high_score": self.high_score}, f)

    def reset_game_state(self):
        self.snake = [(10, 10), (9, 10), (8, 10)]
        self.direction = (1, 0)
        self.food = (random.randint(0, 23), random.randint(0, 23))
        self.score = 0
        self.running = False
        self.paused = False
        self.speed = 150

    def show_menu(self):
        self.canvas.delete("all")
        self.canvas.create_text(300, 280, text="SNAKE PRO", font=("Helvetica", 30, "bold"), fill=COLORS["text"])
        self.canvas.create_text(300, 320, text="Press SPACE to Start", font=("Helvetica", 14), fill=COLORS["text"])

    def handle_keypress(self, event):
        key = event.keysym.lower()
        if key == "space":
            if not self.running:
                self.start_game()
            else:
                self.paused = not self.paused

        mapping = {'up': (0, -1), 'down': (0, 1), 'left': (-1, 0), 'right': (1, 0),
                   'w': (0, -1), 's': (0, 1), 'a': (-1, 0), 'd': (1, 0)}
        if key in mapping:
            new_dir = mapping[key]
            if (new_dir[0] * -1, new_dir[1] * -1) != self.direction: self.direction = new_dir

    def start_game(self):
        self.reset_game_state()
        self.running = True
        self.game_loop()

    def game_loop(self):
        if self.running and not self.paused:
            head = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])
            if (head[0] < 0 or head[0] >= 24 or head[1] < 0 or head[1] >= 24 or head in self.snake):
                self.running = False
            else:
                self.snake.insert(0, head)
                if head == self.food:
                    self.score += 10
                    self.score_label.config(text=f"Score: {self.score}")
                    self.speed = max(50, self.speed - 5)
                    self.food = (random.randint(0, 23), random.randint(0, 23))
                else:
                    self.snake.pop()
                self.render()
            self.root.after(self.speed, self.game_loop)
        elif not self.running and self.score > 0:
            self.game_over()

    def render(self):
        self.canvas.delete("all")
        fx, fy = self.food
        self.canvas.create_oval(fx * GRID_SIZE + 2, fy * GRID_SIZE + 2, (fx + 1) * GRID_SIZE - 2,
                                (fy + 1) * GRID_SIZE - 2, fill=COLORS["food"], outline="")
        for sx, sy in self.snake:
            self.canvas.create_rectangle(sx * GRID_SIZE + 1, sy * GRID_SIZE + 1, (sx + 1) * GRID_SIZE - 1,
                                         (sy + 1) * GRID_SIZE - 1, fill=COLORS["snake"], outline=COLORS["bg"])

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
            self.high_score_label.config(text=f"Best: {self.high_score}")
        self.canvas.create_text(300, 300, text="GAME OVER", font=("Helvetica", 30, "bold"), fill=COLORS["food"])


if __name__ == "__main__":
    root = tk.Tk()
    SnakeGame(root)
    root.mainloop()