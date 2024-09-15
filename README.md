

# Advanced Number Guessing Game

Welcome to the Advanced Number Guessing Game! This is a simple game built using Python and Tkinter, where you can play against an AI opponent to guess a randomly generated number. 

## Features

- **User Interface:** Built with Tkinter for a responsive and user-friendly experience.
- **Difficulty Levels:** Choose from "easy," "medium," or "hard" difficulty settings.
- **AI Opponent:** An AI guesses the number within the same range, providing an additional challenge.
- **Leaderboard:** Track your best scores and compare them with others.
- **Points System:** Earn points based on the number of guesses and time taken.

## Installation

To run the Number Guess Game, you'll need Python installed on your system. Ensure you have Python 3.x.

1. **Clone the repository** or **download the script**:
   ```sh
   git clone https://github.com/mahmudnibir/Advanced-Number-Guessing-Game.git
   cd Advanced-Number-Guessing-Game
   ```

2. **Install dependencies** (Tkinter is included with Python, so no additional packages are needed).

## Usage

1. **Run the game**:
   ```sh
   python Advanced-Number-Guessing-Game.py
   ```

2. **Game Play**:
   - Enter your name and select a difficulty level.
   - Click "Start Game" to begin.
   - Input your guesses in the provided entry field and press Enter.
   - The AI will make guesses as well, and you’ll get feedback on each guess.

3. **Leaderboard**:
   - After the game ends, your score will be added to the leaderboard.
   - Click "View Leaderboard" to see the top scores and your performance.

## Code Overview

- **`read_leaderboard`**: Reads the leaderboard data from `leaderboard.txt`.
- **`write_leaderboard`**: Writes the updated leaderboard data to `leaderboard.txt`.
- **`update_leaderboard`**: Updates the leaderboard with new scores and sorts them.
- **`AI` Class**: Handles AI opponent logic for making guesses.
- **`NumberGuessGame` Class**: Manages the main game logic, user interface, and game flow.

## Files

- **`number_guess_game.py`**: The main script file for the game.
- **`leaderboard.txt`**: Stores the leaderboard data.

## Contributing

Feel free to contribute to the project! If you have suggestions or improvements, open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
