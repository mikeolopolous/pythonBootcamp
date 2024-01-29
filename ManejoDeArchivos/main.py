# Simply reads a file
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# Best way to read a file
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# Best way to write into a file
with open("my_file.txt", mode="a") as file:
    file.write("\nHello World from python")

# If the file does not exist, it creates a new file
with open("new_file.txt", mode="w") as file:
    file.write("\nHello World from python!")
