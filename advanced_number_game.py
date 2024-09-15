import tkinter as tk
import random
import time
import os

# Function to read leaderboard from a file
def read_leaderboard():
    if os.path.exists("leaderboard.txt"):
        with open("leaderboard.txt", "r") as file:
            return [line.strip().split(",") for line in file.readlines()]
    return []

# Function to write leaderboard to a file
def write_leaderboard(scores):
    with open("leaderboard.txt", "w") as file:
        for score in scores:
            file.write(",".join(map(str, score)) + "\n")

# Function to update leaderboard with a new score
def update_leaderboard(player_name, guesses, elapsed_time, points):
    scores = read_leaderboard()
    scores.append([player_name, str(guesses), str(elapsed_time), str(points)])
    scores.sort(key=lambda x: (int(x[1]), float(x[2]), -int(x[3])))
    write_leaderboard(scores)

# AI Opponent Class
class AI:
    def __init__(self, min_num, max_num):
        self.min_num = min_num
        self.max_num = max_num
        self.attempts = 0
        self.max_attempts = 7
        self.guess = None
        self.previous_guesses = []
    
    def make_guess(self):
        if self.min_num > self.max_num or self.attempts >= self.max_attempts:
            return None
        
        self.guess = random.randint(self.min_num, self.max_num)
        while self.guess in self.previous_guesses:
            self.guess = random.randint(self.min_num, self.max_num)
        
        self.previous_guesses.append(self.guess)
        self.attempts += 1
        return self.guess

# Main Game Class
class NumberGuessGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Number Guess Game")
        self.geometry("400x400")
        self.configure(bg="#333333")  # Reverting to the previous dark gray background
        
        self.difficulty = tk.StringVar(value="easy")
        self.player_guesses = 0
        self.ai = None
        self.a = 0
        self.start_time = 0
        self.max_attempts = 7
        self.player_name = tk.StringVar()
        
        # Set up the UI
        self.setup_ui()
    
    def setup_ui(self):
        title = tk.Label(self, text="Welcome to Number Guess Game!", font=("Arial", 16, "bold"), fg="#FFCC00", bg="#333333")
        title.pack(pady=10)
        
        name_label = tk.Label(self, text="Enter your name:", fg="#FFFFFF", bg="#333333")
        name_label.pack()
        name_entry = tk.Entry(self, textvariable=self.player_name)
        name_entry.pack(pady=5)
        
        difficulty_label = tk.Label(self, text="Select difficulty:", fg="#FFFFFF", bg="#333333")
        difficulty_label.pack()
        tk.OptionMenu(self, self.difficulty, "easy", "medium", "hard").pack(pady=5)
        
        start_button = tk.Button(self, text="Start Game", command=self.start_game, bg="#00A8E8", fg="white", font=("Arial", 12, "bold"))
        start_button.pack(pady=10)
        
        leaderboard_button = tk.Button(self, text="View Leaderboard", command=self.show_leaderboard, bg="#00A8E8", fg="white", font=("Arial", 12, "bold"))
        leaderboard_button.pack(pady=10)
        
        self.result_label = tk.Label(self, text="", fg="#FF5733", bg="#333333", font=("Arial", 12, "bold"))
        self.result_label.pack(pady=10)
    
    def start_game(self):
        self.result_label.config(text="")
        self.player_guesses = 0
        self.start_time = time.time()
        
        min_number, max_number, self.max_attempts = self.get_game_parameters()
        self.a = random.randint(min_number, max_number)
        
        self.ai = AI(min_number, max_number)
        
        self.guess_label = tk.Label(self, text=f"Guess the number between {min_number} and {max_number}", fg="#FFFFFF", bg="#333333", font=("Arial", 12))
        self.guess_label.pack(pady=5)
        
        self.attempts_left_label = tk.Label(self, text=f"Attempts left: {self.max_attempts - self.player_guesses}", fg="#FFFF66", bg="#333333", font=("Arial", 12, "bold"))
        self.attempts_left_label.pack(pady=5)
        
        self.guess_entry = tk.Entry(self)
        self.guess_entry.pack(pady=5)
        self.guess_entry.bind("<Return>", self.check_guess)
        
        self.ai_guess_label = tk.Label(self, text="AI is making guesses...", fg="#FFFFFF", bg="#333333", font=("Arial", 12))
        self.ai_guess_label.pack(pady=5)
    
    def get_game_parameters(self):
        difficulty = self.difficulty.get()
        if difficulty == "easy":
            return 1, 50, 10
        elif difficulty == "medium":
            return 1, 100, 7
        else:
            return 1, 200, 5
    
    def check_guess(self, event=None):
        try:
            player_guess = int(self.guess_entry.get())
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")
            return
        
        min_number, max_number, _ = self.get_game_parameters()
        if not (min_number <= player_guess <= max_number):
            self.result_label.config(text=f"Guess out of range! Enter a number between {min_number} and {max_number}.")
            return
        
        self.guess_entry.delete(0, tk.END)
        self.player_guesses += 1
        
        if player_guess > self.a:
            self.result_label.config(text="Enter a lower number, please.")
        elif player_guess < self.a:
            self.result_label.config(text="Enter a higher number, please.")
        else:
            elapsed_time = round(time.time() - self.start_time, 2)
            points = self.calculate_points()
            self.result_label.config(text=f"Congratulations! You guessed it in {self.player_guesses} attempts!")
            self.end_game(elapsed_time, points)
            return
        
        self.attempts_left_label.config(text=f"Attempts left: {self.max_attempts - self.player_guesses}")
        
        if self.player_guesses >= self.max_attempts:
            self.result_label.config(text="Game Over! You've reached the maximum attempts.")
            self.end_game()
            return
        
        # AI makes a guess
        ai_guess = self.ai.make_guess()
        if ai_guess is None:
            self.ai_guess_label.config(text="AI couldn't guess the number.")
        else:
            if ai_guess > self.a:
                self.ai_guess_label.config(text=f"AI guessed {ai_guess}: Try a lower number.")
            elif ai_guess < self.a:
                self.ai_guess_label.config(text=f"AI guessed {ai_guess}: Try a higher number.")
            else:
                self.result_label.config(text=f"AI won! The number was {self.a}.")
                self.end_game()
    
    def calculate_points(self):
        return max(10 - self.player_guesses, 1)
    
    def end_game(self, elapsed_time=None, points=None):
        if points is None:
            points = 0
        if elapsed_time is None:
            elapsed_time = 0
        
        player_name = self.player_name.get() or "Unknown"
        update_leaderboard(player_name, self.player_guesses, elapsed_time, points)
        self.guess_entry.unbind("<Return>")
        self.show_leaderboard()
    
    def show_leaderboard(self):
        scores = read_leaderboard()
        leaderboard_window = tk.Toplevel(self)
        leaderboard_window.title("Leaderboard")
        leaderboard_window.geometry("300x200")
        leaderboard_window.configure(bg="#333333")
        
        tk.Label(leaderboard_window, text="Leaderboard", font=("Arial", 14), fg="#FFCC00", bg="#333333").pack(pady=10)
        
        for idx, score in enumerate(scores[:10]):
            tk.Label(leaderboard_window, text=f"{idx + 1}. {score[0]} - {score[1]} guesses in {score[2]}s with {score[3]} points", fg="#FFFFFF", bg="#333333").pack()

if __name__ == "__main__":
    app = NumberGuessGame()
    app.mainloop()
