import tkinter as tk
import random
from tkinter import simpledialog, messagebox

class SlotMachine:
    def __init__(self, root):
        self.root = root
        self.root.title("Slot Machine")
        self.root.resizable(False, False)

        # Define symbols and initial balance
        self.symbols = ["🍒", "🍋", "🔔", "🍉", "⭐", "7️⃣"]
        self.initial_balance = 100
        self.balance = self.initial_balance

        # Set up GUI elements
        self.balance_label = tk.Label(root, text=f"Balance: ${self.balance}", font=("Helvetica", 14))
        self.balance_label.pack()

        self.reel1 = tk.Label(root, text="❓", font=("Helvetica", 50))
        self.reel1.pack(side=tk.LEFT, padx=20)
        self.reel2 = tk.Label(root, text="❓", font=("Helvetica", 50))
        self.reel2.pack(side=tk.LEFT, padx=20)
        self.reel3 = tk.Label(root, text="❓", font=("Helvetica", 50))
        self.reel3.pack(side=tk.LEFT, padx=20)

        self.spin_button = tk.Button(root, text="Spin", command=self.spin, font=("Helvetica", 14))
        self.spin_button.pack(pady=20)

        self.deposit_button = tk.Button(root, text="Deposit", command=self.deposit, font=("Helvetica", 14))
        self.deposit_button.pack(pady=5)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_game, font=("Helvetica", 14))
        self.reset_button.pack(pady=5)

        self.message_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.message_label.pack()

    def spin(self):
        if self.balance <= 0:
            self.message_label.config(text="Insufficient balance! Please make a deposit.")
            return

        # Deduct bet amount
        self.balance -= 1
        self.balance_label.config(text=f"Balance: ${self.balance}")

        # Spin reels
        self.reel1.config(text=random.choice(self.symbols))
        self.reel2.config(text=random.choice(self.symbols))
        self.reel3.config(text=random.choice(self.symbols))

        self.check_outcome()

    def deposit(self):
        try:
            deposit_amount = simpledialog.askinteger("Deposit", "Enter amount to deposit:")
            if deposit_amount and deposit_amount > 0:
                self.balance += deposit_amount
                self.balance_label.config(text=f"Balance: ${self.balance}")
                self.message_label.config(text=f"Deposited ${deposit_amount}")
            else:
                messagebox.showerror("Invalid input", "Please enter a valid amount.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def reset_game(self):
        self.balance = self.initial_balance
        self.balance_label.config(text=f"Balance: ${self.balance}")
        self.reel1.config(text="❓")
        self.reel2.config(text="❓")
        self.reel3.config(text="❓")
        self.message_label.config(text="")

    def check_outcome(self):
        symbol1 = self.reel1.cget("text")
        symbol2 = self.reel2.cget("text")
        symbol3 = self.reel3.cget("text")

        if symbol1 == symbol2 == symbol3:
            self.message_label.config(text=f"Jackpot! You won $50!")
            self.balance += 50
        elif symbol1 == symbol2 or symbol2 == symbol3 or symbol1 == symbol3:
            self.message_label.config(text=f"You won $5!")
            self.balance += 5
        else:
            self.message_label.config(text=f"Try again!")

        self.balance_label.config(text=f"Balance: ${self.balance}")

def main():
    root = tk.Tk()
    slot_machine = SlotMachine(root)
    root.mainloop()

if __name__ == "__main__":
    main()
