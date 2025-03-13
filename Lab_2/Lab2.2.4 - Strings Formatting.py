"""
YZV102E - Introduction to Programming for Data Science (Python)
Lab 2: Store and Access Data

Part 2: Strings
In this part, we will investigate the strings in Python.
"""

# printing some characters
# using triple quotes
str1 = '''She said, "What's up?"'''

#escaping single quotes
str2 = 'She said, "What\'s up?"'

# escaping double quotes
str3 = "She said, \"What's up?\""

print(str1)
print(str2)
print(str3)

#new line
print('\n')

#tab
print('1\t 2')

name = "Ali"
age = 23
city = "Istanbul"

#printing formatted string
print(name + " is " + str(age) + " years old and lives in " + city + ".")
print("{} is {} years old and lives in {}.".format(name, age, city))
print("{a} is {b} years old and lives in {c}.".format(a=name, b=age, c=city))
print("{a} is {b} years old and lives in {c}.".format(c=city, a=name, b=age))
print("%s is %d years old and lives in %s." % (name, age, city))
print(f"{name} is {age} years old and lives in {city}.")

#printing with precision
pi = 3.14159265359
print(f"{pi:.1f}")
print(f"{pi:.2f}")
print(f"{pi:.3f}")
print(f"{pi:.4f}")
print(f"{pi:.5f}")
