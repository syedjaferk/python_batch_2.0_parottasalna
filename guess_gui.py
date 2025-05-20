import tkinter as tk
import tkinter.simpledialog
from tkinter import messagebox
import random
import os
 
LEADERBOARD_FILE = "leaderboard.txt"
 
class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
 
        self.min_value = 1
        self.max_value = 100
        self.max_attempts = 10
        self.attempts = 0
        self.secret_number = 0
        self.player_name = ""
        self.hints_given = False
 
        self.create_widgets()
 
    def create_widgets(self):
        """Create the main interface widgets."""
        self.difficulty_label = tk.Label(self.root, text="Select Difficulty Level:")
        self.difficulty_label.pack(pady=10)
 
        self.difficulty_var = tk.IntVar(value=2)
        self.difficulty_easy = tk.Radiobutton(self.root, text="Easy (1-50)", variable=self.difficulty_var, value=1, command=self.set_difficulty)
        self.difficulty_medium = tk.Radiobutton(self.root, text="Medium (1-100)", variable=self.difficulty_var, value=2, command=self.set_difficulty)
        self.difficulty_hard = tk.Radiobutton(self.root, text="Hard (1-1000)", variable=self.difficulty_var, value=3, command=self.set_difficulty)
 
        self.difficulty_easy.pack()
        self.difficulty_medium.pack()
        self.difficulty_hard.pack()
 
        self.start_button = tk.Button(self.root, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=10)
 
        self.guess_label = tk.Label(self.root, text="Enter your guess:")
        self.guess_entry = tk.Entry(self.root)
 
        self.submit_button = tk.Button(self.root, text="Submit Guess", command=self.check_guess)
        self.attempts_label = tk.Label(self.root, text="Attempts left: N/A")
 
        self.leaderboard_button = tk.Button(self.root, text="Show Leaderboard", command=self.show_leaderboard)
        self.leaderboard_button.pack(pady=10)
 
    def set_difficulty(self):
        """Set the game difficulty based on user selection."""
        difficulty = self.difficulty_var.get()
        if difficulty == 1:
            self.min_value, self.max_value, self.max_attempts = 1, 50, 10
        elif difficulty == 2:
            self.min_value, self.max_value, self.max_attempts = 1, 100, 7
        else:
            self.min_value, self.max_value, self.max_attempts = 1, 1000, 5
 
    def start_game(self):
        """Start the game by generating a random number and resetting the attempts."""
        self.secret_number = random.randint(self.min_value, self.max_value)
        self.attempts = 0
        self.hints_given = False
 
        self.difficulty_label.pack_forget()
        self.difficulty_easy.pack_forget()
        self.difficulty_medium.pack_forget()
        self.difficulty_hard.pack_forget()
        self.start_button.pack_forget()
 
        self.guess_label.pack(pady=10)
        self.guess_entry.pack(pady=10)
        self.submit_button.pack(pady=10)
        self.attempts_label.pack(pady=10)
        self.update_attempts_label()
 
    def update_attempts_label(self):
        """Update the label that shows how many attempts are left."""
        attempts_left = self.max_attempts - self.attempts
        self.attempts_label.config(text=f"Attempts left: {attempts_left}")
 
    def check_guess(self):
        """Check the user's guess and provide feedback."""
        try:
            guess = int(self.guess_entry.get())
            if guess < self.min_value or guess > self.max_value:
                messagebox.showerror("Error", f"Please enter a number between {self.min_value} and {self.max_value}.")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer.")
            return
 
        self.attempts += 1
        self.update_attempts_label()
 
        if guess < self.secret_number:
            messagebox.showinfo("Result", "Too low! Try again.")
        elif guess > self.secret_number:
            messagebox.showinfo("Result", "Too high! Try again.")
        else:
            messagebox.showinfo("Congratulations!", f"You guessed the number in {self.attempts} attempts.")
            self.record_score()
            self.reset_game()
            return
 
        if self.attempts == self.max_attempts:
            messagebox.showinfo("Game Over", f"Sorry, you've used all {self.max_attempts} attempts. The correct number was {self.secret_number}.")
            self.reset_game()
 
        if self.attempts == self.max_attempts // 2 and not self.hints_given:
            hint = "even" if self.secret_number % 2 == 0 else "odd"
            messagebox.showinfo("Hint", f"Hint: The number is {hint}.")
            self.hints_given = True
 
    def record_score(self):
        """Record the player's score and update the leaderboard."""
        self.player_name = tkinter.simpledialog.askstring("Name", "Enter your name for the leaderboard:")
        if not self.player_name:
            self.player_name = "Anonymous"
 
        leaderboard = self.load_leaderboard()
        leaderboard.append((self.player_name, self.attempts))
        leaderboard = sorted(leaderboard, key=lambda x: x[1])[:10]  # Keep only top 10 scores
        self.save_leaderboard(leaderboard)
 
    def load_leaderboard(self):
        """Load the leaderboard from a file."""
        if os.path.exists(LEADERBOARD_FILE):
            with open(LEADERBOARD_FILE, "r") as file:
                leaderboard = [line.strip().split(",") for line in file.readlines()]
                return [(name, int(score)) for name, score in leaderboard]
        return []
 
    def save_leaderboard(self, leaderboard):
        """Save the leaderboard to a file."""
        with open(LEADERBOARD_FILE, "w") as file:
            for name, score in leaderboard:
                file.write(f"{name},{score}\n")
 
    def show_leaderboard(self):
        """Display the top scores from the leaderboard."""
        leaderboard = self.load_leaderboard()
        if leaderboard:
            leaderboard_str = "\n".join([f"{i+1}. {name}: {score} attempts" for i, (name, score) in enumerate(leaderboard)])
        else:
            leaderboard_str = "No scores yet. Be the first to play!"
        messagebox.showinfo("Leaderboard", leaderboard_str)
 
    def reset_game(self):
        """Reset the game to the initial state."""
        self.guess_label.pack_forget()
        self.guess_entry.pack_forget()
        self.submit_button.pack_forget()
        self.attempts_label.pack_forget()
 
        self.difficulty_label.pack(pady=10)
        self.difficulty_easy.pack()
        self.difficulty_medium.pack()
        self.difficulty_hard.pack()
        self.start_button.pack(pady=10)
 
if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()