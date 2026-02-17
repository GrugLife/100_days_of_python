import random

number = random.randint(1, 1000)


def hard(number):
    turns = 5
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


def easy(number):
    turns = 10
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
    print("I choose a random number from 1 to 1000")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard'")

    if difficulty == "easy":
        outcome = easy(number)
        print(outcome)
    else:
        outcome = hard(number)
        print(outcome)


main()
