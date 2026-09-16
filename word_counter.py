import os

filepath = os.path.join(os.path.dirname(__file__), "sample.txt")

file = open(filepath, "r")

text = file.read()

words = text.split()
lines = text.splitlines()
characters = len(text)

print("Total number of words:", len(words))
print("Total number of lines:", len(lines))
print("Total number of characters:", characters)

file.close()