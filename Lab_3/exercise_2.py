str1 = input("Please enter a string: ")
digit = 0
upper = 0
lower = 0
vowel = 0
consonant = 0

for ch in str1:
    if ch.isdigit():
        digit += 1
    elif ch.isalpha():
        if ch.isupper():
            upper += 1
        else:
            lower += 1

        if ch.lower() in "aeiou":
            vowel += 1
        else:
            consonant += 1

print("Number of digits", digit)
print("Number of upper letters", upper)
print("Number of lower letters", lower)
print("Number of vowels", vowel)
print("Number of consonants", consonant)