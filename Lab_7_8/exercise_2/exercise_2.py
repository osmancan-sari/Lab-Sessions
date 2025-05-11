people = []
with open("/Users/osmancansari/Desktop/YZV104E/Lab Sessions/Lab-Sessions/Lab_7_8/exercise_2/data.csv", "r") as file:
    for line in file.readlines():
        name, gender, age, height, weight, hair_color, eye_color = line.strip().split(",")
        people.append(
            {
                "name": name,
                "gender": gender,
                "age": int(age),
                "height": int(height),
                "weight": int(weight),
                "hair_color": hair_color,
                "eye_color": eye_color
            })

name = input("Enter name: ")

gender = input("Enter gender preference: ")

while gender != "male" and gender != "female":
    print("Invalid gender preference")
    gender = input("Enter gender preference: ")

min_age, max_age = map(int, input("Enter min and max age: ").split())

min_height = int(input("Enter min height: "))
max_weight = int(input("Enter max weight: "))

valid_hair_colors = ["brown", "black", "yellow", "red", "green", "blue", "pink", "purple"]
hair_color = input("Enter hair color: ")

while hair_color not in valid_hair_colors:
    print("Invalid hair color")
    hair_color = input("Enter hair color: ")

valid_eye_colors = ["brown", "black", "blue", "green", "hazel"]
eye_color = input("Enter eye color: ")

while eye_color not in valid_eye_colors:
    print("Invalid eye color")
    eye_color = input("Enter eye color: ")

filtered_people = list(filter(lambda x: x["gender"] == gender, people))

print(len(filtered_people))

filtered_people = list(filter(lambda x: x["age"] >= min_age and x["age"] <= max_age, filtered_people))

print(len(filtered_people))

filtered_people = list(filter(lambda x: x["height"] >= min_height, filtered_people))

print(len(filtered_people))

filtered_people = list(filter(lambda x: x["weight"] <= max_weight, filtered_people))

print(len(filtered_people))

filtered_people = list(filter(lambda x: x["hair_color"] == hair_color, filtered_people))

print(len(filtered_people))

filtered_people = list(filter(lambda x: x["eye_color"] == eye_color, filtered_people))

print(len(filtered_people))

print(filtered_people)








