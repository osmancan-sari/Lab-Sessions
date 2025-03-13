"""
YZV102E - Introduction to Programming for Data Science (Python)
Lab 2: Store and Access Data

Part 3: Dictionaries
In this part, we will investigate the dictionaries in Python.
"""

dict0 = {}
dict1 = {'name': 'Ali', 'age': 23, 'city': 'Istanbul'}
dict2 = {'name': 'Ali', 'age': 23, 'city': 'Istanbul', 'age': 24}
dict3 = dict({'name':'Ali', 'age':'23', 1:1})
print(dict0)
print(dict1)
print(dict2)
print(dict3)

dict0["age"] = 23
dict1["name"] = "Aylin"
print(dict0)
print(dict1)

item = dict3.pop('name')
print(item)
print(dict3)

dict3.clear()
print(dict3)