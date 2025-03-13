"""
YZV102E - Introduction to Programming for Data Science (Python)
Lab 2: Store and Access Data

Part 1: Lists
This section covers list creation and basic operations in Python.
"""

lst = [1, 2, 3, 4, 5, 6]
print(lst)

lst.append(0)
print(lst)

lst.insert(0, -1)
print(lst)

last_item = lst.pop()
print(last_item)
print(lst)

item = lst.pop(1)
print(item)
print(lst)

lst.remove(5)
print(lst)

lst.extend([3, 4, 6, 7])
print(lst)

lst.sort()
print(lst)

lst.reverse()
print(lst)

print(len(lst))

lst.clear()
print(len(lst))
print(lst)
