def recursive_sum_of_digits_in_integer(i:int):
    if i//10 == 0:
        return i
    str_i = str(i)
    return int(str_i[-1]) + recursive_sum_of_digits_in_integer(i//10)

num1 = int(input("Enter an integer: "))

print(recursive_sum_of_digits_in_integer(num1))