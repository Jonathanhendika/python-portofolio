import tkinter as tk
from tkinter import simpledialog, messagebox
import random

class PigGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Pig Game")

        self.num_players = simpledialog.askinteger("Input", "Enter number of players (2 or more):", minvalue=2)
        if not self.num_players:
            self.root.destroy()
            return

        self.player_scores = [0] * self.num_players
        self.turn_total = 0
        self.current_player = 0

        self.score_labels = []
        for i in range(self.num_players):
            label = tk.Label(root, text=f"Player {i+1} Score: {self.player_scores[i]}", font=("Helvetica", 14))
            label.pack()
            self.score_labels.append(label)

        self.turn_total_label = tk.Label(root, text=f"Turn Total: {self.turn_total}", font=("Helvetica", 14))
        self.turn_total_label.pack()

        self.die_label = tk.Label(root, text="Roll: -", font=("Helvetica", 24))
        self.die_label.pack(pady=20)

        self.roll_button = tk.Button(root, text="Roll", command=self.roll_die, font=("Helvetica", 14))
        self.roll_button.pack(pady=5)

        self.hold_button = tk.Button(root, text="Hold", command=self.hold, font=("Helvetica", 14))
        self.hold_button.pack(pady=5)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_game, font=("Helvetica", 14))
        self.reset_button.pack(pady=5)

    def roll_die(self):
        roll = random.randint(1, 6)
        self.die_label.config(text=f"Roll: {roll}")
        if roll == 1:
            self.turn_total = 0
            self.switch_player()
        else:
            self.turn_total += roll
            self.turn_total_label.config(text=f"Turn Total: {self.turn_total}")

    def hold(self):
        self.player_scores[self.current_player] += self.turn_total
        self.turn_total = 0
        self.turn_total_label.config(text=f"Turn Total: {self.turn_total}")

        self.score_labels[self.current_player].config(text=f"Player {self.current_player + 1} Score: {self.player_scores[self.current_player]}")
        if self.player_scores[self.current_player] >= 100:
            messagebox.showinfo("Game Over", f"Player {self.current_player + 1} wins!")
            self.reset_game()
        else:
            self.switch_player()

    def switch_player(self):
        self.current_player = (self.current_player + 1) % self.num_players
        messagebox.showinfo("Turn Over", f"Player {self.current_player + 1}'s turn!")

    def reset_game(self):
        self.player_scores = [0] * self.num_players
        self.turn_total = 0
        self.current_player = 0
        for i in range(self.num_players):
            self.score_labels[i].config(text=f"Player {i+1} Score: {self.player_scores[i]}")
        self.turn_total_label.config(text=f"Turn Total: {self.turn_total}")
        self.die_label.config(text="Roll: -")

def main():
    root = tk.Tk()
    game = PigGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
