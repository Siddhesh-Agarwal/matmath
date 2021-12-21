################################################################################
##                               Basic Matrices                               ##
################################################################################

def null(n, m=None):
    """Creates a null matrix.

    Args:
    n (int)
        Number of rows of the matrix
    m (int, optional): 
        Number of columns of the matrix. Defaults to the number of rows.

    Returns
    -------
    Matrix
        A null matrix of order N x M.
    """
    if m == None:
        m = n
    return [[0] * m] * n

def identity(n, mul=1):
    """Creates an identity matrix.

    Args:
    n (int)
        Number of rows of the matrix
    mul (int/float, optional)
        The multiplication factor. Defaults to 1.

    Returns
    -------
    Matrix
        An identity matrix multiplied by the multiplication factor.
    """
    identity_matrix = null(n)
    for i in range(n):
        identity_matrix[i][i] = mul
    return identity_matrix


################################################################################ 
##                             Types  of  Matrices                            ##
################################################################################

def is_matrix(A):
    """Tells whether an input is actually a matrix or not.

    Args
    ----
    A (compulsory)
        A matrix.

    Returns
    -------
    bool
        True if the input is a matrix, False otherwise.
    """
    for row in A:
        if len(row) != len(A[0]):
            return False
        for element in row:
            if type(element) not in [int, float, complex]:
                return False
    return True

def is_null(A):
    """Tells whether a matrix is a null matrix or not.

    Args
    ----
    A (compulsory)
        A matrix.

    Returns
    -------
    bool
        True if the matrix is a null matrix, False otherwise.
    """
    return [[0] * len(A[0])] * len(A) == A

def is_identity(A):
    """Tells whether a matrix is an identity matrix or not.

    Args
    ----
    A (compulsory)
        A matrix.

    Returns
    -------
    bool
        True if the matrix is an identity matrix, False otherwise.
    """
    return A == identity(len(A))

def is_symmetric(A):
    """Tells whether a matrix is a symmetric matrix or not.

    Args
    ----
    A (compulsory)
        A matrix.

    Returns
    -------
    bool
        True if the matrix is a diagonal matrix, False otherwise.
    """
    for i in range(len(A)):
        for j in range(len(A[0])):
            try:
                if A[i][j] != A[j][i]:
                    return False
            except IndexError: #Would happen if matrix is not square.
                return False
    return True

def is_skew_symmetric(A):
    """Tells whether a matrix is a skew triangular matrix or not.

    Args
    ----
    A (compulsory)
        A matrix.

    Returns
    -------
    bool
        True if the matrix is a skew symmetric matrix, False otherwise.
    """
    for i in range(len(A)):
        for j in range(len(A[0])):
            try:
                if A[i][j] != -1 * A[j][i]:
                    return False
            except IndexError: #Would happen if matrix is not square.
                return False
    return True

def is_diagonal(A):
    """Tells whether a matrix is a diagonal matrix or not.

    Args
    ----
    A (compulsory)
        A matrix.

    Returns
    -------
    bool
        True if the matrix is a diagonal matrix, False otherwise.
    """
    for i in range(len(A)):
        for j in range(len(A[0])):
            try:
                if i != j and A[i][j] != 0:
                    return False
            except IndexError: #Would happen if matrix is not square.
                return False
    return True

def is_square(A):
    """Tells whether a matrix is a square matrix or not.

    Args
    ----
    A (compulsory)
        A matrix.

    Returns
    -------
    bool
        True if the matrix is a square matrix, False otherwise.
    """
    if is_matrix(A):
        return len(A[0]) == len(A)
    raise ValueError("The given matrix is not a matrix.")

def is_utriangular(A):
    """Tells whether a matrix is an upper triangular matrix or not.

    Args
    ----
    A (compulsory)
        A matrix.

    Returns
    -------
    bool
        True if the matrix is an upper triangular matrix, False otherwise.
    """
    for i in range(len(A)):
        for j in range(len(A[0])):
            try:
                if A[i][j] != 0 and i > j:
                    return False
            except IndexError: #Would happen if matrix is not square.
                return False
    return True

def is_ltriangular(A):
    """Tells whether a matrix is an lower triangular matrix or not.

    Args
    ----
    A (compulsory)
        A matrix.

    Returns
    -------
    bool
        True if the matrix is an lower triangular matrix, False otherwise.
    """
    for i in range(len(A)):
        for j in range(len(A[0])):
            try:
                if A[i][j] != 0 and i < j:
                    return False
            except IndexError: #Would happen if matrix is not square.
                return False
    return True


################################################################################
##                           Matrix   Compatibility                           ##
################################################################################

def compatAS(a, b):
    """Tells if the 2 matrices can be added/subtracted.

    Args
    ----
    A (compulsory)
        A matrix.
    B (compulsory):
        Another matrix.

    Raises
    ------
    ValueError
        Raised if the given input is not a matrix.

    Returns
    -------
    bool
        True if the given matrix can be added/subtracted, False otherwise.
    """
    if is_matrix(a) and is_matrix(b):
        return False if len(a) != len(b) or len(a[0]) != len(b[0]) else True
    raise ValueError("The given parameter is not a matrix.")

def compatM(A, B):
    """Tells if the 2 matrices can be multiplied.

    Args
    ----
    A (compulsory)
        A matrix.
    B (compulsory):
        Another matrix.

    Raises
    ------
    ValueError
        Raised if the given input is not a matrix.

    Returns
    -------
    bool
        True if the given matrix can be multiplied, False otherwise.
    """
    if is_matrix(A):
        if is_matrix(B):
            return True if len(A[0]) == len(B) else False
        raise ValueError(f"{B} is not a matrix.")
    raise ValueError(f"{A} is not a matrix.")


################################################################################
##                           Arithmetic  Operations                           ##
################################################################################

def matAdd(a, b):
    """Returns the sum matrix (A+B), if mathematically possible.

    Args
    ----
    A (compulsory)
        A matrix.
    B (compulsory):
        Another matrix.

    Raises
    ------
    ValueError
        Raised when the addition of the two matrices is not possible.
    ValueError
        Raised if the given input is not a matrix.

    Returns
    -------
    Matrix
        The matrix representing the sum of the two matrices.
    """
    if compatAS(a, b):
        matrix = []
        for i in range(len(a)):
            matrix.append([])
            temp = [(a[i][j] + b[i][j]) for j in range(len(a[0]))]
            matrix.append(temp)
        return matrix
    raise ValueError("The 2 matrices do not have the same order.")

def matSub(a, b):
    """Returns the difference matrix (A-B), if mathematically possible.

    Args
    ----
    A (compulsory)
        A matrix.
    B (compulsory):
        Another matrix.

    Raises
    ------
    ValueError
        Raised when the subtraction of the two matrices is not possible.
    ValueError
        Raised if the given input is not a matrix.

    Returns
    -------
    Matrix
        The matrix representing the difference of the two matrices.
    """
    if compatAS(a, b):
        matrix = []
        for i in range(len(a)):
            matrix.append([])
            temp = [(a[i][j] - b[i][j]) for j in range(len(a[0]))]
            matrix.append(temp)
        return matrix
    raise ValueError("The 2 matrices do not have the same order.")

def matMul(a, b):
    """Returns the product matrix (AB), if mathematically possible.

    Args
    ----
    A (compulsory)
        A matrix.
    B (compulsory):
        Another matrix.

    Raises
    ------
    ValueError
        Raised when the multiplication of the two matrices is not possible.
    ValueError
        Raised if the given input is not a matrix.

    Returns
    -------
    Matrix
        The matrix representing the product of the two matrices.
    """
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
    raise ValueError("The 2 matrices are not compatible for multiplication.")

def power(a, power=2):
    """Returns the matrix representing the n^th power of matrix A, if mathematically possible.

    Args
    ----
    A (compulsory)
        A matrix.
    power (optional, int)
        The power of the matrix. defaults to 2.

    Raises
    ------
    ValueError
        Raised if the matrix is not a square matrix.
    ValueError
        Raised if the given input is not a matrix.

    Returns
    -------
    Matrix
        The matrix represting the n^th power of the matrix A.
    """
    if is_square(a):
        matrix = a
        for _ in range(power-1):
            matrix = matMul(a, matrix)
        return matrix
    raise ValueError("The given matrix is not a square matrix.")

def scalarMul(a, mul=1):
    """Returns the scalar product of A and n (nA)

    Args
    ----
    A (compulsory)
        A matrix.
    mul (int/float, optional)
        The multiplication factor. Defaults to 1.

    Returns
    -------
    Matrix
        The matrix multiplied with the multiplication factor
    """
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[j][i] *= mul
    return a


################################################################################
##                             Matrix   Operations                            ##
################################################################################

def cut(A, row=0, column=0):
    """Returns a smaller matrix by removing the required row and column.

    Args
    ----
    A (compulsory)
        A matrix.
    row (int, optional)
        The row to be removed. Defaults to 0.
    column (int, optional)
        The column to be removed. Defaults to 0.

    Returns
    -------
    Matrix
        The matrix with the required rows and columns removed.
    """
    matrix = []
    for i in range(len(A)):
        if i != row:
            x = [A[i][j] for j in range(len(A[i])) if j != column]
            matrix.append(x)
    return matrix

def rotate(A, turns=1):
    """A matrix which is formed by rotating the given matrix, n times, in clockwise sense.

    Args
    ----
    A (compulsory)
        A matrix.
    turns (int, optional)
        The number of turns to rotate the matrix. Defaults to 1.

    Returns
    -------
    Matrix
        The matrix obtained on rotating the given matrix.
    """
    turns = turns % 4
    if turns == 0:
        return A
    elif turns == 2:
        Rotated_A = [i[::-1] for i in A]
        return rotate(Rotated_A, turns-2)
    else:
        Rotated_A = [[A[j][i] for j in range(len(A[i]))][::-1] for i in range(len(A))]
        return rotate(Rotated_A, turns-1)

def transpose(A, mul_factor=1):
    """The transpose of the matrix.

    Args
    ----
    A (compulsory)
        A matrix.
    mul_factor (int/float, optional)
        Multiplication factor of the matrix. Defaults to 1.

    Returns
    -------
    Matrix
        The transpose of the given matrix multiplied by the multiplication factor.
    """
    matrix = []
    for i in range(len(A[0])):
        matrix.append([])
        for j in range(len(A)):
            matrix[i].append(A[j][i] * mul_factor)
    return matrix

def adj(A, mul_factor=1):
    """The adjoint of the matrix.

    Args
    ----
    A (compulsory)
        A matrix.
    mul_factor (int/float, optional)
        Multiplication factor of the matrix. Defaults to 1.

    Raises
    ------
    ValueError
        Raised when the matrix is not a square matrix.

    Returns
    -------
    Matrix
        The adjoint of the given matrix multiplied by the multiplication factor.
    """
    if is_square(A):
        matrix = []
        for i in range(len(A)):
            matrix.append([])
            for j in range(len(A)):
                matrix[i].append(float(det(cut(A, i , j))))
        return transpose(matrix, mul_factor)
    raise ValueError("The given matrix is not a square matrix.")

def inv(A, mul_factor=1):
    """The inverse of the matrix (if and only if the matrices are compatible). 
    
    Args
    ----
    A (compulsory)
        A matrix.
    mul_factor (int/float, optional)
        Multiplication factor of the matrix. Defaults to 1.

    Raises
    ------
    ValueError
        Raised when the matrix is not a square matrix.

    Returns
    -------
    Matrix
        The inverse of the given matrix multiplied by the multiplication factor.
    """
    if is_square(A):
        matrix = []
        for i in range(len(A)):
            temp =  [adj(A, mul_factor)[i][j] for j in range(len(A))]
            matrix.append(temp)
        return matrix
    raise ValueError("The given matrix is not a square matrix.")


################################################################################
##                            Matrix   Properties                             ##
################################################################################
 
def det(A):
    """Returns the determinant of the matrix (if mathematically possible).

    Args
    ----
    A (compulsory)
        A matrix.

    Raises
    ------
    ValueError
        Raised when the matrix is not a square matrix.

    Returns
    -------
    int/float
        The determinant of the given matrix.
    """
    length = len(A)
    if is_square(A):
        det = 1
        for i in range(length):
            for j in range(i+1, length):
                if A[i][i] == 0:
                    A[i][i] = 1
                x = A[j][i] / A[i][i]
                for k in range(length):
                    A[j][k] -= x * A[i][k]
        for i in range(length):
            det *= A[i][i]
        return det
    raise ValueError("The given matrix is not a square matrix.")

def trace(A):
    """Returns the trace of the matrix (i.e the product of elements on the diagonal), if mathematically possible.

    Args
    ----
    A (Compulsory)
        A matrix.

    Raises
    ------
    ValueError
        Raised when the matrix is not a square matrix.

    Returns
    -------
    int/float
        The trace of the given matrix.
    """
    if is_square(A):
        Trace = 1
        for i in range(len(A)):
            Trace *= A[i][i]
        return Trace
    raise ValueError("The given matrix is not a square matrix.")

def order(A):
    """Returns the order of the matrix.

    Args
    ----
    A (compulsory)
        A matrix.

    Returns
    -------
    tuple
        the order of the given matrix in the form (rows, columns).
    """
    return (len(A), len(A[0]))
