def reverse_string(string: str):
    if len(string)==0:
        return ""
    return string[-1] + reverse_string(string[0:-1])

word = input()

print(reverse_string(word))