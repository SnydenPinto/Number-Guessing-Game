import random

random_number = random.randrange(1, 9)

attempts = 0
numberOfHints = 3

guess = int(input("Guess the number :"))


def hints():
    global numberOfHints
    if numberOfHints > 0:
        if random_number % 2 == 0:
            print("The secret number is even")
        else:
            print("The secret number is odd")
        numberOfHints -= 1
    else:
        print("You have used all your hints.")


while guess != random_number:
    if guess < random_number:
        print("Too low")
        guess = int(input("Guess the number :"))
        attempts += 1
    elif guess > random_number:
        print("Too High")
        guess = int(input("Guess the number :"))
        attempts += 1
    else:
        break

    while attempts % 2 == 0:
        user_hints =input(("Would you like to use a hint? yes or no"))
        if user_hints == "yes":
            hints()
        else:
            break
        print("you got " + str(numberOfHints) + " hints left")



print("You guessed the number")
print("It took you " + str(attempts) + " attempts to guess the correct number")
