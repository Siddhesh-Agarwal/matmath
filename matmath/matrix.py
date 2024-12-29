"""A module for matrix operations."""

from typing import Any, Iterator, List, Tuple, Union


number = Union[int, float]


class Matrix:
    """A class to represent a matrix."""

    def __init__(self, mat: List[List[number]]):
        self.matrix: List[List[number]] = []
        self.rows: int = 0
        self.cols: int = 0
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])
        for i, row in enumerate(mat):
            if len(row) != self.cols:
                raise ValueError("The matrix is not a proper matrix.")
            mat[i] = list(row)
        self.matrix = list(mat)

    def __len__(self) -> int:
        """Returns the number of rows in the matrix"""
        return self.rows

    def __iter__(self) -> Iterator[List[number]]:
        """Returns an iterator over the elements of the matrix"""
        return iter(self.matrix)

    def __getitem__(self, r: int) -> List[number]:
        """Returns the element at the specified key"""
        return self.matrix[r]

    def __str__(self):
        """Returns a string representation of the matrix"""
        length = self.rows
        string = ["| "] * length
        for i in range(len(self.matrix[0])):
            temp: List[str] = []
            helper = 0
            for j in range(length):
                element = str(self.matrix[j][i])
                temp.append(element)
                if len(element) > helper:
                    helper = len(element)
            for j in range(length):
                string[j] += temp[j] + " " * (helper - len(temp[j]) + 1)
        return "|\n".join(string) + "|"

    def __repr__(self) -> str:
        sep = ",\n" + " " * 7
        return f"Matrix({sep.join(list(map(lambda x: str(x)[1:-1], self.matrix)))})"

    def __eq__(self, other: Any) -> bool:
        """Checks if the matrix is equal to another matrix"""
        if not isinstance(other, self.__class__):
            return False
        return self.matrix == other.matrix

    def __ne__(self, other: Any) -> bool:
        """Checks if the matrix is not equal to another matrix"""
        return not (self == other)

    def __add__(self, other: "Matrix") -> "Matrix":
        """Returns the sum of the matrices"""
        if self.order == other.order:
            matrix: List[List[number]] = []
            for i in range(self.rows):
                temp = [self.matrix[i][j] + other[i][j] for j in range(self.cols)]
                matrix.append(temp)
            return Matrix(matrix)
        raise ValueError("The 2 matrices do not have the same order.")

    def __sub__(self, other: "Matrix") -> "Matrix":
        """Returns the difference of the matrices"""
        if self.order == other.order:
            matrix: List[List[number]] = []
            for i in range(self.rows):
                matrix.append(
                    [self.matrix[i][j] - other[i][j] for j in range(self.cols)]
                )
            return Matrix(matrix)
        raise ValueError("The 2 matrices do not have the same order.")

    def __mul__(self, other: Union["Matrix", int, float]) -> "Matrix":
        """Returns the product of a matrix and a number/matrix"""
        if isinstance(other, (int, float)):  # Scalar multiplication
            result = [[(element * other) for element in row] for row in self.matrix]
            return Matrix(result)
        if isinstance(other, self.__class__):
            if self.cols == other.cols and self.rows == other.rows:
                result: List[List[number]] = []
                for i in range(self.rows):
                    temp = [self.matrix[i][j] * other[i][j] for j in range(self.cols)]
                    result.append(temp)
                return Matrix(result)
            raise ValueError("The 2 matrices do not have the same order.")
        raise TypeError(
            f"Multiplication not supported between {type(self)} and {type(other)}."
        )

    def __imul__(self, other: Union["Matrix", int, float]) -> "Matrix":
        if isinstance(other, (int, float)):
            return self * other
        return other * self

    def __truediv__(self, other: Union["Matrix", int, float]) -> "Matrix":
        """Returns the division of a matrix and a number/matrix"""
        if isinstance(other, (int, float)):
            result: List[List[number]] = []
            for row in self.matrix:
                new_row = [(element * other) for element in row]
                result.append(new_row)
            return Matrix(result)
        if isinstance(other, self.__class__):
            if self.cols == other.cols and self.rows == other.rows:
                result: List[List[number]] = []
                for i in range(self.rows):
                    temp = [self.matrix[i][j] / other[i][j] for j in range(self.cols)]
                    result.append(temp)
                return Matrix(result)
            raise ValueError("The 2 matrices do not have the same order.")
        raise TypeError(
            f"Division not supported between {type(self)} and {type(other)}."
        )

    def __floordiv__(self, other: Union["Matrix", int, float]) -> "Matrix":
        """Returns the quotient of a matrix and a number/matrix"""
        if isinstance(other, (int, float)):
            result: List[List[number]] = []
            for row in self.matrix:
                new_row = [(element // other) for element in row]
                result.append(new_row)
            return Matrix(result)
        if isinstance(other, self.__class__):
            if self.cols == other.cols and self.rows == other.rows:
                result = []
                for i in range(self.rows):
                    temp = [self.matrix[i][j] // other[i][j] for j in range(self.cols)]
                    result.append(temp)
                return Matrix(result)
            raise ValueError("The 2 matrices do not have the same order.")
        raise TypeError(
            f"Multiplication not supported between {type(self)} and {type(other)}."
        )

    def __matmul__(self, other: "Matrix"):
        """Returns the cross product of two matrices"""
        if not isinstance(other, self.__class__):
            raise ValueError(f"Passed object is not of {type(self)}")
        arr: list[list[number]] = [[0] * other.cols] * self.rows
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(other.rows):
                    arr[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return Matrix(arr)

    def pow(self, power: int = 2) -> "Matrix":
        """Returns the n^th power of the matrix, if mathematically possible."""
        if self.cols == self.rows:
            if power > 0:
                matrix = self.copy()
                for _ in range(power - 1):
                    matrix = matrix * self
                return matrix
            elif power == 0:
                return self.identity(self.rows)
            raise ValueError("The power of the matrix must be a natural number")
        raise ValueError("The given matrix is not a square matrix.")

    def identity(self, n: int = 3) -> "Matrix":
        """
        identity _summary_

        Parameters
        ----------
        n : int
            The order of the identity matrix. defaults to 3.
        """
        matrix: List[List[number]] = [[0] * n] * n
        for i in range(n):
            matrix[i][i] = 1
        return Matrix(matrix)

    def zero(self, order: Tuple[int, int]) -> "Matrix":
        """Returns a zero matrix of the given order."""

        r, c = order
        matrix: List[List[number]] = [[0] * c] * r
        return Matrix(matrix)

    def fill(self, value: int, order: Tuple[int, int]) -> "Matrix":
        """Returns a matrix of the given order filled with the given value."""

        r, c = order
        self.matrix = [[value] * c] * r
        return Matrix(self.matrix)

    def adjoint(self) -> "Matrix":
        """Returns the adjoint representation of the matrix.

        Returns
        -------
        Matrix :
            The adjoint representation of the matrix.
        """
        matrix: List[List[number]] = []
        for i in range(self.rows):
            temp = [self.cofactor(i, j) for j in range(self.cols)]
            matrix.append(temp)
        return Matrix(matrix).transpose()

    def cofactor(self, i: int, j: int) -> float:
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

    def copy(self) -> "Matrix":
        """Returns a shallow copy of this matrix.

        Returns
        -------
        a copy of this matrix
        """
        new_matrix = self.matrix.copy()
        return Matrix(new_matrix)

    def cut(self, i: Union[int, None] = None, j: Union[int, None] = None) -> "Matrix":
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
            return self.copy()
        matrix: List[List[number]] = []
        if i is not None:
            if i < 0 or i >= self.rows:
                raise ValueError("The row to be removed is not present in the matrix.")
            for row in self.matrix:
                matrix.append(row.copy())
            matrix.pop(i)
        if j is not None:
            if j < 0 or j >= self.cols:
                raise ValueError(
                    "The column to be removed is not present in the matrix."
                )
            for i, row in enumerate(matrix):
                matrix[i] = row[:j] + row[j + 1 :]
        return Matrix(matrix)

    def determinant(self) -> number:
        """Returns the determinant of this matrix.

        Returns
        -------
        float :
            The determinant of this matrix.
        """
        if self.is_square():
            determinant = 1
            mat = self.matrix
            for i in range(self.rows):
                for j in range(i + 1, self.rows):
                    if mat[i][i] == 0:
                        mat[i][i] = 1
                    x = mat[j][i] / mat[i][i]
                    for k in range(self.rows):
                        mat[j][k] -= x * mat[i][k]
            for i in range(self.rows):
                determinant *= mat[i][i]
            return determinant
        raise ValueError("The given matrix is not a square matrix.")

    def inverse(self) -> "Matrix":
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
            temp = self.adjoint() / determinant
            return temp.transpose()
        raise ValueError("The given matrix is not a square matrix.")

    def is_diagonal(self) -> bool:
        """Returns True if the matrix is diagonal, False otherwise."""
        if self.cols == self.rows:
            for i in range(self.rows):
                for j in range(self.cols):
                    if i != j and self.matrix[i][j] != 0:
                        return False
            return True
        return False

    def is_identity(self) -> bool:
        """Returns True if the matrix is identity, False otherwise"""
        if self.rows != self.cols:
            return False
        return self == self.identity(self.rows)

    def is_invertible(self) -> bool:
        """Returns True if the matrix is invertible, False otherwise."""
        return self.det() != 0

    def is_lower_triangular(self) -> bool:
        """Returns True if the matrix is lower triangular, False otherwise."""
        if self.cols != self.rows:
            return False
        for i in range(self.rows):
            for j in range(i + 1, self.cols):
                if self.matrix[i][j] != 0:
                    return False
        return True

    def is_null(self) -> bool:
        """Returns True if the matrix is null, False otherwise."""
        return self == self.zero((self.rows, self.cols))

    def is_skew_symmetric(self) -> bool:
        """Returns True if the matrix is skew-symmetric, False otherwise."""
        if self.cols != self.rows:
            return False
        for i in range(self.rows):
            for j in range(i, self.cols):
                if self.matrix[i][j] != -self.matrix[j][i]:
                    return False
        return True

    def is_square(self) -> bool:
        """Returns True if the matrix is square, False otherwise."""
        return self.cols == self.rows

    def is_symmetric(self) -> bool:
        """Returns True if the matrix is symmetric, False otherwise."""
        if self.cols != self.rows:
            return False
        for i in range(self.rows):
            for j in range(i, self.cols):
                if self.matrix[i][j] != self.matrix[j][i]:
                    return False
        return True

    def is_upper_triangular(self) -> bool:
        """Returns True if the matrix is upper triangular, False otherwise."""
        if self.cols != self.rows:
            return False
        for i in range(self.rows):
            for j in range(i):
                if self.matrix[i][j] != 0:
                    return False
        return True

    def minor(self, i: int = 0, j: int = 0) -> number:
        """Returns the minor of the Aij element in matrix A.

        Parameters
        ----------
        i (int, optional)
            The row of the element. Defaults to 0.
        j (int, optional)
            The column of the element. Defaults to 0.

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

    def rotate(self, turns: int = 1) -> "Matrix":
        """Returns the matrix after n rotations.

        Parameters
        turns (int, optional)
            The number of turns to rotate the matrix in clockwise direction.
            Defaults to 1.

        Returns
        -------
        Matrix :
            The matrix after n rotations.
        """
        turns = turns % 4
        if turns == 0:
            return Matrix(self.matrix)
        elif turns == 2:
            rotated = [row[::-1] for row in self.matrix][::-1]
            return Matrix(rotated)
        else:
            rotated = self.matrix
            for _ in range(turns):
                rotated = self.__rotate(rotated)
            return Matrix(rotated)

    def __rotate(self, mat: List[List[number]]):
        rotated: List[List[number]] = [[0] * len(mat)] * len(mat[0])
        for i, row in enumerate(mat):
            for j, element in enumerate(row):
                rotated[j][len(mat) - i - 1] = element
        return rotated

    def trace(self) -> number:
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

    def transpose(self) -> "Matrix":
        """Transposes the given matrix.

        Returns
        -------
        arr: Matrix
            The transposed matrix.
        """
        arr = [[self.matrix[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return Matrix(arr)

    def to_list(self) -> List[List[number]]:
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
    size = order
