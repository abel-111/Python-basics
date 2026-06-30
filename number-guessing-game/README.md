# Number Guessing Game

A simple command-line game where the computer picks a random number between 1 and 100, and you try to guess it within a limited number of attempts.

## How it works

- The computer randomly selects a number between 1 and 100.
- You choose a difficulty:
  - **Easy** (`e`) — 10 attempts
  - **Hard** (`h`) — 5 attempts
- After each guess, you're told if your guess was too high or too low.
- Guess the number before you run out of attempts to win!

## Requirements

- Python 3.x

## How to run

```bash
python number_guessing_game.py
```

## Example

```
Welcome to the Number Guessing Game!
I'm going to select a number between 1 and 100.
Enter 'h' to play HARD or 'e' to play EASY: e
You have 10 attempts
Guess the number: 50
Too high!
You have 9 attempts left
Guess the number: 25
Too low!
You have 8 attempts left
Guess the number: 37
Number found! Well done!
```

## Features

- Two difficulty levels
- Input validation for non-numeric and out-of-range guesses
- Clear feedback after every guess

## Possible improvements

- Add a scoring system based on number of attempts used
- Let the user choose a custom number range
- Add a "play again" loop without restarting the script
