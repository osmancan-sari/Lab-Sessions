extensions = [".txt", ".csv", ".png", ".svg", ".jpg", ".dat", ".py", ".c", ".cpp"]
dic = {extension: 0 for extension in extensions}
for extension in extensions:
    for i in range(1,1000):
        name = (f"Lab_7_8\exercise_4\data\doc_{str(i).zfill(3)}{extension}")

        try:
            with open(name, "w") as file:
                pass
        except:
            continue
        else:
            dic[extension] += 1
            print(name)
print(dic)






