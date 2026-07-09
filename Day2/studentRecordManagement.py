
myStudents = []

def addStudents():
    rNo = input("enter your roll no ")
    for s in myStudents:
        if rNo == s["rollNo"]:
            print("student already exist ")
            return
    name = input("enter your name  ")
    age= input("enter your age  ")
    course = input("enter your course name ")


    student = {
        "rollNo" : rNo,
        "name" : name,
        "age" : age,
        "course" : course

    }
    myStudents.append(student)
    print("student added ")



def viewStudent():
    if len(myStudents)==0:
        print("no students ")
        return
    
    print("Student details ")
    for s in myStudents:
        
        print("Name : " , s["name"]),
        print("Roll no : " , s["rollNo"]),
        print("age : " , s["age"]),
        print("course : " , s["course"])



def searchStudent():
    rNo = input("enter your roll no ")
    for s in myStudents:
        if(rNo == s["rollNo"]):
            print("yes student exists : ")
            print("Name : " , s["name"]),
            print("Roll no : " , s["rollNo"]),
            print("age : " , s["age"]),
            print("course : " , s["course"])
            return
    print("student not found ")
def deleteStudent():
    rNo = input("enter your roll no ")
    for s in myStudents:
        if(rNo == s["rollNo"]):
            myStudents.remove(s)
            print("student deleted")
            return

    print("student not found ")

def updateStudent():
    rNo = input("enter your roll no of student to update ")

    for s in myStudents:
        if(rNo == s["rollNo"]):
            s["name"] = input("enter new name ")
            s["age"] = input("enter new age ")
            s["course"] = input("enter new coursee ")
            print("studnet added ")
            return
    print("not found")

def totStudents():
    print("total num of students :" , len(myStudents))
while(True):
    print("press 1 to add student ")
    print("press 2 to view student ")
    print("press 3 to search Students  ")
    print("press 4 to Delete student ")
    print("press 5 to Update student ")
    print("press 6 to check total number of  student ")
    print("press 9 to exit  ")
    inp = int(input("enter your choice : "))

    if inp == 1:
        addStudents()
    elif inp == 2:
        viewStudent()
    elif inp == 3:
        searchStudent()
    elif inp == 4:
        deleteStudent()
    elif inp == 5:
        updateStudent()
    elif inp == 6:
        totStudents()    
    elif inp == 9:
        break