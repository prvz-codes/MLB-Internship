

def outputMsg(name : str , stdclass : int , avg : float , grade : str , Marks : float , subjDetails : dict , obMarksList : list) :


    print(name , "YOUR RESULT OF CLASS ", stdClass , "IS ")
    for s , m in subjDetails.items():
        print(s , m)

    print("GRADE : " , grade)
    print("Total Obtained Marks : " ,Marks)
    print("Percentage : " , myAvg , "%")

def calculateAvg(obtMarksList : list ,   totalMarksList : list , subjCount : int):
    obtainedMarks = 0
    totalMarks = 0

    for i in range(subjCount):
        obtainedMarks += obtainedMarksList[i]
        totalMarks+= totalMarksList[i]
    obtainedPercentage = (obtainedMarks/totalMarks)*100
    return obtainedPercentage , obtainedMarks

def assignGrade(obtPercentage: float):
    if(obtPercentage >= 90):
        return 'A'
    elif(obtPercentage >= 80 ):
        return 'A-'
    elif(obtPercentage >=70 ):
        return 'B'
    elif(obtPercentage >=60):
        return 'C'
    elif(obtPercentage >=45):
        return 'D'
    else:
        return 'F'
    

subjDetails = {}
studntDetails = {}
totalMarksList= []
obtainedMarksList = []
stdName = str(input("Enter Student name ? "))
stdClass = int(input("Enter Student class ? "))
subjCount = 0
while(True):
    subjName= input("enter subject name : ")
    if subjName == "":
        break
    marks1= int(input("enter total marks of subject ? "))
    marks2 =float( input("enter obtained marks of subject ? "))

    if(subjName not in subjDetails):

        subjDetails[subjName] = marks2
        totalMarksList.append(marks1)
        obtainedMarksList.append(marks2)
        subjCount+=1
    else:
        print("subject already exist")

if(subjCount != 0):

    myAvg , myMarks= calculateAvg(obtainedMarksList , totalMarksList , subjCount)
    myGrade = assignGrade(myAvg)
    outputMsg(stdName , stdClass , myAvg , myGrade , myMarks , subjDetails , obtainedMarksList)
else:
    print("no subjects added!!!")
    