##############################################
# YZV 102E/104E 23-24 Spring Term Midterm 1 Q3
##############################################

# Name Surname: Osmancan Sarı
# Student ID: 150230728

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
    # TODO: FILL THE FUNCTION (HELPER FUNCTION/S CAN BE WRITTEN IF NEEDED
    all_keys = list(table_data.keys())
    n_rows = all_keys[-1][0] + 1
    n_columns = all_keys[-1][1] + 1
    
    for row_n in range(0, n_rows):
        for col_n in range(0, n_columns):
            if table_data[(row_n, col_n)]["style"] == 'right':
                print('{0:{fill}{<}16}'.format(table_data[(row_n, col_n)]['content'], fill=" ", align=<))

            elif table_data[(row_n, col_n)]["style"] == 'left':
                print('{0:{fill}{>}16}'.format(table_data[(row_n, col_n)]['content'], fill=" ", align=>))

            else:
                print('{0:{fill}{^}16}'.format(table_data[(row_n, col_n)]['content'], fill=" ", align=^))

    
if __name__ == '__main__':
    print_table(sample_table)
