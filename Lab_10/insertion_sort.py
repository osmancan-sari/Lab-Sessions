import random

def insertion_sort(lst):
    for i in range(1,len(lst)):
        temp = lst[i]
        j = i
        while j>0 and lst[j-1]>temp:
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = temp
    return lst
lst1 = [random.randint(1,100) for i in range(10)]
print(lst1)
print(insertion_sort(lst1))
