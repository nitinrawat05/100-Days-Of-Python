# ----------------------------
# HANGMAN GAME - BY NITS 🕹️
# ----------------------------

import random
from hangman_words import word_list
from hangman_art import logo, stages

# Number of lives player starts with
lives = 6

# Randomly choose a word from the list
chosen_word = random.choice(word_list)

# Display the starting placeholder (e.g., "_ _ _ _")
placeholder = "_" * len(chosen_word)
print(logo)
print(placeholder)

# Game control variables
game_over = False
correct_guesses = []

# Game loop
while not game_over:
    # Ask player to guess a letter
    guess = input("Guess a letter: ").lower()

    # Already guessed check
    if guess in correct_guesses:
        print(f"You already guessed '{guess}'. Try something else.")
        continue

    # Show logo again each round
    print(logo)

    # Build the display string
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            # Add to guessed letters if not already added
            if guess not in correct_guesses:
                correct_guesses.append(guess)
        elif letter in correct_guesses:
            display += letter
        else:
            display += "_"

    # Show current state of guessed word
    print(display)

    # If guess is wrong
    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess! You lose a life. Lives left: {lives}")
        print(stages[lives])  # Show hangman stage

        if lives == 0:
            game_over = True
            print("💀 You lost! The word was:", chosen_word)
    else:
        print("✅ Correct guess!")

    # Check if player has guessed the whole word
    if "_" not in display:
        game_over = True
        print("🎉 You win!")

# END OF GAME

