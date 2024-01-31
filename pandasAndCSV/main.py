# First option
# with open("weather_data.csv") as file:
#     data = file.readlines()
#
#     print(data)


# Second option
# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)


# BEST option
import pandas as pd

data = pd.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(data["temp"].mean())
#
# print(data["temp"].max())

# print(data[data["day"] == "Monday"])

# max_temp = data[data.temp == data.temp.max()]
# print(max_temp)

# monday = data[data.day == "Monday"]
# print((monday.temp[0] * 9) / 5 + 32)


# Create a dataframe from cero
data_dict = {
    "students": ["Amy", "Bob", "Mike"],
    "scores": [65, 80, 91]
}

students_data = pd.DataFrame(data_dict)
print(data)
students_data.to_csv("new_data.csv")
