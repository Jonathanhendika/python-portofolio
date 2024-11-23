import tkinter
import random
from tkinter import messagebox

ROW = 25
COL = 25
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * ROW
WINDOW_HEIGHT = TILE_SIZE * COL

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# game window
window = tkinter.Tk()
window.title("snake")
window.resizable(False, False)

canvas = tkinter.Canvas(window, bg="black", width=WINDOW_WIDTH, height=WINDOW_HEIGHT, borderwidth=0, highlightthickness=0)
canvas.pack()
window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

# format (w) * (h) + (x) + (y)
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# initializing game
def initialize_game():
    global snake, food, snake_body, velocityX, velocityY, game_over, score
    snake = Tile(5 * TILE_SIZE, 5 * TILE_SIZE)
    food = Tile(10 * TILE_SIZE, 10 * TILE_SIZE)
    snake_body = []
    velocityX = 0
    velocityY = 0
    game_over = False
    score = 0

initialize_game()

def change_direction(e):  # e = event
    global velocityX, velocityY, game_over

    if game_over:
        return

    if e.keysym == "Up" and velocityY != 1:
        velocityX = 0
        velocityY = -1
    elif e.keysym == "Down" and velocityY != -1:
        velocityX = 0
        velocityY = 1
    elif e.keysym == "Left" and velocityX != 1:
        velocityX = -1
        velocityY = 0
    elif e.keysym == "Right" and velocityX != -1:
        velocityX = 1
        velocityY = 0

def move():
    global snake, food, snake_body, game_over, score

    if game_over:
        return

    # Check for collision with window borders
    if snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOW_HEIGHT:
        game_over = True
        return

    # Check for collision with itself
    if any(snake.x == tile.x and snake.y == tile.y for tile in snake_body):
        game_over = True
        return

    # Check for collision with food
    if snake.x == food.x and snake.y == food.y:
        snake_body.append(Tile(food.x, food.y))
        food.x = random.randint(0, COL - 1) * TILE_SIZE
        food.y = random.randint(0, ROW - 1) * TILE_SIZE
        score += 1

    # Update snake body
    if snake_body:
        snake_body = [Tile(snake_body[i - 1].x, snake_body[i - 1].y) for i in range(len(snake_body))]
        snake_body[0].x, snake_body[0].y = snake.x, snake.y

    # Move the snake head
    snake.x += velocityX * TILE_SIZE
    snake.y += velocityY * TILE_SIZE

def game_over_dialog():
    global game_over
    game_over = True
    response = messagebox.askquestion("Game Over", f"Your score is {score}. Do you want to play again?")
    if response == 'yes':
        initialize_game()
        draw()
    else:
        window.destroy()

def draw():
    global snake, game_over, score
    move()

    canvas.delete("all")

    if game_over:
        game_over_dialog()
        return

    # Draw score
    canvas.create_text(30, 20, font=("Helvetica", 10), text=f"Score: {score}", fill="white")

    # Draw food
    canvas.create_oval(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill="red")

    # Draw snake head
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill="blue")

    # Draw snake body
    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x + TILE_SIZE, tile.y + TILE_SIZE, fill="blue")

    window.after(100, draw)

draw()
window.bind("<KeyRelease>", change_direction)
window.mainloop()
