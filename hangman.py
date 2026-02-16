import random

word_list = ["aardvark", "baboon", "camel"]
game_over = False
chosen_word = random.choice(word_list)
placeholder = "_" * len(chosen_word)
display = list(placeholder)
lives = 6

print(chosen_word)
print(placeholder)

while not game_over:
    guess = input("Guess a letter:  ").lower()

    if guess not in chosen_word:
        lives -= 1
    else:
        for idx, letter in enumerate(chosen_word):
            if letter == guess:
                display[idx] = letter

    print("".join(display))

    if "_" not in display:
        print("You win")
        game_over = True
    elif lives == 0:
        print("You lose")
        game_over = True
