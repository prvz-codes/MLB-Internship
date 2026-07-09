                                
                                                      # max and secondmax 

myList = [90, 95, 80]

max =0
secMax = 0
for x in range(len(myList)):
    if(max < int(myList[x])):
        secMax = max
        max = int(myList[x])
    elif(secMax < int(myList[x])):
        secMax = myList[x]


print(max)

print(secMax)

                                #  remove duplicates

myList2 = ['apple' , 'apple' , 'pakistan' , 'pakistan' , 'hi' , 'hello' , 'mobile' , 'laptop' , 'mobile' , 'computer']
mylist3=[]
for x in range(len(myList2)):
    y = x +1
    while(y < len(myList2)):
        if myList2[x] == myList2[y]:
            myList2.pop(y)
        else:
            y = y +1
print(myList2)

                                # common elements
A = [ 2 , 45, 31, 34, 2,41,43,1,4 ,5 ,90]
B = [1, 90, 34, 2, 2,5 ,7, 111,411 ,511 ,901  ]

print([(x , y) for x in A for y in B if x == y])


fruits = ("apple", "banana", "apple", "orange", "apple")
print("tuple " , fruits)
fruitList = list(fruits)

print("tuple to list" , fruitList)


fruits2 = tuple(fruitList)

print("list to tuple : " , fruits2)


# duplicates inset

mySet = [ 2 , 3, 3, 3, 2,4,4,5,4 ,5 ,9]

list_of_set = set(mySet)

print("set : " , list_of_set)

# dict

stds = {
    "name" : "Ali",
    "Age" : 19,
    "class" : 12,
    "gender" : "male"
}
print(stds)


stdMarks = {
    "Ali"  : 90 ,
    "Ayan"  : 91,
    "Hasan" : 98
}

total =0
for m in stdMarks.values():
    total+=int(m)

print(total / 100)