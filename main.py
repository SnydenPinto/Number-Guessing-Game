import game_logic


def display_main_menu():
    while True:
        try:
            print("Welcome to Guess the Number Game!")
            print("1. Start Game")
            print("2. Play Instructions")
            print("3. High Scores")
            print("4. Exit")

            main_menu_user_input = int(input("Please select an option: "))

            if main_menu_user_input in (1, 2, 3, 4):
                return main_menu_user_input
            else:
                print("Invalid input. Please select a valid option (1, 2, 3, or 4).")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    game = game_logic.NumberGuessingGame()

    while True:
        option = display_main_menu()

        if option == 1:
            print("Starting a new game...")
            username = input("Enter your username: ")
            game.set_difficulty()  # Ask for difficulty level
            game.play_game(username)
        elif option == 2:
            game.display_instructions()
        elif option == 3:
            game.display_high_scores()
        elif option == 4:
            print("Exiting the game.")
            break  # Exit the loop when the user chooses to exit


if __name__ == "__main__":
    main()
