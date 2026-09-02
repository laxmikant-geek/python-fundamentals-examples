# greet.py — ask for a name and greet the user
# Run it: python greet.py

# input() waits for the user to type something and press Enter,
# then returns it as a string.
name = input("What's your name? ")

# The f before the quotes makes this an f-string; the expression
# inside {curly braces} is replaced with its value.
print(f"Hello, {name}! Welcome to Python.")

# A small extra: show how many characters are in the name.
print(f"Your name has {len(name)} characters.")
