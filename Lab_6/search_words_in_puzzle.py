##############################################
# YZV 102E/104E 24-25 Spring Term Midterm Exam Q2
##############################################

# Name Surname: Osmancan Sarı
# Student ID: 150230728

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
    f = open(vocabulary_file)
    words_to_find = []
    for line in f:
        words_to_find.append(line.strip())
     
    puzzle_vertical = ["","","","","","","",""]
    for line in puzzle:
        for i in range(0,len(line)):
            puzzle_vertical[i] += line[i]
    for word in words_to_find:
        for line_number in range(0, len(puzzle)):
            for index in range(0, len(puzzle[line_number])-len(word)+1):
                if puzzle[line_number][index:index+len(word)] == word:
                    found_words.append((word, line_number, index, "H"))
        for line_number in range(0, len(puzzle_vertical)):
            for index in range(0, len(puzzle_vertical[line_number])-len(word)+1):
                if puzzle_vertical[line_number][index:index+len(word)] == word:
                    found_words.append((word, index, line_number, "V"))
         
    ### --- END OF YOUR CODE ---
    return found_words


if __name__ == '__main__':
    print(search_words_in_puzzle(PUZZLE, 'vocab.txt'))
