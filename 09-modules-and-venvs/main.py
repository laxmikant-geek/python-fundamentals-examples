# main.py — imports our own module plus a few standard-library ones.
import random
from datetime import date

import greetings  # our module: greetings.py in the same folder


def main():
    names = ["Grace", "Linus", "Ada"]
    print(greetings.greet(random.choice(names)))
    print(greetings.shout("Linus"))
    print(f"Generated on {date.today().isoformat()}")


if __name__ == "__main__":
    main()
