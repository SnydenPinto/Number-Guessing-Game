import random
from game_database import HighScoreDatabase

class NumberGuessingGame:
    DIFFICULTIES = {
        '1': (1, 10),
        '2': (1, 20),
        '3': (1, 50)
    }



    def __init__(self):
        self.generator_instance = None
        self.number_of_attempts = 0
        self.high_score_db = HighScoreDatabase()  # Create an instance of the database
        self.difficulty = None

    def set_difficulty(self):
        while True:
            print("Select a difficulty level:")
            for choice, (lower, upper) in self.DIFFICULTIES.items():
                print(f"{choice}. Guess between {lower} and {upper}")
            choice = input("Enter your choice: ")

            if choice in self.DIFFICULTIES:
                self.difficulty = choice
                print(f"Difficulty set to {self.difficulty}.")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

    def generator(self):
        lower, upper = self.DIFFICULTIES[self.difficulty]
        print(f"Guess the number between {lower} and {upper}")
        return random.randint(lower, upper)

    def get_user_input(self):
        while True:
            try:
                guess = int(input("Guess the number: "))
                return guess
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def play_game(self, username):
        self.generator_instance = self.generator()

        while True:
            user_guess = self.get_user_input()
            self.number_of_attempts += 1

            if user_guess == self.generator_instance:
                print("Congratulations! You guessed it right.")
                print(f"It took you {self.number_of_attempts} tries to guess the correct number.")
                self.high_score_db.add_score(username, self.number_of_attempts)  # Store high score
                break
            elif user_guess < self.generator_instance:
                print("Try again. Your guess is too low.")
            else:
                print("Try again. Your guess is too high.")

        self.number_of_attempts = 0

    def multiplayer(self):
        self.generator_instance = self.generator()
        print("1v1")
        player1_guess = int(input("Player 1, enter your guess: "))
        player2_guess = int(input("Player 2, enter your guess: "))

        while player1_guess != self.generator_instance and player2_guess != self.generator_instance:
            if player1_guess < self.generator_instance:
                print("Too low, Player 1!")
            elif player1_guess > self.generator_instance:
                print("Too high, Player 1!")

            if player2_guess < self.generator_instance:
                print("Too low, Player 2!")
            elif player2_guess > self.generator_instance:
                print("Too high, Player 2!")

            player1_guess = int(input("Player 1, enter your guess: "))
            player2_guess = int(input("Player 2, enter your guess: "))

        if player1_guess == player2_guess == self.generator_instance:
            print("It's a draw! Both players guessed the number.")
        elif player1_guess == self.generator_instance:
            print("Congratulations, Player 1! You guessed the number.")
        else:
            print("Congratulations, Player 2! You guessed the number.")

        print("Game over!")

    def game_mode(self):
        while True:
            print("Select a game mode:")
            print("1. Single Player")
            print("2. Multiplayer")
            choice = input("Enter your choice: ")

            if choice == "1":
                username = input("Enter your username: ")
                self.set_difficulty()
                self.play_game(username)
            elif choice == "2":
                self.multiplayer()
            else:
                print("Invalid choice. Please enter 1 or 2.")


    @staticmethod
    def display_instructions():
        print('''**How to Play:**
        - The game will prompt you to enter your guess.
        - Type your guess using the keyboard and press Enter.
        - If your guess is correct, you win the game!
        - If your guess is incorrect, the game will tell you whether your guess is too low or too high.
        - Continue making guesses until you successfully guess the secret number.
            ''')
        input("Press Enter to return to the main menu...")

    def display_high_scores(self):
        high_scores = self.high_score_db.get_highscores()  # Retrieve high scores from the database
        if high_scores:
            print("High Scores:")
            for rank, (username, score) in enumerate(high_scores, start=1):
                print(f"{rank}. {username}: {score} attempts")
        else:
            print("No high scores yet.")

