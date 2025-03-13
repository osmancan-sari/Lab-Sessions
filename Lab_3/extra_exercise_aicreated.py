"""
Exercise: Word Frequency Counter

Write a program that:
1. Takes a text input from the user
2. Counts the frequency of each word in the text
3. Displays the results in alphabetical order

Example:
Input: "The quick brown fox jumps over the lazy dog"
Output:
brown: 1
dog: 1
fox: 1
jumps: 1
lazy: 1
over: 1
quick: 1
the: 2

Hint: You might want to use:
- split() method to separate words
- dictionary to store word frequencies
- sorted() function to sort the results
- lower() method to handle case sensitivity
"""

# Write your solution below this line 
text = input("Please enter a text: ")
text = text.lower()
words = text.split()

word_frequency = {}

words_set = set(words)

for word in words_set:
    word_frequency[word] = words.count(word)

sorted_word_frequency = sorted(word_frequency.items())
print(sorted_word_frequency)
