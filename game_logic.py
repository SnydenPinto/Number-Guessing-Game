import random

difficulty_ranges = {
    "easy": (1, 10),
    "medium": (1, 50),
    "hard": (1, 100)
}


def get_random_number(difficulty):
    if difficulty in difficulty_ranges:
        return random.randint(*difficulty_ranges[difficulty])
    else:
        print("Invalid difficulty level. Using default range.")
        return random.randint(*difficulty_ranges["easy"])


def provide_hint(number):
    if number % 2 == 0:
        print("The secret number is even")
    else:
        print("The secret number is odd")


def main():
    difficulty = input("Choose difficulty level (easy, medium, hard): ")
    print("you have selected the ", difficulty)
    random_number = get_random_number(difficulty)
    attempts = 0
    number_of_hints = 3

    while True:
        guess = get_guess()
        attempts += 1

        if guess < random_number:
            print("Too low")
        elif guess > random_number:
            print("Too high")
        else:
            print("You guessed the number!")
            print("It took you", attempts, "attempts to guess the correct number")
            break

        if attempts % 2 == 0 and number_of_hints > 0:
            user_hints = input("Would you like to use a hint? (yes or no): ")
            if user_hints == "yes":
                provide_hint(random_number)
                number_of_hints -= 1
                print("You have", number_of_hints, "hints left")

        if number_of_hints == 0:
            print("You have used all your hints.")


def get_guess():
    while True:
        try:
            guess = int(input("Guess the number: "))
            return guess
        except ValueError:
            print("Please enter a valid numeric input.")


if __name__ == "__main__":
    main()
