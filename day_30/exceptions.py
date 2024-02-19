
# try:
#     file = open("a_file.txt")
#
#     # KeyError
#     a_dictionary = {"key1": "value1", "key2": "value2"}
#     print(a_dictionary["key2"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed")


height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be ver 3 meters.")

bmi = weight / (height ** 2)
print(bmi)
