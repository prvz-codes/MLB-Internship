import numpy as np

arr1 = [1,2,3,4,5]
oneDimArr = np.array(arr1) 
twoDimArray = np.array([[5,6,7],[2,3,4],[1,2,9]])
zerosArr = np.zeros(3)
onesArr = np.ones([2,4])
oddArr = np.arange(1 ,10 , 2)
evenArr = np.arange(0,10,2)
identityMatrix = np.eye(2)


print("one dimensional array",oneDimArr)
print("two dimensional array",twoDimArray)
print("zeros array",zerosArr)
print("2d ones array",onesArr)
print("identity array",identityMatrix)
print("odd array",oddArr)
print("even array",evenArr)


print("size of array :" , oddArr.size)
print("size of array :" , oddArr.shape)
print("size of array :" , oddArr.ndim)
print("size of array :" , oddArr.dtype)

print(arr1*2)

print(evenArr ** 2)
# arthematic operations

print("sum of odd array " , oddArr.sum())
print("max in even array " ,evenArr.max())
print("min in 2d array" , twoDimArray.min())
print("mean of 2d array" , twoDimArray.mean())




# Array indexing and slicing

print("1st row , 2nd column index of 2d array ",twoDimArray[1,2])
print("fancy indexing of even array ",evenArr[[0 , 2 , 3]])


print("reverse of odd array ",oddArr[::-1])
print("1 to 3rd index of 1d array  ",oneDimArr[1:4])
# print("1 to 3rd index of 1d array  ",oneDimArr[1 : 4 :4])



matrix = np.array([
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12]
])

print(matrix[0 : 2:, 1:3])


# reshaping

arr_1  = np.array([1,2,3,4,5,6])
print("before reshape : " , arr_1)
arr_to_2d = arr_1.reshape(2,3)
print("after reshape : " ,arr_to_2d)

# returns a copy,doesnt affects org array
print("flatten array",matrix.flatten())
# returns a view , affects org array
print("ravel array",matrix.ravel()) 