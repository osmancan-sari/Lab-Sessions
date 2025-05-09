##############################################
# YZV 102E/104E 23-24 Spring Term Midterm 1 Q3
##############################################

# Name Surname: Osmancan Sarı
# Student ID: 150230728

###################################
# DO NOT ADD ANY ADDITIONAL IMPORTS

def mirror_encode(word):
    left_side = ""
    right_side = ""
    word_len = len(word)
    if word_len <= 1:
        return ""
    else:
        if word[0] != word[-1]:
            left_side += word[-1] + word[0]
            right_side += word[0] + word[-1]

    
    return left_side + mirror_encode(word[1:-1]) + right_side


def is_palindrome(word):
    encoded_word = mirror_encode(word)
    if len(encoded_word) <= 1:
        return True
    else:
        return False



# DO NOT EDIT THE CODE BELOW
if __name__ == "__main__":
    print("Word: \"BLEED\"", "Encoded:", "\"" + mirror_encode("BLEED") + "\"", "Is Palindrome:", is_palindrome("BLEED"))
    print("Word: \"ABBA\"", "Encoded:", "\"" + mirror_encode("ABBA") + "\"", "Is Palindrome:", is_palindrome("ABBA"))
    print("Word: \"RAPTOR\"", "Encoded:", "\"" + mirror_encode("RAPTOR") + "\"", "Is Palindrome:", is_palindrome("RAPTOR"))
    print("Word: \"LEVEL\"", "Encoded:", "\"" + mirror_encode("LEVEL") + "\"", "Is Palindrome:", is_palindrome("LEVEL"))
    print("Word: \"SPEAK\"", "Encoded:", "\"" + mirror_encode("SPEAK") + "\"", "Is Palindrome:", is_palindrome("SPEAK"))
    print("Word: \"ROTATOR\"", "Encoded:", "\"" + mirror_encode("ROTATOR") + "\"", "Is Palindrome:", is_palindrome("ROTATOR"))
