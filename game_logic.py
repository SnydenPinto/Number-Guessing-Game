import random



def generator():
    return random.randint(1, 10)


number_of_hints = 3


def get_userinput():
    while True:
        try:
            guess = int(input("Guess the number: "))
            return guess  # Return the valid guess and exit the loop
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def start_game():
    number_of_attempts = 0
    guess = generator()
    while True:
        user_guess = get_userinput()
        if user_guess == guess:
            print("Congratulations! You guessed it right. It took you", number_of_attempts, "tries to guess the "
                                                                                            "correct number")
            break
        elif user_guess < guess:
            print("Try again. Your guess is too low.")
            number_of_attempts += 1
        else:
            print("Try again. Your guess is too high.")
            number_of_attempts += 1


def game_instructions():
    print('''                       **How to Play:**
                   - The game will prompt you to enter your guess.
                   - Type your guess using the keyboard and press Enter.
                   - If your guess is correct, you win the game!
                   - If your guess is incorrect, the game will tell you whether your guess is too low or too high.
                   - Continue making guesses until you successfully guess the secret number.
    ''')
    input("            Press Enter to return to the main menu...")
