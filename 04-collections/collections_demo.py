"""Python Collections demo: lists, tuples, sets, and dictionaries.

Run it: python collections_demo.py
"""


def lists_demo():
    fruits = ["apple", "banana", "cherry"]
    print("index 0:", fruits[0])       # apple
    print("last:", fruits[-1])         # cherry
    print("slice:", fruits[1:3])       # ['banana', 'cherry']

    fruits.append("date")              # add to the end
    fruits.insert(1, "apricot")        # add at a position
    fruits.remove("banana")            # remove by value
    fruits.pop()                       # remove and return the last item

    ordered = sorted(fruits)           # new sorted list
    print("sorted:", ordered)

    squares = [n * n for n in range(1, 6)]      # list comprehension
    evens = [n for n in range(10) if n % 2 == 0]
    print("squares:", squares)
    print("evens:", evens)


def tuples_demo():
    point = (3, 4)
    x, y = point                       # unpacking
    print("x, y:", x, y)


def sets_demo():
    seen = {"a", "b", "a"}             # duplicate dropped
    seen.add("c")
    print("membership:", "b" in seen)  # fast lookup

    a = {1, 2, 3}
    b = {3, 4, 5}
    print("union:", a | b)
    print("intersection:", a & b)
    print("difference:", a - b)


def dicts_demo():
    person = {"name": "Ada", "role": "engineer"}
    print("name:", person["name"])         # [] access
    print("age:", person.get("age", 0))    # .get() with default

    person["age"] = 36                     # add
    person["role"] = "lead"                # update
    person.update({"city": "London"})

    for key, value in person.items():      # iterate items
        print(f"  {key}: {value}")

    lengths = {w: len(w) for w in ["hi", "hello"]}  # dict comprehension
    print("lengths:", lengths)


def nesting_demo():
    team = [
        {"name": "Ada", "skills": ["python", "sql"]},
        {"name": "Ravi", "skills": ["python", "go"]},
    ]
    print("nested:", team[0]["skills"][1])  # sql


if __name__ == "__main__":
    lists_demo()
    tuples_demo()
    sets_demo()
    dicts_demo()
    nesting_demo()
