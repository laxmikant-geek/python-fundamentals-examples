"""FizzBuzz: a classic showcase of range(), modulo, and ordered conditionals.

Prints 1..20, replacing multiples of 3 with "Fizz", multiples of 5 with
"Buzz", and multiples of both with "FizzBuzz". Check the "both" case first.
"""


def fizzbuzz(limit: int = 20) -> None:
    for n in range(1, limit + 1):
        if n % 15 == 0:          # divisible by both 3 and 5
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)


if __name__ == "__main__":
    fizzbuzz()
