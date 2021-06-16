from warnings import UserWarning

################################################################################
##                               Basic Matrices                               ##
################################################################################

# Returns an identity matrix of order N x N multiplied by the multiplication factor. Default value of mul_factor(multiplication factor) is 1.
def Identity(n, mul_factor = 1):
    imatrix = []
    for i in range(n):
        temp = []
        for j in range(n):
            if i == j: temp.append(mul_factor)
            else: temp.append(0)
        imatrix.append(temp)
    return imatrix

# Returns a null matrix of order N x M. If only 1 parameter is given, returns a null matrix of order N x N.
def Null(a, n, m = 0):
    if m == 0: m = n
    zmatrix = []
    for i in range( n ):
        zmatrix.append( [] )
        for j in range( m ):
            zmatrix[i].append( 0 )
    return zmatrix


################################################################################
##                           Matrix   Compatibility                           ##
################################################################################

# Returns True if matrices are compatible for addition/subtraction else returns False.
def compatAS(a, b):
    if isMatrix(a) and isMatrix(b):
        return False if len(a) != len(b) or len(a[0]) != len(b[0]) else True
    UserWarning("Error: The given parameter is not a matrix.")

# Returns True if matrices are compatible for multiplication else returns False.
def compatM(A, B):
    if isMatrix(A) and isMatrix(B):
        return True if len(A[0]) == len(B) else False
    UserWarning("Error: The given parameter is not a matrix.")


################################################################################
##                           Arithamatic Operations                           ##
################################################################################

# Returns the sum matrix (A + B), provided the matrices are compatible.
def matAdd(a, b):
    if compatAS(a, b):
        matrix = []
        for i in range( len(a) ):
            matrix.append( [] )
            for j in range( len(a[i]) ):
                matrix[i].append( a[i][j] + b[i][j] )
        return matrix
    UserWarning( "Error: matrices do not have same order.")

# Returns the difference matrix (A - B), provided the matrices are compatible.
def matSub(a, b):
    for i in range( len(b) ):
        for j in range( len(b[i]) ):
            b[i][j] *= -1
    return matAdd(a, b)

# Returns the product matrix (AB), provided the matrices are compatible.
def matMul(a, b):
    if compatM(a, b):
        matrix = []
        for i in range( len(a) ):
            matrix.append([])
            for j in range( len(b[0]) ):
                total = 0
                for k in range( len(b) ):
                    total += (a[i][k] * b[k][j])
                matrix[i].append( total )
        return matrix
    UserWarning("Error: matrices not compatible for multiplication.")

# Returns the matrix representing the n^th power of matrix A, provided the matrix is square matrix.
def power(a, n):
    if isSquare(a):
        matrix = a
        for _ in range( n - 1 ):
            matrix = matMul(a, matrix)
        return matrix
    UserWarning("Error: The given matrix is not square.")
    
# Returns the scalar product of A and n (nA).
def scalarMul(a, n=1):
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[j][i] *= n
    return a


################################################################################
##                             Matrix   Operations                            ##
################################################################################

# Returns a smaller matrix by removing the required row and column. The default of row and column is 0.
def cut(A, row=0, column=0):
    matrix = []
    for i in range(len(A)):
        if i != row:
            x = [A[i][j] for j in range(len(A[i])) if j != column]
            matrix.append(x)
    return matrix

# Returns a matrix which is formed by rotating the given matrix, n times, in clockwise sense.
def rotate(A, turns=1):
    turns = turns % 4
    if turns == 0:
        return A
    else:
        Rotated_A = [[A[j][i] for j in range(len(A[i]))][::-1] for i in range(len(A))]
        return rotate(Rotated_A, turns - 1)

# Returns the transpose of the matrix.
def transpose(A, mul_factor=1):
    matrix = []
    for i in range(len(A[0])):
        matrix.append([])
        for j in range(len(A)):
            matrix[i].append(A[j][i] * mul_factor)
    return matrix

# Returns the adjoint of the matrix multiplied by the multiplication factor. Default value of mul_factor(multiplication factor) is 1.
def adj(A, mul_factor=1):
    if isSquare(A):
        matrix = []
        for i in range(len(A)):
            matrix.append([])
            for j in range(len(A)):
                matrix[i].append(float(det(cut(A, i , j))))
        return transpose(matrix, mul_factor)
    UserWarning("Error: The given matrix is not square.")

# Returns the inverse of the matrix (if and only if the matrices are compatible) multiplied by the multiplication factor. Default value of mul_factor (multiplication factor) is 1.
def inv(A, mul_factor=1):
    if isSquare(A):
        matrix = []
        for i in range(len(A)):
            matrix.append([])
            for j in range(len(A)):
                matrix[i].append(adj(A, mul_factor)[i][j])
        return matrix
    UserWarning("Error: The given matrix is not square.")


################################################################################
##                            Matrix   Properties                             ##
################################################################################

# Returns the determinant of the matrix (if and only if the matrices are compatible for multiplication) multiplied by the multiplication factor. Default value of mul_factor (multiplication factor) is 1.
def det(a, mul_factor=1):
    length = len(a)
    if isSquare(a):
        det = mul_factor
        for i in range(length):
            for j in range(i+1, length):
                if a[i][i] == 0:
                    a[i][i] = 1
                x = a[j][i] / a[i][i]
                for k in range(length):
                    a[j][k] -= x * a[i][k]
        for i in range(length):
            det *= a[i][i]
        return det
    UserWarning("Error: The given matrix is not square.")

# Returns the trace of the matrix (i.e the product of elements on the diagonal) if possible.
def trace(A):
    if isSquare(A):
        Trace = 1
        for i in range(len(A)): Trace *= A[i][i]
        return Trace
    UserWarning("Error: The given matrix is not square.")

# Returns the order of the matrix as a tuple (rows, columns).
def order(A):
    return tuple(len(A), len(A[0]))


################################################################################ 
##                             Types  of  Matrices                            ##
################################################################################

# Returns True if matrix is a valid matrix else returns False.
def isMatrix(A):
    for row in A:
        if len(row) != len(A[0]):
            return False
        for element in row:
            if type(element) not in [int, float, complex]:
                return False
    return True

# Returns True if the matrix is a null matrix else returns False.
def isNull(A):
    return [[0] * len(A[0])] * len(A) == A

# Returns True if the matrix is an identity matrix else returns False.
def isIdentity(A):
    return A == Identity(len(A))

# Returns True if matrix is a symmetric matrix else returns False.
def isSymmetric(A):
    for i in range(len(A)):
        for j in range(len(A)):
            try:
                if A[i][j] != A[j][i]:
                    return False
            except IndexError: #Would happen if matrix is not square.
                return False
    return True

# Returns True if matrix is a skew symmetric matrix else returns False.
def isSkewSymmetric(A):
    for i in range(len(A)):
        for j in range(len(A)):
            try:
                if A[i][j] != -1 * A[j][i]:
                    return False
            except IndexError: #Would happen if matrix is not square.
                return False
    return True

# Returns True if matrix is a diagonal matrix else returns False.
def isDiagonal(A):
    for i in range(len(A)):
        for j in range(len(A)):
            try:
                if i != j and A[i][j] != 0:
                    return False
            except IndexError: #Would happen if matrix is not square.
                return False
    return True

# Returns True if matrix is a square matrix else returns False.
def isSquare(A):
    for i in A:
        if len(i) != len(A):
            return False
    return True

# Returns True if matrix is an upper triangular matrix else returns False.
def isUTriangular(A):
    for i in range( len(A) ):
        for j in range( len(A) ):
            try:
                if A[i][j] != 0 and i > j:
                    return False
            except IndexError: #Would happen if matrix is not square.
                return False
    return True

# Returns True if matrix is an lower triangular matrix else returns False.
def isltriangular(A):
    for i in range(len(A)):
        for j in range(len(A)):
            try:
                if A[i][j] != 0 and i < j:
                    return False
            except IndexError: #Would happen if matrix is not square.
                return False
    return True
