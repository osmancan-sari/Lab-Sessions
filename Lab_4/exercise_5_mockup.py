def decrypt_word(word:str):
    left_side = ""
    right_side = ""
    i=0
    while i < len(word)/2:
        if word[i] >= word[-(i+1)]:
            left_side += word[i]
        else:
            right_side += word[-(i+1)]
        
        i += 1
    return left_side + right_side[::-1]

def decrypt_sentence(sentence:str):
    words = sentence.split(" ")
    final_sentence = " ".join([decrypt_word(word) for word in words])
    return final_sentence

sentence = input("Enter sentence: ")

print(decrypt_sentence(sentence))