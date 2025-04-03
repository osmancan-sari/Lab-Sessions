##############################################
# YZV 102E/104E 23-24 Spring Term Midterm 1 Q3
##############################################

# Name Surname:
# Student ID:

###################################
# DO NOT ADD ANY ADDITIONAL IMPORTS

def decrypt_word(word):
    if len(word) == 0:
        # BASE CASE: Trace back if the word has no letters anymore!
        return ""
    
    if word[0] < word[-1]:
        sub_word = decrypt_word(word[1:-1]) + word[-1] # if leftmost is smaller, remove leftmost one
        return sub_word
        # rightmost letter will be retained in the end; so, string addition performed before the further comparisons
        # recursion starts with the remaining letters!
    else:
        sub_word = word[0] + decrypt_word(word[1:-1]) # if rightmost is smaller, remove the rightmost one
        return sub_word
        # leftmost letter will be retained in the end; so, string addition performed before the further comparisons
        # recursion starts with the remaining letters!

        # Tip: When using slicing, Python gracefully handles out-of-range indexes. Instead of raising an error,
        # it simply returns an empty string ('') if the slice indices don't correspond to a valid range within the string.


def decrypt_sentence(sentence):
    decrypted_sentence = []
    for word in sentence.split():
        decrypted_sentence.append(decrypt_word(word))
    
    return " ".join(decrypted_sentence)



# DO NOT EDIT THE CODE BELOW
if __name__ == "__main__":
    user_input = input()
    while user_input.upper() != "EXIT":
        print(decrypt_sentence(user_input))
        user_input = input()
