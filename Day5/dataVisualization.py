import pandas as p

import matplotlib.pyplot as plt
import seaborn as s

data1 = p.read_csv("cleaned_student_data.csv")
data = data1.head()
x = [1,2,3,4]
y = [10 , 20,5,25]

plt.plot(x , y)



plt.show()


















# plt.figure(figsize=(12,6))
# plt.bar(data["Name"], data["Average_Marks"])
# plt.title("Average Marks of Each Student")
# plt.xlabel("Students")
# plt.ylabel("Average Marks")
# plt.xticks(rotation=90)
# plt.tight_layout()
# plt.show()

# plt.figure(figsize=(8,5))
# plt.hist(data["Average_Marks"], bins=10)
# plt.title("Distribution of Average Scores")
# plt.xlabel("Average Marks")
# plt.ylabel("Number of Students")
# plt.show()

# plt.figure(figsize=(7,5))
# plt.scatter(data["Math"], data["Computer"])
# plt.title("Math vs Computer Marks")
# plt.xlabel("Math Marks")
# plt.ylabel("Computer Marks")
# plt.show()

# def performance(avg):
#     if avg >= 90:
#         return "Excellent"
#     elif avg >= 75:
#         return "Good"
#     elif avg >= 60:
#         return "Average"
#     else:
#         return "Poor"

# data["Performance"] = data["Average_Marks"].apply(performance)

# performance_count = data["Performance"].value_counts()

# plt.figure(figsize=(6,6))
# plt.pie(
#     performance_count,
#     labels=performance_count.index,
#     autopct="%1.1f%%",
#     startangle=90
# )
# plt.title("Student Performance Distribution")
# plt.show()