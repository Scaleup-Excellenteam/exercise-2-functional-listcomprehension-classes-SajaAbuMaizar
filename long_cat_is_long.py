import string


def count_words(text):
    table = text.maketrans("", "", string.punctuation)
    words = text.translate(table).lower().split()
    return {word: len(word) for word in words}


text1 = """
You see, wire telegraph is a kind of a very, very long cat.
You pull his tail in New York and his head is meowing in Los Angeles.
Do you understand this?
And radio operates exactly the same way: you send signals here, they receive them there.
The only difference is that there is no cat.
"""

print(count_words(text1))