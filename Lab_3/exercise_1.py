n1 = 0
while n1 <= 0:
    n1 = int(input("Enter the length of the first array: "))
    if n1 <= 0:
        print("Invalid input. Please enter a positive integer.")

lst1 = []

for i in range(n1):
    lst1.append(int(input(f"Enter the {i+1}th element of the first array: ")))

print(lst1)


n2 = 0
while n2 <= 0:
    n2 = int(input("Enter the length of the second array: "))
    if n2 <= 0:
        print("Invalid input. Please enter a positive integer.")

lst2 = []

for i in range(n2):
    lst2.append(int(input(f"Enter the {i+1}th element of the second array: ")))

print(lst2)

set1 = set(lst1)
set2 = set(lst2)

intersection = set1.intersection(set2)

print(intersection)