import pandas as pd

# Read CSV File
data = pd.read_csv("2018_central_park_squirrel_census_squirrel.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

# Create Dataframe with a dict before write into a new csv file
df = pd.DataFrame(data_dict)
df.to_csv("squirrels_count.csv")
