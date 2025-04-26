##############################################
# YZV 102E/104E 23-24 Spring Term Midterm 1 Q3
##############################################

# Name Surname:
# Student ID:

###################################
# DO NOT ADD ANY ADDITIONAL IMPORTS

def mirror_encode(word):
    ### --- YOUR CODE HERE --- ###
    if len(word) < 2:
        return ""
    leftmost = word[0]
    rightmost = word[-1]
    if leftmost == rightmost:
        return mirror_encode(word[1:-1])
    else:
        return rightmost + leftmost + mirror_encode(word[1:-1]) + leftmost + rightmost


def is_palindrome(word):
    ### --- YOUR CODE HERE --- ###
    return len(mirror_encode(word)) == 0
    # return mirror_encode(word) == ""



# DO NOT EDIT THE CODE BELOW
if __name__ == "__main__":
    print("Word: \"BLEED\"", "Encoded:", "\"" + mirror_encode("BLEED") + "\"", "Is Palindrome:", is_palindrome("BLEED"))
    print("Word: \"ABBA\"", "Encoded:", "\"" + mirror_encode("ABBA") + "\"", "Is Palindrome:", is_palindrome("ABBA"))
    print("Word: \"RAPTOR\"", "Encoded:", "\"" + mirror_encode("RAPTOR") + "\"", "Is Palindrome:", is_palindrome("RAPTOR"))
    print("Word: \"LEVEL\"", "Encoded:", "\"" + mirror_encode("LEVEL") + "\"", "Is Palindrome:", is_palindrome("LEVEL"))
    print("Word: \"SPEAK\"", "Encoded:", "\"" + mirror_encode("SPEAK") + "\"", "Is Palindrome:", is_palindrome("SPEAK"))
    print("Word: \"ROTATOR\"", "Encoded:", "\"" + mirror_encode("ROTATOR") + "\"", "Is Palindrome:", is_palindrome("ROTATOR"))
