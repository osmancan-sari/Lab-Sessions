n = int(input("Enter number of names: "))

lst = []
for i in range(n):
    name_surname = input("Enter name:").strip().split()
    lst.append((name_surname[0],name_surname[1]))

print(lst)

formatter = lambda x: (x[0].capitalize(), x[1].upper())

lst = list(map(formatter, lst))

print(lst)

joiner = lambda x: (f"{x[0]} {x[1]}")

lst = list(map(joiner, lst))

print(lst)