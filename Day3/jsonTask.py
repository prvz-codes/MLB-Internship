import json

# with open ("Day3/student.json" , "r") as f:
#     std = json.load(f)
# print(std)


myStd = {
    "name":"Akmal",
    "age":21,
    "cgpa":3.4
}

file = "Day3/student.json"

with open (file , "w") as j:
    json.dump(myStd , j, indent=4 )


with open ("Day3/student.json" , "r") as f:
    std = json.load(f)
print(std)
