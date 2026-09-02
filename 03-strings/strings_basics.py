"""String fundamentals: literals, slicing, immutability, methods, f-strings.

Part of the Python Fundamentals series on GeeksArray.
Run it: python strings_basics.py
"""


def quotes_and_escapes():
    single = 'She said hi'
    double = "It's a nice day"          # double quotes avoid escaping the apostrophe
    raw_path = r"C:\Users\name"          # raw string: backslashes stay literal
    print(single)
    print(double)
    print(raw_path)
    print("Name:\tAda\nRole:\tEngineer")  # \t tab, \n newline

    multiline = """Dear Ada,
Thanks for signing up.
The Team"""
    print(multiline)


def indexing_and_slicing():
    word = "Python"
    print(word[0])      # P  (first character)
    print(word[-1])     # n  (last character)
    print(word[0:3])    # Pyt (stop index is excluded)
    print(word[3:])     # hon
    print(word[::-1])   # nohtyP (reversed)


def immutability():
    name = "ada"
    name.upper()            # returns "ADA" but the result is discarded
    print(name)             # still "ada"
    name = name.upper()     # must assign to keep the change
    print(name)             # "ADA"


def common_methods():
    raw = "  hello, world, hello  "
    print(raw.strip())                  # remove surrounding whitespace
    print(raw.strip().split(", "))      # -> list of parts
    print(raw.count("hello"))           # 2
    print(", ".join(["a", "b", "c"]))   # "a, b, c"
    print(raw.replace("hello", "hi"))
    print(raw.strip().startswith("hello"))
    print(raw.find("world"))            # index, or -1 if absent
    print("world" in raw)               # membership test
    print(len("Python"))                # 6


def formatting():
    name, score = "Ada", 92.4567
    print(f"{name} scored {score:.2f}")   # two decimals
    print(f"{name:>10}|")                 # right-align in 10 columns
    print(f"{name:<10}|")                 # left-align
    print(f"{7:03d}")                     # zero-padded integer -> 007
    print("Hi " + name)                   # concatenation
    print("-" * 20)                       # repetition


if __name__ == "__main__":
    for demo in (quotes_and_escapes, indexing_and_slicing,
                 immutability, common_methods, formatting):
        print(f"--- {demo.__name__} ---")
        demo()
