import game_logic


def display_main_menu():
    while True:
        try:
            main_menu_user_input = int(input("""
            Welcome to Guess the Number Game!
                1. Start Game
                2. Play Instructions
                3. High Scores
                4. Exit
            Please select an option: """))

            if main_menu_user_input in (1, 2, 3, 4):
                return main_menu_user_input
            else:
                print("Invalid input. Please select a valid option (1, 2, 3, or 4).")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    game = game_logic.NumberGuessingGame()
    option = display_main_menu()

    if option == 1:
        username = input("Enter your username: ")
        game.set_difficulty()
        game.play_game(username)
    elif option == 2:
        game.display_instructions()
        main()
    elif option == 3:
        game.display_high_scores()
        main()
    elif option == 4:
        print("Exiting the game.")


if __name__ == "__main__":
    main()
