############################################## 
# YZV 102E/104E 23-24 Spring Term Midter 2 Q2
##############################################

# Name Surname:
# Student ID: 

###################################
# DO NOT ADD ANY ADDITIONAL IMPORTS
import sys
###################################

def extract_iban(transactions):
    """
    Extracts the IBAN numbers from the given transactions and prints the transactions in a sorted order.

        Args:
            transactions (list): A list that contains transactions.
        Returns:
            None
    """
    ##############################
    # YOUR CODE HERE
    split_ibans = map(lambda x:x.split(),transactions)
    filtered_ibans = filter(lambda x: x[0].startswith("TR") or x[1].startswith("TR") ,split_ibans)
    dict_ibans = list(map(lambda x: {"Sender": x[0], "Receiver": x[1]}, filtered_ibans))
    sorted_dict = sorted(dict_ibans, key= lambda x: x["Sender"])
    
    print(sorted_dict)
    # YOUR CODE HERE
    ##############################  
    pass


if __name__ == "__main__":
    transactions = list(sys.argv[1].split(","))
    extract_iban(transactions)