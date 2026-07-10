import json
file = "Day3/student.json"

myStudents = []
try:
    with open (file , "r") as f:
        myStudents = json.load(f)
except (FileNotFoundError , json.JSONDecodeError):
    myStudents = []


def updateData():
    
        with open(file , "w") as f:
            json.dump(myStudents , f , indent=5)
    
      
def addStudents():
    rNo =int(input("enter your roll no "))
    for s in myStudents:
        
        if rNo == s["rollNo"]:
            print("student already exist ")
            return
    name= input("enter new name ")
    try:
        age = int(input("enter new age "))
    except :
        print("invalid input for age ")
        return
    
    course = input("enter your course name ")


    student = {
        "rollNo" : rNo,
        "name" : name,
        "age" : age,
        "course" : course

    }
    myStudents.append(student)
    updateData()

    print("student added ")



def viewStudent():
    if(invalidCase()):
        raise Exception("no students found")
        return
    
    print("Student details ")
    for s in myStudents:
        
        print("Name : " , s["name"]),
        print("Roll no : " , s["rollNo"]),
        print("age : " , s["age"]),
        print("course : " , s["course"])


def invalidCase():
    if len(myStudents)==0:
        return True
    return False
def searchStudent():
    if(invalidCase()):
        raise Exception("no students found")
        return
    rNo = int(input("enter your roll no "))
    for s in myStudents:
        if(rNo == s["rollNo"]):
            print("yes student exists : ")
            print("Name : " , s["name"]),
            print("Roll no : " , s["rollNo"]),
            print("age : " , s["age"]),
            print("course : " , s["course"])
            return
    print("student doesnot exist")
def deleteStudent():
    if(invalidCase()):
        raise Exception("no students found")
        return
    rNo = int(input("enter your roll no "))
    for s in myStudents:
        if(rNo == s["rollNo"]):
            myStudents.remove(s)
            print("student deleted")
            updateData()
            return

    print("no student found to be deleted")

def updateStudent():
    if(invalidCase()):
        raise Exception("no students found")
        return
    rNo = int(input("enter your roll no of student to update "))

    for s in myStudents:
        if(rNo == s["rollNo"]):
            inpName= input("enter new name ")
            try:
                inpAge = int(input("enter new age "))
            except :
                print("invalid input for age ")
                return
            s["name"]= inpName
            s["age"]= inpAge
            s["course"] = input("enter new coursee ")
            print("studnet added ")
            updateData()
            return
    print("student doesnt exist")
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
    try :
        inp = int(input("enter your choice : "))
    except :
        print("invalid input ")
        break
    if inp == 1:
        addStudents()
    elif inp == 2:
        try:
            viewStudent()
        except Exception as e:
            print(e)
    elif inp == 3:
        try:
           searchStudent()
        except Exception as e:
            print(e)
        
    elif inp == 4:
        try:
          deleteStudent()
        except Exception as e:
            print(e)
        
    elif inp == 5:
        try:
          updateStudent()
        except Exception as e:
            print(e)
        
    elif inp == 6:
        totStudents()    
    elif inp == 9:
        break