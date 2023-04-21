from typing import Optional


def zero(n: int, m: Optional[int] = None):
    """Creates a 2D array of size n x m."""
    if m is None:
        m = n
    return [[0] * m] * n


def identity(n: int):
    """Creates a 2D array of size n x m with 1s on the diagonal."""
    return [[int(i == j) for i in range(n)] for j in range(n)]


# ------------------------------------------------------------------------------
class Matrix:
    def __init__(self, *matrix):
        # Check if not empty
        if len(matrix) == 0:
            raise ValueError("Matrix must have at least one element.")
        # reset Matrix if there is only one element inside the matrix
        if len(matrix) == 1 and isinstance(matrix[0][0], (list, tuple)):
            matrix = matrix[0]
        # Check if rows are iteratable
        try:
            for row in matrix:
                # Check if rows are lists or tuples
                if not isinstance(row, (list, tuple)):
                    raise ValueError(f"Matrix must contain list/tuples not {type(row)}")
                iter_check = iter(row)
                # Confirm that elements are numbers.
                for element in iter_check:
                    if not isinstance(element, (int, float, complex)):
                        raise ValueError(f"Matrix must contain only numbers not {type(element)}")
        except TypeError:
            raise TypeError("Matrix argument should be iteratable.")
        # Check if number of elements in each row is the same.
        no_of_cols = len(matrix[0])
        no_of_rows = 0
        for row in matrix:
            no_of_rows += 1
            if len(row) != no_of_cols:
                raise ValueError("The number of elements in the matrix should be equal.")
        # Initialize variables
        self.matrix = [list(row) for row in matrix]
        self.rows = no_of_rows  # Number of rows
        self.cols = no_of_cols  # Number of columns
        self.__index = 0  # Used for iterating over the matrix

    def __len__(self):
        """Returns the number of rows in the matrix"""
        return self.rows

    def __iter__(self):
        """Returns an iterator over the elements of the matrix"""
        return iter(self.matrix)

    def __next__(self):
        """Returns the next element of the matrix"""
        if self.__index < len(self.matrix):
            self.__index += 1
            return self.matrix[self.__index - 1]
        raise StopIteration

    def __getitem__(self, r: int, c: int):
        """Returns the element at the specified key"""
        return self.matrix[r][c]

    def __str__(self):
        """Returns a string representation of the matrix"""
        length = self.rows
        string = ["| "] * length
        for i in range(len(self.matrix[0])):
            temp = []
            helper = 0
            for j in range(length):
                element = str(self.matrix[j][i])
                temp.append(element)
                if len(element) > helper:
                    helper = len(element)
            for j in range(length):
                string[j] += temp[j] + " " * (helper - len(temp[j]) + 1)
        return "|\n".join(string) + "|"

    def __repr__(self):
        sep = ",\n" + " " * 7
        return f"Matrix({sep.join(list(map(lambda x: str(x)[1:-1], self.matrix)))})"

    def __eq__(self, other):
        """Checks if the matrix is equal to another matrix"""
        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
        return True

    def __ne__(self, other):
        """Checks if the matrix is not equal to another matrix"""
        return not (self.matrix == other.matrix)

    def __add__(self, other):
        """Returns the sum of the matrices"""
        if self.order() == other.order():
            matrix = []
            for i in range(self.rows):
                temp = []
                for j in range(self.cols):
                    temp.append(self.matrix[i][j] + other[i][j])
                matrix.append(temp)
            return Matrix(matrix)
        raise ValueError("The 2 matrices do not have the same order.")

    def __iadd__(self, other):
        return self + other

    def __sub__(self, other):
        """Returns the difference of the matrices"""
        if self.order() == other.order():
            matrix = []
            for i in range(self.rows):
                temp = []
                for j in range(self.cols):
                    temp.append(self.matrix[i][j] - other[i][j])
                matrix.append(temp)
            return Matrix(matrix)
        raise ValueError("The 2 matrices do not have the same order.")

    def __isub__(self, other):
        return self - other

    def __mul__(self, other):
        """Returns the product of a matrix and a number/matrix"""
        if isinstance(other, [int, float]):  # Scalar multiplication
            result = []
            for row in self.matrix:
                new_row = [(element * other) for element in row]
                result.append(new_row)
            return Matrix(result)
        elif isinstance(other, Matrix):
            if self.cols == other.cols and self.rows == other.rows:
                result = []
                for i in range(self.rows):
                    temp = []
                    for j in range(self.cols):
                        temp.append(self.matrix[i][j] * other[i][j])
                    result.append(temp)
                return result
            raise ValueError("The 2 matrices do not have the same order.")
        raise TypeError(f"Multiplication not supported between {type(self)} and {type(other)}.")

    def __imul__(self, other):
        return self * other

    def __truediv__(self, other):
        """Returns the division of a matrix and a number/matrix"""
        if isinstance(other, (int, float)):
            result = []
            for row in self.matrix:
                new_row = [(element * other) for element in row]
                result.append(new_row)
            return Matrix(result)
        elif isinstance(other, Matrix):
            if self.cols == other.cols and self.rows == other.rows:
                result = []
                for i in range(self.rows):
                    temp = []
                    for j in range(self.cols):
                        temp.append(self.matrix[i][j] / other[i][j])
                    result.append(temp)
                return result
            raise ValueError("The 2 matrices do not have the same order.")
        raise TypeError(f"Division not supported between {type(self)} and {type(other)}.")

    def __itruediv__(self, other):
        return self / other

    def __floordiv__(self, other):
        """Returns the quotient of a matrix and a number/matrix"""
        if isinstance(other, (int, float)):
            result = []
            for row in self.matrix:
                new_row = [(element // other) for element in row]
                result.append(new_row)
            return Matrix(result)
        elif isinstance(other, Matrix):
            if self.cols == other.cols and self.rows == other.rows:
                result = []
                for i in range(self.rows):
                    temp = []
                    for j in range(self.cols):
                        temp.append(self.matrix[i][j] // other[i][j])
                    result.append(temp)
                return result
            raise ValueError("The 2 matrices do not have the same order.")
        raise TypeError(f"Multiplication not supported between {type(self)} and {type(other)}.")

    def __ifloordiv__(self, other):
        return self // other

    def __matmul__(self, other):
        """Returns the cross product of two matrices"""
        if isinstance(other, Matrix):  # Matrix multiplication
            arr = []
            for i in range(self.rows):
                arr.append([])
                for j in range(other.cols):
                    total = 0
                    for k in range(self.cols):
                        total += self.matrix[i][k] * other.matrix[k][j]
                    arr[i].append(total)
            return Matrix(arr)
        raise ValueError(f"Passed object is not of {type(self)}")

    def __pow__(self, power: int = 2):
        """Returns the matrix representing the n^th power of matrix A, if mathematically possible."""
        if self.cols == self.rows:
            if isinstance(power, int) and int > 0:
                matrix = self.copy()
                for _ in range(power - 1):
                    matrix = matrix * self.matrix
                return matrix
            elif power == 0:
                matrix = identity(self.rows)
                return Matrix(matrix)
            raise ValueError("The power of the matrix must be a natural number")
        raise ValueError("The given matrix is not a square matrix.")

    def identity(self, n: int = 3):
        """
        identity _summary_

        Parameters
        ----------
        n : int
            The order of the identity matrix. defaults to 3.
        """
        matrix = [[0] * n] * n
        for i in range(n):
            matrix[i][i] = 1
        self.matrix = matrix
        self.rows = n
        self.cols = n

    def zero(self, order: tuple):
        r, c = order
        self.matrix = [[0] * c] * r
        self.rows = r
        self.cols = c

    def fill(self, value: int, order: tuple):
        r, c = order
        self.matrix = [[value] * c] * r
        self.rows = r
        self.cols = c

    def adjoint(self):
        """Returns the adjoint representation of the matrix.

        Returns
        -------
        Matrix :
            The adjoint representation of the matrix.
        """
        matrix = []
        for i in range(self.rows):
            temp = []
            for j in range(self.cols):
                temp.append(self.cofactor(i, j))
            matrix.append(temp)
        return Matrix(matrix).transpose()

    def cofactor(self, i: int, j: int):
        """Returns the co-factor representation of the matrix.

        Parameters
        ----------
        i: int
            The index of the row of the matrix.
        j: int
            The index of the column of the matrix.

        Returns
        -------
        float :
            The co-factor representation of the matrix.
        """
        return float((-1) ** (i + j) * self.minor(i, j))

    def copy(self):
        """Returns a shallow copy of this matrix.

        Returns
        -------
        a copy of this matrix
        """
        new_matrix = []
        for row in range(self.matrix):  # O(m*n)
            new_row = [element for element in row]
            new_matrix.append(new_row)
        return Matrix(new_matrix)

    def cut(self, i=None, j=None):
        """Returns a new matrix after removing the i th row and/or j th column.
        Will remove no row and column (by default).

        Parameters
        ----------
        i (int, optional)
            The row to be removed. Starts from 0.
        j (int, optional)
            The column to be removed. Starts from 0.

        Returns
        -------
        Matrix :
            The matrix after removing the i th row and/or j th column.

        Raises
        ------
        ValueError
            Raised if the row or column to be removed is not a natural number.
        """
        if i is None and j is None:
            matrix = self.copy()
            return Matrix(matrix)
        elif i is not None and j is None:
            matrix = []
            for k in range(self.rows):
                if k != i:
                    matrix.append(self.matrix[k])
            return Matrix(matrix)
        elif i is None and j is not None:
            matrix = []
            for k in range(self.cols):
                for l in range(self.rows):
                    if k != j:
                        matrix[l].append(self.matrix[l][k])
            return Matrix(matrix)
        elif i is not None and j is not None:
            matrix = []
            for k in range(self.rows):
                if k != i:
                    temp = []
                    for l in range(self.cols):
                        if l != j:
                            temp.append(self.matrix[k][l])
                    matrix.append(temp)
            return Matrix(matrix)
        raise ValueError("The row or column to be removed is not a natural number.")

    def determinant(self):
        """Returns the determinant of this matrix.

        Returns
        -------
        float :
            The determinant of this matrix.
        """
        if self.is_square():
            determinant = 1
            A = self.matrix
            for i in range(self.rows):
                for j in range(i + 1, self.rows):
                    if A[i][i] == 0:
                        A[i][i] = 1
                    x = A[j][i] / A[i][i]
                    for k in range(self.rows):
                        A[j][k] -= x * A[i][k]
            for i in range(self.rows):
                determinant *= A[i][i]
            return determinant
        raise ValueError("The given matrix is not a square matrix.")

    def inverse(self):
        """Returns the inverse of this matrix

        Returns
        -------
        Matrix :
            The inverse of this matrix
        """
        if self.is_square():
            determinant = self.determinant()
            if determinant == 0:
                raise ValueError("The given matrix is not invertible.")
            return (self.adjoint() / determinant).transpose()
        raise ValueError("The given matrix is not a square matrix.")

    @staticmethod
    def is_diagonal(self):
        """Returns True if the matrix is diagonal, False otherwise."""
        if self.cols == self.rows:
            for i in range(self.rows):
                for j in range(self.cols):
                    if i != j and self.matrix[i][j] != 0:
                        return False
            return True
        return False

    @staticmethod
    def is_identity(self):
        """Returns True if the matrix is identity, False otherwise"""
        for i in range(self.rows):
            for j in range(self.cols):
                if i == j and self.matrix[i][j] != 1:
                    return False
                elif i != j and self.matrix[i][j] != 0:
                    return False
        return True

    @staticmethod
    def is_invertible(self):
        """Returns True if the matrix is invertible, False otherwise."""
        return self.det() != 0

    @staticmethod
    def is_lower_triangular(self):
        """Returns True if the matrix is lower triangular, False otherwise."""
        if self.cols == self.rows:
            for i in range(self.rows):
                for j in range(i + 1, self.cols):
                    if self.matrix[i][j] != 0:
                        return False
            return True
        return False

    @staticmethod
    def is_null(self):
        """Returns True if the matrix is null, False otherwise."""
        for row in self.matrix:
            for item in row:
                if item != 0:
                    return False
        return True

    @staticmethod
    def is_skew_symmetric(self):
        """Returns True if the matrix is skew-symmetric, False otherwise."""
        if self.cols == self.rows:
            for i in range(self.rows):
                for j in range(i, self.cols):
                    if self.matrix[i][j] != -self.matrix[j][i]:
                        return False
            return True
        return False

    @staticmethod
    def is_square(self):
        """Returns True if the matrix is square, False otherwise."""
        return self.cols == self.rows

    @staticmethod
    def is_symmetric(self):
        """Returns True if the matrix is symmetric, False otherwise."""
        if self.cols == self.rows:
            for i in range(self.rows):
                for j in range(i, self.cols):
                    if self.matrix[i][j] != self.matrix[j][i]:
                        return False
            return True
        return False

    @staticmethod
    def is_upper_triangular(self):
        """Returns True if the matrix is upper triangular, False otherwise."""
        if self.cols == self.rows:
            for i in range(self.rows):
                for j in range(i):
                    if self.matrix[i][j] != 0:
                        return False
            return True
        return False

    def minor(self, i, j):
        """Returns the minor of the Aij element in matrix A.

        Parameters
        ----------
        i (int, optional)
            The row of the element. Starts from 0.
        j (int, optional)
            The column of the element. Starts from 0.

        Returns
        -------
        Matrix :
            The minor of the matrix A.

        Raises
        ------
        ValueError
            Raised if the row or column to be removed is not a natural number.
        """
        reduced = self.cut(i, j)
        return reduced.determinant()

    @property
    def order(self):
        """Returns the order of the matrix.

        Returns
        -------
        tuple :
            The order of the matrix.
        """
        return self.rows, self.cols

    def rotate(self, turns=1):
        """Returns the matrix after n rotations.

        Parameters
        turns (int, optional)
            The number of turns to rotate the matrix in clockwise direction. Defaults to 1.

        Returns
        -------
        Matrix :
            The matrix after n rotations.
        """
        if isinstance(turns, int):
            turns = turns % 4
            if turns == 0:
                return self
            elif turns == 2:
                rotated = [row[::-1] for row in self.matrix][::-1]
                return Matrix(rotated)
            else:
                rotated = [[]] * self.cols
                for i in range(self.rows - 1, -1, -1):
                    for j in range(self.cols):
                        rotated[j].append(self.matrix[i][j])
                return Matrix(rotated)
        raise ValueError("The number of turns is an integer.")

    def trace(self):
        """Returns a trace of the matrix.

        Returns
        -------
        int/float/complex ;
            The trace of the matrix.
        """
        if self.is_square():
            total = 0
            for i in range(self.rows):
                total += self.matrix[i][i]
            return total
        raise ValueError("The given matrix is not a square matrix.")

    def transpose(self):
        """Transposes the given matrix.

        Returns
        -------
        arr: Matrix
            The transposed matrix.
        """
        arr = []
        for i in range(self.cols):
            arr.append([])
            for j in range(self.rows):
                arr[i].append(self.matrix[j][i])
        return Matrix(arr)

    def to_list(self):
        """Returns the matrix as a list of lists.

        Returns
        -------
        list :
            The matrix as a list of lists.
        """
        return self.matrix

    # Alias
    adj = adjoint
    det = determinant
    inv = inverse
    is_diagonal_dominant = is_diagonal
    is_upper_hessenberg = is_upper_triangular
    is_lower_hessenberg = is_lower_triangular
