##############################################
# YZV 102E/104E 24-25 Spring Term Midterm Exam Q2
##############################################

# Name Surname:
# Student ID:

###################################
# DO NOT ADD ANY IMPORTS
###################################

PUZZLE = [
    'AGMAERET',
    'WSLFDAYT',
    'FLCARHEH',
    'SWZLIPUN',
    'KGFMVOLT',
    'BRAKENIY',
    'LAESRQRR',
    'ZYBNERTE',
]

def search_words_in_puzzle(puzzle, vocabulary_file):
    """
        The function searches for words in a given puzzle and returns a list of found words.

        Args:
            puzzle (list): A list of strings representing the puzzle.
            vocabulary_file (str): The path to the vocabulary file.

        Returns:
            list: A list of found words.
    """

    # Initialize an empty list to store found words
    found_words = [] # Do not change this line

    ### --- YOUR CODE HERE --- ###
    with open(vocabulary_file, "r") as f:
        words = list(f.readlines())
        words = [word.replace("\n", "") for word in words]

    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            # Horizontal search
            for end in range(j + 1, len(puzzle[0]) + 1):
                potential_word = puzzle[i][j:end]
                if potential_word in words:
                    found_words.append((potential_word, i, j, "H"))
            # Vertical search
            potential_word = puzzle[i][j]
            if potential_word in words:
                found_words.append((potential_word, i, j, "V")) # One letter word option
            for end in range(i + 1, len(puzzle)): # The rest of the length options
                potential_word += puzzle[end][j]
                if potential_word in words:
                    found_words.append((potential_word, i, j, "V"))

    ### --- END OF YOUR CODE ---
    return found_words


if __name__ == '__main__':
    print(search_words_in_puzzle(PUZZLE, 'vocab.txt'))
