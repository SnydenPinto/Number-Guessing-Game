import random
random_number = random.randrange(0,9)

attempts = 0

guess = int(input("Guess the number :"))

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
print("You gassed the number")

print("it took you "+str(attempts)+" attempts to guess the correct number")