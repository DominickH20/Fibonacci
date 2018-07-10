def multiply(inMatA,inMatB):
    outMat = [[0,0],[0,0]]
    outMat[0][0] = inMatA[0][0]*inMatB[0][0] + inMatA[0][1]*inMatB[1][0]
    outMat[0][1] = inMatA[0][0]*inMatB[0][1] + inMatA[0][1]*inMatB[1][1]
    outMat[1][0] = inMatA[1][0]*inMatB[0][0] + inMatA[1][1]*inMatB[1][0]
    outMat[1][1] = inMatA[1][0]*inMatB[0][1] + inMatA[1][1]*inMatB[1][1]
    return outMat

def printMat(matrix):
    print(matrix[0][0],matrix[0][1],sep = ' ')
    print(matrix[1][0],matrix[1][1],sep = ' ')

def power(A,n):
    if(n==0):
        return[[1,0],[0,1]]
    elif(n==1):
        return A
    elif(n%2!=0):
        return multiply(A,power(A,n-1))
    else:
        A = multiply(A,A)
        return power(A,n//2)

def matrixFib(n):
    matrix = power([[1,1],[1,0]],n)
    return matrix[0][1]
