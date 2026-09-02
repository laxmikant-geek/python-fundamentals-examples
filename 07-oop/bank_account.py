"""BankAccount: a small class demonstrating encapsulation and dunder methods.

Run it: python bank_account.py
Part of the Python Fundamentals series on GeeksArray.
"""


class BankAccount:
    """A simple bank account with a protected balance."""

    currency = "USD"  # class attribute, shared by every account

    def __init__(self, owner, balance=0):
        # instance attributes, unique to each object
        self.owner = owner
        self._balance = balance  # leading underscore: "internal, please don't touch"

    @property
    def balance(self):
        """Read-only view of the current balance."""
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        return self._balance

    def __str__(self):
        # friendly, for end users (used by print)
        return f"{self.owner}'s account: {self._balance} {self.currency}"

    def __repr__(self):
        # unambiguous, for developers
        return f"BankAccount({self.owner!r}, {self._balance})"


if __name__ == "__main__":
    acc = BankAccount("Ada", 100)
    print(acc)                 # Ada's account: 100 USD
    acc.deposit(50)
    print("After deposit:", acc.balance)   # 150
    acc.withdraw(30)
    print("After withdraw:", acc.balance)  # 120
    print(repr(acc))           # BankAccount('Ada', 120)

    try:
        acc.withdraw(1000)
    except ValueError as err:
        print("Rejected:", err)
