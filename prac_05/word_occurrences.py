"""Estimate about 20 minutes"""
user_input = input("Please enter a string: ")
words = user_input.split()
string_to_word = {"this", "is", "a", "collection", "of", "words", "of", "nice", "words", "this", "is", "a", "fun",
                  "thing", "it", "is"}
for word in words:
    word = word.lower()
    if word in string_to_word:
        string_to_word[] += 1
    else:
        string_to_word[word] = 1

print("\nWord Occurrences:")
for word, count in string_to_word.items():
    print(f"{word}: {count}")