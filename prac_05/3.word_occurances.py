"""
CP1404/CP5632 Practical
Word occurrences in a string
"""

# User input for a string
text = input("Text: ")

# Split the input text into words and count the occurrences of each word
word_counts = {}
for word in text.split():
    word_counts[word] = word_counts.get(word, 0) + 1

# Sort the word counts and find the maximum word length for formatting
sorted_word_counts = sorted(word_counts.items())
max_word_length = max(len(word) for word in word_counts)

# Print the word occurrences with proper formatting
for word, count in sorted_word_counts:
    print(f"{word:{max_word_length}} : {count}")
