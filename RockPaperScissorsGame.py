import tkinter as tk
from tkinter import messagebox # For displaying messages, though not strictly needed for this game, good practice
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        master.title("Rock-Paper-Scissors")
        master.geometry("500x450") # Set initial window size
        master.resizable(False, False) # Prevent resizing for a fixed layout

        self.user_score = 0
        self.computer_score = 0
        self.choices = ["Rock", "Paper", "Scissors"]

        self.create_widgets()

    def create_widgets(self):
        # --- Title/Instructions Frame ---
        title_frame = tk.Frame(self.master, pady=10)
        title_frame.pack(fill="x")

        tk.Label(title_frame, text="Play Rock, Paper, Scissors!", font=("Arial", 18, "bold")).pack()
        tk.Label(title_frame, text="Choose your move:", font=("Arial", 12)).pack()

        # --- Choice Buttons Frame ---
        buttons_frame = tk.Frame(self.master, pady=15)
        buttons_frame.pack()

        self.rock_button = tk.Button(buttons_frame, text="✊ Rock", font=("Arial", 14), width=10, height=2,
                                     command=lambda: self.play_round("Rock"), bg="#FFDDC1", fg="#333", relief="raised", bd=3)
        self.rock_button.grid(row=0, column=0, padx=10, pady=5)

        self.paper_button = tk.Button(buttons_frame, text="🖐️ Paper", font=("Arial", 14), width=10, height=2,
                                      command=lambda: self.play_round("Paper"), bg="#C1FFDD", fg="#333", relief="raised", bd=3)
        self.paper_button.grid(row=0, column=1, padx=10, pady=5)

        self.scissors_button = tk.Button(buttons_frame, text="✌️ Scissors", font=("Arial", 14), width=10, height=2,
                                        command=lambda: self.play_round("Scissors"), bg="#DDC1FF", fg="#333", relief="raised", bd=3)
        self.scissors_button.grid(row=0, column=2, padx=10, pady=5)

        # --- Game Results Display Frame ---
        results_frame = tk.LabelFrame(self.master, text="Round Details", padx=20, pady=10, bd=2, relief="groove")
        results_frame.pack(pady=10, padx=20, fill="x")

        self.user_choice_label = tk.Label(results_frame, text="Your Choice: ", font=("Arial", 12))
        self.user_choice_label.pack(anchor="w", pady=2)

        self.computer_choice_label = tk.Label(results_frame, text="Computer Choice: ", font=("Arial", 12))
        self.computer_choice_label.pack(anchor="w", pady=2)

        self.result_label = tk.Label(results_frame, text="Result: ", font=("Arial", 14, "bold"), fg="blue")
        self.result_label.pack(pady=5)

        # --- Scoreboard Frame ---
        scoreboard_frame = tk.LabelFrame(self.master, text="Scoreboard", padx=20, pady=10, bd=2, relief="groove")
        scoreboard_frame.pack(pady=10, padx=20, fill="x")

        self.user_score_label = tk.Label(scoreboard_frame, text=f"Your Score: {self.user_score}", font=("Arial", 12))
        self.user_score_label.grid(row=0, column=0, padx=20, pady=5)

        self.computer_score_label = tk.Label(scoreboard_frame, text=f"Computer Score: {self.computer_score}", font=("Arial", 12))
        self.computer_score_label.grid(row=0, column=1, padx=20, pady=5)

        # --- Reset Button ---
        reset_button = tk.Button(self.master, text="Reset Game", command=self.reset_game,
                                 font=("Arial", 12, "bold"), bg="#FF6347", fg="white", relief="raised", bd=3)
        reset_button.pack(pady=15)

    def play_round(self, user_choice):
        """Plays a single round of Rock-Paper-Scissors."""
        computer_choice = random.choice(self.choices)

        self.user_choice_label.config(text=f"Your Choice: {user_choice}")
        self.computer_choice_label.config(text=f"Computer Choice: {computer_choice}")

        result_text, result_color = self.determine_winner(user_choice, computer_choice)
        self.result_label.config(text=f"Result: {result_text}", fg=result_color)

        self.update_scores(result_text)

    def determine_winner(self, user_choice, computer_choice):
        """Determines the winner of the round and returns result text and color."""
        if user_choice == computer_choice:
            return "It's a Tie!", "blue"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            return "You Win!", "green"
        else:
            return "You Lose!", "red"

    def update_scores(self, result):
        """Updates the scores based on the round's result."""
        if "Win" in result:
            self.user_score += 1
        elif "Lose" in result:
            self.computer_score += 1

        self.user_score_label.config(text=f"Your Score: {self.user_score}")
        self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")

    def reset_game(self):
        """Resets the game scores and display."""
        self.user_score = 0
        self.computer_score = 0
        self.user_score_label.config(text=f"Your Score: {self.user_score}")
        self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")
        self.user_choice_label.config(text="Your Choice: ")
        self.computer_choice_label.config(text="Computer Choice: ")
        self.result_label.config(text="Result: ", fg="blue")
        # messagebox.showinfo("Game Reset", "The game has been reset!") # Optional: show a message

# Create the main window and run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()