def recursive_sum_of_list(lst:list):
    if len(lst) == 1:
        return lst[0]
    return lst[0] + recursive_sum_of_list(lst[1:])

lst1 = input("Enter a list: ").split(" ")
lst1 = [float(i) for i in lst1]

result = (recursive_sum_of_list(lst1))
print("Result: %.5f" % result)