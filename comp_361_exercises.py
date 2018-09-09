#Exercise 1
################################################################################

#Write a function that returns an array passed as an argument, except row i.

from numpy import *

def removeRow(a,i):
    n, m = shape(a) #return the number of rows and columns for the array a n = rows, m = columns
    b = zeros((n-1,m)) #this array will hold the result. first fill it with zeros
    for k in range(n-1): #for each column
        if k < i: #if we are not at that row yet
            b[k] = a[k] #set the column of b to the column of a
        else:
            b[k] = a[k+1]
    return b

# testing the function

a = array([[0,1],[1,2],[2,3]])
print("Exercise 1 output:")
print(removeRow(a,1))

#Exercise 2
################################################################################

#write a function that multiplies two matrices

def multMat(a, b):
    rowA, colA = shape(a) #the size of the first matrix
    rowB, colB = shape(b) #the size of the second matrix
    resultMat = zeros((rowA,colB)) #the result matrix, of size rowA x colB
    try:
        assert(rowA == colB) # make sure that the rows of A are equal to the columns of b
    except AssertionError as e:
        print("Matrices are incompatible")
        return
    #if this was true then we can begin multiplying
    for i in range(rowA):
        for j in range(colB):
            sum = 0
            for k in range(colA):
                sum += a[i,k]*b[k,j]
            resultMat[i,j] = sum
    return resultMat

a = array([[1,2,3],[4,5,6]])
b = array([[1,2],[4,5],[7,8]])

print("Exercise 2 output:")
print(multMat(a,b))

#Exercise 3
####################################################################################################################

#write a function that computes the determinant of a matrix

# for a matrix |a b|    the determinant is computed by doing a*d - b*c
#              |c d|

# for a larger matrix we remove the row and column that does not contain that 2*2 square and multiply the determinant of the smaller square
# by the value at the intersection of the indexes where the row and column were removed and add the results while alternating signs

def determinant(a):
    #first we need to check that the array that we passed the function is square
    rowA, colA = shape(a)
    assert(rowA == colA)
    assert(rowA >= 2) # also we need the matrix to be at least 2 x 2

    #the base case
    if(rowA == 2):
        return a[0,0]*a[1,1] - a[0,1]*a[1,0]
    # recursive case
    # we have to build the matrix containing everything but the row and column we are ignoring
    det = 0
    for mat in range(colA):
        # we need a number of new matrices equal to the number of columns that we have
        subMat = zeros((rowA - 1, colA -1))
        for col in range(colA):
            #for each column we have to create the matrix of everything excluding the col and row where
            #we are located
            if col == mat: #if we are on the column equal to the matrix iteration, then we skip it
                continue
            for row in range(1, rowA): #since we are looking at each row except the first one
                if col < mat:
                    subMat[row - 1, col] = a[row,col]
                else:
                    subMat[row - 1, col - 1] = a[row,col]
        det += (-1)**mat*a[0,mat]*determinant(subMat)
    return det




a = array([[2.1,-0.6,1.1],[3.2,4.7,-0.8],[3.1,-6.5,4.1]])
print("Exercise 3 output:")
print(determinant(a))


