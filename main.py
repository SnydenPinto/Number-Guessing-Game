import game_logic


def main_menu():
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


option = main_menu()

if option == 1:
    game_logic.start_game()
    # Call the function to start the game
    pass
elif option == 2:
    # Call the function to display instructions
    game_logic.game_instructions()
    main_menu()
    pass
elif option == 3:
    # Call the function to display high scores
    pass
elif option == 4:
    # Exit the program
    print("Exiting the game.")
