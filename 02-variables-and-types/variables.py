"""Variables, types, and arithmetic — the building blocks.

Run it: python variables.py
"""

# --- Assignment ---
name = "Ada"
age = 36
pi = 3.14159
print(name, age, pi)

# Multiple assignment and swapping
x, y = 10, 20
x, y = y, x
print("after swap:", x, y)  # 20 10

# --- Dynamic typing: one name, different types over time ---
data = 42
print(type(data))   # <class 'int'>
data = "hello"
print(type(data))   # <class 'str'>

# --- The core types ---
count = 3           # int
temperature = 36.6  # float
is_ready = True     # bool
result = None       # NoneType
label = "score"     # str

# --- Checking types ---
print(isinstance(count, int))                  # True
print(isinstance(temperature, (int, float)))   # True
print(type(result))                            # <class 'NoneType'>

# --- Arithmetic operators ---
print(7 / 2)    # 3.5   true division (always float)
print(7 // 2)   # 3     floor division
print(7 % 2)    # 1     remainder (modulo)
print(2 ** 10)  # 1024  power

# Split 135 minutes into hours and minutes
minutes = 135
print(minutes // 60, "h", minutes % 60, "m")  # 2 h 15 m

# --- Precedence ---
print(2 + 3 * 4)     # 14
print((2 + 3) * 4)   # 20

# --- Augmented assignment ---
total = 100
total += 20   # 120
total -= 5    # 115
total *= 2    # 230
print("total:", total)

# --- Type conversion ---
price = float("19.99")
year = int("2026")
text = str(42)
print(price, year, text)
print(bool(0), bool(""), bool(None), bool(7))  # False False False True

# --- Constant by convention ---
TAX_RATE = 0.20
print("tax on 50:", 50 * TAX_RATE)
