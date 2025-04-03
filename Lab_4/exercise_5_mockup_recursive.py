def decrypt_word(word:str):
    letter = ""
    if len(word) == 0:
        return ""
    
    elif word[0] >= word[-1]:
        return word[0] + (decrypt_word(word[1:-1]))
    else:
        return (decrypt_word(word[1:-1])) + word[-1]

def decrypt_sentence(sentence:str):
    words = sentence.split(" ")
    final_sentence = " ".join([decrypt_word(word) for word in words])
    return final_sentence

sentence = input()

print(decrypt_sentence(sentence))

