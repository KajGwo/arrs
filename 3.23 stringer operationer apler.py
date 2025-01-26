import my_text

text = "An apple a day keeps the doctor away"

num_words = my_text.counter(text)
words_longest_to_shortest = my_text.longotshort(text)
words_alphabetically = my_text.alph(text)

print(f"Text: {text}")
print(f"Number of words: {num_words}")
print(f"Words from the longest: {', '.join(words_longest_to_shortest)}")
print(f"Words ordered alphabetically: {', '.join(words_alphabetically)}")