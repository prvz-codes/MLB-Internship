import pandas as p
import matplotlib.pyplot as plt
import seaborn as s

data = p.read_csv("cleaned_student_data.csv")


def showAllStds():
    print("Total Students :", data["Roll_No"].count())


def avgOfEachSubj():

    subjs = [
        "Math",
        "English",
        "Science",
        "Computer",
        "Physics",
        "Chemistry"
    ]

    avg = data[subjs].mean()

    print(avg)

    plt.bar(avg.index, avg.values)
    plt.title("Average Score of Each Subject")
    plt.xlabel("Subjects")
    plt.ylabel("Average Marks")
    plt.show()


def topStds():

    topperStds = data.sort_values(by="Total_Marks", ascending=False).head(5)

    print("Top 5 Performing Students")
    print(topperStds[["Roll_No", "Name", "Total_Marks"]])

    plt.bar(topperStds["Name"], topperStds["Total_Marks"])
    plt.title("Top 5 Performing Students")
    
    plt.xlabel("Students")
    plt.ylabel("Total Marks")
    plt.xticks(rotation=20)
    plt.show()


def weakStds():

    weakStd = data.sort_values(by="Total_Marks").head(5)

    print("Students Needing Improvement")

    print(weakStd[["Roll_No", "Name", "Total_Marks"]])
    
    plt.bar(weakStd["Name"], weakStd["Total_Marks"])
    plt.title("Students Needing Improvement")
    plt.xlabel("Students")
    plt.ylabel("Total Marks")
    plt.xticks(rotation=20)
    plt.show()


def highestClassAvg():

    subjs = ["Math","English","Science","Computer","Physics","Chemistry"]

    avg = data[subjs].mean()
    maxSubject = avg.idxmax()
    maxSubjAvg = avg.max()

    print("Subject with the highest class average:", maxSubject)
    print("Average Marks:", round(maxSubjAvg, 2))

    plt.bar(avg.index, avg.values)
    plt.title("Average Marks of Each Subject")
    plt.xlabel("Subjects")
    plt.ylabel("Average Marks")
    plt.show()

def avgMarksDistribution():

    plt.hist(data["Average_Marks"], bins=10)

    plt.title("Distribution of Average Marks")
    plt.xlabel("Average Marks")
    plt.ylabel("Number of Students")

    plt.show()




def performanceChart():

    performance = []
    for marks in data["Average_Marks"]:
        if marks >= 90:
            performance.append("Excellent")
        elif marks >= 75:
            performance.append("Good")
        elif marks >= 60:
            performance.append("Average")
        else:
            performance.append("Needs Improvement")
    data["Performance"] = performance
    count = data["Performance"].value_counts()
    plt.pie(count, labels=count.index, autopct="%1.1f%%")
    plt.title("Performance Distribution")
    plt.show()


def scatterPlot():

    plt.scatter(data["Computer"], data["Science"])
    plt.title("Computer vs Science")
    plt.xlabel("Computer")
    plt.ylabel("Science")
    plt.show()


def boxPlot():

    subjs = ["Math","English","Science","Computer","Physics","Chemistry"]
    s.boxplot(data=data[subjs])
    plt.title("Marks Distribution")
    plt.show()


while True:
    print("Press  1 to show total stds ")
    print("Press  2 to show average score of every   subject")
    print("Press 3 to show Top 5 Performing Students")
    print("Press 4 to show Students who need Improvement")
    print("Press 5 to show Subject with Highest Class Average")
    print("Press 6 to show Histogram of Avg Marks")
    print("Press 7 to show Performance Pie Chart")
    print("Press 8 to show Scatter Plot")
    print("Press 9 to show Box Plot")
    print("Press 10 to Exit")

    inp = int(input("Enter your choice: "))
    if inp == 1:
        showAllStds()
    elif inp == 2:
        avgOfEachSubj()
    elif inp == 3:
        topStds()
    elif inp == 4:
        weakStds()
    elif inp == 5:
        highestClassAvg()
    elif inp == 6:
        avgMarksDistribution()
    elif inp == 7:
        performanceChart()
    elif inp == 8:
        scatterPlot()
    elif inp == 9:
        boxPlot()
    elif inp == 10:
        break
    else :
        print("Invalid Choice")
        break