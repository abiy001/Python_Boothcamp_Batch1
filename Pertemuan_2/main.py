# ---- number randomizer ----

# secret_number = 37
# guess = 50

# print(guess > secret_number)



import random

level = input("Choose a difficulty level (easy, medium, hard): ").lower()

secret_number = random.randint(1, 100)

guess = int(input("Guess a number between 1 and 10000: "))

while guess != secret_number:
    if guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess = int(input("Guess a number between 1 and 100: "))

print("Congratulations! You guessed the number.")
