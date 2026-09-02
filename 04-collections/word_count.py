"""Count how often each word appears in a piece of text.

Run it: python word_count.py
"""


def count_words(text):
    """Return a dict mapping each lower-cased word to its frequency."""
    counts = {}
    for word in text.lower().split():
        # .get(word, 0) starts a new word at zero on first sight
        counts[word] = counts.get(word, 0) + 1
    return counts


if __name__ == "__main__":
    text = "the cat sat on the mat the cat purred"
    counts = count_words(text)
    for word, n in sorted(counts.items()):
        print(f"{word}: {n}")
