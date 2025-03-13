size_dic = int(input("How many people are in the reading group? "))

reading_group = {}

for i in range(size_dic):
    name = input("Please enter the name of the member: ")
    book_number = input("Please enter the number of read books: ")
    reading_group[name] = book_number

for key in reading_group:
    print(f"{key}, {reading_group[key]}")


while True:
    name_to_remove = input("Please enter the name to be removed: ")
    if name_to_remove not in reading_group.keys():
        print("The name is not valid.")
    else:
        reading_group.pop(name_to_remove)
        break
for key in reading_group:
    print(f"{key}, {reading_group[key]}")
