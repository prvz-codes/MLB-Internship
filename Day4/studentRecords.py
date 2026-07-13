import pandas as p

stdData = p.read_csv("student_records.csv")
sortedData = stdData.sort_values(by="Total_Marks" , ascending= False)

# print("first top students " , sortedData.head())
# print("bottom five students " , sortedData.tail())
# print(stdData.info())


# print(stdData.isnull())

# print(stdData)

def showAllStds():
    print(stdData)

def TopperStudent():
    topper = sortedData.head(1)
    print(topper[["StudentID", "Name", "Total_Marks"]])

def TopTierStds():
    topStds =  sortedData.head(10)
    print(topStds[["StudentID", "Name", "Total_Marks"]] )


def stdWithBestAttendance():
    bestAttendanceStudents = stdData[stdData["Attendance(%)"] > 98]
    print(bestAttendanceStudents[["StudentID", "Name", "Attendance(%) " , "Total_Marks"]])



def chemistryToppers():
    chemToppers = stdData[stdData["Chemistry"] >= 95]
    print(chemToppers[["StudentID", "Name","Chemistry", "Total_Marks"]])

def physicsToppers():
    phyToppers = stdData[stdData["Physics"] >= 95]
    print(phyToppers[["StudentID", "Name" ,"Physics", "Total_Marks"]])

def computerToppers():
    compToppers = stdData[stdData["Computer"] >= 95]
    print(compToppers[["StudentID", "Name","Computer", "Total_Marks"]])
def lowerTierStds():
    lowerStds = sortedData.tail(10)
    print(lowerStds[["StudentID", "Name", "Total_Marks"]])







while(True):
    print("press 1 to show all student ")
    print("press 2 to view Topper Student ")
    print("press 3 to view Top 10 Students  ")
    print("press 4 to view  students with best attendance ")
    print("press 5 to view students with highest marks in chemistry ")
    print("press 6 to view students with highest marks in physics ")
    print("press 7 to view students with  highest marks in computer ")
    print("press 8 to view lower Tier Students ")
    print("press 9 to end ")

    inp = int(input("enter your choice : "))

    if inp == 1:
        showAllStds()
    elif inp == 2:
        TopperStudent()
    elif inp == 3:
        TopTierStds()
    elif inp == 4:
        stdWithBestAttendance()
    elif inp == 5:
        chemistryToppers()
    elif inp == 6:
        physicsToppers()
    elif inp == 7:
        computerToppers()
    elif inp == 8:
        lowerTierStds()        
    elif inp == 9:
        break