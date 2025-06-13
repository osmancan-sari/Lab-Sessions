import random

def selection_sort(lst):
    for i in range(len(lst)-1):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j]<lst[min_index]:
                min_index = j
        temp = lst[i]
        lst[i] = lst[min_index]
        lst[min_index] = temp
    return lst
lst1 = [random.randint(1,100) for i in range(10)]
print(lst1)
print(selection_sort(lst1))