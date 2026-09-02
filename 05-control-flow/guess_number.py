"""A small number-guessing game.

Demonstrates `while True`, `break`, `continue`, comparison operators, and
truthiness for input validation. The program picks a secret number and loops
until the player guesses it.

Run it:  python guess_number.py
"""

import random


def play(low: int = 1, high: int = 100) -> None:
    secret = random.randint(low, high)
    tries = 0

    print(f"I'm thinking of a number between {low} and {high}.")

    while True:
        raw = input("Your guess: ").strip()

        # Skip empty or non-numeric input without counting it as a try.
        if not raw or not raw.lstrip("-").isdigit():
            print("Please enter a whole number.")
            continue

        guess = int(raw)
        tries += 1

        if guess < secret:
            print("Too low! Try higher.")
        elif guess > secret:
            print("Too high! Try lower.")
        else:
            print(f"Correct! You got it in {tries} tries.")
            break


if __name__ == "__main__":
    play()
