n = int(input("Enter number of inputs: "))

lst = []
for i in range(n):
    name, surname = input("Enter name and surname: ").split()
    lst.append((name, surname))

print(lst)

formatter = lambda x: (x[0].capitalize(), x[1].upper())

lst = list(map(formatter, lst))

combiner = lambda x: f"{x[0]} {x[1]}"

lst = list(map(combiner, lst))

print(lst)