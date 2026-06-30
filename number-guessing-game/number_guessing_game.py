import random


def play(num, attempts):
    """Run the guessing loop for a given number of attempts.

    Returns True if the player guessed correctly, False otherwise.
    """
    print(f"You have {attempts} attempts")
    for i in range(1, attempts + 1):
        try:
            guess = int(input("Guess the number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < 1 or guess > 100:
            print("Please guess a number between 1 and 100.")
            continue

        if guess == num:
            return True
        elif guess > num:
            print("Too high!")
        else:
            print("Too low!")

        print(f"You have {attempts - i} attempts left")

    return False


def main():
    print("Welcome to the Number Guessing Game!")
    print("I'm going to select a number between 1 and 100.")

    hardness = input("Enter 'h' to play HARD or 'e' to play EASY: ").lower()
    number = random.randint(1, 100)

    if hardness == 'e':
        found = play(number, 10)
    elif hardness == 'h':
        found = play(number, 5)
    else:
        print("Invalid choice. Please restart and enter 'h' or 'e'.")
        return

    if found:
        print("Number found! Well done!")
    else:
        print(f"Your chances have ended. The number was {number}.")


if __name__ == "__main__":
    main()
