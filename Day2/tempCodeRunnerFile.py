
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
