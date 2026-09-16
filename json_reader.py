import json
import os

filepath = os.path.join(os.path.dirname(__file__), "data.json")

file = open(filepath, "r")

data = json.load(file)

print("----- STUDENT INFORMATION -----")
print("Name:", data["name"])
print("Age:", data["age"])
print("course:", data["course"])
print("college:", data["college"])

print("skills:")
for skill in data["skills"]:
    print("-", skill)

file.close()