##############################################
# YZV 102E/104E 24-25 Spring Term Midterm 1 Q1
##############################################

# Name Surname:
# Student ID:

###################################
# DO NOT ADD ANY ADDITIONAL IMPORTS

sample_table = {
    (0, 0): {'content': 'ID', 'style': 'right'},
    (0, 1): {'content': 'Course Name', 'style': 'left'},
    (0, 2): {'content': 'Credits', 'style': 'center'},
    (1, 0): {'content': '345', 'style': 'right'},
    (1, 1): {'content': 'Mathematics I', 'style': 'left'},
    (1, 2): {'content': '3', 'style': 'center'},
    (2, 0): {'content': '47', 'style': 'right'},
    (2, 1): {'content': 'Physics I', 'style': 'left'},
    (2, 2): {'content': '3', 'style': 'center'},
    (3, 0): {'content': '1423', 'style': 'right'},
    (3, 1): {'content': 'History II', 'style': 'left'},
    (3, 2): {'content': '3', 'style': 'center'},
}


def print_table(table_data):
    # TODO: FILL THE FUNCTION (HELPER FUNCTION/S CAN BE WRITTEN IF NEEDED)
    row_count, col_count = -1, -1
    for r, c in table_data.keys():
        row_count = r if r > row_count else row_count
        col_count = c if c > col_count else col_count
        # Another way to get the greater row and column counts
        # row_count = max(r, row_count)
        # col_count = max(c, col_count)
    row_count += 1
    col_count += 1

    # You could use a helper function for getting the column widths.
    col_widths = []
    for j in range(col_count):
        col_width = 0
        for i in range(row_count):
            cell_width = len(table_data[(i, j)]["content"])
            # Another way to get the greater column width
            # col_width = cell_width if cell_width > col_width else col_width
            col_width = max(cell_width, col_width)
        col_widths.append(col_width)

    for i in range(row_count):
        for j in range(col_count):
            cell_data = table_data[(i, j)]
            style = cell_data["style"]
            if style == "left":
                print(f"{cell_data['content']:<{col_widths[j]}}", end=" " if j < col_count - 1 else "")
            elif style == "center":
                print(f"{cell_data['content']:^{col_widths[j]}}", end=" " if j < col_count - 1 else "")
            elif style == "right":
                print(f"{cell_data['content']:>{col_widths[j]}}", end=" " if j < col_count - 1 else "")
        if i < row_count - 1:
            print()

    """
    # You can also create lists of strings, join them and print the final string like below
    # instead of using comprehension and print.
    rows = []
    for i in range(row_count):
        row_strings = []
        for j in range(col_count):
            cell_data = table_data[(i, j)]
            style = cell_data["style"]
            if style == "left":
                row_strings.append(f"{cell_data['content']:<{col_widths[j]}}")
            elif style == "center":
                row_strings.append(f"{cell_data['content']:^{col_widths[j]}}")
            elif style == "right":
                row_strings.append(f"{cell_data['content']:>{col_widths[j]}}")
        rows.append(" ".join(row_strings))
    print("\n".join(rows), end="")"""


if __name__ == '__main__':
    print_table(sample_table)
