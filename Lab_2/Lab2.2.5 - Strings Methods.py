"""
YZV102E - Introduction to Programming for Data Science (Python)
Lab 2: Store and Access Data

Part 2: Strings
In this part, we will investigate the strings in Python.
"""
str1 = "ITU is a large city university with campuses located in the central points of Istanbul."
str2 = "itu"

print(str2.capitalize())
print(str1.count("a"))
print(str1.startswith("i"))
print(str1.startswith("I"))
print(str1.startswith("It"))
print(str1.startswith("IT"))
print(str1.endswith("istanbul"))
print(str1.endswith("Istanbul"))
print(str1.find("itu"))
print(str1.find("IT"))
print(str1.find("TU"))
print(str2.isupper())
print(str2.islower())
print(str1.replace("ITU", "_IT¨U"))
print(str1.replace("itu", "_IT¨U"))
print(str1.split())
print(str1.split(" "))
print(str1.split("is"))
