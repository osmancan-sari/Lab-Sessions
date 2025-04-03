def is_polindrome(word:str):
    if len(word) <=1:
        return True
    elif word[0] != word[-1]:
        return False
    else:
        return is_polindrome(word[1:-1])
    
word = input()

if is_polindrome(word):
    print("True")
else:
    print("False")