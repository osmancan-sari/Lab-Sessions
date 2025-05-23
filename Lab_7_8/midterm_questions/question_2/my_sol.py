##########################################
# YZV 102E/104E 23-24 Spring Term Final Q3
##########################################

# Name Surname:
# Student ID:

###################################
# DO NOT ADD ANY ADDITIONAL IMPORTS
###################################

class Stock:
    def __init__(self, stock_type, amount=0):
        if not isinstance(stock_type, str) or len(stock_type) == 0:
            raise TypeError("Stock type must be a string and cannot be empty.")
        if not isinstance(amount, (int, float)) or amount<0:
            raise ValueError("Stock amount must be an integer or a float and it should not be negative.")
        self.type = stock_type
        self.amount = amount
    
    def __add__(self, other):
        if isinstance(other, self.__class__):
            if other.type != self.type:
                raise TypeError(f"Stock types cannot be different during the addition of two {self.__class__} objects.")
            else:
                return Stock(self.type, self.amount + other.amount)
        elif isinstance(other, (int, float)):
            if other<0:
                raise ValueError(f"Addition operator for {self.__class__} cannot accept negative values.")
            else:
                return Stock(self.type, self.amount + other)
        else:
            raise TypeError(f"Addition operator for {self.__class__} can only support {self.__class__}, integer, or float.")
    
    def __sub__(self, other):
        if isinstance(other, self.__class__):
            if other.type != self.type:
                raise TypeError(f"Stock types cannot be different during the subtraction of two {self.__class__} objects.")
            elif other.amount > self.amount:
                raise ValueError(f"{self.__class__} objects cannot subtract {self.__class__} objects with amounts greater than its amount.")
            else:
                return Stock(self.type, self.amount - other.amount)
        elif isinstance(other, (int, float)):
            if other < 0:
                raise ValueError(f"Subtraction operator for {self.__class__} cannot accept negative values.")
            elif other > self.amount:
                raise ValueError(f"{self.__class__} objects cannot subtract values greater than its amount.")
            else:
                return Stock(self.type, self.amount - other)
        else:
            raise TypeError(f"Subtraction operator for {self.__class__} can only support {self.__class__}, integer, or float.")
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            if other < 0:
                raise ValueError(f"Multiplication operator for {self.__class__} cannot accept negative values.")
            else:
                return Stock(self.type, self.amount * other)
        
        else:
            raise TypeError(f"Multiplication operator for {self.__class__} can only support integer or float.")
    
    def __lt__(self, other):
        if isinstance(other, self.__class__):
            if other.type != self.type:
                raise TypeError(f"Stock types cannot be different while comparing two {self.__class__} objects.")
            else:
                return self.amount < other.amount
        elif isinstance(other, (int, float)):
            return self.amount < other
        else:
            raise TypeError(f"Less than operator for {self.__class__} can only support {self.__class__}, integer, or float.")
  
    def __str__(self):
        return f"A stock of {self.type} with the amount of {self.amount:.2f}"

    
        
            

###################################
# DO NOT EDIT THE CODE BELOW
#########################################################################################
# The main process is for you to see how your code behaves. It is not a grading criteria.
# You can see the expected output of this main process in expected_output_of_main.txt.
# Your code will be evaluated by test cases not by expected_output_of_main.txt.
#########################################################################################

if __name__ == "__main__":
    try:
        print(Stock("Apple", 3))
    except Exception as e:
        print(e)
    try:
        print()
        print(Stock("Apple", 4.5))
    except Exception as e:
        print(e)
    try:
        print()
        print(Stock("Apple", 4.55))
    except Exception as e:
        print(e)
    try:
        print()
        print(Stock("Apple", 4.55555555))
    except Exception as e:
        print(e)
    try:
        print()
        print(Stock("Apple"))
    except Exception as e:
        print(e)
    try:
        print()
        print(Stock(1.5))
    except Exception as e:
        print(e)
    try:
        print()
        print(Stock(""))
    except Exception as e:
        print(e)
    try:
        print()
        print(Stock("Apple", "1.5"))
    except Exception as e:
        print(e)
    try:
        print()
        print(Stock("Apple", -5))
    except Exception as e:
        print(e)
    try:
        print()
        s1 = Stock("Apple", 1)
        s2 = Stock("Apple", 4)
        print("s1:", s1)
        print("s2:", s2)
        s3 = s1 + s2
        print("After calculation")
        print("s1:", s1)
        print("s2:", s2)
        print("s3 = s1 + s2:", s3)
    except Exception as e:
        print(e)
    try:
        print()
        s1 = Stock("Apple", 1)
        print("s1:", s1)
        s2 = s1 + 4
        print("After calculation")
        print("s1:", s1)
        print("s2 = s1 + 4:", s2)
    except Exception as e:
        print(e)
    try:
        print()
        s1 = Stock("Apple", 1)
        print("s1:", s1)
        s2 = s1 + 4.5
        print("After calculation")
        print("s1:", s1)
        print("s2 = s1 + 4.5:", s2)
    except Exception as e:
        print(e)
    try:
        print()
        s1 = Stock("Apple", 1)
        s2 = Stock("Orange", 4)
        print("s1:", s1)
        print("s2:", s2)
        s3 = s1 + s2
        print("After calculation")
        print("s1:", s1)
        print("s2:", s2)
        print("s3 = s1 + s2:", s3)
    except Exception as e:
        print(e)
    try:
        print()
        s1 = Stock("Apple", 1)
        print("s1:", s1)
        s2 = s1 + -3
        print("After calculation")
        print("s1:", s1)
        print("s2 = s1 + -3:", s2)
    except Exception as e:
        print(e)
    try:
        print()
        s1 = Stock("Apple", 1)
        print("s1:", s1)
        s2 = s1 + "3"
        print("After calculation")
        print("s1:", s1)
        print('s2 = s1 + "3":', s2)
    except Exception as e:
        print(e)
    try:
        print()
        s1 = Stock("Apple", 4)
        s2 = Stock("Apple", 1)
        print("s1:", s1)
        print("s2:", s2)
        s3 = s1 - s2
        print("After calculation")
        print("s1:", s1)
        print("s2:", s2)
        print("s3 = s1 - s2:", s3)
    except Exception as e:
        print(e)
    try:
        print()
        s1 = Stock("Apple", 4)
        print("s1:", s1)
        s2 = s1 - 1
        print("After calculation")
        print("s1:", s1)
        print("s2 = s1 - 1:", s2)
    except Exception as e:
        print(e)
    try:
        print()
        s1 = Stock("Apple", 4)
        print("s1:", s1)
        s2 = s1 - 1.5
        print("After calculation")
        print("s1:", s1)
        print("s2 = s1 - 1.5:", s2)
    except Exception as e:
        print(e)
    try:
        print()
        s1 = Stock("Apple", 4)
        s2 = Stock("Orange", 1)
        print("s1:", s1)
        print("s2:", s2)
        s3 = s1 - s2
        print("After calculation")
        print("s1:", s1)
        print("s2:", s2)
        print("s3 = s1 - s2:", s3)
    except Exception as e:
        print(e)
    try:
        print()
        s1 = Stock("Apple", 1)
        s2 = Stock("Orange", 4)
        print("s1:", s1)
        print("s2:", s2)
        s3 = s1 - s2
        print("After calculation")
        print("s1:", s1)
        print("s2:", s2)
        print("s3 = s1 - s2:", s3)
    except Exception as e:
        print(e)
    try:
        print()
        s1 = Stock("Apple", 1)
        print("s1:", s1)
        s2 = s1 - -3
        print("After calculation")
        print("s1:", s1)
        print("s2 = s1 - -3:", s2)
    except Exception as e:
        print(e)
    try:
        print()
        s1 = Stock("Apple", 1)
        print("s1:", s1)
        s2 = s1 - 3
        print("After calculation")
        print("s1:", s1)
        print("s2 = s1 - 3:", s2)
    except Exception as e:
        print(e)
    try:
        print()
        s1 = Stock("Apple", 1)
        print("s1:", s1)
        s2 = s1 - "3"
        print("After calculation")
        print("s1:", s1)
        print('s2 = s1 - "3":', s2)
    except Exception as e:
        print(e)
    try:
        print()
        s1 = Stock("Apple", 4)
        print("s1:", s1)
        s2 = s1 * 2
        print("After calculation")
        print("s1:", s1)
        print("s2 = s1 * 2:", s2)
    except Exception as e:
        print(e)
    try:
        print()
        s1 = Stock("Apple", 3)
        print("s1:", s1)
        s2 = s1 * 1.5
        print("After calculation")
        print("s1:", s1)
        print("s2 = s1 * 1.5:", s2)
    except Exception as e:
        print(e)
    try:
        print()
        s1 = Stock("Apple", 1)
        print("s1:", s1)
        s2 = s1 * -3
        print("After calculation")
        print("s1:", s1)
        print("s2 = s1 * -3:", s2)
    except Exception as e:
        print(e)
    try:
        print()
        s1 = Stock("Apple", 4)
        s2 = Stock("Apple", 1)
        print("s1:", s1)
        print("s2:", s2)
        s3 = s1 * s2
        print("After calculation")
        print("s1:", s1)
        print("s2:", s2)
        print("s3 = s1 * s2:", s3)
    except Exception as e:
        print(e)
    try:
        print()
        s1 = Stock("Apple", 1)
        s2 = Stock("Apple", 4)
        print("s1:", s1)
        print("s2:", s2)
        print("s1 < s2", s1 < s2)
    except Exception as e:
        print(e)
    try:
        print()
        s1 = Stock("Apple", 1)
        print("s1:", s1)
        print("s1 < 4", s1 < 4)
    except Exception as e:
        print(e)
    try:
        print()
        s1 = Stock("Apple", 1)
        print("s1:", s1)
        print("s1 < 4.5", s1 < 4.5)
    except Exception as e:
        print(e)
    try:
        print()
        s1 = Stock("Apple", 1)
        s2 = Stock("Apple", 1)
        print("s1:", s1)
        print("s2:", s2)
        print("s1 < s2", s1 < s2)
    except Exception as e:
        print(e)
    try:
        print()
        s1 = Stock("Apple", 1)
        print("s1:", s1)
        print("s1 < 1", s1 < 1)
    except Exception as e:
        print(e)
    try:
        print()
        s1 = Stock("Apple", 1.5)
        print("s1:", s1)
        print("s1 < 1.5", s1 < 1.5)
    except Exception as e:
        print(e)
    try:
        print()
        s1 = Stock("Apple", 4)
        s2 = Stock("Apple", 1)
        print("s1:", s1)
        print("s2:", s2)
        print("s1 < s2", s1 < s2)
    except Exception as e:
        print(e)
    try:
        print()
        s1 = Stock("Apple", 4)
        print("s1:", s1)
        print("s1 < 1", s1 < 1)
    except Exception as e:
        print(e)
    try:
        print()
        s1 = Stock("Apple", 4)
        print("s1:", s1)
        print("s1 < 1.5", s1 < 1.5)
    except Exception as e:
        print(e)
    try:
        print()
        s1 = Stock("Apple", 4)
        s2 = Stock("Orange", 1)
        print("s1:", s1)
        print("s2:", s2)
        print("s1 < s2", s1 < s2)
    except Exception as e:
        print(e)
    try:
        print()
        s1 = Stock("Apple", 1)
        print("s1:", s1)
        print('s1 < "3"', s1 < "3")
    except Exception as e:
        print(e)

