import pandas as pd

data = pd.read_csv("player_stats.csv")
print(data)

print(data.info())



print("first 5 values " , data.head())
print("last 5 values " , data.tail())
print("mean value of total shots taken : " , data["shots_total"].mean())

# conditions

filtered1 = data[data["goals"]> 2]
filteredOnteamName = data[data["team"] == "Argentina"]
filteredOnMinutesPlayed = data[data["minutes"] > 130]
print(filtered1)
print(filteredOnteamName) 
print(filteredOnMinutesPlayed)

# summary statistics
print(data.describe())