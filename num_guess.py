import random

EASY_MODE_TURNS = 10
HARD_MODE_TURNS = 5
number = random.randint(1, 100)


def mode(number, turns):
    while turns > 0:
        guess = int(input("What is your guess: "))
        turns -= 1
        if guess == number:
            return f"You guessed the number right: {guess}"
        elif guess > number:
            print(f"Your guess of {guess} is too high, you have {turns} remaining")
        else:
            print(f"Your guess of {guess} is too low, you have {turns} remaining")
    return (
        f"You ran out of turns, better luck next time. The correct number is {number}"
    )


def main():
    print("Welcome to the number guessing game")
    print("I choose a random number from 1 to 100")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard'")

    if difficulty == "easy":
        outcome = mode(number, EASY_MODE_TURNS)
        print(outcome)
    else:
        outcome = mode(number, HARD_MODE_TURNS)
        print(outcome)


main()
