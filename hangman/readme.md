
# Hangman Game 🎮

A simple command-line Hangman game made with Python.

## About

This is a basic implementation of the classic Hangman game.  
The player has 6 lives to guess the hidden word one letter at a time.

The game uses:
- A list of random words (`hangman_words.py`)
- ASCII art for hangman stages and logo (`hangman_art.py`)

## How to Play

1. Run the game using Python.
2. Guess a letter by typing it into the terminal.
3. If the letter is correct, it will be revealed.
4. If the letter is wrong, you lose a life.
5. You win if you guess the full word before losing all 6 lives.

## Files

- `hangman.py`: Main game script
- `hangman_words.py`: Contains a list of words to guess
- `hangman_art.py`: ASCII logo and stages used during the game
- `README.md`: Game info and instructions

## How to Run

Make sure you have Python installed (version 3.6 or above).

```bash
git clone https://github.com/nitinrawat05/hangman.git
cd hangman
python hangman.py
