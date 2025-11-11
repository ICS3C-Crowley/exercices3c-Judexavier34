import tkinter as tk
from tkinter import ttk
import random

CELL = 20
COLS = 30
ROWS = 20
WIDTH = CELL * COLS
HEIGHT = CELL * ROWS
SPEED_MS = 100  # délai entre frames en ms

BG = "#000000"
SNAKE_HEAD = "#00FF00"
SNAKE_BODY = "#0077CC"
FOOD_COLOR = "#FF3333"
TEXT_COLOR = "#FFFFFF"

class SnackGame:
    def __init__(self, parent):
        # parent : frame (onglet) dans lequel on place le canvas
        self.parent = parent
        self.canvas = tk.Canvas(parent, width=WIDTH, height=HEIGHT, bg=BG)
        self.canvas.pack(side="top", fill="both", expand=True)
        self.info = tk.Label(parent, text="", fg=TEXT_COLOR, bg="#222222")
        self.info.pack(fill="x")
        self.reset()
        # binding sur la racine pour capter les touches
        self.parent.master.bind("<Key>", self.on_key)
        self.after_id = None
        self.game_loop()

    def reset(self):
        mid_x = COLS // 2
        mid_y = ROWS // 2
        self.snake = [(mid_x, mid_y), (mid_x-1, mid_y), (mid_x-2, mid_y)]
        self.direction = (1, 0)
        self.spawn_food()
        self.game_over = False
        self.score = 0

    def spawn_food(self):
        while True:
            pos = (random.randrange(COLS), random.randrange(ROWS))
            if pos not in self.snake:
                self.food = pos
                return

    def on_key(self, event):
        k = event.keysym
        if k in ("Left", "a", "A") and self.direction != (1,0):
            self.direction = (-1,0)
        elif k in ("Right", "d", "D") and self.direction != (-1,0):
            self.direction = (1,0)
        elif k in ("Up", "w", "W") and self.direction != (0,1):
            self.direction = (0,-1)
        elif k in ("Down", "s", "S") and self.direction != (0,-1):
            self.direction = (0,1)
        elif k in ("r"):
            self.reset()
        elif k == "Escape":
            self.parent.master.destroy()

    def step(self):
        head = self.snake[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])

        # collisions murs
        if not (0 <= new_head[0] < COLS and 0 <= new_head[1] < ROWS):
            self.game_over = True
            return

        # collision corps
        if new_head in self.snake:
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        # manger la pomme
        if new_head == self.food:
            self.score += 1
            self.spawn_food()
        else:
            self.snake.pop()

    def draw(self):
        self.canvas.delete("all")
        # dessiner pomme
        fx, fy = self.food
        self.canvas.create_rectangle(fx*CELL, fy*CELL, (fx+1)*CELL, (fy+1)*CELL, fill=FOOD_COLOR, outline="#330000")
        # dessiner serpent
        for i, (x,y) in enumerate(self.snake):
            color = SNAKE_HEAD if i == 0 else SNAKE_BODY
            self.canvas.create_rectangle(x*CELL, y*CELL, (x+1)*CELL, (y+1)*CELL, fill=color, outline="#003333")
        # score
        self.canvas.create_text(60, 10, text=f"Score: {self.score}", fill=TEXT_COLOR, anchor="nw", font=("Arial", 12, "bold"))
        if self.game_over:
            self.canvas.create_text(WIDTH//2, HEIGHT//2, text="GAME OVER\nr pour rejouer", fill=TEXT_COLOR, font=("Arial", 24, "bold"), justify="center")

    def game_loop(self):
        if not self.game_over:
            self.step()
        self.draw()
        self.after_id = self.parent.after(SPEED_MS, self.game_loop)

def make_ui():
    root = tk.Tk()
    root.title("Snack Broski - Onglets")

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)

    # Onglet jeu
    game_frame = tk.Frame(notebook, bg="#111111")
    notebook.add(game_frame, text="Jeu")

    # Onglet menu / contrôles
    menu_frame = tk.Frame(notebook, bg="#111111")
    notebook.add(menu_frame, text="Menu")

    # Instancier le jeu dans l'onglet jeu
    game = SnackGame(game_frame)

    # Ajouter contrôles dans l'onglet menu
    lbl = tk.Label(menu_frame, text="Snack Broski — contrôles", fg=TEXT_COLOR, bg="#111111", font=("Arial", 14, "bold"))
    lbl.pack(pady=8)
    instr = tk.Label(menu_frame, text="Flèches / WASD : diriger\nR : rejouer\nÉchap : quitter\n\nClique sur les boutons pour piloter le jeu.", fg=TEXT_COLOR, bg="#111111", justify="left")
    instr.pack(padx=10, anchor="w")

    btn_frame = tk.Frame(menu_frame, bg="#111111")
    btn_frame.pack(pady=10)
    btn_reset = tk.Button(btn_frame, text="Rejouer (R)", command=game.reset, width=15)
    btn_reset.grid(row=0, column=0, padx=6, pady=6)
    btn_quit = tk.Button(btn_frame, text="Quitter (Échap)", command=root.destroy, width=15)
    btn_quit.grid(row=0, column=1, padx=6, pady=6)

    # Permettre de sélectionner l'onglet "Jeu" automatiquement
    notebook.select(game_frame)

    # s'assurer que la fenêtre et le canvas reçoivent le focus clavier
    root.focus_force()
    game.canvas.focus_set()

    def on_tab_changed(event):
        # si on revient sur l'onglet "Jeu", donner le focus au canvas pour capter les touches
        selected_widget = event.widget.nametowidget(event.widget.select())
        if selected_widget is game_frame:
            game.canvas.focus_set()

    notebook.bind("<<NotebookTabChanged>>", on_tab_changed)

    return root

if __name__ == "__main__":
    root = make_ui()
    root.mainloop()
