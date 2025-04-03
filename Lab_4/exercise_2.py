def average_above_threshold(lst:list, th:int):
    sum = 0
    num_of_elements = 0
    for n in lst:
        if n > th:
            num_of_elements += 1
            sum += n
    
    if num_of_elements == 0:
        return 0
    else:
        return sum/num_of_elements

lst1 = input("Enter a float list: ").split(" ")
lst1 = [float(item) for item in lst1]
threshold = float(input("Enter threshold: "))

result = average_above_threshold(lst1, threshold)

print("Result = %.5f" % result)