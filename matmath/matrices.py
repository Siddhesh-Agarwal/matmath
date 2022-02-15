def zero(n, m=None):
    """Creates a 2D array of size n x m."""
    if m is None:
        m = n
    return [[0] * m] * n


def identity(n):
    """Creates a 2D array of size n x m with 1s on the diagonal."""
    return [[int(i == j) for i in range(n)] for j in range(n)]


# ------------------------------------------------------------------------------
class Matrix:
    def __init__(self, *matrix):
        # Check if not empty
        if len(matrix) == 0:
            raise ValueError("Matrix must have at least one element.")
        # reset Matrx if there is only one element inside the matrix
        if len(matrix) == 1 and isinstance(matrix[0][0], (list, tuple)):
            matrix = matrix[0]
        # Check if rows are iteratable
        try:
            for row in matrix:
                # Check if rows are lists or tuples
                if not isinstance(row, (list, tuple)):
                    raise ValueError(
                        f"Matrix must contain list/tuples not {type(row)}")
                iter_check = iter(row)
                # Confirm that elements are numbers.
                for element in iter_check:
                    if not isinstance(element, (int, float, complex)):
                        raise ValueError(
                            f"Matrix must contain only numbers not {type(element)}"
                        )
        except TypeError:
            raise TypeError("Matrix arguement should be iteratable.")
        # Check if number of elements in each row is the same.
        no_of_cols = len(matrix[0])
        no_of_rows = 0
        for row in matrix:
            no_of_rows += 1
            if len(row) != no_of_cols:
                raise ValueError(
                    "The number of elements in the matrix should be equal."
                )
        # Initialize variables
        self.matrix = [list(row) for row in matrix]
        self.rows = no_of_rows   # Number of rows
        self.cols = no_of_cols   # Number of columns
        self._index = 0          # Used for iterating over the matrix

    def __len__(self):
        return self.rows

    def __iter__(self):
        """Returns an iterator over the elements of the matrix."""
        return iter(self.matrix)

    def __next__(self):
        """Returns the next element of the matrix."""
        if self._index < len(self.matrix):
            self._index += 1
            return self.matrix[self._index - 1]
        raise StopIteration

    def __getitem__(self, key):
        """Returns the element at the specified key"""
        return self.matrix[key]

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

    def __add__(self, anotherObj):
        """Returns the sum of the matrices."""
        if self.order() == anotherObj.order():
            matrix = []
            for i in range(self.rows):
                temp = []
                for j in range(self.cols):
                    temp.append(self.matrix[i][j] + anotherObj[i][j])
                matrix.append(temp)
            return Matrix(matrix)
        raise ValueError("The 2 matrices do not have the same order.")

    def __sub__(self, anotherObj):
        """Returns the difference of the matrices"""
        if self.order() == anotherObj.order():
            matrix = []
            for i in range(self.rows):
                temp = []
                for j in range(self.cols):
                    temp.append(self.matrix[i][j] - anotherObj[i][j])
                matrix.append(temp)
            return Matrix(matrix)
        raise ValueError("The 2 matrices do not have the same order.")

    def __mul__(self, anotherObj):
        """Returns the product of a matrix and a nuber/matrix."""
        if isinstance(anotherObj, [int, float]):  # Scalar multiplication
            prod = []
            for row in self.matrix:
                new_row = [(element * anotherObj) for element in row]
                prod.append(new_row)
            return Matrix(prod)
        elif isinstance(anotherObj, Matrix):
            matrix = []
            for i in range(self.rows):
                temp = []
                for j in range(self.cols):
                    temp.append(self.matrix[i][j] * anotherObj[i][j])
                matrix.append(temp)
            return matrix
        raise TypeError(
            f"Mutiplication not supported between type Matrix and type {type(anotherObj)}."
        )

    def __rmul__(self, otherObj):
        """Returns the product of a matrix and a nuber/matrix."""
        return self * otherObj

    def __matmul__(self, anotherObj):
        """Returns the cross product of two matrices."""
        if isinstance(anotherObj, Matrix):  # Matrix multiplication
            arr = []
            length = self.rows
            for i in range(length):
                arr.append([])
                for j in range(length):
                    total = 0
                    for k in range(length):
                        total += self.matrix[i][k] * anotherObj.matrix[k][j]
                    arr[i].append(total)
            return Matrix(arr)

    def __pow__(self, power=2):
        """Returns the matrix representing the n^th power of matrix A, if mathematically possible."""
        if self.cols == self.rows:
            if isinstance(power, int) and int > 0:
                matrix = self.matrix
                for _ in range(power - 1):
                    matrix = matrix * self.matrix
                return matrix
            elif power == 0:
                matrix = identity(self.rows)
                return Matrix(matrix)
            raise ValueError(
                "The power of the matrix must be a natural number")
        raise ValueError("The given matrix is not a square matrix.")

    def adjoint(self):
        """Returns the adjoint representation of the matrix.

        Returns
        -------
        matrix :
            The adjoint representation of the matrix.
        """
        matrix = []
        for i in range(self.rows):
            temp = []
            for j in range(self.cols):
                temp.append(self.cofactor(i, j))
            matrix.append(temp)
        return Matrix(matrix).transpose()

    def cofactor(self, i, j):
        """Returns the cofactor representation of the matrix.

        Args
        ----
        i : integer
            The index of the row of the matrix.
        j : integer
            The index of the column of the matrix.

        Returns
        -------
        cofactor : integer
            The cofactor representation of the matrix.
        """
        return (-1) ** (i + j) * self.minor(i, j)

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

        Args
        ----
        i (int, optional)
            The row to be removed. Starts from 0.
        j (int, optional)
            The column to be removed. Starts from 0.

        Returns
        -------
        Matrix
            The matrix after removing the i th row and/or j th column.

        Raises
        ------
        ValueError
            Raised if the row or column to be removed is not a natural number.
        """
        # if both i and j are None
        if i is None and j is None:
            return self
        # if i is not None and j is None
        elif all([i is not None, i >= 0, i < self.rows, j is None]):
            matrix = []
            for k in range(self.rows):
                if k != i:
                    matrix.append(self.matrix[k])
            return Matrix(matrix)
        # if i is None and j is not None
        elif all([j is not None, j >= 0, j < self.cols, i is None]):
            matrix = []
            for k in range(self.rows):
                temp = []
                for l in range(self.cols):
                    if l != j:
                        temp.append(self.matrix[k][l])
                matrix.append(temp)
            return Matrix(matrix)
        # if both i and j are not None
        elif all(
                [i is not None, j is not None, i >= 0,
                 i < self.rows, j >= 0, j < self.cols]):
            matrix = []
            for k in range(self.rows):
                if k != i:
                    temp = []
                    for l in range(self.cols):
                        if l != j:
                            temp.append(self.matrix[k][l])
                    matrix.append(temp)
            return Matrix(matrix)
        raise ValueError(
            "The row or column to be removed is not a natural number.")

    def determinant(self):
        """Returns the determinant of this matrix.

        Returns
        -------
        determinant : float
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
        inv : Matrix
            The inverse of this matrix
        """
        if self.is_square():
            determinant = self.determinant()
            if determinant == 0:
                raise ValueError("The given matrix is not invertible.")
            return (self.adjoint() / determinant).transpose()
        raise ValueError("The given matrix is not a square matrix.")

    def is_diagonal(self):
        """Returns True if the matrix is diagonal, False otherwise."""
        if self.cols == self.rows:
            for i in range(self.rows):
                for j in range(self.cols):
                    if i != j and self.matrix[i][j] != 0:
                        return False
            return True
        return False

    def is_identity(self):
        """Returns True if the matrix is identity, False otherwise"""
        for i in range(self.rows):
            for j in range(self.cols):
                if i == j and self.matrix[i][j] != 1:
                    return False
                elif i != j and self.matrix[i][j] != 0:
                    return False
        return True

    def is_invertible(self):
        """Returns True if the matrix is invertible, False otherwise."""
        return self.det() != 0

    def is_lower_triangular(self):
        """Returns True if the matrix is lower triangular, False otherwise."""
        if self.cols == self.rows:
            for i in range(self.rows):
                for j in range(i + 1, self.cols):
                    if self.matrix[i][j] != 0:
                        return False
            return True
        return False

    def is_null(self):
        """Returns True if the matrix is null, False otherwise."""
        for row in self.matrix:
            for item in row:
                if item != 0:
                    return False
        return True

    def is_skew_symmetric(self):
        """Returns True if the matrix is skew-symmetric, False otherwise."""
        if self.cols == self.rows:
            for i in range(self.rows):
                for j in range(i, self.cols):
                    if self.matrix[i][j] != -self.matrix[j][i]:
                        return False
            return True
        return False

    def is_square(self):
        """Returns True if the matrix is square, False otherwise."""
        return self.cols == self.rows

    def is_symmetric(self):
        """Returns True if the matrix is symmetric, False otherwise."""
        if self.cols == self.rows:
            for i in range(self.rows):
                for j in range(i, self.cols):
                    if self.matrix[i][j] != self.matrix[j][i]:
                        return False
            return True
        return False

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

        Args
        ----
        i (int, optional)
            The row of the element. Starts from 0.
        j (int, optional)
            The column of the element. Starts from 0.

        Returns
        -------
        Matrix
            The minor of the matrix A.

        Raises
        ------
        ValueError
            Raised if the row or column to be removed is not a natural number.
        """
        return self.cut(i, j).determinant()

    def order(self):
        """Returns the order of the matrix.

        Returns
        -------
        order: tuple
            The order of the matrix.
        """
        return self.rows, self.cols

    def rotate(self, turns=1):
        """Returns the matrix after n rotations.

        Args
        ----
        turns (int, optional)
            The number of turns to rotate the matrix in clockwise direction. Defaults to 1.

        Returns
        -------
        rotated: Matrix
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
        total: int/float/complex
            The trace of the matrix.
        """
        if self.is_square():
            total = 0
            for i in range(self.rows):
                total += self.matrix[i][i]
            return Matrix(total)
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

    # Alias
    adj = adjoint
    det = determinant
    inv = inverse
    is_diagonal_dominant = is_diagonal
    is_upper_hessenberg = is_upper_triangular
    is_lower_hessenberg = is_lower_triangular
